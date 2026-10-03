# Gegenprüfung `module/mathe-q1-flaechen-zwischen-graphen.html`

Prüfer: fachpruefung. Von der Hauptsitzung gekürzt abgelegt (Agent darf keine Dateien schreiben).

**Urteil: freigabefähig.** Kein fachlicher Fehler; Musterlösungen, Einheitenumrechnungen und über 30 Simulationszustände in sympy/Playwright nachgerechnet, keine Abweichung. Modulcheck `blocker: []`, `maengel: []`. Erstprüfung M1–M13 und Technik 1–10 bis auf drei Punkte erledigt.

## Restmängel (alle danach vom Bauagenten behoben, Modulcheck sauber)

| Nr. | Schwere | Befund | Behebung |
|---|---|---|---|
| R1 | mittel | Lehrerteil nennt weiter „b ≈ −0,376“ (Antwort auf sim2) und die Einstellung b = −0,38 mit Werten | Zahl gestrichen, „an der Nullstelle von B“ / „kurz rechts der ersten Schnittstelle“ |
| R2 | gering | sim2 Option 2 als einzige mit „≈“ | alle Optionen „b = …, denn …“ |
| R3 | gering–mittel | Canvas-Schrift bei 390 px ca. 7 px (`kk()` gedeckelt bei 1,7) | Deckel 2,1, Canvas 1000 × 690, Kollisionsfreiheit per Screenshot geprüft |
| R4 | gering | sim2-Rückmeldung nennt −7,88 (b = −1,50 nicht einstellbar, Mindestabstand) | Vergleich b = −1,40 (−5,98) / b = −0,60 (3,74), live bestätigt |
| R5 | gering | a2-`nah`: alle Eingaben lesen zuerst die −7,54-Diagnose | „Falls dein Wert negativ war …“ / „positiv …“; a5 analog |
| R6 | gering | `data-num` an a3/a6/a7 ohne Zahleneingabe (Modulcheck zählte 7 statt 4) | entfernt, Modulcheck zählt 4 |
| R7 | Prozess | Modulliste/Index nicht nachgezogen | Modulliste auf fertig; Index gesammelt nach Durchgang 3 |
