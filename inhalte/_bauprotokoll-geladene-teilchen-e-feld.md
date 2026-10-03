# Bauprotokoll `module/physik-q1-geladene-teilchen-e-feld.html`

Quelle: `inhalte/physik-q1-geladene-teilchen-e-feld.md`. Referenz: `module/physik-q1-induktion.html` (nur lesen).
Notation und `sonder`-Auswertung: `module/physik-q1-elektrisches-feld.html` (nur gelesen).

## Vorgehen (Sitzungslimit-Schutz)

Der Bau laeuft ueber Teildateien im Scratchpad (`bau/*.src`, Formeln als Kurzmarkup) und ein
Zusammenbau-Skript `bau/bau.py`, das die fertige Datei `module/...html` erzeugt. Die Auslieferung
ist eine einzelne HTML-Datei; Skript und Teile sind nur Werkzeug und liegen nicht im Projekt.

## Historische Angaben (Auftrag: per WebSearch pruefen)

WebSearch war in dieser Sitzung **nicht verfuegbar** (Werkzeug gesperrt). Ich habe die Sperre nicht ueber
Bash/curl umgangen. Deshalb nichts als belegt behandelt:

- Millikans Wert von 1913 (1,59·10⁻¹⁹ C, 0,6 % unter dem heutigen Wert): **nicht belegt** -> im Modul nur
  noch vorsichtig formuliert (Abweichung "im Bereich von Bruchteilen eines Prozents bis etwa 1 %").
- Deutung ueber die Luftviskositaet: **nicht belegt** -> als "haeufig genannte Ursache" formuliert, ohne
  Behauptung ueber die Rolle einzelner Personen.
- Mittlere freie Weglaenge 68 nm: im Modul steht nur "rund 0,07 µm" (Groessenordnung, gaengiger
  Lehrbuchwert), die Zahl 68 nm steht nicht im Text.
- Cunningham-Korrektur "8,5 %" / Ladung "13 %": haengt an den Koeffizienten der Fachdidaktik-Formel
  (nicht geprueft) -> im Modul "etwa 8 bis 9 %", Ladung "gut 12 %", Radius "rund 4 %". Groessenordnung
  bleibt, exakte Prozentwerte entfallen.
- Millikan-Beginn 1909 und Zahnarzt-Roentgenroehre 65 kV: allgemein bekannt/plausibel, unveraendert.

## Fortschritt

FORTSCHRITT: Quellen gelesen, Plan steht. Noch nichts gebaut.
FORTSCHRITT: Bauwerkzeug (bau.py) und Teile kopf, s1 (Einstieg), s2 (Erklaerteil), s3 (Vertiefung) geschrieben. Offen: s4 Simulation-Markup, sim.src, daten.src, s5 Uebungen, s6 Abschluss, zuo/namen, Zusammenbau, Tests, Modulcheck.
FORTSCHRITT: s4 (Sim-Markup), sim.src (JS Sim komplett), daten.src (mcDaten/numDaten), zuo.src, namen.src geschrieben. Offen: s5 Uebungen, s6 Abschluss+Lehrerteil, Zusammenbau, Tests, Modulcheck.
FORTSCHRITT: s5 (Uebungen ue1-ue9, drei Hilfeknoepfe auch bei ue7-9) geschrieben. Offen: s6 Abschluss+Lehrerteil, Zusammenbau, Tests, Modulcheck.
FORTSCHRITT: s6 (Abschluss, Lehrerteil) geschrieben. Alle Teile da. Offen: Zusammenbau (bau.py), Tests (Playwright, Handrechnung Sim), Modulcheck.
FORTSCHRITT: Zusammenbau OK (1802 Zeilen). Offen: Modulcheck, Sim-Handrechnung per Playwright, Screenshots.
FORTSCHRITT: Bau komplett, modulcheck bis auf Querscrollen 390 px (117 px) sauber; suche Ursache. Danach Sim-Handrechnung.
Ursache Querscrollen 390: KaTeX-mathml (absolut) in Tabellen mit vielen Formeln ragt aus .tabelle heraus; Abhilfe: .tabelle{position:relative} (einzige CSS-Ergaenzung ausser Touch-Block).
FORTSCHRITT: FERTIG gebaut. modulcheck blocker [], maengel []. Sim gegen Handrechnung (Python) und Spec: Start 26523,2 km/s / 2,26 ns / +2,25 / +17,25 / +4,29 / 8,85 %; Proton 618,9 km/s 96,95 ns -17,25; alpha 439,2 km/s 136,62 ns; Elektron 4 kV 37509,5 km/s, +8,63 mm, 12,51 %/12,44 %/0,6 %; Treffer bei 2,0 cm; Regler 100/200/320/1000/2000/5000/10000/65000/100000 V; Millikan T1-T4 v_s 105,39/127,52/85,36/151,76 µm/s; T1 374 V -0,02, 375 V +0,26, 500 V +35,48, 748 V +105,35, 1000 V +176,34; T2 300 V +0,54 (Kraefte -4,79/+4,81/-0,02, Summe 0,00). sonder-Texte ue1/ue5/ue6, Alt-Einheiten geprueft; ue7-9 Tipp+Ansatz+Loesung nebeneinander funktionieren. Modulliste NICHT auf fertig gesetzt. Offen: Entscheidung Nutzer zu ue7-9 (3 Knoepfe wie Inhaltsdatei vs. nur Musterloesung wie Referenz); historische Angaben (WebSearch gesperrt) vorsichtig formuliert.
FORTSCHRITT: Nutzerentscheidung umgesetzt: ue7-9 nur noch Knopf 'Musterloesung anzeigen' (Referenzlinie), Tipp/Ansatz samt Texten aus HTML und Inhaltsdatei (5-Einleitung, 5.7-5.9, Checkliste Tabelle/Hilfestufen/Punkt 9) sowie Lehrerteil-Absatz entfernt. modulcheck blocker [], maengel []. Modulliste nicht auf fertig.
FORTSCHRITT: Nacharbeit gestartet (Pruefberichte fach+technik). Noch nichts erledigt.
FORTSCHRITT: bau.py: S1 (Entities), Technik 9 (Unicode-Indizes), Technik 10 (Singular), M11 (CSS-Kommentar), Touch-CSS (44 px) erledigt. Offen: S2, M1, M2-M10 in Quellteilen, Sim (kk, Pause, Ruheband, M4/M5), Inhaltsdatei-Spiegel, KaTeX-Pruefung, Modulcheck.
FORTSCHRITT: Quellteile geaendert: S2, M1 (s2/s6), M2 (sim1 Proton 500 V Grenze 110 V/-75,90 mm; sim2 Troepfchen 3 bei 300 V = -22,76 µm/s, Ruheband 0,2), M3, M4, M5, M6-M10, Technik 1-5 (kk 2,4, Diagrammhoehe, Pause). Offen: Tests (Sim-Werte, KaTeX-Fehler mit Netz, 390px-Screenshots), Inhaltsdatei spiegeln, Modulcheck.
FORTSCHRITT: Nacharbeit komplett. S1: Ursache doppelte Entity-Maskierung (esc() auf bereits maskierte Quelle); bau.py entmaskiert vor dem einmaligen Escapen. KaTeX-Pruefung mit Netz (Playwright, echtes KaTeX 0.16.9): 486 .katex gerendert, 0 .katex-error, 0 Formeln ohne Render. S2 ue3-Feedback korrigiert. M1: tan θ und Y vorzeichenbehaftet (Formelkasten 2.4, Herleitung Schritt 6/7, Merksatz, |Y|=S·|U_A|); Betrag nur in ue5/ue4. M2: sim1 = Proton, 500 V, U_A ab +100 V in 5-V-Schritten: Grenze 110 V (y_a −9,90 mm, Y −75,90 mm, θ −18,26°), 115 V Treffer bei 5,9 cm; sim2 = Troepfchen 3 bei 300 V: v_s 85,36 µm/s, U_s 409,05 V, v = −22,76 µm/s (Distraktor 62,6 = 85,36·300/409,05); alle Werte per Python und im Browser abgelesen; Feedback nennt Anzeigewerte. M3: Ruheband 0,2 µm/s (T2 ruht ab 299 V, T4 ab 485 V, T1 374 V), Auftrag umformuliert. M4 Halbsatz in aVc, M5 Beschriftung 'Feldlinien E', M6 4,805e-19 C, M7 rund 13 %, M8 Vorwissen 1-3 nummeriert, M9/M10 Einstieg (Radius, Schweben/Steigen-Sinken; Millikan 1,592e-19 C laut Pruefbericht belegt), M11 Kommentar. Technik 1: kk() bis 2,4, Diagramme 360 px hoch bei schmaler Anzeige, Millikan-Bild ohne Datenblock/Pfeilnotiz bei schmal; Technik 2-4: Touch-CSS (Regler/Selects/Labels 44 px, Radios/Checkboxen 24 px); Technik 5: Pause-Knopf (bPause), im Auftrag und Lehrerteil erwaehnt; Technik 9: Unicode-Indizes im data-plain (U_B bleibt); Technik 10: 'Es fehlt noch 1 Zuordnung.'. Technik 6/7/8 zur Kenntnis. Inhaltsdatei gespiegelt (2.4, 3.3, 4.2-4.9, Lehrerteil, Namensliste, Checkliste). Modulcheck: blocker [], maengel [], kein Querscrollen 1280/900/390. Modulliste unberuehrt.
FORTSCHRITT: Restmaengel Gegenpruefung: R1 Export-Namen sim1/sim2 (Grenzspannung am Plattenpaar / Sinken bei Teilspannung) im Modul; R2 sim2-Feedback 'bei 409 V und 410 V', Lehrerteil Doppelfenster T3; R3 Kraftpfeile auseinandergelegt (±70 px, Labels zentriert), 390-px-Screenshot geprueft; R5 bei aktiver Pause wird animT nicht mehr zurueckgesetzt (getestet: Bild bleibt statisch); R6 Inline-Groesse der Modus-Radios entfernt (gemessen 24x24, Label 44 px hoch); R9 ue7/ue4/Lehrerteil auf Betrag bzw. |Y| = S·|U_A|; R10 unveraendert gelassen (schmales Leerzeichen wird bei Einheiten durchgehend gesetzt). Inhaltsdatei gespiegelt. Modulcheck blocker [], maengel [], kein Querscrollen; KaTeX mit Netz: 486 .katex, 0 .katex-error. Modulliste unberuehrt.
