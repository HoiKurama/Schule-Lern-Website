# Gegenprüfung (Korrekturrunde 1): mathe-q1-abstaende-winkel

Prüfer: fachpruefer (Opus, high), 2026-11-26. Geprüft wurden `module/mathe-q1-abstaende-winkel.html` und
`inhalte/mathe-q1-abstaende-winkel.md` Zeile für Zeile gegen den Erstbericht `fach-mathe-q1-abstaende-winkel.md`.
Alle Werte selbst mit `python3 -c` nachgerechnet, keine Datei geändert.

**Urteil:** bestanden

Modulcheck auf der Endfassung (nach der Korrektur, zweimal gelaufen): 0 Blocker, 0 Mängel, KaTeX 422 von 422,
kein Querscrollen bei 1280, 900 und 390 px, Druckmodi und Formelleiste ohne Befund.

## Befunde aus dem Erstbericht

- **Schwerer Fehler 1 (sim1):** behoben. Option A „… auf der anderen Seite der Ebene“, Feedback „Vorzeichenwechsel von negativ zu positiv“, passt zu Datensatz 1 (w = −4 bei s = 0, +4 bei s = 6).
- **Mangel 1 (Anzeige „Höhe über E“):** behoben. „Weg zu E in x₃-Richtung“, Kästchen „Weg in x₃-Richtung zeigen“, Erklärtext „je nach Lage nach unten oder nach oben“.
- **Mangel 2 (a1):** behoben. tol 0,03, nah-Text nennt zuerst die Rundung. 48,164° angenommen, 47,93° abgelehnt mit passendem Text.
- **Mangel 3 (a4):** behoben. nah-Text spricht zuerst den negativen Winkel (Betrag) an, dann den Kosinus.
- **Mangel 4 (a3):** behoben. Ansatz lässt nur zählen, Zuordnung erst im Lösungsweg.
- **Mangel 5 (windschiefe Geraden):** behoben. Begründung über zwei parallele Ebenen ergänzt, fachlich vollständig.
- **Mangel 6 (α/φ):** behoben. Auf der Seite überall α.
- **Mangel 7 (H doppelt, P nicht eingeführt):** behoben. „Stützpunkt P von g“, Lehrerteil L₁, L₂.
- **Mangel 8 (keine Umkehraufgabe):** behoben. Neue a7, fachlich richtig; Querverweise auf a8, a9 umgestellt.
- **Mangel 9 (Kompetenzbereiche):** behoben.
- **Mangel 10 (33,82°):** behoben.
- **Fragen (Kosinussatz, Startpunkt a4):** unter „Offen“ in der Inhaltsdatei, Antwort von Darren steht aus.

## Neue Befunde

Kein Fehler und kein Mangel. Drei Hinweise:

1. a7 deckt den Lehrerteil-Fehler (6) „nur eine Lösung“ nicht auf, weil die Aufgabe selbst „zwei Werte“ nennt und nur den größeren prüft. Vorschlag: nach dem kleineren Wert fragen oder den Bezug im Lehrerteil abschwächen. *Umgesetzt (Hauptsitzung): Lehrerteil abgeschwächt, mit Hinweis, im Unterricht nach beiden Fällen zu fragen.*
2. Frage: Soll „LE“ für die Koordinate a als falsche Einheit zählen? Fachlich vertretbar. *Offen, nicht geändert.*
3. Inhaltsdatei noch mit „φ“ und „x₃-Höhe“ an einigen Stellen. *Umgesetzt (Hauptsitzung).*

## Nachgerechnet (neue oder geänderte Werte)

| Stelle | Datei | eigenes Ergebnis | ok |
|---|---|---|---|
| a1: 48,164° (cos = 0,667) bei tol 0,03 | angenommen | Abweichung 0,026 | ✓ |
| a1: 48,16° auf der Toleranzgrenze | angenommen | dank eps angenommen | ✓ |
| a1: 47,93° (cos = 0,67) | nah | Faktor 0,995 | ✓ |
| a1: 41,81° (Sinus) | nah | Faktor 0,868 | ✓ |
| a4: −33,85° | nah | Faktor 1,00 | ✓ |
| a4: 56,15° | nah | Faktor 1,66 | ✓ |
| a4: Rundung √29 ≈ 5,39 | 33,82° | 33,820° | ✓ |
| a7: n∘q − d | 2a − 1 | 2a − 1 | ✓ |
| a7: Lösungen | 5 und −4 | 5 und −4, Abstand je 3 | ✓ |
| a7: Seiten | w = 9 und −9 | 9 und −9 | ✓ |
| a7 nah: −4 | Faktor 0,8 | 0,8 | ✓ |
| a7 nah: ohne d | a = 3 | 3, Faktor 0,6 | ✓ |
| a7 weit: ohne Division | a = 2 | 2, Faktor 0,4 | ✓ |
| a7: Vorzeichenfehler bei −x₂ | Text „prüfe den Zähler“ | a = 4, Faktor 0,8, nah | ✓ |
| sim2-Feedback | 0,67 LE, 0,44 pro LE | 0,667; 0,444 | ✓ |
| sim2-Distraktoren | 0,90; 0,50 | 0,896; 0,496 | ✓ |
| Lehrerteil L₁, L₂ | (3\|0\|0), (5\|1\|2), Länge 3 | ebenso | ✓ |

## Fazit

Der schwere Fehler und alle zehn Mängel sind behoben, die neue Aufgabe a7 ist samt Rückmeldungen richtig.
Mit dem sauberen Modulcheck kann das Modul freigegeben werden.
