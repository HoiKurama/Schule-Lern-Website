# Modulinhalt: Funktionsuntersuchung – Extrem- und Wendestellen, Funktionsscharen

**Dateiname des Moduls:** `module/mathe-q1-funktionsuntersuchung.html`
**Fach:** Mathematik · **Kursniveau:** Leistungskurs Q1
**Inhaltsfeld (Chip im Seitenkopf, wörtlich nach `fachliches/kernlehrplan-nrw.md`):** Funktionen und Analysis
**Weitere Chips:** „Kernlehrplan NRW, GOSt" · „ca. 130 Minuten"
**Fachzeile über der Überschrift:** Mathematik · Qualifikationsphase 1 · Leistungskurs
**Seitentitel (`<h1>`):** Funktionsuntersuchung: Extrem- und Wendestellen, Funktionsscharen
**Farbtokens:** `--akzent: #0d7a52` · `--akzent-hell: #e7f6ef` · `--akzent-rand: #b5e0cd`,
dazu der Verlauf in `header.kopf` (sonst bleibt der `<style>`-Block des Referenzmoduls unverändert).

**Voraussetzung (wird *nicht* neu eingeführt):** Ableitung als lokale Änderungsrate und
Tangentensteigung, Potenz-, Faktor- und Summenregel, Ableitung ganzrationaler Funktionen, Lösen
quadratischer Gleichungen. Aus `inhalte/mathe-q1-ableitungsregeln.md` dürfen Produkt- und
Kettenregel vorausgesetzt werden — **dieses Modul braucht sie nicht**: Alle Funktionen sind
ganzrational, abgeleitet wird mit Potenz-, Faktor- und Summenregel. Der Ausblick in 6.5 verweist
darauf, wo sie beim Untersuchen anderer Funktionsklassen ins Spiel kommen.
**Bewusst nicht vorausgesetzt:** Kenntnis der Begriffe Wendepunkt, Sattelpunkt, Krümmung,
Funktionsschar, Ortskurve. Sie werden hier eingeführt.

**Einordnung in den Kernlehrplan (siehe Abschnitt „Offene Zuordnung" im Lehrerteil):** Inhaltsfeld
*Funktionen und Analysis*; Verortung laut Projektfestlegung in Q1 („Fortführung der Analysis").
Ob die Grundlagen der Funktionsuntersuchung (Extrempunkte, Wendepunkte ganzrationaler Funktionen)
im schulinternen Lehrplan schon in der Einführungsphase liegen, ist **offen**; das Modul ist so
gebaut, dass es beides trägt (Einstieg wiederholt, Vertiefung und Scharen sind Q1-Stoff). Es
werden keine wörtlichen Kompetenzformulierungen aus dem Kernlehrplan zitiert.

**Aufbau:** sechs `<section>`-Blöcke mit nummeriertem `.stufe`-Kopf (Einstieg · Erklärteil ·
Vertiefung · Interaktiver Kern · Übungen · Abschluss); Lehrerteil und Checkliste gehören in die
sechste Section bzw. sind Bauanleitung.

**Kontrollrechnungen:** Alle Zahlenwerte dieser Datei wurden mit `sympy` (exakte Brüche) und
numerisch geprüft; Ergebnisse stehen in Abschnitt 0, das Kontrollskript am Dateiende.

---

## 0 · Kontrollrechnungen (Sammelstelle)

**K1 — Vorwissen**
`vw1`: f(x) = x⁴ − 2x³ + 5x ⟹ f′(x) = 4x³ − 6x² + 5 · f″(x) = **12x² − 12x** = 12x(x − 1).
Distraktoren: 4x³ − 6x² + 5 (erste Ableitung) · 12x² − 12x + 5 (Konstante nicht gestrichen).
`vw2`: 3x² − 12x + 9 = 0 ⟹ x² − 4x + 3 = 0 ⟹ **x = 1 oder x = 3**. Distraktor „x = −1, x = −3": Vorzeichenfehler
der pq-Formel; Distraktor „x = 2 (doppelt)": nur der Scheitel −p/2.
`vw3`: f(x) = x² − 4x: f(3) = **−3** · f′(x) = 2x − 4 ⟹ f′(3) = **2** · f′(2) = 0 (Tiefpunkt bei x = 2, f(2) = −4).

**K2 — Erklärteil, durchgängiges Beispiel f(x) = x⁴ − 4x³ + 4x² = x²(x − 2)²** (sympy, exakt)
f′(x) = 4x³ − 12x² + 8x = **4x(x − 1)(x − 2)** · f″(x) = 12x² − 24x + 8 = **4(3x² − 6x + 2)** · f‴(x) = **24(x − 1)**.
Nullstellen von f: **x = 0 und x = 2, beide doppelt** (f ≥ 0 überall).
f′ = 0 bei x = **0, 1, 2**. f″(0) = **8** > 0 ⟹ Tiefpunkt T₁(0 | 0) · f″(1) = **−4** < 0 ⟹ Hochpunkt H(1 | 1) · f″(2) = **8** > 0 ⟹ Tiefpunkt T₂(2 | 0).
f″ = 0 bei x = 1 ∓ √3/3 = **0,4226** und **1,5774**; f‴ dort = ∓8√3 ≈ **∓13,856** ≠ 0 ⟹ beides Wendestellen.
Wendepunkte: W₁(1 − √3/3 | **4/9**) und W₂(1 + √3/3 | **4/9**), 4/9 ≈ 0,4444.
Steigung der Wendetangenten: f′(1 − √3/3) = **8√3/9 ≈ +1,5396** · f′(1 + √3/3) = **−1,5396**.
Symmetrie: f(2 − x) − f(x) = **0** (achsensymmetrisch zur Geraden x = 1) — Wertetabelle:
f(−1) = 9 · f(0) = 0 · f(0,5) = 9/16 = 0,5625 · f(1) = 1 · f(1,5) = 0,5625 · f(2) = 0 · f(3) = 9.
Kontrolle Symmetrie: f(−1) = f(3) = 9 ✓ · f(0,5) = f(1,5) ✓.

**K3 — Erklärteil, Fehlvorstellung (f′ = 0 und f″ = 0 an derselben Stelle)**

| Funktion | f′(x) | f″(x) | f‴(x) | bei x = 0 |
|---|---|---|---|---|
| x⁴ | 4x³ (− → +) | 12x² (≥ 0, kein VZW) | 24x | Tiefpunkt, **kein** Wendepunkt |
| −x⁴ | −4x³ (+ → −) | −12x² (≤ 0, kein VZW) | −24x | Hochpunkt, **kein** Wendepunkt |
| x³ | 3x² (≥ 0, kein VZW) | 6x (− → +) | 6 | Sattelpunkt = Wendepunkt mit waagerechter Tangente |
| x⁵ | 5x⁴ (≥ 0, kein VZW) | 20x³ (− → +) | 60x² | Sattelpunkt (Wendepunkt), f‴(0) = 0 trotzdem |

Vorzeichenproben: f′ von x⁴ bei x = ∓1: −4 / +4 ✓ · f″ von x³ bei x = ∓1: −6 / +6 ✓ · f″ von x⁴ bei x = ∓1: 12 / 12 (kein VZW) ✓.
Merke: x⁵ zeigt, dass f‴(x₀) ≠ 0 **hinreichend, aber nicht notwendig** für eine Wendestelle ist.

**K4 — Herleitung der f″-Bedingung, Zahlenprobe am Beispiel K2**
f″(x₀) = lim_{h→0} [f′(x₀ + h) − f′(x₀)]/h; bei f′(x₀) = 0 ist das lim f′(x₀ + h)/h.
Bei x₀ = 0 (f″(0) = 8): f′(0,1) = 4·0,1·(−0,9)·(−1,9) = **0,684** > 0 · f′(−0,1) = 4·(−0,1)·(−1,1)·(−2,1) = **−0,924** < 0.
Differenzenquotient f′(0,1)/0,1 = **6,84** (→ 8 für h → 0) ✓; f′(−0,1)/(−0,1) = **9,24** (→ 8) ✓.
VZW bei x₀ = 0 von − nach + ⟹ Tiefpunkt, stimmt mit f″(0) = 8 > 0 überein.

**K5 — Vertiefung, Schar f_t(x) = x³ − 3t·x²** (sympy)
f_t′(x) = 3x² − 6t·x = **3x(x − 2t)** · f_t″(x) = **6(x − t)** · f_t‴ = 6.
Extremstellen x = 0 und x = 2t. f_t(0) = 0 · f_t(2t) = **−4t³**. f_t″(0) = **−6t** · f_t″(2t) = **6t**.
Wendestelle x = t, f_t(t) = **−2t³**, Wendepunkt W_t(t | −2t³); Steigung der Wendetangente f_t′(t) = **−3t²**.
Fälle: t > 0: H(0 | 0), T(2t | −4t³) · t < 0: T(0 | 0), H(2t | −4t³) · t = 0: f₀(x) = x³, Sattelpunkt (0 | 0).
Zahlenproben: t = 2: f = x³ − 6x²: H(0|0), T(4 | −32), W(2 | −16) ✓ · t = −1: f = x³ + 3x²: T(0|0), H(−2 | 4), W(−1 | 2) ✓.
Ortskurve der Wendepunkte: x = t, y = −2t³ ⟹ **y = −2x³**. Ortskurve der Extrempunkte (ohne den festen Punkt (0|0)):
aus f_t′(x) = 0, x ≠ 0 ⟹ t = x/2, eingesetzt y = −4t³ = **−x³/2**. Probe t = 2: T(4 | −32): −64/2 = −32 ✓.

**K6 — Simulation: die drei Scharen (Formeln, Ableitungen; symbolisch bestätigt, Punktformeln für a = −1 … 4 in Schritten 0,05 gegen sympy geprüft, 0 Abweichungen)**

| Schar | f_a(x) | f_a′(x) | f_a″(x) | f_a‴(x) |
|---|---|---|---|---|
| 1 | x³/3 − a·x | x² − a | 2x | 2 |
| 2 | x³/3 − x² + a·x | x² − 2x + a | 2(x − 1) | 2 |
| 3 | x⁴/4 − a·x³/3 | x²(x − a) | x(3x − 2a) | 2(3x − a) |

Punktformeln (die Bauvorlage für die Markierungen; alle Formeln gegen sympy bestätigt):
- **Schar 1**, a > 0: H(−√a | +(2/3)·a·√a), T(+√a | −(2/3)·a·√a); a ≤ 0: keine Extrempunkte. Wendepunkt immer W(0 | 0), Steigung der Wendetangente −a. a = 0: f′ = x², Sattelpunkt (0|0).
- **Schar 2**, a < 1: H(1 − s | f(1 − s)), T(1 + s | f(1 + s)) mit s = √(1 − a); f(x) wie oben. a = 1: f′ = (x − 1)² ≥ 0, **Sattelpunkt** (1 | 1/3); a > 1: keine Extrempunkte. Wendepunkt immer W(1 | a − 2/3), Steigung der Wendetangente **a − 1**.
- **Schar 3**, a ≠ 0: Tiefpunkt T(a | −a⁴/12); bei x = 0 f′ = f″ = 0 mit doppelter Nullstelle von f′ ⟹ Sattelpunkt S(0 | 0) (f‴(0) = −2a ≠ 0); zweiter Wendepunkt W(2a/3 | −4a⁴/81), Steigung dort a=1: −0,1481. a = 0: f = x⁴/4, Tiefpunkt (0|0) mit f′ = f″ = f‴ = 0 und **kein** Wendepunkt.

**K7 — Simulation: Startzustände und Testfälle** (`fmt` mit zwei Nachkommastellen)

| Fall | Werte |
|---|---|
| Schar 1, a = 1,00, x₀ = 2,00 (Start) | f = **0,67** · f′ = **3,00** · f″ = **4,00** · H(−1,00 \| 0,67) · T(1,00 \| −0,67) · W(0,00 \| 0,00), m_W = **−1,00** |
| Schar 1, a = 4,00, x₀ = 2,00 | f = **−5,33** · f′ = **0,00** · f″ = **4,00** · H(−2,00 \| 5,33) · T(2,00 \| −5,33) · m_W = **−4,00** |
| Schar 1, a = 2,25 | H(−1,50 \| 2,25) · T(1,50 \| −2,25) |
| Schar 1, a = 0,00 | keine H/T; f′ = x², Sattelpunkt (0,00 \| 0,00), m_W = 0,00 |
| Schar 1, a = −1,00 | keine H/T; W(0,00 \| 0,00), m_W = **+1,00** |
| Schar 2, a = −0,50, x₀ = 2,50 (Start) | f = **−2,29** · f′ = **0,75** · f″ = **3,00** · H(−0,22 \| 0,06) · T(2,22 \| −2,39) · W(1,00 \| −1,17), m_W = **−1,50** |
| Schar 2, a = −1,00 | H(−0,41 \| 0,22) · T(2,41 \| −3,55) · W(1,00 \| −1,67), m_W = −2,00 |
| Schar 2, a = 0,00 | H(0,00 \| 0,00) · T(2,00 \| −1,33) · W(1,00 \| −0,67), m_W = −1,00 |
| Schar 2, a = 0,50 | H(0,29 \| 0,07) · T(1,71 \| −0,40) · W(1,00 \| −0,17), m_W = −0,50 |
| Schar 2, a = 0,95 | H(0,78 \| 0,29) · T(1,22 \| 0,28) · W(1,00 \| 0,28), m_W = **−0,05** |
| Schar 2, a = 1,00 | **Sattelpunkt** (1,00 \| 0,33), m_W = **0,00**, keine H/T |
| Schar 2, a = 1,05 | keine H/T, W(1,00 \| 0,38), m_W = **+0,05** |
| Schar 2, a = 2,00 | keine H/T, W(1,00 \| 1,33), m_W = +1,00 |
| Schar 3, a = 1,00, x₀ = 2,00 (Start) | f = **1,33** · f′ = **4,00** · f″ = **8,00** · T(1,00 \| −0,08) · S(0,00 \| 0,00) · W(0,67 \| −0,05) |
| Schar 3, a = −1,00 | T(−1,00 \| −0,08) · S(0,00 \| 0,00) · W(−0,67 \| −0,05) |
| Schar 3, a = 2,00 | T(2,00 \| −1,33) · S(0,00 \| 0,00) · W(1,33 \| −0,79) |
| Schar 3, a = 0,00 | nur T(0,00 \| 0,00) mit f′(0) = f″(0) = 0,00; **kein** Sattelpunkt, kein Wendepunkt |

Konsistenzproben in der Sim: Bei Schar 2 gilt f″(x₀ = 1) = 0,00 für **jedes** a (Wendestelle fest bei x = 1).
Bei Schar 3 gilt f′(0) = f″(0) = 0,00 für jedes a.

**K8 — Ortskurven der drei Scharen (Spur-Schalter der Simulation)**
Schar 1: aus f′ = 0 folgt a = x², eingesetzt **y = −(2/3)x³** (gilt für H und T, x ∈ [−2; 2]). Proben: a = 1: T(1 | −0,667) ✓ · a = 4: T(2 | −5,333) ✓ · a = 2,25: T(1,5 | −2,25) ✓ · H(−1,5 | +2,25) ✓.
Schar 2: aus f′ = 0 folgt a = 2x − x², eingesetzt **y = x² − (2/3)x³** (H und T). Proben: a = 0: T(2 | −1,333): 4 − 16/3 = −1,333 ✓ · a = −0,5: H(−0,2247 | 0,05808) ✓ (x² = 0,05051, −(2/3)x³ = +0,00757, Summe 0,05808).
Wendepunkte von Schar 2: **x = 1 (senkrechte Gerade)**, y = a − 2/3 läuft von −1,667 (a = −1) bis +3,333 (a = 4).
Schar 3: Tiefpunkt **y = −x⁴/12**; zweiter Wendepunkt (a = 3x/2 eingesetzt) **y = −x⁴/4**; Sattelpunkt fest bei (0|0).
Wichtig: Diese Gleichungen dürfen **nirgends in der Simulation als Text stehen** (sonst ist Verständnisfrage `sim1` ablesbar).

**K9 — Simulation: Fenster und Reglerbereiche (alle Markierungen bleiben im Fenster; Skript-Ergebnis)**

| Schar | x-Fenster | y-Fenster (f) | a-Bereich | Wertebereich der Markierungen |
|---|---|---|---|---|
| 1 | −3 … 3 | −6 … 6 | −1,00 … 4,00 | x ∈ [−2; 2], y ∈ [−5,33; 5,33] |
| 2 | −2 … 4 | −4 … 6 | −1,00 … 4,00 | x ∈ [−0,41; 2,41], y ∈ [−3,55; 3,33] |
| 3 | −2 … 3 | −2 … 3 | −1,00 … 2,00 | x ∈ [−1; 2], y ∈ [−1,33; 0] |

Wertebereiche von f′ und f″ (Prüfung des Ableitungsfensters): Schar 1: f′ ∈ [−4; 10], f″ ∈ [−6; 6] · Schar 2: f′ ∈ [−2; 12], f″ ∈ [−6; 6] · Schar 3: f′ bis 36, f″ bis 33 (dort wird geklippt, das ist gewollt).
Ableitungsfenster (cvAbl): Schar 1: −6 … 10 · Schar 2: −6 … 12 · Schar 3: −3 … 6; Kurven außerhalb werden abgeschnitten.

**K10 — Übung `a1`: f(x) = x³ − 6x² + 9x − 4 = (x − 4)(x − 1)²**
f′ = 3x² − 12x + 9 = 3(x − 1)(x − 3) · f″ = 6x − 12 · f″(1) = −6 (Hochpunkt H(1 | **0**)) · f″(3) = +6 (Tiefpunkt T(3 | **−4**)).
f(3) = 27 − 54 + 27 − 4 = **−4** ✓ · f(1) = 1 − 6 + 9 − 4 = 0 ✓.
Distraktoren: 0 (Hochpunkt gemeint), 3 (Stelle statt Wert).

**K11 — Übung `a2`: f(x) = x³ − 6x² + 5x**
f′ = 3x² − 12x + 5 · f″ = 6x − 12 = 0 ⟹ x_W = **2** · f‴ = 6 ≠ 0 · f(2) = 8 − 24 + 10 = **−6** · f′(2) = 12 − 24 + 5 = **−7**.
Steigungswinkel arctan(−7) = **−81,87°** (Distraktor Einheit „°"). Distraktoren: −6 (Funktionswert, `nah`), 5 (f′(0)), 2, +7.

**K12 — Übung `mc1`: f(x) = ½x⁴ − 4x³ + 9x² − 5**
f′ = 2x³ − 12x² + 18x = **2x(x − 3)²** · f″ = 6x² − 24x + 18 = **6(x − 1)(x − 3)** · f‴ = 12x − 24.
f′(3) = 0, f″(3) = 0, f‴(3) = **12 ≠ 0**; f(3) = 8,5 = 17/2. Vorzeichen von f′ bei x = 2,9 / 3,1: **+0,058 / +0,062** (kein VZW) ⟹ kein Extremum.
Vorzeichen von f″ bei 2,9 / 3,1: −1,14 / +1,26 (VZW) ⟹ Wendepunkt (3 | 8,5) mit waagerechter Tangente = **Sattelpunkt**.
Weitere Punkte: f″(0) = 18 > 0 ⟹ T(0 | −5) · Wendestelle x = 1: W(1 | 0,5), f′(1) = 8.

**K13 — Übung `a3`: Pegel h(t) = 0,1·(t³ − 6t² + 9t) in m, t in Tagen, 0 ≤ t ≤ 5**
h′ = 0,3(t − 1)(t − 3) · lokales Maximum t = 1: h = **0,4 m** (h″(1) = −0,6) · lokales Minimum t = 3: h = **0** (h″(3) = +0,6).
Ränder: h(0) = 0 · h(5) = 0,1·(125 − 150 + 45) = **2,0 m**. Globales Maximum auf [0; 5] am **Rand t = 5**: **2,0 m**.

**K14 — Übung `a4`: Bestand B(t) = −0,02t³ + 0,6t², t in Tagen, 0 ≤ t ≤ 20, B in cm**
B′ = −0,06t² + 1,2t = 0,06t(20 − t) · B″ = −0,12t + 1,2 = 0 ⟹ t = **10** · B‴ = −0,12 < 0 ⟹ Maximum von B′.
B′(10) = −6 + 12 = **6 cm/Tag** · B′(0) = B′(20) = 0 (Ränder) ⟹ 6 ist auch das globale Maximum von B′ auf [0; 20].
B(10) = −20 + 60 = 40 cm · B(20) = −160 + 240 = 80 cm · B(0) = 0.

**K15 — Übung `a5`: f_a(x) = x³ − 6x² + a·x**
f_a′ = 3x² − 12x + a, Diskriminante 144 − 12a = 0 ⟹ **a = 12** ⟹ f₁₂′ = **3(x − 2)²**, Sattelpunkt (2 | 8), f″(2) = 0.
a = 9: f′ = 3(x − 1)(x − 3), zwei Stellen · a = 13: f′ > 0, gar keine · a = 11: Diskriminante 12 > 0, zwei Stellen.
Distraktoren: 9 (Extrempunkt bei x = 1), 4 (aus x² − 4x + a = 0 mit „Diskriminante 16 − 4a", Faktor 3 nicht in a mitgeführt), 36 (Diskriminante 144 − 4a, Faktor 3 vergessen).

**K16 — Übung `z1`: vier Graphen von f′** (siehe Abschnitt 5, SVG-Vorgabe)
A: f′ = −x (f = −x²/2: Hochpunkt (0|0), f″ = −1, kein Wendepunkt) ·
B: f′ = x³ − x (f = x⁴/4 − x²/2: drei Extremstellen −1, 0, 1, f″ = 3x² − 1 = 0 bei ∓0,577: zwei Wendestellen) ·
C: f′ = x² − 1 (f = x³/3 − x: H(−1 | 2/3), T(1 | −2/3), W(0 | 0)) ·
D: f′ = x² (f = x³/3: Sattelpunkt (0|0), keine Extrempunkte).
Lösung: Z1 zwei Extrempunkte + ein Wendepunkt → **C** · Z2 drei Extrempunkte + zwei Wendepunkte → **B** · Z3 waagerechte Tangente ohne Extrempunkt → **D** · Z4 genau ein Hochpunkt, keine Wendepunkte → **A**. Lösungsfolge **C · B · D · A**.

**K17 — Übung `a6`: Schülerlösung zu f(x) = x⁴ − 4x³**
f′ = 4x³ − 12x² = **4x²(x − 3)** · f″ = 12x² − 24x = **12x(x − 2)** · f‴ = 24x − 24 = 24(x − 1).
f′ = 0 bei x = 0 und x = 3. f″(3) = **36** > 0 ⟹ Tiefpunkt T(3 | **−27**) ✓ (f(3) = 81 − 108 = −27).
x = 0: f′(0) = 0, f″(0) = 0 ⟹ f″ entscheidet nichts. f′ bei x = −0,1: **−0,124**, bei x = 0,1: **−0,116** ⟹ **kein VZW**, kein Extremum.
f″ = 0 bei x = 0 und x = 2; f‴(0) = **−24** ≠ 0, f‴(2) = **+24** ≠ 0 ⟹ beide Wendestellen; f″ bei ∓0,1: +2,52 / −2,28 (VZW) ✓.
Wendepunkte W₁(0 | 0) — mit f′(0) = 0 ein Sattelpunkt — und W₂(2 | **−16**), da f(2) = 16 − 32 = −16. Die Schülerin schreibt **−8** (Rechenfehler).
Steigung in W₂: f′(2) = 32 − 48 = **−16**.

**K18 — Übung `a7`: Schar f_a(x) = x³ + a·x² + x**
f_a′ = 3x² + 2a·x + 1, Diskriminante **4a² − 12** ⟹ Extremstellen genau dann, wenn a² > 3, also |a| > √3 ≈ 1,732.
|a| < √3: f_a′ > 0 (streng monoton steigend, keine Extrema); a = ±√3: doppelte Nullstelle, Sattelpunkt bei x = ∓√3/3, y = ∓√3/9 (a = √3: (−0,577 | −0,192)).
Beispiele: a = 0: f′ = 3x² + 1 > 0 · a = 1: Diskriminante −8 < 0 · a = 2: f′ = (x + 1)(3x + 1), H(−1 | 0), T(−1/3 | −4/27 = −0,148) · a = −2: H(1/3 | 4/27 = 0,148), T(1 | 0).
f_a″ = 6x + 2a = 0 ⟹ x = −a/3 für **jedes** a, f‴ = 6 ≠ 0 ⟹ Wendepunkt existiert immer, W(−a/3 | a(2a² − 9)/27).
Ortskurve der Wendepunkte: a = −3x ⟹ **y = x − 2x³** (sympy).

**K19 — Einordnung der Distraktoren in die Zonen der Zahlen-Engine** (Zone `nah`: Quotient Eingabe/Sollwert echt zwischen 0,5 und 2)
`a1` (Soll −4): 0 → weit · 3 → weit · −3 → nah · −5 → nah · 4 → weit.
`a2` (Soll −7): −6 → **nah** · −5 → nah · −8 → nah · 2 → weit · 5 → weit · 7 → weit (Quotient −1).
`a3` (Soll 2,0): 0,4 → weit · 0 → weit · 4 → weit · 1,6 → nah · 3 → nah.
`a4` (Soll 6): 10 → **nah** · 40 → weit · 80 → weit · 3 → weit · 0 → weit.
`a5` (Soll 12): 9 → **nah** · 4 → weit · 36 → weit · 6 → weit · −12 → weit.

**K20 — Übung `a8`: Schar f_t(x) = x³ − 3t²·x** (sympy: `factor(f′) = 3(x−t)(x+t)`, f″ = 6x, f(t) = −2t³, f(−t) = 2t³, f‴ = 6)
t > 0: T(t | −2t³), H(−t | 2t³) · t < 0: H(t | −2t³), T(−t | 2t³) · t = 0: f₀ = x³, f₀′ = 3x² ≥ 0, Sattelpunkt (0|0).
Ortskurve beider Extrempunkte: x = t, y = −2t³ ⟹ **y = −2x³**; x = −t, y = 2t³ = 2(−x)³ ⟹ **y = −2x³** (dieselbe Kurve).
Proben: t = 2: f = x³ − 12x, T(2 | −16), H(−2 | 16) ✓ · t = −1: f = x³ − 3x, H(−1 | 2), T(1 | −2) ✓.

---

## 1 · Einstieg

`<section id="einstieg">`, `.stufe`-Kopf: Nr. **1**, Überschrift **Einstieg**.

### 1.1 Aufhängertext (wörtlich, zwei Absätze)

> Die Passstraße steigt nicht gleichmäßig: erst eine Kuppe, dann eine Senke, dann wieder hinauf.
> Die Planerinnen zeichnen das als Höhenprofil, und sie müssen drei Dinge genau wissen. Wo liegt
> die Kuppe, wo die Senke? Wo fällt die Straße am steilsten ab? Und gibt es irgendwo ein
> waagerechtes Stück, auf dem ein beladener Lkw anfahren muss? Alle drei Fragen lassen sich am
> Graphen nur grob beantworten, mit der Ableitung aber auf den Zentimeter genau.

> Der eigentliche Haken: Das Profil steht noch nicht fest. Ein einziger Steuerwert *a*, etwa die
> Anfangssteigung am Fuß des Hangs, verändert die ganze Kurve. Für einen Teil der *a*-Werte gibt es Kuppe und Senke, für den anderen keine von beiden. Und genau zwischen beiden Bereichen liegt ein Sonderfall, bei dem die
> Tangente waagerecht ist, obwohl es weder Kuppe noch Senke gibt. „Ableitung null heißt Gipfel" ist
> also zu einfach gedacht. In dieser Einheit lernst du, Extrem- und Wendestellen sicher zu
> unterscheiden, eine Funktion vollständig zu untersuchen und das Ganze für eine ganze
> Funktionenschar auf einmal zu tun.

### 1.2 Vorwissen prüfen

Karte `.karte` mit Überschrift „Vorwissen prüfen" und dem Vorspann:
*„Drei Fragen aus der Einführungsphase und der Sekundarstufe I. Wenn du hier hängst, lohnt sich ein
Blick zurück: Für die Funktionsuntersuchung brauchst du zweite Ableitungen, quadratische
Gleichungen und ein sicheres Gefühl dafür, was f′ über den Graphen sagt."*

Drei MC-Aufgaben ohne Rahmen und ohne `.ab`-Chip (`style="border:none;padding:0"` wie im
Referenzmodul).

---

**MC `vw1`** — richtige Option: Index **1**

Frage: *Bestimme die zweite Ableitung von <span class="m" data-tex="f(x) = x^4 - 2x^3 + 5x" data-plain="f(x) = x⁴ − 2x³ + 5x"></span>.*

| Index | Option |
|---|---|
| 0 | <span class="m" data-tex="f''(x) = 4x^3 - 6x^2 + 5" data-plain="f″(x) = 4x³ − 6x² + 5"></span> |
| 1 | <span class="m" data-tex="f''(x) = 12x^2 - 12x" data-plain="f″(x) = 12x² − 12x"></span> |
| 2 | <span class="m" data-tex="f''(x) = 12x^2 - 12x + 5" data-plain="f″(x) = 12x² − 12x + 5"></span> |

Feedback:
- 0: „Das ist die **erste** Ableitung, f′(x) = 4x³ − 6x² + 5. Die zweite Ableitung ist die Ableitung von f′: Du musst dieses Ergebnis noch einmal ableiten."
- 1: „Richtig. Erst f′(x) = 4x³ − 6x² + 5, dann noch einmal: 4x³ → 12x², −6x² → −12x, und die Konstante 5 fällt weg. Faktorisiert: f″(x) = 12x(x − 1)."
- 2: „Bis 12x² − 12x stimmt alles. Die 5 in f′(x) = 4x³ − 6x² + 5 ist aber eine Konstante, und die hat die Ableitung 0. Wer sie stehen lässt, behandelt sie wie eine Variable."

---

**MC `vw2`** — richtige Option: Index **2**

Frage: *Löse <span class="m" data-tex="3x^2 - 12x + 9 = 0" data-plain="3x² − 12x + 9 = 0"></span>.*

| Index | Option |
|---|---|
| 0 | <span class="m" data-tex="x = 2" data-plain="x = 2"></span> (eine doppelte Lösung) |
| 1 | <span class="m" data-tex="x = -1" data-plain="x = −1"></span> oder <span class="m" data-tex="x = -3" data-plain="x = −3"></span> |
| 2 | <span class="m" data-tex="x = 1" data-plain="x = 1"></span> oder <span class="m" data-tex="x = 3" data-plain="x = 3"></span> |

Feedback:
- 0: „x = 2 ist nur der Scheitel der Parabel, −p/2 mit p = −4. Die Lösungen liegen um √(p²/4 − q) = √(4 − 3) = 1 links und rechts davon, also bei 1 und 3. Eine doppelte Lösung gäbe es nur, wenn die Wurzel null wäre."
- 1: „Vorzeichenfehler in der pq-Formel: x = −p/2 ± √(…) mit p = −4 ergibt +2, nicht −2. Probe: Bei x = −1 ist 3 + 12 + 9 = 24, nicht 0."
- 2: „Richtig. Erst durch 3 teilen: x² − 4x + 3 = 0, dann x = 2 ± √(4 − 3) = 2 ± 1. Probe bei x = 1: 3 − 12 + 9 = 0. Genau diese Gleichung ist die Bedingung für waagerechte Tangenten von f(x) = x³ − 6x² + 9x."

---

**MC `vw3`** — richtige Option: Index **0**

Frage: *Für <span class="m" data-tex="f(x) = x^2 - 4x" data-plain="f(x) = x² − 4x"></span> gilt <span class="m" data-tex="f'(3) = 2" data-plain="f′(3) = 2"></span>. Welche Aussage über den Graphen bei <span class="m" data-tex="x = 3" data-plain="x = 3"></span> ist richtig?*

| Index | Option |
|---|---|
| 0 | Der Graph steigt dort, obwohl er unterhalb der x-Achse verläuft. |
| 1 | Der Graph hat dort einen Tiefpunkt. |
| 2 | Der Graph liegt dort oberhalb der x-Achse, weil f′(3) positiv ist. |

Feedback:
- 0: „Richtig. f′(3) = 2 > 0 sagt: Die Tangente steigt. Über die Lage zur x-Achse sagt f′ nichts; dafür ist f(3) = 9 − 12 = −3 zuständig, und das ist negativ. Steigung und Funktionswert sind zwei verschiedene Größen."
- 1: „Ein Tiefpunkt bräuchte f′ = 0. Der Tiefpunkt dieser Parabel liegt bei x = 2, denn f′(2) = 2·2 − 4 = 0 (dort ist f(2) = −4). Bei x = 3 ist die Parabel schon wieder auf dem Weg nach oben."
- 2: „Du vermischst Ableitung und Funktionswert. f′(3) = 2 ist eine Steigung. Ob der Graph über oder unter der x-Achse liegt, entscheidet f(3) = 9 − 12 = −3 < 0, und das liegt unterhalb."

## 2 · Erklärteil

`<section id="erklaerung">`, `.stufe`-Kopf: Nr. **2**, Überschrift **Extrempunkte, Wendepunkte, Kurvendiskussion**.

### 2.1 Was f′ und f″ über den Graphen verraten

Fließtext (wörtlich):

> Die erste Ableitung <span class="m" data-tex="f'(x)" data-plain="f′(x)"></span> ist die Steigung der
> Tangente. Ist sie an einer Stelle positiv, steigt der Graph dort, ist sie negativ, fällt er.
> Die zweite Ableitung <span class="m" data-tex="f''(x)" data-plain="f″(x)"></span> ist die
> Ableitung der Steigungsfunktion, sie sagt also, **wie sich die Steigung ändert**: Ist
> <span class="m" data-tex="f''(x) > 0" data-plain="f″(x) > 0"></span>, wird die Steigung größer,
> der Graph biegt sich nach links, man spricht von einer **Linkskurve**. Ist
> <span class="m" data-tex="f''(x) < 0" data-plain="f″(x) < 0"></span>, wird die Steigung kleiner,
> und der Graph biegt sich nach rechts: eine **Rechtskurve**.

Tabelle in `<div class="tabelle">` (drei Spalten, damit sie unter 420 px nicht überläuft):

| Vorzeichen | Aussage über den Graphen | Beispiel |
|---|---|---|
| <span class="m" data-tex="f'>0" data-plain="f′ > 0"></span> | Graph steigt | Parabel <span class="m" data-tex="x^2" data-plain="x²"></span> für <span class="m" data-tex="x>0" data-plain="x > 0"></span> |
| <span class="m" data-tex="f'<0" data-plain="f′ < 0"></span> | Graph fällt | Parabel <span class="m" data-tex="x^2" data-plain="x²"></span> für <span class="m" data-tex="x<0" data-plain="x < 0"></span> |
| <span class="m" data-tex="f''>0" data-plain="f″ > 0"></span> | Linkskurve (Steigung wächst) | Parabel <span class="m" data-tex="x^2" data-plain="x²"></span> überall |
| <span class="m" data-tex="f''<0" data-plain="f″ < 0"></span> | Rechtskurve (Steigung fällt) | Parabel <span class="m" data-tex="-x^2" data-plain="−x²"></span> überall |

`.hinweis` (Begriffsklärung — Sprache ist im LK Teil der Aufgabe):

> **Vier Wörter, die du nicht durcheinanderbringen darfst.** Die **Extremstelle**
> <span class="m" data-tex="x_E" data-plain="x_E"></span> ist ein x-Wert. Der **Extremwert**
> <span class="m" data-tex="f(x_E)" data-plain="f(x_E)"></span> ist ein y-Wert. Der
> **Extrempunkt** <span class="m" data-tex="(x_E\,|\,f(x_E))" data-plain="(x_E | f(x_E))"></span> ist
> beides zusammen. „Lokal" heißt: Der Funktionswert ist nur in einer Umgebung von
> <span class="m" data-tex="x_E" data-plain="x_E"></span> der größte oder kleinste. Wer nach der
> Extremstelle fragt und den y-Wert antwortet, hat die Frage nicht beantwortet.

### 2.2 Extremstellen

Fließtext:

> Auf dem Gipfel ist die Tangente waagerecht: Vor dem Gipfel steigt der Graph, dahinter fällt er,
> und genau dazwischen muss die Steigung null sein. Das ist die **notwendige Bedingung**. Sie sagt
> aber nur, wo man suchen muss, nicht, was man findet. Dass eine waagerechte Tangente noch kein
> Extremum bedeutet, zeigt gleich Abschnitt 2.4.

`.merksatz`:

> **Extremstellen**
> **Notwendig:** Hat <span class="m" data-tex="f" data-plain="f"></span> bei
> <span class="m" data-tex="x_0" data-plain="x₀"></span> eine lokale Extremstelle, so ist
> <span class="m" data-tex="f'(x_0)=0" data-plain="f′(x₀) = 0"></span>. Die Umkehrung gilt nicht.
> **Hinreichend, Kriterium 1 (Vorzeichenwechsel):** Wechselt
> <span class="m" data-tex="f'" data-plain="f′"></span> bei <span class="m" data-tex="x_0" data-plain="x₀"></span>
> das Vorzeichen, so liegt bei Wechsel von + nach − ein **Hochpunkt**, bei Wechsel von − nach + ein **Tiefpunkt** vor.
> **Hinreichend, Kriterium 2 (zweite Ableitung):** Aus
> <span class="m" data-tex="f'(x_0)=0" data-plain="f′(x₀) = 0"></span> und
> <span class="m" data-tex="f''(x_0)<0" data-plain="f″(x₀) < 0"></span> folgt ein Hochpunkt, aus
> <span class="m" data-tex="f''(x_0)>0" data-plain="f″(x₀) > 0"></span> ein Tiefpunkt. Ist
> <span class="m" data-tex="f''(x_0)=0" data-plain="f″(x₀) = 0"></span>, **entscheidet dieses
> Kriterium nichts**; dann bleibt nur der Vorzeichenwechsel von
> <span class="m" data-tex="f'" data-plain="f′"></span>.

**`<details>` — Herleitung: Warum das f″-Kriterium funktioniert**
Summary: *Herleitung des f″-Kriteriums aus dem Differenzenquotienten*

> Sei <span class="m" data-tex="f'(x_0)=0" data-plain="f′(x₀) = 0"></span> und
> <span class="m" data-tex="f''(x_0)>0" data-plain="f″(x₀) > 0"></span>. Die zweite Ableitung ist
> die Ableitung von <span class="m" data-tex="f'" data-plain="f′"></span>, also der Grenzwert
>
> <span class="m block" data-tex="f''(x_0) = \lim_{h\to 0}\frac{f'(x_0+h)-f'(x_0)}{h} = \lim_{h\to 0}\frac{f'(x_0+h)}{h}" data-plain="f″(x₀) = lim(h→0) [f′(x₀+h) − f′(x₀)]/h = lim(h→0) f′(x₀+h)/h"></span>
>
> Im letzten Schritt wurde <span class="m" data-tex="f'(x_0)=0" data-plain="f′(x₀) = 0"></span>
> benutzt. Der Grenzwert ist positiv. Also ist für alle hinreichend kleinen
> <span class="m" data-tex="h\neq 0" data-plain="h ≠ 0"></span> auch der Quotient
> <span class="m" data-tex="f'(x_0+h)/h" data-plain="f′(x₀+h)/h"></span> positiv. Zwei Fälle:
> Für <span class="m" data-tex="h>0" data-plain="h > 0"></span> muss dann
> <span class="m" data-tex="f'(x_0+h)>0" data-plain="f′(x₀+h) > 0"></span> sein, und für
> <span class="m" data-tex="h<0" data-plain="h < 0"></span> muss
> <span class="m" data-tex="f'(x_0+h)<0" data-plain="f′(x₀+h) < 0"></span> sein, denn ein positiver
> Quotient mit negativem Nenner hat einen negativen Zähler. Das ist genau der Vorzeichenwechsel
> von − nach +: Kriterium 2 ist also ein Spezialfall von Kriterium 1, und
> <span class="m" data-tex="x_0" data-plain="x₀"></span> ist ein Tiefpunkt. Für
> <span class="m" data-tex="f''(x_0)<0" data-plain="f″(x₀) < 0"></span> läuft die Rechnung mit
> umgekehrten Vorzeichen.
>
> **Zahlenprobe** (Beispiel aus 2.5, <span class="m" data-tex="x_0=0" data-plain="x₀ = 0"></span>,
> <span class="m" data-tex="f''(0)=8" data-plain="f″(0) = 8"></span>):
> <span class="m" data-tex="f'(0{,}1)=0{,}684" data-plain="f′(0,1) = 0,684"></span> und
> <span class="m" data-tex="f'(-0{,}1)=-0{,}924" data-plain="f′(−0,1) = −0,924"></span>; die
> Quotienten <span class="m" data-tex="0{,}684/0{,}1 = 6{,}84" data-plain="0,684/0,1 = 6,84"></span> und
> <span class="m" data-tex="(-0{,}924)/(-0{,}1)=9{,}24" data-plain="(−0,924)/(−0,1) = 9,24"></span>
> liegen beide in der Nähe von 8, dem Wert von <span class="m" data-tex="f''(0)" data-plain="f″(0)"></span>, und
> beide sind positiv.
>
> **Was die Herleitung zeigt und was nicht.** Sie zeigt, dass im Fall
> <span class="m" data-tex="f''(x_0)\neq 0" data-plain="f″(x₀) ≠ 0"></span> der Vorzeichenwechsel
> garantiert ist. Für <span class="m" data-tex="f''(x_0)=0" data-plain="f″(x₀) = 0"></span> ist der
> Grenzwert null, und über das Vorzeichen des Quotienten sagt sie nichts. Genau dort liegt die Lücke
> des Kriteriums.

### 2.3 Wendestellen

Fließtext:

> Ein Wendepunkt ist der Ort, an dem der Graph von einer Linkskurve in eine Rechtskurve übergeht
> oder umgekehrt. An dieser Stelle ist die Steigung so groß oder so klein wie nirgends in der
> Nähe, also hat die Funktion
> <span class="m" data-tex="f'" data-plain="f′"></span> dort eine Extremstelle. Wer die
> Extremstellen von <span class="m" data-tex="f'" data-plain="f′"></span> sucht, wendet die Regeln
> aus 2.2 auf <span class="m" data-tex="f'" data-plain="f′"></span> an, und das ist schon der ganze
> Trick. Mit dem Beispiel Passstraße heißt das: Dort, wo die Straße am steilsten fällt, liegt ein
> Wendepunkt.

`.merksatz`:

> **Wendestellen**
> **Notwendig:** Ist <span class="m" data-tex="x_0" data-plain="x₀"></span> eine Wendestelle, so gilt
> <span class="m" data-tex="f''(x_0)=0" data-plain="f″(x₀) = 0"></span>.
> **Hinreichend:** Wechselt <span class="m" data-tex="f''" data-plain="f″"></span> bei
> <span class="m" data-tex="x_0" data-plain="x₀"></span> das Vorzeichen, oder gilt
> <span class="m" data-tex="f''(x_0)=0" data-plain="f″(x₀) = 0"></span> und
> <span class="m" data-tex="f'''(x_0)\neq 0" data-plain="f‴(x₀) ≠ 0"></span>, so liegt ein
> Wendepunkt vor. Die **Wendetangente** ist die Tangente im Wendepunkt; sie hat die größte oder
> kleinste Steigung der Umgebung. Ist die Wendetangente waagerecht, spricht man von einem
> **Sattelpunkt** (auch Terrassenpunkt).

**`<details>` — Herleitung: Warum f‴ ≠ 0 genügt**
Summary: *Wendestellen sind Extremstellen von f′*

> Setze <span class="m" data-tex="g = f'" data-plain="g = f′"></span>. Dann ist
> <span class="m" data-tex="g' = f''" data-plain="g′ = f″"></span> und
> <span class="m" data-tex="g''=f'''" data-plain="g″ = f‴"></span>. Eine Wendestelle von
> <span class="m" data-tex="f" data-plain="f"></span> ist per Definition eine Stelle, an der sich
> das Krümmungsverhalten ändert, also an der <span class="m" data-tex="g'=f''" data-plain="g′ = f″"></span>
> das Vorzeichen wechselt, und das ist exakt der Vorzeichenwechsel-Test für eine Extremstelle von
> <span class="m" data-tex="g" data-plain="g"></span>. Damit folgt sofort:
>
> <span class="m block" data-tex="f''(x_0)=0 \;\wedge\; f'''(x_0)\neq 0 \;\Longrightarrow\; g'(x_0)=0 \;\wedge\; g''(x_0)\neq 0 \;\Longrightarrow\; g \text{ hat bei } x_0 \text{ eine Extremstelle}" data-plain="f″(x₀) = 0 und f‴(x₀) ≠ 0 ⟹ g′(x₀) = 0 und g″(x₀) ≠ 0 ⟹ g = f′ hat bei x₀ eine Extremstelle"></span>
>
> Die Extremstelle von <span class="m" data-tex="g=f'" data-plain="g = f′"></span> ist ein
> Vorzeichenwechsel von <span class="m" data-tex="g'=f''" data-plain="g′ = f″"></span>, und das
> ist die Wendestelle. Nebenbei erklärt die Rechnung den Namen der Wendetangente: Ihre Steigung
> ist der Extremwert <span class="m" data-tex="g(x_0)=f'(x_0)" data-plain="g(x₀) = f′(x₀)"></span>.
>
> **Zahlenprobe** (Beispiel 2.5): <span class="m" data-tex="f'''(x)=24(x-1)" data-plain="f‴(x) = 24(x − 1)"></span>
> hat an den Wendestellen <span class="m" data-tex="x=1\mp\tfrac{\sqrt3}{3}" data-plain="x = 1 ∓ √3/3"></span>
> die Werte <span class="m" data-tex="\mp 8\sqrt 3\approx\mp 13{,}86" data-plain="∓8√3 ≈ ∓13,86"></span>,
> beide ungleich null. Die Steigungen der Wendetangenten
> <span class="m" data-tex="\pm\tfrac{8\sqrt3}{9}\approx\pm 1{,}54" data-plain="±8√3/9 ≈ ±1,54"></span>
> sind die Extremwerte von <span class="m" data-tex="f'" data-plain="f′"></span>: Das lokale Maximum
> der Steigung <span class="m" data-tex="+1{,}54" data-plain="+1,54"></span> liegt links von
> <span class="m" data-tex="x=1" data-plain="x = 1"></span>, das lokale Minimum
> <span class="m" data-tex="-1{,}54" data-plain="−1,54"></span> rechts davon.
>
> **Die Umkehrung gilt nicht.** Bei <span class="m" data-tex="f(x)=x^5" data-plain="f(x) = x⁵"></span>
> ist <span class="m" data-tex="f'''(0)=0" data-plain="f‴(0) = 0"></span>, und trotzdem hat
> <span class="m" data-tex="f''=20x^3" data-plain="f″ = 20x³"></span> bei 0 von − nach + gewechselt.
> Das Kriterium mit <span class="m" data-tex="f'''" data-plain="f‴"></span> ist bequem, aber nicht
> das einzige.

### 2.4 Die Fehlvorstellung: „Null in der Ableitung entscheidet"

`.hinweis` (**die zentrale Fehlvorstellung dieses Moduls**):

> **Häufigster Fehler überhaupt.** „Bei <span class="m" data-tex="f'(x_0)=0" data-plain="f′(x₀) = 0"></span>
> ist ein Extremum" und „bei <span class="m" data-tex="f''(x_0)=0" data-plain="f″(x₀) = 0"></span>
> ist ein Wendepunkt". Beides ist falsch, und du kannst es an zwei Funktionen in einer Minute
> selbst widerlegen: <span class="m" data-tex="x^3" data-plain="x³"></span> hat bei 0 eine
> waagerechte Tangente und **kein** Extremum, und <span class="m" data-tex="x^4" data-plain="x⁴"></span> hat bei 0
> ein Extremum und **keinen** Wendepunkt, obwohl in beiden Fällen
> <span class="m" data-tex="f'(0)=f''(0)=0" data-plain="f′(0) = f″(0) = 0"></span> gilt.

Vergleichstabelle (in `<div class="tabelle">`, Inhalt aus K3):

| Funktion | f′ um x = 0 | f″ um x = 0 | Befund bei x = 0 |
|---|---|---|---|
| <span class="m" data-tex="x^4" data-plain="x⁴"></span> | <span class="m" data-tex="4x^3" data-plain="4x³"></span>: − → + | <span class="m" data-tex="12x^2" data-plain="12x²"></span>: ≥ 0, kein Wechsel | Tiefpunkt, kein Wendepunkt |
| <span class="m" data-tex="-x^4" data-plain="−x⁴"></span> | <span class="m" data-tex="-4x^3" data-plain="−4x³"></span>: + → − | <span class="m" data-tex="-12x^2" data-plain="−12x²"></span>: ≤ 0, kein Wechsel | Hochpunkt, kein Wendepunkt |
| <span class="m" data-tex="x^3" data-plain="x³"></span> | <span class="m" data-tex="3x^2" data-plain="3x²"></span>: ≥ 0, kein Wechsel | <span class="m" data-tex="6x" data-plain="6x"></span>: − → + | Sattelpunkt |

`.merksatz`:

> **Ein Merksatz, der eine Aussage macht.** Eine Nullstelle von
> <span class="m" data-tex="f'" data-plain="f′"></span> ist nur dann eine Extremstelle, wenn
> <span class="m" data-tex="f'" data-plain="f′"></span> dort **das Vorzeichen wechselt**, und eine
> Nullstelle von <span class="m" data-tex="f''" data-plain="f″"></span> ist nur dann eine
> Wendestelle, wenn <span class="m" data-tex="f''" data-plain="f″"></span> dort **das Vorzeichen
> wechselt**. Es kommt auf den Wechsel an, nicht auf die Null. Der Wert
> <span class="m" data-tex="f''(x_0)" data-plain="f″(x₀)"></span> ist nur eine Abkürzung für den
> Vorzeichenwechsel, und die Abkürzung gilt nur, solange er nicht null ist.

### 2.5 Kurvendiskussion als Ablauf: ein Beispiel vollständig

Fließtext:

> Eine vollständige Untersuchung geht immer in derselben Reihenfolge, damit nichts vergessen wird
> und die Ergebnisse aufeinander aufbauen. Die Schritte: **(1)** Definitionsbereich und Symmetrie,
> **(2)** Verhalten für <span class="m" data-tex="x\to\pm\infty" data-plain="x → ±∞"></span>, **(3)** Nullstellen und
> y-Achsenabschnitt, **(4)** Ableitungen, **(5)** Extrempunkte, **(6)** Wendepunkte,
> **(7)** Skizze aus den Ergebnissen. Ein Beispiel, an dem alles vorkommt:
> <span class="m block" data-tex="f(x) = x^4-4x^3+4x^2 = x^2(x-2)^2" data-plain="f(x) = x⁴ − 4x³ + 4x² = x²(x − 2)²"></span>

Schrittweise Rechnung (Kontrollwerte K2), jeweils als eigener Absatz:

> **(1)–(3)** Definitionsbereich ℝ. Der faktorisierte Term zeigt: Nullstellen bei
> <span class="m" data-tex="x=0" data-plain="x = 0"></span> und
> <span class="m" data-tex="x=2" data-plain="x = 2"></span>, beide **doppelt**, also berührt der
> Graph dort die x-Achse, ohne sie zu schneiden; dazu ist
> <span class="m" data-tex="f\ge 0" data-plain="f ≥ 0"></span> überall (ein Quadrat).
> Der Höchstgrad-Term <span class="m" data-tex="x^4" data-plain="x⁴"></span> mit positivem
> Koeffizienten liefert <span class="m" data-tex="f(x)\to+\infty" data-plain="f(x) → +∞"></span> für
> <span class="m" data-tex="x\to\pm\infty" data-plain="x → ±∞"></span>. Symmetrie: Zur y-Achse besteht keine
> (Exponenten 4, 3, 2 gemischt), wohl aber zur Geraden
> <span class="m" data-tex="x=1" data-plain="x = 1"></span>, denn
> <span class="m" data-tex="f(x)=\big((x-1)^2-1\big)^2" data-plain="f(x) = ((x − 1)² − 1)²"></span>
> hängt nur von <span class="m" data-tex="(x-1)^2" data-plain="(x − 1)²"></span> ab. Kontrolle:
> <span class="m" data-tex="f(-1)=f(3)=9" data-plain="f(−1) = f(3) = 9"></span>.
>
> **(4)** <span class="m" data-tex="f'(x)=4x^3-12x^2+8x=4x(x-1)(x-2)" data-plain="f′(x) = 4x³ − 12x² + 8x = 4x(x − 1)(x − 2)"></span>,
> <span class="m" data-tex="f''(x)=12x^2-24x+8" data-plain="f″(x) = 12x² − 24x + 8"></span>,
> <span class="m" data-tex="f'''(x)=24x-24=24(x-1)" data-plain="f‴(x) = 24x − 24 = 24(x − 1)"></span>.
>
> **(5)** Notwendig: <span class="m" data-tex="f'(x)=0" data-plain="f′(x) = 0"></span> bei
> <span class="m" data-tex="x=0,\,1,\,2" data-plain="x = 0, 1, 2"></span>. Hinreichend mit
> <span class="m" data-tex="f''" data-plain="f″"></span>:
> <span class="m" data-tex="f''(0)=8>0" data-plain="f″(0) = 8 > 0"></span> Tiefpunkt,
> <span class="m" data-tex="f''(1)=-4<0" data-plain="f″(1) = −4 < 0"></span> Hochpunkt,
> <span class="m" data-tex="f''(2)=8>0" data-plain="f″(2) = 8 > 0"></span> Tiefpunkt. Die y-Werte
> gehören dazu: <span class="m" data-tex="T_1(0\,|\,0)" data-plain="T₁(0 | 0)"></span>,
> <span class="m" data-tex="H(1\,|\,1)" data-plain="H(1 | 1)"></span>,
> <span class="m" data-tex="T_2(2\,|\,0)" data-plain="T₂(2 | 0)"></span>. Beide Tiefpunkte sind
> zugleich globale Minima, weil <span class="m" data-tex="f\ge0" data-plain="f ≥ 0"></span> ist.
>
> **(6)** Notwendig: <span class="m" data-tex="12x^2-24x+8=0" data-plain="12x² − 24x + 8 = 0"></span>,
> also <span class="m" data-tex="x^2-2x+\tfrac23=0" data-plain="x² − 2x + 2/3 = 0"></span> und
> <span class="m" data-tex="x=1\pm\sqrt{1-\tfrac23}=1\pm\tfrac{\sqrt3}{3}\approx 0{,}423\text{ bzw. }1{,}577" data-plain="x = 1 ± √(1 − 2/3) = 1 ± √3/3 ≈ 0,423 bzw. 1,577"></span>.
> Hinreichend: <span class="m" data-tex="f'''(x)=\mp 8\sqrt3\neq 0" data-plain="f‴(x) = ∓8√3 ≠ 0"></span>.
> Beide y-Werte sind <span class="m" data-tex="\tfrac49\approx 0{,}444" data-plain="4/9 ≈ 0,444"></span>
> (Symmetrie!), die Steigungen der Wendetangenten
> <span class="m" data-tex="\pm\tfrac{8\sqrt3}{9}\approx\pm1{,}54" data-plain="±8√3/9 ≈ ±1,54"></span>.
>
> **(7)** Der Graph hat die Form eines „W": zwei Tiefpunkte auf der x-Achse, dazwischen der
> Hochpunkt <span class="m" data-tex="(1\,|\,1)" data-plain="(1 | 1)"></span>, die Wendepunkte
> zwischen Tief- und Hochpunkt. Das passt zur Steigungsrichtung: Von
> <span class="m" data-tex="T_1" data-plain="T₁"></span> zu <span class="m" data-tex="H" data-plain="H"></span> steigt der Graph, dazwischen
> muss die Steigung ein Maximum haben, und das liegt genau bei der ersten Wendestelle.

`.hinweis`:

> **Selbstkontrolle beim Üben.** Zwei Proben fangen fast alle Rechenfehler: die Symmetrie
> (bei diesem Beispiel <span class="m" data-tex="f(2-x)=f(x)" data-plain="f(2 − x) = f(x)"></span>) und ein Blick auf die
> Form. Steht in der Rechnung ein Tiefpunkt neben einem Tiefpunkt, muss dazwischen ein Hochpunkt
> liegen: **Extrempunkte wechseln sich ab**, und zwischen einem Hoch- und einem Tiefpunkt liegt
> mindestens ein Wendepunkt.

### 2.6 Lokal ist nicht global: Randextrema

Fließtext:

> Ist die Funktion nur auf einem Intervall
> <span class="m" data-tex="[a;b]" data-plain="[a; b]"></span> betrachtet, etwa ein Pegelstand
> über fünf Tage, dann kann der größte Wert am **Rand** liegen, wo die Tangente gar nicht
> waagerecht sein muss. Man bestimmt deshalb zuerst alle lokalen Extremwerte im Inneren und
> vergleicht sie dann mit den Funktionswerten an den Rändern. Der größte dieser Werte ist das
> **globale Maximum**, der kleinste das globale Minimum.

`.merksatz`:

> **Globale Extrema auf einem Intervall.** Kandidaten sind die Nullstellen von
> <span class="m" data-tex="f'" data-plain="f′"></span> im Inneren und die beiden Randwerte. Wer nur
> <span class="m" data-tex="f'=0" data-plain="f′ = 0"></span> löst, übersieht den Rand, und wer nur den Rand betrachtet, übersieht
> den Gipfel im Inneren.

---

## 3 · Vertiefung

`<section id="scharen">`, `.stufe`-Kopf: Nr. **3**, Überschrift **Funktionsscharen: Ein Parameter, viele Graphen**.

### 3.1 Was eine Schar ist und was sie verlangt

Fließtext (wörtlich):

> Steht in einem Funktionsterm neben <span class="m" data-tex="x" data-plain="x"></span> noch ein
> Buchstabe, zum Beispiel <span class="m" data-tex="f_t(x)=x^3-3t\,x^2" data-plain="f_t(x) = x³ − 3t·x²"></span>,
> dann steht der Term für **unendlich viele Funktionen auf einmal**: für jedes
> <span class="m" data-tex="t" data-plain="t"></span> eine. Man nennt das eine **Funktionenschar**
> und <span class="m" data-tex="t" data-plain="t"></span> den **Parameter**. Die Aufgabe ist, die
> Untersuchung einmal für alle durchzuführen. Dafür gilt eine einzige Grundregel: **Beim Ableiten
> nach <span class="m" data-tex="x" data-plain="x"></span> ist der Parameter eine Konstante.** Aus
> <span class="m" data-tex="-3t\,x^2" data-plain="−3t·x²"></span> wird also
> <span class="m" data-tex="-6t\,x" data-plain="−6t·x"></span> — der Faktor
> <span class="m" data-tex="-3t" data-plain="−3t"></span> bleibt stehen wie die 5 in
> <span class="m" data-tex="5x^2" data-plain="5x²"></span>.

`.hinweis`:

> **Zwei Fehler, die immer wieder passieren.** (1) Nach dem Parameter abzuleiten:
> <span class="m" data-tex="(-3t\,x^2)'=-3x^2" data-plain="(−3t·x²)′ = −3x²"></span> wäre die Ableitung
> nach <span class="m" data-tex="t" data-plain="t"></span> und beantwortet eine andere Frage.
> (2) Zu früh durch den Parameter zu teilen: Wer bei
> <span class="m" data-tex="3x(x-2t)=0" data-plain="3x(x − 2t) = 0"></span> durch
> <span class="m" data-tex="t" data-plain="t"></span> kürzt, verliert den Fall
> <span class="m" data-tex="t=0" data-plain="t = 0"></span>. Die Kontrollfrage lautet immer: **Für
> welche Parameterwerte ist die Rechnung überhaupt erlaubt, und was passiert an den Rändern?**

### 3.2 Beispiel mit Fallunterscheidung: f_t(x) = x³ − 3t·x²

Schrittweise Rechnung (Kontrollwerte K5):

> Ableitungen: <span class="m" data-tex="f_t'(x)=3x^2-6t\,x=3x(x-2t)" data-plain="f_t′(x) = 3x² − 6t·x = 3x(x − 2t)"></span>,
> <span class="m" data-tex="f_t''(x)=6x-6t=6(x-t)" data-plain="f_t″(x) = 6x − 6t = 6(x − t)"></span>,
> <span class="m" data-tex="f_t'''(x)=6" data-plain="f_t‴(x) = 6"></span>.
>
> **Extremstellen.** Notwendig:
> <span class="m" data-tex="3x(x-2t)=0" data-plain="3x(x − 2t) = 0"></span> also
> <span class="m" data-tex="x=0" data-plain="x = 0"></span> oder
> <span class="m" data-tex="x=2t" data-plain="x = 2t"></span>. Für
> <span class="m" data-tex="t\neq 0" data-plain="t ≠ 0"></span> sind das zwei verschiedene Stellen.
> Hinreichend: <span class="m" data-tex="f_t''(0)=-6t" data-plain="f_t″(0) = −6t"></span> und
> <span class="m" data-tex="f_t''(2t)=6t" data-plain="f_t″(2t) = 6t"></span>. Jetzt hängt das
> Vorzeichen vom Parameter ab, und deshalb braucht man eine **Fallunterscheidung**:
>
> Tabelle in `<div class="tabelle">`:
>
> | Fall | Bei x = 0 | Bei x = 2t |
> |---|---|---|
> | t > 0 | f″ = −6t < 0: Hochpunkt (0 \| 0) | f″ = 6t > 0: Tiefpunkt (2t \| −4t³) |
> | t < 0 | f″ = −6t > 0: Tiefpunkt (0 \| 0) | f″ = 6t < 0: Hochpunkt (2t \| −4t³) |
> | t = 0 | beide Stellen fallen zusammen: f₀(x) = x³, Sattelpunkt (0 \| 0) | |
>
> **Wendestelle.** <span class="m" data-tex="f_t''(x)=0" data-plain="f_t″(x) = 0"></span> ergibt
> <span class="m" data-tex="x=t" data-plain="x = t"></span>, und
> <span class="m" data-tex="f_t'''=6\neq 0" data-plain="f_t‴ = 6 ≠ 0"></span> gilt für jeden
> Parameter: Der Wendepunkt <span class="m" data-tex="W_t(t\,|\,-2t^3)" data-plain="W_t(t | −2t³)"></span>
> existiert immer. Die Steigung der Wendetangente ist
> <span class="m" data-tex="f_t'(t)=-3t^2" data-plain="f_t′(t) = −3t²"></span>: **nie positiv**, und nur für
> <span class="m" data-tex="t=0" data-plain="t = 0"></span> waagerecht, also genau im Sattelfall.
>
> **Zahlenproben.** <span class="m" data-tex="t=2" data-plain="t = 2"></span>:
> <span class="m" data-tex="f_2(x)=x^3-6x^2" data-plain="f₂(x) = x³ − 6x²"></span> mit
> <span class="m" data-tex="H(0\,|\,0)" data-plain="H(0 | 0)"></span>,
> <span class="m" data-tex="T(4\,|\,-32)" data-plain="T(4 | −32)"></span>,
> <span class="m" data-tex="W(2\,|\,-16)" data-plain="W(2 | −16)"></span>.
> <span class="m" data-tex="t=-1" data-plain="t = −1"></span>:
> <span class="m" data-tex="f_{-1}(x)=x^3+3x^2" data-plain="f₋₁(x) = x³ + 3x²"></span> mit
> <span class="m" data-tex="T(0\,|\,0)" data-plain="T(0 | 0)"></span>,
> <span class="m" data-tex="H(-2\,|\,4)" data-plain="H(−2 | 4)"></span>,
> <span class="m" data-tex="W(-1\,|\,2)" data-plain="W(−1 | 2)"></span>.

`.merksatz`:

> **Der Parameter entscheidet über die Sorte des Punktes.** Bei Scharen ist die Aussage „das
> ist ein Hochpunkt" fast nie für alle Parameterwerte richtig. Ein vollständiges Ergebnis
> besteht aus den **Fällen** und den **Übergangswerten**: Hier wechselt bei
> <span class="m" data-tex="t=0" data-plain="t = 0"></span> ein Hochpunkt in einen Tiefpunkt, und
> genau dort verschmelzen die beiden Extremstellen zum Sattelpunkt.

### 3.3 Die Ortskurve

Fließtext:

> Verändert man den Parameter, wandern die Extrem- und Wendepunkte. Die **Ortskurve** (Ortslinie)
> ist die Kurve, auf der alle diese Punkte liegen. Die Methode besteht aus zwei Schritten:
> **Erstens** die Koordinaten des Punktes in Abhängigkeit vom Parameter aufschreiben,
> **zweitens** den Parameter eliminieren, also aus der x-Koordinate nach
> <span class="m" data-tex="t" data-plain="t"></span> auflösen und in die y-Koordinate einsetzen.

`.merksatz`:

> **Ortskurve bestimmen.** (1) Punkt in Abhängigkeit von
> <span class="m" data-tex="t" data-plain="t"></span> bestimmen:
> <span class="m" data-tex="(x(t)\,|\,y(t))" data-plain="(x(t) | y(t))"></span>. (2) x-Gleichung nach
> <span class="m" data-tex="t" data-plain="t"></span> auflösen. (3) In
> <span class="m" data-tex="y(t)" data-plain="y(t)"></span> einsetzen. Ergebnis: eine Gleichung
> <span class="m" data-tex="y=g(x)" data-plain="y = g(x)"></span> ohne Parameter. Sie gilt nur für
> die Parameterwerte, für die der Punkt überhaupt existiert.

Beispiel (Kontrollwerte K5):

> **Wendepunkte:** <span class="m" data-tex="x=t" data-plain="x = t"></span>,
> <span class="m" data-tex="y=-2t^3" data-plain="y = −2t³"></span>. Auflösen ist trivial
> (<span class="m" data-tex="t=x" data-plain="t = x"></span>), also
> <span class="m block" data-tex="y=-2x^3" data-plain="y = −2x³"></span>
> **Extrempunkte:** Der bewegliche Extrempunkt hat
> <span class="m" data-tex="x=2t" data-plain="x = 2t"></span>, also
> <span class="m" data-tex="t=x/2" data-plain="t = x/2"></span>, und
> <span class="m" data-tex="y=-4t^3=-4\cdot\tfrac{x^3}{8}" data-plain="y = −4t³ = −4·x³/8"></span>, also
> <span class="m block" data-tex="y=-\tfrac12 x^3" data-plain="y = −x³/2"></span>
> Probe: <span class="m" data-tex="t=2" data-plain="t = 2"></span> liefert
> <span class="m" data-tex="T(4\,|\,-32)" data-plain="T(4 | −32)"></span>, und
> <span class="m" data-tex="-\tfrac12\cdot 4^3=-32" data-plain="−(1/2)·4³ = −32"></span> ✓. Der feste Punkt
> <span class="m" data-tex="(0\,|\,0)" data-plain="(0 | 0)"></span> liegt auf beiden Kurven.

**`<details>` — Ein zweiter Weg: die Bedingung f′ = 0 nach dem Parameter auflösen**
Summary: *Ortskurve ohne die Koordinaten des Punktes vorher auszurechnen*

> Manchmal sind die Koordinaten des Extrempunkts unhandlich (Wurzeln!). Dann geht es kürzer:
> Ein Extrempunkt <span class="m" data-tex="(x\,|\,y)" data-plain="(x | y)"></span> erfüllt
> immer zwei Gleichungen gleichzeitig, nämlich
> <span class="m" data-tex="f_t'(x)=0" data-plain="f_t′(x) = 0"></span> und
> <span class="m" data-tex="y=f_t(x)" data-plain="y = f_t(x)"></span>. Löst man die erste nach
> <span class="m" data-tex="t" data-plain="t"></span> auf und setzt das in die zweite ein, so ist der
> Parameter verschwunden, ohne dass man die Extremstelle je explizit ausgerechnet hat. Am Beispiel:
> <span class="m" data-tex="3x^2-6t\,x=0" data-plain="3x² − 6t·x = 0"></span> ergibt für
> <span class="m" data-tex="x\neq0" data-plain="x ≠ 0"></span> die Beziehung
> <span class="m" data-tex="t=x/2" data-plain="t = x/2"></span>; eingesetzt in
> <span class="m" data-tex="y=x^3-3t\,x^2" data-plain="y = x³ − 3t·x²"></span> folgt
> <span class="m" data-tex="y=x^3-\tfrac32 x^3=-\tfrac12x^3" data-plain="y = x³ − (3/2)·x³ = −x³/2"></span>,
> dasselbe Ergebnis wie oben.
>
> **Warum das funktioniert:** Die Gleichung
> <span class="m" data-tex="f_t'(x)=0" data-plain="f_t′(x) = 0"></span> beschreibt alle
> Paare <span class="m" data-tex="(x,t)" data-plain="(x, t)"></span>, bei denen die Tangente
> waagerecht ist. Wer sie nach <span class="m" data-tex="t" data-plain="t"></span> auflöst,
> erhält zu jedem <span class="m" data-tex="x" data-plain="x"></span> den Parameter, für den dort
> eine waagerechte Tangente liegt, und der zugehörige y-Wert ist genau
> <span class="m" data-tex="f_t(x)" data-plain="f_t(x)"></span> mit diesem <span class="m" data-tex="t" data-plain="t"></span>.
>
> **Die Vorsicht dabei.** Das Verfahren liefert alle Punkte mit waagerechter Tangente, also auch
> Sattelpunkte. Ob ein Extrempunkt vorliegt, muss danach noch für jeden Bereich geprüft werden
> (hier: Existenz für alle <span class="m" data-tex="t\neq 0" data-plain="t ≠ 0"></span>).

### 3.4 Einen Parameter bestimmen

Kurzes Beispiel (Standardaufgabentyp im Abitur):

> **Aufgabe:** Für welchen Wert von <span class="m" data-tex="t>0" data-plain="t > 0"></span> liegt
> der Tiefpunkt von <span class="m" data-tex="f_t" data-plain="f_t"></span> auf der Geraden
> <span class="m" data-tex="y=-32" data-plain="y = −32"></span>?
> **Lösung:** Der Tiefpunkt ist <span class="m" data-tex="(2t\,|\,-4t^3)" data-plain="(2t | −4t³)"></span>. Gefordert:
> <span class="m" data-tex="-4t^3=-32" data-plain="−4t³ = −32"></span>, also
> <span class="m" data-tex="t^3=8" data-plain="t³ = 8"></span> und
> <span class="m" data-tex="t=2" data-plain="t = 2"></span> (die einzige reelle Lösung, und sie ist
> größer als null). Probe: <span class="m" data-tex="T(4\,|\,-32)" data-plain="T(4 | −32)"></span> ✓.
> Das Vorgehen lautet immer: Koordinate des Punktes in Abhängigkeit vom Parameter, Bedingung als Gleichung
> für den Parameter, lösen, Bedingung an den Parameter (hier
> <span class="m" data-tex="t>0" data-plain="t > 0"></span>) prüfen.

---

## 4 · Interaktiver Kern

`<section id="simulation">`, `.stufe`-Kopf: Nr. **4**, Überschrift **Scharen im Experiment: Punkte wandern, Punkte verschmelzen**.

Das Modul bekommt **eine** Simulation (eine IIFE, Vorbild `cvSim`/`cvPhi`/`cvU` im Referenzmodul), mit
zwei Canvas, die waagerecht deckungsgleich sind: oben der Graph von f, darunter f′ und f″ mit
Vorzeichenband. Alle drei Scharen gehören zur selben Oberfläche und werden über ein
`<select>` umgeschaltet.

**Der didaktische Kern dieser Simulation (und der Grund für die verdeckten Formeln).** Zwei der drei
Scharen werden **ohne Funktionsterm** gezeigt. Wie bei einer Messreihe sieht man nur Graph,
Messwerte an der Prüfstelle und die Vorzeichenbänder. Die beiden Verständnisfragen
beziehen sich ausschließlich auf diese verdeckten Scharen; damit lassen sie sich weder aus dem
Erklärteil ableiten noch durch Rechnen mit einer sichtbaren Formel lösen, sondern nur durch
Bedienen der Simulation. Erst in der Rückmeldung zur richtigen Antwort wird die Formel offenbart,
und die Lernenden können dann nachrechnen, was sie gesehen haben.

### 4.1 Das Modell

Fließtext über der Simulation (wörtlich):

> Oben siehst du den Graphen einer Funktion, die von einem Parameter *a* abhängt. Verstellst du
> *a*, wandern Hochpunkte, Tiefpunkte und Wendepunkte, und manchmal verschwinden sie. Darunter
> stehen die Ableitungen und zwei Vorzeichenbänder: Wo das obere Band **grün** ist, steigt der
> Graph, wo es **rot** ist, fällt er. Das untere Band ist **blau** in Linkskurven und **orange** in
> Rechtskurven. Bei zwei der drei Scharen ist die Formel verdeckt: Du untersuchst sie wie ein
> Messobjekt, nur mit dem, was die Anzeige hergibt.

Die drei Scharen (**Formeln nur in der IIFE als Kommentar und Code; Schar 2 und 3 werden nirgends
im sichtbaren Text genannt**):

| Nr. | Bezeichnung im `<select>` | f_a(x) | f_a′(x) | f_a″(x) | Fenster x | Fenster y (f) | Fenster y (Ableitungen) | a-Bereich |
|---|---|---|---|---|---|---|---|---|
| 1 | „Schar 1: fₐ(x) = x³/3 − a·x" | x³/3 − a·x | x² − a | 2x | −3 … 3 | −6 … 6 | −6 … 10 | −1,00 … 4,00 |
| 2 | „Schar 2 (Formel verdeckt)" | x³/3 − x² + a·x | x² − 2x + a | 2(x − 1) | −2 … 4 | −4 … 6 | −6 … 12 | −1,00 … 4,00 |
| 3 | „Schar 3 (Formel verdeckt)" | x⁴/4 − a·x³/3 | x²(x − a) | x(3x − 2a) | −2 … 3 | −2 … 3 | −3 … 6 | −1,00 … 2,00 |

Nachweis, dass alle Markierungen im Fenster liegen: K9. Kurven, die das Fenster verlassen, werden per
`ctx.clip()` abgeschnitten, das ist gewollt.

**Charakteristische Punkte (die Simulation rechnet sie mit den Formeln aus K6, nicht numerisch):**
- **Schar 1**: für a > 0 H(−√a | (2/3)·a·√a) und T(√a | −(2/3)·a·√a); immer W(0 | 0), Steigung der Wendetangente m_W = −a; bei a = 0 (Ganzzahltest `Wert === 0`) zusätzlich Kennzeichnung **Sattelpunkt**.
- **Schar 2**: für a < 1 s = √(1 − a), H(1 − s | f(1 − s)), T(1 + s | f(1 + s)); immer W(1 | a − 2/3), m_W = a − 1; bei a = 1 (Ganzzahltest `Wert === 20`) **Sattelpunkt** in W, keine H/T.
- **Schar 3**: für a ≠ 0 T(a | −a⁴/12), S(0 | 0) als **Sattelpunkt**, W(2a/3 | −4a⁴/81); bei a = 0 (`Wert === 0`) nur T(0 | 0), Hinweis „f′ und f″ sind null, f′ wechselt von − nach +".

Wegen der Fließkommadarstellung (a = Wert/20) wird **nie** `a === 1` oder `a === 0` verglichen, sondern der Ganzzahlwert des Reglers.

### 4.2 Bedienelemente

| ID | Element | Bereich / Wirkung | Startwert |
|---|---|---|---|
| `sSchar` | `<select>` | Werte `1`, `2`, `3`; Wechsel setzt a und x₀ auf die Startwerte der Schar (rechte Spalte) und stoppt die Animation | 1 |
| `rA` | Regler Parameter a | `min`/`max`/`step` = −20 … 80 (Schar 1, 2), −20 … 40 (Schar 3), Schritt 1; a = Wert/20, also −1,00 … 4,00 bzw. 2,00 in Schritten von 0,05 | Schar 1: **20** (a = 1,00) · Schar 2: **−10** (a = −0,50) · Schar 3: **20** (a = 1,00) |
| `rX` | Regler Prüfstelle x₀ | x₀ = Wert/20, Schritt 1; Bereich = x-Fenster der Schar: −60 … 60 (Schar 1), −40 … 80 (Schar 2), −40 … 60 (Schar 3) | Schar 1: **40** (2,00) · Schar 2: **50** (2,50) · Schar 3: **40** (2,00) |
| `cTan` | Checkbox „Tangente an der Prüfstelle" | schaltet die gestrichelte Tangente | an |
| `cSpur` | Checkbox „Ortskurve der Extrem- und Wendepunkte" | zeichnet die Spuren aller Extrem- bzw. Wendepunkte über den gesamten a-Bereich (analytisch, 200 Schritte) als punktierte Linien | aus |
| `cAufbau` | Checkbox „f′ und f″ nur bis zur Prüfstelle" | zeichnet f′, f″ und die Vorzeichenbänder nur für x ≤ x₀ | aus |
| `bPlay` | Knopf „▶ Prüfstelle wandern lassen" / „⏸ Pause" | x₀ läuft mit 1,0 pro Sekunde vom linken zum rechten Rand und hält dort; `dtFrame = Math.min(0.05, (jetzt − vorher)/1000)`; liegt x₀ schon am rechten Rand, startet er links | — |
| `bReset` | Knopf „Zurücksetzen" | a und x₀ auf die Startwerte der gewählten Schar, Checkboxen auf Startwerte, Animation stoppen | — |

Zusätzlich: **Ziehen** auf `cvF` setzt x₀ auf die nächste Reglerstufe (Pointer-Events mit
`setPointerCapture`, wie im Referenzmodul; die `touch-action`-Regel `pan-y` bleibt erhalten, damit die
Seite auf dem Handy scrollbar ist).

### 4.3 Canvas 1 `cvF` — der Graph

`<canvas id="cvF" width="1000" height="400">`, CSS `width:100%`.

**Feste Umrechnung (oben in der IIFE als Konstanten dokumentieren):**

```
LX = 70,  RX = 960   // linker/rechter Rand der Zeichenfläche (Pixel)
TY = 20,  BY = 360   // oberer/unterer Rand (Pixel)
px(x) = LX + (x - XMIN) / (XMAX - XMIN) * (RX - LX)
py(y) = BY - (y - YMIN) / (YMAX - YMIN) * (BY - TY)
```

XMIN/XMAX, YMIN/YMAX kommen aus der Tabelle in 4.1. Kontrollwerte, Schar 1 (x: −3 … 3, y: −6 … 6):
x = 0 → **515**; x = 2 → **811,67**; y = 0 → **190**; y = 6 → **20**; Punkt (2 | 0,67) → (811,67 | 171,11).
Die Achsen sind ungleich skaliert, und im Bild ist der Steigungswinkel deshalb **nicht** der
Steigungswinkel der Zahlen. Das steht als Randbemerkung unter dem Canvas (kleine graue Schrift):
„Achsen unterschiedlich skaliert: Beurteile Steigungen an den Messwerten, nicht am Winkel im Bild."

**Zeichenreihenfolge:**
1. Zeichenfläche mit hellem Gitter (Linien alle 1 Einheit), Achsen durch (0|0), Teilstriche und Zahlen
   (Schrift ≥ 13 px), Achsenbeschriftung „x" und „y".
2. Graph von f: Polylinie mit 400 Stützstellen, Breite 3 px, Farbe `--akzent`, mit `ctx.clip()` auf die
   Zeichenfläche.
3. Wenn `cSpur`: Spuren (punktiert, grau, 2 px): Extrempunkte (Schar 1: H und T auf einer gemeinsamen
   Kurve, Schar 2: ebenfalls, Schar 3: nur T) und Wendepunkte (Schar 2: senkrechte Linie, Schar 3:
   zweiter Wendepunkt). Über a von −1 bis a_max in 200 Schritten mit den Formeln aus K6. **Keine
   Beschriftung mit einer Gleichung** (siehe K8).
4. Wenn `cTan`: Tangente im Punkt (x₀ | f(x₀)) mit Steigung f′(x₀), gestrichelt orange `#b45309`,
   im Bild ±1,2 x-Einheiten lang.
5. Wendetangenten: dünn, strichpunktiert, orange, ±0,9 x-Einheiten in jedem Wendepunkt.
6. Markierungen: **Hochpunkt** roter Kreis `#b91c1c` (Radius 7, Buchstabe H), **Tiefpunkt** blauer Kreis
   `#1d4ed8` (T), **Wendepunkt** oranges Quadrat, um 45° gedreht (W), **Sattelpunkt** violettes Quadrat
   `#6d28d9` mit S (ersetzt W, wenn W zugleich waagerechte Tangente hat). Die Buchstaben stehen 10 px
   neben dem Symbol, damit sie sich nicht überdecken.
7. Prüfstelle: senkrechte punktierte Linie in x₀ über beide Canvas, gefüllter Punkt (Radius 6) auf dem
   Graphen.

### 4.4 Canvas 2 `cvAbl` — Ableitungen und Vorzeichenbänder (bauen sich mit auf)

`<canvas id="cvAbl" width="1000" height="330">`, CSS `width:100%`. Dieselben LX, RX wie `cvF`, damit
x-Werte senkrecht untereinander stehen. Oberer Teil: y = 15 … 220 mit dem y-Fenster der Ableitungen
(Tabelle 4.1). Darunter zwei Bänder:

- **f′-Band** y = 240 … 256, links Beschriftung „f′". Grün `#0d7a52` (35 % deckend), wo f′ > 0; rot
  `#b91c1c` (35 %), wo f′ < 0.
- **f″-Band** y = 266 … 282, Beschriftung „f″". Blau `#1d4ed8` (35 %), wo f″ > 0 (Linkskurve); orange
  `#b45309` (35 %), wo f″ < 0 (Rechtskurve).
- Darunter Legende in einer Zeile (Schrift ≥ 13 px).

Bänder werden in 445 Spalten (Breite 2 px) abgetastet; ein Wert mit |·| < 10⁻⁹ übernimmt das Vorzeichen
der vorigen Spalte (sonst entsteht an einer doppelten Nullstelle von f′ eine Lücke im Band, und **genau
dort darf kein Farbwechsel sichtbar sein**: Er ist das Erkennungszeichen des Sattelpunkts).

Kurven: f′ als durchgezogene blaue Linie (3 px, `#1d4ed8`), f″ als gestrichelte orange Linie (3 px,
`#b45309`), Nulllinie grau. Auf der Nulllinie markieren offene Kreise die **Nullstellen von f′** (für
Schar 3: bei x = 0 und x = a; ist a = 0, bei x = 0). Bei x₀ zwei gefüllte Punkte auf f′ und f″. Bei
aktiviertem `cAufbau` wird alles rechts von x₀ weggelassen (Kurven **und** Bänder). Die Kurve baut
sich damit beim Verschieben von x₀ (oder beim Abspielen) von links auf, und der Zusammenhang
**„Nullstelle von f′ ⇒ Stelle mit waagerechter Tangente in cvF"** und **„Extremstelle von f′ ⇒
Wendestelle von f"** wird beim Durchlaufen direkt sichtbar.

### 4.5 Anzeigen (`.anzeige`)

Alle Zahlen über `fmt(zahl, stellen)` mit Komma; ein Wert mit |v| < 0,005 wird als „0,00" angezeigt
(nie „−0,00").

| ID | Inhalt | Format | Start (Schar 1: a = 1,00; x₀ = 2,00) |
|---|---|---|---|
| `anzA` | Parameter | `a = 1,00` | 1,00 |
| `anzX0` | Prüfstelle | `x₀ = 2,00` | 2,00 |
| `anzF` | Funktionswert | 2 Stellen | **0,67** |
| `anzF1` | erste Ableitung | 2 Stellen | **3,00** |
| `anzF2` | zweite Ableitung | 2 Stellen | **4,00** |
| `anzArt` | Text | „steigt / fällt / waagerechte Tangente" + „· Linkskurve / Rechtskurve / f″ = 0" | „steigt · Linkskurve" |
| `anzExt` | Liste der Extrempunkte | „H(−1,00 \| 0,67) · T(1,00 \| −0,67)" oder „keine Extrempunkte" | H(−1,00 \| 0,67) · T(1,00 \| −0,67) |
| `anzWen` | Wendepunkt(e) mit Wendetangentensteigung | „W(0,00 \| 0,00), Steigung −1,00" | W(0,00 \| 0,00), Steigung −1,00 |
| `anzBefund` | Sonderfälle in einem Satz | siehe unten | leer („—") |

`anzBefund` zeigt nur in kritischen Zuständen einen **neutralen** Satz. Er nennt die Messtatsache,
aber weder den Parameterwert noch die Einordnung; die Einordnung liest man an den Markierungen (S, T)
und am Vorzeichenband ab und muss sie begründen:
- Schar 1 bei a = 0, Schar 2 bei a = 1 und Schar 3 bei jedem a, sobald x₀ auf einer Stelle mit f′ = 0 und f″ = 0 steht: „An dieser Stelle sind f′ und f″ beide null."
- sonst „—".

Die Markierungslegende unter `cvF` lautet: H Hochpunkt · T Tiefpunkt · W Wendepunkt · S Sattelpunkt
(Wendepunkt mit waagerechter Tangente).

### 4.6 Selbsttest gegen Handrechnung (Bauagent, vor Auslieferung)

Vor der Auslieferung mindestens diese Zustände einstellen und gegen K7 prüfen:
1. **Start Schar 1** (a = 1,00, x₀ = 2,00): 0,67 · 3,00 · 4,00 · H(−1,00 | 0,67) · T(1,00 | −0,67) · W(0,00 | 0,00), Steigung −1,00.
2. **Schar 1, a = 4,00, x₀ = 2,00**: f′(x₀) = 0,00 (Tangente waagerecht) · T(2,00 | −5,33).
3. **Start Schar 2** (a = −0,50, x₀ = 2,50): −2,29 · 0,75 · 3,00 · H(−0,22 | 0,06) · T(2,22 | −2,39) · W(1,00 | −1,17), Steigung −1,50.
4. **Schar 2, a = 0,95 / 1,00 / 1,05**, x₀ = 1,00: Steigung der Wendetangente −0,05 / 0,00 / +0,05; bei 1,00 nur Sattelpunkt (1,00 | 0,33), bei 0,95 H(0,78 | 0,29), T(1,22 | 0,28).
5. **Start Schar 3** (a = 1,00, x₀ = 2,00): 1,33 · 4,00 · 8,00 · T(1,00 | −0,08) · S(0,00 | 0,00) · W(0,67 | −0,05).
6. **Schar 3, a = 0,00, x₀ = 0,00**: f′ = f″ = 0,00, nur T(0,00 | 0,00) (kein S, kein W), `anzBefund` zeigt den neutralen Satz.
7. **Konsistenz**: Bei Schar 2 gilt f″(x₀ = 1,00) = 0,00 für jedes a; bei Schar 3 gilt f′(0) = f″(0) = 0,00 für jedes a.
8. **Bänder**: Schar 2 bei a = 1,00 — das f′-Band zeigt nirgends einen Farbwechsel (nur grün), das f″-Band wechselt bei x = 1 von orange nach blau. Schar 2 bei a = 0,00 — das f′-Band wechselt bei 0 von grün nach rot und bei 2 von rot nach grün.

### 4.7 Beobachtungsauftrag (`.auftrag`, wörtlich)

> **Beobachtungsauftrag.** Bei Schar 2 und Schar 3 kennst du die Formel nicht. Du untersuchst
> beide wie eine Messreihe: mit dem Graphen, den Messwerten an der Prüfstelle und den
> Vorzeichenbändern.
> **Teil 1 (Schar 2).** Erhöhe *a* von −1,00 in kleinen Schritten bis 2,00 und beobachte
> den Wendepunkt, die Extrempunkte und die Steigung der Wendetangente. Notiere für vier Werte
> von *a* die x-Werte von Hoch- und Tiefpunkt und die Steigung der Wendetangente. Finde den
> Wert von *a*, bei dem die Steigung der Wendetangente 0,00 ist, und beschreibe, was
> im selben Moment mit den beiden Extrempunkten geschieht. Formuliere:
> „Bei *a* = ___ fallen Hoch- und Tiefpunkt zusammen, weil ___."
> **Teil 2 (Schar 3).** Stelle die Prüfstelle auf x₀ = 0,00. Lies f′(0) und f″(0) für
> *a* = −1,00; 1,00; 2,00 und dann für *a* = 0,00 ab. Schau in beiden Bändern, ob f′ bei x = 0 das
> Vorzeichen wechselt. Formuliere: „Bei x = 0 liegt für *a* ≠ 0 ein ___, für *a* = 0 ein ___."
> **Zusatz (Schar 1).** Schalte „Ortskurve" ein, lies für *a* = 1,00 und *a* = 4,00 die Tiefpunkte ab
> und finde eine Gleichung, die zu **beiden** Punkten passt (Hilfe: Abschnitt 3.3).

**Warum diese Fragen nur in der Simulation zu beantworten sind.** Schar 2 und Schar 3 sind
verdeckt: Es gibt keinen Term, den man ableiten könnte. Der Wert a = 1,00, bei dem die Wendetangente
waagerecht wird, und die Sonderrolle der Stelle x = 0 in Schar 3 lassen sich nur an den Messwerten der
Anzeige erkennen. Im Erklärteil steht weder eine der drei Scharen noch der Effekt „Extrempunkte
verschmelzen zu einem Sattelpunkt bei einem bestimmten Parameterwert". Die Frage nach einer
Ortskurve zu Schar 1 ist als Zusatzauftrag ohne Multiple Choice angelegt, weil sie sich mit
Abschnitt 3.3 auch rechnen ließe.

### 4.8 Zwei Verständnisfragen direkt nach der Simulation

Beide im `.aufgabe`-Rahmen mit `.ab`-Chip *Anforderungsbereich II*, **vier Optionen**, jeweils mit
den drei Hilfestufen (siehe Abschnitt 5, Vorlage der Hilfen).

**MC `sim1`** — richtige Option: Index **2**

Frage (wörtlich): *Du hast in Schar 2 den Parameter a von −1,00 bis 2,00 verändert. Welche Beschreibung
trifft zu?*

| Index | Option |
|---|---|
| 0 | Alle drei markierten Punkte wandern gemeinsam nach rechts, ihr Abstand zueinander bleibt gleich. |
| 1 | Der Wendepunkt bleibt bei x = 1,00 stehen und wandert nur senkrecht. Hoch- und Tiefpunkt rücken zusammen und fallen bei a = 0,00 in einem Punkt zusammen; für a > 0 gibt es keine Extrempunkte mehr. |
| 2 | Der Wendepunkt bleibt bei x = 1,00 stehen und wandert nur senkrecht. Hoch- und Tiefpunkt rücken zusammen und fallen bei a = 1,00, wo die Wendetangente waagerecht ist, im Wendepunkt zusammen; für a > 1 gibt es keine Extrempunkte mehr. |
| 3 | Der Wendepunkt bleibt bei x = 1,00 stehen. Hoch- und Tiefpunkt haben bis a = 0,95 einen deutlichen Abstand und verschwinden dann plötzlich, ohne sich vorher angenähert zu haben. |

Feedback:
- 0: „Nur der Wendepunkt ändert seine Lage anders, als du beschreibst: Seine x-Koordinate bleibt bei 1,00. Hoch- und Tiefpunkt wandern nicht gemeinsam, sie rücken aufeinander zu: bei a = −1,00 stehen sie bei x = −0,41 und 2,41, bei a = 0,50 bei 0,29 und 1,71. Ein gleichbleibender Abstand ist nicht zu sehen."
- 1: „Die Bewegung hast du richtig beschrieben, aber den Wert von a verwechselt. Bei a = 0,00 zeigt die Anzeige noch H(0,00 | 0,00) und T(2,00 | −1,33), und die Wendetangente hat die Steigung −1,00. Das Zusammenfallen passiert dort, wo die Steigung der Wendetangente 0,00 anzeigt, und das ist erst bei a = 1,00 der Fall."
- 2: „Richtig. Der Wendepunkt bleibt bei x = 1,00, seine Höhe ist a − 0,67. Hoch- und Tiefpunkt liegen bei 1 ∓ √(1 − a) und rücken zusammen, bei a = 1,00 fallen sie im Wendepunkt zusammen (f′ hat dort eine doppelte Nullstelle, die Wendetangente ist waagerecht, es ist ein Sattelpunkt). Die verdeckte Formel war fₐ(x) = x³/3 − x² + a·x, also fₐ′(x) = x² − 2x + a mit Diskriminante 4 − 4a; sie ist null genau bei a = 1. Nachrechnen lohnt sich."
- 3: „Das Verschwinden ist kein Sprung. Bei a = 0,95 stehen Hoch- und Tiefpunkt noch bei x = 0,78 und 1,22, also nur 0,45 auseinander; bei a = 0,75 sind es 1,00. Der Abstand schrumpft stetig auf null. Wenn du den Regler in kleinen Schritten führst, siehst du beide Punkte langsam aufeinander zulaufen."

**MC `sim2`** — richtige Option: Index **1**

Frage (wörtlich): *In Schar 3 hast du die Prüfstelle auf x₀ = 0,00 gestellt und a = −1,00; 1,00; 2,00 und
danach 0,00 eingestellt. Welche Aussage über die Stelle x = 0 stimmt?*

| Index | Option |
|---|---|
| 0 | Für a ≠ 0 liegt dort ein Tiefpunkt (f′ und f″ sind null, f′ wechselt von − nach +), für a = 0 ein Sattelpunkt. |
| 1 | Für a ≠ 0 liegt dort ein Sattelpunkt (f′ und f″ sind null, f′ wechselt nicht das Vorzeichen). Für a = 0 wird daraus ein Tiefpunkt, obwohl f″(0) weiterhin null ist. |
| 2 | Für jedes a liegt dort ein Sattelpunkt (f′ und f″ sind null, f′ wechselt nie das Vorzeichen); der Tiefpunkt bei x = a kommt für a ≠ 0 dazu, für a = 0 verschwindet er. |
| 3 | Dort liegt für kein a etwas Besonderes vor: Weil f″(0) = 0 ist, kann bei x = 0 weder ein Extrempunkt noch ein Sattelpunkt sein. |

Feedback:
- 0: „Die beiden Fälle sind vertauscht. Für a = 1,00 zeigt das f′-Band bei x = 0 keinen Farbwechsel (links und rechts von 0 beide Male rot), also kein Extremum; für a = 0,00 wechselt es dagegen von rot nach grün, das ist der Tiefpunkt. Achte darauf, wann sich beim Durchgang durch x = 0 die Farbe ändert."
- 1: „Richtig. Für a ≠ 0 hat f′ bei x = 0 eine doppelte Nullstelle: f′(0) = f″(0) = 0 ohne Vorzeichenwechsel, das ist ein Sattelpunkt. Für a = 0 fallen die Stelle bei x = 0 und der Tiefpunkt bei x = a zusammen; das f′-Band wechselt jetzt von rot nach grün, obwohl f″(0) = 0 bleibt. Die verdeckte Formel war fₐ(x) = x⁴/4 − a·x³/3 mit fₐ′(x) = x²(x − a): Bei a = 0 ist f′ = x³ und wechselt das Vorzeichen; bei a ≠ 0 ist der Faktor x² nie negativ und der Faktor (x − a) ist in der Nähe von 0 vorzeichenkonstant (er hat dort das Vorzeichen von −a), also gibt es keinen Wechsel."
- 2: „Das gilt für a ≠ 0, aber nicht für a = 0. Dort zeigt die Simulation nur noch einen einzigen Punkt, T(0,00 | 0,00), und das f′-Band wechselt bei x = 0 von rot nach grün. Ein Sattelpunkt braucht, dass f′ das Vorzeichen nicht wechselt."
- 3: „Aus f″(0) = 0 folgt nichts: Die zweite Ableitung ist nur dann ein Test, wenn sie nicht null ist. Genau bei x = 0 ist f″(0) = 0,00 in allen Fällen, und trotzdem findet die Simulation für a ≠ 0 einen Sattelpunkt und für a = 0 einen Tiefpunkt. Entschieden wird über das Vorzeichen von f′ links und rechts, das siehst du im oberen Band."

**Hilfen zu `sim1`** (`data-hilfe="1|2|3"` im `.aufgabe`-Rahmen, Rollen wie in `bausteine.md`):
1. *Tipp:* „Achte auf die angezeigte Steigung der Wendetangente: Sie ändert sich mit a und geht dabei durch einen besonderen Wert."
2. *Ansatz:* „Stelle a nacheinander auf 0,00; 0,50; 0,95; 1,00 und 1,05 und notiere jedes Mal die x-Werte von Hoch- und Tiefpunkt, die Lage des Wendepunkts und die Steigung der Wendetangente. Vergleiche die Zeilen."
3. *Lösungsweg:* „a = 0,00: H(0,00 | 0,00), T(2,00 | −1,33), Steigung −1,00. a = 0,50: H(0,29 | 0,07), T(1,71 | −0,40), Steigung −0,50. a = 0,95: H(0,78 | 0,29), T(1,22 | 0,28), Steigung −0,05. a = 1,00: nur S(1,00 | 0,33), Steigung 0,00. a = 1,05: keine Extrempunkte, Steigung +0,05. Der Wendepunkt bleibt bei x = 1,00, die Extrempunkte rücken aufeinander zu und fallen bei a = 1,00 mit ihm zusammen, dort ist seine Tangente waagerecht."

**Hilfen zu `sim2`:**
1. *Tipp:* „Die Zahlen f′(0) und f″(0) allein reichen nicht. Schau auf das obere Band rund um x = 0: Ändert sich dort die Farbe?"
2. *Ansatz:* „Setze x₀ = 0,00, notiere f′(0) und f″(0) für a = −1,00; 1,00; 2,00 und 0,00 und prüfe jedes Mal, ob links und rechts von x = 0 dieselbe Farbe im f′-Band steht."
3. *Lösungsweg:* „In allen vier Fällen ist f′(0) = 0,00 und f″(0) = 0,00. Für a = −1,00 steht links und rechts von 0 grün, für a = 1,00 und 2,00 beide Male rot: kein Vorzeichenwechsel von f′, also ein Sattelpunkt S(0,00 | 0,00). Für a = 0,00 wechselt das Band von rot nach grün: Tiefpunkt T(0,00 | 0,00), obwohl f″(0) = 0,00 ist."

Nach den beiden Fragen ein `.hinweis`-Kasten (Abschluss des Abschnitts):

> **Was du mitnehmen solltest.** Eine waagerechte Tangente allein sagt nicht, was für ein Punkt vorliegt. Der Sattelpunkt ist der
> Übergang, an dem ein Hochpunkt und ein Tiefpunkt verschmelzen und verschwinden, und die zweite Ableitung
> kann dort versagen. Was zählt, ist der Vorzeichenwechsel, und den zeigt das Band.

---

## 5 · Übungen

`<section id="uebungen">`, `.stufe`-Kopf: Nr. **5**, Überschrift **Übungen**.

Zehn Aufgaben: zwei im Anforderungsbereich I, sechs im Anforderungsbereich II, zwei im
Anforderungsbereich III. Jede Aufgabe trägt einen `.ab`-Chip mit dem Anforderungsbereich und
**bekommt die drei Hilfestufen** (Tipp → Ansatz → Lösungsweg). Bei den offenen Aufgaben ist Stufe 3 ein
Lösungsgerüst mit den Schlüsselzahlen; die volle Musterlösung liegt in `data-stufe="9"`.

---

### Aufgabe 1 — `a1` · Zahleneingabe · Anforderungsbereich I

Aufgabentext (wörtlich):

> Gegeben ist <span class="m" data-tex="f(x) = x^3 - 6x^2 + 9x - 4" data-plain="f(x) = x³ − 6x² + 9x − 4"></span>.
> Bestimme die **y-Koordinate des Tiefpunkts** des Graphen.

**Einheitenliste im `<select>`:** `LE` · `FE` · `°` (Koordinaten sind Längen im Koordinatensystem; die anderen sind ein Flächeninhalt und ein Winkel).

**Eintrag in `numDaten`:**

```js
a1:{ wert:-4, einheit:"LE", tol:0.05,
     ok:"Richtig. f′(x) = 3x² − 12x + 9 = 3(x − 1)(x − 3), also x = 1 oder x = 3. f″(3) = 6 > 0 ⟹ Tiefpunkt bei x = 3, f(3) = 27 − 54 + 27 − 4 = −4.",
     falschEinheit:"Der Zahlenwert stimmt. Die y-Koordinate eines Punktes ist eine Länge im Koordinatensystem (LE). FE wäre ein Flächeninhalt, ° ein Winkel.",
     nah:"Du bist in der Nähe, aber es steckt ein Einsetzfehler drin. Rechne f(3) einzeln: 3³ = 27, −6·3² = −54, 9·3 = 27, dann −4. Summe: 27 − 54 + 27 − 4.",
     weit:"0 ist die y-Koordinate des Hochpunkts H(1 | 0), nicht des Tiefpunkts: Bei x = 1 ist f″(1) = −6 < 0. 3 ist die x-Koordinate des Tiefpunkts (die Stelle), gefragt ist aber sein y-Wert f(3). +4 ist das richtige Ergebnis mit falschem Vorzeichen: 27 − 54 = −27, plus 27 ergibt 0, minus 4 ergibt −4; der Tiefpunkt liegt unterhalb der x-Achse. Prüfe mit f″, welche der beiden Stellen zum Tiefpunkt gehört, und setze diese in f ein." }
```

**Hilfen:**

1. *Tipp:* „Es gibt zwei Stellen mit waagerechter Tangente, aber nur eine gehört zum Tiefpunkt. Und gefragt ist der y-Wert, nicht die Stelle."
2. *Ansatz:* „Löse <span class="m" data-tex="f'(x)=0" data-plain="f′(x) = 0"></span> (quadratische Gleichung), prüfe an beiden Lösungen das Vorzeichen von <span class="m" data-tex="f''" data-plain="f″"></span> und setze die Stelle mit <span class="m" data-tex="f''>0" data-plain="f″ > 0"></span> in <span class="m" data-tex="f" data-plain="f"></span> ein."
3. *Lösungsweg:* <span class="m" data-tex="f'(x)=3x^2-12x+9=3(x-1)(x-3)=0" data-plain="f′(x) = 3x² − 12x + 9 = 3(x − 1)(x − 3) = 0"></span>, also <span class="m" data-tex="x=1" data-plain="x = 1"></span> oder <span class="m" data-tex="x=3" data-plain="x = 3"></span>. Mit <span class="m" data-tex="f''(x)=6x-12" data-plain="f″(x) = 6x − 12"></span>: <span class="m" data-tex="f''(1)=-6<0" data-plain="f″(1) = −6 < 0"></span> Hochpunkt, <span class="m" data-tex="f''(3)=6>0" data-plain="f″(3) = 6 > 0"></span> Tiefpunkt. <span class="m" data-tex="f(3)=27-54+27-4=-4" data-plain="f(3) = 27 − 54 + 27 − 4 = −4"></span>, also <span class="m" data-tex="T(3\,|\,-4)" data-plain="T(3 | −4)"></span>. Kontrolle: <span class="m" data-tex="f(x)=(x-4)(x-1)^2" data-plain="f(x) = (x − 4)(x − 1)²"></span> hat bei <span class="m" data-tex="x=1" data-plain="x = 1"></span> die doppelte Nullstelle, dort liegt der Hochpunkt <span class="m" data-tex="H(1\,|\,0)" data-plain="H(1 | 0)"></span> ✓.

**Kontrollrechnung:** K10.

---

### Aufgabe 2 — `a2` · Zahleneingabe · Anforderungsbereich I

Aufgabentext (wörtlich):

> Gegeben ist <span class="m" data-tex="f(x) = x^3 - 6x^2 + 5x" data-plain="f(x) = x³ − 6x² + 5x"></span>.
> Bestimme die **Steigung der Wendetangente**.

**Einheitenliste:** `ohne Einheit` (`value="1"`) · `LE` · `°` · `FE`. Die Steigung ist ein Quotient
zweier Längen. `°` ist der plausible Distraktor (Steigungswinkel statt Steigung).

**Eintrag in `numDaten`:**

```js
a2:{ wert:-7, einheit:"1", tol:0.05,
     ok:"Richtig. f″(x) = 6x − 12 = 0 ⟹ x = 2, f‴ = 6 ≠ 0. Die Steigung dort ist f′(2) = 3·4 − 12·2 + 5 = −7.",
     falschEinheit:"Der Zahlenwert stimmt. Eine Steigung ist der Quotient zweier Längen und hat keine Einheit. In Grad wäre der Steigungswinkel angegeben, arctan(−7) ≈ −81,87°, und das ist eine andere Größe.",
     nah:"−6 ist der Funktionswert f(2), also die y-Koordinate des Wendepunkts, nicht die Steigung. Auch bei anderen Werten in dieser Nähe hast du vermutlich in f statt in f′ eingesetzt oder dich verrechnet. Die Steigung liefert f′(2) = 3·2² − 12·2 + 5.",
     weit:"2 ist die Wendestelle selbst, also die Stelle, an der du f′ auswerten sollst. 5 ist f′(0), die Steigung bei x = 0. +7 hat das falsche Vorzeichen: Die Wendetangente fällt, denn 3·4 = 12 und 12 − 24 = −12, plus 5 ergibt −7." }
```

**Hilfen:**

1. *Tipp:* „Die Wendestelle bestimmst du mit der zweiten Ableitung; die Steigung der Tangente aber mit der ersten."
2. *Ansatz:* „Löse <span class="m" data-tex="f''(x)=0" data-plain="f″(x) = 0"></span> und setze das Ergebnis in <span class="m" data-tex="f'" data-plain="f′"></span> ein, nicht in <span class="m" data-tex="f" data-plain="f"></span>."
3. *Lösungsweg:* <span class="m" data-tex="f'(x)=3x^2-12x+5" data-plain="f′(x) = 3x² − 12x + 5"></span>, <span class="m" data-tex="f''(x)=6x-12=0" data-plain="f″(x) = 6x − 12 = 0"></span> also <span class="m" data-tex="x_W=2" data-plain="x_W = 2"></span>, und <span class="m" data-tex="f'''(x)=6\neq0" data-plain="f‴(x) = 6 ≠ 0"></span> bestätigt die Wendestelle. <span class="m" data-tex="f'(2)=3\cdot4-12\cdot2+5=12-24+5=-7" data-plain="f′(2) = 3·4 − 12·2 + 5 = 12 − 24 + 5 = −7"></span>. Zur Einordnung: <span class="m" data-tex="f(2)=8-24+10=-6" data-plain="f(2) = 8 − 24 + 10 = −6"></span>, der Wendepunkt ist <span class="m" data-tex="W(2\,|\,-6)" data-plain="W(2 | −6)"></span>. Die Steigung <span class="m" data-tex="-7" data-plain="−7"></span> ist der kleinste Wert von <span class="m" data-tex="f'" data-plain="f′"></span> überhaupt: <span class="m" data-tex="f'(x)=3(x-2)^2-7" data-plain="f′(x) = 3(x − 2)² − 7"></span>.

**Kontrollrechnung:** K11 (dort auch arctan(−7) = −81,87°).

---

### Aufgabe 3 — `mc1` · Multiple Choice · Anforderungsbereich II — richtige Option: Index **3**

Frage (wörtlich):

> Für <span class="m" data-tex="f(x) = \tfrac12x^4 - 4x^3 + 9x^2 - 5" data-plain="f(x) = ½x⁴ − 4x³ + 9x² − 5"></span>
> ist <span class="m" data-tex="f'(x)=2x(x-3)^2" data-plain="f′(x) = 2x(x − 3)²"></span> und
> <span class="m" data-tex="f''(x)=6(x-1)(x-3)" data-plain="f″(x) = 6(x − 1)(x − 3)"></span>. Untersuche die Stelle
> <span class="m" data-tex="x=3" data-plain="x = 3"></span>. Welche Aussage ist **vollständig und richtig
> begründet**?

| Index | Option |
|---|---|
| 0 | Tiefpunkt, denn f′(3) = 0. |
| 1 | Weder Extrem- noch Wendepunkt, denn f″(3) = 0 liefert keine Entscheidung. |
| 2 | Wendepunkt, denn f″(3) = 0. Dass die Tangente dort waagerecht ist, ist Zufall. |
| 3 | Sattelpunkt: f′ wechselt bei x = 3 das Vorzeichen nicht (f′ = 2x(x − 3)² ist für x > 0 nie negativ), f″ wechselt es dagegen (von − nach +). Also ein Wendepunkt mit waagerechter Tangente. |

Feedback:
- 0: „f′(3) = 0 ist nur die notwendige Bedingung. Ob ein Tiefpunkt vorliegt, entscheidet der Vorzeichenwechsel von f′, und den gibt es nicht: f′ = 2x(x − 3)² ist für x > 0 nie negativ, weil (x − 3)² ein Quadrat ist. Bei x = 2,9 ist f′ = +0,058, bei x = 3,1 ist f′ = +0,062, beide Male positiv. Der Graph steigt durch die waagerechte Stelle hindurch."
- 1: „‚f″ = 0 liefert keine Entscheidung' stimmt für das f″-Kriterium, heißt aber nur: Du musst mit dem Vorzeichenwechsel weiterprüfen, nicht: Es passiert nichts. Und hier passiert etwas: f″ = 6(x − 1)(x − 3) wechselt bei x = 3 das Vorzeichen (−1,14 bei x = 2,9, +1,26 bei x = 3,1). Das ist eine Wendestelle."
- 2: „Das Ergebnis ‚Wendepunkt' stimmt, die Begründung reicht aber nicht: f″(3) = 0 ist nur notwendig (x⁴ hat bei 0 f″ = 0 und keinen Wendepunkt). Es fehlt der Vorzeichenwechsel von f″ oder f‴(3) = 12 ≠ 0. Außerdem ist die waagerechte Tangente kein Zufall, sondern macht den Punkt erst zum Sattelpunkt."
- 3: „Richtig, und das ist die vollständige Begründung. f′(3) = 0 (waagerecht), kein Vorzeichenwechsel von f′ ⟹ kein Extremum; f″(3) = 0 mit Vorzeichenwechsel (oder f‴(3) = 12 ≠ 0) ⟹ Wendepunkt (3 | 8,5). Waagerechte Tangente plus Wendepunkt heißt Sattelpunkt."

**Hilfen:**

1. *Tipp:* „Du hast zwei Kriterien zur Verfügung, und eines davon wird an dieser Stelle nichts liefern. Welches, und was bleibt dann?"
2. *Ansatz:* „Prüfe mit den gegebenen Termen das Vorzeichen von <span class="m" data-tex="f'" data-plain="f′"></span> links und rechts von 3, danach das von <span class="m" data-tex="f''" data-plain="f″"></span>. Ein Quadrat wie <span class="m" data-tex="(x-3)^2" data-plain="(x − 3)²"></span> ist nie negativ."
3. *Lösungsweg:* <span class="m" data-tex="f'(2{,}9)=2\cdot2{,}9\cdot0{,}01=0{,}058" data-plain="f′(2,9) = 2·2,9·0,01 = 0,058"></span> und <span class="m" data-tex="f'(3{,}1)=2\cdot3{,}1\cdot0{,}01=0{,}062" data-plain="f′(3,1) = 2·3,1·0,01 = 0,062"></span>: kein Vorzeichenwechsel, kein Extremum. <span class="m" data-tex="f''(2{,}9)=6\cdot1{,}9\cdot(-0{,}1)=-1{,}14" data-plain="f″(2,9) = 6·1,9·(−0,1) = −1,14"></span> und <span class="m" data-tex="f''(3{,}1)=6\cdot2{,}1\cdot0{,}1=1{,}26" data-plain="f″(3,1) = 6·2,1·0,1 = 1,26"></span>: Vorzeichenwechsel, Wendestelle. Kontrolle mit <span class="m" data-tex="f'''(x)=12x-24" data-plain="f‴(x) = 12x − 24"></span>: <span class="m" data-tex="f'''(3)=12\neq0" data-plain="f‴(3) = 12 ≠ 0"></span> ✓. Wegen <span class="m" data-tex="f'(3)=0" data-plain="f′(3) = 0"></span> ist es ein Sattelpunkt <span class="m" data-tex="S(3\,|\,8{,}5)" data-plain="S(3 | 8,5)"></span> mit <span class="m" data-tex="f(3)=40{,}5-108+81-5=8{,}5" data-plain="f(3) = 40,5 − 108 + 81 − 5 = 8,5"></span>.

**Kontrollrechnung:** K12.

---

### Aufgabe 4 — `a3` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Der Wasserstand eines Flusses wird für die ersten fünf Tage einer Beobachtung modelliert durch
> <span class="m" data-tex="h(t) = 0{,}1\,(t^3 - 6t^2 + 9t)" data-plain="h(t) = 0,1·(t³ − 6t² + 9t)"></span>
> (<span class="m" data-tex="h" data-plain="h"></span> in m, <span class="m" data-tex="t" data-plain="t"></span> in Tagen,
> <span class="m" data-tex="0\le t\le5" data-plain="0 ≤ t ≤ 5"></span>). Bestimme den **größten Wasserstand**
> in diesem Zeitraum.

**Einheitenliste:** `m` · `m/Tag` · `Tage` · `cm` (mit `alt`).

**Eintrag in `numDaten`:**

```js
a3:{ wert:2.0, einheit:"m", tol:0.02, alt:{wert:200, einheit:"cm"},
     ok:"Richtig. h′(t) = 0,3(t − 1)(t − 3): lokales Maximum bei t = 1 mit h(1) = 0,4 m, lokales Minimum bei t = 3 mit h(3) = 0. Der größte Wert liegt aber am Rand: h(5) = 0,1·(125 − 150 + 45) = 2,0 m.",
     falschEinheit:"Der Zahlenwert stimmt. Ein Wasserstand ist eine Länge: m (oder 200 cm). m/Tag wäre die Änderungsrate, Tage ein Zeitpunkt.",
     nah:"Prüfe das Einsetzen am Rand: h(5) = 0,1·(5³ − 6·5² + 9·5) = 0,1·(125 − 150 + 45). Liegt dein Wert zwischen 1 und 4, ist dir vermutlich beim Einsetzen ein Rechenfehler unterlaufen oder du hast einen anderen Randwert oder Zeitpunkt benutzt.",
     weit:"0,4 m ist nur das lokale Maximum bei t = 1 im Inneren des Intervalls; 0 ist das lokale Minimum bei t = 3 und zugleich der Randwert h(0). Bei einem Intervall reicht f′ = 0 nicht: Du musst die Randwerte h(0) und h(5) mit den lokalen Extremwerten vergleichen. 4 ist doppelt so groß wie der gesuchte Wert: Prüfe, ob du 5³ − 6·5² + 9·5 = 20 und den Faktor 0,1 (0,1·20 = 2,0) richtig verrechnet hast." }
```

**Hilfen:**

1. *Tipp:* „Was bedeutet die Angabe <span class="m" data-tex="0\le t\le5" data-plain="0 ≤ t ≤ 5"></span> für deine Kandidatenliste?"
2. *Ansatz:* „Kandidaten: die Nullstellen von <span class="m" data-tex="h'" data-plain="h′"></span> im Inneren und die Randwerte <span class="m" data-tex="h(0)" data-plain="h(0)"></span> und <span class="m" data-tex="h(5)" data-plain="h(5)"></span>. Berechne alle Funktionswerte und wähle den größten."
3. *Lösungsweg:* <span class="m" data-tex="h'(t)=0{,}1(3t^2-12t+9)=0{,}3(t-1)(t-3)" data-plain="h′(t) = 0,1·(3t² − 12t + 9) = 0,3·(t − 1)(t − 3)"></span>. Kandidaten im Inneren: <span class="m" data-tex="t=1" data-plain="t = 1"></span> und <span class="m" data-tex="t=3" data-plain="t = 3"></span>. Werte: <span class="m" data-tex="h(0)=0" data-plain="h(0) = 0"></span>, <span class="m" data-tex="h(1)=0{,}1\cdot4=0{,}4" data-plain="h(1) = 0,1·4 = 0,4"></span>, <span class="m" data-tex="h(3)=0{,}1\cdot(27-54+27)=0" data-plain="h(3) = 0,1·(27 − 54 + 27) = 0"></span>, <span class="m" data-tex="h(5)=0{,}1\cdot(125-150+45)=2{,}0" data-plain="h(5) = 0,1·(125 − 150 + 45) = 2,0"></span>. Der größte Wert ist <span class="m" data-tex="2{,}0\,\mathrm{m}" data-plain="2,0 m"></span> am **Rand** <span class="m" data-tex="t=5" data-plain="t = 5"></span>. Das lokale Maximum <span class="m" data-tex="0{,}4\,\mathrm{m}" data-plain="0,4 m"></span> bei <span class="m" data-tex="t=1" data-plain="t = 1"></span> ist nur ein lokales. Der Pegel steigt danach weiter, und die Modellgrenze bei <span class="m" data-tex="t=5" data-plain="t = 5"></span> schneidet den Anstieg ab.

**Kontrollrechnung:** K13.

---

### Aufgabe 5 — `a4` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Die Höhe eines Bambussprosses wird beschrieben durch
> <span class="m" data-tex="B(t) = -0{,}02\,t^3 + 0{,}6\,t^2" data-plain="B(t) = −0,02·t³ + 0,6·t²"></span>
> (<span class="m" data-tex="B" data-plain="B"></span> in cm, <span class="m" data-tex="t" data-plain="t"></span> in Tagen,
> <span class="m" data-tex="0\le t\le20" data-plain="0 ≤ t ≤ 20"></span>). Bestimme die **größte
> Wachstumsgeschwindigkeit** in diesem Zeitraum.

**Einheitenliste:** `cm/Tag` · `cm` · `Tage` · `cm²`.

**Eintrag in `numDaten`:**

```js
a4:{ wert:6, einheit:"cm/Tag", tol:0.05,
     ok:"Richtig. Die Wachstumsgeschwindigkeit ist B′(t) = −0,06t² + 1,2t. Ihr Maximum liegt bei B″(t) = −0,12t + 1,2 = 0, also t = 10 (eine Wendestelle von B), und dort ist B′(10) = −6 + 12 = 6 cm pro Tag. Die Randwerte B′(0) = B′(20) = 0 sind kleiner.",
     falschEinheit:"Der Zahlenwert stimmt. Eine Geschwindigkeit des Wachstums ist eine Länge pro Zeit (cm/Tag). cm wäre die Höhe selbst, Tage ein Zeitpunkt, cm² eine Fläche.",
     nah:"10 ist die Wendestelle von B, also der Zeitpunkt, zu dem das Wachstum am schnellsten ist (Einheit: Tage). Gefragt ist aber die Geschwindigkeit selbst, also B′(10). Auch bei anderen Werten in dieser Nähe hast du vermutlich in B oder B″ statt in B′ eingesetzt.",
     weit:"40 cm ist die Höhe B(10) und 80 cm die Endhöhe B(20), das sind Bestände. Gefragt ist die Änderungsrate des Bestands, also B′. 0 sind nur die Randwerte von B′. Bestimme das Maximum der Funktion B′, dazu brauchst du B″. 12 ist nur der lineare Summand 1,2t von B′ bei t = 10; der Term −0,06t² gehört mit dazu (−6 + 12 = 6)." }
```

**Hilfen:**

1. *Tipp:* „Die Geschwindigkeit ist selbst eine Funktion der Zeit. Gesucht ist deren größter Wert."
2. *Ansatz:* „Die Wachstumsgeschwindigkeit ist <span class="m" data-tex="B'(t)" data-plain="B′(t)"></span>. Bestimme die Extremstelle von <span class="m" data-tex="B'" data-plain="B′"></span> mit <span class="m" data-tex="B''(t)=0" data-plain="B″(t) = 0"></span> und prüfe mit <span class="m" data-tex="B'''" data-plain="B‴"></span>, dass es ein Maximum ist. Vergleiche mit den Randwerten von <span class="m" data-tex="B'" data-plain="B′"></span>."
3. *Lösungsweg:* <span class="m" data-tex="B'(t)=-0{,}06t^2+1{,}2t=0{,}06\,t\,(20-t)" data-plain="B′(t) = −0,06t² + 1,2t = 0,06·t·(20 − t)"></span>. <span class="m" data-tex="B''(t)=-0{,}12t+1{,}2=0" data-plain="B″(t) = −0,12t + 1,2 = 0"></span> ergibt <span class="m" data-tex="t=10" data-plain="t = 10"></span>, und <span class="m" data-tex="B'''=-0{,}12<0" data-plain="B‴ = −0,12 < 0"></span> zeigt: Maximum von <span class="m" data-tex="B'" data-plain="B′"></span>. <span class="m" data-tex="B'(10)=-0{,}06\cdot100+12=-6+12=6" data-plain="B′(10) = −0,06·100 + 12 = −6 + 12 = 6"></span> cm/Tag. Ränder: <span class="m" data-tex="B'(0)=0" data-plain="B′(0) = 0"></span>, <span class="m" data-tex="B'(20)=-24+24=0" data-plain="B′(20) = −24 + 24 = 0"></span>. Also <span class="m" data-tex="6\,\mathrm{cm/Tag}" data-plain="6 cm/Tag"></span>. Merke: **Die größte Änderungsrate liegt an einer Wendestelle des Bestands.**

**Kontrollrechnung:** K14.

---

### Aufgabe 6 — `a5` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Für jedes <span class="m" data-tex="a" data-plain="a"></span> ist
> <span class="m" data-tex="f_a(x) = x^3 - 6x^2 + a\,x" data-plain="f_a(x) = x³ − 6x² + a·x"></span> eine Funktion.
> Bestimme den Wert von <span class="m" data-tex="a" data-plain="a"></span>, für den der Graph von
> <span class="m" data-tex="f_a" data-plain="f_a"></span> **genau eine** Stelle mit waagerechter Tangente hat.

**Einheitenliste:** `ohne Einheit` (`value="1"`) · `LE` · `°` · `FE`.

**Eintrag in `numDaten`:**

```js
a5:{ wert:12, einheit:"1", tol:0.05,
     ok:"Richtig. f_a′(x) = 3x² − 12x + a hat genau eine Nullstelle, wenn die Diskriminante 144 − 12a null ist, also a = 12. Dann ist f′ = 3(x − 2)² und der Sattelpunkt liegt bei (2 | 8).",
     falschEinheit:"Der Zahlenwert stimmt. Der Parameter a hat hier keine Einheit; gefragt ist eine reine Zahl.",
     nah:"9 ist der Wert, bei dem f′(1) = 0 gilt (Extrempunkt bei x = 1): Dort gibt es aber zwei Stellen mit waagerechter Tangente, x = 1 und x = 3, denn 3x² − 12x + 9 = 3(x − 1)(x − 3). Gesucht ist der Wert, bei dem beide Stellen zu einer zusammenfallen, also die Diskriminante von f′ null wird.",
     weit:"4 entsteht, wenn du 3x² − 12x + a durch 3 teilst, aber a nicht mitteilst: Aus x² − 4x + a/3 = 0 wird bei dir x² − 4x + a = 0 mit Diskriminante 16 − 4a. 36 entsteht, wenn du bei der Diskriminante den Faktor 3 von 3x² vergisst (144 − 4a). Wende die Diskriminante b² − 4ac direkt auf 3x² − 12x + a an: 144 − 12a. Wer auf 6 kommt, hat die Gleichung 144 − 12a = 0 vermutlich falsch aufgelöst: Bei a = 6 ist D = 72 > 0, es gäbe also noch zwei Stellen." }
```

**Hilfen:**

1. *Tipp:* „Waagerechte Tangenten sind Nullstellen von <span class="m" data-tex="f_a'" data-plain="f_a′"></span>. Wie viele Nullstellen kann eine quadratische Funktion haben, und wann ist es genau eine?"
2. *Ansatz:* „Berechne <span class="m" data-tex="f_a'(x)=3x^2-12x+a" data-plain="f_a′(x) = 3x² − 12x + a"></span> und setze die Diskriminante <span class="m" data-tex="b^2-4ac" data-plain="b² − 4ac"></span> dieser quadratischen Funktion gleich null."
3. *Lösungsweg:* <span class="m" data-tex="D=(-12)^2-4\cdot3\cdot a=144-12a=0" data-plain="D = (−12)² − 4·3·a = 144 − 12a = 0"></span>, also <span class="m" data-tex="a=12" data-plain="a = 12"></span>. Dann ist <span class="m" data-tex="f_{12}'(x)=3x^2-12x+12=3(x-2)^2" data-plain="f₁₂′(x) = 3x² − 12x + 12 = 3(x − 2)²"></span> mit der doppelten Nullstelle <span class="m" data-tex="x=2" data-plain="x = 2"></span>. Probe: <span class="m" data-tex="f_{12}''(2)=6\cdot2-12=0" data-plain="f₁₂″(2) = 6·2 − 12 = 0"></span>, <span class="m" data-tex="f_{12}'" data-plain="f₁₂′"></span> wechselt nicht das Vorzeichen (ein Quadrat), also ein Sattelpunkt <span class="m" data-tex="S(2\,|\,8)" data-plain="S(2 | 8)"></span>. Gegenprobe: <span class="m" data-tex="a=11" data-plain="a = 11"></span> ergibt <span class="m" data-tex="D=12>0" data-plain="D = 12 > 0"></span> (zwei Stellen), <span class="m" data-tex="a=13" data-plain="a = 13"></span> ergibt <span class="m" data-tex="D=-12<0" data-plain="D = −12 < 0"></span> (keine).

**Kontrollrechnung:** K15.

---

### Aufgabe 6a — `a8` · offene Aufgabe · Anforderungsbereich II (Nachtrag nach Fachprüfung M4)

Steht im Modul zwischen `a5` und `z1`. Aufgabentext (wörtlich):

> Für jedes t ist f_t(x) = x³ − 3t²·x eine Funktion.
> **(a)** Bestimme die Extrempunkte von f_t in Abhängigkeit von t mit vollständiger Fallunterscheidung.
> **(b)** Bestimme die Gleichung der Ortskurve, auf der alle Extrempunkte liegen.

`<textarea>` mit Platzhalter „Deine Lösung mit Fallunterscheidung und Ortskurve…“, Musterlösung über `data-loesung="a8"`. Dreistufige Hilfe:
1. *Tipp:* Beim Ableiten nach x ist t eine Konstante; das Vorzeichen von f_t″ an den beiden Extremstellen hängt vom Vorzeichen von t ab: Unterscheide die Fälle t > 0, t < 0 und t = 0.
2. *Ansatz:* f_t′(x) = 3x² − 3t², faktorisieren, Extremstellen ablesen, mit f_t″(x) = 6x das Vorzeichen je Fall prüfen; für die Ortskurve beide Punkte in Abhängigkeit von t aufschreiben und t eliminieren.
3. *Lösungsgerüst* (Knopf „Lösungsgerüst“, nur Schlüsselzahlen): f_t′ = 3(x − t)(x + t), f_t″ = 6x, f_t(t) = −2t³, f_t(−t) = 2t³. Gliederung: drei Fälle · beide Punkte getrennt in Abhängigkeit von t parametrisieren und t eliminieren · Probe mit t = 2. Die volle Lösung steht nur in `data-stufe="9"`.

Musterlösung: siehe Modul (`data-stufe="9"`), Bewertungskriterien enthalten. Sie hält fest, dass y = −2x³ dieselbe Gleichung ist wie bei den Wendepunkten in 3.2 (beide Punktfamilien haben die Form (t | −2t³)), und fordert zum Nachprüfen auf. Der Export hängt den Text der Textarea an (nicht über `ergebnisse`); die Textareas von `a8`, `a6`, `a7` tragen `data-offen` mit sprechender Beschriftung, der Export nutzt `ta.dataset.offen || ("Offene Aufgabe " + (i+1))`.
Die Funktion ist bewusst nicht die aus 3.2 (x³ − 3t·x²), damit die Lösung nicht im Erklärteil nachzulesen ist.

**Kontrollrechnung:** K20.

---

### Aufgabe 7 — `z1` · Zuordnung · Anforderungsbereich II

Aufgabentext (wörtlich):

> Die vier Diagramme zeigen jeweils den Graphen der **Ableitung** <span class="m" data-tex="f'" data-plain="f′"></span>
> einer ganzrationalen Funktion <span class="m" data-tex="f" data-plain="f"></span> (nicht den Graphen von
> <span class="m" data-tex="f" data-plain="f"></span> selbst!). Ordne jeder Beschreibung von
> <span class="m" data-tex="f" data-plain="f"></span> das passende Diagramm zu.

**Diagramme (Inline-SVG in `.diagramme`, je `viewBox="0 0 220 160"`, Breite 100 %, `figure` mit `figcaption` A–D):**
Gemeinsame Umrechnung: Ursprung bei (110 | 80), **60 Pixel pro x-Einheit, 28 Pixel pro y-Einheit**
(y nach oben), x-Bereich −1,6 … 1,6, Punkte im Abstand 0,2. Achsen als Linien: waagerecht von (10 | 80) bis (210 | 80),
senkrecht von (110 | 10) bis (110 | 150), Teilstriche bei x = ±1 (Pixel 50 und 170), Beschriftung „f′" am oberen Ende der
y-Achse. Kurven als `<polyline>` in `--akzent`, Strichbreite 2,5, ohne Füllung:

| Diagramm | f′(x) | `points` (fertig berechnet) |
|---|---|---|
| **A** | −x | `14,35 26,41 38,46 50,52 62,58 74,63 86,69 98,74 110,80 122,86 134,91 146,97 158,102 170,108 182,114 194,119 206,125` |
| **B** | x³ − x | `14,150 26,118 38,95 50,80 62,72 74,69 86,71 98,75 110,80 122,85 134,89 146,91 158,88 170,80 182,65 194,42 206,10` |
| **C** | x² − 1 | `14,36 26,53 38,68 50,80 62,90 74,98 86,104 98,107 110,108 122,107 134,104 146,98 158,90 170,80 182,68 194,53 206,36` |
| **D** | x² | `14,8 26,25 38,40 50,52 62,62 74,70 86,76 98,79 110,80 122,79 134,76 146,70 158,62 170,52 182,40 194,25 206,8` |

Die Kurven liegen auf ganze Pixel gerundet; die Rundung ist mit bloßem Auge nicht sichtbar. In der Aufgabe
selbst stehen die **Funktionsgleichungen nicht** dabei.

**Zeilen (in dieser Reihenfolge, sie entspricht nicht der Diagrammreihenfolge):**

| Zeile | Beschreibung | `data-loesung` |
|---|---|---|
| 1 | f hat genau zwei Extrempunkte und genau einen Wendepunkt. | **C** |
| 2 | f hat drei Extrempunkte und zwei Wendepunkte. | **B** |
| 3 | f hat genau eine Stelle mit waagerechter Tangente, aber keinen Extrempunkt. | **D** |
| 4 | f hat genau einen Extrempunkt, und der ist ein Hochpunkt; einen Wendepunkt gibt es nicht. | **A** |

Jedes `<select>` bietet `…`, `A`, `B`, `C`, `D`. Lösungsfolge **C · B · D · A**.

**Rückmeldungen (Zuordnungs-Engine, in der Zuordnung `ergebnisse.z1` setzen):**
- alle vier richtig: „Richtig. Vorgehen: Nullstellen von f′ zählen, dabei zwischen Schneiden (Vorzeichenwechsel: Extrempunkt) und Berühren (waagerechte Tangente ohne Extremum) unterscheiden; dann die Gipfel und Täler von f′ zählen, denn jede Extremstelle von f′ ist eine Wendestelle von f."
- Teilerfolg: „n von 4 stimmen. Deine Denkstrategie prüfen: Die Diagramme zeigen f′. Zähle zuerst, wo der Graph die x-Achse schneidet, dort wechselt f′ das Vorzeichen (Extrempunkt von f), und wo er sie nur berührt (waagerechte Tangente von f ohne Extrempunkt). Zähle dann die höchsten und tiefsten Stellen des Diagramms im Inneren: Jede ist eine Wendestelle von f. Kontrolliere die Zeilen, die du für falsch hältst, gegen genau diese beiden Zählungen."
- keine richtig: „Keine Zuordnung stimmt. Vermutlich hast du die Diagramme als Graphen von f gelesen. Sie zeigen aber f′: Eine Nullstelle im Diagramm heißt waagerechte Tangente von f, und die Extrempunkte von f stehen dort, wo das Diagramm die x-Achse durchquert."

**Hilfen:**

1. *Tipp:* „Lies die Diagramme als Bild der Steigung von f: Wo ist die Steigung null, und wo ändert sie sich am schnellsten?"
2. *Ansatz:* „Extremstellen von <span class="m" data-tex="f" data-plain="f"></span> = Nullstellen von <span class="m" data-tex="f'" data-plain="f′"></span> **mit** Vorzeichenwechsel (Schnittpunkte mit der x-Achse). Wendestellen von <span class="m" data-tex="f" data-plain="f"></span> = Extremstellen von <span class="m" data-tex="f'" data-plain="f′"></span> (Gipfel und Täler im Diagramm)."
3. *Lösungsweg:* A: <span class="m" data-tex="f'=-x" data-plain="f′ = −x"></span>, eine Nullstelle mit Wechsel von + nach −, kein Gipfel oder Tal: ein Hochpunkt, kein Wendepunkt. B: <span class="m" data-tex="f'=x^3-x" data-plain="f′ = x³ − x"></span>, drei Nullstellen mit Wechsel, zwei Extrema von <span class="m" data-tex="f'" data-plain="f′"></span> (bei <span class="m" data-tex="x=\pm0{,}58" data-plain="x = ±0,58"></span>): drei Extrem- und zwei Wendepunkte. C: <span class="m" data-tex="f'=x^2-1" data-plain="f′ = x² − 1"></span>, zwei Nullstellen mit Wechsel, ein Tal bei <span class="m" data-tex="x=0" data-plain="x = 0"></span>: zwei Extrem- und ein Wendepunkt. D: <span class="m" data-tex="f'=x^2" data-plain="f′ = x²"></span>, eine Nullstelle **ohne** Wechsel (Berührung), ein Tal bei 0: waagerechte Tangente ohne Extremum, also ein Sattelpunkt. Zugehörige Funktionen: <span class="m" data-tex="-\tfrac{x^2}{2}" data-plain="−x²/2"></span>, <span class="m" data-tex="\tfrac{x^4}{4}-\tfrac{x^2}{2}" data-plain="x⁴/4 − x²/2"></span>, <span class="m" data-tex="\tfrac{x^3}{3}-x" data-plain="x³/3 − x"></span>, <span class="m" data-tex="\tfrac{x^3}{3}" data-plain="x³/3"></span>.

**Kontrollrechnung:** K16.

---

### Aufgabe 8 — `a6` · offene Aufgabe · Anforderungsbereich III

Aufgabentext (wörtlich):

> Eine Schülerin untersucht <span class="m" data-tex="f(x)=x^4-4x^3" data-plain="f(x) = x⁴ − 4x³"></span> und schreibt:
> **(1)** <span class="m" data-tex="f'(x)=4x^3-12x^2=4x^2(x-3)" data-plain="f′(x) = 4x³ − 12x² = 4x²(x − 3)"></span>, also
> <span class="m" data-tex="f'(x)=0" data-plain="f′(x) = 0"></span> für <span class="m" data-tex="x=0" data-plain="x = 0"></span> und
> <span class="m" data-tex="x=3" data-plain="x = 3"></span>.
> **(2)** <span class="m" data-tex="f''(x)=12x^2-24x" data-plain="f″(x) = 12x² − 24x"></span>; wegen
> <span class="m" data-tex="f''(3)=36>0" data-plain="f″(3) = 36 > 0"></span> Tiefpunkt
> <span class="m" data-tex="T(3\,|\,-27)" data-plain="T(3 | −27)"></span>.
> **(3)** „Es ist <span class="m" data-tex="f''(0)=0" data-plain="f″(0) = 0"></span>, also liegt bei
> <span class="m" data-tex="x=0" data-plain="x = 0"></span> kein Extremum vor."
> **(4)** <span class="m" data-tex="f''(x)=12x(x-2)=0" data-plain="f″(x) = 12x(x − 2) = 0"></span> für
> <span class="m" data-tex="x=0" data-plain="x = 0"></span> und <span class="m" data-tex="x=2" data-plain="x = 2"></span>;
> „das sind die Wendestellen".
> **(5)** Wendepunkte <span class="m" data-tex="W_1(0\,|\,0)" data-plain="W₁(0 | 0)"></span> und
> <span class="m" data-tex="W_2(2\,|\,-8)" data-plain="W₂(2 | −8)"></span>.
> **Beurteile die Lösung Schritt für Schritt:** Welche Ergebnisse stimmen, welche Begründungen tragen nicht,
> was fehlt, und wo steckt ein Rechenfehler? Gib die korrekte Angabe für Schritt (5) an.

`<textarea>` mit Platzhalter „Deine Beurteilung…", darunter `<button data-loesung="a6">Musterlösung anzeigen</button>`.

**Hilfen:**

1. *Tipp:* „Prüfe jeden Schritt zweifach: Stimmt das Ergebnis? Und würde dieselbe Begründung auch bei <span class="m" data-tex="x^4" data-plain="x⁴"></span> zu einem richtigen Ergebnis führen?"
2. *Ansatz:* „Lege eine Tabelle mit den Spalten ‚Ergebnis richtig?' und ‚Begründung ausreichend?' an. Für (3) brauchst du das Vorzeichen von <span class="m" data-tex="f'" data-plain="f′"></span> links und rechts von 0, für (4) den Wert von <span class="m" data-tex="f'''" data-plain="f‴"></span> an den beiden Stellen, für (5) den Funktionswert <span class="m" data-tex="f(2)" data-plain="f(2)"></span>."
3. *Lösungsgerüst:* „(1) und (2) stimmen. Zu (3): <span class="m" data-tex="f'(-0{,}1)=-0{,}124" data-plain="f′(−0,1) = −0,124"></span> und <span class="m" data-tex="f'(0{,}1)=-0{,}116" data-plain="f′(0,1) = −0,116"></span>. Zu (4): <span class="m" data-tex="f'''(x)=24x-24" data-plain="f‴(x) = 24x − 24"></span>, also <span class="m" data-tex="f'''(0)=-24" data-plain="f‴(0) = −24"></span> und <span class="m" data-tex="f'''(2)=24" data-plain="f‴(2) = 24"></span>. Zu (5): <span class="m" data-tex="f(2)=16-32" data-plain="f(2) = 16 − 32"></span>. Gliedere deine Antwort: was stimmt · Lücke in (3) · Lücke in (4) · Rechenfehler in (5) · Fazit."

**Musterlösung in `.hilfe-text[data-stufe="9"]`:**

> **Erwartete Argumentation.**
> **(1)** richtig: <span class="m" data-tex="f'(x)=4x^2(x-3)" data-plain="f′(x) = 4x²(x − 3)"></span>, Nullstellen 0 und 3.
> **(2)** richtig: <span class="m" data-tex="f''(3)=12\cdot9-24\cdot3=36>0" data-plain="f″(3) = 12·9 − 24·3 = 36 > 0"></span> und
> <span class="m" data-tex="f(3)=81-108=-27" data-plain="f(3) = 81 − 108 = −27"></span>.
> **(3)** Das **Ergebnis** stimmt (bei 0 liegt kein Extremum), die **Begründung** nicht. Aus
> <span class="m" data-tex="f''(0)=0" data-plain="f″(0) = 0"></span> folgt weder „Extremum" noch „kein Extremum":
> Bei <span class="m" data-tex="x^4" data-plain="x⁴"></span> ist <span class="m" data-tex="f''(0)=0" data-plain="f″(0) = 0"></span> und es
> gibt dort einen Tiefpunkt. Die Schülerin hätte auf den Vorzeichenwechsel von
> <span class="m" data-tex="f'" data-plain="f′"></span> zurückgreifen müssen:
> <span class="m" data-tex="f'(-0{,}1)=-0{,}124<0" data-plain="f′(−0,1) = −0,124 < 0"></span> und
> <span class="m" data-tex="f'(0{,}1)=-0{,}116<0" data-plain="f′(0,1) = −0,116 < 0"></span>: kein Wechsel
> (das Quadrat <span class="m" data-tex="x^2" data-plain="x²"></span> in <span class="m" data-tex="f'" data-plain="f′"></span> ist nie negativ,
> <span class="m" data-tex="x-3" data-plain="x − 3"></span> bleibt in der Nähe von 0 negativ), also kein Extremum, sondern
> eine waagerechte Tangente ohne Extremum.
> **(4)** Notwendig, aber nicht hinreichend. Ergänzen: <span class="m" data-tex="f'''(x)=24x-24" data-plain="f‴(x) = 24x − 24"></span>,
> <span class="m" data-tex="f'''(0)=-24\neq0" data-plain="f‴(0) = −24 ≠ 0"></span> und
> <span class="m" data-tex="f'''(2)=24\neq0" data-plain="f‴(2) = 24 ≠ 0"></span>, oder Vorzeichenwechsel von
> <span class="m" data-tex="f''" data-plain="f″"></span> (bei −0,1 / 0,1: +2,52 / −2,28; bei 1,9 / 2,1: −2,28 / +2,52). Damit sind beide
> Stellen tatsächlich Wendestellen.
> **(5)** <span class="m" data-tex="W_1(0\,|\,0)" data-plain="W₁(0 | 0)"></span> stimmt, und wegen
> <span class="m" data-tex="f'(0)=0" data-plain="f′(0) = 0"></span> ist es sogar ein **Sattelpunkt**, den die Schülerin nicht
> benennt. <span class="m" data-tex="W_2" data-plain="W₂"></span> ist falsch: Es ist
> <span class="m" data-tex="f(2)=2^4-4\cdot2^3=16-32=-16" data-plain="f(2) = 2⁴ − 4·2³ = 16 − 32 = −16"></span>, also
> <span class="m" data-tex="W_2(2\,|\,-16)" data-plain="W₂(2 | −16)"></span> (die Steigung der Wendetangente ist
> <span class="m" data-tex="f'(2)=32-48=-16" data-plain="f′(2) = 32 − 48 = −16"></span>).
> **Fazit:** Die Lösung landet bei allen Stellen und beim Tiefpunkt auf richtigen Ergebnissen, hat aber zwei
> tragende Begründungslücken (3) und (4) und einen Rechenfehler. Gefährlich ist (3): dieselbe
> Argumentation führt bei <span class="m" data-tex="x^4" data-plain="x⁴"></span> zu einem falschen Ergebnis.
>
> **Bewertungskriterien.** Schritte (1) und (2) als richtig erkannt · Schritt (3) als
> Ergebnis-richtig-aber-Begründung-ungültig erkannt, mit Gegenbeispiel <span class="m" data-tex="x^4" data-plain="x⁴"></span> ·
> Ersatzbegründung über den Vorzeichenwechsel von <span class="m" data-tex="f'" data-plain="f′"></span> mit Zahlenwerten ·
> Lücke in (4) benannt (nur notwendige Bedingung) und behoben mit
> <span class="m" data-tex="f'''\neq0" data-plain="f‴ ≠ 0"></span> oder Vorzeichenwechsel · Rechenfehler in (5) gefunden und
> <span class="m" data-tex="W_2(2\,|\,-16)" data-plain="W₂(2 | −16)"></span> korrekt angegeben · Sattelpunkt bei <span class="m" data-tex="x=0" data-plain="x = 0"></span> erkannt (Zusatz) ·
> saubere Trennung von „Ergebnis richtig" und „Begründung tragfähig".

**Kontrollrechnung:** K17.

---

### Aufgabe 9 — `a7` · offene Aufgabe · Anforderungsbereich III

Aufgabentext (wörtlich):

> Für jeden Wert von <span class="m" data-tex="a" data-plain="a"></span> ist
> <span class="m" data-tex="f_a(x)=x^3+a\,x^2+x" data-plain="f_a(x) = x³ + a·x² + x"></span> eine Funktion. Ein Schüler behauptet:
> „Für jedes <span class="m" data-tex="a" data-plain="a"></span> hat der Graph von <span class="m" data-tex="f_a" data-plain="f_a"></span> einen Hochpunkt und einen Tiefpunkt,
> denn jede Funktion dritten Grades sieht so aus."
> **(a)** Nimm Stellung und belege deine Bewertung mit einem konkreten Parameterwert.
> **(b)** Gib an, für welche Werte von <span class="m" data-tex="a" data-plain="a"></span> es Extrempunkte gibt, und begründe,
> was am Übergang passiert.
> **(c)** Begründe, dass der Graph für **jedes** <span class="m" data-tex="a" data-plain="a"></span> genau einen Wendepunkt hat.

`<textarea>` mit Platzhalter „Deine Stellungnahme…", darunter `<button data-loesung="a7">Musterlösung anzeigen</button>`.

**Hilfen:**

1. *Tipp:* „Ob es Extrempunkte gibt, hängt davon ab, ob die **erste** Ableitung Nullstellen hat, und das ist eine quadratische Gleichung mit dem Parameter."
2. *Ansatz:* „Bestimme <span class="m" data-tex="f_a'" data-plain="f_a′"></span> und untersuche mit der Diskriminante, für welche <span class="m" data-tex="a" data-plain="a"></span> es zwei, eine oder keine Nullstelle gibt. Für die Wendestelle brauchst du <span class="m" data-tex="f_a''" data-plain="f_a″"></span> und <span class="m" data-tex="f_a'''" data-plain="f_a‴"></span>."
3. *Lösungsgerüst:* „<span class="m" data-tex="f_a'(x)=3x^2+2ax+1" data-plain="f_a′(x) = 3x² + 2a·x + 1"></span>, Diskriminante <span class="m" data-tex="D=4a^2-12" data-plain="D = 4a² − 12"></span>. Gegenbeispiel <span class="m" data-tex="a=0" data-plain="a = 0"></span>: <span class="m" data-tex="f'=3x^2+1>0" data-plain="f′ = 3x² + 1 > 0"></span>. Übergang bei <span class="m" data-tex="D=0" data-plain="D = 0"></span>, also <span class="m" data-tex="a=\pm\sqrt3" data-plain="a = ±√3"></span>. Wendestelle: <span class="m" data-tex="f_a''(x)=6x+2a=0" data-plain="f_a″(x) = 6x + 2a = 0"></span> ergibt <span class="m" data-tex="x=-a/3" data-plain="x = −a/3"></span>, und <span class="m" data-tex="f_a'''=6" data-plain="f_a‴ = 6"></span>. Gliedere: Urteil · Gegenbeispiel · Bedingung an <span class="m" data-tex="a" data-plain="a"></span> · Übergang · Wendepunkt."

**Musterlösung in `.hilfe-text[data-stufe="9"]`:**

> **Erwartete Argumentation.**
> **(a)** Die Behauptung ist **falsch**. Dass der Graph einer kubischen Funktion „so aussieht", ist ein Trugschluss:
> Jede solche Funktion hat einen Wendepunkt, aber nicht jede Extrempunkte. Gegenbeispiel
> <span class="m" data-tex="a=0" data-plain="a = 0"></span>: <span class="m" data-tex="f_0(x)=x^3+x" data-plain="f₀(x) = x³ + x"></span> hat
> <span class="m" data-tex="f_0'(x)=3x^2+1>0" data-plain="f₀′(x) = 3x² + 1 > 0"></span> für alle
> <span class="m" data-tex="x" data-plain="x"></span>, ist also streng monoton wachsend und hat weder Hoch- noch Tiefpunkt.
> **(b)** <span class="m" data-tex="f_a'(x)=3x^2+2a\,x+1" data-plain="f_a′(x) = 3x² + 2a·x + 1"></span> hat die Diskriminante
> <span class="m" data-tex="D=4a^2-12" data-plain="D = 4a² − 12"></span>. Es gibt Extrempunkte genau dann, wenn
> <span class="m" data-tex="D>0" data-plain="D > 0"></span>, also <span class="m" data-tex="a^2>3" data-plain="a² > 3"></span>, also
> <span class="m" data-tex="|a|>\sqrt3\approx1{,}73" data-plain="|a| > √3 ≈ 1,73"></span>. Beispiel
> <span class="m" data-tex="a=2" data-plain="a = 2"></span>: <span class="m" data-tex="f_2'=(x+1)(3x+1)" data-plain="f₂′ = (x + 1)(3x + 1)"></span>,
> Hochpunkt <span class="m" data-tex="H(-1\,|\,0)" data-plain="H(−1 | 0)"></span>, Tiefpunkt
> <span class="m" data-tex="T(-\tfrac13\,|\,-\tfrac4{27})" data-plain="T(−1/3 | −4/27)"></span>. Für
> <span class="m" data-tex="|a|<\sqrt3" data-plain="|a| < √3"></span> hat
> <span class="m" data-tex="f_a'" data-plain="f_a′"></span> keine Nullstelle und bleibt positiv (der Graph steigt überall). Am Übergang
> <span class="m" data-tex="a=\pm\sqrt3" data-plain="a = ±√3"></span> ist <span class="m" data-tex="D=0" data-plain="D = 0"></span>: doppelte Nullstelle von
> <span class="m" data-tex="f_a'" data-plain="f_a′"></span>, kein Vorzeichenwechsel, also ein
> **Sattelpunkt**, an dem Hoch- und Tiefpunkt zusammenfallen und verschwinden.
> **(c)** <span class="m" data-tex="f_a''(x)=6x+2a=0" data-plain="f_a″(x) = 6x + 2a = 0"></span> hat für **jedes**
> <span class="m" data-tex="a" data-plain="a"></span> genau die Lösung <span class="m" data-tex="x=-a/3" data-plain="x = −a/3"></span>, und
> <span class="m" data-tex="f_a'''(x)=6\neq0" data-plain="f_a‴(x) = 6 ≠ 0"></span> gilt unabhängig von <span class="m" data-tex="a" data-plain="a"></span>:
> ein Wendepunkt mit <span class="m" data-tex="y=a(2a^2-9)/27" data-plain="y = a(2a² − 9)/27"></span>. Das Vorzeichen von
> <span class="m" data-tex="f_a''" data-plain="f_a″"></span> wechselt, weil <span class="m" data-tex="f_a''" data-plain="f_a″"></span> eine Gerade mit Steigung 6 ist.
> **Zusatz (freiwillig):** Ortskurve der Wendepunkte: <span class="m" data-tex="a=-3x" data-plain="a = −3x"></span> eingesetzt ergibt
> <span class="m" data-tex="y=x-2x^3" data-plain="y = x − 2x³"></span>.
>
> **Bewertungskriterien.** Behauptung als falsch erkannt · Gegenbeispiel mit Rechnung
> (<span class="m" data-tex="a=0" data-plain="a = 0"></span>: <span class="m" data-tex="f'>0" data-plain="f′ > 0"></span>) · Existenzbedingung über die Diskriminante von
> <span class="m" data-tex="f_a'" data-plain="f_a′"></span> mit korrektem Bereich <span class="m" data-tex="|a|>\sqrt3" data-plain="|a| > √3"></span> ·
> Übergangsfall <span class="m" data-tex="|a|=\sqrt3" data-plain="|a| = √3"></span> als Sattelpunkt gedeutet · Wendepunkt für alle
> <span class="m" data-tex="a" data-plain="a"></span> begründet (lineares <span class="m" data-tex="f''" data-plain="f″"></span>, <span class="m" data-tex="f'''\neq 0" data-plain="f‴ ≠ 0"></span>) ·
> Unterscheidung „Extrempunkte existieren nicht immer, ein Wendepunkt immer" klar formuliert.

**Kontrollrechnung:** K18.

---

## 6 · Abschluss

`<section id="abschluss">`, `.stufe`-Kopf: Nr. **6**, Überschrift **Abschluss**.

### 6.1 Vier Kernaussagen (je ein `<div class="merksatz">`)

**1. Null allein entscheidet nichts.**
> Eine Nullstelle von <span class="m" data-tex="f'" data-plain="f′"></span> ist nur ein Kandidat für eine
> Extremstelle. Sie ist eine, wenn <span class="m" data-tex="f'" data-plain="f′"></span> dort das
> Vorzeichen wechselt; die Abkürzung <span class="m" data-tex="f''\neq0" data-plain="f″ ≠ 0"></span> ist bequem, versagt aber genau in
> den Fällen, in denen <span class="m" data-tex="f''=0" data-plain="f″ = 0"></span> ist.

**2. Wendestellen sind Extremstellen von f′.**
> Eine Wendestelle ist dort, wo sich das Krümmungsverhalten ändert, also
> <span class="m" data-tex="f''" data-plain="f″"></span> das Vorzeichen wechselt. Hinreichend ist
> <span class="m" data-tex="f''=0" data-plain="f″ = 0"></span> mit <span class="m" data-tex="f'''\neq0" data-plain="f‴ ≠ 0"></span>. Ein
> Sattelpunkt ist ein Wendepunkt mit waagerechter Tangente. In Sachkontexten liegt die größte
> Änderungsrate eines Bestands an einer Wendestelle des Bestands.

**3. Ein Ergebnis ist vollständig, wenn es das Ganze beantwortet.**
> Zu einem Extrempunkt gehört der y-Wert, zu einem globalen Extremum auf einem Intervall der Vergleich
> mit den Randwerten, zu einer Behauptung die Begründung oder das Gegenbeispiel. Extremstelle,
> Extremwert und Extrempunkt sind drei verschiedene Antworten.

**4. Bei Scharen entscheidet der Parameter über die Sorte des Punktes.**
> Beim Ableiten ist der Parameter eine Konstante. Ein vollständiges Ergebnis enthält die Fälle
> (etwa <span class="m" data-tex="t>0" data-plain="t > 0"></span>, <span class="m" data-tex="t<0" data-plain="t < 0"></span>, <span class="m" data-tex="t=0" data-plain="t = 0"></span>) und die
> Übergangswerte, an denen Extrempunkte verschmelzen und verschwinden. Die Ortskurve entsteht, indem man den Parameter
> aus den Koordinaten des Punktes eliminiert.

### 6.2 Blick aufs Zentralabitur (`<div class="hinweis">`)

> **So begegnet dir das im Zentralabitur.** Extrem- und Wendepunkte, Funktionenscharen mit
> Parameter, Ortskurven und Aufgaben der Art „Für welchen Wert des Parameters …?" gehören zu den
> Standardbausteinen der Analysis-Aufgaben im Leistungskurs. Typische Arbeitsaufträge lauten
> *Bestimme*, *Zeige, dass*, *Begründe* und *Beurteile*: Das erste verlangt eine saubere Rechnung
> (Ableitungen, Nullstellen, hinreichende Bedingung, y-Koordinate), das zweite einen lückenlosen Nachweis,
> das dritte und vierte eine Argumentation mit Gegenbeispiel oder Zahlenwerten. Häufige Punktverluste:
> die y-Koordinate vergessen, die hinreichende Bedingung nicht prüfen, Randwerte übersehen und bei Scharen die
> Fallunterscheidung weglassen. Wie die Prüfung in Teile mit und ohne Hilfsmittel gegliedert ist und welche
> Hilfsmittel zugelassen sind, legen die jeweils gültigen Vorgaben zum Zentralabitur fest; sieh dort nach
> und übe die Ableitungen und Nullstellen von Hand, ganz gleich, was der Taschenrechner kann.

### 6.3 Selbstcheck (`.karte` mit `<h3>Selbstcheck</h3>`, sechs `.check`-Zeilen)

Formuliert als „Ich kann …", nah an den prozessbezogenen Kompetenzbereichen (Argumentieren,
Problemlösen, Modellieren, Werkzeuge nutzen), **ohne** wörtliche Kernlehrplan-Zitate:

1. Ich kann mit der ersten und zweiten Ableitung Monotonie und Krümmung eines Graphen beschreiben.
2. Ich kann Extremstellen ganzrationaler Funktionen bestimmen und mit dem Vorzeichenwechsel von f′ oder mit f″ begründen, und ich weiß, wann das f″-Kriterium nichts entscheidet.
3. Ich kann Wendestellen und Sattelpunkte bestimmen und hinreichend begründen (Vorzeichenwechsel von f″ oder f‴ ≠ 0).
4. Ich kann eine ganzrationale Funktion vollständig untersuchen (Symmetrie, Verhalten im Unendlichen, Nullstellen, Extrem- und Wendepunkte) und auf einem Intervall globale Extrema mit den Randwerten bestimmen.
5. Ich kann bei Funktionenscharen nach x ableiten, Fallunterscheidungen durchführen, Parameter aus Bedingungen bestimmen und Ortskurven berechnen.
6. Ich kann Behauptungen und Lösungswege zu Extrem- und Wendepunkten beurteilen und mit Gegenbeispielen oder Zahlenwerten begründen.

### 6.4 Export und Druck

Wie im Referenzmodul: Knopf `#bExport` (Ergebnisse in die Zwischenablage), Druckknopf, `@media print`
unverändert. Die Namensliste im Export (`var namen = {…}`) bekommt **diese** Schlüssel:

```js
var namen = {
  vw1:"Vorwissen 1 (zweite Ableitung)", vw2:"Vorwissen 2 (quadratische Gleichung)",
  vw3:"Vorwissen 3 (Steigung und Funktionswert)",
  sim1:"Simulation 1 (Schar 2: Punkte wandern)", sim2:"Simulation 2 (Schar 3: Stelle x = 0)",
  a1:"Tiefpunkt (y-Koordinate)", a2:"Steigung der Wendetangente", mc1:"Sattelpunkt begründen",
  a3:"Pegel: globales Maximum", a4:"Größte Wachstumsgeschwindigkeit", a5:"Parameter für Sattelpunkt",
  z1:"Ableitungsgraphen zuordnen"
};
```

Zwölf Schlüssel. Die drei offenen Aufgaben (`a8`, `a6`, `a7`) laufen nicht über `ergebnisse`; ihre
`<textarea>`-Texte werden wie im Referenzmodul beim Export angehängt.

### 6.5 Anschlusshinweis (`<div class="hinweis">`)

> **Wie es weitergeht.** Alle Funktionen in dieser Einheit waren ganzrational. Mit der
> Produkt- und Kettenregel aus der letzten Einheit lassen sich Extrem- und Wendepunkte demnächst auch
> bei Wurzel- und gebrochenrationalen Funktionen bestimmen, und mit der Exponentialfunktion
> kommen Funktionen wie <span class="m" data-tex="x\cdot\mathrm{e}^{-x}" data-plain="x · e⁻ˣ"></span> dazu, die weder Nullstellen im Inneren noch ein
> globales Maximum verstecken. Das Vorgehen bleibt dasselbe: Kandidaten mit
> <span class="m" data-tex="f'=0" data-plain="f′ = 0"></span> sammeln, den Vorzeichenwechsel prüfen, Ränder und Verhalten im Unendlichen nicht vergessen.

---

## Lehrerteil

`<details class="lehrer">` am Ende der sechsten Section; verschwindet beim Drucken.

### Einordnung

Das Modul gehört in das Inhaltsfeld **Funktionen und Analysis** und setzt die Analysis der Qualifikationsphase
fort. Es steht nach den Ableitungsregeln (Produkt-, Ketten-, Quotientenregel) und vor den Integralen. Die Funktionen sind bewusst
ganzrational: Der Erkenntnisgewinn liegt in den **Begründungen** (hinreichend statt nur
notwendig) und in der **Schar** als Vorbereitung auf die Abituraufgaben, nicht in neuer
Ableitungstechnik.

**Offene Zuordnung (Rückfrage an die Fachkonferenz).** Die Projektdatei
`fachliches/kernlehrplan-nrw.md` ordnet die „Funktionsuntersuchung" der Analysis der Q1 zu. Ob die
Grundlagen (Extrem- und Wendepunkte ganzrationaler Funktionen, Monotonie und Krümmung) im schulinternen
Lehrplan schon in der Einführungsphase liegen und die Q1 hier nur wiederholt und vertieft, ist
offen und wurde nicht geraten. Ebenso offen: die genaue Zuordnung von Funktionenscharen und
Ortskurven zu den ausgewiesenen Kompetenzerwartungen. Das Modul zitiert deshalb keine
Kompetenzformulierungen; der Chip im Kopf nennt nur das Inhaltsfeld. Der Bezug zu den prozessbezogenen
Kompetenzen (Argumentieren, Problemlösen, Modellieren, Werkzeuge nutzen) ist über die
Übungen belegt: Aufgaben `a6` und `a7` bedienen das Argumentieren, `a3` und `a4` das Modellieren.

### Zeitbedarf

Tabelle in `<div class="tabelle">`:

| Abschnitt | Minuten | Hinweis |
|---|---|---|
| 1 Einstieg (Aufhänger, drei Vorwissensfragen) | 10 | Vorwissensfragen als Blitzrunde |
| 2 Erklärteil (2.1–2.6, zwei Herleitungen in `details`) | 30 | Herleitungen ggf. als Hausaufgabe |
| 3 Vertiefung Funktionsscharen | 20 | 3.3 (Ortskurve) kann in Q1 nach hinten rücken |
| 4 Simulation mit Beobachtungsauftrag und zwei Fragen | 20 | Paararbeit; Teil 1 und Teil 2 einzeln möglich |
| 5 Übungen (zehn Aufgaben) | 45 | Pflicht: `a1`, `a2`, `mc1`, `a8`, `z1`, `a6`; Rest (u. a. `a3`) Differenzierung |
| 6 Abschluss und Selbstcheck | 5 | |
| **Summe** | **130** | etwa 1,5 Doppelstunden; bei zwei Doppelstunden Luft für Sicherung |

### Typische Schülerfehler — und wo anzuhalten ist

1. **„f′(x₀) = 0 ⟹ Extremum."** Bei 2.4 anhalten, bevor die Tabelle erscheint: Lernende raten lassen, welche Sorte Punkt x³ bei 0 hat. Danach in der Simulation (Schar 3, x₀ = 0) zeigen, dass f′ und f″ null sein können und trotzdem alles davon abhängt, ob das obere Band die Farbe wechselt.
2. **„f″(x₀) = 0 ⟹ Wendepunkt" oder „⟹ kein Extremum".** Beide Richtungen kommen vor. Bei `mc1` und `a6` (Schritt 3) anhalten, im Plenum Distraktor 1 und 2 aus `mc1` gegeneinander stellen.
3. **Extremstelle, Extremwert, Extrempunkt vermischen.** Antwort „T(3)" oder „−4" statt „T(3 | −4)". Bei `a1` liegt der Fall umgekehrt: Dort ist ausdrücklich nur die y-Koordinate gefragt, und −4 ist die richtige Antwort. Nutze das für die Begriffsunterscheidung: Lass mündlich den vollständigen Punkt T(3 | −4) nachliefern und halte daneben, was die Aufgabe verlangt hat.
4. **Randextrema übersehen.** Bei 2.6 und `a3` anhalten; Lernende zeichnen den Verlauf von h(t) und sehen, dass der Graph an der Grenze noch steigt. Impuls: „Was wäre, wenn der Beobachtungszeitraum sechs Tage lang wäre?" (Es wäre h(6) = 0,1·(216 − 216 + 54) = 5,4 m, das Modell steigt also weiter.)
5. **Parameter wie eine Variable behandeln, nach t ableiten, durch t kürzen.** Bei 3.1 die beiden Fehler an die Tafel; bei `a5` zeigen, dass „Diskriminante null" den Übergangswert liefert.
6. **Fallunterscheidung vergessen.** In 3.2 die Tabelle t > 0, t < 0, t = 0 von den Lernenden selbst füllen lassen (Rechnung bis f″(0) = −6t und f″(2t) = 6t vorgeben); `a8` wiederholt diese Technik samt Ortskurve. Bei `a7` erneut: Wer nur „für alle a" schreibt, verliert die Bedingung |a| > √3.
7. **Ortskurve: nur eine Koordinate eliminiert oder Parameter nicht ersetzt.** Bei 3.3 an einem zweiten Beispiel wiederholen (Schar 1 der Simulation: aus f′ = 0 folgt a = x², eingesetzt y = −(2/3)x³ — nur als Zusatz, nicht als Ergebnis vorwegnehmen).
8. **Diagramm von f′ als Graph von f lesen.** Bei `z1` anhalten: Erst die Frage „Was sieht man hier eigentlich?" stellen. Kontrastiere mit der Reihe f, f′, f″ aus der Simulation.
9. **Steigungswinkel im Bild als Zahlenwert nehmen.** Die Achsen der Simulation sind ungleich skaliert; bei der Auswertung der Wendetangente ausdrücklich auf die Messwerte verweisen.

### Differenzierung

- **Zum Erleichtern:** `a1`, `a2`, `mc1` mit den Hilfestufen; im Erklärteil 2.5 als Schritt-für-Schritt-Vorlage benutzen; die Simulation nur mit Teil 1 (Schar 2) bearbeiten und die Verständnisfrage `sim1` zuerst ohne Rückmeldung lesen.
- **Standard:** alle Pflichtaufgaben (darunter `a8`), beide Teile des Beobachtungsauftrags. `a3` (Randextrema) entfällt im Standardweg und wird bei Bedarf mit 2.6 nachgeholt.
- **Zum Vertiefen:** `a8` (Fallunterscheidung und Ortskurve), `a7` einschließlich Zusatz (Ortskurve y = x − 2x³), die Herleitungen in `details` selbst nachvollziehen, der Zusatzauftrag zu Schar 1 (Ortskurve aus zwei abgelesenen Punkten bestimmen und mit Abschnitt 3.3 beweisen). Als Anschlussaufgabe: Die Formel der Schar 3 aus den Messwerten rekonstruieren (vorher Formel verdeckt lassen), z. B. „Finde eine Funktion 4. Grades mit f′(x) = x²(x − a)".
- **Alternative zur verdeckten Formel:** Wer die Simulation lieber mit sichtbarer Formel einsetzt, blendet die Formeln über eine Schalterkonstante am Anfang der IIFE ein; dann sind `sim1` und `sim2` allerdings auch rechnend lösbar.

### Bezug zu Realexperimenten und Daten

- **Bewegungssensor.** Der Ort-Zeit-Verlauf eines Wagens auf der schiefen Ebene, der abgebremst wird, liefert s(t), v = s′ und a = s″ aus der Messwerttabelle. Die Umkehrpunkte sind Extrempunkte von s, die Stellen mit größter Geschwindigkeit sind Wendepunkte von s. Die Kette f, f′, f″ der Simulation ist genau dieses Diagramm-Trio.
- **Biegelinie eines Lineals oder Balkens.** Ein an beiden Enden fest eingeklemmtes Lineal, in der Mitte belastet: Die Biegelinie ist in der Mitte nach unten durchgebogen und an den Enden entgegengesetzt gekrümmt; dazwischen liegen zwei Wendepunkte. Wendepunkt = Krümmungswechsel, mit bloßem Auge sichtbar.
- **Höhenprofil aus GPS-Daten.** Aufgezeichnete Wanderstrecke; die Steigung aus den Höhendaten liegt als Zahlenreihe vor, größte Steigung = Wendepunkt des Höhenprofils. Passt zum Aufhänger.
- **Wachstumsdaten.** Höhe einer Pflanze über zwei Wochen messen; das Modell aus `a4` ist ein möglicher Fit; die Frage „wann wächst sie am schnellsten?" ist die Frage nach der Wendestelle.
- **Software.** GeoGebra oder der GTR mit Schieberegler für den Parameter: Die Simulation dieses Moduls lässt sich damit nachbauen, und es entsteht ein zweiter Zugang zur Ortskurve (Spur des Punktes).

### Zur Gestaltung der Simulationsfragen

`sim1` und `sim2` beziehen sich auf **Scharen, deren Formel verdeckt ist**. Zweck: Sie lassen sich nur durch
Bedienen der Simulation beantworten. Die Formel wird erst in der Rückmeldung zur richtigen Option offenbart, und
die Lernenden können dann nachrechnen, was sie gesehen haben. Frühere Fassungen anderer Module hatten Fragen, die sich
aus dem Erklärtext ableiten ließen; diese hier sind durch Aufbau (verdeckte Formel, konkrete Ablesewerte
in den Distraktoren) dagegen abgesichert. Die einzige Frage, die sich auch rechnen ließe (Ortskurve Schar 1), ist
absichtlich nur ein Zusatzauftrag ohne Multiple Choice.

---

## Checkliste für den Bauagenten

### Benötigte Aufgabenbausteine und ihre Schlüssel

| Schlüssel | Baustein | `data`-Attribut | Optionen / Besonderheit | AB |
|---|---|---|---|---|
| `vw1` | Multiple Choice | `data-mc="vw1"` | 3 Optionen, `r: 1` | — |
| `vw2` | Multiple Choice | `data-mc="vw2"` | 3 Optionen, `r: 2` | — |
| `vw3` | Multiple Choice | `data-mc="vw3"` | 3 Optionen, `r: 0` | — |
| `sim1` | Multiple Choice | `data-mc="sim1"` | **4** Optionen, `r: 2`, Hilfen 1–3 | II |
| `sim2` | Multiple Choice | `data-mc="sim2"` | **4** Optionen, `r: 1`, Hilfen 1–3 | II |
| `a1` | Zahleneingabe | `data-num="a1"` | `wert: -4`, `"LE"`, `tol: 0.05`, Einheiten LE · FE · ° | I |
| `a2` | Zahleneingabe | `data-num="a2"` | `wert: -7`, Einheit `"1"` (Anzeige „ohne Einheit"), `tol: 0.05` | I |
| `mc1` | Multiple Choice | `data-mc="mc1"` | **4** Optionen, `r: 3`, Hilfen 1–3 | II |
| `a3` | Zahleneingabe | `data-num="a3"` | `wert: 2.0`, `"m"`, `tol: 0.02`, `alt: 200 "cm"` | II |
| `a4` | Zahleneingabe | `data-num="a4"` | `wert: 6`, `"cm/Tag"`, `tol: 0.05`, kein `alt` | II |
| `a5` | Zahleneingabe | `data-num="a5"` | `wert: 12`, Einheit `"1"` („ohne Einheit"), `tol: 0.05` | II |
| `z1` | Zuordnung | `data-check="zuordnung"` | 4 Inline-SVG mit fertigen `points` (Abschnitt 5, Aufgabe 7), Lösung **C · B · D · A**, Hilfen 1–3 | II |
| `a6` | offene Aufgabe | `data-loesung="a6"` | `<textarea>`, Musterlösung in `data-stufe="9"`, Hilfen 1–3 (3 = Gerüst) | III |
| `a7` | offene Aufgabe | `data-loesung="a7"` | `<textarea>`, Musterlösung in `data-stufe="9"`, Hilfen 1–3 (3 = Gerüst) | III |

Verteilung der Anforderungsbereiche in Abschnitt 5: **I** `a1`, `a2` · **II** `mc1`, `a3`, `a4`, `a5`, `z1` ·
**III** `a6`, `a7`. `a8` (AB II, offen mit Musterlösung, nicht über `ergebnisse`) kommt hinzu. Zusammen zehn Übungsaufgaben, zwei davon im Anforderungsbereich III als Bewertungs- bzw.
Begründungsaufgaben mit Musterlösung **und** Bewertungskriterien.

**Dreistufige Hilfen** (`data-hilfe="1|2|3"` plus `.hilfe-text[data-stufe="1|2|3"]`) bekommen **alle** zehn
Übungsaufgaben und die zwei Simulationsfragen. Bei den offenen Aufgaben ist Stufe 3 ein Lösungsgerüst mit den
Schlüsselzahlen; die volle Musterlösung steht in Stufe 9.

### Anpassungen an der kopierten Engine

1. **Zuordnungs-Engine:** `ergebnisse.a3 = (n === zeilen.length);` wird zu
   `ergebnisse.z1 = (n === zeilen.length);`. Sonst überschreibt die Zuordnung das Ergebnis der Zahleneingabe
   `a3` (in diesem Modul ist `a3` der Pegelstand!).
2. **MC-Engine:** unverändert, aber `sim1`, `sim2`, `mc1` haben **vier** Optionen; `fb`-Arrays mit genau vier
   Einträgen, `data-i` lückenlos 0…3, `name` des Radios gleich `data-mc`.
3. **Zahlen-Engine:** unverändert. `a2` und `a5` benutzen `einheit:"1"` mit `<option value="1">ohne Einheit</option>`;
   die Einheitenprüfung darf den Wert „1" nicht als „leer" behandeln.
4. **Hilfen in MC- und Zuordnungsaufgaben:** Der Hilfehandler sucht `.aufgabe` mit `closest`, es genügt also,
   die Buttons und `.hilfe-text` in die jeweiligen Blöcke zu setzen (bei `sim1`, `sim2`, `mc1`, `z1`).
5. **Eine Simulations-IIFE** mit zwei Canvas (`cvF`, `cvAbl`); einziger globaler Zustand bleibt `ergebnisse`.
6. **Farbtokens:** Mathematik-Grün wie in `CLAUDE.md`.
7. **Vier `<table>`-Elemente** in `<div class="tabelle">`: 2.1 (Vorzeichen), 2.4 (Vergleich), 3.2 (Fallunterscheidung),
   Zeitbedarf im Lehrerteil (`z1` hat keine Tabelle, nur SVG).
8. **Drei `<details>`-Blöcke** mit Herleitungen: 2.2 (f″-Kriterium), 2.3 (f‴ ≠ 0), 3.3 (Ortskurve, zweiter Weg).
9. **Formeln der verdeckten Scharen** nur im JS (dort im Kommentar) und in der jeweiligen Rückmeldung zur richtigen Option,
   nie im sichtbaren Text der Simulation oder im `<select>`.

### Simulationsbausteine

| Element | `id` | Bereich / Werte |
|---|---|---|
| Canvas Graph | `cvF` | `width="1000" height="400"`, `LX=70`, `RX=960`, `TY=20`, `BY=360` |
| Canvas Ableitungen | `cvAbl` | `width="1000" height="330"`, Fläche y 15…220, Bänder y 240…256 und 266…282 |
| Auswahl Schar | `sSchar` | 1, 2, 3 |
| Regler `a` | `rA` | −20…80 (Schar 3: −20…40), Schritt 1, `a = Wert/20` |
| Regler `x₀` | `rX` | Bereich je nach Schar, Schritt 1, `x₀ = Wert/20` |
| Schalter | `cTan`, `cSpur`, `cAufbau` | Start: an, aus, aus |
| Knöpfe | `bPlay`, `bReset` | 1,0 pro Sekunde, `dtFrame = Math.min(0.05, …)` |
| Anzeigen | `anzA`, `anzX0`, `anzF`, `anzF1`, `anzF2`, `anzArt`, `anzExt`, `anzWen`, `anzBefund` | Stellen und Startwerte in 4.5 |

Ein `.auftrag`-Kasten (4.7), zwei MC-Fragen danach (`sim1`, `sim2`), ein `.hinweis`-Kasten am Ende von Abschnitt 4,
eine graue Randbemerkung unter `cvF` zur ungleichen Achsenskalierung.

### Prüfpunkte vor der Abnahme

1. **Startzustände** (K7): Schar 1 (a = 1,00, x₀ = 2,00): 0,67 · 3,00 · 4,00 · H(−1,00 | 0,67) · T(1,00 | −0,67) · W(0,00 | 0,00), −1,00.
   Schar 2 (a = −0,50, x₀ = 2,50): −2,29 · 0,75 · 3,00 · H(−0,22 | 0,06) · T(2,22 | −2,39) · W(1,00 | −1,17), −1,50.
   Schar 3 (a = 1,00, x₀ = 2,00): 1,33 · 4,00 · 8,00 · T(1,00 | −0,08) · S(0,00 | 0,00) · W(0,67 | −0,05).
2. **Kritische Zustände:** Schar 2 bei a = 0,95 / 1,00 / 1,05: Steigung der Wendetangente −0,05 / 0,00 / +0,05; bei 1,00 nur S(1,00 | 0,33). Schar 3 bei a = 0,00: nur T(0,00 | 0,00). Schar 1 bei a = 0,00: kein H/T, S(0,00 | 0,00).
3. **Bänder:** Am Sattelpunkt kein Farbwechsel im f′-Band (Schar 2 bei a = 1,00; Schar 3 bei x = 0, a = 1,00). Am Tiefpunkt Wechsel rot → grün (Schar 3, a = 0,00, x = 0).
4. **Regler über den ganzen Bereich** bewegen (Schar 1 bis 3, `rA` und `rX` von Anschlag zu Anschlag): keine Markierung außerhalb des Fensters (K9), keine Fehlermeldung in der Konsole, `anzBefund` nur in den kritischen Zuständen.
5. **Ganzzahltest:** kritische Zustände werden über `Wert === 0` bzw. `Wert === 20` erkannt, nicht über `a === 1` (Fließkomma).
6. **Ortskurve-Spur:** Schar 1: Hoch- und Tiefpunkte auf derselben Kurve, sie geht durch (0|0), (1,5|−2,25), (2|−5,33), und (−1,5|2,25). Es steht **keine Gleichung** dabei.
7. **Ziehen** auf `cvF` setzt `x₀` und aktualisiert beide Canvas und alle Anzeigen; auf dem Handy bleibt die Seite vertikal scrollbar.
8. **Jede Zahleneingabe in allen vier Fällen** (richtig · richtige Zahl mit falscher Einheit · `nah` · `weit`), Zonen aus **K19**; `a3` zusätzlich 200 cm mit geerbter Toleranz 2 cm.
9. **Zuordnung in beiden Richtungen:** C · B · D · A vollständig richtig, ein Teilerfolg, keine richtig; `ergebnisse.z1` wird gesetzt.
10. **Alle Hilfestufen** aller zehn Aufgaben und der beiden Simulationsfragen öffnen; bei `a6`, `a7` und `a8` zusätzlich die Musterlösung.
11. **`data-plain` überall gefüllt**, ohne LaTeX-Reste (Unicode für `′`, `″`, `‴`, `⟹`, `≠`, `≈`, `√`, `±`). Test ohne Netz.
12. **Kein waagerechtes Scrollen** bei 1280, 900 und 390 px; die vier Tabellen stehen im Wrapper; beide Canvas `width:100%`.
13. **Druckansicht** enthält Aufgabentexte, Simulationsbeschreibung und Diagramme, aber keine Regler, Knöpfe und keinen Lehrerteil.
14. **Export** listet die zwölf Schlüssel und hängt die Texte der drei `<textarea>` (`a8`, `a6`, `a7`) an.
15. `PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/mathe-q1-funktionsuntersuchung.html"` meldet weder `blocker` noch `maengel`.
16. Eintrag in `fachliches/modulliste.md` erst danach von `in Arbeit` auf `fertig` setzen (nicht Aufgabe dieses Dokuments).

### Offene Punkte und Unsicherheiten

- **Kernlehrplan-Zuordnung offen** (Einführungsphase oder Q1, Scharen/Ortskurven): siehe Lehrerteil, keine Zitate.
- **Verdeckte Formeln** sind eine bewusste Designentscheidung; wenn die Fachschaft die Formeln sichtbar haben will, sind `sim1` und `sim2` auch rechnend lösbar (Lehrerteil, Differenzierung).
- **Modulumfang:** 130 Minuten sind mit zehn Übungsaufgaben knapp; die Pflichtauswahl im Lehrerteil ist die Kürzung.
- **Die Aufgabenstellung nennt Produkt- und Kettenregel als Voraussetzung.** Sie werden in diesem Modul nicht gebraucht; wer die Aufgaben um Wurzel- oder gebrochenrationale Funktionen erweitern will, kann `a3`/`a4` durch Beispiele aus `mathe-q1-ableitungsregeln.md` ergänzen.

### Quelle der Kontrollrechnungen

Alle Zahlenwerte stehen gesammelt in Abschnitt 0 (**K1** bis **K19**). Sie wurden symbolisch mit `sympy` (exakte Brüche, `factor`/`simplify` für Identitäten) und numerisch geprüft. Das Kontrollskript unten lief mit dem Ergebnis
„ALLE PRUEFUNGEN BESTANDEN (44)". Der Bauagent muss nichts nachrechnen, sollte aber jede Zahl, die er in die HTML-Datei schreibt,
gegen diese Liste abgleichen.

Die Simulation selbst wurde nicht gebaut; die Zahlen in 4.6 sind Sollwerte für den Bau, gerechnet mit denselben Formeln.

### Kontrollskript (vollständig, Python 3 mit sympy; Laufzeit etwa 12 Sekunden)

```python
# Kontrollskript Modul mathe-q1-funktionsuntersuchung (sympy, exakt). Ausgabe: "ALLE PRUEFUNGEN BESTANDEN".
from sympy import symbols, diff, solve, Rational as R, sqrt, simplify, factor, discriminant, atan, pi, N

x, a, t = symbols("x a t", real=True)
d = lambda f, n=1: diff(f, x, n)
ok = []
def check(name, cond):
    assert cond, "FEHLER: " + name
    ok.append(name)

# K1 Vorwissen
f = x**4 - 2*x**3 + 5*x
check("vw1", simplify(d(f, 2) - (12*x**2 - 12*x)) == 0)
check("vw2", sorted(solve(3*x**2 - 12*x + 9, x)) == [1, 3])
g = x**2 - 4*x
check("vw3", (g.subs(x, 3), d(g).subs(x, 3), d(g).subs(x, 2)) == (-3, 2, 0))

# K2 Beispiel x^4 - 4x^3 + 4x^2
f = x**4 - 4*x**3 + 4*x**2
check("K2 f'", simplify(d(f) - 4*x*(x - 1)*(x - 2)) == 0)
check("K2 f''(0,1,2)", [d(f, 2).subs(x, v) for v in (0, 1, 2)] == [8, -4, 8])
check("K2 y-Werte", [f.subs(x, v) for v in (0, 1, 2)] == [0, 1, 0])
ws = solve(d(f, 2), x)
check("K2 Wendepunkte y=4/9", all(simplify(f.subs(x, w) - R(4, 9)) == 0 for w in ws))
check("K2 f''' = -+8 sqrt3", sorted([simplify(d(f, 3).subs(x, w)) for w in ws], key=N) == [-8*sqrt(3), 8*sqrt(3)])
check("K2 Symmetrie", simplify(f.subs(x, 2 - x) - f) == 0)
check("K2 Wendetangente", abs(N(d(f).subs(x, 1 - sqrt(3)/3)) - 1.5396) < 1e-4)

# K3 / K4
check("K3 x^5", (d(x**5, 2), d(x**5, 3).subs(x, 0)) == (20*x**3, 0))
check("K4 f'(0,1), f'(-0,1)", (d(f).subs(x, R(1, 10)), d(f).subs(x, -R(1, 10))) == (R(684, 1000), -R(924, 1000)))

# K5 Schar x^3 - 3t x^2
ft = x**3 - 3*t*x**2
check("K5 Extremwerte", (ft.subs(x, 2*t), ft.subs(x, t)) == (-4*t**3, -2*t**3))
check("K5 f''(0), f''(2t)", (d(ft, 2).subs(x, 0), d(ft, 2).subs(x, 2*t)) == (-6*t, 6*t))
check("K5 Ort W", simplify(ft.subs(x, t).subs(t, x) + 2*x**3) == 0)
check("K5 Ort T", simplify((ft.subs(x, 2*t)).subs(t, x/2) + x**3/2) == 0)

# K6-K9 Scharen der Simulation
S = {1: x**3/3 - a*x, 2: x**3/3 - x**2 + a*x, 3: x**4/4 - a*x**3/3}
check("K6 Ableitungen", (factor(d(S[3])) == x**2*(x - a), simplify(d(S[2], 2) - 2*(x - 1)) == 0, d(S[1]) == x**2 - a))
def pts(k, av):
    g = S[k].subs(a, av)
    return {"ext": [(s, g.subs(x, s)) for s in solve(d(g), x)], "wen": [(s, g.subs(x, s), d(g).subs(x, s)) for s in solve(d(g, 2), x)]}
p = pts(1, R(9, 4)); check("K7 S1 a=2,25", sorted([(e[0], e[1]) for e in p["ext"]]) == [(-R(3, 2), R(9, 4)), (R(3, 2), -R(9, 4))])
p = pts(2, 1); check("K7 S2 a=1 Sattel", p["ext"] == [(1, R(1, 3))] and p["wen"] == [(1, R(1, 3), 0)])
p = pts(2, R(19, 20)); check("K7 S2 a=0,95", abs(N(p["wen"][0][2]) + 0.05) < 1e-12)
p = pts(3, 1); check("K7 S3 a=1", (1, -R(1, 12)) in p["ext"] and (0, 0) in p["ext"])
p = pts(3, 0); check("K7 S3 a=0", p["ext"] == [(0, 0)] and p["wen"] == [(0, 0, 0)])
check("K8 Ort S1", simplify(S[1].subs(a, x**2) + R(2, 3)*x**3) == 0)
check("K8 Ort S2", simplify(S[2].subs(a, 2*x - x**2) - (x**2 - R(2, 3)*x**3)) == 0)
check("K8 Ort S3", simplify(S[3].subs(x, a).subs(a, x) + x**4/12) == 0)
# alle Markierungsformeln fuer a in [-1,4] (Schritt 0,05) gegen sympy
for k, lo, hi in ((1, -20, 80), (2, -20, 80), (3, -20, 40)):
    for i in range(lo, hi + 1):
        av = R(i, 20); g = S[k].subs(a, av)
        for s in solve(d(g), x):
            assert abs(N(d(g).subs(x, s))) < 1e-9
check("K6 Punkte a-Raster", True)

# Fenster K9
def inside(k, xr, yr, arange):
    for i in arange:
        av = R(i, 20)
        for (px, py) in [(e[0], e[1]) for e in pts(k, av)["ext"]] + [(w[0], w[1]) for w in pts(k, av)["wen"]]:
            if not (xr[0] <= N(px) <= xr[1] and yr[0] <= N(py) <= yr[1]):
                return False
    return True
check("K9 Fenster S1", inside(1, (-3, 3), (-6, 6), range(-20, 81)))
check("K9 Fenster S2", inside(2, (-2, 4), (-4, 6), range(-20, 81)))
check("K9 Fenster S3", inside(3, (-2, 3), (-2, 3), range(-20, 41)))

# K10..K15
f = x**3 - 6*x**2 + 9*x - 4; check("a1", f.subs(x, 3) == -4 and d(f, 2).subs(x, 3) == 6)
f = x**3 - 6*x**2 + 5*x; check("a2", solve(d(f, 2), x) == [2] and d(f).subs(x, 2) == -7 and f.subs(x, 2) == -6)
f = R(1, 2)*x**4 - 4*x**3 + 9*x**2 - 5
check("mc1", (d(f).subs(x, 3), d(f, 2).subs(x, 3), d(f, 3).subs(x, 3), f.subs(x, 3)) == (0, 0, 12, R(17, 2)))
h = R(1, 10)*(t**3 - 6*t**2 + 9*t)
check("a3", [h.subs(t, v) for v in (0, 1, 3, 5)] == [0, R(2, 5), 0, 2])
B = -R(2, 100)*t**3 + R(6, 10)*t**2
check("a4", solve(diff(B, t, 2), t) == [10] and diff(B, t).subs(t, 10) == 6 and diff(B, t).subs(t, 20) == 0)
f = x**3 - 6*x**2 + a*x
check("a5", solve(discriminant(d(f), x), a) == [12] and factor(d(f).subs(a, 12)) == 3*(x - 2)**2)
# K17 a6
f = x**4 - 4*x**3
check("a6", (f.subs(x, 3), f.subs(x, 2), d(f).subs(x, 2), d(f, 3).subs(x, 0), d(f, 3).subs(x, 2)) == (-27, -16, -16, -24, 24))
# K18 a7
f = x**3 + a*x**2 + x
check("a7 Diskriminante", simplify(discriminant(d(f), x) - (4*a**2 - 12)) == 0)
check("a7 Ort", simplify(f.subs(x, -a/3).subs(a, -3*x) - (x - 2*x**3)) == 0)
check("a7 a=2", sorted([(s, f.subs(a, 2).subs(x, s)) for s in solve(d(f.subs(a, 2)), x)]) == [(-1, 0), (-R(1, 3), -R(4, 27))])
# K16 z1
for name, fp, ne, nw in (("A", -x, 1, 0), ("B", x**3 - x, 3, 2), ("C", x**2 - 1, 2, 1), ("D", x**2, 0, 1)):
    check("z1 " + name, len(solve(d(fp), x)) == nw)
# Pixel
px = lambda X: 70 + (X + 3)/6*890
py = lambda Y: 360 - (Y + 6)/12*340
check("Pixel", (px(0), round(float(px(2)), 2), py(0), py(6), round(float(py(R(2, 3))), 2)) == (515, 811.67, 190, 20, 171.11))
print("ALLE PRUEFUNGEN BESTANDEN (%d)" % len(ok))
```

Ausgabe des Laufs: `ALLE PRUEFUNGEN BESTANDEN (44)`.
