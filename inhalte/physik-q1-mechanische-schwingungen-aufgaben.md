# Mechanische Schwingungen — Abschnitte 4 bis 6 (Simulation, Übungen, Abschluss)

Ergänzung zu `physik-q1-mechanische-schwingungen.md` (dort Abschnitte 1 bis 3). Die alte Datei
bleibt unverändert, weil sie mit 782 Zeilen die Grenze von ~400 Zeilen längst überschritten hat.
Stand: gebautes Modul `module/physik-q1-mechanische-schwingungen.html`, Modulcheck ohne Befund.

## 4 Das Pendel in der Simulation

Horizontales Federpendel, Masse auf reibungsfreier Schiene. Drei Zeichenflächen: Pendel, x-t-Diagramm
der letzten zehn Sekunden (mit Hüllkurve bei freier gedämpfter Schwingung und mit der Erregerkraft),
Resonanzkurve aus der Formel mit einem Ring für die gemessene Amplitude.

| Regler | Bereich | Schritt | Startwert |
|---|---|---|---|
| Masse m | 0,1 bis 0,5 kg | 0,05 | 0,2 |
| Federkonstante D | 2 bis 20 N/m | 0,5 | 8 |
| Reibung b | 0 bis 4 kg/s | 0,01 | 0,20 |
| Anfangsauslenkung | 1 bis 12 cm | 1 | – |
| Erregerkraft F₀ | 0,1 bis 0,8 N | 0,05 | – |
| Erregerfrequenz f_e | 0,2 bis 2,5 Hz | 0,01 | – |

Bedienung: Masse ziehen, Erreger ein/aus, Zeitraffer ×5, Pause, „Grenzfall“ (setzt b = 2·√(m·D)),
Zurücksetzen. Anzeigen: x, v, Periode, δ, Dämpfungsfall, Amplitude gemessen und nach Formel, Phase.
Numerik: RK4, Schritt 0,002 s. Grenze der Auslenkung 45 cm.

Beobachtungsauftrag (drei Schritte): (1) b = 0, Periode bei 3 cm und 10 cm ablesen, unabhängig von
der Amplitude; (2) b = 0,20 kg/s, zwei benachbarte Maxima, Verhältnis gegen e^(−Λ); (3) Erreger ein,
Einschwingen abwarten, Periode der Masse bestimmen, dann die Erregerfrequenz suchen, bei der die
Amplitude am größten ist.

Probe der Simulation gegen die Formel (Playwright, 14 s Zeitraffer, jeweils eingeschwungen):

| m / kg | D / N/m | b / kg/s | F₀ / N | f_e / Hz | gemessen | Formel | Phase |
|---|---|---|---|---|---|---|---|
| 0,2 | 8 | 0,5 | 0,5 | 1,0 | 15,9 cm | 15,9 cm | 88° |
| 0,3 | 10 | 1,0 | 0,4 | 1,2 | 3,9 cm | 3,9 cm | 133° |
| 0,2 | 8 | 0,3 | 0,3 | 2,0 | 1,3 cm | 1,3 cm | 171° |

## 5 Übungen

Sieben Aufgaben, vier mit Zahleneingabe. Alle Zahlen nachgerechnet (`pruefe.py` im Arbeitsverlauf).

| Nr. | Bereich | Inhalt | Lösung |
|---|---|---|---|
| a1 | I | Federpendel m = 0,250 kg, D = 12 N/m: Schwingungsdauer | T₀ = 0,9069 s |
| a2 | I | Fadenpendel, T = 3,0 s, g = 9,81 m/s²: Länge | l = 2,236 m |
| a3 | II | Vier x-t-Diagramme, vier Fälle zuordnen (Zuordnungsaufgabe) | A Grenzfall, B ungedämpft, C Kriechfall, D schwach gedämpft |
| a4 | II | Maxima 10,0 cm und 6,0 cm, Dekrement und Abklingkonstante | Λ ≈ 0,511, δ = 0,6385 1/s |
| a5 | II | Resonator m = 0,50 kg, D = 50 N/m, b = 1,0 kg/s, F₀ = 2,0 N, ω_e = 8,0 rad/s: Amplitude | x̂ = 10,15 cm |
| a6 | III | Waschmaschine beim Hochfahren der Schleuder: Erklärung mit erzwungener Schwingung | Musterlösung im Modul |
| a7 | III | Behauptung „Schaukel im Takt der Eigenfrequenz schaukelt sich immer höher, Reibung nebensächlich“ | Musterlösung im Modul |

Hinweise zu a6: Die echte Unwuchtkraft wächst mit ω_e²; das ist im Modul als Zusatz vermerkt, die
Modellaussage (Durchfahren der Resonanz, Amplitude begrenzt durch Dämpfung) bleibt unberührt.
Hinweise zu a7: Die Leistungsbilanz P_zu ~ x̂ gegen P_ab ~ x̂² begrenzt die Amplitude bei
x̂ = F₀/(b·ω₀).

Die Hilfen sind dreistufig. Bei a4 beginnt Hilfe 2 mit „Benutze das Dekrement: …“, damit der
Anfangszustand keine Lösung verrät.

## 6 Zusammenfassung und Selbstcheck

- „Das Wichtigste in sechs Sätzen“: Rückstellkraft und Periode, Unabhängigkeit der Periode von der
  Amplitude, Energieumwandlung, Dämpfung und die drei Fälle, erzwungene Schwingung mit Erregerfrequenz,
  Resonanz und ihre Grenze durch die Dämpfung.
- „Ich kann …“-Liste mit Kontrollkästchen, Bezug zu den Abschnitten.
- Hinweiskasten „Blick aufs Zentralabitur“, Export- und Druckknöpfe (Arbeitsblatt, mit Lösungen).
- Einklappbarer Lehrerteil: Einordnung, offene Punkte, Zeitbedarf (Abschnitte 1 und 2 etwa 50 Minuten,
  Abschnitt 3 etwa 40, Simulation 25, Übungen 35), typische Hürden, Modellgrenzen, Formelleiste,
  Experimentbezug, Differenzierung.

## Formelleiste (Besonderheiten dieses Moduls)

Zwölf Einträge in zwei Gruppen. **Bewusst nicht enthalten:** F = −D·x, die Energiesumme und
f = 1/T, weil sie Antworten auf die Vorwissensfragen vw1 bis vw3 wären.

Die Amplitude der erzwungenen Schwingung steht in der Leiste und am Sprungziel als **x̂**
(mit Dach), im übrigen Text als x_max. Grund: Ein Leisteneintrag, der mit einem Subskript beginnt
(`x_{\max} = …`), überdeckt mit seinen KaTeX-Spans den Sprunglink des Eintrags darüber. Der Satz vor
der Formel erklärt, dass beide Schreibweisen dieselbe Größe meinen.

## Offene Fragen an den Nutzer (Kernlehrplan)

1. Steht Dämpfung und Resonanz in Q1 des Kernlehrplans oder erst später?
2. Ist das logarithmische Dekrement Pflicht oder Vertiefung?
3. Abiturverbindlichkeit der erzwungenen Schwingung.
Es wurden bewusst keine Kernlehrplan-Zitate erfunden.

Noch ausstehend: fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
