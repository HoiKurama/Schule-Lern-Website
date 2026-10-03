# Doppelspalt und Gitter — Inhaltsprotokoll

Stand: gebautes Modul `module/physik-q1-doppelspalt-gitter.html` (Physik LK Q1, Chip „Inhaltsfeld: Schwingende Systeme und Wellen“,
ca. 120 Minuten). Modulcheck ohne Blocker und Mängel, 389 von 389 Formeln gesetzt, kein Querscrollen bei 390, 900 und 1280 px.
Gebaut auf der Vorlage `physik-q1-mechanische-schwingungen.html`, Bauskript wie beim Wellen-Modul (sechs Teildateien).

## Aufbau

| Abschnitt | Inhalt |
|---|---|
| 1 Einstieg | Laserpointer, Haar, CD-Farben (Spurabstand etwa 1,6 µm); Details: Warum sprechen dunkle Stellen für Wellen; vw1 Gangunterschied 2,5 λ (Auslöschung), vw2 λ = c/f für Licht, vw3 arctan |
| 2 Wellen in der Ebene (`grundlagen`) | Kreiswellen, Wellenfront, ebene Welle; Huygens’sches Prinzip, Beugung (Abb. 1: breiter und schmaler Spalt), Schall um die Hausecke; zwei Quellen, Δs = \|r₂ − r₁\|, Beispiel 2 cm; Details: Hyperbeln, Zahl der Linien nλ < d; Kohärenz |
| 3 Doppelspalt (`doppelspalt`) | Aufbau (Tabelle g, e, a_n, α_n, n), Elementarwellen aus zwei Spalten, Fernfeld, Δs = g·sin α (Abb. 2), Maxima und Minima, Tabelle der Ordnungen, a_n = n·λ·e/g, Δa = λ·e/g; Details: Näherung sin α ≈ tan α, Intensität I = I_max·cos²(π·g·sin α/λ) und Einhüllende; Wellenlängenmessung |
| 4 Gitter (`gitter`) | d = 1/z, Hauptmaxima d·sin α = n·λ (gleiche Bedingung wie beim Doppelspalt), höchste Ordnung nλ < d, Schärfe der Maxima (Zeiger, erstes Minimum bei d·sin α = λ/N), Spektren bei weißem Licht (Abb. 3, Überlappung ab 2. Ordnung), Wellenlängenmessung, CD und Röntgenstrahlen |
| 5 Simulation | Drei Einstellungen, siehe unten |
| 6 Übungen | a1 bis a7; a3 ist die Zuordnungsaufgabe (Intensitätsverteilungen) |
| 7 Abschluss | Zusammenfassung, Zentralabitur-Hinweis, Selbstcheck, Export und Druck, Lehrerteil |

Formelleiste: 5 Einträge in drei Gruppen (gang · maxima, minima · gitter, gitterk), `abschnitt`-Ids `grundlagen`, `doppelspalt`, `gitter`.
Nicht drin: a_n = n·λ·e/g (a1 und sim2), die Kleinwinkelnäherung, nλ < d (sim1 und a4), Intensitätsformeln, Δs = g·sin α.

## Simulation

Zwei Canvas: `cvW` (oben, 1000 × 400), `cvU` (unten, nur in der Einstellung „Zwei Quellen“).

| Einstellung | Modell | Besonderheit |
|---|---|---|
| Zwei Quellen | Wellenwanne mit λ = 2,0 cm, f = 1,0 Hz, Wand mit zwei Öffnungen (d 2–12 cm), Feld = (sin(ωt − k·r₁) + sin(ωt − k·r₂))/2 auf einem Raster aus 8-Pixel-Zellen | Verstärkungslinien (Gold) und Auslöschungslinien (gestrichelt) als Hyperbeln, Messpunkt P (zwei Regler), unten Zeitverlauf der Teilwellen und der Summe an P |
| Doppelspalt | I = sinc²(π·b·sin α/λ)·cos²(π·g·sin α/λ), sin α = a/√(a² + e²), Fenster ±50 mm | Regler λ 400–750 nm, g 0,10–0,50 mm, e 1–5 m, b 0,02–0,08 mm; Schirmbild in der Farbe der Wellenlänge, Kurve, Einhüllende einblendbar, Ordnungen beschriftet |
| Gitter | I = sinc²(π·0,2·d·sin α/λ)·[sin(Nδ)/(N·sin δ)]², δ = π·d·sin α/λ, Fenster ±60° | Regler Striche je mm 200–800, N 2–12, λ; „Weißes Licht“: 31 Wellenlängen 400–700 nm, Helligkeit × 5, drei Kurven (650, 540, 450 nm) |

Anzeigen je Einstellung (Wellenwanne: d, Richtungen der Verstärkungslinien, r₁, r₂, Δs, Ergebnis an P, Amplitude der Summe;
Doppelspalt: λ, g, e, a₁, α₁; Gitter: d, höchste Ordnung, α₁ bis α₃).
Gegengeprüft mit `simtest.py` im Browser: Wellenwanne sechs Einstellungen (r₁, r₂, Δs, Amplitude 2·|cos(π·Δs/λ)|, Zahl der Linien), Lage der
Maxima im Schirmbild bei sechs Einstellungen des Doppelspalts (Abweichung höchstens 0,17 mm bei einem Pixel von 0,11 mm; Maxima mit stark gedämpfter Einhüllende nicht ausgewertet) und sechs Einstellungen des Gitters
(bei N ≥ 5 höchstens 0,33°, bei N = 12 höchstens 0,06°; bei kleinem N verschiebt die Einhüllende die Maxima geringfügig), Winkel der
Ordnungen und höchste Ordnung, Farbreihenfolge bei weißem Licht (Violett innen, Rot außen, Mitte weiß), Reglerlauf in allen Einstellungen
ohne NaN, keine Konsolenfehler.

## Aufgabenzahlen (nachgerechnet, `zahlen.py`)

| Aufgabe | Ergebnis |
|---|---|
| vw1 | Δs = 4,25 m − 3,00 m = 1,25 m = 2,5 λ: Auslöschung |
| vw2 | λ = 3,0·10⁸ / 5,0·10¹⁴ = 6,0·10⁻⁷ m |
| vw3 | arctan(0,30/2,0) = 8,5° |
| a1 | g = 0,25 mm, λ = 500 nm, e = 4,0 m: Δa = 8,0 mm |
| a2 | 300 Striche/mm, 2. Ordnung bei 22,0°: λ = 624 nm |
| a3 | Gitter N = 6 → B; Doppelspalt 2g → A; Referenz → D; 1,5 λ → C |
| a4 | 600 Striche/mm, 633 nm: α₂ = 49,4°, 3. Ordnung existiert nicht (sin = 1,14) |
| a5 | 500 Striche/mm, e = 2,00 m, 1. Ordnung 400 bis 700 nm: 0,408 m bis 0,747 m, Breite 0,339 m (mit sin statt tan 0,30 m) |
| sim1 | d = 7,0 cm, λ = 2,0 cm: n ≤ 3, also 7 Verstärkungslinien |
| sim2 | g 0,20 → 0,40 mm bei 500 nm, 2,0 m: Δa 5,0 → 2,5 mm |
| sim3 | Rot außen, Violett innen (600 Striche/mm: α₁ = 13,9° bis 24,8°) |

Rechenbeispiele im Text: λ = 633 nm, g = 0,20 mm, e = 2,0 m → Δa = 6,3 mm (α₁ = 0,18°); Messbeispiel g = 0,25 mm, e = 3,0 m, 45,6 mm über sechs
Abstände → 633 nm; 600 Striche/mm, 633 nm: Maxima bei 0°, ±22,3°, ±49,4°; 500 Striche/mm: 1. Ordnung 11,5° bis 20,5°, 2. Ordnung 23,6° bis 44,4°,
3. Ordnung ab 36,9° ohne Rot; Natrium 589 nm → 17,1°.

## Technische Notizen

- Abbildungen als Inline-SVG im Bauskript: `@@ABB1@@` (Beugung), `@@ABB2@@` (Gangunterschied und Aufbau), `@@ABB3@@` (Spektren am Gitter),
  `@@DIAGRAMME@@` (Zuordnung, aus den Formeln berechnet, Achse in Einheiten von λ/g, gestrichelt die Maxima 1. Ordnung der Referenz).
- Das Bauskript fügt die CSS-Regel für `button[aria-pressed="true"]` im Simulationsbereich ein.
- Die Einheit „µm“ im Auswahlfeld von a2 steht im Bauskript in einer Querprüfung gegen `daten.py`.

## Offen

- Kernlehrplan: Inhaltsfeld und Jahrgang von Doppelspalt und Gitter im schulinternen Lehrplan (hier an „Schwingende Systeme und Wellen“
  angeschlossen); Pflichtstatus der Intensitätsverteilung, der Einhüllende des Einzelspalts und der Herleitung der Gitterschärfe. Keine Zitate erfunden.
- Die Beugung am Einzelspalt hat keinen eigenen Abschnitt, nur den qualitativen Teil und die Einhüllende (Minimum bei b·sin α = λ).
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
