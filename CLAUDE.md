# Projekt: Interaktive Lernseiten Q1 (NRW)

Interaktive HTML-Lernseiten für den Unterricht an einem Gymnasium in Nordrhein-Westfalen.
Fächer: Physik, Mathematik, Informatik, Mathematik-Erweiterungskurs. Stufe: Qualifikationsphase 1.
Eigenes Git-Repo, öffentlich über GitHub Pages. Pfade hier gelten relativ zu diesem Ordner,
Befehle starten im Vault: `projekte/q1-lernplattform/…`.

## Zielgruppe, gilt für jede Datei
- **Niveau: Leistungskurs Q1** nach Kernlehrplan NRW. Maßstab ist das Zentralabitur, nicht das
  Schulbuch-Mittelmaß.
- **Anrede: duzen.** „Berechne …“, „Was beobachtest du?“ Niemals siezen.
- **Sprache: Deutsch**, durchgängig, auch die Kommentare im Code. Das weicht von der Vault-Regel ab
  und gilt, bis der Nutzer entscheidet.
- Dezimaltrennzeichen in allen angezeigten Zahlen ist das **Komma** (`toFixed(2).replace(".", ",")`).
- Einheiten mit schmalem Abstand vor der Einheit, SI-konform.

## Verbindliche Referenz
`module/physik-q1-induktion.html` ist das Referenzmodul: fertig, geprüft, im Unterricht einsetzbar.
Jedes neue Modul entsteht als Kopie dieser Datei. CSS-Block und generische Skriptteile bleiben
unverändert, was ausgetauscht wird, steht in `vorlage/bausteine.md`. Nicht neu erfinden, was dort
schon existiert: Farbtokens, Klassennamen, Aufgaben-Engine, Hilfesystem, Druck-CSS, Export.
Aufbau der Seite, Farbtokens und Definition of Done stehen in `.claude/rules/q1-module.md` im Vault.
Sie laden beim Arbeiten in `module/`.

## Technische Regeln
- Eine Datei pro Thema, alles inline. Keine Imports, keine Build-Tools, keine gemeinsamen Assets.
- Einzige externe Abhängigkeit ist KaTeX über `https://cdn.jsdelivr.net/npm/katex@0.16.9/`. Jede
  Formel steht als `<span class="m" data-tex="…" data-plain="…">`. `data-plain` ist **Pflicht** und
  ohne KaTeX lesbar (Unicode: Φ, Δ, ⁻⁴, ·, ≈). Die Seite funktioniert ohne Netz.
- Speichern nur über den generischen Speicherblock (`vorlage/bausteine.md` § 9), Schlüssel
  `q1lernen:<datei>.html`. Sonst kein `localStorage`, kein `sessionStorage`, keine Cookies. Nichts
  verlässt das Gerät, Ergebnisse gehen nur über den Kopieren-Knopf hinaus. Jedes Modul hat den Knopf
  „Gespeicherten Stand löschen“, die Übersicht einen für alle Module (geteilte Schulrechner).
- Grafik nur mit Canvas oder Inline-SVG, keine Chart- oder Physik-Bibliothek.
- Touch: `pointerdown`/`pointermove` statt Mausereignisse. Canvas mit festen internen Maßen
  (`width="1000"`) und `width:100%` per CSS. Der `@media print`-Block bleibt unverändert.
- Kein Framework, kein jQuery, kein Build-Schritt, keine Minifizierung.

## Fachliche Regeln
- Vor jedem neuen Thema `fachliches/kernlehrplan-nrw.md` lesen. Das Inhaltsfeld steht als Chip im
  Seitenkopf. Keine erfundenen Lehrplanzitate: Unklares als offen markieren und den Nutzer fragen.
- Vorzeichen und Konventionen konsistent halten. Im Induktionsmodul gilt `U_ind = −N·dΦ/dt`,
  das Minuszeichen bleibt stehen.
- Jeder Zahlenwert ist vorher gerechnet, mit Zwischenschritten und Einheitenumrechnung.
- Falsche Antwortoptionen bekommen Feedback, das den typischen Denkfehler benennt. „Leider falsch“
  ist ein Mangel.
- Aufgaben im Anforderungsbereich III verlangen Begründung oder Bewertung, mit Musterlösung **und**
  Bewertungskriterien. Eine längere Rechnung ist kein AFB III.
- Keine Platzhalter, kein Lorem ipsum, keine `TODO`-Kommentare in ausgelieferten Dateien.

## Ordner
```
index.html               Übersichtsseite als Lernpfad, verlinkt alle Module
module/                  die Lernseiten, eine Datei pro Thema
vorlage/                 bausteine.md (Engine-Verträge), Formelleiste, Druck, fallen.md
fachliches/              kernlehrplan-nrw.md, modulliste.md (Status je Modul)
inhalte/                 erarbeitete Modulinhalte als Markdown
pruefung/                Prüfberichte
shots/                   Bildschirmfotos
werkzeug/modulcheck.py   Prüfskript, Teilschritte in werkzeug/pruefschritte/
plan-lernseiten-q1.md    Gesamtkonzept vom 31.08.2026
output/                  Arbeitsdateien und Testskripte, nicht im Repo
_archiv/                 alte Agenten und Übergaben, nicht im Repo, nicht lesen
```
Benennung: `fach-q1-thema.html`, klein, Bindestriche, ohne Umlaute. Präfixe `physik-`, `mathe-`,
`info-`, `mathe-ek-`. Bestehende Module nie überschreiben: Änderungen in der vorhandenen Datei,
ein Ersatz nur unter neuem Namen. Das Referenzmodul nur ändern, wenn der Nutzer es ausdrücklich will.

## Arbeitsweise
- Neues Modul: `/q1-modul <thema>`. Fachprüfung: `/q1-pruefen <modul>`. Den Bericht legt die
  Hauptsitzung unter `pruefung/fach-<modul>.md` ab. Gibt es die Datei schon, `-gegenpruefung`,
  dann `-gegenpruefung-2` anhängen. Berichte nie überschreiben.
- `index.html` und `fachliches/modulliste.md` schreibt nur die Hauptsitzung, nie ein Subagent.
- Prüfskript (auch für `/pruefen`), dauert 5 bis 10 Minuten:
  `python projekte/q1-lernplattform/werkzeug/modulcheck.py projekte/q1-lernplattform/module/DATEI.html`
  Ein zweites Argument legt einen Ordner für Bildschirmfotos an. Ausgabe: JSON mit `blocker` und
  `maengel`. Kein Modul gilt als fertig, solange dort etwas steht.
- Node.js gibt es auf diesem Rechner nicht. Playwright ist das Python-Paket.
- Stand des Projekts: `gedaechtnis/projekt-q1-lernplattform.md` im Vault.
