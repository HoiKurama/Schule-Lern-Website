# Fachprüfung: mathe-q1-abstaende-winkel

Prüfer: fachpruefer (Opus, high), 2026-11-26. Geprüft wurden `module/mathe-q1-abstaende-winkel.html` und
`inhalte/mathe-q1-abstaende-winkel.md`. Alle Werte hat der Prüfer selbst mit `python3 -c` nachgerechnet.

- **Urteil:** Nacharbeit nötig
- **Modulcheck:** Der offizielle `werkzeug/modulcheck.py` ist nicht gelaufen, weil Playwright fehlte. Laut Auftrag hat der Ersatztest im eingebauten Browser keine Blocker gefunden. Druckansicht, KaTeX-Satz, Überlauf und Schublade sind nicht geprüft.

## Schwere Fehler

1. **sim1: Die falsche Option A und ihr Feedback widersprechen der Simulation.**
   Fundstelle: Modul Z. 551 (Option A), Z. 1174 (Feedback); Inhaltsdatei Z. 287.
   Option A begründet ihren Denkfehler mit „weil P danach unter der Ebene liegt“, das Feedback sagt „Nur der Wert n∘P − d wird negativ“. In Datensatz 1 (Q₀ = (0|2|−1), u = (2|−1|2)) ist es umgekehrt: Vor s = 3 liegt P unter E (n∘P − d = −4 bei s = 0), danach über E (+4 bei s = 6). Wer der Aufforderung „Schau auf die Anzeige n∘P − d“ folgt, sieht den Wert positiv werden. Das ist der Fall „Widerspruch zwischen Erklärtext und Simulation“ aus `vorlage/fallen.md`.
   Korrekturvorschlag: Option A „… weil P danach auf der anderen Seite der Ebene liegt“, Feedback „n∘P − d wechselt bei s = 3 das Vorzeichen (von negativ zu positiv), der Abstand ist sein Betrag.“ Oder Datensatz 1 umdrehen.

## Mängel

1. **Anzeige „Höhe über E in x₃-Richtung“ bei Punkten unter E** (Z. 516, 1535, Legende Z. 505, Kästchen Z. 540, Code Z. 1400). Die Anzeige zeigt immer einen positiven Betrag, auch wenn P unter E liegt; das Kästchen „Weg senkrecht nach unten zeigen“ führt für s < 3 nach oben. Vorschlag: „senkrechter Abstand zu E in x₃-Richtung“, „senkrechten Weg zur Ebene zeigen“.
2. **a1: Toleranzbegründung falsch, nah-Feedback mit falscher Diagnose** (Inhaltsdatei Z. 309; Modul Z. 1202, 1205). cos⁻¹(0,667) = 48,164°, also 48,16°, liegt außerhalb der Toleranz 0,02 und bekommt „Prüfe, ob du den Sinus statt des Kosinus benutzt hast“. Vorschlag: Toleranz 0,03 oder nah-Text, der zuerst die Rundung anspricht.
3. **a4: fehlender Betrag führt zur falschen Diagnose** (Z. 1212–1216). −33,85° landet im nah-Bereich und bekommt den Kosinus-Hinweis; der Hinweis auf den Betrag steht nur im weit-Text.
4. **a3: Hilfestufen kaum abgestuft** (Z. 645–647). Der Ansatz nennt die vollständige Zuordnung. Eher AFB I/II.
5. **Windschiefe Geraden: Begründung fehlt, die der Selbstcheck verlangt** (Z. 471, 793, 783). Es fehlt, warum der Abstand der Hilfsebene der kürzeste zwischen g und h ist (jede Verbindungsstrecke verbindet zwei parallele Ebenen).
6. **Uneinheitliche Bezeichnung des Winkels Gerade/Ebene**: Erklärteil und Leiste α, Simulation φ (φ sonst Winkel zwischen Vektoren). Vorschlag: in der Simulation α.
7. **Doppelt belegtes Symbol H** (Z. 471, Lehrerteil Z. 811): Hilfsebene und Lotfußpunkt auf h. In Z. 471 wird P benutzt, ohne als Stützpunkt von g eingeführt zu sein.
8. **Für den LK fehlt eine Aufgabe mit Umkehrung oder Parameter** (Übungen Z. 574–765).
9. **Lehrerteil nennt keine Kompetenzbereiche** (Z. 808).
10. **Kleiner Zahlenfehler in der Inhaltsdatei** (Z. 347): mit √29 ≈ 5,39 ergibt sich 33,82°, nicht 33,83°. Ohne Auswirkung.

**Fragen an den Autor:** a4: Wo startet der Landeanflug? Von S(0|0|10) aus träfe die Bahn die Dachebene bei (9,33|0|3), neben dem Dach (bis x₁ = 8). · Hatte der Kurs den Kosinussatz (vw1, Herleitung)? · Die Offen-Notiz zur Lehrplanverbindlichkeit von HNF, Punkt–Gerade und windschiefen Geraden ist berechtigt; der Chip ist wörtlich richtig, kein Zitat erfunden.

## Nachgerechnet

| Stelle | Datei | eigenes Ergebnis | ok |
|---|---|---|---|
| Einstieg d(S,E) | 35/√29 ≈ 6,50 m | 6,4993 | ✓ |
| Einstieg Dachpunkt, Höhendifferenz | (0\|0\|3), 7 m | (0\|0\|3), 7 | ✓ |
| Dachebene passend zum Vorgängermodul | −2x₂ + 5x₃ = 15 | ∥ (0\|−2\|5), d = 15 | ✓ |
| Beispiel 1 | 60° | 60,00° | ✓ |
| Beispiel 2 | −4; 116,39°; 63,61° | −4; 116,388°; 63,612° | ✓ |
| Beispiel 3 | 62,73°; mit Kosinus 27,27° | 62,734°; 27,266° | ✓ |
| Beispiel 4 | 0,2357; 76,37° | 0,23570; 76,367° | ✓ |
| Beispiel 5 | t = −1, F(1\|2\|1), 3 LE | ebenso | ✓ |
| Beispiel 6 | 9r − 9, F(3\|1\|0), 3 LE | ebenso | ✓ |
| Beispiel 7 | n = (2\|1\|2), 3 LE; G(3\|0\|0), H(5\|1\|2) | ebenso | ✓ |
| a1 | 48,19°, tol 0,02 | 48,190° | ✓ |
| a1 Zwischenrundung (Inhaltsdatei) | 48,17° | 48,164°, abgelehnt | ✗ |
| a1 nah-Wert | 41,81° | 41,810° | ✓ |
| a2 | 5 LE; nah 4,33; weit 15 | 5; 4,333; 15 | ✓ |
| a4 | 0,5571; 33,85°; nah 56,15° | 0,55709; 33,855°; 56,145° | ✓ |
| a4 Rundung √29 ≈ 5,39 | 33,83° | 33,820° | kleine Abweichung |
| a5 | r = 2, F(4\|5\|4), 6 LE; nah 8,49 | ebenso | ✓ |
| a6 | n = (2\|−1\|2), 4 LE; nah 4,58 | ebenso | ✓ |
| a7 | 3 LE; Kontrolle 18/6; Faktor 8 | ebenso | ✓ |
| a8 | r = 1, F(1\|2\|1), √21 ≈ 4,58; Skalarprodukt 3 | ebenso | ✓ |
| sim2 | sin ≈ 0,44; cos ≈ 0,90; tan ≈ 0,50 | 0,4444; 0,8958; 0,4961 | ✓ |
| Simulation, alle Sollzustände | Inhaltsdatei Z. 270–276 | alle gleich | ✓ |
| Winkel der Datensätze | 26,39° / 0° / 90° | ebenso | ✓ |
| Abbildungen Lot und Gerade/Ebene | rechter Winkel, α und 90° − α | ✓ | ✓ |

Simulationscode: P(s) = Q₀ + s·u/3, w = n∘P − d, d = |w|/3, F = P − (w/9)·n, x₃-Strecke = |w|/2, φ = arcsin(|n∘u| / (3·|u|)). Stimmt mit der Fachtheorie überein, die Projektion entspricht dem angegebenen Schrägbild.

## Gut gelöst

- Simulationsebene begründet gewählt (Textebene: Normalenvektor im Schrägbild senkrecht).
- sim2 verbindet Simulation und Theorie, Distraktoren cos und tan sind echte Fehlvorstellungen.
- a8 (Tim) ist echter AFB III mit Gegenbeispiel, allgemeiner Begründung und Probe.
- a7 (Lena) mit Skalierungsargument.
- Gezielte nah-Werte (√72, √21, 4,33).
- Durchgehender Drohnenkontext, Lotfußpunkt liegt auf dem Dachstück.
- Saubere Herleitungen (Kosinussatz, Lotgerade), Hinweis auf die Doppelbedeutung von d.

## Fazit

Alle Rechenwerte im Modul, in den Lösungswegen und in der Simulation sind richtig. Der einzige schwere Fehler ist das sim1-Feedback. Die übrigen Mängel betreffen Diagnosetexte (a1, a4), die Abstufung in a3, eine fehlende Begründung bei windschiefen Geraden und uneinheitliche Bezeichnungen. Nach diesen Korrekturen und einem vollständigen Modulcheck kann man mit dem Modul zuverlässig Abstände und Winkel auf LK-Niveau lernen.
