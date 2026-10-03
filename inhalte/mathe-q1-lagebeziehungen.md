# Lagebeziehungen — Inhaltsprotokoll

Stand: gebautes Modul `module/mathe-q1-lagebeziehungen.html` (Mathematik LK Q1, Inhaltsfeld „Analytische Geometrie
und Lineare Algebra“, ca. 120 Minuten). Gebaut auf der Vorlage `mathe-q1-flaechen-zwischen-graphen.html` mit dem
Bauskript des Moduls „Geraden und Ebenen“. Baut auf `mathe-q1-geraden-ebenen` auf.

## Aufbau

| Abschnitt | Inhalt |
|---|---|
| 1 Einstieg | Zwei Drohnen (S(0\|0\|10)+t(4\|3\|1), T(100\|0\|20)+s(−2\|1\|0)): gleiche Stelle (40\|30\|20), aber zu verschiedenen Zeiten (t = 10, s = 30); dritte Drohne landet auf dem Garagendach (4\|5\|5); Vorwissen vw1 (Punktprobe Gerade), vw2 (Gleichungssystem), vw3 (Punktprobe Koordinatenform) |
| 2 Zwei Geraden (`geraden`) | Vier Lagen (Tabelle, Abbildung), Schritt 1 Richtungsvektoren vergleichen (Punktprobe: identisch oder parallel), Schritt 2 Gleichsetzen mit getrennten Parametern (Schnittpunkt S(3\|4\|4), windschief), typischer Fehler (gleicher Parameter), Merksatz |
| 3 Gerade/Ebene und Ebene/Ebene (`ebenen`) | Einsetzen der Geraden in die Koordinatenform (eine Lösung, keine, jedes r); Ebenen: Normalenvektoren vergleichen, Schnittgerade aus zwei Koordinatengleichungen; zwei Abbildungen, Übersichtstabelle |
| 4 Simulation | Gerade und Ebene im Schrägbild, Wert n∘X − d entlang der Geraden, Gleichung für r auf Wunsch |
| 5 Übungen | a1 bis a7; a3 ist die Zuordnungsaufgabe (Geradenpaar ↔ Lage) |
| 6 Abschluss | Zusammenfassung, Zentralabitur-Hinweis, Selbstcheck, Export und Druck, Lehrerteil |

Formelleiste: 5 Einträge in zwei Gruppen (`geraden`: parallel, gleichsetzen · `ebenen`: koord, einsetzen, ebenenpar). Die
`abschnitt`-Ids sind `geraden` und `ebenen`. Nicht drin: Entscheidungswege, Schnittgerade (Verfahren, keine Formel). Die Leiste
sagt nicht, was ein konstanter oder einmal verschwindender Wert n∘X − d bedeutet (sim1, sim2).

## Simulation

Schrägbild wie im Vorgängermodul, Canvas `cvL`, Maßstab und Mitte je Datensatz. Ebene E: 2x₁ + x₂ + 2x₃ = 6 (Ausschnitt
a, b ∈ [−2; 2]). Regler r von −2 bis 2 in Schritten von 0,5; goldene Raute, wenn X in E liegt.

| Datensatz | p | u | n∘X − d | Lage |
|---|---|---|---|---|
| 1 | (2\|0\|0) | (−1\|2\|1) | 2r − 2 | schneidet bei r = 1, S(1\|2\|1) |
| 2 | (0\|0\|1) | (1\|−2\|0) | −4 | parallel |
| 3 | (3\|0\|0) | (1\|−2\|0) | 0 | g liegt in E |

Gegengeprüft mit `simtest.py` (9 Reglerstellungen je Datensatz: n∘X, n∘X − d, Nullstellen, Gleichung und Lösungstext;
keine Konsolenfehler). Die Textbeispiele benutzen dieselbe Ebene mit anderen Geraden, damit die Simulation eine Beobachtung bleibt.

## Aufgabenzahlen (nachgerechnet)

| Aufgabe | Ergebnis |
|---|---|
| a1 | g: (2\|0\|1)+r(1\|2\|1), h: (8\|0\|1)+s(−4\|4\|2): s = 1, r = 2, dritte Gleichung stimmt, x₃ = 3 |
| a2 | g: (1\|0\|2)+r(2\|1\|1), E: x₁+2x₂−x₃ = 5: −1 + 3r = 5, r = 2 |
| a3 | Referenz g: (0\|1\|2)+r(1\|2\|−1): Zeilen C (schneidend, S bei r = s = 1), A (identisch), D (windschief, dritte Gleichung 1 ≠ 2), B (parallel, 3·u, Punktprobe schlägt fehl) |
| a4 | E: 2x₁−x₂+2x₃ = 7, g: (1\|1\|0)+r(1\|a\|2): n∘u = 6 − a = 0, a = 6; Stützpunkt: 1 ≠ 7, also parallel |
| a5 | E₁: x₁+x₂+x₃ = 6, E₂: x₁−x₂+3x₃ = 2: x₃ = 3 ⇒ x₁ = −2, x₂ = 5; Schnittgerade (4\|2\|0)+t(−2\|1\|1) |
| a6 | Aussage „nicht Vielfache ⇒ schneiden sich“ ist falsch, Gegenbeispiel windschief |
| a7 | Beweis: Zwei Punkte von g in E ⇒ g in E |

## Technische Notizen

- `abschnitt` in `formelDaten` entspricht den Section-Ids `geraden` und `ebenen`.
- Abbildungen `@@FIG1@@` (vier Lagen zweier Geraden), `@@FIG2@@` (Gerade/Ebene), `@@FIG3@@` (Ebene/Ebene) als Inline-SVG im Bauskript.
- Modulcheck: 0 Blocker, 0 Mängel, KaTeX 352 von 352, kein Querscrollen bei 1280, 900, 390 px, Formelleiste ohne Überlauf.

## Offen

- Kernlehrplan: Ob das Gauß-Verfahren in Q1 verlangt wird, ist nicht geklärt; das Modul löst alle Systeme durch Einsetzen
  oder Addieren. Kreuzprodukt wird nicht genutzt.
- Ebenen in Parameterform: Lage nur über Umwandlung in Koordinatenform, der direkte Weg steht kurz im Text.
- Notation (windschief, Schnittgerade, Stützvektor) ist Unterrichtsüblichkeit.
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
- Folgemodul `mathe-q1-abstaende-winkel` ist in der Kachelreihe als geplant eingetragen.
