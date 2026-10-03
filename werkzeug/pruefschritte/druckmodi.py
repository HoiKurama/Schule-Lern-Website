# -*- coding: utf-8 -*-
"""Pruefschritt Druck als Arbeitsblatt und mit Loesungen (vorlage/baustein-druck.md).

Zuerst wird der Bildschirm im Anfangszustand geprueft: keine Loesung, keine Schreiblinie, keine
Formelsammlung sichtbar. Dann wird die Seite absichtlich "bearbeitet": Auswahlaufgaben abwechselnd
richtig und falsch beantwortet, jede Hilfe, Musterloesung und Herleitung aufgeklappt, Zahlen,
Zuordnungen und Text eingetragen. Das Arbeitsblatt darf davon nichts zeigen und keinen Text, der
im Anfangszustand nicht zu sehen war.

Gedruckt wird wie im Browser: Der Knopf ruft window.print(), das hier beforeprint ausloest, das
Druckbild bei A4-Satzbreite (680 px) aufnimmt und afterprint ausloest. Die Formeln laufen ohne
Netz ueber data-plain, damit der Textvergleich mit innerText lueckenlos ist.
"""
import os

A4 = {"width": 680, "height": 900}   # 210 mm minus 2 x 15 mm Rand bei 96 dpi

JS_BEARBEITEN = r"""() => {
  // Auswahlaufgaben abwechselnd richtig und falsch beantworten
  let i = 0;
  document.querySelectorAll("[data-mc]").forEach(b => {
    const d = (typeof mcDaten !== "undefined") ? mcDaten[b.dataset.mc] : null;
    const n = b.querySelectorAll(".opt").length, r = d ? d.r : 0;
    const o = b.querySelector('.opt[data-i="' + ((i++ % 2 === 0) ? r : (r + 1) % Math.max(n, 1)) + '"]');
    if (o) o.click(); });
  document.querySelectorAll("[data-hilfe], .aufgabe [data-loesung]").forEach(k => { if (!k.classList.contains("zeile")) k.click(); });
  document.querySelectorAll(".aufgabe details").forEach(d => { d.open = true; });
  document.querySelectorAll(".eingabe").forEach(e => {
    const i = e.querySelector("input"), s = e.querySelector("select"), k = e.querySelector("button");
    if (i) i.value = "1"; if (s && s.options.length > 1) s.selectedIndex = 1; if (k) k.click(); });
  // Zuordnung abwechselnd richtig und falsch, damit beide Zeilenfarben auf dem Papier landen koennten
  document.querySelectorAll(".zuordnung .zeile select").forEach((s, k) => { const l = s.closest(".zeile").dataset.loesung;
    const anders = [...s.options].map(o => o.value).find(v => v && v !== l);
    s.value = (k % 2 === 0 || !anders) ? l : anders; });
  const z = document.querySelector('[data-check="zuordnung"]'); if (z) z.click();
  document.querySelectorAll("textarea").forEach(t => { t.value = "Meine Antwort"; });
  document.querySelectorAll(".check input").forEach(c => { c.checked = true; });
}"""

JS_PROBEN = r"""() => {
  // Satzstuecke aus allen Loesungstexten, ohne Formeln, mindestens 30 Zeichen lang
  const out = [], nimm = t => String(t || "").replace(/\s+/g, " ").split(/[=·→⁻²³|]/)
    .map(s => s.trim()).filter(s => s.length >= 30).forEach(s => out.push(s.slice(0, 70)));
  document.querySelectorAll(".hilfe-text, .druck-loesung, .nur-loesung").forEach(h => nimm(h.textContent));
  if (typeof mcDaten !== "undefined") Object.values(mcDaten).forEach(d => nimm(d.fb[d.r]));
  if (typeof numDaten !== "undefined") Object.values(numDaten).forEach(d => nimm(d.ok));
  return [...new Set(out)];
}"""

# Sichtbarer Text je Aufgabe, zeilenweise
JS_AUFGABENTEXT = r"""() => [...document.querySelectorAll(".aufgabe")].map(a =>
  (a.innerText || "").split("\n").map(z => z.replace(/\s+/g, " ").trim()).filter(Boolean))"""

JS_BILDSCHIRM = r"""(proben) => {
  const sicht = e => { const c = getComputedStyle(e); return c.display !== "none" && c.visibility !== "hidden" && e.getClientRects().length > 0; };
  const text = document.body.innerText.replace(/\s+/g, " ");
  return {druck: [".druck-loesung", ".schreiblinien", ".formelsammlung", ".hilfe-text"]
            .filter(s => [...document.querySelectorAll(s)].some(sicht)),
          lecks: proben.filter(p => text.includes(p)).slice(0, 3)};
}"""

# Wird im Stub von window.print() aufgerufen, also mit dem Zustand nach beforeprint
JS_DRUCKBILD = r"""(proben) => {
  const sicht = e => { const c = getComputedStyle(e); return c.display !== "none" && c.visibility !== "hidden" && e.getClientRects().length > 0; };
  const zahl = s => [...document.querySelectorAll(s)].filter(sicht).length;
  const r = {klassen: document.body.className};
  r.hilfe = zahl(".hilfe-text"); r.hilfeGesamt = document.querySelectorAll(".hilfe-text").length;
  r.loesung = zahl(".druck-loesung"); r.mc = document.querySelectorAll("[data-mc]").length;
  r.nurLoesung = zahl(".nur-loesung");
  r.rueck = zahl(".rueck"); r.lehrer = zahl(".lehrer"); r.leiste = zahl(".formelleiste, .fl-knopf, .fl-schleier");
  r.aufgaben = zahl(".aufgabe"); r.aufgabenGesamt = document.querySelectorAll(".aufgabe").length;
  r.bedien = [...document.querySelectorAll("input, select, textarea, button")].filter(e => !e.closest(".formelleiste")).filter(sicht)
    .map(e => e.tagName.toLowerCase() + (e.type ? "[" + e.type + "]" : "")).slice(0, 8);
  r.fixiert = [...document.querySelectorAll("body *")].filter(e => getComputedStyle(e).position === "fixed" && sicht(e))
    .map(e => e.className || e.tagName).slice(0, 4);
  const fs = document.querySelector(".formelsammlung");
  r.sammlung = fs && sicht(fs) ? [...fs.querySelectorAll(".fs-zeile")].filter(sicht).length : 0;
  r.formeln = (typeof formelDaten !== "undefined") ? formelDaten.reduce((n, g) => n + g.formeln.length, 0) : 0;
  r.ohneLinien = [...document.querySelectorAll(".aufgabe")].filter(a => a.querySelector("textarea, .eingabe"))
    .filter(a => { const l = a.querySelector(".schreiblinien"); return !l || !sicht(l) || l.getBoundingClientRect().height < 40; })
    .map(a => a.getAttribute("data-num") || a.getAttribute("data-mc") || "?");
  // Alles, woran man die richtige Option erkennen koennte
  const EIG = ["color", "backgroundColor", "backgroundImage", "fontWeight", "fontStyle", "textDecorationLine",
    "borderTopWidth", "borderRightWidth", "borderBottomWidth", "borderLeftWidth", "borderTopColor", "borderRightColor",
    "borderBottomColor", "borderLeftColor", "borderTopStyle", "outlineStyle", "outlineWidth", "boxShadow", "opacity"];
  const sig = o => [o, "::before", "::after"].map((p, i) => { const c = i ? getComputedStyle(o, p) : getComputedStyle(o);
      return EIG.map(k => c[k]).join(",") + (i ? "|" + c.content : ""); }).join("#");
  r.mcGleich = []; r.mcMarkiert = [];
  document.querySelectorAll("[data-mc]").forEach(box => {
    const d = (typeof mcDaten !== "undefined") ? mcDaten[box.dataset.mc] : null; if (!d) return;
    const s = [...box.querySelectorAll(".opt")].map(sig);
    if (new Set(s).size === 1) r.mcGleich.push(box.dataset.mc);
    else if (s.filter((x, i) => i !== d.r && x === s[d.r]).length === 0) r.mcMarkiert.push(box.dataset.mc);
  });
  r.zeilen = [...document.querySelectorAll(".zeile[data-loesung]")].map(z => getComputedStyle(z, "::after").content);
  const zsig = [...document.querySelectorAll(".zuordnung .zeile")].map(z => { const c = getComputedStyle(z);
    return [c.backgroundColor, c.borderTopColor, c.borderLeftColor, c.color].join(","); });
  r.zeilenGleich = new Set(zsig).size <= 1;
  const text = document.body.innerText.replace(/\s+/g, " ");
  r.lecks = proben.filter(p => text.includes(p)).slice(0, 4);
  r.probenGesamt = proben.length;
  r.probenSichtbar = proben.filter(p => text.includes(p)).length;
  r.aufgabentext = [...document.querySelectorAll(".aufgabe")].map(a =>
    (a.innerText || "").split("\n").map(z => z.replace(/\s+/g, " ").trim()).filter(Boolean));
  return r;
}"""

# window.print() wie im Browser: beforeprint, Druckbild aufnehmen, afterprint
JS_STUB = r"""(bildQuelle) => {
  const bild = eval("(" + bildQuelle + ")");
  window.__druck = [];
  window.print = () => {
    window.dispatchEvent(new Event("beforeprint"));
    window.__druck.push({klassen: document.body.className, bild: window.__proben ? bild(window.__proben) : null});
    window.dispatchEvent(new Event("afterprint"));
  };
  window.__strgP = () => { window.dispatchEvent(new Event("beforeprint"));
    const b = bild(window.__proben); window.dispatchEvent(new Event("afterprint")); return b; };
}"""


def _zeigt_buchstaben(content):
    c = (content or "").strip()
    return c not in ("", "none", "normal", '""', "''")


def _neuer_text(vorher, nachher):
    """Zeilen, die im Druck je Aufgabe stehen, auf dem Bildschirm im Anfangszustand aber nicht."""
    neu = []
    for k, zeilen in enumerate(nachher):
        alt = vorher[k] if k < len(vorher) else []
        alles = " ".join(alt)
        neu += [z for z in zeilen if z not in alt and z not in alles]
    return neu


def _bewerten(r, modus, anfang, B, M):
    wo = "Druck '%s'" % (modus or "Strg+P ohne Knopf")
    if r["lehrer"]:
        B(wo + ": Lehrerteil sichtbar")
    if r["leiste"]:
        B(wo + ": Formelleiste oder Knopf sichtbar")
    if r["bedien"]:
        B(wo + ": Eingabefelder oder Knoepfe sichtbar: %s" % r["bedien"])
    if r["fixiert"]:
        M(wo + ": fest positionierte Elemente stehen auf jeder Seite: %s" % r["fixiert"])
    if r["rueck"]:
        B(wo + ": %d Rueckmeldungen aus der Bearbeitung sichtbar" % r["rueck"])
    if r["aufgaben"] != r["aufgabenGesamt"]:
        B(wo + ": nur %d von %d Aufgaben sichtbar" % (r["aufgaben"], r["aufgabenGesamt"]))
    if r["sammlung"] != r["formeln"]:
        B(wo + ": Formelsammlung mit %d von %d Formeln" % (r["sammlung"], r["formeln"]))
    if not r["zeilenGleich"]:
        B(wo + ": Zuordnungszeilen zeigen den Bearbeitungsstand (Farbe)")
    if modus == "arbeitsblatt":
        if r["hilfe"] or r["loesung"] or r["nurLoesung"]:
            B(wo + ": %d Hilfen, %d Loesungszeilen und %d .nur-loesung sichtbar" % (r["hilfe"], r["loesung"], r["nurLoesung"]))
        if r["lecks"]:
            B(wo + ": Loesungstext sichtbar, z.B. '%s'" % r["lecks"][0])
        neu = _neuer_text(anfang, r["aufgabentext"])
        if neu:
            B(wo + ": %d Textzeilen stehen nur im Druck, nicht auf dem Bildschirm, z.B. '%s'" % (len(neu), neu[0][:90]))
        ungleich = r["mc"] - len(r["mcGleich"])
        if ungleich:
            B(wo + ": in %d Auswahlaufgaben ist die richtige oder angeklickte Option erkennbar" % ungleich)
        zeigt = [c for c in r["zeilen"] if _zeigt_buchstaben(c)]
        if zeigt:
            B(wo + ": Zuordnung zeigt die Loesung (%s)" % zeigt[0])
        if r["ohneLinien"]:
            M(wo + ": keine Schreiblinien bei %s" % r["ohneLinien"])
    else:
        if r["hilfe"] != r["hilfeGesamt"]:
            B(wo + ": nur %d von %d Hilfen und Musterloesungen sichtbar" % (r["hilfe"], r["hilfeGesamt"]))
        if r["loesung"] != r["mc"]:
            B(wo + ": nur %d von %d Auswahlaufgaben mit Loesungszeile" % (r["loesung"], r["mc"]))
        if len(r["mcMarkiert"]) != r["mc"]:
            M(wo + ": richtige Option nur in %d von %d Auswahlaufgaben eindeutig markiert" % (len(r["mcMarkiert"]), r["mc"]))
        if r["zeilen"] and not all(_zeigt_buchstaben(c) for c in r["zeilen"]):
            M(wo + ": Zuordnung ohne Loesungsbuchstaben")


def _pruefen(pg, B, M, dm):
    knoepfe = pg.evaluate("() => [...document.querySelectorAll('[data-druck]')].map(b => b.getAttribute('data-druck'))")
    if sorted(knoepfe) != ["arbeitsblatt", "loesungen"]:
        B("Druckknoepfe fehlen: erwartet data-druck='arbeitsblatt' und 'loesungen', gefunden %s" % knoepfe)
    proben = pg.evaluate(JS_PROBEN)
    b = pg.evaluate(JS_BILDSCHIRM, proben)
    if b["druck"]:
        B("Bildschirm: im Anfangszustand sichtbar, obwohl nur fuer den Druck: %s" % b["druck"])
    if b["lecks"]:
        B("Bildschirm: Loesungstext schon im Anfangszustand sichtbar, z.B. '%s'" % b["lecks"][0])
    anfang = pg.evaluate(JS_AUFGABENTEXT)
    pg.evaluate(JS_BEARBEITEN)
    pg.wait_for_timeout(150)
    pg.evaluate(JS_STUB, JS_DRUCKBILD)

    # Am Bildschirm: echter Klick, vor dem Drucken steht genau eine Druckklasse, danach keine
    for modus in knoepfe:
        pg.click('[data-druck="%s"]' % modus)
        auf = pg.evaluate("() => window.__druck.slice(-1)")
        klassen = auf[0]["klassen"].split() if auf else []
        if "druck-" + modus not in klassen or len([k for k in klassen if k.startswith("druck-")]) != 1:
            B("Knopf '%s': beim Drucken steht am body %s statt genau druck-%s" % (modus, klassen, modus))
        rest = pg.evaluate("() => [...document.body.classList].filter(k => k.startsWith('druck-'))")
        if rest:
            B("Nach dem Drucken bleibt die Klasse %s am body stehen" % rest)

    # Druckbild bei A4-Satzbreite, aufgenommen waehrend window.print()
    pg.set_viewport_size(A4)
    pg.emulate_media(media="print")
    pg.evaluate("p => { window.__proben = p; }", proben)
    for modus in ("arbeitsblatt", "loesungen", ""):
        if modus and modus not in knoepfe:
            continue
        pg.wait_for_timeout(100)
        if modus:
            pg.evaluate("m => document.querySelector('[data-druck=\"' + m + '\"]').click()", modus)
            r = pg.evaluate("() => window.__druck.slice(-1)[0].bild")
        else:
            r = pg.evaluate("() => window.__strgP()")
        dm[modus or "standard"] = {k: r[k] for k in ("hilfe", "hilfeGesamt", "loesung", "mc", "aufgaben",
                                                    "aufgabenGesamt", "sammlung", "probenSichtbar", "probenGesamt")}
        _bewerten(r, modus, anfang, B, M)
    pg.emulate_media(media="screen")


def druckmodi_pruefen(br, url, B, M, notiz, shots=None, name=None):
    from .formelleiste import kurz
    dm = {}
    notiz["druckmodi"] = dm
    ctx = br.new_context(viewport={"width": 1280, "height": 900})
    ctx.set_default_timeout(10000)
    pg = ctx.new_page()
    pg.route("**/cdn.jsdelivr.net/**", lambda route: route.abort())
    pfehler = []
    pg.on("pageerror", lambda e: pfehler.append(str(e)))
    try:
        pg.goto(url, wait_until="load", timeout=30000)
        pg.wait_for_timeout(1700)
        _pruefen(pg, B, M, dm)
    except Exception as ex:
        B("Pruefschritt Druckmodi abgebrochen: " + kurz(ex))
    finally:
        ctx.close()
    for e in pfehler:
        B("pageerror bei der Druckpruefung: " + e)

    if shots and name:
        # PDFs mit echtem KaTeX, ueber den Knopf ausgeloest; page.pdf() feuert beforeprint und afterprint
        ctx2 = br.new_context(viewport={"width": 1280, "height": 900})
        pg2 = ctx2.new_page()
        try:
            pg2.goto(url, wait_until="load", timeout=30000)
            pg2.wait_for_timeout(1700)
            os.makedirs(shots, exist_ok=True)
            pg2.evaluate("() => { window.print = () => {}; }")
            for modus in ("arbeitsblatt", "loesungen"):
                pg2.evaluate("m => document.querySelector('[data-druck=\"' + m + '\"]').click()", modus)
                pfad = os.path.join(shots, "%s-%s.pdf" % (name, modus))
                pg2.pdf(path=pfad, format="A4", margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"})
                dm["pdf_" + modus] = pfad
        except Exception as ex:
            B("PDF-Erzeugung abgebrochen: " + kurz(ex))
        finally:
            ctx2.close()
