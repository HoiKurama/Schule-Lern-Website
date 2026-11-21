# Q1-Modul bauen

Du baust eine einzelne interaktive Lernseite als eigenständige HTML-Datei. Die fachlichen Inhalte
bekommst du fertig geliefert. Du erfindest keine Aufgaben und keine Erklärtexte und änderst keine
Zahlenwerte. Alle Pfade gelten ab dem Projektordner.

## Zuerst lesen
1. `CLAUDE.md` des Projekts und `.claude/rules/module.md`. Die technischen Regeln dort
   sind nicht verhandelbar.
2. `vorlage/bausteine.md`: Engine-Verträge, Markup-Muster, was kopiert und was ersetzt wird
3. `vorlage/baustein-formelleiste.md`: Datenvertrag für `formelDaten`
4. `vorlage/fallen.md`: Fehler, die schon einmal passiert sind
5. `module/physik-q1-induktion.html` vollständig, es ist deine Vorlage. In großen Stücken lesen.
6. die genannte Inhaltsdatei unter `inhalte/`

## Vorgehen
1. Kopiere das Referenzmodul auf den neuen Dateinamen in `module/`.
2. Tausche im `:root`-Block die drei Akzent-Tokens und den Kopfverlauf nach der Farbtabelle.
   Sonst bleibt das CSS unverändert.
3. **Simulation zuerst:** als eigene IIFE nach der Spezifikation der Inhaltsdatei.
4. Ersetze den Inhalt der Sections. Halte dich exakt an die Markup-Muster aus `bausteine.md`, vor
   allem an die Kopplung von `data-mc`, `name` und den `data-i`-Indizes.
5. Schreibe `mcDaten` und `numDaten` aus den Aufgaben, `formelDaten` aus dem Abschnitt
   „Formelleiste“ der Inhaltsdatei. Texte wörtlich übernehmen.
6. Trage alle Aufgabenschlüssel in die Namensliste der Exportfunktion ein.
7. Entferne jeden Rest des Referenzmoduls: Texte, Fußzeile, Antwortschlüssel, Lehrerteil.
8. Prüfe selbst, bevor du abgibst (unten).

Speichere nach jedem Schritt. Hilfsskripte (z. B. `baue.py`, `daten.py`, `sim.js`) gehören nach
`output/<modul>/`, nie nach `module/`. Ein Bauskript ist erlaubt, wenn am Ende eine einzelne Datei
herauskommt. Das Referenzmodul, `index.html` und `fachliches/modulliste.md` fasst du nicht an.

## Eigenprüfung vor der Abgabe
1. Kurzes Playwright-Skript in `output/<modul>/`, als Datei, nicht per Heredoc. Browserstart und
   Import wie in `vorlage/fallen.md` beschrieben.
   - Simulation einstellen, Momentanwerte auslesen und **gegen die Sollwerte der Inhaltsdatei**
     vergleichen. Stimmt ein Wert nicht, ist die Simulation falsch, nicht die Rechnung.
   - Screenshot der Simulation aufnehmen und selbst ansehen.
2. Prüfe auf Steuerzeichen: kein Zeichen mit Code unter 32 außer Zeilenumbruch.
3. Den Modulcheck startest du erst im nächsten Schritt.

Ist das CDN gesperrt, ist das kein Fehler. Dann müssen lesbare Klartextformeln erscheinen und
keine LaTeX-Reste.

Melde zurück: Dateiname, welche Prüfungen liefen, welche Werte du nachgerechnet hast, was offen ist.
Fehlt in der Inhaltsdatei etwas, das du brauchst: nicht selbst erfinden, sondern als offen melden.
