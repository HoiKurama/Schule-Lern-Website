# Modulinhalt: Produktregel, Kettenregel, Quotientenregel

**Dateiname des Moduls:** `module/mathe-q1-ableitungsregeln.html`
**Fach:** Mathematik · **Kursniveau:** Leistungskurs Q1
**Inhaltsfeld (Chip im Seitenkopf, wörtlich nach `fachliches/kernlehrplan-nrw.md`):** Funktionen und Analysis
**Weitere Chips:** „Kernlehrplan NRW, GOSt" · „ca. 90 Minuten"
**Fachzeile über der Überschrift:** Mathematik · Qualifikationsphase 1 · Leistungskurs
**Seitentitel (`<h1>`):** Produkt-, Ketten- und Quotientenregel
**Farbtokens:** `--akzent: #0d7a52` · `--akzent-hell: #e7f6ef` · `--akzent-rand: #b5e0cd`,
dazu der Verlauf in `header.kopf` (sonst bleibt der `<style>`-Block des Referenzmoduls unverändert).

**Voraussetzung aus der Einführungsphase (wird *nicht* neu eingeführt):** Potenzregel, Faktorregel,
Summenregel, Ableitung ganzrationaler Funktionen, Ableitung als lokale Änderungsrate und als
Tangentensteigung, Differenzenquotient und Grenzwertbegriff.
**Bewusst nicht vorausgesetzt:** Ableitungen von <span class="m" data-tex="\sin" data-plain="sin"></span>,
<span class="m" data-tex="\cos" data-plain="cos"></span> und
<span class="m" data-tex="\mathrm{e}^x" data-plain="eˣ"></span>. Alle Beispiele kommen mit
Potenzen, Wurzeln und gebrochenrationalen Termen aus. Auf die späteren Funktionsklassen wird
nur hingewiesen (Abschnitt 3.5).

**Aufbau:** sechs `<section>`-Blöcke mit nummeriertem `.stufe`-Kopf, Reihenfolge wie unten
(Lehrerteil und Checkliste sind keine eigenen Sektionen, sondern gehören in die sechste).

**Kontrollrechnungen:** Alle Zahlenwerte dieser Datei wurden symbolisch mit `sympy` und numerisch
geprüft; die Ergebnisse stehen vollständig in Abschnitt 0. Der Bauagent muss nichts nachrechnen,
darf aber jede Zahl gegen diese Liste prüfen.

---

## 0 · Kontrollrechnungen (Sammelstelle)

**K1 — Einstieg und Simulation 1: Freibad, <span class="m" data-tex="p(t) = 5 + 0{,}1\,t" data-plain="p(t) = 5 + 0,1 t"></span> (€), <span class="m" data-tex="n(t) = 400 - 6\,t" data-plain="n(t) = 400 − 6 t"></span> (Besucher)**
U(t) = p(t)·n(t) = 2000 + 10 t − 0,6 t² (ausmultipliziert, symbolisch bestätigt).
U(0) = 2000,00 € · U′(t) = 10 − 1,2 t · U′(0) = **10,00 €/Tag**.
Über die Produktregel: p′·n + p·n′ = 0,10 · 400 + 5,00 · (−6) = 40 − 30 = **10,00 €/Tag** ✓
Naives (falsches) Produkt der Ableitungen: 0,10 · (−6) = **−0,60** — falsches Vorzeichen *und* falsche Größenordnung.
U(1) = 5,10 · 394 = 2009,40 € · U(1) − U(0) = **9,40 €**.
Zerlegung dieser 9,40 €: Δp·n(0) + p(0)·Δn + Δp·Δn = 40,00 − 30,00 − 0,60 = **9,40** ✓
Umsatzmaximum: U′(t) = 0 ⟺ t* = 25/3 = **8,3333 Tage**; U(t*) = 6125/3 = **2041,67 €**;
p(t*) = 5,8333 € · n(t*) = 350,0 Besucher.

**K2 — Vorwissen `vw1`:** f(x) = 3x⁴ − 5x² + 2x − 9 ⟹ f′(x) = **12x³ − 10x + 2**; f′(1) = 4.

**K3 — Vorwissen `vw2`:** f(x) = 1/x³ = x⁻³ ⟹ f′(x) = −3x⁻⁴ = **−3/x⁴**; f′(2) = −3/16.
Distraktorwerte bei x = 2: −3/x² → −0,75 · +3/x⁴ → +0,1875.

**K4 — Vorwissen `vw3`:** Modell N(t) = 400 − 6t; N(5) = 370, N(6) = 364, Differenz **−6** pro Tag.

**K5 — Gegenbeispiel zur Fehlvorstellung (uv)′ = u′v′**
x · x = x² ⟹ Ableitung **2x**; naives Produkt der Ableitungen: 1 · 1 = **1**.
Bei x = 4: richtig 8, naiv 1. Bei (x+1)·(x+1): richtig 2x + 2, bei x = 4 also 10, naiv 1.

**K6 — Erklärteil, Produktregel-Beispiel f(x) = (x³ − 2x)(4x + 5)**
Ausmultipliziert: f(x) = 4x⁴ + 5x³ − 8x² − 10x ⟹ f′(x) = **16x³ + 15x² − 16x − 10**.
Produktregel: u′v = (3x² − 2)(4x + 5) = 12x³ + 15x² − 8x − 10; uv′ = (x³ − 2x)·4 = 4x³ − 8x;
Summe = **16x³ + 15x² − 16x − 10** ✓ (symbolisch als identisch bestätigt).
Stichproben: f′(1) = 5 · f′(2) = 146.

**K7 — Erklärteil, Kettenregel-Beispiel f(x) = (2x − 1)³**
Ausmultipliziert: 8x³ − 12x² + 6x − 1 ⟹ Ableitung **24x² − 24x + 6**.
Kettenregel: 3(2x − 1)²·2 = 6(2x − 1)² = 24x² − 24x + 6 ✓
f′(2) = 6·3² = **54**; Distraktor ohne innere Ableitung: 3·3² = 27.

**K8 — Erklärteil, Kettenregel mit Wurzel:** f(x) = √(x² + 1) ⟹ f′(x) = **x/√(x² + 1)**;
f′(2) = 2/√5 = 2√5/5 ≈ **0,8944**.

**K9 — Gegenbeispiel zur Fehlvorstellung (u/v)′ = u′/v′**
x²/x = x (für x ≠ 0) ⟹ Ableitung **1**; naiv u′/v′ = 2x/1 = 2x, bei x = 3 also **6** statt 1.

**K10 — Vertiefung, Quotientenregel-Beispiel f(x) = (x² + 1)/(x − 2), D = ℝ\\{2}**
f′(x) = [2x(x − 2) − (x² + 1)·1]/(x − 2)² = **(x² − 4x − 1)/(x − 2)²**.
f′(3) = (9 − 12 − 1)/1 = **−4** · f′(0) = (0 − 0 − 1)/4 = **−0,25**.

**K11 — Quotientenregel als Folgerung (symbolische Probe)**
d/dx [u/v] − (u′v − uv′)/v² = **0** für allgemeine Funktionen u, v (sympy, exakt).
Reziprokenregel-Proben: (1/x)′ = −1/x² ✓ · (1/(x²+1))′ = −2x/(x²+1)² ✓

**K12 — Simulation 1, Startzustand (p₀ = 5,00 € · n₀ = 400 · b = 0,10 · d = −6 · t = 0 · Δt = 1,0)**
p = 5,00 € · n = 400,0 · U = 2000,00 €
Beitrag p′·n = **40,00 €/Tag** · Beitrag p·n′ = **−30,00 €/Tag** · U′ = **10,00 €/Tag**
U(t+Δt) = 2009,40 € · Sekantensteigung ΔU/Δt = **9,40 €/Tag** · Eckanteil (Δp·Δn)/Δt = **−0,60 €/Tag**
Probe: 40,00 − 30,00 − 0,60 = 9,40 ✓

**K13 — Simulation 1, Verkleinern von Δt bei t = 0 (Tabelle für den Beobachtungsauftrag)**

| Δt (Tage) | U(t+Δt) (€) | Sekante ΔU/Δt (€/Tag) | Eckanteil (€/Tag) | Abstand zu U′ = 10 |
|---|---|---|---|---|
| 4,00 | 2030,40 | 7,60 | −2,40 | 2,40 |
| 2,00 | 2017,60 | 8,80 | −1,20 | 1,20 |
| 1,00 | 2009,40 | 9,40 | −0,60 | 0,60 |
| 0,50 | 2004,85 | 9,70 | −0,30 | 0,30 |
| 0,25 | 2002,4625 | 9,85 | −0,15 | 0,15 |

Beim Halbieren von Δt **halbiert** sich der Eckanteil (weil Δp·Δn sich viertelt und durch Δt
geteilt wird). Der Abstand der Sekante zur Ableitung ist in jeder Zeile exakt der Eckanteil.

**K14 — Simulation 1, zweiter Testfall (t = 12 · Δt = 0,5 · sonst Startwerte)**
p = 6,20 € · n = 328,0 · U = 2033,60 €
Beitrag p′·n = **32,80** · Beitrag p·n′ = **−37,20** · U′ = **−4,40 €/Tag**
U(t+Δt) = 2031,25 € · Sekante = **−4,70 €/Tag** · Eckanteil = **−0,30 €/Tag**; Probe 32,80 − 37,20 − 0,30 = −4,70 ✓

**K15 — Simulation 1, Maximum und Reglergrenzen**
Maximum bei t* = −(b·n₀ + p₀·d)/(2bd); mit den Startwerten t* = **8,3333 Tage**, U(t*) = **2041,67 €**.
Dort gilt p′·n = 0,10 · 350 = **+35,00** und p·n′ = 5,8333 · (−6) = **−35,00**, Summe 0 ✓
Reglerränder (p₀ = 5,00 €, n₀ = 400 fest, t + Δt ≤ 25):
p(25) zwischen 1,25 € (b = −0,15) und 12,50 € (b = +0,30) → Preisachse bis **14 €** reicht.
n(25) zwischen 100 (d = −12) und 600 (d = +8) → Besucherachse bis **600** reicht.
U′(0) am Reglerrand: von −120,00 €/Tag (b = −0,15, d = −12) bis +160,00 €/Tag (b = +0,30, d = +8).
Umsatz im Reglerbereich: zwischen 125,00 € und 7500,00 €.

**K16 — Simulation 2 (Ölteppich), Startzustand r₀ = 5 m · c = 0,5 m/s · t = 20 s · Δt = 1,0 s**
r = **15,000 m** · Umfang 2πr = **94,2478 m** · A = πr² = **706,8583 m²**
dA/dr = 2πr = **94,2478 m** · dr/dt = c = 0,5 m/s · dA/dt = 2πr·c = **47,1239 m²/s**
Δr = c·Δt = 0,500 m · Ringfläche exakt π((r+Δr)² − r²) = **47,90929 m²** ·
Näherung 2πr·Δr = **47,12389 m²** · Fehler πΔr² = **0,78540 m²** (1,639 %).

**K17 — Simulation 2, Fehlerverhalten bei halbiertem Δt (Beobachtungsauftrag)**

| Δt (s) | Δr (m) | Ring exakt (m²) | Näherung 2πr·Δr (m²) | Fehler πΔr² (m²) | relativer Fehler |
|---|---|---|---|---|---|
| 2,00 | 1,000 | 97,38937 | 94,24778 | 3,14159 | 3,226 % |
| 1,00 | 0,500 | 47,90929 | 47,12389 | 0,78540 | 1,639 % |
| 0,50 | 0,250 | 23,75829 | 23,56194 | 0,19635 | 0,826 % |
| 0,25 | 0,125 | 11,83006 | 11,78097 | 0,04909 | 0,415 % |

Absoluter Fehler **viertelt** sich, relativer Fehler **halbiert** sich.
Weitere Reglerstellungen zur Probe:
r₀ = 10, c = 1,2, t = 30, Δt = 0,5 → r = 46,000 m · A = 6647,6101 m² · dA/dt = 346,8318 m²/s · Fehler 1,13097 m²
r₀ = 2, c = 0,1, t = 0, Δt = 2,0 → r = 2,000 m · A = 12,5664 m² · dA/dt = 1,2566 m²/s · Fehler 0,12566 m²
Größtmöglicher Radius im Reglerbereich: r₀ = 20 m, c = 2,0 m/s, t = 50 s → r = **120 m** (A = 45238,93 m²).

**K18 — Aufgabe `a1`: Solarfeld l(t) = 40 + 3t (m), b(t) = 25 + 2t (m)**
A(t) = 6t² + 155t + 1000 ⟹ A′(t) = 12t + 155 ⟹ A′(0) = **155 m²/Jahr**.
Produktregel: l′·b(0) = 3 · 25 = **75 m²/Jahr**, l(0)·b′ = 40 · 2 = **80 m²/Jahr**, Summe 155 ✓
Eckstück eines ganzen Jahres: Δl·Δb = 3 · 2 = **6 m²**; A(1) − A(0) = 161 = 75 + 80 + 6 ✓
Kontrollwert A′(5) = 215 m²/Jahr.

**K19 — Aufgabe `a2`: Ballon V = (4/3)πr³ mit r(t) = 2 + 0,5t (cm, t in s)**
r(4) = **4,0 cm** · V(4) = 256π/3 ≈ 268,083 cm³
V′(t) = 4πr²·r′ ⟹ V′(4) = 4π · 16 · 0,5 = **32π ≈ 100,531 cm³/s**.
Distraktorwerte: 4πr² = 64π ≈ **201,062** (innere Ableitung vergessen, Faktor genau 2) ·
4π·2²·0,5 = 8π ≈ 25,133 (r₀ statt r(4)) · 4π·3,5²·0,5 ≈ 76,969 (r falsch abgelesen).

**K20 — Aufgabe `a3`: c(t) = 20t/(t² + 4) in mg/L, t in h**
c′(t) = [20(t² + 4) − 20t·2t]/(t² + 4)² = **(80 − 20t²)/(t² + 4)²** = −20(t−2)(t+2)/(t²+4)².
c′(1) = 60/25 = **2,4 mg/(L·h)** · c′(2) = **0** · c′(3) = −100/169 ≈ −0,592.
Funktionswerte: c(1) = 4 mg/L · c(2) = 5 mg/L · c(4) = 4 mg/L.
Der Nenner t² + 4 hat **keine** reelle Nullstelle — D = ℝ, hier also t ≥ 0 ohne Einschränkung.
Distraktorwerte: u′/v′ = 20/(2t) → **10** · ohne Quadrat im Nenner 60/5 = **12** ·
Zähler vertauscht **−2,4**.

**K21 — Aufgabe `a4`: Zylinder r(t) = 3 + 0,2t (cm), h(t) = 20 − 0,5t (cm), V = πr²h**
V(t) = π(−t³/50 + t²/5 + 39t/2 + 180) ⟹ V′(t) = π(−3t²/50 + 2t/5 + 39/2).
Bei t = 5: r = 4,0 cm · h = 17,5 cm · V(5) = 280π ≈ 879,646 cm³.
V′(5) = π[2·4·0,2·17,5 + 4²·(−0,5)] = π[28 − 8] = **20π ≈ 62,832 cm³/s**.
Distraktorwerte: π(2·4·17,5 − 8) ≈ **414,690** (innere Ableitung von r² vergessen) ·
28π ≈ **87,965** (nur der erste Summand) · −8π ≈ −25,133 (nur der zweite Summand) ·
mit π ≈ 3,14: 62,80 (liegt innerhalb der Toleranz).

**K22 — Aufgabe `a5`: p(t) = 4 + 0,2t (€), n(t) = 300 − 5t (Besucher)**
U′(t) = p′n + pn′ = 0,2(300 − 5t) + (4 + 0,2t)(−5) = (60 − t) + (−20 − t) = **40 − 2t**.
Nullstelle: t = **20 Tage** (= 480 Stunden); U″(t) = −2 < 0, also Maximum.
U(t) = −t² + 40t + 1200; U(0) = 1200 € · U(20) = **1600 €** · U(30) = 1500 €.
p(20) = 8,00 € · n(20) = 200 Besucher; Probe 8,00 · 200 = 1600 ✓
Vorzeichenfalle: 0,2(300 − 5t) − (4 + 0,2t)(−5) = 80 — konstant, also nie null.

**K23 — Aufgabe `z1`: vier Ableitungen aus denselben Bausteinen (alle symbolisch bestätigt)**

| Funktion | Regel | Ableitung | Probe bei x = 1 |
|---|---|---|---|
| f₁(x) = (2x + 1)³ | Kettenregel | 6(2x + 1)² | 54 |
| f₂(x) = x³(2x + 1) | Produktregel | 8x³ + 3x² = x²(8x + 3) | 11 |
| f₃(x) = x³/(2x + 1) | Quotientenregel | (4x³ + 3x²)/(2x + 1)² | 7/9 |
| f₄(x) = (2x + 1)/x³ | Quotientenregel | −(4x + 3)/x⁴ | −7 |

**K24 — Aufgabe `mc1`: f(x) = (2x − 3)⁴**
f′(x) = 4(2x − 3)³·2 = **8(2x − 3)³**; ausmultipliziert 64x³ − 288x² + 432x − 216, identisch mit der
Ableitung von 16x⁴ − 96x³ + 216x² − 216x + 81 ✓
f′(1,5) = 8·0³ = 0 (waagerechte Tangente) · f′(2) = 8·1³ = 8 · Distraktor 4(2x − 3)³ bei x = 2: 4.

**K25 — Aufgabe `a6`: Gegenbeispiel zu „beide Faktoren wachsen ⟹ Produkt wächst"**
u(t) = t, v(t) = t − 10; u′ = v′ = 1 > 0. An der Stelle t = 1: u = 1, v = −9,
(uv)′ = u′v + uv′ = 1·(−9) + 1·1 = **−8 < 0**.
Kontrolle über den Differenzenquotienten: (uv)(1) = −9,00 · (uv)(1,1) = −9,79 ·
Differenzenquotient = **−7,9** (nähert sich −8) ✓
Mit u, v > 0 stimmt die Behauptung: u = t + 1, v = t + 2 bei t = 0 ⟹ (uv)′ = 3 > 0.

**K26 — Aufgabe `a8`: f = g² auf zwei Wegen**
Produktregel auf g·g: g′g + gg′ = 2g·g′ · Kettenregel auf g²: 2g·g′ · Differenz **0** (symbolisch).
Beispiel g(x) = 3x + 1, f = g³: Kettenregel 3(3x+1)²·3 = **9(3x + 1)²**;
Produktregel auf (3x+1)(3x+1)(3x+1) ergibt ebenfalls **9(3x + 1)²** ✓

**K27 — Vertiefung, kombiniertes Beispiel f(x) = x²·√(2x + 1), D = [−0,5; ∞[**
f′(x) = 2x√(2x + 1) + x²/√(2x + 1) = **x(5x + 2)/√(2x + 1)** (beide Formen symbolisch identisch).
f(4) = 16·3 = **48** · f′(4) = 4·22/3 = **88/3 ≈ 29,333** · f′(1) = 7√3/3 ≈ 4,041 · f′(0) = 0.
Tangente bei x = 4: y = (88/3)x − 208/3; y-Achsenabschnitt −208/3 ≈ −69,333.

**K28 — Vertiefung, mehrfache Verkettung f(x) = √((3x² + 1)³) = (3x² + 1)^{3/2}**
f′(x) = (3/2)(3x² + 1)^{1/2}·6x = **9x√(3x² + 1)**.
f(1) = 8 · f′(1) = **18** · f(0) = 1 · f′(0) = 0 · f′(2) = 18√13 ≈ 64,900.

**K29 — Einordnung der Distraktoren in die Zonen der Zahlen-Engine**
Die Engine zeigt `nah`, wenn der Quotient aus Eingabe und Sollwert echt zwischen 0,5 und 2 liegt,
sonst `weit`. Geprüft:
`a1` (Soll 155): 6 → weit · 75 → weit (Faktor 0,484) · 80 → **nah** (Faktor 0,516) · 310 → weit.
`a2` (Soll 100,531): 201,062 → **weit** (Faktor exakt 2,0) · 25,133 → weit · 76,969 → nah.
`a3` (Soll 2,4): 10 → weit · 12 → weit · −2,4 → **nah** (Betragsfaktor 1,0) · 1,2 → weit.
`a4` (Soll 62,832): 414,690 → weit · 87,965 → **nah** (Faktor 1,4) · −25,133 → weit · 62,80 → im Toleranzband.
`a5` (Soll 20): 10 → weit · 30 → **nah** · 40 → weit · 60 → weit · 1600 → weit.
Alternativeinheit bei `a5`: 480 Stunden, geerbte Toleranz 0,2 · 480/20 = **4,8 h**.

---

## 1 · Einstieg

`<section id="einstieg">`, `.stufe`-Kopf: Nr. **1**, Überschrift **Einstieg**.

### 1.1 Aufhängertext (wörtlich, zwei Absätze)

> Ein Freibad hebt den Eintrittspreis jeden Tag um 10 Cent an — und jeden Tag kommen sechs
> Besucherinnen und Besucher weniger. Der Preis steigt also, die Nachfrage fällt. Was die
> Betreiberin interessiert, ist der Umsatz: Preis mal Besucherzahl. Steigt er, fällt er oder
> bleibt er gleich? Auf den ersten Blick ist das nicht zu sehen, denn die beiden Kurven zeigen in
> entgegengesetzte Richtungen.

> Naheliegend wäre, einfach die beiden Änderungsraten miteinander zu verrechnen: +0,10 mal (−6)
> ergibt −0,6, der Umsatz fiele also. Das ist falsch, und zwar nicht knapp: In Wirklichkeit
> **steigt** der Umsatz am ersten Tag um 10 € pro Tag. Zwischen dem naiven Ergebnis und der
> Wahrheit liegen ein Vorzeichen und ein Faktor von rund 17 (10,00 gegen 0,60, genauer 16,7). In dieser Einheit lernst du die drei Regeln
> kennen, mit denen man zusammengesetzte Funktionen ableitet: Produkte, Verkettungen und
> Quotienten. Potenzregel, Faktorregel und Summenregel aus der Einführungsphase setzt du dabei als
> bekannt voraus — ab jetzt reichen sie nicht mehr aus.

### 1.2 Vorwissen prüfen

Karte `.karte` mit Überschrift „Vorwissen prüfen" und dem Vorspann:
*„Drei Fragen aus der Einführungsphase. Wenn du hier hängst, lohnt sich ein Blick zurück, bevor du
weitermachst — die drei neuen Regeln bauen alle auf der Potenzregel und auf der Deutung der
Ableitung als Änderungsrate auf."*

Drei MC-Aufgaben ohne Rahmen und ohne `.ab`-Chip (`style="border:none;padding:0"` wie im
Referenzmodul).

---

**MC `vw1`** — richtige Option: Index **1**

Frage: *Leite ab: <span class="m" data-tex="f(x) = 3x^4 - 5x^2 + 2x - 9" data-plain="f(x) = 3x⁴ − 5x² + 2x − 9"></span>*

| Index | Option |
|---|---|
| 0 | <span class="m" data-tex="f'(x) = 12x^3 - 10x^2 + 2" data-plain="f′(x) = 12x³ − 10x² + 2"></span> |
| 1 | <span class="m" data-tex="f'(x) = 12x^3 - 10x + 2" data-plain="f′(x) = 12x³ − 10x + 2"></span> |
| 2 | <span class="m" data-tex="f'(x) = 12x^3 - 10x + 2x - 9" data-plain="f′(x) = 12x³ − 10x + 2x − 9"></span> |

Feedback:
- 0: „Beim mittleren Summanden hast du zwar mit dem Exponenten multipliziert (−5 · 2 = −10), den Exponenten selbst aber stehen lassen. Die Potenzregel senkt ihn um eins: aus −5x² wird −10x¹, also −10x."
- 1: „Richtig. Summanden einzeln ableiten, Vorfaktoren stehen lassen, Exponenten um eins senken: 3x⁴ → 12x³, −5x² → −10x, 2x → 2, −9 → 0."
- 2: „Die letzten beiden Summanden sind unverändert stehen geblieben. 2x hat die konstante Steigung 2, nicht 2x; und eine additive Konstante wie −9 verschiebt den Graphen nur nach unten — auf die Steigung hat sie keinen Einfluss, ihre Ableitung ist 0."

---

**MC `vw2`** — richtige Option: Index **0**

Frage: *Leite ab: <span class="m" data-tex="f(x) = \dfrac{1}{x^{3}}" data-plain="f(x) = 1/x³"></span> für <span class="m" data-tex="x \neq 0" data-plain="x ≠ 0"></span>.*

| Index | Option |
|---|---|
| 0 | <span class="m" data-tex="f'(x) = -\dfrac{3}{x^{4}}" data-plain="f′(x) = −3/x⁴"></span> |
| 1 | <span class="m" data-tex="f'(x) = -\dfrac{3}{x^{2}}" data-plain="f′(x) = −3/x²"></span> |
| 2 | <span class="m" data-tex="f'(x) = \dfrac{3}{x^{4}}" data-plain="f′(x) = 3/x⁴"></span> |

Feedback:
- 0: „Richtig. Schreibe zuerst um: 1/x³ = x⁻³. Die Potenzregel senkt den Exponenten um eins, also −3 − 1 = −4, und liefert −3x⁻⁴ = −3/x⁴. Probe bei x = 2: −3/16."
- 1: „Du hast den Exponenten −3 um eins **erhöht** statt gesenkt. Die Potenzregel senkt immer, auch bei negativen Exponenten: aus x⁻³ wird x⁻⁴, nicht x⁻²."
- 2: „Das Vorzeichen fehlt. Der Faktor, mit dem die Potenzregel multipliziert, ist der alte Exponent — und der ist hier −3, nicht +3. Inhaltlich passt das: 1/x³ fällt für x > 0, die Ableitung muss dort also negativ sein."

---

**MC `vw3`** — richtige Option: Index **2**

Frage: *<span class="m" data-tex="N(t)" data-plain="N(t)"></span> gibt die Besucherzahl eines Freibades am Tag <span class="m" data-tex="t" data-plain="t"></span> an, gemessen in Personen. Es ist <span class="m" data-tex="N'(5) = -6" data-plain="N′(5) = −6"></span>. Was bedeutet das?*

| Index | Option |
|---|---|
| 0 | Am fünften Tag waren 6 Besucher da. |
| 1 | Vom ersten bis zum fünften Tag sind insgesamt 6 Besucher weniger gekommen. |
| 2 | Um den fünften Tag herum nimmt die Besucherzahl mit etwa 6 Personen pro Tag ab. |

Feedback:
- 0: „Das wäre N(5), der Funktionswert. Die Ableitung misst nicht den Bestand, sondern seine Änderung. Im Modell N(t) = 400 − 6t ist N(5) = 370 — und N′(5) trotzdem −6."
- 1: „Das wäre die Gesamtänderung N(5) − N(1), also eine Differenz über vier Tage. N′(5) ist dagegen eine **Rate**: eine Änderung *pro Tag*, an der Stelle t = 5."
- 2: „Richtig. Die Ableitung ist die lokale Änderungsrate; ihre Einheit ist hier Personen pro Tag. Probe im Modell N(t) = 400 − 6t: N(5) = 370, N(6) = 364, Differenz −6. Genau diese Unterscheidung zwischen Wert und Rate brauchst du gleich bei jeder der drei neuen Regeln."

## 2 · Erklärteil

`<section id="regeln">`, `.stufe`-Kopf: Nr. **2**, Überschrift **Produktregel und Kettenregel**.

### 2.1 Warum die bekannten Regeln nicht reichen

Fließtext (wörtlich):

> Summenregel und Faktorregel haben eine bequeme Eigenschaft: Man darf die Funktion zerlegen,
> die Teile einzeln ableiten und die Ergebnisse wieder zusammensetzen. Genau diese Eigenschaft
> verführt dazu, dasselbe beim Produkt zu erwarten. Das Gegenbeispiel ist so klein, dass es in
> eine Zeile passt.

Abgesetzte Formel (`.m.block`):

`data-tex`: `f(x) = x\cdot x = x^{2} \quad\Longrightarrow\quad f'(x) = 2x, \qquad \text{aber}\quad x'\cdot x' = 1\cdot 1 = 1`
`data-plain`: `f(x) = x · x = x² ⟹ f′(x) = 2x,  aber  x′ · x′ = 1 · 1 = 1`

> An der Stelle x = 4 sagt die eine Rechnung 8, die andere 1. Das ist kein Rundungsproblem,
> sondern ein Strukturfehler: Ein Produkt ist keine Summe, und beim Ableiten darf man es nicht
> wie eine behandeln.

`.hinweis`-Kasten (**die zentrale Fehlvorstellung dieses Moduls**):

> **Häufigster Fehler überhaupt.** „Beim Produkt leite ich beide Faktoren ab und multipliziere
> die Ergebnisse." Das ist falsch, und du kannst es dir mit
> <span class="m" data-tex="x\cdot x" data-plain="x · x"></span> jederzeit in fünf Sekunden selbst
> widerlegen. Dieselbe Falle gibt es beim Quotienten: Auch
> <span class="m" data-tex="\left(\frac{u}{v}\right)' = \frac{u'}{v'}" data-plain="(u/v)′ = u′/v′"></span>
> ist falsch — siehe Abschnitt 3.1.

### 2.2 Die Produktregel

Fließtext:

> Was beim Produkt tatsächlich passiert, siehst du am besten an einem Rechteck. Seine Seiten seien
> <span class="m" data-tex="u(x)" data-plain="u(x)"></span> und
> <span class="m" data-tex="v(x)" data-plain="v(x)"></span>, sein Flächeninhalt ist das Produkt
> <span class="m" data-tex="P(x) = u(x)\cdot v(x)" data-plain="P(x) = u(x) · v(x)"></span>. Wächst
> <span class="m" data-tex="x" data-plain="x"></span> um ein kleines Stück
> <span class="m" data-tex="h" data-plain="h"></span>, so kommen drei Flächenstücke hinzu: ein
> Streifen der Breite <span class="m" data-tex="\Delta u" data-plain="Δu"></span> entlang der
> Seite <span class="m" data-tex="v" data-plain="v"></span>, ein Streifen der Breite
> <span class="m" data-tex="\Delta v" data-plain="Δv"></span> entlang der Seite
> <span class="m" data-tex="u" data-plain="u"></span> — und in der Ecke ein kleines Rechteck
> <span class="m" data-tex="\Delta u\cdot\Delta v" data-plain="Δu · Δv"></span>.

Abgesetzte Formel:

`data-tex`: `\Delta P = v\cdot\Delta u \;+\; u\cdot\Delta v \;+\; \Delta u\cdot\Delta v`
`data-plain`: `ΔP = v · Δu + u · Δv + Δu · Δv`

> Teilt man durch <span class="m" data-tex="h" data-plain="h"></span>, so werden aus den beiden
> großen Streifen die Ausdrücke
> <span class="m" data-tex="v\cdot\frac{\Delta u}{h}" data-plain="v · Δu/h"></span> und
> <span class="m" data-tex="u\cdot\frac{\Delta v}{h}" data-plain="u · Δv/h"></span> — also genau
> die beiden Differenzenquotienten, jeweils bewertet mit der momentanen Länge der anderen Seite.
> Das Eckstück dagegen enthält **zwei** kleine Faktoren; geteilt durch
> <span class="m" data-tex="h" data-plain="h"></span> bleibt immer noch einer davon übrig und geht
> gegen null. Genau das ist der Grund, warum in der Produktregel ein Pluszeichen steht und kein
> Malzeichen.

`.merksatz`:

> **Produktregel**
> Für differenzierbare Funktionen <span class="m" data-tex="u" data-plain="u"></span> und
> <span class="m" data-tex="v" data-plain="v"></span> gilt
> <span class="m" data-tex="(u\cdot v)' = u'\cdot v + u\cdot v'" data-plain="(u · v)′ = u′ · v + u · v′"></span>.
> Inhaltlich: Ändern sich beide Faktoren, so setzt sich die Änderungsrate des Produkts **additiv**
> aus zwei Beiträgen zusammen. Jeder Faktor steuert seine eigene Änderung bei, und diese Änderung
> wird mit dem **momentanen Wert** des jeweils anderen Faktors bewertet. Wer nur die Raten
> miteinander multipliziert, lässt beide Werte unter den Tisch fallen.

Abgesetzte Formel (die Regel groß):

`data-tex`: `\big(u(x)\cdot v(x)\big)' \;=\; u'(x)\,v(x) \;+\; u(x)\,v'(x)`
`data-plain`: `(u(x) · v(x))′ = u′(x) · v(x) + u(x) · v′(x)`

**`<details>` — vollständige Herleitung über den Differenzenquotienten**
Summary: *Herleitung der Produktregel aus dem Differenzenquotienten*

> Sei <span class="m" data-tex="f = u\cdot v" data-plain="f = u · v"></span> mit differenzierbaren
> Funktionen <span class="m" data-tex="u" data-plain="u"></span> und
> <span class="m" data-tex="v" data-plain="v"></span>. Der Differenzenquotient lautet
>
> <span class="m block" data-tex="\frac{f(x+h)-f(x)}{h} = \frac{u(x+h)\,v(x+h) - u(x)\,v(x)}{h}" data-plain="[f(x+h) − f(x)]/h = [u(x+h)·v(x+h) − u(x)·v(x)]/h"></span>
>
> Im Zähler steht ein einziger Ausdruck, aus dem sich noch kein Differenzenquotient ablesen lässt.
> Der Trick besteht darin, eine passende Null zu addieren, nämlich
> <span class="m" data-tex="-\,u(x)\,v(x+h) + u(x)\,v(x+h)" data-plain="−u(x)·v(x+h) + u(x)·v(x+h)"></span>:
>
> <span class="m block" data-tex="\frac{u(x+h)v(x+h) - u(x)v(x+h) + u(x)v(x+h) - u(x)v(x)}{h}" data-plain="[u(x+h)v(x+h) − u(x)v(x+h) + u(x)v(x+h) − u(x)v(x)] / h"></span>
>
> Jetzt lassen sich die ersten beiden und die letzten beiden Summanden zusammenfassen:
>
> <span class="m block" data-tex="= \frac{u(x+h)-u(x)}{h}\cdot v(x+h) \;+\; u(x)\cdot\frac{v(x+h)-v(x)}{h}" data-plain="= [u(x+h) − u(x)]/h · v(x+h) + u(x) · [v(x+h) − v(x)]/h"></span>
>
> Nun der Grenzübergang <span class="m" data-tex="h\to 0" data-plain="h → 0"></span>. Der erste
> Differenzenquotient strebt gegen
> <span class="m" data-tex="u'(x)" data-plain="u′(x)"></span>, der zweite gegen
> <span class="m" data-tex="v'(x)" data-plain="v′(x)"></span>. Bleibt der Faktor
> <span class="m" data-tex="v(x+h)" data-plain="v(x+h)"></span>: Weil
> <span class="m" data-tex="v" data-plain="v"></span> differenzierbar ist, ist
> <span class="m" data-tex="v" data-plain="v"></span> auch stetig, und deshalb gilt
> <span class="m" data-tex="v(x+h)\to v(x)" data-plain="v(x+h) → v(x)"></span>. Insgesamt:
>
> <span class="m block" data-tex="f'(x) = u'(x)\,v(x) + u(x)\,v'(x)" data-plain="f′(x) = u′(x)·v(x) + u(x)·v′(x)"></span>
>
> Zwei Beobachtungen zum Mitnehmen. Erstens: Die Stetigkeit von
> <span class="m" data-tex="v" data-plain="v"></span> wird wirklich gebraucht — ohne sie bricht der
> Beweis an dieser einen Stelle zusammen. Zweitens: In der Rechteckdeutung ist der ergänzte
> Nullterm genau das Eckstück; es taucht auf und verschwindet wieder, weil es zwei kleine Faktoren
> enthält.

**Durchgerechnetes Beispiel mit Selbstkontrolle** (Fließtext + Formeln, Kontrollwerte aus K6):

> <span class="m" data-tex="f(x) = (x^{3}-2x)(4x+5)" data-plain="f(x) = (x³ − 2x)(4x + 5)"></span>
> mit <span class="m" data-tex="u(x)=x^{3}-2x" data-plain="u(x) = x³ − 2x"></span> und
> <span class="m" data-tex="v(x)=4x+5" data-plain="v(x) = 4x + 5"></span>, also
> <span class="m" data-tex="u'(x)=3x^{2}-2" data-plain="u′(x) = 3x² − 2"></span> und
> <span class="m" data-tex="v'(x)=4" data-plain="v′(x) = 4"></span>.
>
> <span class="m block" data-tex="f'(x) = (3x^{2}-2)(4x+5) + (x^{3}-2x)\cdot 4 = 12x^{3}+15x^{2}-8x-10 + 4x^{3}-8x = 16x^{3}+15x^{2}-16x-10" data-plain="f′(x) = (3x² − 2)(4x + 5) + (x³ − 2x)·4 = 12x³ + 15x² − 8x − 10 + 4x³ − 8x = 16x³ + 15x² − 16x − 10"></span>
>
> Diese Aufgabe kannst du selbst kontrollieren, und das solltest du beim Üben auch tun:
> Ausmultiplizieren liefert
> <span class="m" data-tex="f(x)=4x^{4}+5x^{3}-8x^{2}-10x" data-plain="f(x) = 4x⁴ + 5x³ − 8x² − 10x"></span>,
> und die Potenzregel darauf ergibt dasselbe Ergebnis. Stichprobe:
> <span class="m" data-tex="f'(1)=5" data-plain="f′(1) = 5"></span> und
> <span class="m" data-tex="f'(2)=146" data-plain="f′(2) = 146"></span>.

`.hinweis`:

> **Wann lohnt sich die Produktregel überhaupt?** Bei einem Produkt zweier Polynome kommst du auch
> durch Ausmultiplizieren ans Ziel — bei kleinen Termen ist das oft sogar schneller. Unverzichtbar
> wird die Regel, sobald ein Faktor **nicht** ausmultiplizierbar ist, etwa
> <span class="m" data-tex="x^{2}\sqrt{2x+1}" data-plain="x²·√(2x+1)"></span> (Abschnitt 3.4) oder
> später <span class="m" data-tex="x\cdot\mathrm{e}^{x}" data-plain="x · eˣ"></span>. Bis dahin ist
> das Ausmultiplizieren deine beste Selbstkontrolle.

### 2.3 Der Einstieg, jetzt gerechnet

> Zurück ins Freibad. Preis
> <span class="m" data-tex="p(t)=5{,}00 + 0{,}10\,t" data-plain="p(t) = 5,00 + 0,10 t"></span> in €,
> Besucherzahl <span class="m" data-tex="n(t)=400-6t" data-plain="n(t) = 400 − 6 t"></span>,
> Umsatz <span class="m" data-tex="U(t)=p(t)\cdot n(t)" data-plain="U(t) = p(t) · n(t)"></span>.
>
> <span class="m block" data-tex="U'(t) = p'(t)\,n(t) + p(t)\,n'(t) = 0{,}10\cdot n(t) + p(t)\cdot(-6)" data-plain="U′(t) = p′(t)·n(t) + p(t)·n′(t) = 0,10 · n(t) + p(t) · (−6)"></span>
>
> Am Tag <span class="m" data-tex="t=0" data-plain="t = 0"></span>:
> <span class="m" data-tex="U'(0) = 0{,}10\cdot 400 + 5{,}00\cdot(-6) = 40 - 30 = 10" data-plain="U′(0) = 0,10 · 400 + 5,00 · (−6) = 40 − 30 = 10"></span>, also **+10 € pro Tag**.
> Die beiden Beiträge haben handfeste Bedeutungen: 40 €/Tag kommen dadurch herein, dass die noch
> vorhandenen 400 Gäste 10 Cent mehr zahlen; 30 €/Tag gehen verloren, weil sechs Gäste zu je 5 €
> ausbleiben. Der Preisbeitrag überwiegt — vorerst.

`.merksatz`:

> **Warum die naive Rechnung so gründlich danebenliegt**
> <span class="m" data-tex="p'\cdot n' = 0{,}10\cdot(-6) = -0{,}60" data-plain="p′ · n′ = 0,10 · (−6) = −0,60"></span>
> hat nicht nur den falschen Betrag, sondern auch das falsche Vorzeichen. Der Grund ist immer
> derselbe: In der Produktregel stehen die **Werte** 400 und 5,00 — und die sind hier hundertmal
> größer als die Raten. Eine kleine relative Änderung eines großen Bestands ist ein großer
> absoluter Beitrag.

### 2.4 Die Kettenregel

> Der zweite Bauplan für zusammengesetzte Funktionen ist die Verkettung. Bei
> <span class="m" data-tex="f(x)=(2x-1)^{3}" data-plain="f(x) = (2x − 1)³"></span> passiert
> zweierlei nacheinander: Erst wird aus <span class="m" data-tex="x" data-plain="x"></span> der
> Wert <span class="m" data-tex="u=2x-1" data-plain="u = 2x − 1"></span> gebildet, dann wird dieser
> Wert hoch drei genommen. Man nennt
> <span class="m" data-tex="u(x)=2x-1" data-plain="u(x) = 2x − 1"></span> die **innere** und
> <span class="m" data-tex="v(u)=u^{3}" data-plain="v(u) = u³"></span> die **äußere** Funktion;
> zusammen ist <span class="m" data-tex="f(x)=v\big(u(x)\big)" data-plain="f(x) = v(u(x))"></span>.

Kleine Tabelle (in `<div class="tabelle">`) — Zerlegung üben:

| Funktion | innere Funktion <span class="m" data-tex="u(x)" data-plain="u(x)"></span> | äußere Funktion <span class="m" data-tex="v(u)" data-plain="v(u)"></span> |
|---|---|---|
| <span class="m" data-tex="(2x-1)^{3}" data-plain="(2x − 1)³"></span> | <span class="m" data-tex="2x-1" data-plain="2x − 1"></span> | <span class="m" data-tex="u^{3}" data-plain="u³"></span> |
| <span class="m" data-tex="\sqrt{x^{2}+1}" data-plain="√(x² + 1)"></span> | <span class="m" data-tex="x^{2}+1" data-plain="x² + 1"></span> | <span class="m" data-tex="\sqrt{u}" data-plain="√u"></span> |
| <span class="m" data-tex="\dfrac{1}{4x+7}" data-plain="1/(4x + 7)"></span> | <span class="m" data-tex="4x+7" data-plain="4x + 7"></span> | <span class="m" data-tex="u^{-1}" data-plain="u⁻¹"></span> |
| <span class="m" data-tex="\big(x^{2}-3x\big)^{5}" data-plain="(x² − 3x)⁵"></span> | <span class="m" data-tex="x^{2}-3x" data-plain="x² − 3x"></span> | <span class="m" data-tex="u^{5}" data-plain="u⁵"></span> |

Abgesetzte Formel (die Regel):

`data-tex`: `\big(v(u(x))\big)' \;=\; v'\big(u(x)\big)\cdot u'(x) \qquad\text{oder}\qquad \frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}u}\cdot\frac{\mathrm{d}u}{\mathrm{d}x}`
`data-plain`: `(v(u(x)))′ = v′(u(x)) · u′(x)   oder   dy/dx = dy/du · du/dx`

`.merksatz`:

> **Kettenregel**
> Äußere Ableitung mal innere Ableitung — und die äußere Ableitung wird **an der Stelle
> <span class="m" data-tex="u(x)" data-plain="u(x)"></span>** ausgewertet, nicht an der Stelle
> <span class="m" data-tex="x" data-plain="x"></span>. Inhaltlich ist die Kettenregel eine Aussage
> über Übersetzungsverhältnisse: Werden zwei Abhängigkeiten hintereinandergeschaltet, so
> **multiplizieren** sich ihre Änderungsraten, genau wie bei zwei Getriebestufen. Dreht sich die
> zweite Welle dreimal so schnell wie die erste und die erste doppelt so schnell wie die Kurbel,
> dann ist der Gesamtfaktor sechs — und nicht fünf.

**`<details>` — Herleitung der Kettenregel, mit ehrlich benannter Lücke**
Summary: *Warum sich die Änderungsraten multiplizieren*

> Der Ansatz ist eine Erweiterung des Differenzenquotienten. Sei
> <span class="m" data-tex="f(x)=v(u(x))" data-plain="f(x) = v(u(x))"></span> und
> <span class="m" data-tex="k = u(x+h)-u(x)" data-plain="k = u(x+h) − u(x)"></span> die Änderung
> der inneren Funktion. Solange
> <span class="m" data-tex="k\neq 0" data-plain="k ≠ 0"></span> ist, darf man erweitern:
>
> <span class="m block" data-tex="\frac{v(u(x+h))-v(u(x))}{h} = \underbrace{\frac{v(u(x)+k)-v(u(x))}{k}}_{\to\, v'(u(x))}\cdot\underbrace{\frac{u(x+h)-u(x)}{h}}_{\to\, u'(x)}" data-plain="[v(u(x+h)) − v(u(x))]/h = ([v(u(x)+k) − v(u(x))]/k) · ([u(x+h) − u(x)]/h) → v′(u(x)) · u′(x)"></span>
>
> Für <span class="m" data-tex="h\to 0" data-plain="h → 0"></span> geht auch
> <span class="m" data-tex="k\to 0" data-plain="k → 0"></span>, weil
> <span class="m" data-tex="u" data-plain="u"></span> als differenzierbare Funktion stetig ist.
> Der linke Faktor ist dann der Differenzenquotient von
> <span class="m" data-tex="v" data-plain="v"></span> an der Stelle
> <span class="m" data-tex="u(x)" data-plain="u(x)"></span> — und genau hier sieht man, warum
> <span class="m" data-tex="v'" data-plain="v′"></span> an der Stelle
> <span class="m" data-tex="u(x)" data-plain="u(x)"></span> und nicht an der Stelle
> <span class="m" data-tex="x" data-plain="x"></span> ausgewertet wird.
>
> **Die Lücke.** Das Argument setzt voraus, dass
> <span class="m" data-tex="k\neq 0" data-plain="k ≠ 0"></span> ist. Es gibt Funktionen, bei denen
> <span class="m" data-tex="u(x+h)=u(x)" data-plain="u(x+h) = u(x)"></span> für beliebig kleine
> <span class="m" data-tex="h" data-plain="h"></span> vorkommt; dann steht im Nenner eine Null.
> Ein vollständiger Beweis vermeidet das Dividieren, indem er die Differenzierbarkeit als lineare
> Näherung schreibt: <span class="m" data-tex="v(u_0+k) = v(u_0) + v'(u_0)\,k + r(k)\cdot k" data-plain="v(u₀ + k) = v(u₀) + v′(u₀)·k + r(k)·k"></span>
> mit <span class="m" data-tex="r(k)\to 0" data-plain="r(k) → 0"></span>. Dieser Weg wird im
> Leistungskurs nicht verlangt — dass die obige Rechnung eine Lücke hat, solltest du trotzdem
> wissen, statt sie für einen lückenlosen Beweis zu halten.

**Zwei durchgerechnete Beispiele** (Kontrollwerte aus K7 und K8):

> **(a)** <span class="m" data-tex="f(x)=(2x-1)^{3}" data-plain="f(x) = (2x − 1)³"></span>:
> äußere Ableitung <span class="m" data-tex="3u^{2}" data-plain="3u²"></span>, innere Ableitung 2,
> also
> <span class="m" data-tex="f'(x)=3(2x-1)^{2}\cdot 2 = 6(2x-1)^{2}" data-plain="f′(x) = 3(2x − 1)² · 2 = 6(2x − 1)²"></span>.
> Kontrolle durch Ausmultiplizieren:
> <span class="m" data-tex="f(x)=8x^{3}-12x^{2}+6x-1" data-plain="f(x) = 8x³ − 12x² + 6x − 1"></span>,
> abgeleitet
> <span class="m" data-tex="24x^{2}-24x+6 = 6(2x-1)^{2}" data-plain="24x² − 24x + 6 = 6(2x − 1)²"></span> ✓
> Stichprobe: <span class="m" data-tex="f'(2)=6\cdot 3^{2}=54" data-plain="f′(2) = 6 · 3² = 54"></span>.
>
> **(b)** <span class="m" data-tex="f(x)=\sqrt{x^{2}+1}" data-plain="f(x) = √(x² + 1)"></span>:
> mit <span class="m" data-tex="v(u)=\sqrt{u}=u^{1/2}" data-plain="v(u) = √u = u^(1/2)"></span> ist
> <span class="m" data-tex="v'(u)=\frac{1}{2\sqrt{u}}" data-plain="v′(u) = 1/(2√u)"></span>, also
> <span class="m block" data-tex="f'(x) = \frac{1}{2\sqrt{x^{2}+1}}\cdot 2x = \frac{x}{\sqrt{x^{2}+1}}" data-plain="f′(x) = 1/(2·√(x²+1)) · 2x = x/√(x² + 1)"></span>
> Hier ist Ausmultiplizieren keine Option mehr — ohne Kettenregel kommst du nicht weiter.
> Stichprobe: <span class="m" data-tex="f'(2)=\tfrac{2}{\sqrt 5}\approx 0{,}8944" data-plain="f′(2) = 2/√5 ≈ 0,8944"></span>.

`.hinweis` (**zweite und dritte Fehlvorstellung**):

> **Zwei Fallen bei der Kettenregel.**
> **(1) Die innere Ableitung fehlt.** Aus
> <span class="m" data-tex="(2x-3)^{4}" data-plain="(2x − 3)⁴"></span> wird gern
> <span class="m" data-tex="4(2x-3)^{3}" data-plain="4(2x − 3)³"></span> statt
> <span class="m" data-tex="8(2x-3)^{3}" data-plain="8(2x − 3)³"></span>. Probe: Der Graph von
> <span class="m" data-tex="(2x-3)^{4}" data-plain="(2x − 3)⁴"></span> ist gegenüber
> <span class="m" data-tex="x^{4}" data-plain="x⁴"></span> waagerecht gestaucht — er wird steiler,
> die Ableitung muss also größer ausfallen, nicht kleiner.
> **(2) Die äußere Ableitung wird an der falschen Stelle ausgewertet.** In
> <span class="m" data-tex="v'(u(x))" data-plain="v′(u(x))"></span> steht die **innere Funktion**
> im Argument, nicht <span class="m" data-tex="x" data-plain="x"></span>. Bei
> <span class="m" data-tex="\sqrt{x^{2}+1}" data-plain="√(x² + 1)"></span> heißt das
> <span class="m" data-tex="\frac{1}{2\sqrt{x^{2}+1}}" data-plain="1/(2·√(x²+1))"></span> und
> eben nicht <span class="m" data-tex="\frac{1}{2\sqrt{x}}" data-plain="1/(2√x)"></span>.

## 3 · Vertiefung

`<section id="kombination">`, `.stufe`-Kopf: Nr. **3**, Überschrift **Die Quotientenregel — und wie die drei Regeln zusammenspielen**.

### 3.1 Der Quotient: dieselbe Falle, dasselbe Gegenbeispiel

> Auch beim Bruch liegt die naive Vermutung nahe: oben ableiten, unten ableiten, fertig. Und auch
> hier widerlegt ein Einzeiler die Vermutung.

Abgesetzte Formel:

`data-tex`: `f(x) = \frac{x^{2}}{x} = x \;\Longrightarrow\; f'(x) = 1, \qquad \text{aber}\quad \frac{(x^{2})'}{(x)'} = \frac{2x}{1} = 2x`
`data-plain`: `f(x) = x²/x = x ⟹ f′(x) = 1,  aber  (x²)′/(x)′ = 2x/1 = 2x`

> An der Stelle <span class="m" data-tex="x=3" data-plain="x = 3"></span> steht 1 gegen 6. Die
> Funktion <span class="m" data-tex="x^{2}/x" data-plain="x²/x"></span> ist für
> <span class="m" data-tex="x\neq 0" data-plain="x ≠ 0"></span> nichts anderes als die Gerade
> <span class="m" data-tex="y=x" data-plain="y = x"></span> mit der konstanten Steigung 1 — die
> naive Rechnung behauptet dagegen eine Steigung, die mit
> <span class="m" data-tex="x" data-plain="x"></span> wächst.

### 3.2 Erst der Kehrwert: die Reziprokenregel

> Bevor wir den allgemeinen Bruch angehen, klären wir den Spezialfall
> <span class="m" data-tex="w = \frac{1}{v}" data-plain="w = 1/v"></span>. Dafür braucht es nicht
> einmal eine neue Idee, sondern nur die Produktregel und einen Blick auf die Gleichung
> <span class="m" data-tex="v(x)\cdot w(x) = 1" data-plain="v(x) · w(x) = 1"></span>.

**`<details>` — Reziprokenregel aus der Produktregel**
Summary: *Warum <span class="m" data-tex="\left(\frac{1}{v}\right)' = -\frac{v'}{v^{2}}" data-plain="(1/v)′ = −v′/v²"></span> gilt*

> Sei <span class="m" data-tex="v(x)\neq 0" data-plain="v(x) ≠ 0"></span> und
> <span class="m" data-tex="w(x)=\frac{1}{v(x)}" data-plain="w(x) = 1/v(x)"></span>. Dann ist
> <span class="m" data-tex="v(x)\cdot w(x) = 1" data-plain="v(x) · w(x) = 1"></span> für alle
> zulässigen <span class="m" data-tex="x" data-plain="x"></span>. Beide Seiten werden abgeleitet;
> rechts steht eine Konstante, ihre Ableitung ist null. Links greift die Produktregel:
>
> <span class="m block" data-tex="v'(x)\,w(x) + v(x)\,w'(x) = 0 \quad\Longrightarrow\quad w'(x) = -\frac{v'(x)\,w(x)}{v(x)} = -\frac{v'(x)}{v(x)^{2}}" data-plain="v′(x)·w(x) + v(x)·w′(x) = 0 ⟹ w′(x) = −v′(x)·w(x)/v(x) = −v′(x)/v(x)²"></span>
>
> Im letzten Schritt wurde <span class="m" data-tex="w(x)=1/v(x)" data-plain="w(x) = 1/v(x)"></span>
> eingesetzt. Probe an <span class="m" data-tex="v(x)=x" data-plain="v(x) = x"></span>:
> <span class="m" data-tex="(1/x)' = -1/x^{2}" data-plain="(1/x)′ = −1/x²"></span> ✓ — dasselbe
> Ergebnis liefert die Potenzregel über
> <span class="m" data-tex="x^{-1}" data-plain="x⁻¹"></span>. Zweite Probe:
> <span class="m" data-tex="v(x)=x^{2}+1" data-plain="v(x) = x² + 1"></span> ergibt
> <span class="m" data-tex="-\frac{2x}{(x^{2}+1)^{2}}" data-plain="−2x/(x² + 1)²"></span> ✓
>
> Dieser Weg hat einen Vorzug gegenüber dem naheliegenden „schreibe
> <span class="m" data-tex="1/v" data-plain="1/v"></span> als
> <span class="m" data-tex="v^{-1}" data-plain="v⁻¹"></span> und wende die Kettenregel an": Er
> setzt die Potenzregel für negative Exponenten nicht voraus, sondern kommt allein mit der
> Produktregel aus.

### 3.3 Die Quotientenregel

> Jetzt der allgemeine Fall. Ein Bruch ist ein Produkt mit einem Kehrwert:
> <span class="m" data-tex="\frac{u}{v} = u\cdot\frac{1}{v}" data-plain="u/v = u · (1/v)"></span>.
> Produktregel und Reziprokenregel zusammen liefern die dritte Regel, ohne dass irgendetwas Neues
> angenommen werden muss.

**`<details>` — vollständige Herleitung der Quotientenregel**
Summary: *Die Quotientenregel aus Produkt- und Reziprokenregel*

> <span class="m block" data-tex="\left(\frac{u}{v}\right)' = \left(u\cdot\frac{1}{v}\right)' = u'\cdot\frac{1}{v} + u\cdot\left(-\frac{v'}{v^{2}}\right) = \frac{u'}{v} - \frac{u\,v'}{v^{2}}" data-plain="(u/v)′ = (u · 1/v)′ = u′ · (1/v) + u · (−v′/v²) = u′/v − u·v′/v²"></span>
>
> Beide Summanden werden auf den Hauptnenner
> <span class="m" data-tex="v^{2}" data-plain="v²"></span> gebracht:
>
> <span class="m block" data-tex="= \frac{u'\,v}{v^{2}} - \frac{u\,v'}{v^{2}} = \frac{u'\,v - u\,v'}{v^{2}}" data-plain="= u′v/v² − uv′/v² = (u′v − uv′)/v²"></span>
>
> Vorausgesetzt wird dabei: <span class="m" data-tex="u" data-plain="u"></span> und
> <span class="m" data-tex="v" data-plain="v"></span> sind differenzierbar und
> <span class="m" data-tex="v(x)\neq 0" data-plain="v(x) ≠ 0"></span> an der betrachteten Stelle.
> Die zweite Bedingung ist keine Formalie: An einer Nullstelle des Nenners ist die Funktion gar
> nicht definiert, dort kann man auch nicht ableiten.

Abgesetzte Formel (die Regel):

`data-tex`: `\left(\frac{u(x)}{v(x)}\right)' = \frac{u'(x)\,v(x) - u(x)\,v'(x)}{\big(v(x)\big)^{2}}, \qquad v(x)\neq 0`
`data-plain`: `(u(x)/v(x))′ = [u′(x)·v(x) − u(x)·v′(x)] / (v(x))²,  v(x) ≠ 0`

`.merksatz`:

> **Quotientenregel**
> Sie ist keine vierte, eigenständige Regel, sondern Produkt- und Reziprokenregel in einer Zeile.
> Zwei Dinge unterscheiden sie von der Produktregel, und beide sind inhaltlich begründet.
> **Erstens** steht im Zähler ein Minus: Ein wachsender Nenner macht den Bruch kleiner, deshalb
> geht <span class="m" data-tex="v'" data-plain="v′"></span> mit negativem Vorzeichen ein.
> **Zweitens** darfst du die beiden Summanden im Zähler nicht vertauschen — bei der Produktregel
> ist die Reihenfolge gleichgültig, hier entscheidet sie über das Vorzeichen des Ergebnisses.
> Merkhilfe für die Reihenfolge: Der Zähler beginnt mit der Ableitung des Zählers.

**Durchgerechnetes Beispiel** (Kontrollwerte aus K10):

> <span class="m" data-tex="f(x)=\dfrac{x^{2}+1}{x-2}" data-plain="f(x) = (x² + 1)/(x − 2)"></span>
> mit <span class="m" data-tex="D = \mathbb{R}\setminus\{2\}" data-plain="D = ℝ \ {2}"></span>.
> Es ist <span class="m" data-tex="u=x^{2}+1,\; u'=2x,\; v=x-2,\; v'=1" data-plain="u = x² + 1, u′ = 2x, v = x − 2, v′ = 1"></span>:
>
> <span class="m block" data-tex="f'(x) = \frac{2x(x-2) - (x^{2}+1)\cdot 1}{(x-2)^{2}} = \frac{2x^{2}-4x-x^{2}-1}{(x-2)^{2}} = \frac{x^{2}-4x-1}{(x-2)^{2}}" data-plain="f′(x) = [2x(x − 2) − (x² + 1)·1]/(x − 2)² = (2x² − 4x − x² − 1)/(x − 2)² = (x² − 4x − 1)/(x − 2)²"></span>
>
> Stichproben: <span class="m" data-tex="f'(3) = \frac{9-12-1}{1} = -4" data-plain="f′(3) = (9 − 12 − 1)/1 = −4"></span> und
> <span class="m" data-tex="f'(0) = \frac{-1}{4} = -0{,}25" data-plain="f′(0) = −1/4 = −0,25"></span>.
> Beachte: Der Nenner wird **nicht** ausmultipliziert. Faktorisiert stehen zu lassen spart Arbeit,
> und für die Suche nach Nullstellen von
> <span class="m" data-tex="f'" data-plain="f′"></span> zählt ohnehin nur der Zähler.

`.hinweis`:

> **Nullstellen der Ableitung bei Brüchen.** Ein Bruch ist genau dann null, wenn sein Zähler null
> ist und der Nenner nicht. Weil der Nenner
> <span class="m" data-tex="v^{2}" data-plain="v²"></span> auf dem gesamten Definitionsbereich
> positiv ist, gilt die bequeme Regel: **Waagerechte Tangenten findest du allein über
> <span class="m" data-tex="u'v - uv' = 0" data-plain="u′v − uv′ = 0"></span>.** Wer den Nenner
> ausmultipliziert, macht sich unnötig Arbeit.

### 3.4 Welche Regel zuerst? Die Regeln kombinieren

> In der Praxis steckt selten nur eine Regel in einem Term. Die Entscheidung fällt immer gleich:
> **Schau auf die äußerste Verknüpfung** — auf diejenige Rechenoperation, die du als letzte
> ausführen würdest, wenn du für ein konkretes
> <span class="m" data-tex="x" data-plain="x"></span> den Funktionswert berechnest. Nicht auf die
> auffälligste, sondern auf die äußerste.

Tabelle (in `<div class="tabelle">`):

| Term | letzte Rechenoperation | zuerst anzuwendende Regel |
|---|---|---|
| <span class="m" data-tex="x^{2}\sqrt{2x+1}" data-plain="x² · √(2x + 1)"></span> | Multiplikation | Produktregel, darin Kettenregel für die Wurzel |
| <span class="m" data-tex="\big(x^{2}(2x+1)\big)^{3}" data-plain="(x²(2x + 1))³"></span> | Potenzieren | Kettenregel, darin Produktregel für die innere Funktion |
| <span class="m" data-tex="\dfrac{x^{3}}{2x+1}" data-plain="x³/(2x + 1)"></span> | Division | Quotientenregel |
| <span class="m" data-tex="\left(\dfrac{x}{x+1}\right)^{4}" data-plain="(x/(x + 1))⁴"></span> | Potenzieren | Kettenregel, darin Quotientenregel |

**Durchgerechnetes Beispiel** (Kontrollwerte aus K27):

> <span class="m" data-tex="f(x)=x^{2}\sqrt{2x+1}" data-plain="f(x) = x² · √(2x + 1)"></span> mit
> <span class="m" data-tex="D = \left[-\tfrac12;\,\infty\right[" data-plain="D = [−0,5; ∞["></span>.
> Äußerste Operation ist die Multiplikation, also Produktregel mit
> <span class="m" data-tex="u=x^{2}" data-plain="u = x²"></span> und
> <span class="m" data-tex="v=\sqrt{2x+1}" data-plain="v = √(2x + 1)"></span>. Für
> <span class="m" data-tex="v'" data-plain="v′"></span> brauchst du die Kettenregel:
> <span class="m" data-tex="v'(x) = \frac{1}{2\sqrt{2x+1}}\cdot 2 = \frac{1}{\sqrt{2x+1}}" data-plain="v′(x) = 1/(2·√(2x+1)) · 2 = 1/√(2x + 1)"></span>.
>
> <span class="m block" data-tex="f'(x) = 2x\sqrt{2x+1} + x^{2}\cdot\frac{1}{\sqrt{2x+1}} = \frac{2x(2x+1) + x^{2}}{\sqrt{2x+1}} = \frac{5x^{2}+2x}{\sqrt{2x+1}} = \frac{x(5x+2)}{\sqrt{2x+1}}" data-plain="f′(x) = 2x·√(2x+1) + x²/√(2x+1) = [2x(2x+1) + x²]/√(2x+1) = (5x² + 2x)/√(2x+1) = x(5x+2)/√(2x+1)"></span>
>
> Stichprobe an der Stelle <span class="m" data-tex="x=4" data-plain="x = 4"></span>:
> <span class="m" data-tex="f(4)=16\cdot 3=48" data-plain="f(4) = 16 · 3 = 48"></span> und
> <span class="m" data-tex="f'(4)=\frac{4\cdot 22}{3}=\frac{88}{3}\approx 29{,}33" data-plain="f′(4) = 4 · 22/3 = 88/3 ≈ 29,33"></span>.
> Die Tangente dort lautet
> <span class="m" data-tex="y=\tfrac{88}{3}x-\tfrac{208}{3}" data-plain="y = (88/3)·x − 208/3"></span>.

### 3.5 Mehrfache Verkettung und Ausblick

> Die Kettenregel lässt sich beliebig oft hintereinander anwenden — man arbeitet sich von außen
> nach innen durch und multipliziert alle Ableitungen auf. Beispiel
> <span class="m" data-tex="f(x)=\sqrt{(3x^{2}+1)^{3}} = (3x^{2}+1)^{3/2}" data-plain="f(x) = √((3x² + 1)³) = (3x² + 1)^(3/2)"></span>:
>
> <span class="m block" data-tex="f'(x) = \tfrac{3}{2}(3x^{2}+1)^{1/2}\cdot 6x = 9x\sqrt{3x^{2}+1}" data-plain="f′(x) = (3/2)·(3x² + 1)^(1/2) · 6x = 9x·√(3x² + 1)"></span>
>
> Stichproben: <span class="m" data-tex="f(1)=8" data-plain="f(1) = 8"></span>,
> <span class="m" data-tex="f'(1)=18" data-plain="f′(1) = 18"></span>,
> <span class="m" data-tex="f'(0)=0" data-plain="f′(0) = 0"></span>,
> <span class="m" data-tex="f'(2)=18\sqrt{13}\approx 64{,}90" data-plain="f′(2) = 18·√13 ≈ 64,90"></span>.

`.merksatz`:

> **Die drei Regeln auf einen Blick**
> Die drei Regeln sagen nicht dasselbe, aber sie hängen zusammen: Die Produktregel ist die
> grundlegende, die Kettenregel beschreibt Hintereinanderschaltung, und die Quotientenregel folgt
> aus beiden. Welche Regel du brauchst, entscheidest **nicht** durch Hinsehen auf einzelne Symbole,
> sondern durch die Frage: Welche Rechenoperation führe ich zuletzt aus?

`.hinweis`:

> **Was in den nächsten Einheiten dazukommt.** Alle drei Regeln sind vollkommen unabhängig davon,
> *welche* Funktionen <span class="m" data-tex="u" data-plain="u"></span> und
> <span class="m" data-tex="v" data-plain="v"></span> sind — sie gelten für jede differenzierbare
> Funktion. Sobald du die Ableitungen von
> <span class="m" data-tex="\sin" data-plain="sin"></span>,
> <span class="m" data-tex="\cos" data-plain="cos"></span> und der natürlichen Exponentialfunktion
> kennst, kannst du ohne eine einzige neue Regel Terme wie
> <span class="m" data-tex="x\,\mathrm{e}^{-2x}" data-plain="x · e⁻²ˣ"></span> oder
> <span class="m" data-tex="\dfrac{\sin x}{x}" data-plain="sin x / x"></span> ableiten. Genau
> deshalb steht dieses Modul am Anfang der Q1-Analysis.

## 4 · Interaktiver Kern

`<section id="simulation">`, `.stufe`-Kopf: Nr. **4**, Überschrift **Zwei Bilder: das Umsatzrechteck und der Ölring**.

Das Modul bekommt **zwei** Simulationen in derselben Sektion, jede in einer eigenen IIFE
(Vorbild: `cvSim`/`cvPhi`/`cvU` und `cvLenz` im Referenzmodul). Die erste macht die Produktregel
sichtbar, die zweite die Kettenregel. Die Quotientenregel bekommt bewusst **keine** eigene
Simulation — sie folgt aus den beiden anderen (Abschnitt 3.3), und das ist ein Argument, kein Bild.

---

### 4.A Simulation 1 — das Umsatzrechteck (Produktregel)

#### 4.A.1 Das Modell

Fließtext über der Simulation (wörtlich):

> Das Rechteck ist der Umsatz: Seine Breite ist die Besucherzahl, seine Höhe der Eintrittspreis,
> sein Flächeninhalt das Produkt aus beidem. Schiebst du die Zeit vorwärts, ändern sich beide
> Seiten gleichzeitig. Die drei eingefärbten Flächenstücke zeigen dir, woher die Änderung kommt.

Festgrößen und Funktionen (alle in der IIFE oben als Konstanten dokumentieren):

| Größe | Formel / Wert | Einheit |
|---|---|---|
| Grundpreis <span class="m" data-tex="p_0" data-plain="p₀"></span> | 5,00 (fest) | € |
| Grundbesucherzahl <span class="m" data-tex="n_0" data-plain="n₀"></span> | 400 (fest) | Personen |
| Preis | <span class="m" data-tex="p(t) = p_0 + b\,t" data-plain="p(t) = p₀ + b·t"></span> | € |
| Besucherzahl | <span class="m" data-tex="n(t) = n_0 + d\,t" data-plain="n(t) = n₀ + d·t"></span> | Personen |
| Umsatz | <span class="m" data-tex="U(t) = p(t)\cdot n(t)" data-plain="U(t) = p(t) · n(t)"></span> | € |
| Preisbeitrag | <span class="m" data-tex="p'(t)\,n(t) = b\cdot n(t)" data-plain="p′(t)·n(t) = b · n(t)"></span> | €/Tag |
| Mengenbeitrag | <span class="m" data-tex="p(t)\,n'(t) = p(t)\cdot d" data-plain="p(t)·n′(t) = p(t) · d"></span> | €/Tag |
| Ableitung | <span class="m" data-tex="U'(t) = b\,n(t) + p(t)\,d" data-plain="U′(t) = b·n(t) + p(t)·d"></span> | €/Tag |
| Sekantensteigung | <span class="m" data-tex="\frac{U(t+\Delta t)-U(t)}{\Delta t}" data-plain="[U(t+Δt) − U(t)]/Δt"></span> | €/Tag |
| Eckanteil | <span class="m" data-tex="\frac{\Delta p\cdot\Delta n}{\Delta t} = b\,d\,\Delta t" data-plain="(Δp · Δn)/Δt = b · d · Δt"></span> | €/Tag |
| Maximum | <span class="m" data-tex="t^{*} = -\dfrac{b\,n_0 + p_0\,d}{2\,b\,d}" data-plain="t* = −(b·n₀ + p₀·d)/(2·b·d)"></span> (nur falls <span class="m" data-tex="b\,d\neq 0" data-plain="b·d ≠ 0"></span>) | Tage |

Dabei ist <span class="m" data-tex="\Delta p = b\,\Delta t" data-plain="Δp = b · Δt"></span> und
<span class="m" data-tex="\Delta n = d\,\Delta t" data-plain="Δn = d · Δt"></span>.

**Die Identität, um die es geht** (sie muss in jedem Zustand auf drei Nachkommastellen aufgehen —
der Bauagent prüft das als Selbsttest):

`data-tex`: `\frac{\Delta U}{\Delta t} \;=\; \underbrace{p'\,n}_{\text{Preisbeitrag}} \;+\; \underbrace{p\,n'}_{\text{Mengenbeitrag}} \;+\; \underbrace{\frac{\Delta p\,\Delta n}{\Delta t}}_{\text{Eckanteil}}`
`data-plain`: `ΔU/Δt = p′·n (Preisbeitrag) + p·n′ (Mengenbeitrag) + (Δp·Δn)/Δt (Eckanteil)`

#### 4.A.2 Regler (`.regler`)

| ID | Größe | Sliderbereich (`min`/`max`/`step`) | Umrechnung | Startwert |
|---|---|---|---|---|
| `rT` | Zeit <span class="m" data-tex="t" data-plain="t"></span> | 0 … 210, Schritt 1 | <span class="m" data-tex="t = \text{Wert}/10" data-plain="t = Wert/10"></span> → 0 … 21,0 Tage | **0** (0,0 Tage) |
| `rDt` | Zeitschritt <span class="m" data-tex="\Delta t" data-plain="Δt"></span> | 1 … 16, Schritt 1 | <span class="m" data-tex="\Delta t = \text{Wert}\cdot 0{,}25" data-plain="Δt = Wert · 0,25"></span> → 0,25 … 4,00 Tage | **4** (1,00 Tage) |
| `rB` | Preisänderung <span class="m" data-tex="b" data-plain="b"></span> | −15 … 30, Schritt 1 | <span class="m" data-tex="b = \text{Wert}/100" data-plain="b = Wert/100"></span> → −0,15 … +0,30 €/Tag | **10** (0,10 €/Tag) |
| `rD` | Besucheränderung <span class="m" data-tex="d" data-plain="d"></span> | −12 … 8, Schritt 1 | direkt, Personen pro Tag | **−6** |

Die Grenzen sind so gewählt, dass **alle** dargestellten Größen im Achsenbereich bleiben
(Nachweis in K15): Der größte auftretende Preis ist 12,50 € (Achse bis 14 €), die größte
Besucherzahl 600 (Achse bis 600), und wegen
<span class="m" data-tex="t \le 21" data-plain="t ≤ 21"></span> und
<span class="m" data-tex="\Delta t \le 4" data-plain="Δt ≤ 4"></span> gilt immer
<span class="m" data-tex="t+\Delta t \le 25" data-plain="t + Δt ≤ 25"></span>. Dadurch bleibt
<span class="m" data-tex="n(t+\Delta t)\ge 100" data-plain="n(t+Δt) ≥ 100"></span> und
<span class="m" data-tex="p(t+\Delta t)\ge 1{,}25\ \text{€}" data-plain="p(t+Δt) ≥ 1,25 €"></span> —
es gibt keine negativen Seitenlängen.

#### 4.A.3 Knöpfe (`.knopfleiste`)

| ID | Beschriftung | Wirkung |
|---|---|---|
| `bPlay` | ▶ Start / ⏸ Pause | Animation: <span class="m" data-tex="t" data-plain="t"></span> läuft mit **2,0 Tagen pro Sekunde** bis 21,0 und hält dort an. `requestAnimationFrame` mit `dtFrame = Math.min(0.05, (jetzt − vorher)/1000)`. |
| `bMax` | Zum Umsatzmaximum | Setzt <span class="m" data-tex="t" data-plain="t"></span> auf <span class="m" data-tex="t^{*}" data-plain="t*"></span>, gerundet auf 0,1 Tage, falls <span class="m" data-tex="0\le t^{*}\le 21" data-plain="0 ≤ t* ≤ 21"></span>. Sonst Textmeldung „In diesem Zeitraum gibt es kein Maximum — der Umsatz ist durchgehend monoton." |
| `bReset` | Zurücksetzen | alle vier Regler auf die Startwerte, Animation stoppen |

#### 4.A.4 Canvas 1 `cvRecht` — das Umsatzrechteck

`<canvas id="cvRecht" width="1000" height="440">`, CSS `width:100%`.

**Feste Umrechnung Pixel ↔ Sachgröße (oben in der IIFE als Konstante dokumentieren):**

```
OX = 90     // Ursprung waagerecht (Pixel)
OY = 390    // Ursprung senkrecht (Pixel)
SX = 1.4    // Pixel pro Besucher     -> 600 Besucher = 840 px, rechter Rand bei x = 930
SY = 24     // Pixel pro Euro         ->     14 Euro   = 336 px, oberer Rand bei y = 54
px(n) = OX + SX * n
py(p) = OY - SY * p
```

Kontrollwerte: <span class="m" data-tex="n = 400 \to x = 650" data-plain="n = 400 → x = 650"></span> ·
<span class="m" data-tex="p = 5{,}00 \to y = 270" data-plain="p = 5,00 → y = 270"></span> ·
<span class="m" data-tex="n = 600 \to x = 930" data-plain="n = 600 → x = 930"></span> ·
<span class="m" data-tex="p = 14 \to y = 54" data-plain="p = 14 → y = 54"></span>.

**Zeichenreihenfolge (wichtig, die letzten beiden Schritte überlagern sich):**

1. Achsen mit Beschriftung: waagerecht „Besucherzahl n", Teilstriche alle 100; senkrecht
   „Preis p in €", Teilstriche alle 2 €.
2. **Grundrechteck** von <span class="m" data-tex="(OX, OY)" data-plain="(OX, OY)"></span> bis
   <span class="m" data-tex="(px(n), py(p))" data-plain="(px(n), py(p))"></span> in
   `--akzent-hell` mit Rand `--akzent`. Beschriftung in der Mitte: `U = p · n = …  €`.
3. **Mengenbeitrag** <span class="m" data-tex="p\cdot\Delta n" data-plain="p · Δn"></span>:
   Rechteck zwischen <span class="m" data-tex="px(n)" data-plain="px(n)"></span> und
   <span class="m" data-tex="px(n+\Delta n)" data-plain="px(n+Δn)"></span>, senkrecht von
   <span class="m" data-tex="OY" data-plain="OY"></span> bis
   <span class="m" data-tex="py(p)" data-plain="py(p)"></span>.
   Farbe **grün** `#0d7a52` bei <span class="m" data-tex="\Delta n > 0" data-plain="Δn > 0"></span>,
   **rot** `#b91c1c` bei <span class="m" data-tex="\Delta n < 0" data-plain="Δn < 0"></span>, je 35 % deckend.
4. **Preisbeitrag** <span class="m" data-tex="n\cdot\Delta p" data-plain="n · Δp"></span>:
   Rechteck zwischen <span class="m" data-tex="OX" data-plain="OX"></span> und
   <span class="m" data-tex="px(n)" data-plain="px(n)"></span>, senkrecht von
   <span class="m" data-tex="py(p)" data-plain="py(p)"></span> bis
   <span class="m" data-tex="py(p+\Delta p)" data-plain="py(p+Δp)"></span>.
   Farbregel wie oben, nach dem Vorzeichen von <span class="m" data-tex="\Delta p" data-plain="Δp"></span>.
5. **Eckstück** <span class="m" data-tex="\Delta p\cdot\Delta n" data-plain="Δp · Δn"></span>:
   Rechteck zwischen <span class="m" data-tex="px(n)" data-plain="px(n)"></span> und
   <span class="m" data-tex="px(n+\Delta n)" data-plain="px(n+Δn)"></span> sowie zwischen
   <span class="m" data-tex="py(p)" data-plain="py(p)"></span> und
   <span class="m" data-tex="py(p+\Delta p)" data-plain="py(p+Δp)"></span>, **diagonal schraffiert**
   (Linien im 45°-Abstand von 6 px) in `#b45309`, mit voll deckendem Rand.

**Warum die Reihenfolge zählt.** Mit den Startwerten ist
<span class="m" data-tex="\Delta n < 0" data-plain="Δn < 0"></span> und
<span class="m" data-tex="\Delta p > 0" data-plain="Δp > 0"></span>. Dann liegt das Eckstück
**innerhalb** des Preisstreifens: Der Preisstreifen wurde über die volle alte Breite
<span class="m" data-tex="n" data-plain="n"></span> gezeichnet, obwohl das Rechteck nur noch
<span class="m" data-tex="n+\Delta n" data-plain="n+Δn"></span> breit ist. Das schraffierte Eckstück
ist genau diese Korrektur — es wird **abgezogen**. Deshalb muss es zuletzt und über den
Preisstreifen gezeichnet werden. Genau daran lässt sich im Unterricht zeigen, dass die drei
Summanden in der Produktregel keine willkürliche Zerlegung sind.

Rechts oben eine kleine Legende mit drei Farbkästchen und den aktuellen Zahlenwerten der drei
Flächenstücke (nicht der Raten): <span class="m" data-tex="p\,\Delta n" data-plain="p·Δn"></span>,
<span class="m" data-tex="n\,\Delta p" data-plain="n·Δp"></span>,
<span class="m" data-tex="\Delta p\,\Delta n" data-plain="Δp·Δn"></span> in €.
Startwerte: −30,00 € · +40,00 € · −0,60 €; Summe −30,00 + 40,00 − 0,60 = **+9,40 €** = ΔU ✓ (K12).

#### 4.A.5 Canvas 2 `cvU` — Umsatz über der Zeit

`<canvas id="cvU" width="1000" height="280">`, darüber ein `.trenner` wie im Referenzmodul.

**Waagerechte Achse fest, senkrechte Achse mitskalierend** (die Ausschläge sind bei manchen
Reglerstellungen klein gegenüber dem Niveau — eine feste Achse würde die Kurve platt drücken):

```
AX0 = 90, AX1 = 950          // t = 0 bis t = 25 Tage  -> 34,4 px pro Tag
AY0 = 250 (unten), AY1 = 50  // 200 px Hoehe
Umin, Umax = kleinster/groesster Wert von U(t) auf [0; 25]
   (Randwerte U(0), U(25) und, falls 0 <= t* <= 25, zusaetzlich U(t*))
spanne = Umax - Umin;  falls spanne < 1 : spanne = 1
Uunten = Umin - 0.1*spanne;  Uoben = Umax + 0.1*spanne
pxT(t) = AX0 + (AX1-AX0) * t/25
pyU(U) = AY0 - (AY0-AY1) * (U - Uunten)/(Uoben - Uunten)
```

Gezeichnet wird:

1. die **vollständige** Kurve <span class="m" data-tex="U(t)" data-plain="U(t)"></span> auf
   <span class="m" data-tex="[0;25]" data-plain="[0; 25]"></span> blass (`--akzent` bei 25 % Deckung),
2. der bereits durchlaufene Teil <span class="m" data-tex="[0;t]" data-plain="[0; t]"></span> kräftig
   (2,5 px) — beim Abspielen **baut sich die Kurve mit auf**,
3. der Punkt <span class="m" data-tex="(t, U(t))" data-plain="(t, U(t))"></span> als gefüllter Kreis (5 px),
4. die **Sekante** durch <span class="m" data-tex="(t,U(t))" data-plain="(t, U(t))"></span> und
   <span class="m" data-tex="(t+\Delta t, U(t+\Delta t))" data-plain="(t+Δt, U(t+Δt))"></span>, gestrichelt in `#b45309`,
   mit einem zweiten kleinen Kreis am rechten Ende,
5. die **Tangente** mit Steigung <span class="m" data-tex="U'(t)" data-plain="U′(t)"></span>, durchgezogen in `#0d7a52`,
   gezeichnet über <span class="m" data-tex="\pm 3" data-plain="±3"></span> Tage um <span class="m" data-tex="t" data-plain="t"></span>,
6. falls <span class="m" data-tex="0\le t^{*}\le 25" data-plain="0 ≤ t* ≤ 25"></span>: eine graue
   senkrechte Hilfslinie bei <span class="m" data-tex="t^{*}" data-plain="t*"></span> mit der
   Beschriftung `Maximum`,
7. Achsenbeschriftung „t in Tagen" und „U in €", senkrecht drei Marken:
   <span class="m" data-tex="U_{\text{unten}}" data-plain="U_unten"></span>, Mitte,
   <span class="m" data-tex="U_{\text{oben}}" data-plain="U_oben"></span>.

**Der didaktische Kern dieses Diagramms:** Die gestrichelte Sekante und die durchgezogene Tangente
fallen umso besser zusammen, je kleiner <span class="m" data-tex="\Delta t" data-plain="Δt"></span>
ist — und der Abstand zwischen beiden Steigungen ist *exakt* der Eckanteil (K13).

#### 4.A.6 Anzeigefelder (`.anzeige`, alle über `fmt(zahl, stellen)` mit Komma)

| ID | Größe | Stellen | Startwert |
|---|---|---|---|
| `anzT` | Zeit <span class="m" data-tex="t" data-plain="t"></span> | 1 | 0,0 Tage |
| `anzP` | Preis <span class="m" data-tex="p(t)" data-plain="p(t)"></span> | 2 | 5,00 € |
| `anzN` | Besucherzahl <span class="m" data-tex="n(t)" data-plain="n(t)"></span> | 1 | 400,0 |
| `anzU` | Umsatz <span class="m" data-tex="U(t)" data-plain="U(t)"></span> | 2 | 2000,00 € |
| `anzBp` | Preisbeitrag <span class="m" data-tex="p'\,n" data-plain="p′·n"></span> | 2 | 40,00 €/Tag |
| `anzBn` | Mengenbeitrag <span class="m" data-tex="p\,n'" data-plain="p·n′"></span> | 2 | −30,00 €/Tag |
| `anzUs` | Ableitung <span class="m" data-tex="U'(t)" data-plain="U′(t)"></span> | 2 | 10,00 €/Tag |
| `anzSek` | Sekantensteigung | 2 | 9,40 €/Tag |
| `anzEck` | Eckanteil | 2 | −0,60 €/Tag |

Zweiter Testfall zum Abgleich beim Bauen (K14): <span class="m" data-tex="t = 12{,}0" data-plain="t = 12,0"></span>,
<span class="m" data-tex="\Delta t = 0{,}5" data-plain="Δt = 0,5"></span> ergibt
6,20 € · 328,0 · 2033,60 € · 32,80 · −37,20 · **−4,40** · −4,70 · −0,30.

#### 4.A.7 Beobachtungsauftrag (wörtlich in den `.auftrag`-Kasten)

> **Beobachtungsauftrag**
> Setze die Regler zurück (<span class="m" data-tex="b = 0{,}10" data-plain="b = 0,10"></span> €/Tag,
> <span class="m" data-tex="d = -6" data-plain="d = −6"></span>, <span class="m" data-tex="t = 0" data-plain="t = 0"></span>).
> **(1)** Notiere für <span class="m" data-tex="\Delta t = 4{,}00" data-plain="Δt = 4,00"></span>;
> 2,00; 1,00; 0,50 und 0,25 Tage jeweils die Sekantensteigung und den Eckanteil. Welche Zahl
> ändert sich dabei **nicht**, und wie verhält sich der Abstand der Sekantensteigung zu dieser Zahl?
> **(2)** Halbiere <span class="m" data-tex="\Delta t" data-plain="Δt"></span> noch einmal und sage
> vorher, welchen Eckanteil du erwartest, bevor du liest.
> **(3)** Drücke „Zum Umsatzmaximum" und vergleiche dort Preisbeitrag und Mengenbeitrag.
> Schreibe zum Schluss **einen** Satz auf, der erklärt, warum die Sekantensteigung immer genau um
> den Eckanteil von der Ableitung abweicht.

Erwartete Notizen (für die Lehrkraft, in den Lehrerteil, nicht auf die Schülerseite):

| Δt | Sekante | Eckanteil | Abstand zu U′ = 10,00 |
|---|---|---|---|
| 4,00 | 7,60 | −2,40 | 2,40 |
| 2,00 | 8,80 | −1,20 | 1,20 |
| 1,00 | 9,40 | −0,60 | 0,60 |
| 0,50 | 9,70 | −0,30 | 0,30 |
| 0,25 | 9,85 | −0,15 | 0,15 |

Unverändert bleibt <span class="m" data-tex="U'(0) = 10{,}00" data-plain="U′(0) = 10,00"></span> €/Tag.
Am Maximum (<span class="m" data-tex="t^{*}=8{,}3" data-plain="t* = 8,3"></span> Tage) stehen
+35,00 €/Tag gegen −35,00 €/Tag.

#### 4.A.8 Verständnisfragen zur Simulation 1

---

**MC `sim1`** — Anforderungsbereich **II** — richtige Option: Index **1**

Frage: *Stelle ein: <span class="m" data-tex="b = 0{,}20" data-plain="b = 0,20"></span> €/Tag, <span class="m" data-tex="d = -8" data-plain="d = −8"></span> Personen/Tag, <span class="m" data-tex="t = 6{,}0" data-plain="t = 6,0"></span> Tage und <span class="m" data-tex="\Delta t = 2{,}00" data-plain="Δt = 2,00"></span> Tage. Welche Sekantensteigung <span class="m" data-tex="\Delta U/\Delta t" data-plain="ΔU/Δt"></span> zeigt die Anzeige?*

| Index | Option |
|---|---|
| 0 | 20,80 €/Tag |
| 1 | 17,60 €/Tag |
| 2 | 24,00 €/Tag |
| 3 | 70,40 €/Tag |

Feedback:
- 0: „20,80 €/Tag ist die Ableitung U′(t), die Steigung der Tangente – sie steht in der Anzeige „Ableitung U′(t)“. Die Sekante läuft von t = 6 bis t = 8 und liegt wegen des Eckanteils b·d·Δt = 0,20 · (−8) · 2 = −3,20 um genau diesen Betrag darunter.“
- 1: „Richtig. U(6) = 6,20 · 352 = 2182,40 €, U(8) = 6,60 · 336 = 2217,60 €, Differenz 35,20 € in 2 Tagen, also 17,60 €/Tag. Kontrolle über die Produktregel: U′ + Eckanteil = 20,80 + (−3,20) = 17,60.“
- 2: „Das Vorzeichen des Eckanteils ist vertauscht: Er beträgt b·d·Δt = 0,20 · (−8) · 2 = −3,20, weil d negativ ist. Zur Ableitung 20,80 kommt also −3,20 hinzu, nicht +3,20 (das wären die 24,00). Lies Ableitung und Eckanteil in der Anzeige ab und verknüpfe sie.“
- 3: „70,40 €/Tag ist nur der Preisbeitrag p′·n = 0,20 · 352. Der Mengenbeitrag p·n′ = 6,20 · (−8) = −49,60 €/Tag fehlt, dazu der Eckanteil. Beide Seiten des Rechtecks ändern sich gleichzeitig.“

---

**MC `sim2`** — Anforderungsbereich **II** — richtige Option: Index **2**

Frage: *Setze die Regler zurück und stelle dann nur die Besucheränderung auf <span class="m" data-tex="d = -7" data-plain="d = −7"></span> Personen/Tag (<span class="m" data-tex="b = 0{,}10" data-plain="b = 0,10"></span> €/Tag bleibt). Drücke „Zum Umsatzmaximum". Welche Zeit und welchen Umsatz zeigt die Anzeige?*

| Index | Option |
|---|---|
| 0 | t = 8,33 Tage, U = 1993,06 € |
| 1 | t = 7,14 Tage, U = 2000,00 € |
| 2 | t = 3,57 Tage, U = 2008,93 € |
| 3 | t = 0,00 Tage, U = 2000,00 € |

Feedback:
- 0: „8,33 Tage ist das Maximum für d = −6 aus dem Text, also der alte Wert. Die Lage von t* hängt aber von d ab: t* = −(b·400 + 5·d)/(2·b·d). Bei d = −7 liegt es früher; bei t = 8,33 ist der Umsatz mit 1993,06 € sogar kleiner als am Start.“
- 1: „Hier fehlt der Faktor 2 im Nenner: 7,14 ≈ 5/0,7 ist die Stelle, an der der Umsatz wieder auf den Startwert 2000,00 € zurückgefallen ist. Das Maximum liegt in der Mitte zwischen t = 0 und dieser Stelle, nämlich bei der Hälfte, t = 25/7 ≈ 3,57 Tage. Das folgt aus U′(t) = 5 − 1,4·t.“
- 2: „Richtig. U′(t) = 0,10 · (400 − 7t) + (5 + 0,10t) · (−7) = 5 − 1,4t, also t* = 25/7 ≈ 3,57 Tage. Dort ist p = 5,36 €, n = 375 und U = 2008,93 € – etwas mehr als die 2000,00 € am Start.“
- 3: „Das Maximum am Start gilt für d = −8: Dort ist U′(0) = 40 − 40 = 0. Bei d = −7 ist U′(0) = 0,10 · 400 + 5 · (−7) = +5 €/Tag, der Umsatz steigt also zunächst noch, das Maximum liegt später.“

---

### 4.B Simulation 2 — der Ölring (Kettenregel)

#### 4.B.1 Das Modell

Fließtext über der Simulation:

> Aus einem Leck breitet sich ein kreisrunder Ölteppich aus. Der Radius wächst gleichmäßig, die
> Fläche nicht — und genau darum geht es. Die Fläche hängt vom Radius ab, der Radius von der Zeit.
> Das ist eine Kette aus zwei Abhängigkeiten, und ihre Raten multiplizieren sich.

| Größe | Formel | Einheit |
|---|---|---|
| Radius | <span class="m" data-tex="r(t) = r_0 + c\,t" data-plain="r(t) = r₀ + c·t"></span> | m |
| Fläche | <span class="m" data-tex="A(r) = \pi r^{2}" data-plain="A(r) = π·r²"></span> | m² |
| innere Rate | <span class="m" data-tex="\frac{\mathrm{d}r}{\mathrm{d}t} = c" data-plain="dr/dt = c"></span> | m/s |
| äußere Rate | <span class="m" data-tex="\frac{\mathrm{d}A}{\mathrm{d}r} = 2\pi r" data-plain="dA/dr = 2π·r"></span> | m |
| Kettenregel | <span class="m" data-tex="\frac{\mathrm{d}A}{\mathrm{d}t} = \frac{\mathrm{d}A}{\mathrm{d}r}\cdot\frac{\mathrm{d}r}{\mathrm{d}t} = 2\pi r\,c" data-plain="dA/dt = dA/dr · dr/dt = 2π·r·c"></span> | m²/s |
| Ringbreite | <span class="m" data-tex="\Delta r = c\,\Delta t" data-plain="Δr = c · Δt"></span> | m |
| Ring exakt | <span class="m" data-tex="\pi\big((r+\Delta r)^{2}-r^{2}\big)" data-plain="π·((r+Δr)² − r²)"></span> | m² |
| Ring genähert | <span class="m" data-tex="2\pi r\cdot\Delta r" data-plain="2π·r · Δr"></span> | m² |
| Fehler | <span class="m" data-tex="\pi\,\Delta r^{2}" data-plain="π·Δr²"></span> | m² |

Der Zusammenhang, der hier sichtbar werden soll: **Die äußere Ableitung
<span class="m" data-tex="2\pi r" data-plain="2πr"></span> ist der Umfang des Kreises.** Ein Ring
der Breite <span class="m" data-tex="\Delta r" data-plain="Δr"></span> hat näherungsweise die
Fläche „Umfang mal Breite" — und der Fehler dabei ist
<span class="m" data-tex="\pi\Delta r^{2}" data-plain="π·Δr²"></span>, also wieder ein Term zweiter
Ordnung, wie das Eckstück in Simulation 1.

#### 4.B.2 Regler

| ID | Größe | Sliderbereich | Umrechnung | Startwert |
|---|---|---|---|---|
| `rR0` | Anfangsradius <span class="m" data-tex="r_0" data-plain="r₀"></span> | 2 … 20, Schritt 1 | direkt, m | **5** |
| `rC` | Ausbreitungsgeschwindigkeit <span class="m" data-tex="c" data-plain="c"></span> | 1 … 20, Schritt 1 | <span class="m" data-tex="c=\text{Wert}/10" data-plain="c = Wert/10"></span> → 0,1 … 2,0 m/s | **5** (0,5 m/s) |
| `rTk` | Zeit <span class="m" data-tex="t" data-plain="t"></span> | 0 … 100, Schritt 1 | <span class="m" data-tex="t=\text{Wert}/2" data-plain="t = Wert/2"></span> → 0 … 50 s | **40** (20,0 s) |
| `rDtk` | Zeitschritt <span class="m" data-tex="\Delta t" data-plain="Δt"></span> | 1 … 8, Schritt 1 | <span class="m" data-tex="\Delta t=\text{Wert}\cdot 0{,}25" data-plain="Δt = Wert · 0,25"></span> → 0,25 … 2,00 s | **4** (1,00 s) |

Größter auftretender Radius: <span class="m" data-tex="20 + 2{,}0\cdot 50 = 120" data-plain="20 + 2,0 · 50 = 120"></span> m (K17) — deshalb der Maßstab **1 m = 1 px**.
Keine Animation, kein `requestAnimationFrame`: Neu gezeichnet wird ausschließlich im
`input`-Ereignis der vier Regler und beim Klick auf `bResetK` (setzt alle vier auf die Startwerte).

#### 4.B.3 Canvas `cvKette`

`<canvas id="cvKette" width="1000" height="340">`, CSS `width:100%`.

**Linke Hälfte — der Teppich (Maßstab 1 m = 1 px):**

```
MX = 240, MY = 170     // Kreismittelpunkt in Pixeln
Radius in Pixeln = r   // 1 m = 1 px, groesster Wert 120 px
```

1. gefüllter Kreis mit Radius <span class="m" data-tex="r" data-plain="r"></span> in `--akzent-hell`, Rand `--akzent`,
2. **Ring** zwischen <span class="m" data-tex="r" data-plain="r"></span> und
   <span class="m" data-tex="r+\Delta r" data-plain="r+Δr"></span> in `#b45309` bei 45 % Deckung.
   Weil <span class="m" data-tex="\Delta r" data-plain="Δr"></span> bis auf 0,025 m heruntergehen
   kann, wird der Ring **mit einer Mindeststrichstärke von 2 px** gezeichnet; dass er in
   Wirklichkeit dünner ist, steht als Bildunterschrift dabei: „Ringbreite zur Sichtbarkeit
   mindestens 2 px dargestellt".
3. Maßpfeil vom Mittelpunkt nach rechts mit Beschriftung `r = … m`,
4. Bildunterschrift `A = π r² = … m²`.

**Rechte Hälfte — der Vergleich (Balken, gemeinsame Skala):**

```
BX = 480          // linke Kante der Balken
BW = 460          // volle Balkenlaenge entspricht dem groesseren der beiden Werte
Skala = BW / max(Ring_exakt, Ring_naeherung)
```

Drei waagerechte Balken, je 34 px hoch, mit 26 px Abstand, beschriftet:

| Balken | Wert | Farbe |
|---|---|---|
| „Ringfläche exakt: <span class="m" data-tex="\pi((r+\Delta r)^{2}-r^{2})" data-plain="π((r+Δr)² − r²)"></span>" | 47,90929 m² (Start) | `#b45309` |
| „Näherung: Umfang <span class="m" data-tex="\cdot" data-plain="·"></span> Ringbreite <span class="m" data-tex="= 2\pi r\,\Delta r" data-plain="= 2πr·Δr"></span>" | 47,12389 m² (Start) | `--akzent` |
| „Differenz <span class="m" data-tex="\pi\,\Delta r^{2}" data-plain="π·Δr²"></span>" | 0,78540 m² (Start) | `#64748b` |

Der dritte Balken wird mit **derselben** Skala gezeichnet — er ist am Anfang nur 8 px lang, und
genau das ist die Aussage.

#### 4.B.4 Anzeigefelder (`.anzeige`)

| ID | Größe | Stellen | Startwert |
|---|---|---|---|
| `anzR` | Radius <span class="m" data-tex="r(t)" data-plain="r(t)"></span> | 3 | 15,000 m |
| `anzA` | Fläche <span class="m" data-tex="A" data-plain="A"></span> | 3 | 706,858 m² |
| `anzDAdr` | äußere Rate <span class="m" data-tex="\mathrm{d}A/\mathrm{d}r = 2\pi r" data-plain="dA/dr = 2πr"></span> | 4 | 94,2478 m |
| `anzDrdt` | innere Rate <span class="m" data-tex="\mathrm{d}r/\mathrm{d}t = c" data-plain="dr/dt = c"></span> | 2 | 0,50 m/s |
| `anzDAdt` | Produkt <span class="m" data-tex="\mathrm{d}A/\mathrm{d}t" data-plain="dA/dt"></span> | 4 | 47,1239 m²/s |
| `anzRingEx` | Ring exakt | 5 | 47,90929 m² |
| `anzRingNa` | Ring genähert | 5 | 47,12389 m² |
| `anzFehler` | Differenz (absolut und relativ) | 5 / 3 | 0,78540 m² (1,639 %) |

Weitere Prüfstellungen beim Bauen (K17): <span class="m" data-tex="r_0=10" data-plain="r₀ = 10"></span>,
<span class="m" data-tex="c=1{,}2" data-plain="c = 1,2"></span>,
<span class="m" data-tex="t=30" data-plain="t = 30"></span>,
<span class="m" data-tex="\Delta t=0{,}5" data-plain="Δt = 0,5"></span> →
46,000 m · 6647,610 m² · 289,0265 m · 346,8318 m²/s · Differenz 1,13097 m².

#### 4.B.5 Beobachtungsauftrag (zweiter `.auftrag`-Kasten)

> **Beobachtungsauftrag**
> Startwerte lassen (<span class="m" data-tex="r_0=5" data-plain="r₀ = 5"></span> m,
> <span class="m" data-tex="c=0{,}5" data-plain="c = 0,5"></span> m/s,
> <span class="m" data-tex="t=20" data-plain="t = 20"></span> s). Vergleiche die exakte Ringfläche
> mit der Näherung „Umfang mal Ringbreite" für
> <span class="m" data-tex="\Delta t = 2{,}00" data-plain="Δt = 2,00"></span>; 1,00; 0,50 und 0,25 s.
> Notiere jedes Mal die absolute **und** die relative Differenz. Verdopple anschließend
> <span class="m" data-tex="t" data-plain="t"></span> auf 40 s und prüfe, ob sich die Fläche
> ebenfalls verdoppelt — und ob sich die Rate
> <span class="m" data-tex="\mathrm{d}A/\mathrm{d}t" data-plain="dA/dt"></span> verdoppelt.
> Formuliere zum Schluss einen Satz darüber, was der Umfang mit der Ableitung der Kreisfläche zu tun hat.

Erwartete Notizen (Lehrerteil): Tabelle aus K17; bei
<span class="m" data-tex="t=40" data-plain="t = 40"></span> s ist
<span class="m" data-tex="r = 25" data-plain="r = 25"></span> m,
<span class="m" data-tex="A = 1963{,}50" data-plain="A = 1963,50"></span> m² (also **nicht** das
Doppelte von 706,858, sondern das 2,78-fache), während
<span class="m" data-tex="\mathrm{d}A/\mathrm{d}t = 78{,}5398" data-plain="dA/dt = 78,5398"></span> m²/s
genau das <span class="m" data-tex="25/15" data-plain="25/15"></span>-fache von 47,1239 ist — die
Rate wächst linear mit <span class="m" data-tex="r" data-plain="r"></span>, die Fläche quadratisch.

#### 4.B.6 Verständnisfrage zur Simulation 2

---

**MC `sim3`** — Anforderungsbereich **II** — richtige Option: Index **0**

Frage: *Stelle die Regler in dieser Reihenfolge ein: r₀ = 8 m, c = 1,2 m/s, t = 15 s, Δt = 1,50 s. Welchen Wert zeigt die Anzeige „Ring exakt“?*

| Index | Option |
|---|---|
| 0 | 304,23 m² |
| 1 | 294,05 m² |
| 2 | 252,11 m² |
| 3 | 100,66 m² |

Feedback:
- 0: „Richtig. Radius r = 8 + 1,2 · 15 = 26 m, Ringbreite Δr = 1,2 · 1,5 = 1,8 m. Exakt: π · (27,8² − 26²) = π · 96,84 ≈ 304,23 m². Die Näherung 2π · 26 · 1,8 ≈ 294,05 m² liegt darunter; die Differenz π · Δr² ≈ 10,18 m² ist der Term zweiter Ordnung."
- 1: „294,05 m² ist die Näherung „Umfang mal Ringbreite“ (2π · 26 · 1,8), nicht die exakte Ringfläche. Die exakte Fläche ist um den Fehlerterm π · Δr² = 10,18 m² größer, also 304,23 m². Beide Werte stehen in der Anzeige direkt untereinander."
- 2: „Hier wurde Δr = Δt = 1,5 m gesetzt: π · (27,5² − 26²) ≈ 252,11 m². Die Ringbreite ist aber der Weg, den der Rand in der Zeit Δt zurücklegt, also Δr = c · Δt = 1,2 · 1,5 = 1,8 m. Die Geschwindigkeit c fehlt."
- 3: „100,66 m² ergibt sich, wenn der Ring am Anfangsradius r₀ = 8 m statt am Radius zum Zeitpunkt t berechnet wird: π · (9,8² − 8²). Zum Zeitpunkt t = 15 s ist der Teppich aber schon auf r = 8 + 1,2 · 15 = 26 m angewachsen, und der Ring liegt weiter außen."

`.hinweis` nach den Simulationen:

> **Was die Simulationen zeigen — und was nicht.** Beide Bilder machen plausibel, warum in der
> Produktregel zwei Summanden und in der Kettenregel ein Produkt steht, und warum die jeweils
> übrigbleibenden Terme im Grenzwert verschwinden. Ein **Beweis** sind sie nicht: Dass ein Term
> bei fünf getesteten Werten von <span class="m" data-tex="\Delta t" data-plain="Δt"></span>
> kleiner wird, zeigt nicht, dass er gegen null geht. Den Nachweis liefern die Herleitungen in den
> Details-Blöcken der Abschnitte 2 und 3.

## 5 · Übungen

`<section id="uebungen">`, `.stufe`-Kopf: Nr. **5**, Überschrift **Übungen**.

Zehn Aufgaben: zwei im Anforderungsbereich I, fünf im Anforderungsbereich II, drei im
Anforderungsbereich III. Jede Aufgabe trägt einen `.ab`-Chip mit dem Anforderungsbereich.

---

### Aufgabe 1 — `a1` · Zahleneingabe · Anforderungsbereich I

Aufgabentext (wörtlich):

> Ein rechteckiges Solarfeld wird jedes Jahr erweitert. Seine Länge wächst nach
> <span class="m" data-tex="l(t) = 40 + 3t" data-plain="l(t) = 40 + 3 t"></span> (in Metern), seine
> Breite nach <span class="m" data-tex="b(t) = 25 + 2t" data-plain="b(t) = 25 + 2 t"></span>
> (in Metern); <span class="m" data-tex="t" data-plain="t"></span> zählt die Jahre seit der
> Inbetriebnahme. Berechne mit der Produktregel, wie schnell der Flächeninhalt zum Zeitpunkt
> <span class="m" data-tex="t = 0" data-plain="t = 0"></span> wächst.

**Einheitenliste im `<select>`:** `m²/Jahr` · `m/Jahr` · `m²` · `m²·Jahr`
(die letzten drei sind Distraktoren: eine Länge pro Zeit, eine Fläche ohne Zeitbezug und eine
Fläche mal Zeit).

**Eintrag in `numDaten`:**

```js
a1:{ wert:155, einheit:"m²/Jahr", tol:0.5,
     ok:"Richtig. A′(t) = l′(t)·b(t) + l(t)·b′(t) = 3·(25+2t) + (40+3t)·2, also A′(0) = 3·25 + 40·2 = 75 + 80 = 155 m² pro Jahr.",
     falschEinheit:"Der Zahlenwert stimmt. Gesucht ist aber eine Änderungsrate einer Fläche, also Quadratmeter pro Jahr — m² allein wäre ein Flächeninhalt, m/Jahr die Wachstumsrate einer einzelnen Seite.",
     nah:"Du hast vermutlich nur einen der beiden Summanden gerechnet: 3·25 = 75 (die Verlängerung entlang der Breite) oder 40·2 = 80 (die Verbreiterung entlang der Länge). Beide Streifen entstehen gleichzeitig, beide zählen.",
     weit:"6 m²/Jahr wäre das Produkt der beiden Ableitungen 3·2 — das ist nur das kleine Eckquadrat, das in einem Jahr hinzukommt, und damit der kleinste der drei Beiträge. Rechne die beiden großen Streifen zuerst: 3 m mehr Länge über 25 m Breite und 2 m mehr Breite über 40 m Länge." }
```

**Hilfen:**

1. *Tipp:* „Zeichne das Rechteck und den Zuwachs nach einem Jahr ein. Du bekommst zwei lange, schmale Streifen und ein winziges Quadrat in der Ecke."
2. *Ansatz:* „Produktregel: <span class="m" data-tex="A(t)=l(t)\cdot b(t)" data-plain="A(t) = l(t) · b(t)"></span>, also <span class="m" data-tex="A'(t)=l'(t)\,b(t)+l(t)\,b'(t)" data-plain="A′(t) = l′(t)·b(t) + l(t)·b′(t)"></span>. Die beiden Ableitungen <span class="m" data-tex="l'=3" data-plain="l′ = 3"></span> und <span class="m" data-tex="b'=2" data-plain="b′ = 2"></span> sind konstant; einzusetzen sind zusätzlich die **Werte** <span class="m" data-tex="l(0)" data-plain="l(0)"></span> und <span class="m" data-tex="b(0)" data-plain="b(0)"></span>."
3. *Lösungsweg:* <span class="m" data-tex="A'(0) = 3\cdot 25 + 40\cdot 2 = 75 + 80 = 155" data-plain="A′(0) = 3 · 25 + 40 · 2 = 75 + 80 = 155"></span> m²/Jahr.
   Kontrolle durch Ausmultiplizieren: <span class="m" data-tex="A(t) = 6t^{2}+155t+1000" data-plain="A(t) = 6t² + 155t + 1000"></span>, also <span class="m" data-tex="A'(t)=12t+155" data-plain="A′(t) = 12t + 155"></span> und <span class="m" data-tex="A'(0)=155" data-plain="A′(0) = 155"></span> ✓
   Zweite Kontrolle über den echten Zuwachs eines Jahres: <span class="m" data-tex="A(1)-A(0)=161" data-plain="A(1) − A(0) = 161"></span> m² — das sind die 155 m² der beiden Streifen plus 6 m² Eckquadrat.

**Kontrollrechnung:** K18.

---

### Aufgabe 2 — `a2` · Zahleneingabe · Anforderungsbereich I

Aufgabentext (wörtlich):

> Ein kugelförmiger Wetterballon wird aufgeblasen. Sein Radius wächst nach
> <span class="m" data-tex="r(t) = 2 + 0{,}5\,t" data-plain="r(t) = 2 + 0,5 t"></span> (in cm,
> <span class="m" data-tex="t" data-plain="t"></span> in Sekunden). Für das Volumen einer Kugel
> gilt <span class="m" data-tex="V = \tfrac{4}{3}\pi r^{3}" data-plain="V = (4/3)·π·r³"></span>.
> Berechne, wie schnell das Volumen nach 4 Sekunden zunimmt.

**Einheitenliste:** `cm³/s` · `cm²/s` · `cm³` · `cm/s`

**Eintrag in `numDaten`:**

```js
a2:{ wert:100.53, einheit:"cm³/s", tol:0.15,
     ok:"Richtig. r(4) = 4,0 cm; V′(t) = 4πr²·r′ = 4π·16·0,5 = 32π ≈ 100,53 cm³/s.",
     falschEinheit:"Der Zahlenwert stimmt. Ein Volumen pro Zeit wird in cm³ pro Sekunde gemessen; cm²/s wäre eine Flächenänderung, cm³ ein Volumen ohne Zeitbezug.",
     nah:"Prüfe zuerst den Radius: Gefragt ist der Zeitpunkt t = 4 s, dort ist r(4) = 2 + 0,5·4 = 4,0 cm — nicht 2 cm und nicht 3,5 cm. Eingesetzt wird r(4), abgeleitet wird nach t.",
     weit:"201,06 cm³/s ist genau das Doppelte des richtigen Werts: Dir fehlt die innere Ableitung r′ = 0,5. Der Ausdruck 4πr² allein ist die Kugeloberfläche (64π ≈ 201,06) und hat die Einheit cm², keine Rate. 25,13 cm³/s bekommt man, wenn man r = 2 statt r(4) = 4 einsetzt." }
```

**Hilfen:**

1. *Tipp:* „Zwei Dinge hängen hier voneinander ab: Das Volumen hängt vom Radius ab, der Radius von der Zeit. Kläre zuerst, welche Größe die innere und welche die äußere ist."
2. *Ansatz:* „Kettenregel in der Leibniz-Schreibweise: <span class="m" data-tex="\frac{\mathrm{d}V}{\mathrm{d}t} = \frac{\mathrm{d}V}{\mathrm{d}r}\cdot\frac{\mathrm{d}r}{\mathrm{d}t}" data-plain="dV/dt = dV/dr · dr/dt"></span>. Bestimme <span class="m" data-tex="\mathrm{d}V/\mathrm{d}r" data-plain="dV/dr"></span> aus der Kugelformel und lies <span class="m" data-tex="\mathrm{d}r/\mathrm{d}t" data-plain="dr/dt"></span> direkt aus <span class="m" data-tex="r(t)" data-plain="r(t)"></span> ab. Setze erst zum Schluss <span class="m" data-tex="r(4)" data-plain="r(4)"></span> ein."
3. *Lösungsweg:* <span class="m" data-tex="\frac{\mathrm{d}V}{\mathrm{d}r} = \tfrac{4}{3}\pi\cdot 3r^{2} = 4\pi r^{2}" data-plain="dV/dr = (4/3)·π·3r² = 4π·r²"></span> und <span class="m" data-tex="\frac{\mathrm{d}r}{\mathrm{d}t}=0{,}5" data-plain="dr/dt = 0,5"></span> cm/s.
   Mit <span class="m" data-tex="r(4)=2+0{,}5\cdot 4 = 4{,}0" data-plain="r(4) = 2 + 0,5 · 4 = 4,0"></span> cm folgt
   <span class="m" data-tex="\frac{\mathrm{d}V}{\mathrm{d}t}\Big|_{t=4} = 4\pi\cdot 16\cdot 0{,}5 = 32\pi \approx 100{,}53" data-plain="dV/dt bei t = 4: 4π · 16 · 0,5 = 32π ≈ 100,53"></span> cm³/s.
   Zur Einordnung: Das Volumen beträgt dort <span class="m" data-tex="V(4)=\tfrac{256}{3}\pi\approx 268{,}08" data-plain="V(4) = (256/3)·π ≈ 268,08"></span> cm³ — pro Sekunde kommt also gut ein Drittel des aktuellen Volumens hinzu.

**Kontrollrechnung:** K19.

---

### Aufgabe 3 — `mc1` · Multiple Choice · Anforderungsbereich II — richtige Option: Index **1**

Frage (wörtlich):

> Der Graph von <span class="m" data-tex="f(x) = (2x-3)^{4}" data-plain="f(x) = (2x − 3)⁴"></span>
> hat an der Stelle <span class="m" data-tex="x = 1{,}5" data-plain="x = 1,5"></span> eine
> waagerechte Tangente. Welche Begründung ist vollständig **und** richtig?

| Index | Option |
|---|---|
| 0 | Weil <span class="m" data-tex="f(1{,}5)=0" data-plain="f(1,5) = 0"></span> ist und an einer Nullstelle die Ableitung immer null ist. |
| 1 | Weil <span class="m" data-tex="f'(x) = 8(2x-3)^{3}" data-plain="f′(x) = 8(2x − 3)³"></span> ist und der Faktor <span class="m" data-tex="(2x-3)^{3}" data-plain="(2x − 3)³"></span> bei <span class="m" data-tex="x=1{,}5" data-plain="x = 1,5"></span> verschwindet. |
| 2 | Weil <span class="m" data-tex="f'(x) = 4(2x-3)^{3}" data-plain="f′(x) = 4(2x − 3)³"></span> ist und die innere Ableitung dort null wird. |
| 3 | Weil die innere Funktion <span class="m" data-tex="2x-3" data-plain="2x − 3"></span> bei <span class="m" data-tex="x=1{,}5" data-plain="x = 1,5"></span> ihr Minimum hat. |

Feedback:
- 0: „Eine Nullstelle der Funktion hat mit der Ableitung nichts zu tun. Gegenbeispiel: f(x) = 2x − 3 hat bei x = 1,5 ebenfalls eine Nullstelle, aber überall die Steigung 2. Dass hier tatsächlich f′(1,5) = 0 gilt, liegt an der vierten Potenz, nicht an der Nullstelle."
- 1: „Richtig. Kettenregel: äußere Ableitung 4(2x − 3)³, innere Ableitung 2, zusammen 8(2x − 3)³. Bei x = 1,5 ist der Klammerterm null, also f′(1,5) = 0. Der Graph berührt die x-Achse dort von oben — typisch für eine gerade Potenz."
- 2: „Der Faktor 2 aus der inneren Ableitung fehlt; richtig ist 8(2x − 3)³. Vor allem aber ist die Begründung falsch: Die innere Ableitung ist konstant 2 und wird nirgends null. Null wird die **innere Funktion** — das ist etwas anderes."
- 3: „2x − 3 ist eine Gerade; sie hat weder Minimum noch Maximum, sie fällt oder steigt gleichmäßig. Ein Extremum hat hier nur die zusammengesetzte Funktion, und zwar deshalb, weil die vierte Potenz aus einem Vorzeichenwechsel ein Minimum macht."

---

### Aufgabe 4 — `a3` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Nach der Einnahme eines Medikaments beschreibt
> <span class="m" data-tex="c(t) = \dfrac{20\,t}{t^{2}+4}" data-plain="c(t) = 20 t / (t² + 4)"></span>
> die Wirkstoffkonzentration im Blut in mg/L; <span class="m" data-tex="t" data-plain="t"></span>
> ist die Zeit in Stunden seit der Einnahme. Berechne, wie schnell die Konzentration eine Stunde
> nach der Einnahme zunimmt.

**Einheitenliste:** `mg/(L·h)` · `mg/L` · `mg·h/L` · `h`

**Eintrag in `numDaten`:**

```js
a3:{ wert:2.4, einheit:"mg/(L·h)", tol:0.02,
     ok:"Richtig. c′(t) = (80 − 20t²)/(t² + 4)², also c′(1) = 60/25 = 2,4 mg pro Liter und Stunde.",
     falschEinheit:"Der Zahlenwert stimmt. Gefragt ist aber eine Änderungsrate: Konzentration pro Zeit, also mg/(L·h). mg/L wäre die Konzentration selbst — die beträgt bei t = 1 übrigens 4 mg/L.",
     nah:"Das Vorzeichen passt nicht. −2,4 entsteht, wenn man die beiden Summanden im Zähler vertauscht: Die Quotientenregel beginnt mit der Ableitung des Zählers, also u′v − uv′ und nicht uv′ − u′v. Inhaltlich muss der Wert positiv sein — eine Stunde nach der Einnahme steigt die Konzentration noch, ihr Maximum liegt erst bei t = 2 h.",
     weit:"10 mg/(L·h) bekommt man mit der falschen Regel u′/v′ = 20/(2t). Dass sie falsch ist, siehst du an x²/x: gekürzt ist das x mit der Steigung 1, die naive Rechnung liefert 2x. 12 mg/(L·h) entsteht, wenn der Nenner nicht quadriert wird — in der Quotientenregel steht v², hier also (t² + 4)² = 25." }
```

**Hilfen:**

1. *Tipp:* „Zähler und Nenner hängen beide von <span class="m" data-tex="t" data-plain="t"></span> ab. Kürzen lässt sich nichts, umschreiben als Produkt lohnt sich hier nicht — das ist der Standardfall für die Quotientenregel."
2. *Ansatz:* „<span class="m" data-tex="u(t)=20t,\ v(t)=t^{2}+4" data-plain="u(t) = 20t, v(t) = t² + 4"></span>, also <span class="m" data-tex="u'=20" data-plain="u′ = 20"></span> und <span class="m" data-tex="v'=2t" data-plain="v′ = 2t"></span>. Einsetzen in <span class="m" data-tex="c'=\frac{u'v-uv'}{v^{2}}" data-plain="c′ = (u′v − uv′)/v²"></span> und **erst danach** <span class="m" data-tex="t=1" data-plain="t = 1"></span> einsetzen — der Nenner wird nicht ausmultipliziert."
3. *Lösungsweg:*
   <span class="m block" data-tex="c'(t) = \frac{20(t^{2}+4) - 20t\cdot 2t}{(t^{2}+4)^{2}} = \frac{20t^{2}+80-40t^{2}}{(t^{2}+4)^{2}} = \frac{80-20t^{2}}{(t^{2}+4)^{2}}" data-plain="c′(t) = [20(t² + 4) − 20t · 2t]/(t² + 4)² = (20t² + 80 − 40t²)/(t² + 4)² = (80 − 20t²)/(t² + 4)²"></span>
   Einsetzen: <span class="m" data-tex="c'(1) = \frac{80-20}{25} = \frac{60}{25} = 2{,}4" data-plain="c′(1) = (80 − 20)/25 = 60/25 = 2,4"></span> mg/(L·h).
   Probe auf Plausibilität: Der Zähler wird bei <span class="m" data-tex="t=2" data-plain="t = 2"></span> null, dort liegt das Konzentrationsmaximum mit <span class="m" data-tex="c(2)=5" data-plain="c(2) = 5"></span> mg/L. Vor diesem Zeitpunkt muss die Rate positiv sein — sie ist es.

**Kontrollrechnung:** K20.

---

### Aufgabe 5 — `a4` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Ein zylindrisches Gefäß wird von außen aufgeweitet und gleichzeitig zusammengedrückt: Sein
> Innenradius wächst nach <span class="m" data-tex="r(t) = 3 + 0{,}2\,t" data-plain="r(t) = 3 + 0,2 t"></span>,
> seine Höhe sinkt nach <span class="m" data-tex="h(t) = 20 - 0{,}5\,t" data-plain="h(t) = 20 − 0,5 t"></span>
> (beides in cm, <span class="m" data-tex="t" data-plain="t"></span> in Sekunden). Für das
> Fassungsvermögen gilt <span class="m" data-tex="V = \pi r^{2} h" data-plain="V = π · r² · h"></span>.
> Berechne <span class="m" data-tex="V'(5)" data-plain="V′(5)"></span> und entscheide damit, ob das
> Gefäß nach fünf Sekunden gerade mehr oder weniger fasst.

**Einheitenliste:** `cm³/s` · `cm²/s` · `cm³` · `cm/s`

**Eintrag in `numDaten`:**

```js
a4:{ wert:62.83, einheit:"cm³/s", tol:0.1,
     ok:"Richtig. V′(t) = π(2r·r′·h + r²·h′); bei t = 5 ist r = 4,0 cm und h = 17,5 cm, also V′(5) = π(2·4·0,2·17,5 + 16·(−0,5)) = π(28 − 8) = 20π ≈ 62,83 cm³/s. Positiv — das Gefäß fasst zu diesem Zeitpunkt noch mehr.",
     falschEinheit:"Der Zahlenwert stimmt. Ein Fassungsvermögen ändert sich in Kubikzentimetern pro Sekunde; cm²/s wäre eine Flächenrate, cm³ ein Volumen.",
     nah:"87,96 cm³/s ist 28π — das ist nur der erste Summand. Du hast den Beitrag der sinkenden Höhe unterschlagen: r²·h′ = 16·(−0,5) = −8 zieht π·8 ≈ 25,13 cm³/s wieder ab. Beim Produkt zählen immer beide Beiträge, auch wenn einer negativ ist.",
     weit:"414,69 cm³/s entsteht, wenn r² wie ein einfaches r behandelt wird: Die Ableitung von r(t)² ist nach der Kettenregel 2·r(t)·r′(t) = 2·4·0,2 = 1,6 und nicht 2·r(t) = 8. −25,13 cm³/s ist umgekehrt nur der zweite Summand. Rechne beide Summanden getrennt auf und addiere sie erst am Schluss." }
```

**Hilfen:**

1. *Tipp:* „Hier steckt eine Regel in der anderen. Frage dich zuerst: Welche Rechenoperation führst du als **letzte** aus, wenn du <span class="m" data-tex="V" data-plain="V"></span> für ein konkretes <span class="m" data-tex="t" data-plain="t"></span> ausrechnest?"
2. *Ansatz:* „Äußerste Operation ist die Multiplikation von <span class="m" data-tex="r(t)^{2}" data-plain="r(t)²"></span> mit <span class="m" data-tex="h(t)" data-plain="h(t)"></span>, also Produktregel — der Faktor <span class="m" data-tex="\pi" data-plain="π"></span> bleibt nach der Faktorregel davor stehen. Für die Ableitung von <span class="m" data-tex="r(t)^{2}" data-plain="r(t)²"></span> brauchst du die Kettenregel: <span class="m" data-tex="\big(r(t)^{2}\big)' = 2\,r(t)\,r'(t)" data-plain="(r(t)²)′ = 2·r(t)·r′(t)"></span>."
3. *Lösungsweg:*
   <span class="m block" data-tex="V'(t) = \pi\Big(2\,r(t)\,r'(t)\,h(t) + r(t)^{2}\,h'(t)\Big)" data-plain="V′(t) = π · (2·r(t)·r′(t)·h(t) + r(t)²·h′(t))"></span>
   Mit <span class="m" data-tex="r(5)=4{,}0" data-plain="r(5) = 4,0"></span> cm,
   <span class="m" data-tex="h(5)=17{,}5" data-plain="h(5) = 17,5"></span> cm,
   <span class="m" data-tex="r'=0{,}2" data-plain="r′ = 0,2"></span> cm/s,
   <span class="m" data-tex="h'=-0{,}5" data-plain="h′ = −0,5"></span> cm/s:
   <span class="m block" data-tex="V'(5) = \pi\big(2\cdot 4\cdot 0{,}2\cdot 17{,}5 + 4^{2}\cdot(-0{,}5)\big) = \pi(28 - 8) = 20\pi \approx 62{,}83" data-plain="V′(5) = π · (2 · 4 · 0,2 · 17,5 + 4² · (−0,5)) = π(28 − 8) = 20π ≈ 62,83"></span>
   also **+62,83 cm³/s**: Das Gefäß fasst nach fünf Sekunden noch mehr, der Radiusgewinn überwiegt
   den Höhenverlust. Zum Vergleich: <span class="m" data-tex="V(5)=280\pi\approx 879{,}65" data-plain="V(5) = 280π ≈ 879,65"></span> cm³.

**Kontrollrechnung:** K21.

---

### Aufgabe 6 — `z1` · Zuordnung · Anforderungsbereich II

Aufgabentext:

> Vier Funktionen sind aus denselben beiden Bausteinen
> <span class="m" data-tex="x^{3}" data-plain="x³"></span> und
> <span class="m" data-tex="2x+1" data-plain="2x + 1"></span> aufgebaut — nur unterschiedlich
> verknüpft. Ordne jeder Funktion ihre Ableitung zu.

**Karten A bis D** in `.diagramme`. Abweichend vom Referenzmodul enthalten die
`<figure>`-Elemente hier **kein Inline-SVG, sondern je eine Formel** als
`<div class="m block" data-tex="…" data-plain="…">`; `<figcaption>` trägt den Buchstaben. Die
Engine `[data-check="zuordnung"]` bleibt unverändert, weil sie nur die `<select>`-Werte gegen
`data-loesung` prüft. `formelnRendern()` läuft beim Laden ohnehin über alle `.m`-Elemente.

| Karte | Term |
|---|---|
| **A** | <span class="m" data-tex="8x^{3}+3x^{2}" data-plain="8x³ + 3x²"></span> |
| **B** | <span class="m" data-tex="-\dfrac{4x+3}{x^{4}}" data-plain="−(4x + 3)/x⁴"></span> |
| **C** | <span class="m" data-tex="6(2x+1)^{2}" data-plain="6(2x + 1)²"></span> |
| **D** | <span class="m" data-tex="\dfrac{4x^{3}+3x^{2}}{(2x+1)^{2}}" data-plain="(4x³ + 3x²)/(2x + 1)²"></span> |

**Zeilen der Zuordnung** (Reihenfolge bewusst **nicht** die der Karten):

| Zeile | Funktion | `data-loesung` |
|---|---|---|
| 1 | <span class="m" data-tex="f(x)=\dfrac{x^{3}}{2x+1}" data-plain="f(x) = x³/(2x + 1)"></span> | **D** |
| 2 | <span class="m" data-tex="f(x)=(2x+1)^{3}" data-plain="f(x) = (2x + 1)³"></span> | **C** |
| 3 | <span class="m" data-tex="f(x)=\dfrac{2x+1}{x^{3}}" data-plain="f(x) = (2x + 1)/x³"></span> | **B** |
| 4 | <span class="m" data-tex="f(x)=x^{3}(2x+1)" data-plain="f(x) = x³(2x + 1)"></span> | **A** |

Lösungsfolge von oben nach unten: **D · C · B · A**.

Rückmeldungen der Zuordnungs-Engine (die Engine des Referenzmoduls unterscheidet „alles richtig"
und „teilweise richtig"):
- alles richtig: „Alle vier stimmen. Beachte, wie nah die beiden Brüche beieinanderliegen und wie unterschiedlich ihre Ableitungen aussehen — beim Quotienten entscheidet die Reihenfolge von Zähler und Nenner alles."
- teilweise richtig: „Noch nicht alles. Zwei Strategien helfen: Erstens entscheidet die **äußerste** Rechenoperation über die Regel — Potenz, Produkt oder Division. Zweitens kannst du zwei der vier Ableitungen ohne jede Regel kontrollieren, indem du die Funktion vorher umformst (ausmultiplizieren bzw. gliedweise dividieren)."

**Kontrollrechnung:** K23. Für Zeile 4 ist
<span class="m" data-tex="x^{3}(2x+1) = 2x^{4}+x^{3}" data-plain="x³(2x + 1) = 2x⁴ + x³"></span>
und damit <span class="m" data-tex="8x^{3}+3x^{2}" data-plain="8x³ + 3x²"></span>; für Zeile 3 ist
<span class="m" data-tex="\frac{2x+1}{x^{3}} = 2x^{-2}+x^{-3}" data-plain="(2x + 1)/x³ = 2x⁻² + x⁻³"></span>
und damit <span class="m" data-tex="-4x^{-3}-3x^{-4} = -\frac{4x+3}{x^{4}}" data-plain="−4x⁻³ − 3x⁻⁴ = −(4x + 3)/x⁴"></span>.
Beide Umformungen sind die in der Rückmeldung genannte Selbstkontrolle.

---

### Aufgabe 7 — `a5` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Ein Freibad führt ein neues Preismodell ein. Der Eintrittspreis steigt nach
> <span class="m" data-tex="p(t) = 4{,}00 + 0{,}20\,t" data-plain="p(t) = 4,00 + 0,20 t"></span>
> (in €), die Besucherzahl sinkt nach
> <span class="m" data-tex="n(t) = 300 - 5t" data-plain="n(t) = 300 − 5 t"></span>;
> <span class="m" data-tex="t" data-plain="t"></span> zählt die Tage. Bestimme den Tag, an dem der
> Tagesumsatz am größten ist.

**Einheitenliste:** `Tage` · `Stunden` · `€` · `€/Tag`

**Eintrag in `numDaten`:**

```js
a5:{ wert:20, einheit:"Tage", tol:0.2,
     alt:{wert:480, einheit:"Stunden"},
     ok:"Richtig. U′(t) = 0,20·(300 − 5t) + (4,00 + 0,20t)·(−5) = (60 − t) + (−20 − t) = 40 − 2t; Nullstelle bei t = 20 Tagen. Wegen U″ = −2 < 0 liegt dort das Maximum mit U(20) = 8,00 € · 200 = 1600 €.",
     falschEinheit:"Der Zahlenwert stimmt, aber gefragt ist ein Zeitpunkt. 20 Tage (oder gleichwertig 480 Stunden) — nicht Euro und nicht Euro pro Tag. 1600 € wäre der zugehörige Umsatz, nicht der Tag.",
     nah:"Prüfe die beiden Summanden einzeln: p′·n = 0,20·(300 − 5t) = 60 − t und p·n′ = (4,00 + 0,20t)·(−5) = −20 − t. Ihre Summe ist 40 − 2t. Wenn bei dir stattdessen 40 − t oder 60 − 2t herauskommt, ist beim Ausmultiplizieren einer der beiden Terme verloren gegangen.",
     weit:"Setze nicht U(t), sondern U′(t) gleich null — gesucht ist die Stelle, an der der Umsatz aufhört zu steigen, nicht die, an der er verschwindet. t = 60 ist die Nullstelle von n(t), dort ist niemand mehr im Bad. Und wenn dein U′(t) gar kein t mehr enthält (etwa die Konstante 80), hast du das Minuszeichen von n′ zweimal gezählt." }
```

**Hilfen:**

1. *Tipp:* „Der Umsatz ist das Produkt aus Preis und Besucherzahl. Ein Maximum erkennst du an der Stelle, an der die Änderungsrate des Umsatzes das Vorzeichen wechselt."
2. *Ansatz:* „Stelle <span class="m" data-tex="U(t)=p(t)\cdot n(t)" data-plain="U(t) = p(t) · n(t)"></span> auf, leite mit der Produktregel ab und löse <span class="m" data-tex="U'(t)=0" data-plain="U′(t) = 0"></span>. Für den Nachweis, dass es ein Maximum und kein Minimum ist, genügt hier das Vorzeichen von <span class="m" data-tex="U''" data-plain="U″"></span>."
3. *Lösungsweg:*
   <span class="m block" data-tex="U'(t) = 0{,}20\,(300-5t) + (4{,}00+0{,}20t)\cdot(-5) = (60-t) + (-20-t) = 40-2t" data-plain="U′(t) = 0,20 · (300 − 5t) + (4,00 + 0,20t) · (−5) = (60 − t) + (−20 − t) = 40 − 2t"></span>
   <span class="m" data-tex="40-2t = 0 \Leftrightarrow t = 20" data-plain="40 − 2t = 0 ⟺ t = 20"></span>, also am **20. Tag**.
   Nachweis: <span class="m" data-tex="U''(t) = -2 < 0" data-plain="U″(t) = −2 < 0"></span> für alle <span class="m" data-tex="t" data-plain="t"></span>, also Maximum.
   Kontrolle durch Ausmultiplizieren: <span class="m" data-tex="U(t) = -t^{2}+40t+1200" data-plain="U(t) = −t² + 40t + 1200"></span>; Scheitel bei <span class="m" data-tex="t=20" data-plain="t = 20"></span> ✓
   Zugehöriger Umsatz: <span class="m" data-tex="U(20) = 8{,}00\ \text{€}\cdot 200 = 1600\ \text{€}" data-plain="U(20) = 8,00 € · 200 = 1600 €"></span> gegenüber 1200 € am Anfang.

**Kontrollrechnung:** K22.

---

### Aufgabe 8 — `a6` · offene Aufgabe · Anforderungsbereich III

Aufgabentext (wörtlich):

> In einem Heft stehen zwei selbstformulierte Merksätze:
> **(1)** „Wenn beide Faktoren wachsen, wächst auch ihr Produkt."
> **(2)** „Wenn ein Faktor wächst und der andere fällt, kann man über das Produkt nichts sagen."
> Nimm zu beiden Sätzen Stellung. Belege deine Bewertung jeweils mit einem konkreten Beispiel und
> gib bei Satz (1) an, unter welcher Zusatzvoraussetzung er richtig wird.

`<textarea>` mit Platzhalter „Deine Stellungnahme…", darunter
`<button data-loesung="a6">Musterlösung anzeigen</button>`.

**Hilfen:**

1. *Tipp:* „‚Wachsen' ist eine Aussage über die Ableitung. Was in der Produktregel zusätzlich vorkommt, sind die Funktions**werte** — und über deren Vorzeichen ist bisher nichts gesagt."
2. *Ansatz:* „Schreibe <span class="m" data-tex="(uv)' = u'v + uv'" data-plain="(u·v)′ = u′v + uv′"></span> hin und prüfe für beide Sätze, welche der vier Größen <span class="m" data-tex="u,\ v,\ u',\ v'" data-plain="u, v, u′, v′"></span> durch die Voraussetzung festgelegt sind und welche frei bleiben."
3. *Lösungsweg (Strukturhilfe, keine Rechnung):* „Gliedere deine Antwort in drei Teile: erstens die allgemeine Entscheidungsgrundlage (die Produktregel), zweitens ein Gegenbeispiel zu Satz (1) mit einem negativen Funktionswert, drittens die Widerlegung von Satz (2) — dort ist der Fehler nicht ein falsches Ergebnis, sondern die Behauptung, es gebe keins."

**Musterlösung in `.hilfe-text[data-stufe="9"]`:**

> **Erwartete Argumentation.**
> **Zu (1):** Der Satz ist in dieser Form **falsch**. Aus
> <span class="m" data-tex="u' > 0" data-plain="u′ > 0"></span> und
> <span class="m" data-tex="v' > 0" data-plain="v′ > 0"></span> folgt nach der Produktregel
> <span class="m" data-tex="(uv)' = u'v + uv'" data-plain="(uv)′ = u′v + uv′"></span> — über das
> Vorzeichen dieser Summe entscheiden aber auch die **Werte**
> <span class="m" data-tex="u" data-plain="u"></span> und
> <span class="m" data-tex="v" data-plain="v"></span>, und die dürfen negativ sein.
> Gegenbeispiel: <span class="m" data-tex="u(t)=t" data-plain="u(t) = t"></span>,
> <span class="m" data-tex="v(t)=t-10" data-plain="v(t) = t − 10"></span>, beide streng monoton
> wachsend mit <span class="m" data-tex="u'=v'=1" data-plain="u′ = v′ = 1"></span>. An der Stelle
> <span class="m" data-tex="t=1" data-plain="t = 1"></span> ist
> <span class="m" data-tex="(uv)'(1) = 1\cdot(-9) + 1\cdot 1 = -8 < 0" data-plain="(uv)′(1) = 1·(−9) + 1·1 = −8 < 0"></span>:
> Das Produkt **fällt**, obwohl beide Faktoren wachsen. (Anschaulich:
> <span class="m" data-tex="uv = t^{2}-10t" data-plain="uv = t² − 10t"></span> ist eine nach oben
> geöffnete Parabel mit Scheitel bei <span class="m" data-tex="t=5" data-plain="t = 5"></span>.)
> **Richtig wird der Satz mit der Zusatzvoraussetzung
> <span class="m" data-tex="u>0" data-plain="u > 0"></span> und
> <span class="m" data-tex="v>0" data-plain="v > 0"></span>** an der betrachteten Stelle: Dann sind
> beide Summanden positiv, und die Summe ist es auch.
>
> **Zu (2):** Auch dieser Satz ist **falsch**, aber aus einem anderen Grund. Er verwechselt „das
> Ergebnis hängt von den Daten ab" mit „man kann nichts sagen". Tatsächlich ist die Frage
> vollständig entscheidbar: Man berechnet
> <span class="m" data-tex="u'v + uv'" data-plain="u′v + uv′"></span> und liest das Vorzeichen ab.
> Beispiel aus dem Einstieg: Preis
> <span class="m" data-tex="p(t)=5{,}00+0{,}10t" data-plain="p(t) = 5,00 + 0,10 t"></span> steigt,
> Besucherzahl <span class="m" data-tex="n(t)=400-6t" data-plain="n(t) = 400 − 6 t"></span> fällt —
> und trotzdem steht fest:
> <span class="m" data-tex="U'(0) = 0{,}10\cdot 400 + 5{,}00\cdot(-6) = +10" data-plain="U′(0) = 0,10 · 400 + 5,00 · (−6) = +10"></span> €/Tag,
> der Umsatz steigt. Richtig an Satz (2) ist nur, dass man das Vorzeichen **nicht ohne Rechnung**
> ablesen kann — und dass es von der Stelle abhängt: bei
> <span class="m" data-tex="t=12" data-plain="t = 12"></span> ist dieselbe Ableitung −4,40 €/Tag.
>
> **Bewertungskriterien.** Produktregel als Entscheidungsgrundlage genannt ·
> Satz (1) korrekt als falsch bewertet · tragfähiges Gegenbeispiel mit Rechnung und negativem
> Funktionswert · Zusatzvoraussetzung <span class="m" data-tex="u,v>0" data-plain="u, v > 0"></span>
> formuliert · Satz (2) als Fehlschluss erkannt (entscheidbar, aber nicht ohne Rechnung) ·
> konkretes Gegenbeispiel zu (2) · saubere sprachliche Trennung von Funktionswert und Änderungsrate.

**Kontrollrechnung:** K25 und K1.

---

### Aufgabe 9 — `a7` · offene Aufgabe · Anforderungsbereich III

Aufgabentext (wörtlich):

> „Die Quotientenregel ist eigentlich überflüssig." Begründe, ob diese Behauptung zutrifft. Gehe
> dabei auf drei Punkte ein: wie man die Quotientenregel aus anderen Regeln gewinnt, welche
> Voraussetzung dabei gebraucht wird, und was das Minuszeichen im Zähler inhaltlich bedeutet.
> Schließe mit einer Bewertung: Würdest du die Regel trotzdem auswendig lernen?

`<textarea>`, Knopf `data-loesung="a7"`.

**Hilfen:**

1. *Tipp:* „Ein Bruch ist eine Schreibweise, keine eigene Rechenart. Frage dich, als was du <span class="m" data-tex="\frac{u}{v}" data-plain="u/v"></span> sonst noch schreiben kannst."
2. *Ansatz:* „<span class="m" data-tex="\frac{u}{v} = u\cdot\frac{1}{v}" data-plain="u/v = u · (1/v)"></span>. Damit ist es ein Produkt, und für den zweiten Faktor brauchst du die Reziprokenregel aus Abschnitt 3.2. Für die inhaltliche Deutung des Minuszeichens hilft ein Blick auf <span class="m" data-tex="f(x)=1/x" data-plain="f(x) = 1/x"></span>."
3. *Lösungsweg (Strukturhilfe):* „Baue die Antwort in vier Schritten auf: (a) Umschreiben als Produkt, (b) Ableiten mit Produkt- und Reziprokenregel, (c) Zusammenfassen auf den Hauptnenner <span class="m" data-tex="v^{2}" data-plain="v²"></span>, (d) Voraussetzung und Deutung. Die Bewertung am Schluss darf begründet in beide Richtungen ausfallen."

**Musterlösung (Stufe 9):**

> **Erwartete Argumentation.** Die Behauptung trifft im mathematischen Sinn **zu**: Die
> Quotientenregel ist keine unabhängige Regel, sondern eine Folgerung.
>
> **(a) Herleitung.** <span class="m" data-tex="\frac{u}{v} = u\cdot\frac{1}{v}" data-plain="u/v = u · (1/v)"></span>.
> Die Reziprokenregel
> <span class="m" data-tex="\left(\frac{1}{v}\right)' = -\frac{v'}{v^{2}}" data-plain="(1/v)′ = −v′/v²"></span>
> gewinnt man selbst wieder aus der Produktregel, indem man
> <span class="m" data-tex="v\cdot\frac1v = 1" data-plain="v · (1/v) = 1"></span> ableitet. Damit:
> <span class="m block" data-tex="\left(\frac{u}{v}\right)' = u'\cdot\frac{1}{v} + u\cdot\left(-\frac{v'}{v^{2}}\right) = \frac{u'v}{v^{2}} - \frac{uv'}{v^{2}} = \frac{u'v-uv'}{v^{2}}" data-plain="(u/v)′ = u′·(1/v) + u·(−v′/v²) = u′v/v² − uv′/v² = (u′v − uv′)/v²"></span>
>
> **(b) Voraussetzung.** Gebraucht wird
> <span class="m" data-tex="v(x)\neq 0" data-plain="v(x) ≠ 0"></span> an der betrachteten Stelle —
> sonst ist die Funktion dort gar nicht definiert und die Frage nach der Ableitung sinnlos. Außerdem
> müssen <span class="m" data-tex="u" data-plain="u"></span> und
> <span class="m" data-tex="v" data-plain="v"></span> dort differenzierbar sein.
>
> **(c) Deutung des Minuszeichens.** Der Nenner wirkt umgekehrt auf den Funktionswert: Wächst
> <span class="m" data-tex="v" data-plain="v"></span>, so wird der Bruch kleiner. Deshalb geht
> <span class="m" data-tex="v'" data-plain="v′"></span> mit negativem Vorzeichen ein. Am Beispiel
> <span class="m" data-tex="f(x)=1/x" data-plain="f(x) = 1/x"></span> sieht man es unmittelbar:
> <span class="m" data-tex="f'(x) = -1/x^{2} < 0" data-plain="f′(x) = −1/x² < 0"></span> für alle
> <span class="m" data-tex="x\neq 0" data-plain="x ≠ 0"></span>. Daraus folgt auch die praktische
> Warnung: Anders als bei der Produktregel darf man die beiden Summanden im Zähler **nicht**
> vertauschen, weil sich dabei das Vorzeichen des gesamten Ergebnisses umdreht.
>
> **(d) Bewertung.** Beide Antworten sind vertretbar, wenn sie begründet werden. Für das
> Auswendiglernen spricht die Arbeitsersparnis in Klausuren und dass die fertige Form weniger
> Umformungsfehler zulässt; dagegen spricht, dass eine hergeleitete Regel bei einer
> Gedächtnislücke rekonstruierbar bleibt, eine auswendig gelernte nicht. Fachlich wichtig ist die
> Einsicht: Wer die Produkt- und die Kettenregel sicher beherrscht, kann **jede**
> Quotientenaufgabe auch ohne die dritte Regel lösen.
>
> **Bewertungskriterien.** Umschreiben des Bruchs als Produkt ·
> Reziproken- oder Kettenregel korrekt auf <span class="m" data-tex="1/v" data-plain="1/v"></span>
> angewendet · fehlerfreies Zusammenfassen auf den Hauptnenner
> <span class="m" data-tex="v^{2}" data-plain="v²"></span> · Voraussetzung
> <span class="m" data-tex="v(x)\neq 0" data-plain="v(x) ≠ 0"></span> genannt · inhaltliche Deutung
> des Minuszeichens (wachsender Nenner verkleinert den Bruch) mit Beispiel · begründete Bewertung
> mit mindestens einem Argument pro Seite.

**Kontrollrechnung:** K11 und K26.

---

### Aufgabe 10 — `a8` · offene Aufgabe · Anforderungsbereich III

Aufgabentext (wörtlich):

> Jemand behauptet: „Die Kettenregel brauche ich gar nicht. Jede Potenz einer Funktion kann ich
> auch mit der Produktregel ableiten — ich schreibe
> <span class="m" data-tex="g(x)^{2}" data-plain="g(x)²"></span> einfach als
> <span class="m" data-tex="g(x)\cdot g(x)" data-plain="g(x) · g(x)"></span>."
> **(a)** Zeige, dass beide Wege bei
> <span class="m" data-tex="f(x) = g(x)^{2}" data-plain="f(x) = g(x)²"></span> dasselbe Ergebnis
> liefern.
> **(b)** Nimm zu der Behauptung insgesamt Stellung und nenne mindestens zwei Fälle, in denen das
> Verfahren nicht mehr trägt.

`<textarea>`, Knopf `data-loesung="a8"`.

**Hilfen:**

1. *Tipp:* „Teil (a) ist schnell erledigt: Leite <span class="m" data-tex="g\cdot g" data-plain="g · g"></span> mit der Produktregel ab und vergleiche mit dem Ergebnis der Kettenregel."
2. *Ansatz:* „Für Teil (b) frage dich, welche Verkettungen sich überhaupt als Produkt schreiben lassen. Was ist mit <span class="m" data-tex="\sqrt{2x+1}" data-plain="√(2x + 1)"></span>? Was mit <span class="m" data-tex="(3x-1)^{40}" data-plain="(3x − 1)⁴⁰"></span>?"
3. *Lösungsweg (Strukturhilfe):* „Gliedere: (a) beide Rechnungen nebeneinander, (b) erst zugeben, worin die Behauptung recht hat (ganzzahlige Exponenten), dann die Grenzen aufzählen — nicht ganzzahlige Exponenten, nicht als Potenz schreibbare Verkettungen, praktische Undurchführbarkeit. Ein Schlusssatz zur Reichweite der Aussage gehört dazu."

**Musterlösung (Stufe 9):**

> **(a) Beide Wege.**
> Produktregel: <span class="m" data-tex="(g\cdot g)' = g'\,g + g\,g' = 2\,g\,g'" data-plain="(g · g)′ = g′·g + g·g′ = 2·g·g′"></span>.
> Kettenregel mit äußerer Funktion <span class="m" data-tex="v(u)=u^{2}" data-plain="v(u) = u²"></span>:
> <span class="m" data-tex="\big(g(x)^{2}\big)' = 2\,g(x)\cdot g'(x)" data-plain="(g(x)²)′ = 2·g(x)·g′(x)"></span>.
> Dasselbe Ergebnis. Beispiel <span class="m" data-tex="g(x)=3x+1" data-plain="g(x) = 3x + 1"></span>,
> hier sogar für die dritte Potenz: Die Kettenregel liefert
> <span class="m" data-tex="3(3x+1)^{2}\cdot 3 = 9(3x+1)^{2}" data-plain="3(3x + 1)² · 3 = 9(3x + 1)²"></span>,
> die zweifach angewendete Produktregel auf
> <span class="m" data-tex="(3x+1)(3x+1)(3x+1)" data-plain="(3x + 1)(3x + 1)(3x + 1)"></span>
> ebenfalls <span class="m" data-tex="9(3x+1)^{2}" data-plain="9(3x + 1)²"></span>.
>
> **(b) Stellungnahme.** Die Behauptung ist in einem **engen Spezialfall richtig** und als
> allgemeine Aussage **falsch**. Richtig ist sie für Potenzen mit natürlichem Exponenten: Dort lässt
> sich die Potenz als wiederholtes Produkt schreiben, und die Produktregel führt (mit vollständiger
> Induktion sauber begründbar) auf
> <span class="m" data-tex="(g^{n})' = n\,g^{n-1}g'" data-plain="(gⁿ)′ = n·gⁿ⁻¹·g′"></span>.
> Sie trägt jedoch nicht, sobald eine der folgenden Situationen eintritt:
> **(1) Nicht ganzzahlige Exponenten.**
> <span class="m" data-tex="\sqrt{2x+1} = (2x+1)^{1/2}" data-plain="√(2x + 1) = (2x + 1)^(1/2)"></span>
> ist kein Produkt von Kopien — „ein halbes Mal mit sich selbst multipliziert" gibt es nicht.
> **(2) Verkettungen, die keine Potenzen sind.** Bei
> <span class="m" data-tex="\frac{1}{4x+7}" data-plain="1/(4x + 7)"></span>, später bei
> <span class="m" data-tex="\sin(3x)" data-plain="sin(3x)"></span> oder
> <span class="m" data-tex="\mathrm{e}^{-2x}" data-plain="e⁻²ˣ"></span> gibt es überhaupt keine
> Produktdarstellung, auf die man die Produktregel ansetzen könnte.
> **(3) Praktische Grenze.** Selbst dort, wo es geht, ist es unbrauchbar:
> <span class="m" data-tex="(3x-1)^{40}" data-plain="(3x − 1)⁴⁰"></span> als 40-faches Produkt
> abzuleiten ist ein Rechenweg, den niemand zu Ende geht.
> Hinzu kommt ein grundsätzlicher Einwand: Der Weg über die Produktregel *erklärt* nicht, warum der
> Faktor <span class="m" data-tex="g'" data-plain="g′"></span> auftaucht; die Kettenregel tut es, weil
> sie ihn als Übersetzungsfaktor zwischen zwei Änderungsraten deutet.
>
> **Bewertungskriterien.** Teil (a) mit beiden Rechnungen vollständig und korrekt ·
> Übereinstimmung ausdrücklich festgestellt · Zugeständnis formuliert, in welchem Fall die
> Behauptung trägt (natürliche Exponenten) · mindestens zwei tragfähige Gegenfälle mit Beispiel ·
> Unterscheidung zwischen „rechnerisch möglich" und „praktisch durchführbar" ·
> abschließende, eindeutige Bewertung der Behauptung.

**Kontrollrechnung:** K26.

---

## 6 · Abschluss

`<section id="abschluss">`, `.stufe`-Kopf: Nr. **6**, Überschrift **Zusammenfassung und Selbstcheck**.

### 6.1 Vier Kernaussagen (je ein `<div class="merksatz">`)

**Kernaussage 1 — Beim Produkt werden Raten mit Werten bewertet, nicht mit Raten.**
<span class="m" data-tex="(u\cdot v)' = u'v + uv'" data-plain="(u · v)′ = u′v + uv′"></span>: Die
Änderungsrate eines Produkts ist eine **Summe aus zwei Beiträgen**, und in jedem Beitrag steht
neben einer Ableitung ein **Funktionswert**. Genau diese Werte lässt die naive Rechnung
<span class="m" data-tex="u'v'" data-plain="u′v′"></span> unter den Tisch fallen — im Freibadbeispiel
unterscheiden sich beide Ergebnisse um ein Vorzeichen und einen Faktor von rund 17 (genauer 16,7): +10,00 €/Tag gegenüber
−0,60. Wer die Produktregel behalten will, merkt sich nicht die Buchstaben, sondern das Rechteck:
zwei Streifen zählen, das Eckstück nicht mehr.

**Kernaussage 2 — Bei der Verkettung multiplizieren sich die Änderungsraten.**
<span class="m" data-tex="\big(v(u(x))\big)' = v'(u(x))\cdot u'(x)" data-plain="(v(u(x)))′ = v′(u(x)) · u′(x)"></span>,
in Leibniz-Schreibweise
<span class="m" data-tex="\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}u}\cdot\frac{\mathrm{d}u}{\mathrm{d}x}" data-plain="dy/dx = dy/du · du/dx"></span>.
Zwei hintereinandergeschaltete Abhängigkeiten wirken wie zwei Getriebestufen: Ihre
Übersetzungsverhältnisse werden multipliziert. Entscheidend ist die **Auswertungsstelle** — die
äußere Ableitung wird bei <span class="m" data-tex="u(x)" data-plain="u(x)"></span> genommen, nicht
bei <span class="m" data-tex="x" data-plain="x"></span>. Der Ölring zeigt dieselbe Aussage als Bild:
<span class="m" data-tex="\mathrm{d}A/\mathrm{d}r = 2\pi r" data-plain="dA/dr = 2πr"></span> ist der
Umfang, und die Fläche wächst genau dort, wo neuer Rand entsteht.

**Kernaussage 3 — Die Quotientenregel ist eine Folgerung, kein Zusatzgesetz.**
<span class="m" data-tex="\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^{2}}" data-plain="(u/v)′ = (u′v − uv′)/v²"></span>
für <span class="m" data-tex="v(x)\neq 0" data-plain="v(x) ≠ 0"></span>. Sie entsteht aus
<span class="m" data-tex="\frac{u}{v} = u\cdot\frac{1}{v}" data-plain="u/v = u · (1/v)"></span> mit
Produkt- und Reziprokenregel. Das Minuszeichen ist inhaltlich begründet: Ein wachsender Nenner
macht den Bruch kleiner. Deshalb gilt hier — anders als beim Produkt — die Reihenfolge streng.
Der Zähler beginnt mit der Ableitung des Zählers; wer die beiden Summanden vertauscht, dreht das
Vorzeichen des gesamten Ergebnisses um.

**Kernaussage 4 — Welche Regel gilt, entscheidet die zuletzt ausgeführte Rechenoperation.**
Nicht das Aussehen des Terms entscheidet, sondern die Frage: *Was rechne ich zuletzt, wenn ich
einen Zahlenwert einsetze?* Bei <span class="m" data-tex="\pi\,r(t)^{2}h(t)" data-plain="π · r(t)² · h(t)"></span>
ist das die Multiplikation — also Produktregel, und die Kettenregel steckt darin für
<span class="m" data-tex="r(t)^{2}" data-plain="r(t)²"></span>. Alle drei Regeln haben denselben
Grund: Die weggelassenen Terme sind **von zweiter Ordnung**. Das Eckstück
<span class="m" data-tex="\Delta p\,\Delta n" data-plain="Δp · Δn"></span> und der Ringfehler
<span class="m" data-tex="\pi\,\Delta r^{2}" data-plain="π · Δr²"></span> werden beim Halbieren des
Zeitschritts nicht halbiert, sondern geviertelt; geteilt durch
<span class="m" data-tex="\Delta t" data-plain="Δt"></span> bleibt ein Rest, der gegen null geht.
Deshalb stehen in den Regeln endlich viele Summanden und kein Korrekturterm.

### 6.2 Blick aufs Zentralabitur (`<div class="hinweis">`)

**Im Zentralabitur.** Die drei Regeln sind kein eigenes Prüfungsthema — sie sind das Handwerkzeug,
ohne das in der Analysis keine Teilaufgabe funktioniert. In diesen Gestalten begegnen sie dir:

- **Funktionsuntersuchung einer zusammengesetzten Funktion.** Der Standardtyp ist ein Produkt aus
  Polynom und Exponentialfunktion, etwa
  <span class="m" data-tex="f(x) = x\,\mathrm{e}^{-0{,}5x}" data-plain="f(x) = x · e^(−0,5x)"></span>.
  Dort brauchst du in derselben Aufgabe Produkt- **und** Kettenregel — und für
  <span class="m" data-tex="f''" data-plain="f″"></span> beide noch einmal auf dein eigenes
  Zwischenergebnis. Übe deshalb, die erste Ableitung sofort zu **faktorisieren** (hier
  <span class="m" data-tex="f'(x) = (1-0{,}5x)\,\mathrm{e}^{-0{,}5x}" data-plain="f′(x) = (1 − 0,5x) · e^(−0,5x)"></span>):
  Das macht die zweite Ableitung und die Nullstellensuche kurz.
- **Gebrochenrationale Funktionen im Sachkontext.** Konzentrations-, Wirkungs- und Kostenmodelle
  wie <span class="m" data-tex="c(t)=\frac{20t}{t^{2}+4}" data-plain="c(t) = 20t/(t² + 4)"></span>
  aus Aufgabe `a3`. Gefragt sind Maximum, Wendestelle und Grenzverhalten; der Nenner bleibt dabei
  als Quadrat stehen und wird nie ausmultipliziert.
- **Extremwertaufgaben mit Nebenbedingung.** Volumen, Umsatz, Materialverbrauch — die Zielgröße ist
  fast immer ein Produkt zweier veränderlicher Größen. Die inhaltliche Pointe ist dieselbe wie in
  Aufgabe `a5`: Im Optimum heben sich die beiden Beiträge der Produktregel gegenseitig auf.
- **Funktionenscharen.** Bei <span class="m" data-tex="f_k(x)" data-plain="f_k(x)"></span> wird nach
  <span class="m" data-tex="x" data-plain="x"></span> abgeleitet;
  <span class="m" data-tex="k" data-plain="k"></span> ist ein Faktor und **keine** Variable. Der
  häufigste Scharfehler ist eine erfundene Kettenregel für
  <span class="m" data-tex="k" data-plain="k"></span>.
- **Nachweisaufgaben.** „Zeige, dass <span class="m" data-tex="F" data-plain="F"></span> eine
  Stammfunktion von <span class="m" data-tex="f" data-plain="f"></span> ist." Das ist eine reine
  Ableitungsaufgabe mit Produkt- und Kettenregel. Sie geht selten durch Rechenfehler verloren,
  sondern durch unsauberes Zusammenfassen am Ende.
- **Hilfsmittelfreier Teil.** Ein Teil der Abiturklausur wird ohne Rechner bearbeitet, und genau
  dort werden Ableitungen wie
  <span class="m" data-tex="\big(\sqrt{2x+1}\big)'" data-plain="(√(2x + 1))′"></span> oder
  <span class="m" data-tex="\left(\frac{x}{x^{2}+1}\right)'" data-plain="(x/(x² + 1))′"></span> in
  einer Zeile verlangt. *Der genaue Zuschnitt dieses Teils wird jährlich in den Vorgaben des Landes
  festgelegt; er ist hier bewusst nicht zitiert.*
- **Begründungsaufgaben im LK.** Warum liefert
  <span class="m" data-tex="u'v'" data-plain="u′v′"></span> nichts Sinnvolles? Warum ist die
  Quotientenregel entbehrlich? Warum trägt die Produktregel bei
  <span class="m" data-tex="\sqrt{g(x)}" data-plain="√(g(x))"></span> nicht mehr? Genau diese drei
  Fragen hast du in `a6`, `a7` und `a8` bearbeitet.

### 6.3 Selbstcheck (`.karte` mit `<h3>Selbstcheck</h3>`, sechs `.check`-Zeilen)

Vorspann: *Hak ehrlich ab. Jeder Satz, bei dem du zögerst, kostet dich in der Klausur nicht eine
Aufgabe, sondern alle — diese drei Regeln stecken in jeder Analysis-Aufgabe der Q1.*

1. Ich kann Produkt-, Ketten- und Quotientenregel korrekt formulieren, einschließlich der
   Auswertungsstelle <span class="m" data-tex="u(x)" data-plain="u(x)"></span> bei der äußeren
   Ableitung und der Voraussetzung
   <span class="m" data-tex="v(x)\neq 0" data-plain="v(x) ≠ 0"></span> beim Quotienten.
2. Ich kann bei einem zusammengesetzten Term entscheiden, welche Regel zuerst anzuwenden ist,
   indem ich frage, welche Rechenoperation zuletzt ausgeführt wird — und ich kann zwei Regeln in
   derselben Aufgabe verschachteln, etwa bei
   <span class="m" data-tex="x^{2}\sqrt{2x+1}" data-plain="x² · √(2x + 1)"></span>.
3. Ich kann die Produktregel aus dem Differenzenquotienten herleiten und angeben, an welcher Stelle
   der Term zweiter Ordnung verschwindet und warum das zulässig ist.
4. Ich kann die Fehlvorstellungen
   <span class="m" data-tex="(uv)'=u'v'" data-plain="(uv)′ = u′v′"></span> und
   <span class="m" data-tex="(u/v)'=u'/v'" data-plain="(u/v)′ = u′/v′"></span> mit einem selbst
   gewählten Gegenbeispiel in einer Zeile widerlegen.
5. Ich kann in einem Sachzusammenhang eine Änderungsrate mit den Regeln bestimmen, ihr Vorzeichen
   und ihre Einheit deuten und daraus auf Wachstum, Abnahme oder ein Extremum schließen.
6. Ich kann begründen, warum die Quotientenregel aus Produkt- und Reziprokenregel folgt, und eine
   Aussage über Ableitungsregeln bewerten, statt sie nur anzuwenden.

### 6.4 Export und Druck

Knopfleiste wie im Referenzmodul: `Ergebnisse kopieren` (`id="bExport"`) und
`Als Arbeitsblatt drucken`. Darunter der Hinweis, dass nichts gespeichert wird und die Ergebnisse
die Seite nur über die Zwischenablage verlassen.

`var namen = {…}` am Skriptende (die Reihenfolge bestimmt die Reihenfolge im Export):

```
vw1: "Vorwissen 1 – Potenz- und Summenregel"
vw2: "Vorwissen 2 – negative Exponenten"
vw3: "Vorwissen 3 – Ableitung als Änderungsrate"
sim1:"Simulation 1 – Sekantensteigung ablesen"
sim2:"Simulation 1 – Umsatzmaximum bei d = −7"
sim3:"Simulation 2 – exakte Ringfläche ablesen"
a1:  "Aufgabe 1 – Solarfeld, Produktregel"
a2:  "Aufgabe 2 – Wetterballon, Kettenregel"
mc1: "Aufgabe 3 – waagerechte Tangente bei (2x − 3)⁴"
a3:  "Aufgabe 4 – Wirkstoffkonzentration, Quotientenregel"
a4:  "Aufgabe 5 – Zylinder, Produkt- und Kettenregel"
z1:  "Aufgabe 6 – Zuordnung der vier Ableitungen"
a5:  "Aufgabe 7 – Umsatzmaximum"
```

Die offenen Aufgaben `a6`, `a7` und `a8` werden nicht automatisch ausgewertet und stehen deshalb
nicht in dieser Liste. Ihre Texte hängt die Export-Funktion des Referenzmoduls ohnehin als
`<textarea>`-Inhalte aus `#uebungen` an — hier also drei statt zwei.

**Achtung, eine Zeile der kopierten Engine muss angepasst werden.** Die Zuordnungs-Engine des
Referenzmoduls schreibt ihr Ergebnis fest nach `ergebnisse.a3`. In diesem Modul heißt die Zuordnung
`z1`, und `a3` ist eine Zahleneingabe. Die Zeile

```js
ergebnisse.a3 = (n === zeilen.length);   // Referenzmodul
ergebnisse.z1 = (n === zeilen.length);   // hier stattdessen
```

muss also geändert werden. Wird das übersehen, überschreibt die Zuordnung das Ergebnis der
Zahleneingabe `a3`, und im Export stehen beide falsch.

### 6.5 Anschlusshinweis (`<div class="hinweis">`)

**Wie es weitergeht.** Du kannst jetzt jedes Produkt, jede Verkettung und jeden Quotienten
ableiten — bisher allerdings nur aus Potenzen, Wurzeln und Brüchen gebaut. Der nächste Schritt
bringt keine vierte Regel, sondern neue **Bausteine**: die natürliche Exponentialfunktion mit
<span class="m" data-tex="(\mathrm{e}^{x})' = \mathrm{e}^{x}" data-plain="(eˣ)′ = eˣ"></span> sowie
Sinus und Kosinus. Ab dann leitest du Terme wie
<span class="m" data-tex="x\,\mathrm{e}^{-0{,}5x}" data-plain="x · e^(−0,5x)"></span> oder
<span class="m" data-tex="\frac{\sin x}{x}" data-plain="sin x / x"></span> ab, ohne etwas Neues über
das *Ableiten* zu lernen — du setzt nur andere Funktionen in dieselben drei Regeln ein. Danach folgt
die vollständige Funktionsuntersuchung, in der diese Ableitungen nicht mehr das Ziel sind, sondern
der erste von mehreren Schritten.

---

## Lehrerteil

`<details class="lehrer">` mit `<summary>Für die Lehrkraft</summary>`, am Ende von Abschnitt 6.
Verschwindet beim Drucken (`@media print` des Referenzmoduls, unverändert übernommen).

### Einordnung

Inhaltsfeld **„Funktionen und Analysis"** (Kernlehrplan Mathematik für die gymnasiale Oberstufe
NRW). Q1 umfasst nach der für dieses Projekt maßgeblichen Verteilung die Fortführung der Analysis;
dieses Modul liefert dafür das Werkzeug: die Ableitungsregeln für zusammengesetzte Funktionen.

Prozessbezogene Schwerpunkte sind **Argumentieren** (die beiden Herleitungen in 2.2 und 2.4, die
Aufgaben `a6`, `a7`, `a8`), **Problemlösen** (Regelwahl und Verschachtelung in `a4` und `z1`),
**Modellieren** (`a1`, `a2`, `a3`, `a5`) und **Werkzeuge nutzen** (die beiden Simulationen als
Messinstrument: Es werden Zahlen abgelesen und verglichen, nicht Bilder bewundert).

**Vorausgesetzt** werden aus der Einführungsphase: Potenz-, Faktor- und Summenregel, Ableitung
ganzrationaler Funktionen, Ableitung als lokale Änderungsrate und als Tangentensteigung,
Differenzenquotient und Grenzwertbegriff sowie das Rechnen mit negativen und gebrochenen
Exponenten (<span class="m" data-tex="1/x^{3}=x^{-3}" data-plain="1/x³ = x⁻³"></span>,
<span class="m" data-tex="\sqrt{x}=x^{1/2}" data-plain="√x = x^(1/2)"></span>). Die Vorwissensfragen
`vw1` bis `vw3` prüfen genau diese drei Punkte; wer dort scheitert, scheitert später an der
Kettenregel, ohne dass die Kettenregel die Ursache wäre.

**Bewusst nicht vorausgesetzt** sind die Ableitungen von
<span class="m" data-tex="\sin" data-plain="sin"></span>,
<span class="m" data-tex="\cos" data-plain="cos"></span> und
<span class="m" data-tex="\mathrm{e}^{x}" data-plain="eˣ"></span>. Alle Beispiele und alle zehn
Aufgaben kommen mit Potenzen, Wurzeln und gebrochenrationalen Termen aus. Wird das Modul in einem
Kurs eingesetzt, in dem die e-Funktion bereits eingeführt ist, lassen sich die Aufgaben `a1`, `a2`
und `a4` unverändert stehen lassen und um je ein Beispiel mit
<span class="m" data-tex="\mathrm{e}^{kt}" data-plain="e^(kt)"></span> ergänzen; umgekehrt bricht
nichts, wenn sie noch fehlt.

**Stellung in der Reihe:** vor `mathe-q1-funktionsuntersuchung.html` und vor
`mathe-q1-exponentialfunktionen.html`. Die Reihenfolge ist nicht beliebig — die
Funktionsuntersuchung setzt voraus, dass die erste und die zweite Ableitung eines Produkts ohne
Nachdenken gebildet werden können, sonst verbraucht die Kurvendiskussion ihre Zeit an
Ableitungsfehlern.

*Offen markiert (fachdidaktische Setzungen dieses Moduls, keine Vorgaben des Kernlehrplans):*

- Die Reihenfolge **Produktregel → Kettenregel → Quotientenregel** und die Darstellung der
  Quotientenregel als Folgerung statt als eigenständige vierte Regel. Begründung: Sie macht die
  Herleitung in `a7` zu einer echten Aufgabe und reduziert die Merklast auf zwei Regeln.
- Der Verzicht auf einen vollständigen Beweis der Kettenregel. Der Details-Block in 2.4 benennt die
  Lücke (der Fall <span class="m" data-tex="k=u(x+h)-u(x)=0" data-plain="k = u(x+h) − u(x) = 0"></span>)
  ausdrücklich, statt sie zu verschweigen. Ob dieser Fall im Kurs behandelt wird, ist eine
  Entscheidung der Lehrkraft; für die Klausur ist er nicht relevant, für die Ehrlichkeit des
  Beweisbegriffs schon.
- Die Zuordnung des Moduls an den **Anfang** der Q1. Die Ableitungsregeln können schulintern auch
  am Ende der Einführungsphase liegen. Das ändert an Inhalt und Niveau nichts, wohl aber an der
  Frage, wie viel Zeit für die Herleitungen bleibt.

### Zeitbedarf

Ausgelegt auf eine Doppelstunde von 90 Minuten (die Tabelle im Modul in `<div class="tabelle">`
kapseln):

| Abschnitt | Zeit | Sozialform |
|---|---|---|
| 1 Einstieg (Freibad, drei Vorwissensfragen) | 8 min | Plenum, Fragen in Einzelarbeit |
| 2 Produktregel: Gegenbeispiel, Rechteckbild, Regel, Herleitung, Kettenregel | 25 min | lehrergelenkt, Details-Blöcke je nach Kurs |
| 3 Vertiefung: Quotient, Reziprokenregel, Quotientenregel, Regelwahl | 18 min | Plenum mit zwei Sicherungsphasen |
| 4 Zwei Simulationen mit Beobachtungsaufträgen und drei MC-Fragen | 22 min | Partnerarbeit am Gerät |
| 5 Übungen (Auswahl, siehe Differenzierung) | 12 min | Einzel- oder Partnerarbeit |
| 6 Abschluss, Selbstcheck, Export | 5 min | Plenum |

In 90 Minuten realistisch schaffbar sind die Abschnitte 1 bis 4 vollständig sowie die Aufgaben `a1`
und `a2`. Alles Weitere ist Hausaufgabe oder Material für die Folgestunde. Wer beide Herleitungen
im Plenum entwickelt statt sie lesen zu lassen, braucht dafür allein 20 bis 25 Minuten — dann
entfällt der Übungsteil in der Stunde.

**Schnitt bei zwei Einzelstunden:** nach Abschnitt 2 (Produkt- und Kettenregel). Simulation 1
gehört dann ans Ende der ersten Stunde, Simulation 2 an den Anfang der zweiten; die Quotientenregel
eröffnet die zweite Stunde mit dem Gegenbeispiel
<span class="m" data-tex="x^{2}/x" data-plain="x²/x"></span>.

**Kurzfassung für 45 Minuten** (etwa als Vertretungsstunde oder Wiederholung vor der Klausur):
Einstieg, 2.1 bis 2.4, Simulation 1 mit `sim1`, Aufgaben `a1` und `a2`. Die Quotientenregel
entfällt dann vollständig — sie ist der einzige Abschnitt, der ohne Folgeschaden verschoben werden
kann, weil `a7` sie ohnehin als Folgerung behandelt.

### Typische Schülerfehler — und wo anzuhalten ist

**(1) <span class="m" data-tex="(uv)'=u'v'" data-plain="(uv)′ = u′v′"></span>.** Der Leitfehler
dieses Moduls, und er verschwindet nicht durch einmaliges Nennen. Ursache ist die Übertragung der
Summenregel, die genau so funktioniert („Teile einzeln ableiten und wieder zusammensetzen").
→ **Anhalten** sofort in 2.1, **bevor** die Produktregel steht. Nicht die richtige Regel vorsagen,
sondern <span class="m" data-tex="x\cdot x" data-plain="x · x"></span> an die Tafel schreiben und
den Kurs beide Wege rechnen lassen: 2x gegen 1. Die Erfahrung, dass die eigene Vermutung in fünf
Sekunden widerlegbar ist, trägt länger als jede Warnung. `a6` prüft es später.

**(2) Innere Ableitung vergessen.** <span class="m" data-tex="\big((2x-1)^{3}\big)' = 3(2x-1)^{2}" data-plain="((2x − 1)³)′ = 3(2x − 1)²"></span>
statt <span class="m" data-tex="6(2x-1)^{2}" data-plain="6(2x − 1)²"></span>. Bei innerer Ableitung
1 fällt der Fehler nie auf — deshalb ist in diesem Modul **kein einziges** Beispiel mit innerer
Ableitung 1 gewählt.
→ **Anhalten** nach dem ersten Kettenregel-Beispiel in 2.4. Kontrolle vorführen: ausmultiplizieren
und mit der Potenzregel gegenrechnen (K7). Als Kursregel etablieren: *Bei jeder Kettenregel wird
die innere Ableitung zuerst hingeschrieben, nicht zuletzt.*

**(3) Äußere Ableitung an der falschen Stelle ausgewertet.** Geschrieben wird
<span class="m" data-tex="v'(x)\cdot u'(x)" data-plain="v′(x) · u′(x)"></span> statt
<span class="m" data-tex="v'(u(x))\cdot u'(x)" data-plain="v′(u(x)) · u′(x)"></span>. Sichtbar wird
das erst bei nicht linearen äußeren Funktionen.
→ **Anhalten** beim Merksatz in 2.4 und die Leibniz-Schreibweise danebenstellen. Bei
<span class="m" data-tex="\mathrm{d}A/\mathrm{d}r=2\pi r" data-plain="dA/dr = 2πr"></span> ist
körperlich klar, dass hier der **aktuelle Radius** einzusetzen ist und nicht die Zeit — deshalb
steht Simulation 2 genau an dieser Stelle.

**(4) Wert und Rate werden verwechselt.** In der Produktregel wird
<span class="m" data-tex="u'" data-plain="u′"></span> mit
<span class="m" data-tex="v'" data-plain="v′"></span> multipliziert, weil „da ja Ableitungen
stehen", oder es wird <span class="m" data-tex="r_0" data-plain="r₀"></span> statt
<span class="m" data-tex="r(4)" data-plain="r(4)"></span> eingesetzt (`a2`).
→ **Anhalten** beim Merksatz in 2.3 („die Werte 400 und 5,00 sind hundertmal größer als die
Raten"). Gute Tafelfrage: „Welche der vier Zahlen in
<span class="m" data-tex="u'v+uv'" data-plain="u′v + uv′"></span> hat welche Einheit?" Erst wenn
€/Tag · Personen neben € · Personen/Tag steht, ist der Unterschied gesichert.

**(5) Vorzeichen und Reihenfolge in der Quotientenregel.**
<span class="m" data-tex="uv'-u'v" data-plain="uv′ − u′v"></span> statt
<span class="m" data-tex="u'v-uv'" data-plain="u′v − uv′"></span> — in `a3` als Distraktor −2,4
ausdrücklich abgefangen.
→ **Anhalten** direkt nach dem Merksatz in 3.3. Nicht die Merkformel wiederholen, sondern die
Plausibilitätsprobe einführen: Bei <span class="m" data-tex="f(x)=1/x" data-plain="f(x) = 1/x"></span>
muss die Ableitung negativ sein. Wer das in zehn Sekunden prüft, korrigiert sein Vorzeichen selbst.

**(6) Nenner wird nicht quadriert** oder vorher ausmultipliziert. Beides kostet in der Klausur
Folgepunkte, weil die Nullstellensuche danach nicht mehr funktioniert.
→ **Anhalten** beim durchgerechneten Beispiel in 3.3. Regel für den Kurs: *Der Nenner bleibt als
Quadrat stehen; im Zähler wird zusammengefasst.* Genau das ist auch der Weg, der in `a3` zur
faktorisierten Form <span class="m" data-tex="-20(t-2)(t+2)" data-plain="−20(t − 2)(t + 2)"></span>
und damit sofort zum Maximum führt.

**(7) Falsche Regelwahl bei verschachtelten Termen.** Bei
<span class="m" data-tex="\pi r(t)^{2}h(t)" data-plain="π·r(t)²·h(t)"></span> (`a4`) wird entweder
nur die Produktregel oder nur die Kettenregel angewendet.
→ **Anhalten** in 3.4 und die Frage schriftlich an die Tafel: *Welche Rechenoperation führe ich
zuletzt aus?* Die Aufgabe `z1` ist als Sicherung genau dafür gebaut: vier Funktionen aus denselben
zwei Bausteinen, vier verschiedene Regeln.

**(8) „Die Simulation beweist es."** Nach Abschnitt 4 halten viele die schrumpfenden Eckstücke für
einen Beweis.
→ **Anhalten** beim `.hinweis`-Kasten am Ende von Abschnitt 4. Fünf gemessene Werte zeigen kein
Grenzverhalten. Das ist die Gelegenheit, den Unterschied zwischen Plausibilisierung und Beweis an
einem Beispiel zu klären, das die Lernenden gerade selbst erzeugt haben — und der Grund, warum die
Herleitungen trotz Simulation im Modul stehen.

**(9) Ableitung eines Produkts mit drei Faktoren.** Kommt spätestens bei
<span class="m" data-tex="\pi r^{2}h" data-plain="π·r²·h"></span> auf, wenn
<span class="m" data-tex="\pi" data-plain="π"></span> als dritter Faktor mitgeschleppt wird.
→ **Anhalten** nur kurz: Konstante Faktoren gehören vor die Klammer (Faktorregel), nicht in die
Produktregel. Für echte Dreifachprodukte
<span class="m" data-tex="(uvw)'=u'vw+uv'w+uvw'" data-plain="(uvw)′ = u′vw + uv′w + uvw′"></span>
siehe Differenzierung.

### Differenzierung

**Für schnellere Lernende:**

- **Dreifaktorregel selbst herleiten.** Aus
  <span class="m" data-tex="(uvw)' = \big((uv)w\big)'" data-plain="(uvw)′ = ((uv)·w)′"></span> folgt
  <span class="m" data-tex="u'vw+uv'w+uvw'" data-plain="u′vw + uv′w + uvw′"></span>. Anschlussfrage:
  Wie sieht das Bild dazu aus? (Quader statt Rechteck: drei Platten, drei Kanten, eine Ecke — die
  Terme höherer Ordnung sind hier von zweiter **und** dritter Ordnung.)
- **Verallgemeinerung der Potenzregel.** Aus der Kettenregel und
  <span class="m" data-tex="(g^{n})' = n g^{n-1}g'" data-plain="(gⁿ)′ = n·gⁿ⁻¹·g′"></span> per
  vollständiger Induktion die Aussage für alle
  <span class="m" data-tex="n\in\mathbb{N}" data-plain="n ∈ ℕ"></span> beweisen. Das ist die saubere
  Fassung dessen, was `a8` inhaltlich vorbereitet, und ein guter Anschluss an den
  Erweiterungskurs.
- **Ableitung der Umkehrfunktion.** Aus
  <span class="m" data-tex="f^{-1}(f(x))=x" data-plain="f⁻¹(f(x)) = x"></span> mit der Kettenregel
  <span class="m" data-tex="(f^{-1})'(y) = 1/f'(x)" data-plain="(f⁻¹)′(y) = 1/f′(x)"></span>
  gewinnen und an <span class="m" data-tex="f(x)=x^{2}" data-plain="f(x) = x²"></span>,
  <span class="m" data-tex="x>0" data-plain="x > 0"></span> prüfen (Ergebnis
  <span class="m" data-tex="1/(2\sqrt{y})" data-plain="1/(2√y)"></span>). Das ist die eleganteste
  Anwendung der Kettenregel, die ohne neue Funktionsklassen auskommt.
- **Simulation 1 quantitativ auswerten.** Den Eckanteil über
  <span class="m" data-tex="\Delta t" data-plain="Δt"></span> auftragen lassen (Papier oder
  Tabellenkalkulation): eine Ursprungsgerade mit Steigung
  <span class="m" data-tex="b\,d = -0{,}6" data-plain="b · d = −0,6"></span>. Damit ist die Aussage
  „von erster Ordnung in <span class="m" data-tex="\Delta t" data-plain="Δt"></span>" gemessen und
  nicht behauptet.
- **Zusatzfrage zu `a5`:** Für welche Preisänderungen
  <span class="m" data-tex="b" data-plain="b"></span> liegt das Umsatzmaximum überhaupt im
  betrachteten Zeitraum? (Ansatz
  <span class="m" data-tex="t^{*} = -(b n_0 + p_0 d)/(2bd)" data-plain="t* = −(b·n₀ + p₀·d)/(2·b·d)"></span>
  aus Simulation 1 — die Formel steht im Modul, die Diskussion der Fälle
  <span class="m" data-tex="bd>0" data-plain="b·d > 0"></span> und
  <span class="m" data-tex="bd<0" data-plain="b·d < 0"></span> nicht.)

**Für Lernende, die mehr Zeit brauchen:**

- **Pflichtteil sind `a1`, `a2` und `z1`.** `a1` ist die Produktregel im einfachsten Fall, `a2` die
  Kettenregel im einfachsten Fall, und `z1` verlangt keine einzige eigene Rechnung, trägt aber die
  zentrale Einsicht zur Regelwahl. Von den drei AB-III-Aufgaben genügt `a6`: Sie hängt an einem
  einzigen Gegenbeispiel, während `a7` eine vollständige Herleitung und `a8` eine Fallunterscheidung
  verlangt.
- **Die beiden Details-Blöcke überspringen.** Das Rechteckbild in 2.2 und die Simulationen tragen
  die Einsicht auch ohne die Grenzwertrechnung; die Herleitung lässt sich in der Folgestunde
  nachholen, wenn die Regel handwerklich sitzt.
- **Ableitungsbaustein-Übung vorschalten.** Fünf Terme, zu denen nur die *Regel* genannt werden
  soll, ohne zu rechnen: <span class="m" data-tex="x^{2}(x+1)" data-plain="x²(x + 1)"></span> ·
  <span class="m" data-tex="(x+1)^{5}" data-plain="(x + 1)⁵"></span> ·
  <span class="m" data-tex="\frac{x}{x+1}" data-plain="x/(x + 1)"></span> ·
  <span class="m" data-tex="\sqrt{3x}" data-plain="√(3x)"></span> ·
  <span class="m" data-tex="3x^{2}+x" data-plain="3x² + x"></span> (der letzte braucht **keine** der
  neuen Regeln — genau darum geht es).
- **Die Selbstkontrolle explizit machen.** Zwei der vier Funktionen in `z1` lassen sich ohne jede
  neue Regel prüfen: <span class="m" data-tex="x^{3}(2x+1)=2x^{4}+x^{3}" data-plain="x³(2x + 1) = 2x⁴ + x³"></span>
  und <span class="m" data-tex="(2x+1)/x^{3}=2x^{-2}+x^{-3}" data-plain="(2x + 1)/x³ = 2x⁻² + x⁻³"></span>.
  Wer das einmal vorgeführt bekommt, hat ein Kontrollverfahren für jede Klausur.
- **Hilfestufe 2 vorab freigeben.** Bei `a3` und `a4` ist der Ansatz die eigentliche Hürde, nicht
  die Rechnung. Wird Stufe 2 von vornherein gelesen, bleibt die Aufgabe trotzdem eine Aufgabe.

### Bezug zu Realexperimenten und Daten

- **Das Rechteck aus Papier.** Ein DIN-A4-Blatt, zwei Schnitte: Ein Streifen oben, ein Streifen
  rechts, ein kleines Eck bleibt doppelt. Die drei Teile lassen sich wiegen oder ausmessen — das
  Eckstück ist bei 5 % Zuwachs in beide Richtungen gerade 0,25 % der Fläche. Das ist die
  Produktregel zum Anfassen und in zwei Minuten gemacht. Aufwand: eine Schere.
- **Öltropfen oder Tinte auf Löschpapier.** Ein Tropfen auf saugfähigem Papier breitet sich
  annähernd kreisförmig aus. Mit Handyvideo und Lineal wird der Radius alle fünf Sekunden gemessen,
  daraus <span class="m" data-tex="\mathrm{d}r/\mathrm{d}t" data-plain="dr/dt"></span> und
  <span class="m" data-tex="\mathrm{d}A/\mathrm{d}t" data-plain="dA/dt"></span> bestimmt. Die
  Lernenden sehen, dass die Flächenrate wächst, obwohl die Radiusrate sinkt — und dass die
  Kettenregel beides verbindet. (Anders als in Simulation 2 ist
  <span class="m" data-tex="r(t)" data-plain="r(t)"></span> hier **nicht** linear; genau das macht
  es zum ehrlichen Experiment.)
- **Fahrrad-Übersetzung.** Die Kettenregel im Wortsinn: Kettenblatt 50 Zähne, Ritzel 25, Rad 28
  Zoll. Umdrehungen pro Minute an der Kurbel, am Rad, daraus die Geschwindigkeit. Die
  Übersetzungsverhältnisse multiplizieren sich — dieselbe Struktur wie
  <span class="m" data-tex="\mathrm{d}y/\mathrm{d}x = \mathrm{d}y/\mathrm{d}u\cdot\mathrm{d}u/\mathrm{d}x" data-plain="dy/dx = dy/du · du/dx"></span>,
  nur mit konstanten Faktoren. Gut als Einstieg in 2.4, wenn der Kurs mit dem Getriebebild wenig
  anfangen kann.
- **Echte Preis-Absatz-Daten.** Schulkiosk, Mensa oder Schülerzeitung: Preis und Absatz über
  mehrere Wochen protokollieren. Schon zehn Datenpunkte reichen, um zu zeigen, dass die
  Umsatzänderung nicht das Produkt der beiden Änderungen ist. Das Modell aus dem Einstieg ist
  bewusst linear gehalten; die Diskussion, warum reale Daten das nicht sind, gehört in die
  Modellierungskritik.
- **Kondensator oder Kochtopf (Anschluss Physik).** Sobald die e-Funktion eingeführt ist, liefert
  jeder Abkühl- oder Entladevorgang ein Produkt aus Polynom und Exponentialfunktion. Eine Absprache
  mit der Physik-Fachschaft lohnt sich: Dort wird
  <span class="m" data-tex="U(t)=U_0\mathrm{e}^{-t/RC}" data-plain="U(t) = U₀·e^(−t/RC)"></span>
  abgeleitet, oft ohne dass der Faktor
  <span class="m" data-tex="-1/RC" data-plain="−1/RC"></span> als innere Ableitung benannt wird.
- **CAS/GTR.** Sinnvoll erst **nach** dieser Stunde, und dann in genau einer Rolle: als
  Kontrollinstanz. Wer `derive` kennt, bevor er die Regeln kennt, hält das Ableiten für eine Taste.
  Ein guter Einsatz ist die Gegenprobe der eigenen Ergebnisse in `a3` und `a4` — und die Erfahrung,
  dass das Werkzeug eine andere, algebraisch gleichwertige Form ausgibt als der eigene Zettel. Die
  Frage „Sind das dieselben Terme?" ist mathematisch ergiebiger als das Ergebnis selbst.

---

## Checkliste für den Bauagenten

### Benötigte Aufgabenbausteine und ihre Schlüssel

| Schlüssel | Baustein | `data`-Attribut | Optionen / Besonderheit | AB |
|---|---|---|---|---|
| `vw1` | Multiple Choice | `data-mc="vw1"` | 3 Optionen, `r: 1` | — |
| `vw2` | Multiple Choice | `data-mc="vw2"` | 3 Optionen, `r: 0` | — |
| `vw3` | Multiple Choice | `data-mc="vw3"` | 3 Optionen, `r: 2` | — |
| `sim1` | Multiple Choice | `data-mc="sim1"` | **4** Optionen, `r: 1` | II |
| `sim2` | Multiple Choice | `data-mc="sim2"` | **4** Optionen, `r: 2` | II |
| `sim3` | Multiple Choice | `data-mc="sim3"` | **4** Optionen, `r: 0` | II |
| `a1` | Zahleneingabe | `data-num="a1"` | `wert: 155`, `"m²/Jahr"`, `tol: 0.5`, kein `alt` | I |
| `a2` | Zahleneingabe | `data-num="a2"` | `wert: 100.53`, `"cm³/s"`, `tol: 0.15`, kein `alt` | I |
| `mc1` | Multiple Choice | `data-mc="mc1"` | **4** Optionen, `r: 1` | II |
| `a3` | Zahleneingabe | `data-num="a3"` | `wert: 2.4`, `"mg/(L·h)"`, `tol: 0.02`, kein `alt` | II |
| `a4` | Zahleneingabe | `data-num="a4"` | `wert: 62.83`, `"cm³/s"`, `tol: 0.1`, kein `alt` | II |
| `z1` | Zuordnung | `data-check="zuordnung"` | 4 **Formelkarten** statt SVG, Lösung **D · C · B · A** | II |
| `a5` | Zahleneingabe | `data-num="a5"` | `wert: 20`, `"Tage"`, `tol: 0.2`, `alt: 480 "Stunden"` | II |
| `a6` | offene Aufgabe | `data-loesung="a6"` | `<textarea>`, Musterlösung in `data-stufe="9"` | III |
| `a7` | offene Aufgabe | `data-loesung="a7"` | `<textarea>`, Musterlösung in `data-stufe="9"` | III |
| `a8` | offene Aufgabe | `data-loesung="a8"` | `<textarea>`, Musterlösung in `data-stufe="9"` | III |

Verteilung der Anforderungsbereiche in Abschnitt 5: **I** `a1`, `a2` · **II** `mc1`, `a3`, `a4`,
`z1`, `a5` · **III** `a6`, `a7`, `a8`. Damit sind zehn Übungsaufgaben vorhanden, drei davon im
Anforderungsbereich III als Begründungs- bzw. Bewertungsaufgaben mit Musterlösung **und**
Bewertungskriterien.

**Dreistufige Hilfen** (`data-hilfe="1|2|3"` plus `.hilfe-text[data-stufe="1|2|3"]`) bekommen:
`a1`, `a2`, `a3`, `a4`, `a5`, `a6`, `a7`, `a8`. Bei den drei offenen Aufgaben ist Stufe 3 eine
**Strukturhilfe** (Gliederung der Antwort), keine Rechnung — die Rechnung steht in Stufe 9.

`mc1` und `z1` bekommen **keine** Hilfestufen, wie im Referenzmodul: Dort trägt das
Distraktor-Feedback bzw. die Teilerfolgs-Rückmeldung die Hilfefunktion. *Als offene Entscheidung
markiert:* Wenn die Fachkonferenz auf dreistufiger Hilfe bei **jeder** Übung besteht, bekommt `z1`
zusätzlich Tipp/Ansatz/Lösungsweg nach dem Muster „äußerste Rechenoperation bestimmen" →
„drei Regeln nebeneinanderstellen" → „zwei der vier Ableitungen durch Umformen kontrollieren".

### Anpassungen an der kopierten Engine

1. **Zuordnungs-Engine:** `ergebnisse.a3 = (n === zeilen.length);` wird zu
   `ergebnisse.z1 = (n === zeilen.length);`. Sonst überschreibt die Zuordnung das Ergebnis der
   Zahleneingabe `a3`. (Siehe 6.4.)
2. **MC-Engine:** unverändert, aber vier der sieben MC-Aufgaben haben **vier** Optionen. Die
   `fb`-Arrays müssen genau vier Einträge haben, `data-i` läuft lückenlos 0…3, und `name` des
   Radios ist gleich dem Wert von `data-mc`.
3. **Zuordnungskarten:** Die `<figure>`-Elemente enthalten hier `<div class="m block">` statt
   Inline-SVG. `formelnRendern()` läuft beim Laden über alle `.m`-Elemente, ein Nachruf ist nicht
   nötig, solange die Karten statisch im Markup stehen.
4. **Zwei Simulations-IIFEs** statt einer, jede mit eigenem Zustand; gemeinsamer globaler Zustand
   bleibt allein `ergebnisse`.
5. **Farbtokens:** `--akzent: #0d7a52`, `--akzent-hell: #e7f6ef`, `--akzent-rand: #b5e0cd`, dazu der
   Verlauf in `header.kopf`. Sonst bleibt der `<style>`-Block unverändert.
6. **Drei `<table>`-Elemente** im Modul (Zerlegungstabelle in 2.4, Regelwahltabelle in 3.4,
   Zeitbedarfstabelle im Lehrerteil) — jede in `<div class="tabelle">`.
7. **Vier `<details>`-Blöcke** mit Herleitungen: Produktregel (2.2), Kettenregel mit benannter Lücke
   (2.4), Reziprokenregel (3.2), Quotientenregel (3.3).

### Simulationsbausteine

**Simulation 1 — Umsatzrechteck (`cvRecht`, `cvU`), eigene IIFE, mit `requestAnimationFrame`:**

| Element | `id` | Bereich / Werte |
|---|---|---|
| Canvas Rechteck | `cvRecht` | `width="1000" height="440"`, `OX=90`, `OY=390`, `SX=1.4`, `SY=24` |
| Canvas Umsatzkurve | `cvU` | `width="1000" height="280"`, `AX0=90`, `AX1=950`, `AY0=250`, `AY1=50` |
| Regler `t` | `rT` | 0…210, Schritt 1 → `t = Wert/10`, Start **0** |
| Regler `Δt` | `rDt` | 1…16, Schritt 1 → `Δt = Wert·0,25`, Start **4** |
| Regler `b` | `rB` | −15…30, Schritt 1 → `b = Wert/100`, Start **10** |
| Regler `d` | `rD` | −12…8, Schritt 1, direkt, Start **−6** |
| Knöpfe | `bPlay`, `bMax`, `bReset` | Animation 2,0 Tage/s bis `t = 21`; `dtFrame = Math.min(0.05, …)` |
| Anzeigen | `anzT`, `anzP`, `anzN`, `anzU`, `anzBp`, `anzBn`, `anzUs`, `anzSek`, `anzEck` | Stellen und Startwerte in 4.A.6 |

**Simulation 2 — Ölring (`cvKette`), eigene IIFE, ohne Animation:**

| Element | `id` | Bereich / Werte |
|---|---|---|
| Canvas | `cvKette` | `width="1000" height="340"`, `MX=240`, `MY=170`, Maßstab 1 m = 1 px, Balken ab `BX=480`, `BW=460` |
| Regler `r₀` | `rR0` | 2…20, Schritt 1, direkt in m, Start **5** |
| Regler `c` | `rC` | 1…20, Schritt 1 → `c = Wert/10`, Start **5** |
| Regler `t` | `rTk` | 0…100, Schritt 1 → `t = Wert/2`, Start **40** |
| Regler `Δt` | `rDtk` | 1…8, Schritt 1 → `Δt = Wert·0,25`, Start **4** |
| Knopf | `bResetK` | setzt alle vier Regler auf die Startwerte |
| Anzeigen | `anzR`, `anzA`, `anzDAdr`, `anzDrdt`, `anzDAdt`, `anzRingEx`, `anzRingNa`, `anzFehler` | Stellen und Startwerte in 4.B.4 |

Zwei `.auftrag`-Kästen (4.A.7 und 4.B.5), drei MC-Fragen danach (`sim1`, `sim2` nach Simulation 1;
`sim3` nach Simulation 2), ein `.hinweis`-Kasten am Ende von Abschnitt 4.

### Prüfpunkte vor der Abnahme

1. **Simulation 1, Startzustand** (`t = 0`, `Δt = 1,00`, `b = 0,10`, `d = −6`) zeigt exakt:
   5,00 € · 400,0 · 2000,00 € · Preisbeitrag 40,00 · Mengenbeitrag −30,00 · U′ 10,00 ·
   Sekante 9,40 · Eckanteil −0,60 (K12). Legende: −30,00 € · +40,00 € · −0,60 €.
2. **Simulation 1, zweiter Testfall** `t = 12,0`, `Δt = 0,50`: 6,20 € · 328,0 · 2033,60 € ·
   32,80 · −37,20 · **−4,40** · −4,70 · −0,30 (K14).
3. **Identitätstest** (als Konsolen-Selbsttest beim Bauen, danach entfernen): In jedem
   Reglerzustand gilt Sekante = Preisbeitrag + Mengenbeitrag + Eckanteil auf drei Nachkommastellen.
4. **Knopf „Zum Umsatzmaximum"** setzt bei Startwerten auf `t = 8,3` Tage; dort stehen +35,00 und
   −35,00 €/Tag, U′ ≈ 0,00 (K15). Bei `b = 0` oder `d = 0` erscheint stattdessen die Textmeldung.
5. **Δt-Reihe** bei `t = 0`: Sekante 7,60 · 8,80 · 9,40 · 9,70 · 9,85 für Δt = 4,00 · 2,00 · 1,00 ·
   0,50 · 0,25; Eckanteil jeweils −2,40 · −1,20 · −0,60 · −0,30 · −0,15 (K13).
6. **Simulation 2, Startzustand** (`r₀ = 5`, `c = 0,5`, `t = 20,0`, `Δt = 1,00`): 15,000 m ·
   706,858 m² · 94,2478 m · 0,50 m/s · 47,1239 m²/s · Ring exakt 47,90929 · Näherung 47,12389 ·
   Differenz 0,78540 m² (1,639 %) (K16).
7. **Simulation 2, Fehlerreihe** für Δt = 2,00 · 1,00 · 0,50 · 0,25: Differenz 3,14159 · 0,78540 ·
   0,19635 · 0,04909 m², relativ 3,226 % · 1,639 % · 0,826 % · 0,415 % (K17). Zweiter Testfall
   `r₀ = 10`, `c = 1,2`, `t = 30,0`, `Δt = 0,50`: 46,000 m · 6647,610 m² · 289,0265 m ·
   346,8318 m²/s · Differenz 1,13097 m².
8. **Randlage prüfen:** `r₀ = 20`, `c = 2,0`, `t = 50,0` ergibt `r = 120 m`; der Kreis muss mit
   `MX = 240`, `MY = 170` vollständig im Canvas liegen und darf die Balken ab `BX = 480` nicht
   überlappen.
9. **Jede Zahleneingabe in allen vier Fällen testen** (richtig · richtige Zahl mit falscher
   Einheit · `nah` · `weit`). Die zu erwartende Zone jedes Distraktors steht in **K29**; bei `a5`
   zusätzlich die Alternativeinheit 480 Stunden mit geerbter Toleranz 4,8 h.
10. **Zuordnung in beiden Richtungen prüfen:** vollständig richtig (D · C · B · A) und teilweise
    richtig; beide Rückmeldungstexte müssen erscheinen, und `ergebnisse.z1` muss gesetzt werden.
11. **Alle drei Hilfestufen** jeder der acht Aufgaben mit Hilfen öffnen und schließen; bei `a6`,
    `a7`, `a8` zusätzlich die Musterlösung über `data-loesung`.
12. **`data-plain` überall gefüllt** und ohne LaTeX-Reste: Unicode für `Δ`, `π`, `√`, `·`, `−`,
    `⁻³`, `′`, `≈`, `⟹`. Test mit abgeschaltetem Netz.
13. **Kein waagerechtes Scrollen** bei 1280, 900 und 390 px; die drei Tabellen stehen in
    `<div class="tabelle">`, beide Canvas auf `width:100%`.
14. **Druckansicht** enthält Aufgabentexte, aber keine Regler, Knöpfe und keinen Lehrerteil.
15. **Export** listet die 13 Schlüssel aus 6.4 und hängt die Texte der drei `<textarea>` an.
16. `PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/mathe-q1-ableitungsregeln.html"`
    meldet weder `blocker` noch `maengel`.
17. Eintrag in `fachliches/modulliste.md` erst danach von `in Arbeit` auf `fertig` setzen.

### Quelle der Kontrollrechnungen

Alle Zahlenwerte dieses Dokuments stehen gesammelt in Abschnitt 0 (**K1** bis **K29**). Sie wurden
symbolisch mit `sympy` (exakte Brüche, `simplify`/`factor` für die Identität zweier Ableitungsformen)
und numerisch gegengeprüft; die Herleitungsidentitäten K11 und K26 sind als exakte Null bestätigt,
nicht als kleine Zahl. Der Bauagent muss nichts nachrechnen, sollte aber jede Zahl, die er in die
HTML-Datei schreibt, gegen diese Liste abgleichen.

Nachgerechnet und bestätigt wurden insbesondere: K1, K13, K14 (Freibadmodell und Δt-Reihe),
K16, K17 (Ölring, alle vier Zeilen und beide Zusatzfälle), K18 bis K23 (alle Übungsaufgaben mit
Zahlenergebnis), K24, K25, K27 und K28 (Stichproben der Erklär- und Vertiefungsbeispiele).

---

## Anmerkung zur Hilfsdatei `inhalte/_bau_basis.md`

`_bau_basis.md` ist eine **wortgleiche Kopie der Zeilen 1–213 dieser Datei** (Kopfdaten und
Abschnitt 0 mit den Kontrollrechnungen K1–K29); die Inhalte sind korrekt, aber vollständig
redundant. Sie enthält nichts, was hier nicht steht. Nach Fertigstellung des Moduls kann sie
gelöscht werden — solange sie liegen bleibt, besteht die Gefahr, dass jemand die Kontrollrechnungen
dort pflegt und die Fassung in dieser Datei veraltet.

<!-- FORTSCHRITT: VOLLSTAENDIG: Abschnitte 0-6, Lehrerteil, Checkliste, Anmerkung zu _bau_basis.md; zuletzt fertig: Checkliste fuer den Bauagenten; als Naechstes: nichts offen - Datei kann an den Bauagenten uebergeben werden -->
