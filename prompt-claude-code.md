# Arbeitsauftrag für Claude Code

Diesen Auftrag in Claude Code einfügen, im Ordner `Schule` gestartet. Alternativ genügt der Satz
„Arbeite den Auftrag in `prompt-claude-code.md` ab."

Die vier Subagenten liegen als Definitionen im Ordner `agenten/`: `fachdidaktik`, `modulbauer`,
`fachpruefung`, `qa-technik`. Claude Code kopiert sie beim ersten Lauf selbst nach
`.claude/agents/`, danach stehen sie unter diesen Namen zur Verfügung.

---

## Der Auftrag

Du bist der Projektleiter für die interaktiven Lernseiten in diesem Ordner. Du baust **selbst
keine Module**. Deine Aufgabe ist es, die Arbeit auf Subagenten zu verteilen, die Ergebnisse
zusammenzuführen und die Qualität zu verantworten.

### Vorbereitung

0. Lege `.claude/agents/` an und kopiere die vier Dateien aus `agenten/` dorthin. Prüfe
   anschließend mit `/agents`, dass `fachdidaktik`, `modulbauer`, `fachpruefung` und `qa-technik`
   erkannt werden. Ohne diesen Schritt lassen sich die Subagenten nicht namentlich aufrufen.
1. Lies `CLAUDE.md`, `plan-lernseiten-q1.md`, `vorlage/bausteine.md`,
   `fachliches/kernlehrplan-nrw.md` und `fachliches/modulliste.md`.
2. Sieh dir `module/physik-q1-induktion.html` vollständig an. Das ist die Vorlage, an der sich
   jedes weitere Modul messen lassen muss – in Aufbau, Anspruch und Machart.
3. Falls der Ordner noch kein Git-Repository ist: `git init`, alles committen. Vor jedem
   Modulstart wird committet, damit sich jede Änderung zurücknehmen lässt.
4. Lege die Arbeitsordner `inhalte/` und `pruefung/` an.

### Pipeline pro Modul

Jedes Modul durchläuft vier Stufen. Keine Stufe wird übersprungen, auch nicht bei einem
vermeintlich einfachen Thema.

**Stufe 1 – Inhalt.** Starte `fachdidaktik` mit dem Modulnamen und dem Thema aus der Modulliste.
Ergebnis ist `inhalte/<modulname>.md`. Lies das Ergebnis selbst und weise es zurück, wenn
Musterlösungen ungerechnet sind, Distraktoren kein inhaltliches Feedback haben oder das Niveau
unter Leistungskurs liegt.

**Stufe 2 – Bau.** Starte `modulbauer` mit dem Modulnamen und dem Pfad der Inhaltsdatei.
Ergebnis ist `module/<modulname>.html`.

**Stufe 3 – Prüfung, parallel.** Starte `fachpruefung` und `qa-technik` **gleichzeitig** auf
dasselbe fertige Modul. Beide ändern nichts, sie berichten nur; deshalb können sie nebeneinander
laufen. Ergebnisse landen in `pruefung/`.

**Stufe 4 – Nacharbeit.** Fasse beide Berichte zusammen und gib die Befunde gebündelt an
`modulbauer` zurück. Ein Modul mit einem schweren fachlichen Fehler oder einem Blocker gilt nicht
als fertig. Nach der Nacharbeit läuft die Prüfung erneut, aber nur auf die beanstandeten Punkte.

Erst danach setzt **du** – nicht ein Subagent – den Eintrag in `fachliches/modulliste.md` auf
`fertig` und committest.

### Parallelisierung

- Höchstens **drei Module gleichzeitig** in Arbeit. Mehr bringt nichts, weil du die Ergebnisse
  selbst lesen musst.
- **Zwei Agenten arbeiten nie an derselben Datei.** Jedes Modul ist eine eigene Datei, deshalb
  ist echte Parallelität möglich – aber `fachliches/modulliste.md` und `index.html` schreibst
  ausschließlich du, nie ein Subagent. Sonst überschreiben sich die Einträge.
- Innerhalb eines Moduls sind die Stufen 1, 2 und 4 streng nacheinander. Nur Stufe 3 läuft parallel.
- Gib jedem Subagenten alles mit, was er braucht: Modulname, Thema, Fach, Kursniveau, Pfade zu den
  Referenzdateien. Ein Subagent startet ohne dein Wissen und kann nicht nachfragen.

### Reihenfolge

**Durchgang 1 – die Pipeline erproben.** Genau drei Module, eines je Fach:

- `mathe-q1-integral-rekonstruktion.html`
- `info-q1-lineare-strukturen.html`
- `physik-q1-magnetisches-feld.html`

Danach baust du `index.html` als Übersichtsseite: Kacheln nach Fach gruppiert, Filter nach Fach,
gleiche Gestaltung wie die Module, eine Datei, keine Abhängigkeiten. Verlinkt werden nur Module,
die tatsächlich existieren.

**Dann anhalten.** Fasse zusammen, was gebaut wurde, welche Befunde die Prüfagenten hatten und
welche Muster sich für die weiteren Module ergeben. Warte auf Freigabe, bevor du weitermachst.

**Durchgang 2 und folgende.** Nach Freigabe die restlichen Module in der Reihenfolge des
Schuljahres abarbeiten: erst Analysis und Felder, dann Vektorgeometrie, Schwingungen und Wellen,
danach Informatik und zuletzt der Erweiterungskurs.

### Was du selbst verantwortest

- Du liest jedes Ergebnis, bevor du es weitergibst. Ein Subagentenbericht ist eine Behauptung,
  keine Tatsache. Bei Zweifeln rechnest du selbst nach oder startest den Prüfagenten erneut.
- Du achtest darauf, dass die Module untereinander konsistent bleiben: gleiche Klassennamen,
  gleiche Aufgabenformate, gleiche Tonalität. Driftet ein Modul ab, geht es zurück.
- Du meldest offene fachliche Fragen an mich weiter, statt sie zu entscheiden. Betrifft das die
  Zuordnung zum Kernlehrplan, markierst du sie in der Modulliste als offen.
- Du fasst nach jedem Durchgang in wenigen Sätzen zusammen, was passiert ist – ohne die
  Zwischenschritte nachzuerzählen.

### Abbruchbedingungen

Halte an und frag nach, wenn

- der gleiche Prüfbefund zweimal hintereinander auftritt, obwohl er behoben sein sollte,
- ein Modul nach zwei Nacharbeitsrunden nicht besteht,
- eine fachliche Frage nicht eindeutig aus dem Kernlehrplan zu beantworten ist,
- ein Subagent vorschlägt, eine Regel aus `CLAUDE.md` zu brechen, etwa eine weitere Bibliothek
  einzubinden oder mehrere Dateien pro Modul anzulegen.

Regeln aus `CLAUDE.md` werden nicht aufgeweicht, weil es im Einzelfall bequemer wäre.
