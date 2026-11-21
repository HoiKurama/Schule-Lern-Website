"""Bettet inhalte/physik-q1-spiel-daten.json in spiel/physik-q1-spiel.html ein.

Die Spielseite bleibt eine Datei ohne Imports. Die Daten stehen zwischen den Markierungen
/*DATEN-ANFANG*/ und /*DATEN-ENDE*/. Nach jeder Änderung an der JSON-Datei erneut ausführen:

    python projekte/q1-lernplattform/werkzeug/spieldaten_einbetten.py
"""
import json
import re
import sys
from pathlib import Path

PROJEKT = Path(__file__).resolve().parent.parent
JSON_DATEI = PROJEKT / "inhalte" / "physik-q1-spiel-daten.json"
HTML_DATEI = PROJEKT / "spiel" / "physik-q1-spiel.html"
MUSTER = re.compile(r"/\*DATEN-ANFANG\*/.*?/\*DATEN-ENDE\*/", re.S)


def daten_als_js(daten):
    text = json.dumps(daten, ensure_ascii=False, indent=1)
    # Ein "</" im Text würde den <script>-Block vorzeitig beenden
    return text.replace("</", "<\\/")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    daten = json.loads(JSON_DATEI.read_text(encoding="utf-8"))
    html = HTML_DATEI.read_text(encoding="utf-8")
    if not MUSTER.search(html):
        sys.exit("Markierungen /*DATEN-ANFANG*/ und /*DATEN-ENDE*/ fehlen in " + str(HTML_DATEI))
    neu = MUSTER.sub(lambda m: "/*DATEN-ANFANG*/" + daten_als_js(daten) + "/*DATEN-ENDE*/", html, count=1)
    HTML_DATEI.write_text(neu, encoding="utf-8", newline="\n")
    print("eingebettet: %d Stationen, %d Expertenaufträge" % (
        len(daten.get("stationen", [])), len(daten.get("expertenauftraege", []))))


if __name__ == "__main__":
    main()
