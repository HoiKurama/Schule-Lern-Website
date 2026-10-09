# -*- coding: utf-8 -*-
"""Generischer Modulcheck fuer die Lernseiten (Playwright, Python).

    python modulcheck.py "module/DATEI.html" [shots]

Ausgabe ist JSON mit "blocker" (Modul gilt nicht als fertig) und "maengel". Mit dem zweiten
Argument entstehen dort Bildschirmfotos und beide Druckfassungen als PDF.
Die Pruefschritte fuer Formelleiste und Druckmodi liegen in pruefschritte/.
"""
import sys, os, json, re
from playwright.sync_api import sync_playwright
from pruefschritte import browser_starten, formelleiste_pruefen, druckmodi_pruefen

# Unter Windows ist stdout in einer Pipe cp1252; Befunde mit Φ oder → braeche das JSON sonst ab.
sys.stdout.reconfigure(encoding="utf-8")

DATEI = sys.argv[1]
SHOTS = sys.argv[2] if len(sys.argv) > 2 else None
URL = "file:///" + os.path.abspath(DATEI).replace("\\", "/")
blocker, maengel, notiz = [], [], {}
def B(t): blocker.append(t)
def M(t): maengel.append(t)

# Steuerzeichen im Quelltext entstehen, wenn ein Skript "\a" oder "\f" ohne Raw-String schreibt;
# KaTeX zeigt dann roten Rohtext statt der Formel. Das faellt auch ohne Netz auf.
with open(DATEI, encoding="utf-8") as f:
    for nr, zeile in enumerate(f, 1):
        treffer = re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", zeile)
        if treffer:
            B("Steuerzeichen %s in Zeile %d: %s" % (repr(treffer[0]), nr, zeile.strip()[:90]))

JS_KATEX = r"""() => { const alle = [...document.querySelectorAll('.m')];
  const roh = alle.filter(m => !m.querySelector('.katex, .katex-error'));
  return {da: typeof katex !== 'undefined', gesamt: alle.length, roh: roh.length,
          bsp: roh.slice(0, 3).map(m => m.getAttribute('data-plain')),
          fehler: [...document.querySelectorAll('.katex-error')].map(e => e.getAttribute('title') || e.textContent).slice(0, 5),
          n: document.querySelectorAll('.katex-error').length}; }"""

JS_VERTRAEGE = r"""() => {
  const out = {mc:[], num:[], zuo:0, hilfen:0, loesungen:0, formeln:0, ohnePlain:0,
               tabellenOhneWrapper:0, schluessel:[]};
  const mcD = (typeof mcDaten !== "undefined") ? mcDaten : {};
  const nuD = (typeof numDaten !== "undefined") ? numDaten : {};
  document.querySelectorAll("[data-mc]").forEach(a => {
    const k = a.getAttribute("data-mc");
    const opts = [...a.querySelectorAll(".opt")];
    const idx = opts.map(o => o.getAttribute("data-i"));
    const namen = [...new Set([...a.querySelectorAll("input[type=radio]")].map(r => r.name))];
    out.mc.push({k, n:opts.length, fb:(mcD[k]&&mcD[k].fb)?mcD[k].fb.length:null,
                 r:(mcD[k]?mcD[k].r:null), idx, namen, hatDaten:!!mcD[k]});
    out.schluessel.push(k);
  });
  document.querySelectorAll("[data-num]").forEach(a => {
    const k = a.getAttribute("data-num"); const d = nuD[k] || null;
    const einheiten = [...a.querySelectorAll(".eingabe select option")]
                        .map(o => o.value).filter(v => v);
    const hatFeld = !!a.querySelector(".eingabe input[type=number]");
    out.num.push({k, hatFeld, hatDaten:!!d, wert:d?d.wert:null, einheit:d?d.einheit:null,
                  tol:d?d.tol:null, alt:(d&&d.alt)?d.alt:null, einheiten,
                  texte:d?["ok","falschEinheit","nah","weit"].filter(x=>!d[x]):null});
    out.schluessel.push(k);
  });
  out.zuo = document.querySelectorAll('[data-check="zuordnung"]').length;
  out.hilfen = document.querySelectorAll("[data-hilfe]").length;
  out.loesungen = document.querySelectorAll("[data-loesung]").length
                - document.querySelectorAll(".zeile[data-loesung]").length;
  document.querySelectorAll(".m").forEach(m => {
    out.formeln++;
    const p = m.getAttribute("data-plain");
    if (!p || !p.trim()) out.ohnePlain++;
  });
  document.querySelectorAll("table").forEach(t => {
    if (!t.closest(".tabelle")) out.tabellenOhneWrapper++;
  });
  return out;
}"""

JS_HILFEN = r"""() => {
  const schlecht = [];
  document.querySelectorAll("[data-hilfe]").forEach(b => {
    b.click();
    const box = b.closest(".aufgabe") || document.body;
    const stufe = b.getAttribute("data-hilfe");
    const t = box.querySelector('.hilfe-text[data-stufe="' + stufe + '"]');
    if (!t) { schlecht.push("Stufe " + stufe + " ohne Textblock"); return; }
    if (getComputedStyle(t).display === "none")
      schlecht.push("Stufe " + stufe + " bleibt nach Klick verborgen");
    if (t.innerText.trim().length < 20)
      schlecht.push("Hilfetext Stufe " + stufe + " zu kurz");
  });
  document.querySelectorAll("[data-loesung]").forEach(b => {
    if (b.classList.contains("zeile")) return;
    b.click();
    const box = b.closest(".aufgabe") || document.body;
    const t = box.querySelector('.hilfe-text[data-stufe="9"]');
    if (!t || getComputedStyle(t).display === "none")
      schlecht.push("Musterloesung '" + b.getAttribute("data-loesung") + "' oeffnet nicht");
  });
  return schlecht;
}"""

JS_REGLER = r"""() => {
  const r = [];
  document.querySelectorAll('input[type=range]').forEach(s => {
    const mi = +s.min, ma = +s.max, st = +s.step || 1, n = 14;
    for (let i = 0; i <= n; i++) {
      const v = mi + (ma - mi) * i / n;
      s.value = String(Math.round(v / st) * st);
      s.dispatchEvent(new Event("input", {bubbles:true}));
      s.dispatchEvent(new Event("change", {bubbles:true}));
    }
    r.push({id:s.id, min:mi, max:ma, step:st, ende:s.value});
  });
  return r;
}"""

JS_ANZEIGE = r"""() => {
  const b = [];
  document.querySelectorAll(".anzeige span, .anzeige div").forEach(e => {
    const t = e.textContent || "";
    if (/NaN|Infinity|undefined/.test(t)) b.push("unbrauchbarer Wert: " + t.slice(0, 40));
    if (/[0-9]\.[0-9]/.test(t)) b.push("Punkt statt Komma: " + t.slice(0, 40));
  });
  return b;
}"""

JS_DRUCK = r"""() => {
  const sicht = e => getComputedStyle(e).display !== "none";
  return {
    bedienelemente: [...document.querySelectorAll(".steuer,.knopfleiste,.hilfen")].filter(sicht).length,
    lehrer: [...document.querySelectorAll(".lehrer")].filter(sicht).length,
    aufgaben: [...document.querySelectorAll(".aufgabe")].filter(sicht).length,
    aufgabenGesamt: document.querySelectorAll(".aufgabe").length
  };
}"""

JS_OFFLINE = r"""() => {
  let leer = 0, bsp = null;
  document.querySelectorAll(".m").forEach(m => {
    const t = (m.textContent || "").trim();
    if (!t) { leer++; if (!bsp) bsp = m.getAttribute("data-plain"); }
  });
  return {leer, bsp, gesamt: document.querySelectorAll(".m").length};
}"""

def rueck_zuordnung(pg):
    return pg.evaluate(r"""() => {
      const b = document.querySelector('[data-check="zuordnung"]');
      if (!b) return null;
      const box = b.closest(".aufgabe");
      const r = box ? box.querySelector(".rueck") : null;
      return r ? {t:r.innerText.trim(), c:r.className} : null;
    }""")

def pruefen(p):
    br, notiz["browser"] = browser_starten(p)
    ctx = br.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    kons, pfehler = [], []
    pg.on("console", lambda m: kons.append((m.type, m.text)) if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: pfehler.append(str(e)))
    # Echtes KaTeX: throwOnError:false setzt Parsefehler still als rote .katex-error. Kommt das CDN
    # erst nach dem 1,5-s-Rueckfall der Seite, bleiben Formeln roh; dann gilt der Lauf nicht und
    # die Seite wird neu geladen.
    for versuch in range(3):
        kons.clear(); pfehler.clear()
        if versuch:
            pg.reload(wait_until="load")
        else:
            pg.goto(URL, wait_until="load")
        pg.wait_for_timeout(1500)
        kx = pg.evaluate(JS_KATEX)
        if not kx["da"] or not kx["roh"]:
            break

    for e in pfehler:
        B("pageerror beim Laden: " + e)
    for t, m in kons:
        (B if t == "error" else M)("Konsole %s: %s" % (t, m[:200]))
    stand = len(pfehler)

    if not kx["da"]:
        M("KaTeX nicht geladen (kein Netz?) - Formeln mit echtem KaTeX ungeprueft")
    elif kx["roh"]:
        B("KaTeX-Pruefung ungueltig: %d von %d Formeln nach drei Ladeversuchen ungesetzt, z.B. %s"
          % (kx["roh"], kx["gesamt"], kx["bsp"][:1]))
    elif kx["n"]:
        B("%d KaTeX-Fehler (.katex-error), z.B. %s" % (kx["n"], kx["fehler"][0][:150]))
    notiz["katex_fehler"] = kx["n"] if kx["da"] else None
    notiz["katex_gesetzt"] = "%d von %d" % (kx["gesamt"] - kx["roh"], kx["gesamt"]) if kx["da"] else None

    v = pg.evaluate(JS_VERTRAEGE)
    notiz["zaehlung"] = {"mc": len(v["mc"]), "num": len(v["num"]), "zuordnung": v["zuo"],
                         "hilfeknoepfe": v["hilfen"], "musterloesungen": v["loesungen"],
                         "formeln": v["formeln"]}
    if v["ohnePlain"]:
        B("%d Formeln ohne data-plain" % v["ohnePlain"])
    if v["tabellenOhneWrapper"]:
        M('%d <table> ohne <div class="tabelle">-Wrapper' % v["tabellenOhneWrapper"])
    if v["zuo"] > 1:
        B("mehr als eine Zuordnungsaufgabe, die Engine kennt nur eine")

    for a in v["mc"]:
        if not a["hatDaten"]:
            B("MC '%s' fehlt in mcDaten" % a["k"]); continue
        if a["fb"] != a["n"]:
            B("MC '%s': %d Optionen, aber %s Feedbacktexte" % (a["k"], a["n"], a["fb"]))
        if a["idx"] != [str(i) for i in range(a["n"])]:
            B("MC '%s': data-i ist %s, erwartet 0..%d" % (a["k"], a["idx"], a["n"] - 1))
        if a["namen"] != [a["k"]]:
            B("MC '%s': radio-name %s, muss '%s' sein" % (a["k"], a["namen"], a["k"]))
        if a["r"] is None or not (0 <= a["r"] < a["n"]):
            B("MC '%s': r=%s ausserhalb der Optionen" % (a["k"], a["r"]))
    for a in v["num"]:
        if not a["hatFeld"]:
            continue                      # data-num nur als Export-Schluessel
        if not a["hatDaten"]:
            B("Zahleneingabe '%s' fehlt in numDaten" % a["k"]); continue
        if a["texte"]:
            B("Zahleneingabe '%s': Rueckmeldung fehlt fuer %s" % (a["k"], a["texte"]))
        if a["einheit"] not in a["einheiten"]:
            B("Zahleneingabe '%s': Solleinheit '%s' fehlt im Auswahlfeld %s"
              % (a["k"], a["einheit"], a["einheiten"]))
        if len(a["einheiten"]) < 2:
            M("Zahleneingabe '%s': keine Distraktor-Einheit" % a["k"])

    for a in v["mc"]:
        for i in range(a["n"]):
            sel = '[data-mc="%s"]' % a["k"]
            pg.click('%s .opt[data-i="%d"] input' % (sel, i))
            pg.wait_for_timeout(50)
            txt = pg.inner_text(sel + " .rueck").strip()
            kl = pg.get_attribute(sel + " .rueck", "class") or ""
            if not txt:
                B("MC '%s' Option %d: keine Rueckmeldung" % (a["k"], i))
            elif len(txt) < 25:
                M("MC '%s' Option %d: Rueckmeldung nur %d Zeichen" % (a["k"], i, len(txt)))
            soll = "ok" if i == a["r"] else "nein"
            if soll not in kl.split():
                B("MC '%s' Option %d: Wertung '%s', erwartet '%s'" % (a["k"], i, kl.strip(), soll))

    for a in v["num"]:
        if not (a["hatFeld"] and a["hatDaten"]):
            continue
        sel = '[data-num="%s"]' % a["k"]
        altE = a["alt"].get("einheit") if a["alt"] else None
        falsche = [e for e in a["einheiten"] if e != a["einheit"] and e != altE]
        w, tol = a["wert"], (a["tol"] or 0.0)
        faelle = [("richtig", w, a["einheit"], "ok"),
                  ("knapp daneben", w * 1.3 + tol * 4 + 0.001, a["einheit"], "nein"),
                  ("weit daneben", w * 6.0 + 7.0, a["einheit"], "nein")]
        if falsche:
            faelle.append(("falsche Einheit", w, falsche[0], "nein"))
        if a["alt"]:
            faelle.append(("Alternativeinheit", a["alt"]["wert"], a["alt"]["einheit"], "ok"))
        for name, zahl, einh, soll in faelle:
            pg.fill(sel + " input[type=number]", "")
            pg.fill(sel + " input[type=number]", repr(zahl))
            pg.select_option(sel + " select", einh)
            pg.click(sel + " .eingabe button")
            pg.wait_for_timeout(50)
            kl = pg.get_attribute(sel + " .rueck", "class") or ""
            txt = pg.inner_text(sel + " .rueck").strip()
            if not txt:
                B("Zahleneingabe '%s' Fall '%s': keine Rueckmeldung" % (a["k"], name))
            if soll not in kl.split():
                B("Zahleneingabe '%s' Fall '%s' (%r %s): Wertung '%s', erwartet '%s'"
                  % (a["k"], name, zahl, einh, kl.strip(), soll))

    if v["zuo"]:
        notiz["zuordnung_zeilen"] = pg.eval_on_selector_all(".zuordnung .zeile", "z => z.length")
        pg.eval_on_selector_all(".zuordnung .zeile", r"""z => z.forEach(r => {
            r.querySelector("select").value = r.getAttribute("data-loesung"); })""")
        pg.click('[data-check="zuordnung"]')
        pg.wait_for_timeout(80)
        rk = rueck_zuordnung(pg)
        if not rk or "ok" not in rk["c"].split():
            B("Zuordnung: die vollstaendig richtige Loesung wird nicht als richtig gewertet (%s)" % (rk,))
        pg.eval_on_selector_all(".zuordnung .zeile", r"""z => z.forEach(r => {
            const s = r.querySelector("select");
            const opt = [...s.options].map(o => o.value).filter(x => x);
            s.value = opt.find(x => x !== r.getAttribute("data-loesung")) || opt[0]; })""")
        pg.click('[data-check="zuordnung"]')
        pg.wait_for_timeout(80)
        rk2 = rueck_zuordnung(pg)
        if rk2 and "ok" in rk2["c"].split():
            B("Zuordnung: eine falsche Loesung wird als richtig gewertet")

    for s in pg.evaluate(JS_HILFEN):
        B("Hilfesystem: " + s)

    notiz["regler"] = pg.evaluate(JS_REGLER)
    pg.wait_for_timeout(300)
    for s in sorted(set(pg.evaluate(JS_ANZEIGE))):
        B("Anzeige nach dem Reglerlauf: " + s)
    for e in pfehler[stand:]:
        B("pageerror bei der Bedienung: " + e)
    stand = len(pfehler)

    ctx.grant_permissions(["clipboard-read", "clipboard-write"])
    pg.click("#bExport")
    pg.wait_for_timeout(400)
    notiz["export"] = pg.inner_text("#exportInfo").strip()
    if not notiz["export"]:
        B("Export: keine Rueckmeldung nach Klick auf #bExport")

    pg.emulate_media(media="print")
    pg.wait_for_timeout(250)
    dr = pg.evaluate(JS_DRUCK)
    if dr["bedienelemente"]:
        B("Druckansicht zeigt %d Bedienelemente" % dr["bedienelemente"])
    if dr["lehrer"]:
        B("Druckansicht zeigt den Lehrerteil")
    if dr["aufgaben"] != dr["aufgabenGesamt"]:
        B("Druckansicht zeigt nur %d von %d Aufgaben" % (dr["aufgaben"], dr["aufgabenGesamt"]))
    notiz["druck"] = dr
    pg.emulate_media(media="screen")

    scroll = {}
    for w in (1280, 900, 390):
        pg.set_viewport_size({"width": w, "height": 900})
        pg.wait_for_timeout(300)
        ue = pg.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
        scroll[str(w)] = ue
        if ue > 0:
            B("Querscrollen bei %d px: %d px Ueberlauf" % (w, ue))
        if SHOTS:
            os.makedirs(SHOTS, exist_ok=True)
            name = os.path.basename(DATEI)[:-5]
            pg.screenshot(path=os.path.join(SHOTS, "%s-%d.png" % (name, w)), full_page=(w == 390))
    notiz["querscrollen"] = scroll
    for e in pfehler[stand:]:
        B("pageerror beim Umschalten der Breite: " + e)
    ctx.close()

    ctx2 = br.new_context(viewport={"width": 1280, "height": 900})
    pg2 = ctx2.new_page()
    pg2.route("**/cdn.jsdelivr.net/**", lambda route: route.abort())
    pf2 = []
    pg2.on("pageerror", lambda e: pf2.append(str(e)))
    pg2.goto(URL, wait_until="load")
    pg2.wait_for_timeout(1400)
    off = pg2.evaluate(JS_OFFLINE)
    if off["leer"]:
        B("Ohne Netz bleiben %d von %d Formeln leer (z.B. '%s')" % (off["leer"], off["gesamt"], off["bsp"]))
    for e in pf2:
        B("pageerror ohne Netz: " + e)
    notiz["offline"] = off
    ctx2.close()

    formelleiste_pruefen(br, URL, B, M, notiz, physik=os.path.basename(DATEI).startswith("physik-"))
    druckmodi_pruefen(br, URL, B, M, notiz, SHOTS, os.path.basename(DATEI)[:-5])
    br.close()


try:
    with sync_playwright() as p:
        pruefen(p)
except Exception as ex:
    # Auch nach einem Abbruch das JSON mit allem ausgeben, was bis dahin gefunden wurde
    B("Modulcheck abgebrochen: " + (str(ex).strip().splitlines() or [type(ex).__name__])[0][:200])

print(json.dumps({"datei": DATEI, "blocker": blocker, "maengel": maengel, "notiz": notiz},
                 ensure_ascii=False, indent=2))
