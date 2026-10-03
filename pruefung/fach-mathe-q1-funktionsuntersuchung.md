# Fachprüfung `module/mathe-q1-funktionsuntersuchung.html`

Prüfdatum: 20.09.2026 · Prüfgrundlage: Modul, `inhalte/mathe-q1-funktionsuntersuchung.md`,
`inhalte/_bauprotokoll-funktionsuntersuchung.md`, `fachliches/kernlehrplan-nrw.md`,
`module/physik-q1-induktion.html` (Referenz).
Alle Zahlenwerte mit sympy/exakten Brüchen nachgerechnet, die Simulation als Python-Portierung
gegen sympy über **jede** Reglerstellung geprüft. Am Modul wurde nichts geändert.

## Urteil

**Nacharbeit nötig** — aber nur an Texten, nicht an der Mathematik.

Kein einziger Zahlenwert ist falsch, keine Formel steht außerhalb ihres Gültigkeitsbereichs, der
Lehrplanbezug ist echt und wörtlich, die Simulation rechnet exakt. Was fehlt, sind vier
Textstellen, die nicht zueinander passen (Lehrerteil gegen Aufgabe 1, Einstiegsnarrativ gegen
Schar 1, Rückmeldungszonen gegen die geänderte Zahlen-Engine) und eine Lücke im Übungsteil
(Ortskurve und Fallunterscheidung werden gelehrt und im Selbstcheck behauptet, aber nicht geübt).
Der Aufwand für die Nacharbeit liegt bei einer knappen Stunde.

---

## Schwere Fehler

**Keine.** Geprüft und nicht gefunden wurden: falsche Zahlenwerte (52 Einzelwerte nachgerechnet,
alle richtig), inkonsistente Vorzeichen, erfundene Kernlehrplan-Zitate, Formeln außerhalb ihres
Gültigkeitsbereichs, zu großzügige Toleranzen, als AB III ausgewiesene Rechenaufgaben.

Drei Punkte, an denen ein schwerer Fehler zu erwarten gewesen wäre und keiner vorliegt:

- **Chip "Inhaltsfeld: Funktionen und Analysis"** steht wörtlich so in
  `fachliches/kernlehrplan-nrw.md` (Mathematik LK, Inhaltsfeld 1). Die Q1-Verortung ist dort
  ebenfalls belegt: "Q1 umfasst die Fortführung der Analysis (Ableitungsregeln,
  **Funktionsuntersuchung**, …)". Der Lehrerteil zitiert **keine** Kompetenzformulierung und
  markiert die offene Frage (Einführungsphase oder Q1) ausdrücklich als Rückfrage an die
  Fachkonferenz, statt sie zu raten. Genau so ist es vorgeschrieben.
- **Beide AB-III-Aufgaben sind echte AB III.** `a6` (Schülerlösung beurteilen) und `a7`
  (Behauptung widerlegen, Existenzbereich begründen) verlangen Beurteilen und Begründen mit
  Gegenbeispiel, nicht eine längere Rechnung, und beide haben Musterlösung **und**
  Bewertungskriterien. Die sonst häufigste Beanstandung entfällt hier.
- **Die Umstellung der Zahlen-Engine auf den vorzeichenbehafteten Quotienten wirkt korrekt**
  an allen fünf Zahleneingaben (Nachweis unten). Ohne sie wären +7 bei `a2` und −12 bei `a5`
  als "fast richtig" durchgegangen.

---

## Mängel

### M1 — Lehrerteil widerspricht Aufgabe 1 · Schweregrad: **mittel**

**Fundstelle:** HTML Z. 840 (Lehrerteil, typischer Schülerfehler 3); gespiegelt aus
`inhalte/mathe-q1-funktionsuntersuchung.md` Z. 1476.

> "Antwort 'T(3)' oder '−4' statt 'T(3 | −4)'. Beim Tiefpunkt der ersten Aufgabe in der
> Rückmeldung darauf bestehen: Nur die Angabe des Punkts beantwortet die Frage nach dem Punkt."

Die erste Aufgabe fragt nach der **y-Koordinate** des Tiefpunkts (Z. 524), und die richtige
Antwort ist dort genau −4. Die Zahlen-Engine kann gar nichts anderes entgegennehmen. Die
Lehrkraft wird also aufgefordert, die richtige Antwort als unvollständig zu behandeln. Das ist
ein Folgefehler aus der Inhaltsdatei: Der Fehlertyp ist real und wichtig, nur die Verankerung
an `a1` ist falsch gewählt.

**Korrekturvorschlag:** Bezug auf `a1` umdrehen, etwa: "Bei `a1` liegt der Fall umgekehrt: Dort
ist ausdrücklich nur die y-Koordinate gefragt. Nutze das für die Begriffsunterscheidung — lass
mündlich den vollständigen Punkt T(3 | −4) nachliefern und halte daneben, was die Aufgabe
verlangt hat."

### M2 — Rückmeldungstexte von `a1` nach der Engine-Umstellung nicht nachgezogen · Schweregrad: **mittel**

**Fundstelle:** HTML Z. 951 (`a1.nah`) und Z. 952 (`a1.weit`), Engine Z. 1006–1014.

Seit der Quotient vorzeichenbehaftet gebildet wird, ist die nah-Zone von `a1` (Soll −4) das
Intervall (−8; −2) — **ausschließlich negative Werte**. Ein reiner Vorzeichenfehler (+4,
Quotient −1,00) landet jetzt in der weit-Zone.

- Der nah-Text beginnt aber mit "Du bist in der Nähe, aber es steckt ein Einsetz- oder
  **Vorzeichenfehler** drin." Ein Vorzeichenfehler kann in dieser Zone nicht mehr vorkommen.
- Der weit-Text erklärt nur 0 und 3. Wer +4 eingibt — der plausibelste Fehler bei einem
  negativen Sollwert — bekommt die Erklärung zu einem Fehler, den er nicht gemacht hat.

Bei `a2` ist dieselbe Umstellung **vorbildlich** nachgezogen worden ("+7 hat das falsche
Vorzeichen: …"). Nur `a1` wurde vergessen.

**Korrekturvorschlag:** In `a1.weit` ergänzen: "+4 ist das richtige Ergebnis mit falschem
Vorzeichen: 27 − 54 = −27, plus 27 ergibt 0, minus 4 ergibt −4 — der Tiefpunkt liegt unterhalb
der x-Achse." In `a1.nah` das Wort "Vorzeichen-" streichen.

### M3 — Einstiegsnarrativ gilt für Schar 2, nicht für die zuerst sichtbare Schar 1 · Schweregrad: **mittel**

**Fundstelle:** HTML Z. 206 (Einstieg) gegen Z. 446 und Z. 1096 (Simulation, Schar 1).

Der Einstieg verspricht: "Bei kleinem *a* gibt es Kuppe und Senke, bei **größerem** *a*
verschwinden beide." Für die verdeckte Schar, mit der `sim1` arbeitet
(f_a(x) = x³/3 − x² + a·x), stimmt das exakt: Extrempunkte für a < 1, keine für a > 1, und a ist
dort sogar die Anfangssteigung f_a′(0) = a, wie der Einstieg sagt.

Beim Öffnen des Moduls ist aber **Schar 1** eingestellt, f_a(x) = x³/3 − a·x mit sichtbarer
Formel, und die verhält sich genau umgekehrt: a ≤ 0 → keine Extrempunkte, a > 0 → Hoch- und
Tiefpunkt bei ∓√a. Wer den Einstieg gelesen hat und als Erstes den Regler von Schar 1 bewegt,
sieht das Gegenteil dessen, was ihm angekündigt wurde.

**Korrekturvorschlag:** Im Einstieg neutral formulieren ("Für einen Teil der *a*-Werte gibt es
Kuppe und Senke, für den anderen keine von beiden, und dazwischen liegt ein Sonderfall"), oder
in Abschnitt 4 einen Satz ergänzen: "Achtung, bei Schar 1 ist es andersherum als im Einstieg —
prüfe selbst, für welche *a* es Extrempunkte gibt."

### M4 — Ortskurve und Fallunterscheidung werden gelehrt und im Selbstcheck behauptet, aber nicht geübt · Schweregrad: **mittel**

**Fundstelle:** Abschnitt 3.2 und 3.3 (Z. 359–401), Selbstcheck Z. 806, Übungen Z. 522–766.

Der Selbstcheck verlangt: "Ich kann bei Funktionenscharen nach x ableiten,
**Fallunterscheidungen durchführen**, Parameter aus Bedingungen bestimmen und **Ortskurven
berechnen**." Im Übungsteil kommt beides nicht als Pflichtaufgabe vor:

- Ortskurve: nur als freiwilliger Zusatz in `a7` und als Zusatzauftrag der Simulation.
- Fallunterscheidung (Hochpunkt wird zu Tiefpunkt je nach Parametervorzeichen): gar nicht.
  `a5` ist eine Diskriminantenaufgabe, `a7` eine Existenzaufgabe.

Für ein LK-Modul, dessen Vertiefung genau diese beiden Techniken sind, ist das die spürbarste
Lücke — und es ist die Technik, die im Zentralabitur am zuverlässigsten abgefragt wird.

**Korrekturvorschlag:** Eine Übung im AB II ergänzen, etwa zu f_t(x) = x³ − 3t·x² aus 3.2 (alle
Werte liegen in K5 der Inhaltsdatei nachgerechnet vor): "Bestimme die Extrempunkte von f_t in
Abhängigkeit von t mit vollständiger Fallunterscheidung und gib die Ortskurve der beweglichen
Extrempunkte an." Lösung: t > 0 → H(0 | 0), T(2t | −4t³); t < 0 umgekehrt; t = 0 → Sattelpunkt;
Ortskurve y = −x³/2.

### M5 — `vw3`: die richtige Option enthält eine Aussage, die aus der Voraussetzung gerade nicht folgt · Schweregrad: **gering**

**Fundstelle:** HTML Z. 233–237.

Der Stamm lautet "Für f(x) = x² − 4x gilt f′(3) = 2. Was **folgt daraus** für den Graphen bei
x = 3?", die richtige Option 0 lautet "Der Graph steigt dort, obwohl er unterhalb der x-Achse
verläuft." Der zweite Halbsatz ist für diese Funktion wahr (f(3) = −3), folgt aber nicht aus
f′(3) = 2 — und genau mit dieser Begründung wird Option 2 als falsch zurückgewiesen. In einer
Aufgabe, die das Auseinanderhalten von Steigung und Funktionswert prüft, ist diese Unschärfe im
Stamm ungünstig; die Rückmeldung repariert es inhaltlich sauber.

**Korrekturvorschlag:** Stamm ändern in "Welche Aussage über den Graphen bei x = 3 ist richtig?"

### M6 — doppeltes `</style>` · Schweregrad: **gering**

**Fundstelle:** HTML Z. 180 und 181. Das zweite Endtag ist ein Bauartefakt (die Referenz hat nur
eines). Browser ignorieren es, der Modulcheck schlägt nicht an, aber die Datei ist damit nicht
valide. Zeile 181 ersatzlos streichen.

### M7 — Verständnisfragen: Antwortlänge und Marker verraten zu viel · Schweregrad: **gering**

**Fundstelle:** `sim2` Z. 496–499; Marker-Logik Z. 1132–1156.

(a) In `sim2` ist die richtige Option (Index 1) mit deutlichem Abstand die längste und die
einzige mit Klammerbegründung — ein Test-Wiseness-Hinweis, der die Aufgabe teilweise ohne
Simulation lösbar macht. Die Distraktoren 0 und 2 ließen sich um je einen Begründungshalbsatz
verlängern.

(b) Die Simulation beschriftet die Punktsorte selbst (H/T/W/**S**). Damit ist "Für a ≠ 0 liegt
dort ein Sattelpunkt" ablesbar, ohne über den Vorzeichenwechsel nachzudenken. AB II bleibt
vertretbar, weil die Distraktoren mehrere Reglerstellungen verlangen; die eigentliche
Denkleistung erzwingt aber erst der Beobachtungsauftrag ("Schau in beiden Bändern, ob f′ bei
x = 0 das Vorzeichen wechselt"). Beide Fragen sind — das ist der Kern der Prüffrage — **nicht**
ohne die Simulation lösbar, weil die Formeln der Scharen 2 und 3 nirgends im sichtbaren Text
stehen (geprüft: Klartext nur im JS-Kommentar bei `FORMELN_SICHTBAR = false`, in der Rückmeldung
zur richtigen Option und im Lehrerteil).

### M8 — `a3`: der Tipp nimmt die Pointe vorweg · Schweregrad: **gering**

**Fundstelle:** HTML Z. 611: "Ein Zeitraum ist ein abgeschlossenes Intervall. Wo kann der größte
Wert liegen, außer an einer Stelle mit waagerechter Tangente?" Damit ist die einzige Hürde der
Aufgabe (Randextremum) schon auf Stufe 1 genommen, Stufe 2 fügt nichts Neues hinzu. Alle anderen
acht Übungen sind sauber gestuft.
**Korrekturvorschlag:** Stufe 1 auf "Was bedeutet die Angabe 0 ≤ t ≤ 5 für deine Kandidatenliste?"
zurücknehmen.

### M9 — weit-Texte decken nicht alle erreichbaren weit-Werte ab · Schweregrad: **gering**

**Fundstelle:** `a3` Z. 962, `a4` Z. 967, `a5` Z. 972.

Erreichbare, plausible Eingaben, die in die weit-Zone fallen und im Text nicht vorkommen:
`a3` → 4 (Quotient genau 2,00), `a4` → 12, `a5` → 6. Der Lernende bekommt dann die Erklärung zu
einem fremden Fehler. Der jeweils letzte Satz ist allgemein gehalten, sodass kein falscher
Hinweis entsteht — es fehlt nur der passende.
**Korrekturvorschlag:** je einen Halbsatz ergänzen oder mit "Falls du auf einen anderen Wert
gekommen bist: …" abschließen.

### M10 — fachsprachliche Unschärfe in der `sim2`-Rückmeldung · Schweregrad: **gering**

**Fundstelle:** HTML Z. 919: "… und der Faktor (x − a) in der Nähe von 0 **konstant**".
Gemeint und richtig ist **vorzeichenkonstant**; konstant ist der Faktor nicht. In einem Modul,
dessen erklärtes Ziel die Unterscheidung "Null" gegen "Vorzeichenwechsel" ist, sollte gerade
dieses Wort stimmen.

---

## Nachgerechnet

Alle Werte mit sympy (exakte Brüche) bzw. in der angegebenen Genauigkeit. "Datei" = der im Modul
angegebene Wert.

### Erklärteil und Vertiefung

| Stelle | Größe | Eigenes Ergebnis | Datei | |
|---|---|---|---|---|
| 2.5 | f′(x) faktorisiert | 4x(x−1)(x−2) | 4x(x−1)(x−2) | ok |
| 2.5 | f″(0), f″(1), f″(2) | 8, −4, 8 | 8, −4, 8 | ok |
| 2.5 | Extrempunkte | T1(0/0), H(1/1), T2(2/0) | dito | ok |
| 2.5 | Wendestellen | 1 ∓ √3/3 = 0,4226 / 1,5774 | 0,423 / 1,577 | ok |
| 2.5 | y-Wert beider Wendepunkte | 4/9 = 0,4444 | 4/9 ≈ 0,444 | ok |
| 2.5 | Steigung der Wendetangenten | ±8√3/9 = ±1,5396 | ±1,54 | ok |
| 2.5 | f‴ an den Wendestellen | ∓8√3 = ∓13,856 | ∓13,86 | ok |
| 2.5 | Symmetrie f(2−x) − f(x) | 0 | achsensymmetrisch zu x = 1 | ok |
| 2.5 | f(−1), f(3) | 9, 9 | 9 | ok |
| 2.2 | f′(0,1), f′(−0,1) | 0,684; −0,924 | 0,684; −0,924 | ok |
| 2.2 | Differenzenquotienten | 6,84; 9,24 | 6,84; 9,24 | ok |
| 2.3 | x⁵: f‴(0) = 0, f″ = 20x³ mit VZW | bestätigt | bestätigt | ok |
| 3.2 | f_t′, f_t″, f_t‴ | 3x(x−2t), 6(x−t), 6 | dito | ok |
| 3.2 | f_t(2t), f_t″(0), f_t″(2t) | −4t³, −6t, 6t | dito | ok |
| 3.2 | Wendepunkt, Steigung | W(t / −2t³), m = −3t² | dito | ok |
| 3.2 | Probe t = 2 | H(0/0), T(4/−32), W(2/−16) | dito | ok |
| 3.2 | Probe t = −1 | T(0/0), H(−2/4), W(−1/2) | dito | ok |
| 3.3 | Ortskurven | y = −2x³ (Wendepunkte), y = −x³/2 (Extrempunkte) | dito | ok |
| 3.4 | −4t³ = −32 | t = 2, einzige reelle Lösung | t = 2 | ok |

### Übungen

| Aufgabe | Größe | Eigenes Ergebnis | Datei | |
|---|---|---|---|---|
| `a1` | f′ = 3(x−1)(x−3), f″(1) = −6, f″(3) = 6 | T(3/−4), H(1/0) | Soll −4, T(3/−4) | ok |
| `a1` | Kontrolle (x−4)(x−1)² | = x³−6x²+9x−4 | dito | ok |
| `a2` | x_W = 2, f(2) = −6, f′(2) = −7 | −7 | −7 | ok |
| `a2` | f′ = 3(x−2)²−7; arctan(−7) | −81,8699° | −81,87° | ok |
| `mc1` | f′ = 2x(x−3)², f″ = 6(x−1)(x−3), f‴(3) = 12 | Sattelpunkt S(3/8,5) | S(3/8,5) | ok |
| `mc1` | f′(2,9) / f′(3,1) | +0,058 / +0,062 | 0,058 / 0,062 | ok |
| `mc1` | f″(2,9) / f″(3,1) | −1,14 / +1,26 | −1,14 / 1,26 | ok |
| `a3` | h(0), h(1), h(3), h(5) | 0; 0,4; 0; **2,0** | 0; 0,4; 0; 2,0 m | ok |
| `a3` | Lehrerteil h(6) | 5,4 m | 5,4 m | ok |
| `a4` | B″ = 0 → t = 10, B′(10) | **6 cm/Tag**, B′(0) = B′(20) = 0 | 6 cm/Tag | ok |
| `a4` | B(10), B(20) | 40 cm, 80 cm | 40, 80 | ok |
| `a5` | D = 144 − 12a = 0 | **a = 12**, f′ = 3(x−2)², S(2/8) | a = 12, S(2/8) | ok |
| `a5` | Gegenprobe a = 11 / 13 | D = +12 / −12 | +12 / −12 | ok |
| `a5` | Herkunft der Distraktoren 4 und 36 | 16−4a = 0 bzw. 144−4a = 0 | dito | ok |
| `z1` | A/B/C/D aus den SVG-Stützpunkten | f′ = −x / x³−x / x²−1 / x² | dito | ok |
| `z1` | Skalierung der SVG (28 px je Einheit) | in allen vier Bildern konsistent | — | ok |
| `z1` | Lösungsfolge | C · B · D · A | C · B · D · A | ok |
| `a6` | f″(3) = 36, f(3) = −27 | 36, −27 | 36, −27 | ok |
| `a6` | f′(−0,1) / f′(0,1) | −0,124 / −0,116, kein VZW | −0,124 / −0,116 | ok |
| `a6` | f‴(0), f‴(2) | −24, +24 | −24, +24 | ok |
| `a6` | f″ bei ∓0,1 und bei 1,9/2,1 | +2,52/−2,28 und −2,28/+2,52 | dito | ok |
| `a6` | **Korrektur zu Schritt (5)** | W2(2/−16), f′(2) = −16 | W2(2/−16), −16 | ok |
| `a7` | D = 4a² − 12, Bedingung | abs(a) > √3 ≈ 1,7321 | abs(a) > √3 ≈ 1,73 | ok |
| `a7` | a = 2: H(−1/0), T(−1/3 / −4/27) | bestätigt (f″ = −2 bzw. +2) | dito | ok |
| `a7` | Wendepunkt für jedes a | x = −a/3, y = a(2a²−9)/27 | dito | ok |
| `a7` | Ortskurve (Zusatz) | y = x − 2x³ | y = x − 2x³ | ok |
| `a7` | Sattelfall a = √3 | x = −√3/3, y = −√3/9 | nur Inhaltsdatei | ok |

### Simulation

Die drei Scharen wurden als Python-Portierung der JS-Funktionen `punkte()` und `nullstellenF1()`
gegen sympy geprüft — für **jede** ganzzahlige Reglerstellung (Schar 1 und 2: a = −1,00 … 4,00;
Schar 3: a = −1,00 … 2,00; zusammen 263 Zustände). Verglichen wurden Lage, y-Wert, Typ (H/T/W/S)
und Wendetangentensteigung gegen die exakt bestimmten Nullstellen von f′ und f″ mit
Vorzeichenwechseltest. **Abweichungen: 0** (drei Treffer in der 10. Nachkommastelle sind reine
Gleitkommadarstellung).

Zwei Zustände von Hand ausgeschrieben:

| Zustand | Größe | Handrechnung | Anzeige | |
|---|---|---|---|---|
| Schar 1, a = 1,00, x0 = 2,00 | f(2) = 8/3 − 2 | 0,6667 | 0,67 | ok |
| | f′(2) = 4 − 1 | 3 | 3,00 | ok |
| | f″(2) = 2·2 | 4 | 4,00 | ok |
| | H(−√a / (2/3)a√a), T(√a / −(2/3)a√a) | (−1/0,6667), (1/−0,6667) | H(−1,00/0,67), T(1,00/−0,67) | ok |
| | W(0/0), m = −a | m = −1 | −1,00 | ok |
| Schar 2, a = −0,50, x0 = 2,50 | f(2,5) = 15,625/3 − 6,25 − 1,25 | −2,2917 | −2,29 | ok |
| | f′(2,5) = 6,25 − 5 − 0,5 | 0,75 | 0,75 | ok |
| | f″(2,5) = 2·1,5 | 3 | 3,00 | ok |
| | w = √1,5 = 1,2247; H(1−w), T(1+w) | (−0,2247/0,05808), (2,2247/−2,39164) | H(−0,22/0,06), T(2,22/−2,39) | ok |
| | W(1 / a − 2/3), m = a − 1 | (1/−1,1667), m = −1,50 | W(1,00/−1,17), −1,50 | ok |

Weitere geprüfte Zustände, alle deckungsgleich mit K7 der Inhaltsdatei: S1 a = 4,00 → f = −5,33,
f′ = 0,00, H(−2,00/5,33), T(2,00/−5,33), m = −4,00 · S1 a = 0,00 → S(0,00/0,00), m = 0,00 ·
S1 a = −1,00 → keine Extrempunkte, m = +1,00 · S2 a = −1,00 / 0,00 / 0,50 / 0,95 / 1,00 / 1,05 /
2,00 → sämtliche Punktkoordinaten und Steigungen wie tabelliert (a = 0,95: H(0,78/0,29),
T(1,22/0,28), m = −0,05; a = 1,00: nur S(1,00/0,33), m = 0,00) · S3 a = 1,00 → f = 1,33,
f′ = 4,00, f″ = 8,00, T(1,00/−0,08), S(0,00/0,00), W(0,67/−0,05) · S3 a = 2,00 → T(2,00/−1,33),
W(1,33/−0,79) · S3 a = 0,00 → nur T(0,00/0,00), kein Wendepunkt.

Aus dem Quelltext abgeleitete Beziehungen und ihre Prüfung:

| Prüfpunkt | Befund |
|---|---|
| Ableitungen im Code (Z. 1095–1108) | f′ und f″ aller drei Scharen sind exakt die Ableitungen von f — ok |
| Punktformeln | H/T von Schar 1 bei ∓√a mit y = ±(2/3)a√a; Schar 2 bei 1∓√(1−a); Schar 3 T(a / −a⁴/12), S(0/0), W(2a/3 / −4a⁴/81) — alle symbolisch bestätigt |
| Sonderfälle | Erkennung über den ganzzahligen Reglerwert (`aInt === 20` statt `a === 1`), also kein Fließkommavergleich — ok |
| Pixelumrechnung `px`/`py`/`pd` | px(0) = 515, px(2) = 811,67, py(0) = 190, py(6) = 20 — stimmt mit Quelltextkommentar und Handrechnung überein |
| Ziehen bei 70 % Breite (Schar 2) | x = −2 + (700−70)/890·6 = 2,2472 → gerundet x0 = 2,25 — ok |
| Abspielen | 1,00 Einheit je Sekunde, stoppt am Reglerende — ok |
| Vorzeichenbänder | f′ > 0 grün, f′ < 0 rot, f″ > 0 blau, f″ < 0 orange — deckungsgleich mit Fließtext und Legende |
| Band an Sattelpunkten | Null-Spalten übernehmen das vorige Vorzeichen; dadurch keine falsche Farbgrenze bei Schar 1/a = 0 und Schar 3. Bei Schar 2/x = 1 wird die f″-Farbgrenze dadurch um 2 px nach rechts verschoben — unterhalb der Wahrnehmungsschwelle |
| Anzeige "waagerechte Tangente" | Schwelle `nz` = 0,005 identisch mit der Rundungsschwelle von `fmt`, deshalb nie "0,00" bei gleichzeitigem "steigt" |
| Befundzeile "f′ und f″ beide null" | ausgelöst bei S1/a=0/x0=0, S2/a=1/x0=1, S3/x0=0 — in allen drei Fällen sachlich richtig |
| Ortskurven-Spuren | Parameterbereiche der Spuren decken sich mit den Existenzbereichen der Punkte (Schar 1 nur a ≥ 0, Schar 2 Extrema nur a ≤ 1) |
| Zahlenformat | `fmt` liefert durchgehend Komma und U+2212 als Minuszeichen |
| Beobachtungsauftrag beantwortbar | Teil 1: m = a − 1 wird bei a = 1,00 exakt 0,00, Schrittweite 0,05 trifft den Wert. Teil 2: x0 = 0,00 und a = −1,00/0,00/1,00/2,00 sind bei Schar 3 alle einstellbar. Zusatz: T(1/−0,67) und T(2/−5,33) liegen beide auf y = −(2/3)x³ — ok |

### Zonen der Zahlen-Engine (vorzeichenbehafteter Quotient)

Zone nah gilt für Quotient Eingabe/Sollwert aus (0,5; 2), sonst weit.

| Aufgabe | Eingabe | Quotient | Zone berechnet | Zone laut K19 | |
|---|---|---|---|---|---|
| `a1` (−4) | 0 / 3 / −3 / −5 / 4 | 0 / −0,75 / 0,75 / 1,25 / −1,00 | weit / weit / nah / nah / weit | identisch | ok |
| `a2` (−7) | −6 / −5 / −8 / 2 / 5 / **7** | 0,857 / 0,714 / 1,143 / −0,286 / −0,714 / **−1,00** | nah / nah / nah / weit / weit / **weit** | identisch | ok |
| `a3` (2,0) | 0,4 / 0 / 4 / 1,6 / 3 | 0,2 / 0 / 2,0 / 0,8 / 1,5 | weit / weit / weit / nah / nah | identisch | ok |
| `a4` (6) | 10 / 40 / 80 / 3 / 0 | 1,667 / 6,67 / 13,3 / 0,5 / 0 | nah / weit / weit / weit / weit | identisch | ok |
| `a5` (12) | 9 / 4 / 36 / 6 / **−12** | 0,75 / 0,333 / 3,0 / 0,5 / **−1,00** | nah / weit / weit / weit / **weit** | identisch | ok |

Die fett gesetzten Zeilen sind genau die Fälle, für die die Umstellung gebaut wurde: Mit
Betragsquotient wären +7 (Soll −7) und −12 (Soll 12) als nah durchgegangen. **Die Änderung wirkt
an allen fünf Aufgaben korrekt.** Toleranzen (0,05, bei `a3` 0,02) sind eng genug: −4,06 bei `a1`
und 5,9 bei `a5` werden zurückgewiesen. Die Alternativeinheit von `a3` (200 cm) wird mit
mitskalierter Toleranz (2 cm) gleich streng geprüft. Einzige verbliebene Schwäche ist der
Begleittext, siehe M2 und M9.

### Struktur, Sprache, Lehrplan

| Prüfpunkt | Befund |
|---|---|
| Chip "Funktionen und Analysis" | wörtlich aus `kernlehrplan-nrw.md`, Mathematik LK, Inhaltsfeld 1 — ok |
| Q1-Verortung | dort ausdrücklich für "Funktionsuntersuchung" belegt — ok |
| Kompetenzzitate | keine; offene Zuordnung sauber als Rückfrage an die Fachkonferenz markiert — ok |
| Kompetenzbereiche über das Rechnen hinaus | Argumentieren (`a6`, `a7`, `mc1`), Modellieren (`a3`, `a4`), Werkzeuge nutzen (Simulation), Kommunizieren (Begriffsschärfung 2.1) — ok |
| Anforderungsbereiche, eigene Zuordnung | `a1`/`a2` I (geübtes Routineverfahren), `mc1`/`a3`/`a4`/`a5`/`z1`/`sim1`/`sim2` II, `a6`/`a7` III — **deckungsgleich** mit der Auszeichnung in der Datei |
| AB III mit Bewertungskriterien | beide vorhanden und operationalisierbar — ok |
| LK-Niveau | angemessen: Scharen, Fallunterscheidung, Ortskurve, Randextrema, zwei Beurteilungsaufgaben. Die Rechenaufgaben selbst sind eher leicht (kubische Funktionen mit ganzzahligen Nullstellen); das Niveau trägt über die Begründungen, nicht über den Rechenaufwand |
| Sechs Abschnitte mit nummerierten `.stufe`-Köpfen | ok |
| Anrede | durchgehend geduzt; die sieben Treffer auf "Sie"/"Ihre" sind ausnahmslos Personalpronomen der 3. Person ("Sie sagt aber nur, wo man suchen muss") — ok |
| Dezimaltrennzeichen | Komma in allen sichtbaren Zahlen, auch in `data-plain` und in allen JS-Rückmeldungen; kein einziger Dezimalpunkt gefunden — ok |
| `data-plain` | 476 Formelelemente, **0** davon ohne `data-plain` — ok |
| Distraktor-Feedback | alle 22 Optionen mit inhaltlichem Feedback, kein "Leider falsch" — ok |
| Hilfestufen | drei Stufen bei allen neun Übungen und beiden Simulationsfragen; Stufung tragfähig außer bei `a3` (M8) |
| Zeitbedarf | 10+30+20+20+40+5 = 125 Minuten, stimmt mit dem Chip "ca. 125 Minuten" — ok. 40 Minuten für neun Aufgaben inklusive zweier Beurteilungsaufgaben sind knapp, die Pflichtauswahl im Lehrerteil entschärft das |
| "neun Aufgaben" im Lehrerteil | neun Übungen gezählt — ok |
| Quotientenregel im Lehrerteil erwähnt | in `module/mathe-q1-ableitungsregeln.html` tatsächlich behandelt, die Reihenfolgeaussage stimmt — ok |
| `werkzeug/modulcheck.py`, eigener Lauf | `blocker: []`, `maengel: []`; Druckansicht 14/14 Aufgaben, 0 Bedienelemente, 0 Lehrerteil, kein Querscrollen bei 1280/900/390 px |
| Eintrag in `fachliches/modulliste.md` | "in Arbeit" — DoD-Punkt 7 bewusst offen, wie im Bauprotokoll vermerkt |
| Schmaler Abstand vor Einheiten | im Modul nicht verwendet — die Referenz `physik-q1-induktion.html` verwendet ihn ebenfalls nirgends (0 Vorkommen von U+202F/U+2009). Projektweite Frage, **nicht** diesem Modul anzulasten |
| `button.primaer:hover{background:#1a43b8}` (Blau) | unverändert aus der Referenz; CLAUDE.md verlangt, außer den Akzenttokens nichts zu ändern — regelkonform, aber beim nächsten Referenz-Update mitzuziehen |
| Druckansicht zeigt die Musterlösungen (`data-stufe="9"`) | folgt aus dem unverändert übernommenen `@media print`-Block der Referenz, dort ebenso — kein Befund gegen dieses Modul |

---

## Gut gelöst

1. **Die Fehlvorstellung ist das Thema, nicht ein Anhängsel.** Abschnitt 2.4, der Merksatz "Es
   kommt auf den Wechsel an, nicht auf die Null", `mc1`, Schritt (3) von `a6` und die Simulation
   zu Schar 3 arbeiten alle auf dieselbe Einsicht hin. Das ist ein durchgehender roter Faden
   statt einer Aufzählung von Verfahren.
2. **Zwei verdeckte Scharen.** Die Formeln von Schar 2 und 3 stehen nirgends im sichtbaren Text,
   die Punktsorten ergeben sich nur aus Messwerten und Vorzeichenbändern. Damit sind `sim1` und
   `sim2` tatsächlich nur mit der Simulation lösbar — die Anforderung, an der sonst fast jedes
   Modul scheitert. Dass die richtige Rückmeldung die Formel anschließend offenlegt und zum
   Nachrechnen einlädt, ist die richtige Auflösung.
3. **Die Verschmelzung von Hoch- und Tiefpunkt als didaktisches Zentrum.** Dass der Sattelpunkt
   nicht als Sonderfall abgehandelt wird, sondern als beobachtbarer Übergang (Beobachtungsauftrag
   Teil 1; Distraktor 3 in `sim1`: "Das Verschwinden ist kein Sprung"), ist die stärkste Stelle
   des Moduls.
4. **Charakteristische Punkte aus geschlossenen Formeln statt numerischer Suche** (Z. 1131–1156).
   Deshalb stimmen sie in allen 263 geprüften Zuständen exakt, und die Sonderfälle werden über
   den ganzzahligen Reglerwert erkannt statt über Fließkommavergleiche. Diese Konstruktion sollte
   in andere Module übernommen werden.
5. **`a6` ist eine Musteraufgabe für AB III.** Eine Schülerlösung, in der die Ergebnisse
   überwiegend stimmen, aber zwei Begründungen nicht tragen und ein Rechenfehler steckt, trennt
   "Ergebnis richtig" von "Begründung tragfähig" schärfer als jede Rechenaufgabe.
6. **Die Rückmeldungen nennen den Denkfehler und rechnen ihn vor**, statt ihn nur zu benennen:
   Bei `a5` wird zu jedem Distraktor die fehlerhafte Diskriminante mitgeliefert (16 − 4a → 4,
   144 − 4a → 36). Solche Texte kann man im Unterricht direkt vorlesen.
7. **Der Lehrerteil ist brauchbar, nicht dekorativ:** neun konkrete Anhaltepunkte mit Ort im
   Modul, ein durchgerechneter Impuls (h(6) = 5,4 m), fünf Experimentbezüge, die wirklich zum
   Thema passen (Biegelinie eines eingespannten Lineals als sichtbarer Krümmungswechsel), und ein
   dokumentierter Schalter `FORMELN_SICHTBAR` samt Hinweis auf dessen Nebenwirkung.

---

## Fazit in fünf Sätzen

Fachlich ist das Modul einwandfrei: Von der Kurvendiskussion über die Scharen bis zu jeder
einzelnen Musterlösung und jedem Sollwert der Simulation stimmt jede Zahl, und die
Vorzeichenkonventionen sind über die ganze Datei konsistent. Die Simulation ist besser als
verlangt — sie bestimmt ihre charakteristischen Punkte aus geschlossenen Formeln und traf in
allen 263 geprüften Reglerstellungen exakt die sympy-Werte, und ihre beiden Verständnisfragen
sind dank der verdeckten Formeln wirklich nur durch Bedienen lösbar. Der Lehrplanbezug ist echt
und wörtlich, die offene Zuordnung wurde markiert statt erfunden, und beide AB-III-Aufgaben sind
Begründungsaufgaben mit Bewertungskriterien statt verkleideter Rechnungen. Zu beanstanden sind
zehn Stellen, von denen vier wirklich stören: Der Lehrerteil verlangt bei Aufgabe 1 eine Antwort,
die die Aufgabe gar nicht zulässt (M1), die Rückmeldungen von `a1` wurden nach der Umstellung der
Zahlen-Engine nicht nachgezogen (M2), das Einstiegsnarrativ beschreibt genau andersherum, als
sich die zuerst sichtbare Schar 1 verhält (M3), und Ortskurve wie Fallunterscheidung werden
gelehrt und im Selbstcheck behauptet, aber in keiner Pflichtaufgabe geübt (M4). In den Unterricht
kann das Modul auch jetzt schon, weil niemand daran etwas Falsches lernt — aber M1 bis M4 sollten
vor dem ersten Einsatz eingearbeitet werden, weil M1 die Lehrkraft zu einer falschen Korrektur
verleitet und M4 die zentrale LK-Technik des Moduls ungeübt lässt.
