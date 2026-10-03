# Technikprüfung `mathe-q1-hauptsatz.html`

Verdikt: **bestanden mit Nacharbeit.** Keine Blocker.

Modulcheck: `blocker: []`, `maengel: []`. Konsole und `pageerror` leer, kein waagerechtes Scrollen bei 1280 und 390 px.
Simulation (Bildschirmfotos bei 1280 und 390 px): Fläche grün/rot, Tangente, Integralfunktion, Regler, Abspielen, Pause, Zurücksetzen und Ziehen im Bild funktionieren. Stichproben: Rate A, a = 10,8, x = 1,8 → −23,33 m³; Rate B, x = 7,5 → −1,50 m³; „Unterschied" überall 0,000.

## Mängel

1. **Achsenbeschriftung Rate C.** `fmt(yMax,0)` rundet die Achsenenden 4,5 und −0,5 (oben) auf „5" und „−1", ±14,5 (unten) auf „15" und „−15". Beschriftung passt nicht zur Achsenlage. Stelle: `gitter()`, um Zeile 1130, `raten.C.fMin/fMax/iMin/iMax`. Abhilfe: Achsenenden ganzzahlig wählen (5, −1, 15, −15).
2. **Diagrammtitel im Canvas.** Unteres Diagramm zeigt „Integralfunktion I_a(x) = …" mit Unterstrich-Rest, Rate C zeigt „e^(−0,3t)". Abhilfe: „Iₐ(x)" und „e^(−0,3·t)" per Unicode.
3. **390 px.** Canvas skaliert auf etwa 0,32, Achsenzahlen und Titel haben etwa 4 px Schrifthöhe; die Werte stehen lesbar in den Anzeigen darunter. Touchziele: Checkbox „Tangente" 16 × 16 px, Regler 16 px hoch, Knöpfe 41 px (unter 44 px). Betrifft die geerbte Referenzstruktur; nur beobachtet, nicht behoben.

Bildschirmfotos: Scratchpad-Ordner der Sitzung (`shots/`).
