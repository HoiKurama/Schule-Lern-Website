---
name: q1-modul
description: Neues Q1-Lernmodul von Inhalt über Bau bis Prüfung. Nur auf Aufruf mit /q1-modul <thema>.
argument-hint: <thema>
disable-model-invocation: true
---
Baue ein Q1-Modul zum Thema „$ARGUMENTS“. Melde Darren nach jedem Schritt eine Zeile Zwischenstand.

## 1. Vorbereiten
- `fachliches/modulliste.md` lesen und das Thema einem Eintrag zuordnen. Daraus folgt `<modul>`,
  z. B. `mathe-q1-abstaende-winkel`. Fehlt der Eintrag oder ist Niveau oder Unterthema unklar:
  Darren fragen und warten.
- Status in der Modulliste auf `in Arbeit`.

## 2. Inhalt
Arbeite nach `${CLAUDE_SKILL_DIR}/inhalt.md`. Ergebnis: `inhalte/<modul>.md`.
Stehen unter „Offen“ Lehrplanfragen, die den Inhalt ändern würden: Darren fragen, bevor gebaut wird.

## 3. Bau
Arbeite nach `${CLAUDE_SKILL_DIR}/bau.md`. Ergebnis: `module/<modul>.html`. Danach Status `prüfung`.

## 4. Technikprüfung
Im Hintergrund starten, dauert 5 bis 10 Minuten:
`python3 werkzeug/modulcheck.py module/<modul>.html`

## 5. Fachprüfung
Agent `fachpruefer` mit dem Auftrag: „Prüfe `<modul>` nach `.claude/skills/q1-pruefen/SKILL.md`.
Modulcheck-Ergebnis: …“. Den Bericht unter `pruefung/fach-<modul>.md` ablegen, nie überschreiben.

## 6. Korrektur, höchstens 2 Runden
- Fachliche Fehler zuerst in `inhalte/<modul>.md` korrigieren, dann in die Seite übertragen.
- Danach Modulcheck und Fachprüfung nur für die beanstandeten Punkte wiederholen.
- Nach der zweiten Runde aufhören. Status bleibt `prüfung`, Darren entscheidet über den Rest.

## 7. Abschluss
Nur wenn der Modulcheck sauber ist und das Urteil „bestanden“ lautet:
- `fachliches/modulliste.md` auf `fertig`, in `index.html` das Modul nach dem Muster eines fertigen freischalten.
- Committen. Nicht pushen, das Repo ist öffentlich.
- Bericht an Darren, höchstens 8 Zeilen: Datei, Urteil, Modulcheck, offene Fragen.
- Stand in `gedaechtnis/projekt-q1-lernplattform.md` im Vault aktualisieren, falls der Vault erreichbar ist.

Ein Modul pro Aufruf. Was zählt, sind Modulcheck und Fachprüfung, nicht die eigene Einschätzung.
