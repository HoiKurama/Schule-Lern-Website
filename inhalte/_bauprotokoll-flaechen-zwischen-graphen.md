# Bauprotokoll `module/mathe-q1-flaechen-zwischen-graphen.html`

Quelle: `inhalte/mathe-q1-flaechen-zwischen-graphen.md`. Referenz: `module/physik-q1-induktion.html` (nur lesen).

FORTSCHRITT: Start. Bausteine, Inhaltsdatei (Abschnitt 1-6, Lehrerteil, Checkliste) gelesen. Noch nichts gebaut.
FORTSCHRITT: Bauweise: Python-Generator im Scratchpad (`.../scratchpad/build.py`, Teile in `.../scratchpad/parts/`, Kurzschreibweise [[tex ;; plain]] fuer Formeln). Module-Datei wird von build.py erzeugt; Skript-Teile (Engines) werden 1:1 aus dem Referenzmodul geschnitten.
HILFE-ENGINE: In bausteine.md und Referenz gilt: [data-hilfe] bindet ueber closest(".aufgabe") an JEDE Aufgabe, [data-loesung] ebenso -> Hilfe an a3, a6, a7 technisch zulaessig (Browsertest folgt).
FORTSCHRITT: Teile parts/body1.html (Kopf, Abschnitt 1-3) und parts/body2.html (Abschnitt 4 Markup, Abschnitt 5 a1-a7 mit Hilfen) im Scratchpad geschrieben. Offen: body3 (Abschnitt 6 + Lehrerteil), Skript (mcDaten, numDaten, Zuordnung, Sim-IIFE, Export), build.py, Tests, Modulcheck.
FORTSCHRITT: build.py laeuft, Modul-Datei erzeugt (1300+ Zeilen). Offen: Tests (Browser), Handrechnung Simwerte, Modulcheck.
FORTSCHRITT: Wiederaufnahme nach Sitzungslimit. Modul komplett erzeugt (module/mathe-q1-flaechen-zwischen-graphen.html, 1415 Zeilen). Eigener Playwright-Test (scratchpad/test.py): 206 OK, 0 FAIL. Geprueft: alle MC je richtig/falsch, alle Zahleneingaben inkl. alt-Einheit und Fehlwerte, Zuordnung voll/Teil, Hilfen 1-3 an a1-a7 (auch a3, a6, a7 funktionieren), Musterloesungen a6/a7, alle 17 Kontrolltabellenzeilen der Simulation (4.3), sim1/sim2-Werte (9,58/11,39/0,72; -1,81/-0,58/-0,02/0,03/9,44), kein -0,00, Abstandsregel, Abspielen stoppt bei hi, Pointer-Ziehen a und b, Reset, Konsole ohne Fehler.
FORTSCHRITT: Modulcheck blocker [], maengel []. Modulliste unberuehrt.
HINWEIS: a2 -7,54 landet mit der unveraenderten Engine (Math.abs im Faktor) im nah-Text, nicht im weit-Text; der nah-Text von a2 enthaelt deshalb auch die Erklaerung zum negativen Wert.
HINWEIS: Kein zusaetzliches CSS (kein 600px-Touch-Block wie im Hauptsatz-Modul) noetig; Modulcheck 390 px: 0 Querscroll.
FORTSCHRITT: Nacharbeit-Start (fach M1-M13, technik 1-10). Noch nichts erledigt.
FORTSCHRITT: Nacharbeit HTML erledigt (M1-M9,M11,M12, Technik 1-8): Lehrerteil-Loesungsabsatz raus, sim2-Feedback 3,59/P 1,79, Plateau ab -0,37, a2-nah umgestellt, sim1/sim2-Optionen angeglichen, Anzeige 'in (a; b)', Ganzrational-Zusatz, a5 zwei Nachkommastellen, Querschnitt/G/T im Einstieg, Paar C Einheit min + Titel, Marken a/b versetzt, Legende gemessen, Canvas 1000x670, touch-action:none, Touch-CSS <=600px, Paar-B-Hinweis, Einheiten m2/m3 vereinheitlicht. Offen: Test, Modulcheck, Inhaltsdatei spiegeln (M13).
FORTSCHRITT: Inhaltsdatei gespiegelt (M13), Nachtrag zur Darstellung in 4.5/4.6. Technik 9: Druck-CSS identisch mit Referenz, keine Aenderung. Technik 10: nur aria-label am Canvas ergaenzt.
FORTSCHRITT: Restmaengel R1-R6 erledigt (Lehrerteil ohne sim2-Loesung, sim2-Option ohne Tilde, kk-Deckel 2,1 + Canvas 1000x690, sim2-Feedback b=-1,40/-0,60 live -5,98/3,74 geprueft, a2/a5 nah/weit mit 'Falls ...', data-num an a3/a6/a7 entfernt, Modulcheck weiter leer). Inhaltsdatei gespiegelt. Screenshots 390 px Paar A/B/C ohne Kollision.
