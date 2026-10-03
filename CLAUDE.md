# Projekt: Interaktive Lernseiten Q1 (NRW)

Interaktive HTML-Lernseiten für den Unterricht an einem Gymnasium in Nordrhein-Westfalen.
Fächer: Physik, Mathematik, Informatik, Mathematik-Erweiterungskurs. Stufe: Qualifikationsphase 1.

## Zielgruppe – gilt für jede Datei

- **Niveau: Leistungskurs Q1**, ausgerichtet am Kernlehrplan NRW für die gymnasiale Oberstufe.
  Anforderungen entsprechen dem Zentralabitur, nicht dem Schulbuch-Mittelmaß.
- **Anrede: duzen.** „Berechne …", „Was beobachtest du?" Niemals siezen.
- **Sprache: Deutsch**, durchgängig, inklusive Kommentaren im Code.
- Dezimaltrennzeichen in allen angezeigten Zahlen ist das **Komma** (`toFixed(2).replace(".", ",")`).
- Einheiten mit schmalem Abstand vor der Einheit, SI-konform.

## Verbindliche Referenz

`module/physik-q1-induktion.html` ist das Referenzmodul. Es ist fertig, geprüft und im Unterricht einsetzbar.

**Jedes neue Modul entsteht als Kopie dieser Datei.** CSS-Block und die generischen Teile des
Skripts werden **unverändert** übernommen. Was ausgetauscht wird, steht in `vorlage/bausteine.md`.
Ohne diese Datei gelesen zu haben, wird kein Modul gebaut.

Nicht neu erfinden, was dort schon existiert: Farbtokens, Klassennamen, Aufgaben-Engine,
Hilfesystem, Druck-CSS, Export-Funktion.

## Aufbau jeder Seite

Sechs Abschnitte in dieser Reihenfolge, jeder mit `<section>` und nummeriertem `.stufe`-Kopf:

1. **Einstieg** – konkreter Aufhänger aus der Lebenswelt, dann 3 Vorwissensfragen (Multiple Choice)
2. **Erklärteil** – schrittweise, Herleitungen in `<details>`, Merksätze abgesetzt
3. **Vertiefung** – zweiter fachlicher Block, sofern das Thema es hergibt
4. **Interaktiver Kern** – Simulation oder Visualisierung, immer mit Beobachtungsauftrag
   und zwei anschließenden Verständnisfragen, die sich nur mit der Simulation beantworten lassen
5. **Übungen** – mindestens fünf Aufgaben, verteilt über die Anforderungsbereiche I, II und III,
   jede mit dreistufigem Hilfesystem (Tipp → Ansatz → Lösungsweg)
6. **Abschluss** – Zusammenfassung, Hinweis zum Zentralabitur, Selbstcheck, Export, Lehrerteil

Der Lehrerteil (`<details class="lehrer">`) enthält Einordnung, Zeitbedarf, typische Schülerfehler,
Differenzierung und Experimentbezug. Er verschwindet beim Drucken.

## Technische Regeln

- **Eine Datei pro Thema.** Alles inline: CSS im `<style>`, JS im `<script>`. Keine Imports,
  keine Build-Tools, keine gemeinsamen Assets.
- **Einzige erlaubte externe Abhängigkeit ist KaTeX** über
  `https://cdn.jsdelivr.net/npm/katex@0.16.9/`. Jede Formel steht als
  `<span class="m" data-tex="…" data-plain="…">` im Markup. `data-plain` ist **Pflicht** und muss
  ohne KaTeX lesbar sein (Unicode: Φ, Δ, ⁻⁴, ·, ≈). Die Seite muss ohne Netz funktionieren.
- **Speichern nur über den generischen Speicherblock.** Er legt den Bearbeitungsstand eines
  Moduls im `localStorage` dieses Browsers ab (Schlüssel `q1lernen:<datei>.html`), spielt ihn
  beim Laden über die Engine wieder ein und liefert der Übersicht eine Kurzbilanz. Sonst kein
  `localStorage`, kein `sessionStorage`, keine Cookies. Nichts verlässt das Gerät; Ergebnisse
  gehen nur über den Kopieren-Button hinaus. Jedes Modul hat den Knopf „Gespeicherten Stand
  löschen“, die Übersicht einen für alle Module (gemeinsam genutzte Schulrechner).
- **Grafik ausschließlich mit Canvas oder Inline-SVG.** Keine Chart- oder Physik-Bibliothek.
- **Touch-tauglich**: `pointerdown`/`pointermove` statt `mousedown`/`mousemove`.
- **Responsiv**: Canvas mit festen internen Maßen (`width="1000"`) und `width:100%` per CSS.
- **Druckbar**: Der `@media print`-Block wird unverändert übernommen.
- Kein Framework, kein jQuery, kein Build-Schritt, keine Minifizierung.

## Fachliche Regeln

- Vor jedem neuen Thema `fachliches/kernlehrplan-nrw.md` lesen und die Einordnung im Seitenkopf
  als Chip angeben (Inhaltsfeld laut Kernlehrplan).
- **Vorzeichen und Konventionen konsistent halten.** Im Induktionsmodul gilt
  `U_ind = −N·dΦ/dt`; das Minuszeichen wird nicht stillschweigend weggelassen.
- Bei jeder gerechneten Musterlösung muss der Zahlenwert stimmen. Rechne nach, bevor du ihn
  in die Datei schreibst – auch Zwischenschritte und Einheitenumrechnungen.
- Falsche Antwortoptionen bekommen **inhaltliches Feedback**, das den typischen Denkfehler benennt.
  Ein bloßes „Leider falsch" ist ein Mangel und wird zurückgewiesen.
- Aufgaben im Anforderungsbereich III sind Begründungs- oder Bewertungsaufgaben mit
  Musterlösung **und** Bewertungskriterien, keine längeren Rechnungen.

## Dateiorganisation

```
CLAUDE.md                    diese Datei
plan-lernseiten-q1.md        Gesamtkonzept
prompt-claude-code.md        Arbeitsauftrag mit Subagenten
index.html                   Übersichtsseite, verlinkt alle Module
module/                      die Lernseiten, eine Datei pro Thema
vorlage/bausteine.md         Aufgabenbausteine, Engine-Verträge, Kopiervorlagen
fachliches/kernlehrplan-nrw.md   Inhaltsfelder und Kompetenzen NRW
fachliches/modulliste.md     alle geplanten Module mit Status
agenten/                     Subagenten-Definitionen, beim ersten Lauf nach .claude/agents/ kopieren
inhalte/                     Zwischenstand: erarbeitete Modulinhalte als Markdown
pruefung/                    Prüfberichte der Kontrollagenten
werkzeug/modulcheck.py       automatischer Modulcheck, siehe unten
```

### Der Modulcheck

`werkzeug/modulcheck.py` prüft ein fertiges Modul mit Playwright im Browser und meldet, was
kein Blick in den Quelltext findet:

```bash
PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/DATEI.html"
```

Geprüft werden Konsole und `pageerror`, die Engine-Verträge (Optionszahl gegen Feedbackzahl,
Lücken in `data-i`, Radio-Namen, fehlende Rückmeldungstexte), alle Fälle jeder Zahleneingabe,
die Zuordnung in beiden Richtungen, jede Hilfestufe, jeder Regler über seinen ganzen Bereich,
der Export, die Druckansicht, der Offline-Fallback über `data-plain` und waagerechtes Scrollen
bei 1280, 900 und 390 px. Ausgabe ist JSON mit `blocker` und `maengel`.

**Maßstab: kein Modul gilt als fertig, solange hier etwas steht.** Ein zweites Argument legt
einen Ordner für Bildschirmfotos an. Node.js gibt es auf diesem Rechner nicht — Playwright ist
das Python-Paket.

Benennung: `fach-q1-thema.html`, kleingeschrieben, Bindestriche, keine Umlaute.
Beispiele: `physik-q1-induktion.html`, `mathe-q1-hauptsatz.html`, `info-q1-baeume.html`.
Präfixe: `physik-`, `mathe-`, `info-`, `mathe-ek-`.

**Bestehende Module werden nie überschrieben.** Änderungswünsche werden in der vorhandenen
Datei eingearbeitet; ein Ersatz entsteht nur als neue, anders benannte Datei.

## Farbtokens pro Fach

Im `:root`-Block wird nur `--akzent` und `--akzent-hell`/`--akzent-rand` getauscht, sonst nichts:

| Fach | `--akzent` | `--akzent-hell` | `--akzent-rand` |
|---|---|---|---|
| Physik | `#1d4ed8` | `#eff6ff` | `#bfdbfe` |
| Mathematik | `#0d7a52` | `#e7f6ef` | `#b5e0cd` |
| Informatik | `#b45309` | `#fef6e7` | `#f3ddb3` |
| Mathe-Erweiterungskurs | `#6d28d9` | `#f4eeff` | `#d9c9f5` |

Der Kopfverlauf in `header.kopf` wird passend zum Akzent angepasst, alles andere bleibt.

## Definition of Done

Ein Modul gilt erst als fertig, wenn **alle** Punkte erfüllt sind:

1. Die Seite lädt ohne Fehler in der Konsole (Playwright, headless Chromium).
2. Ohne Netzverbindung ist jede Formel über `data-plain` lesbar.
3. Jede interaktive Komponente wurde per Skript angeklickt und reagiert korrekt.
4. Die Simulation zeigt physikalisch bzw. mathematisch richtige Werte – stichprobenartig gegen
   eine Handrechnung geprüft, nicht nur „sie bewegt sich".
5. Alle Musterlösungen sind nachgerechnet.
6. Die Druckansicht enthält die Aufgaben und keine Bedienelemente.
7. Der Eintrag in `fachliches/modulliste.md` steht auf `fertig`.

## Was nicht getan wird

- Keine Änderungen am Referenzmodul, außer sie sind ausdrücklich beauftragt.
- Keine neuen Abhängigkeiten, auch nicht „nur für die Formeln" oder „nur für die Animation".
- Keine Platzhalterinhalte, kein Lorem ipsum, keine `TODO`-Kommentare in ausgelieferten Dateien.
- Keine erfundenen Kernlehrplan-Zitate. Wenn eine Zuordnung unklar ist, wird sie als offen
  markiert und nachgefragt, statt sie zu erfinden.
- Keine Aufgaben, deren Lösung nicht vorher gerechnet wurde.
