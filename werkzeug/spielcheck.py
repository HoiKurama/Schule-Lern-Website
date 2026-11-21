# -*- coding: utf-8 -*-
"""Prüfskript für das Lernspiel Feldläufer (Playwright, Python).

    python projekte/q1-lernplattform/werkzeug/spielcheck.py projekte/q1-lernplattform/spiel/physik-q1-spiel.html [shots]

Ausgabe ist JSON mit "blocker" (Spiel gilt nicht als fertig) und "maengel". Mit dem zweiten Argument
entstehen dort Bildschirmfotos. Der Modulcheck passt nicht auf das Spiel, er bricht ohne #bExport ab.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from playwright.sync_api import sync_playwright  # noqa: E402
from pruefschritte import browser_starten  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

DATEI = sys.argv[1]
SHOTS = sys.argv[2] if len(sys.argv) > 2 else None
URL = "file:///" + os.path.abspath(DATEI).replace("\\", "/")
blocker, maengel, notiz = [], [], {}


def B(t):
    blocker.append(t)


def M(t):
    maengel.append(t)


REGLER_EINHEITEN = {"m", "cm", "mm", "nm", "T", "mT", "µT", "V", "kV", "F", "mF", "µF", "nF", "pF", "Ω", "kΩ",
                    "Hz", "kHz", "MHz", "s", "ms", "m/s", "cm/s", "H", "mH"}
IDS = ["efeld", "teilchen", "magnet", "induktion", "selbst", "pendel", "schwingkreis", "wellen", "gitter"]
SCHLUESSEL_SIM = ["dauer", "zeichne", "anzeige", "urteil", "loese"]
VERBOTEN_IM_TEXT = re.compile(r"TODO|Lorem|undefined|NaN|\bnull\b|<[a-z/][^>]*>")
FLOSKELN = ["Darüber hinaus", "nahtlos", "robust", "bedeutend", "eintauchen", "Leider falsch"]


def steuerzeichen():
    with open(DATEI, encoding="utf-8") as f:
        for nr, zeile in enumerate(f, 1):
            t = re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", zeile)
            if t:
                B("Steuerzeichen %s in Zeile %d" % (repr(t[0]), nr))


def texte_sammeln(o, pfad, aus):
    if isinstance(o, str):
        aus.append((pfad, o))
    elif isinstance(o, list):
        for i, x in enumerate(o):
            texte_sammeln(x, "%s[%d]" % (pfad, i), aus)
    elif isinstance(o, dict):
        for k, x in o.items():
            texte_sammeln(x, pfad + "." + k, aus)


def daten_pruefen(d):
    st = d.get("stationen", [])
    if [s["id"] for s in st] != IDS:
        B("Stationen: erwartet %s, gefunden %s" % (IDS, [s.get("id") for s in st]))
    if len(d.get("expertenauftraege", [])) != 2:
        B("Expertenaufträge: erwartet 2, gefunden %d" % len(d.get("expertenauftraege", [])))
    for s in st:
        i = s["id"]
        r = s["regler"]
        if r["einheit"] not in REGLER_EINHEITEN:
            B("%s: Reglereinheit %s fehlt in FAKTOR" % (i, r["einheit"]))
        if not (r["min"] < r["max"] and r["schritt"] > 0):
            B("%s: Reglerbereich unsinnig" % i)
        if len(s["varianten"]) != 3:
            B("%s: %d Varianten statt 3" % (i, len(s["varianten"])))
        if len(s["hilfen"]) != 3:
            B("%s: %d Hilfen statt 3" % (i, len(s["hilfen"])))
        if len(s["fragen"]) != 3:
            B("%s: %d Bossfragen statt 3" % (i, len(s["fragen"])))
        if not (2 <= len(s["formelkarten"]) <= 3):
            M("%s: %d Formelkarten (erwartet 2 bis 3)" % (i, len(s["formelkarten"])))
        if s["welt"] != (1 if IDS.index(i) < 5 else 2):
            B("%s: falsche Welt %s" % (i, s["welt"]))
        loes = []
        for k, v in enumerate(s["varianten"]):
            l, a, b = v["loesung"], v["treffer_min"], v["treffer_max"]
            loes.append(l)
            eps = 1e-9 * max(1, abs(l))
            if not (a - eps <= l <= b + eps):
                B("%s V%d: Lösung %s liegt nicht in %s..%s" % (i, k + 1, l, a, b))
            if not (r["min"] <= l <= r["max"]):
                B("%s V%d: Lösung %s außerhalb des Reglers %s..%s" % (i, k + 1, l, r["min"], r["max"]))
            n = int((b - a) / r["schritt"] + 1e-9) + 1
            if n < 2:
                B("%s V%d: nur %d Rasterpunkt(e) im Trefferbereich" % (i, k + 1, n))
            mitte = r["min"] + (r["max"] - r["min"]) / 2
            if abs(l - mitte) < r["schritt"]:
                M("%s V%d: Lösung liegt auf dem Reglerstart" % (i, k + 1))
            if not (a >= r["min"] and b <= r["max"]):
                M("%s V%d: Trefferbereich ragt über den Regler" % (i, k + 1))
            if not v.get("rechnung"):
                B("%s V%d: Rechnung fehlt" % (i, k + 1))
        for x in range(3):
            for y in range(x + 1, 3):
                if abs(loes[x] - loes[y]) < 0.15 * max(abs(loes[x]), abs(loes[y])):
                    M("%s: Varianten %d und %d liegen unter 15 %% auseinander" % (i, x + 1, y + 1))
        fr = list(s["fragen"]) + [s["abifrage"]] + ([s["vorhersage"]] if s.get("vorhersage") else [])
        if i in ("induktion", "pendel") and not s.get("vorhersage"):
            M("%s: Vorhersage fehlt" % i)
        for k, f in enumerate(fr):
            if f["typ"] == "mc":
                if len(f["optionen"]) != 4 or len(f["feedback"]) != 4:
                    B("%s Frage %d: Optionen/Feedback nicht je 4" % (i, k))
                elif not f["feedback"][f["richtig"]].startswith("Richtig"):
                    M("%s Frage %d: Feedback der richtigen Option beginnt nicht mit „Richtig“" % (i, k))
                else:
                    for j, t in enumerate(f["feedback"]):
                        if j != f["richtig"] and (t.startswith("Richtig") or len(t) < 25):
                            M("%s Frage %d: Feedback %d zu knapp oder falsch markiert" % (i, k, j))
                if len(set(f["optionen"])) != 4:
                    B("%s Frage %d: doppelte Optionen" % (i, k))
            elif f["typ"] == "zahl":
                if not f.get("loesungsweg") or not f.get("feedback_falsch"):
                    B("%s Frage %d: Lösungsweg oder Feedback fehlt" % (i, k))
                if f["loesung"] == 0:
                    B("%s Frage %d: Lösung 0" % (i, k))
                for e, fa in f.get("einheiten_alternativ", {}).items():
                    if not isinstance(fa, (int, float)) or fa <= 0:
                        B("%s Frage %d: Faktor für %s ungültig" % (i, k, e))
            else:
                B("%s Frage %d: unbekannter Typ %s" % (i, k, f["typ"]))
            if f.get("afb") not in ("I", "II", "III"):
                B("%s Frage %d: afb=%r" % (i, k, f.get("afb")))
    alle = []
    texte_sammeln({"stationen": [{k: v for k, v in s.items() if k not in ("params",)} for s in st],
                   "experten": d.get("expertenauftraege", [])}, "", alle)
    for pfad, t in alle:
        if VERBOTEN_IM_TEXT.search(t) and not pfad.endswith(".tex"):
            B("Verdächtiger Text bei %s: %s" % (pfad, t[:80]))
        for fl in FLOSKELN:
            if fl.lower() in t.lower():
                M("Floskel „%s“ bei %s" % (fl, pfad))
        if re.search(r"\d\.\d", t) and not re.search(r"\d\.\d\d\d", t):
            M("Dezimalpunkt statt Komma bei %s: %s" % (pfad, t[:70]))
        if re.search(r"\bSie\b|\bIhre?\b", t):
            M("Siezen bei %s" % pfad)
    for e in d.get("expertenauftraege", []):
        w = len(e["musterloesung"].split())
        if not (100 <= w <= 260):
            M("Experte Welt %s: Musterlösung hat %d Wörter" % (e["welt"], w))
        if not (4 <= len(e["kriterien"]) <= 6):
            M("Experte Welt %s: %d Kriterien" % (e["welt"], len(e["kriterien"])))


def main():
    steuerzeichen()
    with sync_playwright() as p:
        br, name = browser_starten(p)
        notiz["browser"] = name
        ctx = br.new_context(viewport={"width": 1280, "height": 900})
        pg = ctx.new_page()
        konsole = []
        pg.on("console", lambda m: konsole.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: konsole.append("pageerror: " + str(e)))
        pg.goto(URL)
        pg.wait_for_timeout(800)
        pg.evaluate("spielTest.schnell = true")
        d = pg.evaluate("spielTest.daten")
        if not d.get("stationen"):
            B("DATEN leer: spieldaten_einbetten.py nicht gelaufen")
            br.close()
            return
        daten_pruefen(d)

        # Simulationen vorhanden und Gegenrechnung
        sims = pg.evaluate("Object.keys(SIMS)")
        for i in IDS:
            if i not in sims:
                B("%s: keine Simulation" % i)
        for i in IDS:
            if i not in sims:
                continue
            fehlt = pg.evaluate("(id, ks) => ks.filter(k => typeof SIMS[id][k] !== 'function' && k !== 'dauer')", [i, SCHLUESSEL_SIM])
            if fehlt:
                B("%s: SIMS fehlt %s" % (i, fehlt))
        st = {s["id"]: s for s in d["stationen"]}
        for i in IDS:
            if i not in sims or i not in st:
                continue
            for k, v in enumerate(st[i]["varianten"]):
                try:
                    l = pg.evaluate("(a) => SIMS[a[0]].loese(spielTest.daten.stationen.filter(s => s.id === a[0])[0].varianten[a[1]])", [i, k])
                except Exception as e:
                    B("%s V%d: loese() wirft %s" % (i, k + 1, str(e)[:80]))
                    continue
                if not isinstance(l, (int, float)) or abs(l - v["loesung"]) > 1e-3 * abs(v["loesung"]):
                    B("%s V%d: Gegenrechnung %s weicht von loesung %s ab" % (i, k + 1, l, v["loesung"]))

        # Spielen: je Station und Variante gewinnen und verlieren
        pg.evaluate("document.getElementById('bAlleOffen').click()")
        for i in IDS:
            if i not in st or i not in sims:
                continue
            s = st[i]
            for k, v in enumerate(s["varianten"]):
                try:
                    pg.evaluate("(a) => spielTest.oeffne(a[0], a[1])", [i, k])
                    if s.get("vorhersage"):
                        pg.evaluate("spielTest.vorhersage(0)")
                    pg.evaluate("(w) => spielTest.setzeWert(w)", v["loesung"])
                    pg.evaluate("spielTest.los()")
                    r = pg.evaluate("spielTest.runde()")
                    if not (r and r["gewonnen"] and r["sterne"] == 3):
                        B("%s V%d: Lösungswert gewinnt nicht mit 3 Sternen: %s" % (i, k + 1, r))
                    # Rand des Trefferbereichs (innen) gewinnt, knapp außen verliert
                    for rand in (v["treffer_min"], v["treffer_max"]):
                        pg.evaluate("(a) => spielTest.oeffne(a[0], a[1])", [i, k])
                        if s.get("vorhersage"):
                            pg.evaluate("spielTest.vorhersage(0)")
                        pg.evaluate("(w) => spielTest.setzeWert(w)", rand)
                        pg.evaluate("spielTest.los()")
                        r = pg.evaluate("spielTest.runde()")
                        if not (r and r["gewonnen"]):
                            B("%s V%d: Trefferrand %s gewinnt nicht" % (i, k + 1, rand))
                    schritt = s["regler"]["schritt"]
                    falsch = []
                    for faktor in (0.5, 2.0):
                        w = v["loesung"] * faktor
                        w = max(s["regler"]["min"], min(s["regler"]["max"], w))
                        if not (v["treffer_min"] <= w <= v["treffer_max"]):
                            falsch.append(w)
                    for w in falsch:
                        pg.evaluate("(a) => spielTest.oeffne(a[0], a[1])", [i, k])
                        if s.get("vorhersage"):
                            pg.evaluate("spielTest.vorhersage(0)")
                        pg.evaluate("(w) => spielTest.setzeWert(w)", w)
                        pg.evaluate("spielTest.los()")
                        r = pg.evaluate("spielTest.runde()")
                        if r and r["gewonnen"]:
                            B("%s V%d: falscher Wert %s gewinnt" % (i, k + 1, w))
                        u = pg.evaluate("(a) => spielTest.urteil(a[0], a[1], a[2])", [i, k, w])
                        if not u["text"] or VERBOTEN_IM_TEXT.search(u["text"]):
                            B("%s V%d: urteil leer oder verdächtig: %r" % (i, k + 1, u["text"]))
                        # Urteil darf die Lösung nicht verraten
                        if re.search(re.escape(("%g" % round(v["loesung"], 2)).replace(".", ",")) + r"\b", u["text"]):
                            M("%s V%d: urteil nennt womöglich die Lösung: %s" % (i, k + 1, u["text"][:100]))
                    ut = pg.evaluate("(a) => spielTest.urteil(a[0], a[1], a[2])", [i, k, v["loesung"]])
                    if not ut["treffer"]:
                        B("%s V%d: urteil() meldet am Lösungswert keinen Treffer" % (i, k + 1))
                    # Ruhebild/Animation ohne NaN
                    anz = pg.evaluate("Array.from(document.querySelectorAll('#stAnzeige div')).map(d => d.textContent)")
                    for t in anz:
                        if re.search(r"NaN|undefined|Infinity|\d\.\d", t):
                            B("%s V%d: Anzeige fehlerhaft: %s" % (i, k + 1, t))
                except Exception as e:
                    B("%s V%d: Fehler beim Spielen: %s" % (i, k + 1, str(e)[:120]))

        # Reglerdurchlauf: kein NaN im Ruhebild
        for i in IDS:
            if i not in st or i not in sims:
                continue
            r = st[i]["regler"]
            try:
                pg.evaluate("(a) => spielTest.oeffne(a[0], 0)", [i])
                for t in (0.0, 0.25, 0.5, 0.75, 1.0):
                    w = r["min"] + (r["max"] - r["min"]) * t
                    pg.evaluate("(w) => spielTest.setzeWert(w)", w)
                    anz = pg.evaluate("Array.from(document.querySelectorAll('#stAnzeige div')).map(d => d.textContent)")
                    for tx in anz:
                        if re.search(r"NaN|undefined|Infinity|\d\.\d", tx):
                            B("%s: Anzeige im Ruhebild bei w=%s fehlerhaft: %s" % (i, w, tx))
            except Exception as e:
                B("%s: Reglerdurchlauf: %s" % (i, str(e)[:100]))

        if konsole:
            B("Konsolenfehler: %s" % konsole[:5])

        # Seite von vorn: Karte, Formelbuch, Ergebnis, Abi, Speichern
        pg.goto(URL)
        pg.wait_for_timeout(500)
        pg.evaluate("spielTest.schnell = true")
        pg.evaluate("document.getElementById('bAlleOffen').click()")
        anz_knoten = pg.evaluate("document.querySelectorAll('.knoten').length")
        if anz_knoten != 9:
            B("Karte zeigt %d Stationen statt 9" % anz_knoten)
        # Abiprüfung durchklicken (immer erste Option)
        pg.evaluate("spielTest.zeige('vAbi')")
        pg.evaluate("document.getElementById('cAbiZeit').checked = false")
        pg.evaluate("document.getElementById('bAbiLos').click()")
        for _ in range(9):
            ok = pg.evaluate("""() => { const r = document.querySelector('#abiFrage input[type=radio]');
              if (r) { r.checked = true; r.dispatchEvent(new Event('change')); return true; }
              const t = document.querySelector('#abiFrage input[type=text]');
              if (t) { t.value = '1'; document.querySelector('#abiFrage button.primaer').click(); return true; }
              return false; }""")
            if not ok:
                B("Abiprüfung: Frage nicht bedienbar")
                break
            pg.evaluate("document.getElementById('bAbiWeiter').click()")
        if pg.evaluate("document.getElementById('abiEnde').hidden"):
            B("Abiprüfung endet nicht nach 9 Fragen")
        # Station komplett: Bossfragen, Formelbuch, Ergebnis
        pg.evaluate("(a) => spielTest.oeffne(a, 0)", IDS[0])
        pg.evaluate("spielTest.setzeWert(%s)" % st[IDS[0]]["varianten"][0]["loesung"])
        pg.evaluate("spielTest.los()")
        pg.evaluate("document.getElementById('bZuFragen').click()")
        n = pg.evaluate("document.querySelectorAll('#stFragen .aufgabe').length")
        if n != 3:
            B("Station 1 zeigt %d Bossfragen" % n)
        pg.evaluate("""() => document.querySelectorAll('#stFragen .aufgabe').forEach(a => {
            const r = a.querySelector('input[type=radio]');
            if (r) { r.checked = true; r.dispatchEvent(new Event('change')); }
            else { a.querySelector('input[type=text]').value = '1'; a.querySelector('button.primaer').click(); } })""")
        if pg.evaluate("document.getElementById('stAbschluss').hidden"):
            B("Nach drei Bossfragen erscheint kein Abschluss-Knopf")
        gespeichert = pg.evaluate("Object.keys(localStorage).filter(k => k.indexOf('q1lernen:') === 0)")
        if not gespeichert:
            B("Kein Spielstand unter q1lernen: gespeichert")
        else:
            bil = pg.evaluate("JSON.parse(localStorage.getItem(%r)).bilanz" % gespeichert[0])
            if not bil or bil.get("gesamt") != 36:
                B("bilanz.gesamt = %r, erwartet 36" % (bil,))
        pg.reload()
        pg.wait_for_timeout(400)
        sterne = pg.evaluate("spielTest.zustand().stationen.%s.sterne" % IDS[0])
        if sterne != 3:
            B("Spielstand nach Neuladen: %s Sterne statt 3" % sterne)
        for ansicht in ("vFormelbuch", "vErgebnis"):
            pg.evaluate("spielTest.zeige(%r)" % ansicht)
            pg.wait_for_timeout(300)
            t = pg.evaluate("document.getElementById(%r).innerText" % ansicht)
            if re.search(r"NaN|undefined", t):
                B("%s zeigt NaN/undefined" % ansicht)
        # Offline: ohne KaTeX lesbar
        ctx2 = br.new_context(viewport={"width": 1280, "height": 900})
        ctx2.route("**/cdn.jsdelivr.net/**", lambda r: r.abort())
        pg2 = ctx2.new_page()
        pg2.goto(URL)
        pg2.wait_for_timeout(800)
        pg2.evaluate("spielTest.schnell = true")
        pg2.evaluate("document.getElementById('bAlleOffen').click()")
        pg2.evaluate("(a) => spielTest.oeffne(a, 0)", IDS[0])
        pg2.evaluate("spielTest.setzeWert(%s)" % st[IDS[0]]["varianten"][0]["loesung"])
        pg2.evaluate("spielTest.los()")
        pg2.evaluate("spielTest.zeige('vFormelbuch')")
        pg2.wait_for_timeout(400)
        leer = pg2.evaluate("Array.from(document.querySelectorAll('#fbInhalt .m')).filter(m => !m.textContent.trim()).length")
        if leer:
            B("Offline: %d leere Formeln im Formelbuch" % leer)
        ctx2.close()

        # Überlauf in drei Breiten, mit Foto
        for breite in (1280, 900, 390):
            c3 = br.new_context(viewport={"width": breite, "height": 900})
            p3 = c3.new_page()
            p3.goto(URL)
            p3.wait_for_timeout(600)
            p3.evaluate("spielTest.schnell = true")
            p3.evaluate("document.getElementById('bAlleOffen').click()")
            for ans, vorb in (("vKarte", None), ("vStation", IDS[0]), ("vFormelbuch", None), ("vErgebnis", None)):
                if vorb:
                    p3.evaluate("(a) => spielTest.oeffne(a, 0)", vorb)
                else:
                    p3.evaluate("(a) => spielTest.zeige(a)", ans)
                p3.wait_for_timeout(250)
                ueber = p3.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                if ueber > 2:
                    B("Querscrollen %d px bei %d px Breite in %s" % (ueber, breite, ans))
                if SHOTS:
                    os.makedirs(SHOTS, exist_ok=True)
                    p3.screenshot(path=os.path.join(SHOTS, "spiel-%s-%d.png" % (ans, breite)), full_page=True)
            if SHOTS and breite in (1280, 390):
                for i in IDS:
                    if i not in st or i not in sims:
                        continue
                    p3.evaluate("(a) => spielTest.oeffne(a, 0)", i)
                    p3.evaluate("(w) => spielTest.setzeWert(w)", st[i]["varianten"][0]["loesung"])
                    p3.wait_for_timeout(150)
                    p3.screenshot(path=os.path.join(SHOTS, "station-%s-ruhe-%d.png" % (i, breite)), full_page=False)
                    p3.evaluate("spielTest.los()")
                    p3.wait_for_timeout(150)
                    p3.screenshot(path=os.path.join(SHOTS, "station-%s-ende-%d.png" % (i, breite)), full_page=False)
            c3.close()
        # Druck
        c4 = br.new_context(viewport={"width": 1000, "height": 900})
        p4 = c4.new_page()
        p4.goto(URL)
        p4.wait_for_timeout(500)
        p4.emulate_media(media="print")
        p4.evaluate("spielTest.zeige('vErgebnis')")
        sichtbar = p4.evaluate("""() => ['.spielleiste', '#bExport', '#bStandLoeschen', 'details.lehrer']
            .filter(s => { const e = document.querySelector(s); return e && getComputedStyle(e).display !== 'none'; })""")
        if sichtbar:
            M("Im Druck sichtbar: %s" % sichtbar)
        br.close()
    print(json.dumps({"blocker": blocker, "maengel": maengel, "notiz": notiz}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
