# Q1-Lernplattform (NRW)

Interaktive HTML-Lernseiten für die Qualifikationsphase 1 an einem Gymnasium in NRW: Physik,
Mathematik, Informatik, Mathe-Erweiterungskurs. Darren (Q1, Mathe- und Physik-LK) lernt damit selbst.
Repo `HoiKurama/Schule-Lern-Website`, **öffentlich** über GitHub Pages. Pfade hier gelten ab diesem Ordner.

## Zielgruppe, gilt für jede Datei
- **Niveau Leistungskurs Q1** nach Kernlehrplan NRW. Maßstab ist das Zentralabitur.
- **Duzen**, durchgehend **Deutsch**, auch in Code-Kommentaren.
- Dezimalkomma in allen angezeigten Zahlen (`toFixed(2).replace(".", ",")`).
- Einheiten SI-konform mit schmalem Abstand vor der Einheit.

## Referenz
`module/physik-q1-induktion.html` ist das Referenzmodul. Jedes neue Modul entsteht als Kopie davon.
Was ausgetauscht wird, steht in `vorlage/bausteine.md`. Nicht neu erfinden, was es dort schon gibt
(Farbtokens, Klassennamen, Aufgaben-Engine, Hilfesystem, Druck-CSS, Export).
Seitenaufbau, Farben je Fach und Definition of Done: `.claude/rules/module.md`.
Bekannte Fehler aus früheren Durchgängen: `vorlage/fallen.md`.

## Technik
- Eine Datei pro Thema, alles inline. Kein Framework, kein Build-Schritt, keine gemeinsamen Assets.
- Einzige externe Abhängigkeit: KaTeX über `https://cdn.jsdelivr.net/npm/katex@0.16.9/`. Jede Formel
  als `<span class="m" data-tex="…" data-plain="…">`. `data-plain` ist Pflicht und ohne Netz lesbar.
- Speichern nur über den Speicherblock (`vorlage/bausteine.md` § 9), Schlüssel `q1lernen:<datei>.html`.
  Sonst kein `localStorage`, keine Cookies. Jedes Modul hat „Gespeicherten Stand löschen“.
- Grafik nur mit Canvas oder Inline-SVG. Touch über `pointerdown`/`pointermove`.
  Canvas mit fester interner Größe (`width="1000"`) und `width:100%`. `@media print` bleibt unverändert.

## Fachlich
- Vor jedem neuen Thema `fachliches/kernlehrplan-nrw.md` lesen. Keine erfundenen Lehrplanzitate,
  Unklares als offen markieren und Darren fragen.
- Jeder Zahlenwert ist vorher mit Python gerechnet, mit Zwischenschritten und Einheiten.
- Vorzeichen konsistent. Im Induktionsmodul gilt `U_ind = −N·dΦ/dt`.
- Falsche Antwortoptionen bekommen Feedback, das den Denkfehler benennt.
- AFB III verlangt Begründung oder Bewertung, mit Musterlösung und Bewertungskriterien.
- Keine Platzhalter und keine `TODO` in fertigen Dateien.

## Ordner
| Ordner | Inhalt |
|---|---|
| `index.html` | Übersicht als Lernpfad. Ändert nur die Hauptsitzung. |
| `module/` | Lernseiten, `fach-q1-thema.html` (`physik-`, `mathe-`, `info-`, `mathe-ek-`) |
| `inhalte/` | erarbeitete Inhalte je Modul als Markdown |
| `vorlage/` | Bausteine, Formelleiste, Druck, `fallen.md` |
| `fachliches/` | `kernlehrplan-nrw.md`, `modulliste.md` (Status je Modul, ändert nur die Hauptsitzung) |
| `pruefung/` | Prüfberichte, nie überschreiben, bei Bedarf `-gegenpruefung`, `-gegenpruefung-2` |
| `spiel/`, `shots/`, `werkzeug/` | Lernspiel, Bildschirmfotos, Prüfskripte |
| `output/` | Arbeitsdateien und Rechenskripte, nicht im Repo |

Bestehende Module nie durch einen Neubau ersetzen: Änderungen in der Datei selbst. Das Referenzmodul
nur ändern, wenn Darren es ausdrücklich will.

## Arbeitsweise
- Neues Modul: `/q1-modul <thema>`. Fachprüfung: `/q1-pruefen <modul>`.
- Technikprüfung (5 bis 10 Minuten, im Hintergrund starten):
  `python3 werkzeug/modulcheck.py module/DATEI.html`. Braucht das Python-Paket Playwright.
  Ein Modul ist nicht fertig, solange in `blocker` oder `maengel` etwas steht.
- **Push nur, wenn Darren es sagt**, denn das Repo ist öffentlich. Vorher prüfen, dass keine Daten
  anderer Personen drinstehen.
- Projektstand: `gedaechtnis/projekt-q1-lernplattform.md` im Repo `HoiKurama/Claude-Vault`.
