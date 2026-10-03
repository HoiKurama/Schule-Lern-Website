# Technikprüfung `module/mathe-q1-funktionsuntersuchung.html`

Prüfer: qa-technik (Playwright). Bericht von der Hauptsitzung abgelegt, weil der Agent keine Dateien schreiben darf.

**Urteil: bestanden.** Keine Blocker, nur kleinere Mängel. `modulcheck.py`: `blocker: []`, `maengel: []`.

## Mängel

| Nr. | Schwere | Befund |
|---|---|---|
| 1 | gering | Touchziel: Zuordnungs-`select` (`.zeile select`) bei 390 px nur 36 × 19 px. |
| 2 | gering | Touchziel: Regler `#rA` und `#rX` bei 390 px nur 16 px hoch. |
| 3 | gering | Darstellung 390 px: `cvF` und `cvAbl` auf ca. 0,36 verkleinert; Beschriftungen H, T, W, f′/f″ sehr klein, Regler stehen unter beiden Diagrammen. Komfortfrage. |
| 4 | informativ | Druck: Eingabefelder, Einheiten-Selects und Prüfen-Knöpfe bleiben sichtbar (5 Knöpfe, 9 Selects, 5 Zahlenfelder); mit Referenzmodul nicht verglichen. |
| 5 | informativ | Dezimalkomma im `type=number`-Feld in headless Chromium nicht testbar; Code ersetzt Komma durch Punkt. |

Hinweis: Leeres Zahlenfeld gibt nur „Bitte Zahlenwert und Einheit angeben.“ aus (Wert/Einheit fehlt nicht unterschieden).

## Testabdeckung

- Konsole und `pageerror`: sauber, mit Netz und mit blockiertem jsdelivr.
- 476 Formeln, alle mit `data-plain`, keine LaTeX-Reste.
- 21 MC-Optionen einzeln geklickt, je eigenes Feedback, genau die richtige grün.
- Zahleneingaben a1–a5: richtig, falsche Einheit, weit falsch, leer; a3 akzeptiert 200 cm.
- Zuordnung: richtig / 2 von 4 / keine, drei verschiedene Texte.
- 33 Hilfestufen und 2 Musterlösungen auf- und zuklappbar; Export meldet Erfolg.
- Simulation: alle drei Scharen über den ganzen Reglerbereich ohne NaN/undefined/Infinity; Start, Pause, Reset, Ziehen (Klemmung bei ±3,00).
- Kein waagerechtes Scrollen bei 1280, 900, 390 px. Kein `localStorage`, `sessionStorage`, Cookie, `TODO`.
- Screenshots: `C:\Users\49176\AppData\Local\Temp\claude\x\` (full/sim für 1280, 900, 390; print.pdf).
