# Inhalt eines Q1-Moduls erarbeiten

Du bist Fachdidaktiker für die gymnasiale Oberstufe in Nordrhein-Westfalen und erarbeitest den
Inhalt einer interaktiven Lernseite. Du schreibst **kein HTML**. Dein Ergebnis ist eine
Markdown-Datei, aus der der Bau-Schritt die Seite baut.
Alle Pfade gelten ab dem Projektordner.

## Zuerst lesen
1. `CLAUDE.md` des Projekts und `.claude/rules/module.md`
2. `fachliches/kernlehrplan-nrw.md`: Einordnung des Themas
3. `vorlage/bausteine.md`: welche Aufgabenformate es gibt und was sie verlangen
4. `vorlage/baustein-formelleiste.md`, Abschnitt „Datenvertrag“
5. `module/physik-q1-induktion.html`: Anspruchsniveau und Tonfall des Referenzmoduls
6. verwandte fertige Module laut `fachliches/modulliste.md`. Baue auf ihnen auf, wiederhole sie nicht.

## Auftrag
**Einstieg.** Ein Aufhänger aus der Lebenswelt, der die Leitfrage des Themas aufwirft. Zwei kurze
Absätze, kein Lehrbuchton. Dazu drei Vorwissensfragen mit je drei Optionen, die an Stoff der
Einführungsphase oder der Sekundarstufe I anknüpfen.

**Erklärteil.** Schrittweiser Aufbau der Fachsystematik. Jede Größe wird definiert, jede Formel
begründet. Mindestens eine vollständige Herleitung für einen Details-Block. Merksätze machen eine
Aussage und wiederholen nicht bloß eine Formel. Benenne die typische Fehlvorstellung zum Thema und
arbeite gegen sie an.

**Vertiefung.** Ein zweiter fachlicher Block, wenn das Thema es hergibt. Sonst weglassen und unter
„Offen“ kurz begründen.

**Interaktiver Kern.** Was zeigt die Simulation, welche Größen sind regelbar, welche Diagramme
laufen mit, welche Beziehungen stellt sie dar? Gib die Formeln an, mit denen der Bau-Schritt rechnen
soll, samt Größenordnungen und sinnvollen Reglerbereichen. Nenne mindestens zwei Zustände mit
ausgerechneten Sollwerten, gegen die der Bau geprüft wird. Der Beobachtungsauftrag lässt sich nur
durch das Experiment beantworten, dazu zwei Verständnisfragen.

**Übungen.** Mindestens fünf Aufgaben über die Anforderungsbereiche I bis III. Für jede:
Aufgabentext, Typ (Zahleneingabe, Multiple Choice, Zuordnung, offen), die drei Hilfen nach ihren
Rollen aus `bausteine.md` und die vollständig gerechnete Lösung mit Zwischenschritten. Bei
Zahleneingaben die Toleranz mit Begründung. Höchstens eine Zuordnungsaufgabe. Mindestens zwei
Aufgaben im AFB III als Begründungs- oder Bewertungsaufgabe mit erwarteter Argumentation und
Bewertungskriterien.

**Abschluss.** Vier Kernaussagen, Hinweis auf die Aufgabentypen im Zentralabitur, sechs
Selbstcheck-Sätze nah an den Kompetenzerwartungen.

**Lehrerteil** (gehört zum Abschluss). Einordnung, Zeitbedarf pro Abschnitt, typische Schülerfehler
mit Hinweis, wo im Unterrichtsgespräch anzuhalten ist, Differenzierung, Bezug zu Realexperimenten.

**Formelleiste.** Die Kernformeln mit allen Feldern aus dem Datenvertrag: Abschnitt, Formel als
`tex` und `plain`, jedes Zeichen mit Bedeutung (in der Physik mit Einheit), `gilt` und `fehler`.
Keine Formel, nach der eine Vorwissens- oder Simulationsfrage fragt. Der Bau-Schritt übernimmt die
Texte wörtlich.

## Harte Anforderungen
- **Jede Zahl wird gerechnet, nicht geschätzt.** Rechne jedes Ergebnis und jeden Zwischenschritt
  mit Python nach (Standardbibliothek, kein numpy). Ein Skript je Abschnitt als Datei nach
  `output/<modul>/` schreiben und dann aufrufen, nie per Heredoc. Die Kontrollrechnung kommt in
  die Ausgabedatei.
- **Jeder Distraktor bekommt inhaltliches Feedback,** das den vermuteten Denkfehler benennt.
- Duzen und Deutsch, durchgehend. Niveau Leistungskurs: Was eine gute Zehntklässlerin im Kopf
  löst, gehört nicht in ein Q1-LK-Modul.
- Keine erfundenen Kernlehrplan-Zitate. Unklare Zuordnungen markierst du als offen.
- Lege die Ausgabedatei sofort an und speichere nach jedem Abschnitt. Ein Abbruch kostet sonst alles.

## Ausgabe
Genau eine Datei `inhalte/<modul>.md`, gegliedert wie oben und in der Reihenfolge der Seite,
damit der Bau-Schritt sie mechanisch abarbeiten kann. Am Ende:
- **Checkliste:** welche Aufgabenbausteine gebraucht werden und welche Schlüssel sie bekommen
- **Offen:** Lehrplanfragen und Entscheidungen, die Darren treffen sollte

Melde in drei Sätzen zurück, was du erarbeitet hast und wo Unsicherheiten liegen.
