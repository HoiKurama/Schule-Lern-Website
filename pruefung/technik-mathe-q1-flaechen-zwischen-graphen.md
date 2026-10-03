# Technikprüfung `module/mathe-q1-flaechen-zwischen-graphen.html`

Prüfer: qa-technik (Playwright). Bericht von der Hauptsitzung abgelegt, weil der Agent keine Dateien schreiben darf.

**Urteil: bestanden mit Nacharbeit, keine Blocker.** `modulcheck.py`: `blocker: []`, `maengel: []`.

## Mängel

| Nr. | Schwere | Befund |
|---|---|---|
| 1 | mittel | Simulationscanvas ohne `touch-action` (CSS `.sim canvas`, Wert `auto`): Wischen beim Ziehen von a/b löst auf echten Touchgeräten `pointercancel`/Seitenscroll aus. Erwartet `touch-action:none`. Kommt aus der Vorlage (Referenzmodul hat es auch nicht). Synthetische Touch-Events funktionieren, echter Fingertest steht aus. |
| 2 | mittel | Touchziele: 4 Zuordnungs-`select` 36 × 19 px, Regler `#rA`/`#rB` 16 px hoch. |
| 3 | mittel | 390 px: Canvas 348 × 216 px, Achsenzahlen ca. 7 px, Titel/Legende/Buchstaben f, g winzig; `kk()` bei 1,7 gedeckelt. |
| 4 | gering | 390 px: Diagrammtitel nur ca. 2 px vom Canvasrand (kein Anschnitt bestätigt); im unteren Diagramm Titel und Legende ca. 3 px auseinander. |
| 5 | gering | Grenzlinie a läuft bei a = untere Grenze durch den ersten Buchstaben der Titel; Marke „b“ kollidiert bei b nahe oberer Grenze mit Label „f“ (Paar A). |
| 6 | gering | Paar B: orange Kurve „Flächeninhalt“ liegt exakt unter der blauen (Bilanz = Fläche), Legende führt sie, sichtbar ist sie nicht. Kurzer Hinweis im Text fehlt. |
| 7 | gering | Rückmeldetexte passen nicht immer zur Eingabe: a5 mit 10,54 m² (FE-Wert ohne Einheit) beginnt mit „52,08 m² ist die Bilanz …“; a2 mit 740 cm² nennt nur dm²-Werte; a1 mit 0 FE beginnt mit „1,33 (= 4/3) …“. |
| 8 | gering | Einheiten uneinheitlich: a5 `numDaten.a5.ok` „105,42 m² je Meter Trassenlänge“ vs. Lösungsweg Stufe 3 „105,42 m³ je Meter“; a6 „gut 52 m³“ vs. Musterlösung „52,08 m²“. Zahlenwerte stimmen. |
| 9 | gering | Druck (aus Vorlage): 4 Prüfen-Knöpfe bleiben sichtbar; alle Hilfestufen und Musterlösungen stehen immer im Ausdruck (`.hilfe-text{display:block !important}`); 3 geschlossene Herleitungs-`details` fehlen. |
| 10 | Hinweis | `data-num` auch an a3, a6, a7 ohne Zahleneingabe (Modulcheck zählt 7, real 4); Canvas ohne `aria-label`, Wertefelder ohne `aria-live`. |

## Testabdeckung

- Laden ohne Fehler, online und mit blockiertem CDN; 574 Formeln alle mit `data-plain`, keine LaTeX-Reste.
- 15 MC-Optionen, 27 Zahleneingabe-Fälle, Zuordnung (leer/teilweise/richtig), 21 Hilfeknöpfe, 2 Musterlösungen, 4 details, Export.
- Simulation: ca. 1130 Zustände ohne NaN/undefined; Bilanz und Fläche gegen unabhängige Numerik max. Abweichung 0,005; Handrechnung Paar A 9,58 und Paar C −2,33 stimmen; Start/Pause/Ende/Reset; Ziehen mit Maus und synthetischem Touch.
- Kein waagerechtes Scrollen bei 1280/900/390 px; kein `localStorage`/`sessionStorage`/Cookie/`TODO`.
- Screenshots: `C:\Users\49176\AppData\Local\Temp\claude\C--Users-49176-Documents-Claude-Projects-Schule\a4e21d4f-5e40-4a28-8031-ae2059d6cc04\scratchpad\t\`.
