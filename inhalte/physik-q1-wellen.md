# Wellen — Inhaltsprotokoll

Stand: gebautes Modul `module/physik-q1-wellen.html` (Physik LK Q1, Chip „Inhaltsfeld: Schwingende Systeme und Wellen“,
ca. 120 Minuten). Modulcheck ohne Blocker und Mängel, 341 von 341 Formeln gesetzt, kein Querscrollen bei 390, 900 und 1280 px.
Gebaut auf der Vorlage `physik-q1-mechanische-schwingungen.html`, Bauskript wie beim Schwingkreis.

## Aufbau

| Abschnitt | Inhalt |
|---|---|
| 1 Einstieg | Stadionwelle („La Ola“, Rechenbeispiel 10 m/s); vw1 f = 1/T, vw2 Schall als Longitudinalwelle (Teilchen schwingen längs), vw3 sin(2π·t/T) bei T/4 |
| 2 Ausbreitung (`grundlagen`) | Welle transportiert Energie, keine Materie; Transversal-/Longitudinalwelle (Tabelle); Momentaufnahme und Zeitverlauf (SVG); c = λ·f; Seilpunkt-Geschwindigkeit v_max = 2π·f·ŷ gegen c; Wellenfunktion aus der Verzögerung x/c hergeleitet, Zahlenbeispiel y(0,30 m; 0,20 s) = 9,5 cm, Vorzeichenprüfung am Wellenberg |
| 3 Überlagerung (`ueberlagerung`) | Superposition; zwei gleiche Wellen mit Gangunterschied (φ = 2π·Δs/λ, Summe = 2ŷ·cos(φ/2)·sin(…)), Bedingungen Δs = nλ und Δs = (n+½)λ, Tabelle; Reflexion am festen/losen Ende (SVG); stehende Welle y = 2ŷ·sin(kx)·cos(ωt) aus ankommender und reflektierter Welle; Saite mit zwei festen Enden, fₙ = n·c/(2L), SVG der Eigenschwingungen, Gitarrenbeispiel; c = √(F/μ) ohne Herleitung; Details zu Pfeifen |
| 4 Simulation | Seilwelle in drei Einstellungen, siehe unten |
| 5 Übungen | a1 bis a7; a3 ist die Zuordnungsaufgabe (Eigenschwingung ↔ Frequenz oder Wellenlänge) |
| 6 Abschluss | Zusammenfassung, Zentralabitur-Hinweis, Selbstcheck, Export und Druck, Lehrerteil |

Formelleiste: 5 Einträge in zwei Gruppen (ausbreitung, wellenfunktion · konstruktiv, destruktiv, saite). Die `abschnitt`-Ids sind
`grundlagen` und `ueberlagerung`. Nicht drin: v_max = 2π·f·ŷ (sim1), c = √(F/μ) und λₙ = 2L/n (sim2), f = 1/T (vw1), Pfeifenformeln.

## Simulation „Seilwelle“

Zwei Canvas: `cvS` (Momentaufnahme y(x), 0–6 m, in der Einstellung „Stehende Welle“ 0–3 m), `cvT` (Zeitverlauf am Ort x₀, Fenster 4 s).
Kein Integrationsverfahren: alle Kurven kommen direkt aus y = Σ aᵢ·sin(ω·t + sᵢ·k·x + φᵢ). Regler (je Einstellung ein- oder
ausgeblendet): f 0,5–3 Hz, λ 1–4 m, ŷ 5–40 cm, x₀ 0–3 m (Schritt 0,05), φ 0–360° (15°), n 1–4, F 2–16 N. Haken: „Welle 2 läuft
entgegen“, „Teilwellen zeigen“, „Zeitlupe (¼)“.

| Einstellung | Modell | Besonderheit |
|---|---|---|
| Laufende Welle | y = ŷ·sin(ωt − kx), c = λ·f | orange Punkte auf den Wellenbergen, Klammer für λ |
| Zwei Wellen | y₁ + y₂ mit y₂ = ŷ·sin(ωt ∓ kx − φ) | Gangunterschied bei x₀ in λ und m; Amplitude der Summe über die letzte Periode |
| Stehende Welle | L = 3,0 m, μ = 0,20 kg/m, c = √(F/μ), λ = 2L/n, f = n·c/(2L); Teilwellen −ŷ·sin(ωt − kx) und +ŷ·sin(ωt + kx) | goldene Knoten, gestrichelte Hüllkurve |

Anzeigen: Zeit, f, T, λ, c, Auslenkung bei x₀, Geschwindigkeit des Seilpunkts, Amplitude bei x₀, Gangunterschied, Knoten und Bäuche.
Gegengeprüft mit `simtest.py` im Browser (Pause, Zustand lesen, gegen exakte Formel): laufende Welle bei fünf Einstellungen,
zwei Wellen gleichsinnig (sechs φ) und gegenläufig (sieben Kombinationen), stehende Welle (sieben Kombinationen), Reglerlauf in
allen Einstellungen ohne NaN. Keine Abweichungen, keine Konsolenfehler. Das beobachtete v_max bei ŷ = 10 cm und 1 Hz ist 0,63 m/s (sim1).

## Aufgabenzahlen (nachgerechnet, `zahlen.py`)

| Aufgabe | Ergebnis |
|---|---|
| a1 | 440 Hz, 343 m/s: λ = 0,78 m |
| a2 | y = 0,05 m·sin(2π(t/0,40 s − x/1,2 m)): c = 1,2 m / 0,40 s = 3,0 m/s |
| a3 | L = 0,65 m, f₁ = 110 Hz: f = 330 Hz → D (n = 3), λ = 0,65 m → A (n = 2), λ = 1,30 m → C (n = 1), f = 440 Hz → B (n = 4) |
| a4 | gedeckte Pfeife, L = 0,20 m: λ = 4L = 0,80 m, f = 429 Hz (offen wäre 858 Hz) |
| a5 | Saite verkürzt auf 0,45 m: c = 143 m/s, f = 159 Hz |
| sim1 | ŷ = 10 cm, f = 1 Hz: v_max = 0,63 m/s < c = 2,0 m/s (bei ŷ = 40 cm: 2,5 m/s) |
| sim2 | n = 2: F = 4 N → 16 N, λ = 3,0 m bleibt, f 1,49 → 2,98 Hz |

## Technische Notizen

- Das Bauskript fügt eine CSS-Regel ein, die `button[aria-pressed="true"]` im Simulationsbereich hervorhebt; das Grundgerüst
  zeigt den aktiven Knopf sonst nicht an. Dieselbe Regel ist im Schwingkreis nachgetragen.
- Abbildungen als Inline-SVG im Bauskript: `@@ABB1@@` (Momentaufnahme und Zeitverlauf), `@@ABB2@@` (Reflexion), `@@ABB3@@`
  (Eigenschwingungen), `@@DIAGRAMME@@` (Zuordnung).
- Der Regler x₀ hat die Schrittweite 0,05 m, damit sich die Knoten bei n = 4 (0,75 m) treffen lassen.
- Rechenbeispiele ohne Herstellerangaben: Gitarre (0,65 m, 110 Hz, 80 N, 3,9 g/m), Schall 343 m/s bei 20 °C, Kammerton 440 Hz.

## Offen

- Kernlehrplan: Ist die Wellenfunktion mit Ort und Zeit Pflicht, oder genügt die qualitative Beschreibung? Gehören Saiten und
  Pfeifen (Eigenfrequenzen, gedeckte Pfeife) und c = √(F/μ) zum Pflichtstoff? Keine Zitate erfunden.
- Der Gangunterschied ist nur eindimensional eingeführt; Quellen in der Ebene gehören ins Modul `physik-q1-doppelspalt-gitter`.
- In der Einstellung „Laufende Welle“ sind f und λ unabhängig einstellbar (das Medium legt c eigentlich fest); im Lehrerteil benannt.
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
