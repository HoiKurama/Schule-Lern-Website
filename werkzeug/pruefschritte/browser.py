# -*- coding: utf-8 -*-
"""Browserstart fuer den Modulcheck.

Nach einem Update des Python-Pakets fehlt oft die passende Playwright-eigene Chromium-Kopie
("Executable doesn't exist ... playwright install"). Statt dann abzubrechen, weicht der Check
auf den installierten Chrome und danach auf Edge aus. Beide sind Chromium und verhalten sich
bei Layout, Druckemulation und PDF-Ausgabe gleich.
"""


def browser_starten(p):
    """Startet Chromium headless. Gibt (browser, name) zurueck."""
    fehler = []
    for kanal in (None, "chrome", "msedge"):
        try:
            br = p.chromium.launch(channel=kanal) if kanal else p.chromium.launch()
            return br, (kanal or "playwright-chromium")
        except Exception as e:  # naechsten Kanal versuchen
            fehler.append("%s: %s" % (kanal or "playwright-chromium", str(e).splitlines()[0][:120]))
    raise RuntimeError("Kein Chromium startbar:\n  " + "\n  ".join(fehler))
