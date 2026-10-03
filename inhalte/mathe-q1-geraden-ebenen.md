# Geraden und Ebenen — Inhaltsprotokoll

Stand: gebautes Modul `module/mathe-q1-geraden-ebenen.html` (Mathematik LK Q1, Inhaltsfeld „Analytische Geometrie
und Lineare Algebra“, ca. 120 Minuten). Gebaut auf der Vorlage `mathe-q1-flaechen-zwischen-graphen.html` mit dem
Bauskript des Vektoren-Moduls. Baut inhaltlich auf `mathe-q1-vektoren-grundlagen` auf.

## Aufbau

| Abschnitt | Inhalt |
|---|---|
| 1 Einstieg | Drohne auf gerader Bahn (S(0\|0\|10), pro Sekunde (4\|3\|1)) und Garagendach als Ebene (A(0\|0\|3), Kanten (8\|0\|0) und (0\|10\|4)); Vorwissen vw1 (Mittelpunkt), vw2 (parallele Vektoren), vw3 (Gleichungssystem für einen Parameter) |
| 2 Parameterform | Gerade (Stützvektor, Richtungsvektor, Parameter), Zweipunkteform, Nicht-Eindeutigkeit, Punktprobe, Ebene (Spannvektoren), Dreipunkteform, Punktprobe mit 3 Gleichungen und 2 Unbekannten; zwei SVG-Abbildungen (Gerade in der Ebene, Dach im Schrägbild) |
| 3 Normalen- und Koordinatenform | Skalarprodukt nur in dem Umfang, den die Normalenform braucht (Komponentenformel, Orthogonalitätskriterium mit Begründung über Pythagoras), Normalenvektor aus zwei Gleichungen, Normalenform, Koordinatenform, Punktprobe durch Einsetzen, besondere Lagen (Tabelle), Spurpunkte, Umwandlung Koordinatenform → Parameterform (über Spurpunkte oder freie Parameter), Tabelle „Welche Form wofür“, Hinweis zur Geraden in Ebene und Raum; eine SVG-Abbildung (Spurdreieck mit Normalenvektor) |
| 4 Simulation | Ebene in Parameterform im Schrägbild, Normalenvektor, Probepunkt Q, drei Datensätze |
| 5 Übungen | a1 bis a7; a3 ist die Zuordnungsaufgabe (Koordinatengleichung ↔ Lage) |
| 6 Abschluss | Selbstcheck, Zentralabitur-Hinweis, Export und Druck, Lehrerteil |

Formelleiste: 8 Einträge in zwei Gruppen (gerade, zweipunkt, ebene, dreipunkt · skalar, ortho, normalen, koord). Die
`abschnitt`-Ids sind `parameterform` und `normalenform`. Nicht drin: Umrechnungsverfahren, Spurpunkte, Formeln, die nur in
Aufgaben vorkommen. In der Leiste steht bewusst nicht, dass n∘X für alle Punkte der Ebene denselben Wert hat (sim1).

## Simulation

Schrägbild (x₂ nach rechts, x₃ nach oben, x₁ nach links unten, halbe Kästchendiagonale). Maßstab und Mitte werden je
Datensatz aus den Eckpunkten des Ausschnitts, den Probepunkten und der Spitze des Normalenvektors berechnet, damit alles
ins Bild passt. Regler r und s von −2 bis 2 in Schritten von 0,5. Das hellblaue Parallelogramm ist der Ausschnitt für
r, s ∈ [−2; 2]. Anzeigen: P, u, v, n, n∘u und n∘v, Einstellung, X, n∘X, Probepunkt Q, n∘Q, Abstand X–Q und „Punktprobe“
(erst nach Klick). Zwei Probepunkte je Datensatz: Q1 liegt in der Ebene (ganzzahlige Parameter im Reglerbereich), Q2
liegt daneben.

| Datensatz | p | u | v | n | d = n∘p | Q1 (in E) | Q2 (nicht in E) |
|---|---|---|---|---|---|---|---|
| 1 | (3\|0\|0) | (−1\|2\|0) | (−1\|0\|1) | (2\|1\|2) | 6 | (1\|2\|1), r = s = 1 | (2\|1\|1), n∘Q = 7 |
| 2 | (4\|0\|0) | (−2\|1\|0) | (0\|0\|1) | (1\|2\|0) | 4 | (2\|1\|2), r = 1, s = 2 | (3\|1\|1), n∘Q = 5 |
| 3 | (3\|0\|0) | (2\|1\|0) | (0\|1\|1) | (1\|−2\|2) | 3 | (5\|2\|1), r = s = 1 | (3\|2\|1), n∘Q = 1 |

Datensatz 1 ist dieselbe Ebene wie das Beispiel 2x₁ + x₂ + 2x₃ = 6 im Text (u dort verdoppelt). Datensatz 2 ist parallel
zur x₃-Achse, Datensatz 3 hat eine negative Komponente im Normalenvektor.

Gegengeprüft: `zahlen.py` (exakte Brüche, alle Zahlen aus Text, Aufgaben und Rückmeldungen) und `simtest.py` im Browser:
In allen drei Datensätzen ist n∘X bei 49 Einstellungen gleich d, die Anzeigen n∘Q und die Punktprobe stimmen, Q1 wird mit
den angezeigten Parametern auf 0,00 LE getroffen, keine Konsolenfehler.

## Aufgabenzahlen (nachgerechnet)

| Aufgabe | Ergebnis |
|---|---|
| a1 | g durch A(2\|−1\|4), B(5\|3\|10): AB = (3\|4\|6); x₂ = 11 ⇒ r = 3; x₃ = 22 (Punkt (11\|11\|22)); nah: 28 (r mit A, aber B als Stützpunkt) |
| a2 | P(1\|2\|3), n = (2\|−1\|4): d = 12; nah: 16 (Vorzeichenfehler bei x₂) |
| a3 | x₃ = 3 → C, 2x₁ − x₂ + 3x₃ = 0 → A, 2x₁ + 3x₂ + x₃ = 6 → D (Spurpunkte (3\|0\|0), (0\|2\|0), (0\|0\|6)), x₁ + 2x₂ = 4 → B |
| a4 | E: (1\|0\|2) + r(2\|1\|0) + s(−1\|0\|1), P(a\|3\|5): r = 3, s = 3, a = 4; nah: 7 (−s vergessen) |
| a5 | A(2\|0\|1), B(3\|1\|3), C(2\|2\|0), n = (5\|n₂\|n₃): AB = (1\|1\|2), AC = (0\|2\|−1); n₂ = −1, n₃ = −2; d = 8; nah: +1 (Vorzeichen) |
| a6 | A(1\|0\|2), B(3\|1\|3), C(7\|3\|5): AC = 3·AB, Punkte kollinear, Dreipunkteform beschreibt nur die Gerade, keine eindeutige Ebene |
| a7 | E₁: x₁ − 2x₂ + 2x₃ = 3, E₂ = 2·E₁ (gleiche Ebene), E₃ gleiche linke Seite wie E₂, rechts 5: parallel, verschieden; Punktprobe mit (3\|0\|0) |

## Technische Notizen

- Das Bauskript ergänzt `koordstrich()`: Koordinatentupel wie `(3|2)` und `(-1|0|4)` im tex-Teil bekommen automatisch
  `\,|\,`. Ausdrücke wie `|r|` bleiben unberührt, weil das Muster nur Klammern mit Zahlen trifft.
- `abschnitt` in `formelDaten` muss genau die `id` der `<section>` sein (`parameterform`, `normalenform`). Der Modulcheck
  meldet sonst einen Blocker und alle Sprungziele als Mangel.
- Die Abbildungen stehen als `@@FIG1@@` bis `@@FIG3@@` in den Teildateien und werden im Bauskript als Inline-SVG erzeugt.

## Offen

- Skalarprodukt: Die Planung nennt es erst im Modul „Abstände und Winkel“. Für die Normalenform wird es hier minimal
  eingeführt (Komponentenformel, Orthogonalität), Winkel und Projektion bleiben dem Folgemodul. Wenn die Fachschaft die
  Koordinatenform zuerst ohne Skalarprodukt (Eliminieren der Parameter) behandelt, muss Abschnitt 3 anders aufgebaut werden.
- Kernlehrplan: Ob das Vektorprodukt (Kreuzprodukt) Pflicht ist, ist nicht geklärt; das Modul nutzt es nicht. Ebenso offen:
  Achsenabschnittsform. Keine Zitate erfunden.
- Notation (Stützvektor, Spannvektor, Normalenvektor, Spurpunkte) ist Unterrichtsüblichkeit, die Schule kann andere
  Namen vereinbart haben.
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
- Das Folgemodul `mathe-q1-lagebeziehungen` ist im Text bereits angekündigt (Gleichheit zweier Geraden-Gleichungen).
