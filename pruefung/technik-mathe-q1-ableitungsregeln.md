# Technikprüfung mathe-q1-ableitungsregeln.html

## Schritt 1: werkzeug/modulcheck.py
Bestanden: blocker=[], maengel=[]. 7 MC, 5 Zahleneingaben, 1 Zuordnung (4 Zeilen), 24 Hilfeknöpfe, 3 Musterlösungen, 454 Formeln (Offline: 0 leer von 454), 8 Regler (rT, rDt, rB, rD, rR0, rC, rTk, rDtk) über ganzen Bereich ohne Meldung, Export ok, Druck: 0 Bedienelemente, 0 Lehrerteil, 16/16 Aufgaben, Querscrollen 1280/900/390 = 0.

## Schritt 2: eigenes Skript (Konsole, Offline, Simulation, Ziehen, Darstellung, Regeltreue)
Bestanden:
- Konsole/pageerror: online 0, offline (jsdelivr abgebrochen) 0.
- Offline: 454 `.m`-Elemente, alle mit `data-plain`, 0 leer, kein LaTeX-Rest (\frac, \cdot ...) im Text.
- Simulation 1 (rT, rDt, rB, rD): alle 16 Extremkombinationen, kein NaN/Infinity/undefined, kein Dezimalpunkt in `.anzeige`. Simulation 2 Kettenregel (rR0, rC, rTk, rDtk): 16 Extremkombinationen, ebenfalls sauber.
- Start/Pause/Zurücksetzen: Start läuft (~2 Tage/s, t=33 nach 1,5 s), Pause hält, Reset setzt t=0 und "0,0 Tage".
- Ziehen auf #cvU mit synthetischen Pointer-Events (touch): 0,1 -> 3; 0,5 -> 119; 0,9 -> 210; Werte außerhalb (1,2 / -0,2) werden auf 210 / 0 geklemmt. Kein Fehler.
- Regeltreue: kein localStorage/sessionStorage/Cookie, kein TODO/Lorem; externe Verweise nur jsdelivr/KaTeX 0.16.9; kein Dezimalpunkt im sichtbaren Text; keine englischen Oberflächentexte (Treffer "Start" ist Knopfbeschriftung "▶ Start", deutsch/gebräuchlich).
- Druck: Bedienelemente 0, Lehrerteil 0, 16/16 Aufgaben sichtbar, kein Querscrollen (scrollWidth 1000). Die Druck-Vollseite (1000x21620) war im Vorschaubild zu klein, um Kästen einzeln zu beurteilen.
- Screenshots: C:/Users/49176/AppData/Local/Temp/w/ (full/sim/kette je 1280, 900, 390; print.png). Bei 1280 Diagramme und Anzeigefelder sauber, keine Überlappungen.

## Mängel
1. Canvas-Beschriftungen bei 390 px unlesbar: alle drei Canvas (#cvRecht, #cvU, #cvKette, width=1000) werden mit Faktor 0,35 dargestellt; Schrift 11-15 px im Canvas (Zeilen 1294-1458) wird zu ca. 4-5 px. Achsenbeschriftungen, Legende, "Summe = ..." und Kettenregel-Balkenbeschriftungen sind auf dem Handy nicht zu entziffern (sim390.png, kette390.png). Vorschlag: bei schmaler Breite größere Canvas-Schrift (Skalierung nach Client-Breite) oder Legende als HTML. Nicht als Blocker: die Zahlen stehen zusätzlich in den HTML-Anzeigen. Das Referenzmodul nutzt allerdings dasselbe Verfahren (17px/13px), Mangel ist also generisch.
2. Zeitachse im Umsatzdiagramm ist fest (0 bis 25 Tage, Regler bis 21), sie wächst nicht mit; die Kurve bleibt dabei im sichtbaren Bereich. Nur Hinweis, kein Fehler.
3. Touchziele bei 390 px: Radio-Inputs 13x17 px (Label-Zeilen 316x21 px, also klickbar, aber knapp unter 44 px Höhe). Geringfügig.
4. Dateilänge 1534 Zeilen, über der Wurzelregel (~400); Referenzmodul hat 1122 Zeilen, daher modulbedingt üblich. Hinweis.

## Blocker
Keine.

## Kurzfazit
Urteil: bestanden (mit kleinen Mängeln). modulcheck.py meldet blocker=[] und maengel=[]. Eigene Prüfungen bestätigen: keine Konsolenfehler, Offline-Fallback vollständig, beide Simulationen NaN-frei über die Extrembereiche, Ziehmodus funktioniert, kein Querscrollen. Nacharbeit optional: Lesbarkeit der Canvas-Schrift bei 390 px. Nicht eigens wiederholt (vom modulcheck abgedeckt): Einzelklick auf jede MC-Option mit Farbprüfung und die vier Zahlenfälle je Eingabe; eine eigene Nachprüfung dieser Fälle wurde nicht durchgeführt.
