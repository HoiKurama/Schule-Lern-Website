# Vektoren: Grundlagen — Inhaltsprotokoll

Stand: gebautes Modul `module/mathe-q1-vektoren-grundlagen.html` (Mathematik LK Q1, Inhaltsfeld „Analytische Geometrie
und Lineare Algebra“, ca. 120 Minuten). Modulcheck ohne Blocker und Mängel, 403 von 403 Formeln gesetzt, kein
Querscrollen bei 390, 900 und 1280 px. Gebaut auf der Vorlage `mathe-q1-flaechen-zwischen-graphen.html`.

## Aufbau

| Abschnitt | Inhalt |
|---|---|
| 1 Einstieg | Drohne mit zwei Verschiebungen, (20\|0\|5) und (0\|30\|5), Ergebnis (20\|30\|10), Luftlinie 37,4 m; Vorwissen vw1 (Verschiebung eines Punktes), vw2 (Pythagoras im Rechteck), vw3 (2×2-Gleichungssystem) |
| 2 Grundlagen | Raumkoordinaten und Schrägbild (x₁ nach links unten, halbe Kästchendiagonale), Vektor als Verschiebung, Ortsvektor, AB = b − a, Rechnen (Tabelle, Rechengesetze), Betrag mit Herleitung, Einheitsvektor, Mittelpunkt, Parallelität; drei SVG-Abbildungen |
| 3 Vertiefung | Linearkombination, lineare (Un-)Abhängigkeit über r·a + s·b + t·c = 0, zwei Beispiele mit Gleichungssystem, Folgerungen (parallel, komplanar, Basis), zwei Begründungen, Parallelogramm, Schwerpunkt, Ausblick Geraden und Ebenen |
| 4 Simulation | Pfeilkette r·a, s·b, t·c im Schrägbild, Zielpunkt, Abstand, drei Datensätze |
| 5 Übungen | a1 bis a7; a3 ist die Zuordnungsaufgabe |
| 6 Abschluss | Selbstcheck, Zentralabitur-Hinweis, Export und Druck, Lehrerteil |

Formelleiste: 10 Einträge in zwei Gruppen (vab, betrag, betragv, einheit, mittel, parallel · lk, unabh, schwer,
parallelogramm). Nicht drin: die komponentenweisen Rechenregeln (Tabelle) und die Rechengesetze (Merksatz).

## Simulation

Schrägbild mit Boden-Gitter, Achsen x₁ bis x₃ und den drei Vektoren a, b, c (dünn). Regler r, s, t von −3 bis 3 in
Schritten von 0,5 legen die Pfeilkette fest. Anzeigen: a, b, c, Einstellung, Endpunkt E, Zielpunkt, Abstand,
„Die Vektoren sind …“ und „Lösungen für das Ziel“ (beide erst nach Klick). Zwei Zielpunkte je Datensatz (P, Q).

| Datensatz | a | b | c | Ziel P | Ziel Q | Befund |
|---|---|---|---|---|---|---|
| 1 | (2\|0\|1) | (0\|2\|1) | (1\|1\|−1) | (1\|3\|4) | (0\|4\|−2) | unabhängig, für beide Ziele genau eine Lösung, P = (1\|2\|−1), Q = (−1\|1\|2) |
| 2 | (2\|0\|1) | (0\|2\|1) | (2\|−2\|0) | (2\|2\|2) | (2\|2\|0) | c = a − b, Ebene x₁ + x₂ − 2x₃ = 0; P unendlich viele (r = 1 − t, s = 1 + t), Q keine |
| 3 | (2\|0\|1) | (−4\|0\|−2) | (1\|2\|0) | (3\|2\|1) | (2\|2\|2) | b = −2a, Ebene −2x₁ + x₂ + 4x₃ = 0; P unendlich viele (t = 1, r = 1 + 2s), Q keine |

Rechnerisch nachgeprüft (exakte Brüche, `pruefe.py`): alle Lösungen, alle Ebenengleichungen, kleinster Abstand von Q zur
Ebene in Datensatz 3 = 6/√21 ≈ 1,31 LE (auf dem Regler-Raster 1,41 LE), in Datensatz 2 = 4/√6 ≈ 1,63 LE (Raster 1,73 LE).
Playwright-Test gegen diese Werte: alle Anzeigen stimmen, keine Konsolenfehler.

## Aufgabenzahlen (nachgerechnet)

| Aufgabe | Ergebnis |
|---|---|
| a1 | A(2\|−1\|4), B(5\|3\|16): AB = (3\|4\|12), Länge 13 LE |
| a2 | A(−2\|5\|7), B(10\|1\|−3): M(4\|3\|2), x₃ = 2 |
| a3 | C (Tripel mit c = 2a + b), D (Nullvektor), A (unabhängig, det = 3), B (b = −2a) |
| a4 | a = (2\|t\|6) ∥ b = (−1\|3\|−3): r = −2, t = −6 |
| a5 | A(1\|0\|2), B(4\|2\|3), C(5\|6\|1): D(2\|4\|0), x₂ = 4 (falsch: A+B−C gibt −4, B+C−A gibt 8) |
| a6 | Gegenbeispiel (1\|0\|0), (0\|1\|0), (1\|1\|0): paarweise nicht parallel, aber komplanar |
| a7 | Beweis: AB = DC ⇒ a + c = b + d ⇒ gleiche Mittelpunkte der Diagonalen |

## Technische Notizen

- Kurzschreibweise im Bauskript: `\V(a;b;c)` im tex-Teil erzeugt einen Spaltenvektor (pmatrix), Klammern in Komponenten
  sind erlaubt. Ein Minus nach `|`, `(`, `,`, `;` oder `=` wird automatisch als Vorzeichen gesetzt, sonst bleibt bei
  `P(2\,|\,-1)` eine Lücke wie bei einer Subtraktion.
- KaTeX-Falle: `\vec{p}\,'` (Strich nach Leerraum) wirft „Got group of unknown type: 'internal'“. Stattdessen einen
  anderen Buchstaben nehmen.
- Druck-Falle: Formeln, die auf `\vec{d}` enden, ragen im Druck um 3 px über den Rand. Abhilfe ist `\;` am Ende des tex.
- Der Modulcheck wirft „Lösungstext schon im Anfangszustand sichtbar“, wenn der Anfang einer Hilfestufe wortgleich an
  einer sichtbaren Stelle steht (hier Tipp von a4 und Zusammenfassung).
- Pro Modul nur eine Zuordnungsaufgabe. Zwei der Tripel in a3 sind bewusst nicht die Beispiele aus dem Text.

## Offen

- Kernlehrplan: In welcher Tiefe verlangt der LK in Q1 lineare Unabhängigkeit, Basis und Komplanarität? Determinante und
  Spatprodukt sind ausgelassen, das Gauß-Verfahren wird nicht eingeführt (Gleichungssysteme mit drei Unbekannten durch
  Einsetzen). Keine Zitate erfunden.
- Notation (Pfeil über dem Buchstaben, Ortsvektor klein geschrieben) und Schrägbild-Konvention sind Unterrichtsüblichkeit, die
  Schule kann andere vereinbart haben.
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
