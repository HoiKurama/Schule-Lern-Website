---
paths:
  - "module/**"
---
# Q1-Module bauen

## Aufbau jeder Seite
Sechs Abschnitte in dieser Reihenfolge, jeder als `<section>` mit nummeriertem `.stufe`-Kopf:

1. **Einstieg:** Aufhänger aus der Lebenswelt, dann 3 Vorwissensfragen (Multiple Choice)
2. **Erklärteil:** schrittweise, Herleitungen in `<details>`, Merksätze abgesetzt
3. **Vertiefung:** zweiter fachlicher Block, falls das Thema es hergibt
4. **Interaktiver Kern:** Simulation mit Beobachtungsauftrag und zwei Verständnisfragen,
   die sich nur mit der Simulation beantworten lassen
5. **Übungen:** mindestens fünf Aufgaben über AFB I bis III, jede mit Hilfe in drei Stufen
   (Tipp → Ansatz → Lösungsweg)
6. **Abschluss:** Zusammenfassung, Hinweis zum Zentralabitur, Selbstcheck, Export, Lehrerteil

Der Lehrerteil (`<details class="lehrer">`) enthält Einordnung, Zeitbedarf, typische Fehler,
Differenzierung und Experimentbezug. Er verschwindet beim Drucken.

## Farben je Fach
Im `:root`-Block werden nur diese drei Tokens getauscht, sonst nichts:

| Fach | `--akzent` | `--akzent-hell` | `--akzent-rand` |
|---|---|---|---|
| Physik | `#1d4ed8` | `#eff6ff` | `#bfdbfe` |
| Mathematik | `#0d7a52` | `#e7f6ef` | `#b5e0cd` |
| Informatik | `#b45309` | `#fef6e7` | `#f3ddb3` |
| Mathe-Erweiterungskurs | `#6d28d9` | `#f4eeff` | `#d9c9f5` |

## Fertig ist ein Modul erst, wenn
1. die Seite ohne Konsolenfehler lädt (Playwright, headless Chromium),
2. ohne Netz jede Formel über `data-plain` lesbar ist,
3. jede interaktive Komponente per Skript angeklickt wurde und richtig reagiert,
4. die Simulation fachlich richtige Werte zeigt, stichprobenartig gegen eine Handrechnung geprüft,
5. alle Musterlösungen nachgerechnet sind,
6. die Druckansicht die Aufgaben und keine Bedienelemente enthält,
7. `fachliches/modulliste.md` auf `fertig` steht.

Punkte 1, 2, 3 und 6 prüft `werkzeug/modulcheck.py`. Punkte 4 und 5 prüft `/q1-pruefen`.
Punkt 7 setzt die Hauptsitzung, nie ein Subagent.
