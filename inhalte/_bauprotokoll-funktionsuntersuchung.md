# Bauprotokoll `module/mathe-q1-funktionsuntersuchung.html`

Quelle: `inhalte/mathe-q1-funktionsuntersuchung.md`. Referenz: `module/physik-q1-induktion.html` (nur lesen).

## Arbeitsweise (bei Abbruch hier weitermachen)

Bauteile liegen als Teildateien im Scratchpad
`C:/Users/49176/AppData/Local/Temp/claude/C--Users-49176-Documents-Claude-Projects-Schule/a4e21d4f-5e40-4a28-8031-ae2059d6cc04/scratchpad/`
(p1..p6.html, engine.js, sim.js, bau.py). `bau.py` setzt sie zur Moduldatei zusammen
(Kurzschreibweise `[[tex ;; plain]]` wird zu `<span class="m" data-tex data-plain>`).
Falls das Scratchpad weg ist: Modul direkt aus der Inhaltsdatei neu bauen.

## Fortschritt
- Quellen gelesen (CLAUDE.md, bausteine.md, Referenz, Inhaltsdatei).
- Teile p1-p4 (Sektionen 1-6 + Lehrerteil), daten.js (mcDaten/numDaten/Engines), sim.js (Simulation), bau.py geschrieben; Modul erstmals gebaut (module/mathe-q1-funktionsuntersuchung.html, ~1520 Zeilen).
- Abweichung von der Engine: Zahlen-Engine vergleicht den Quotienten Eingabe/Sollwert jetzt VORZEICHENBEHAFTET (ohne Betrag), sonst waeren bei a1 (Soll -4) der Wert 3 und bei a2 (Soll -7) der Wert +7 "nah" statt "weit" (Inhaltsdatei K19). Zuordnung setzt ergebnisse.z1 (statt a3), mit eigenem Text fuer "keine richtig".
- Als Naechstes: Modulcheck, Playwright-Handrechnung der Simulation, Screenshot.
- Modulcheck (nach Legenden-/Marker-Korrektur): blocker [], maengel []. Modulliste NICHT auf fertig gesetzt (Auftrag).
- Simulation gegen Handrechnung (Playwright, Anzeigen ausgelesen, alle identisch mit K7/4.6):
  S1 a=1,x0=2: f 0,67 · f' 3,00 · f'' 4,00 · H(-1|0,67) T(1|-0,67) W(0|0) m -1,00.
  S1 a=4,x0=2: f -5,33 · f' 0,00 · T(2|-5,33) · m -4,00. S1 a=0: keine H/T, S(0|0). S1 a=-1: m +1,00.
  S2 a=-0,5,x0=2,5: f -2,29 · f' 0,75 · f'' 3,00 · H(-0,22|0,06) T(2,22|-2,39) W(1|-1,17) m -1,50 (Hand: 2,22 / -2,39 / -1,17 ok).
  S2 x0=1: a=0,95 m -0,05 H(0,78|0,29) T(1,22|0,28); a=1,00 nur S(1|0,33) m 0,00 + Befundsatz; a=1,05 m +0,05; f''(1)=0,00 fuer jedes a.
  S3 a=1,x0=2: f 1,33 · f' 4,00 · f'' 8,00 · T(1|-0,08) S(0|0) W(0,67|-0,05); a=0,x0=0: nur T(0|0), kein S/W, Befundsatz.
  Baender (Pixelproben cvAbl): S2 a=1 f'-Band nur gruen, f''-Band orange -> blau bei x=1; S2 a=0 f'-Band gruen/rot/gruen.
  Abspielen: nach 2,009 s von x0=-3 -> x0 = -1,00; stoppt bei 3,00. Ziehen: 70 % Breite -> x0 = 2,25 (Hand 2,25).
- Zahleneingaben (alle Zonen aus K19), MC (richtig/falsch je Option), Zuordnung (C-B-D-A, Teilerfolg, keine), Hilfen/Musterloesungen, Export, Konsole: ohne Fehler.
- Offen: Kernlehrplan-Zuordnung (Einfuehrungsphase/Q1) laut Inhaltsdatei Rueckfrage an Fachkonferenz; Modulliste-Eintrag (nicht auf fertig gesetzt).

## Nacharbeit nach Fach- und Technikprüfung
- M1 Lehrerteil (Bezug auf a1 umgedreht), M2 a1.nah/weit (+4 erklaert, "Vorzeichen" aus nah gestrichen), M3 Einstieg neutral formuliert (Teil der a-Werte / genau zwischen beiden Bereichen), M5 vw3-Stamm ("Welche Aussage ... ist richtig?"), M6 doppeltes </style> entfernt, M7 sim2-Optionen 0 und 2 mit Klammerbegruendung verlaengert, M8 a3-Tipp auf "Was bedeutet 0 <= t <= 5 fuer deine Kandidatenliste?", M9 weit-Zusaetze fuer a3 (4), a4 (12), a5 (6), M10 "vorzeichenkonstant".
- M4: GEWAEHLT wurde die Uebung (nicht die Abschwaechung des Selbstchecks): neue offene Aufgabe `a8` (AB II, zwischen a5 und z1), drei Hilfestufen, Musterlösung mit Bewertungskriterien. ABWEICHUNG vom Berichtsvorschlag: statt f_t = x^3 - 3t x^2 (Loesung steht wortgleich in 3.2/3.3) f_t(x) = x^3 - 3t^2 x. Ergebnis (sympy geprueft): Extremstellen ±t, t>0 T(t|-2t^3), H(-t|2t^3); t<0 vertauscht; t=0 Sattelpunkt; Ortskurve beider Punkte y = -2x^3; Proben t=2 T(2|-16), H(-2|16), t=-1 H(-1|2), T(1|-2).
  Folgen nachgezogen: Lehrerteil (zehn Aufgaben, Typischer Fehler 6, Vertiefen), Zeitbedarf 40->45 min, Summe 130, Chip "ca. 130 Minuten" (Modul und Inhaltsdatei), Checkliste/Pruefpunkte 10 und 14, Export haengt drei Textareas an (a8 nicht in namen, laeuft nicht ueber ergebnisse; Zaehlung "Zwoelf Schluessel" bleibt).
- Inhaltsdatei gespiegelt: Einstieg, vw3, a3-Tipp, a1/a3/a4/a5-Rueckmeldungen, sim2-Optionen und -Rueckmeldung, Aufgabe 6a (a8) samt K20, Lehrerteil, Zeit, Checkliste. Kontrollrechnungen K1-K19 unberuehrt und weiter gueltig; K19-Zonen durch die neuen Zusatztexte nicht veraendert.
- Technik 1/2: Touch-CSS <=600 px (Buttons 44 px, Regler 32 px, Selects 44 px hoch/72 px breit, Checkboxen 24 px) gemessen bei 390 px. Technik 3: Schriftfaktor der Canvas jetzt min(2,7, 900/Breite) (bei 390 px Beschriftungen ~13 px angezeigt), Legende auf Kurzform. Technik 4/5: Druck geprueft, Referenzmodul zeigt Eingabefelder/Prüfen-Knoepfe ebenso -> nicht geaendert; Dezimalkomma im number-Feld weiter per Code (Komma->Punkt), nicht testbar.
- Modulcheck: blocker [], maengel []; Druck 15/15 Aufgaben, kein Querscrollen. Modulliste NICHT auf fertig gesetzt.

## Restmaengel R1-R8 (Gegenpruefung)
- R1 Zeit-Chip im Kopf jetzt "ca. 130 Minuten" (war beim Nacharbeiten uebersehen worden, weil der Kopf im Bauskript stand).
- R2 a8 in der Pflichtliste des Lehrerteils (Tiefpunkt, Wendetangente, Sattelpunkt begruenden, a8, Zuordnung, Schuelerloesung); a3 (Pegel) in die Differenzierung geschoben, Standardweg-Satz angepasst; Zeit bleibt 45 min / 130 min. Inhaltsdatei (Zeitzeile, Standard) nachgefuehrt.
- R3 a8 Stufe 3: Knopf "Loesungsgeruest", nur Schluesselzahlen und Gliederung; volle Loesung nur in data-stufe="9". R4 Musterloesung mit Satz zur gleichen Ortskurve y = -2x^3 wie bei den Wendepunkten in 3.2 (Form (t | -2t^3)), Nachpruefen gefordert. R5 Klammer im Aufgabentext gestrichen, Faelle erst im Tipp.
- R6 data-offen an den drei Textareas (a8, a6, a7), Export nutzt ta.dataset.offen || "Offene Aufgabe i" (Clipboard-Test bestaetigt). R7 .check input 24x24 im 600-px-Block. R8 Kommentarkopf "Touch (schmale Geraete)".
- Korrektur einer Angabe weiter oben: Die Canvas-Beschriftungen sind bei 390 px real ca. 11,8 px gross (nicht 13 px).
- Inhaltsdatei gespiegelt (Aufgabe 6a, Zeit, Pflichtliste, Standard). Modulcheck: blocker [], maengel []. Modulliste nicht angefasst.
