# -*- coding: utf-8 -*-
"""Pruefschritt Formelleiste (vorlage/baustein-formelleiste.md).

Geprueft wird:
  - der Datenvertrag von formelDaten samt Formelsammlung (Pflichtfelder, ids, Backslashes,
    Uebereinstimmung mit der Formel am Sprungziel, jede id="f-..." im Text hat einen Eintrag)
  - jede Erklaerung klappt per Klick auf und wieder zu und zeigt alle Zeichen und Einheiten
  - jeder Link "im Text" bringt sein Ziel ins Bild, und danach ist genau diese Formel
    hervorgehoben, mit und ohne weiches Scrollen, bei 1280 px und in der Schublade bei 390 px
  - die Hervorhebung folgt der Lesestelle (IntersectionObserver)
  - ab 1100 px mitlaufende Leiste neben dem Inhalt, darunter Schublade mit Knopf, Schliessen per
    x, Esc und Klick daneben, Doppelklick, Fokusfalle, Trefferflaechen >= 44 px, kein Querscrollen
  - mit echtem KaTeX: keine Formel ueberragt ihre Box, weder in der Leiste noch im Druck (A4)
Jeder Teilschritt faengt seine Ausnahmen selbst und meldet sie als Blocker. Die Leiste wird danach
hart zurueckgesetzt, damit ein einzelner Fehler keine Folgemeldungen und keinen Abbruch erzeugt.
"""
from playwright.sync_api import TimeoutError as PWTimeout
from .formelleiste_js import (JS_VERTRAG, JS_ERKLAERUNG, JS_ZIEL, JS_AKTIV, JS_AKTIV_IST, JS_GROESSE,
                              JS_SCHUBLADE, JS_ZURUECK, JS_UEBERLAUF)

# Unter Last (mehrere Checks parallel) liefert Chrome kaum Frames: Hervorhebung und Klickbereitschaft
# brauchen dann Sekunden. Gewartet wird per Abfrage, die Grenzen gelten nur fuer echte Fehler.
WARTEN = 8000    # ms bis zur richtigen Hervorhebung
AKTION = 10000   # ms fuer Klicks und Tastendruck
LESELINIE = 0.4  # wie LESESTELLE im Seitenskript


def kurz(e):
    """Erste Zeile einer Ausnahme, bei Playwright ergaenzt um das Element, auf das gewartet wurde."""
    t = str(e).strip()
    if not t:
        return type(e).__name__
    zeilen = t.splitlines()
    worauf = next((z.strip().lstrip("- ") for z in zeilen if "waiting for" in z), "")
    return zeilen[0][:120] + (" (%s)" % worauf[:90] if worauf else "")


def _warte_aktiv(pg, fid):
    """Wartet, bis genau der Eintrag fid hervorgehoben ist (fid None: keiner). Liefert (ok, aktiv)."""
    try:
        pg.wait_for_function(JS_AKTIV_IST, arg=fid, timeout=WARTEN, polling=50)
        return True, ([fid] if fid else [])
    except PWTimeout:
        return False, pg.evaluate(JS_AKTIV)


def _warte_ruhe(pg, max_ms=4000):
    """Wartet, bis das weiche Scrollen zur Ruhe gekommen ist (Position 3 Messungen lang gleich).
    Lange Seiten scrollen laenger als der Hervorhebungs-Wechsel dauert."""
    pg.wait_for_timeout(250)  # das weiche Scrollen setzt erst kurz nach dem Klick ein
    letzte, gleich = None, 0
    for _ in range(max_ms // 80):
        y = pg.evaluate("() => Math.round(window.scrollY)")
        gleich = gleich + 1 if y == letzte else 0
        if gleich >= 4:
            return
        letzte = y
        pg.wait_for_timeout(80)


def _offen(pg):
    return pg.evaluate("() => document.querySelector('.formelleiste').classList.contains('offen')")


def _erklaerungen(pg, soll, B, modus):
    """Jede Erklaerung auf- und wieder zuklappen."""
    offen = 0
    for i, s in enumerate(soll):
        wo = "Formelleiste (%s), Erklaerung %s" % (modus, s["id"])
        try:
            knopf = pg.locator(".formelleiste .fl-info").nth(i)
            knopf.click()
            pg.wait_for_timeout(60)
            e = pg.evaluate(JS_ERKLAERUNG, i)
            if e["hidden"] or not e["sichtbar"]:
                B(wo + ": bleibt nach Klick auf den i-Knopf verborgen")
                continue
            if e["expanded"] != "true":
                B(wo + ": ist offen, aber aria-expanded bleibt '%s'" % e["expanded"])
            offen += 1
            if e["zeichen"] != s["zeichen"]:
                B(wo + ": zeigt %d von %d Zeichenbedeutungen" % (e["zeichen"], s["zeichen"]))
            if e["einheiten"] != s["einheiten"]:
                B(wo + ": zeigt %d von %d Einheiten" % (e["einheiten"], s["einheiten"]))
            if not (e["gilt"] and e["fehler"]):
                B(wo + ": Gueltigkeit oder typischer Fehler fehlt")
            if not e["link"]:
                B(wo + ": kein Link 'im Text'")
            knopf.click()
            pg.wait_for_timeout(40)
            e2 = pg.evaluate(JS_ERKLAERUNG, i)
            if not e2["hidden"]:
                B(wo + ": klappt beim zweiten Klick nicht wieder zu")
            elif e2["expanded"] != "false":
                B(wo + ": ist zu, aber aria-expanded bleibt '%s'" % e2["expanded"])
        except Exception as ex:
            B(wo + ": nicht bedienbar: " + kurz(ex))
        finally:
            pg.evaluate(JS_ZURUECK)
    return offen


def _sprunglinks(pg, soll, B, M, modus, schublade):
    """Jeden Link 'im Text' anklicken: Ziel im Bild, genau diese Formel hervorgehoben."""
    getroffen = markiert = 0
    for i, s in enumerate(soll):
        wo = "Formelleiste (%s), Link zu %s" % (modus, s["id"])
        try:
            pg.evaluate(JS_ZURUECK)
            if schublade:
                pg.click(".fl-knopf")
                pg.wait_for_timeout(300)
            pg.locator(".formelleiste .fl-info").nth(i).click()
            pg.wait_for_timeout(60)
            e = pg.evaluate(JS_ERKLAERUNG, i)
            if e["hidden"] or not e["link"]:
                continue  # schon bei den Erklaerungen gemeldet
            pg.locator('[id="%s"] a.fl-link' % e["id"]).click()
            ok, akt = _warte_aktiv(pg, e["formel"])
            _warte_ruhe(pg)
            z = pg.evaluate(JS_ZIEL, e["link"])
            if not z["da"]:
                B(wo + ": Ziel %s existiert nicht" % e["link"])
                continue
            if not z["gerendert"] or z["zu"]:
                B(wo + ": Ziel ist nach dem Sprung nicht sichtbar (zugeklappte Herleitung?)")
            elif not z["imBild"]:
                B(wo + ": Ziel steht nach dem Sprung nicht im Bild (top=%s)" % z["top"])
            else:
                getroffen += 1
            if ok:
                markiert += 1
            else:
                M(wo + ": nach dem Sprung ist %s hervorgehoben statt %s" % (akt or "nichts", e["formel"]))
            if schublade and _offen(pg):
                B(wo + ": Schublade bleibt nach dem Sprung offen und verdeckt das Ziel")
        except Exception as ex:
            B(wo + ": nicht bedienbar: " + kurz(ex))
        finally:
            pg.evaluate(JS_ZURUECK)
    return "%d von %d im Bild, %d hervorgehoben" % (getroffen, len(soll), markiert)


def _hervorhebung(pg, M, notiz):
    """Formelziel an die Lesestelle schieben; der zugehoerige Eintrag muss hervorgehoben sein."""
    daten = pg.evaluate("() => formelDaten.flatMap(g => g.formeln.map(f => ({id: f.id, ziel: f.ziel})))")
    treffer, fehl, unerreichbar = 0, [], 0
    for f in daten:
        vorher = pg.evaluate(JS_AKTIV)
        # Ziel knapp ueber die Leselinie schieben; eine zugeklappte Herleitung zaehlt mit ihrer Position
        ok = pg.evaluate("""([z, lin]) => { const e = document.getElementById(z); if (!e) return false;
            const bez = e.closest('details:not([open])') || e;
            window.scrollTo(0, scrollY + bez.getBoundingClientRect().top - innerHeight * lin + 6);
            const t = bez.getBoundingClientRect().top;
            return t <= innerHeight * lin && t > innerHeight * lin - 40; }""", [f["ziel"], LESELINIE])
        if not ok:
            unerreichbar += 1
            continue
        gut, akt = _warte_aktiv(pg, f["id"])
        if gut:
            treffer += 1
        else:
            fehl.append("%s -> %s%s" % (f["id"], akt, " (aendert sich nicht)" if akt == vorher else ""))
    if fehl:
        M("Formelleiste: Hervorhebung folgt der Lesestelle nicht bei %s" % "; ".join(fehl[:6]))
    ohne = pg.evaluate("""() => { const mit = new Set(formelDaten.map(g => g.abschnitt));
        const s = [...document.querySelectorAll('.wrap > section[id]')].find(x => !mit.has(x.id) && x.id !== 'einstieg');
        if (!s) return null; window.scrollTo(0, scrollY + s.getBoundingClientRect().top - innerHeight * 0.1); return s.id; }""")
    if ohne and not _warte_aktiv(pg, None)[0]:
        M("Formelleiste: im Abschnitt #%s ohne Formeln bleibt ein Eintrag hervorgehoben" % ohne)
    notiz["hervorhebung"] = "%d von %d" % (treffer, len(daten)) + (
        ", %d Ziele nicht an die Leselinie scrollbar" % unerreichbar if unerreichbar else "")


def _desktop(pg, B, M):
    for breite in (1280, 1100):
        pg.set_viewport_size({"width": breite, "height": 900})
        pg.evaluate("() => window.scrollTo(0, 0)")
        pg.wait_for_timeout(200)
        d = pg.evaluate("""() => { const l = document.querySelector('.formelleiste'), w = document.querySelector('.seite > .wrap');
            const k = document.querySelector('.fl-knopf'), r = l.getBoundingClientRect();
            return {pos: getComputedStyle(l).position, sichtbar: getComputedStyle(l).visibility !== 'hidden' && r.width > 0,
                    nebenInhalt: !!w && r.left >= w.getBoundingClientRect().right - 1, rechts: r.right <= innerWidth,
                    knopf: k && getComputedStyle(k).display !== 'none',
                    ueberlauf: document.documentElement.scrollWidth - document.documentElement.clientWidth}; }""")
        wo = "Formelleiste bei %d px" % breite
        if d["pos"] != "sticky" or not d["sichtbar"]:
            B(wo + ": keine sichtbare mitlaufende Leiste (position %s)" % d["pos"])
        if not (d["nebenInhalt"] and d["rechts"]):
            B(wo + ": Leiste steht nicht rechts neben dem Inhalt")
        if d["knopf"]:
            M(wo + ": Knopf 'Formeln' ist trotz Leiste sichtbar")
        if d["ueberlauf"] > 0:
            B(wo + ": Querscrollen %d px" % d["ueberlauf"])
    pg.set_viewport_size({"width": 1280, "height": 900})
    pg.evaluate("() => window.scrollTo(0, document.body.scrollHeight * 0.5)")
    pg.wait_for_timeout(200)
    mit = pg.evaluate("() => { const r = document.querySelector('.formelleiste').getBoundingClientRect(); return r.top >= 0 && r.top < 60 && r.bottom <= innerHeight + 1; }")
    if not mit:
        B("Formelleiste bei 1280 px: laeuft beim Scrollen nicht mit (sticky greift nicht)")
    klein = [g for g in pg.evaluate(JS_GROESSE, ".formelleiste .fl-info") if min(g) < 44]
    if klein:
        B("Formelleiste: %d i-Knoepfe unter 44 px, z.B. %s" % (len(klein), klein[0]))


def _schublade(pg, B, M, breite):
    """Schublade oeffnen und auf drei Wegen schliessen; Fokus, Groessen, Fokusfalle."""
    wo = "Formelleiste bei %d px" % breite
    s = pg.evaluate(JS_SCHUBLADE)
    if s["sichtbar"] or not s["knopf"]:
        B(wo + ": Leiste ist nicht eingeklappt oder der Knopf 'Formeln' fehlt")
        return
    g = pg.evaluate(JS_GROESSE, ".fl-knopf")
    if g and min(g[0]) < 44:
        B(wo + ": Knopf 'Formeln' nur %s px" % g[0])
    if s["ueberlauf"] > 0:
        B(wo + ": Querscrollen %d px bei geschlossener Schublade" % s["ueberlauf"])
    for wie in ("Esc", "x", "daneben"):
        try:
            pg.click(".fl-knopf")
            pg.wait_for_timeout(320)
            s = pg.evaluate(JS_SCHUBLADE)
            if not (s["offen"] and s["sichtbar"] and s["expanded"] == "true" and s["schleier"]):
                B(wo + ": Knopf 'Formeln' oeffnet die Schublade nicht")
                return
            if s["links"] < 0 or s["rechts"] > s["breite"] + 1:
                B(wo + ": Schublade ragt aus dem Bild (%d..%d)" % (s["links"], s["rechts"]))
            if s["ueberlauf"] > 0:
                B(wo + ": Querscrollen %d px bei offener Schublade" % s["ueberlauf"])
            if not s["fokusDrin"] or s["rolle"] != "dialog":
                M(wo + ": offene Schublade ist kein Dialog mit Fokus darin")
            if wie == "Esc":
                klein = [x for x in pg.evaluate(JS_GROESSE, ".formelleiste .fl-info, .fl-zu") if min(x) < 44]
                if klein:
                    B(wo + ": %d Knoepfe in der Schublade unter 44 px" % len(klein))
                # Fokusfalle: Klick auf Text in der Schublade, dann Umschalt+Tab
                pg.click("#fl-titel", force=True)
                pg.keyboard.press("Shift+Tab")
                if not pg.evaluate(JS_SCHUBLADE)["fokusDrin"]:
                    M(wo + ": Umschalt+Tab fuehrt aus der offenen Schublade hinaus")
                pg.keyboard.press("Escape")
            elif wie == "x":
                pg.click(".fl-zu")
            else:
                pg.wait_for_timeout(150)  # der Schleier ignoriert Klicks kurz nach dem Oeffnen (Doppelklick)
                pg.mouse.click(8, 430)
            pg.wait_for_timeout(320)
            s = pg.evaluate(JS_SCHUBLADE)
            if s["offen"] or s["sichtbar"] or s["schleier"]:
                B(wo + ": Schliessen per %s funktioniert nicht" % wie)
            elif not s["fokusKnopf"]:
                M(wo + ": nach Schliessen per %s liegt der Fokus nicht wieder auf dem Knopf" % wie)
        except Exception as ex:
            B(wo + ": Schublade (%s) nicht bedienbar: %s" % (wie, kurz(ex)))
        finally:
            pg.evaluate(JS_ZURUECK)


def _ueberlauf(pg, M, fl):
    """Mit echtem KaTeX: Formeln in der Leiste (1280 px) und im Druck (A4 hoch, 680 px Satzbreite)."""
    if not pg.evaluate("() => typeof katex !== 'undefined' && !document.body.classList.contains('no-katex')"):
        fl["ueberlauf"] = "ungeprueft, KaTeX nicht geladen"
        return
    pg.set_viewport_size({"width": 1280, "height": 900})
    pg.wait_for_timeout(100)
    leiste = pg.evaluate(JS_UEBERLAUF, ".fl-zeile .m")
    if leiste:
        M("Formelleiste: %d Formeln ueberragen die Leiste, z.B. %s" % (len(leiste), leiste[0]))
    pg.set_viewport_size({"width": 680, "height": 900})
    pg.emulate_media(media="print")
    pg.wait_for_timeout(150)
    druck = pg.evaluate(JS_UEBERLAUF, ".m")
    pg.emulate_media(media="screen")
    if druck:
        M("Druck (A4): %d Formeln laufen ueber den Rand und werden abgeschnitten, z.B. %s" % (len(druck), druck[0]))
    fl["ueberlauf"] = {"leiste": len(leiste), "druck": len(druck)}


def formelleiste_pruefen(br, url, B, M, notiz, physik=False):
    fl = {}
    notiz["formelleiste"] = fl
    ctx = br.new_context(viewport={"width": 1280, "height": 900}, reduced_motion="reduce")
    ctx.set_default_timeout(AKTION)
    pg = ctx.new_page()
    pfehler = []
    pg.on("pageerror", lambda e: pfehler.append(str(e)))
    try:
        pg.goto(url, wait_until="load", timeout=30000)
        pg.wait_for_timeout(1500)
        v = pg.evaluate(JS_VERTRAG, {"physik": physik})
        if not v["vorhanden"]:
            B("Formelleiste fehlt: kein Objekt formelDaten")
            return
        for t in v["fehler"]:
            B("formelDaten: " + t)
        for t in v["maengel"]:
            M("formelDaten: " + t)
        fl.update(gruppen=v["gruppen"], formeln=v["formeln"], eintraege=v.get("eintraege"))
        if v.get("eintraege") != v["formeln"] or v.get("knoepfe") != v["formeln"]:
            B("Formelleiste zeigt %s Eintraege, formelDaten hat %d Formeln" % (v.get("eintraege"), v["formeln"]))
            return
        soll = v["soll"]

        _desktop(pg, B, M)
        fl["erklaerungen_1280"] = "%d von %d" % (_erklaerungen(pg, soll, B, "1280 px"), len(soll))
        fl["sprunglinks_1280"] = _sprunglinks(pg, soll, B, M, "1280 px", False)
        _hervorhebung(pg, M, fl)
        for breite in (1099, 900, 390):
            pg.set_viewport_size({"width": breite, "height": 860})
            pg.evaluate("() => window.scrollTo(0, 0)")
            pg.wait_for_timeout(300)
            _schublade(pg, B, M, breite)
        fl["sprunglinks_390"] = _sprunglinks(pg, soll, B, M, "390 px", True)
        _ueberlauf(pg, M, fl)
    except Exception as ex:
        B("Pruefschritt Formelleiste abgebrochen: " + kurz(ex))
    finally:
        ctx.close()

    # Weiches Scrollen und Einfahr-Animation, wie ohne Einstellung "Bewegung reduzieren"
    ctx = br.new_context(viewport={"width": 1280, "height": 900}, reduced_motion="no-preference")
    ctx.set_default_timeout(AKTION)
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: pfehler.append(str(e)))
    try:
        pg.goto(url, wait_until="load", timeout=30000)
        pg.wait_for_timeout(1500)
        soll = pg.evaluate(JS_VERTRAG, {"physik": physik}).get("soll", [])
        fl["sprunglinks_weich"] = _sprunglinks(pg, soll, B, M, "1280 px, weiches Scrollen", False)
        pg.set_viewport_size({"width": 900, "height": 860})
        pg.wait_for_timeout(300)
        pg.dblclick(".fl-knopf")
        pg.wait_for_timeout(450)
        if not _offen(pg):
            M("Formelleiste bei 900 px: ein Doppelklick auf 'Formeln' schliesst die Schublade gleich wieder")
    except Exception as ex:
        B("Pruefschritt Formelleiste (weiches Scrollen) abgebrochen: " + kurz(ex))
    finally:
        ctx.close()
    for e in pfehler:
        B("pageerror in der Formelleiste: " + e)
