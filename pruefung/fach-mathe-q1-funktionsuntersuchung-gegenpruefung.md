# Gegenprüfung `module/mathe-q1-funktionsuntersuchung.html`

Prüfer: fachpruefung. Von der Hauptsitzung gekürzt abgelegt (Agent darf keine Dateien schreiben).

**Urteil: Nacharbeit (klein), danach freigabefähig.** Kein Zahlenwert falsch; 40 Werte und die neue Aufgabe a8 (f_t(x) = x³ − 3t²x, Extremstellen ±t, Ortskurve y = −2x³) mit sympy bestätigt; zwei Simulationszustände von Hand, zehn weitere im Browser bestätigt; Touch-CSS (≤600 px) ändert nichts außer sieben Touch-Regeln, kein Querscrollen bei neun Breiten; Modulcheck `blocker: []`, `maengel: []`.

M1–M3, M5–M10 und Technik 1–3 behoben; M4 nur halb (a8 nur in Differenzierung).

## Restmängel (alle danach vom Bauagenten behoben, Modulcheck sauber, Stichprobe der Hauptsitzung: Chip 130 min, „Lösungsgerüst“ vorhanden)

| Nr. | Schwere | Befund |
|---|---|---|
| R1 | mittel | Zeit-Chip „ca. 125 Minuten“ gegen Lehrertabelle 130. |
| R2 | mittel | a8 nur in Differenzierung, Selbstcheck behauptet Fallunterscheidung/Ortskurve für alle → a8 in Pflichtliste, a3 in Differenzierung. |
| R3 | gering–mittel | a8 Stufe 3 „Lösungsweg“ verrät die ganze Lösung → „Lösungsgerüst“ mit Schlüsselzahlen. |
| R4 | gering | Ergebnis y = −2x³ steht wörtlich in 3.2 → Hinweissatz in Musterlösung. |
| R5 | gering | Fallunterscheidung im Aufgabentext vorweggenommen → Klammer gestrichen. |
| R6 | gering | Export nummeriert offene Aufgaben nur durch → `data-offen`. |
| R7 | gering | `.check input` 13×17 px → 24×24 px im 600-px-Block. |
| R8 | kosmetisch | Kommentarkopf „Druck“ über Touch-Block → korrigiert. |
| R9 | Hinweis | `--akzent` = `--gruen` (Hover falscher Option wie richtige), `button.primaer:hover` blau: kommt aus Referenz/Farbtabelle, nicht diesem Modul anzulasten; an Referenz zurückmelden. |

Kanonische Schriftgröße bei 390 px real ca. 11,8 px (Protokoll korrigiert).
