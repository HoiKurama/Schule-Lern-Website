# Prüfbericht: module/info-q1-lineare-strukturen.html

Fach: Informatik · Leistungskurs Q1 · Inhaltsfeld „Daten und ihre Strukturierung"
Prüfdatum: 2026-09-07
Prüfgrundlage: `inhalte/info-q1-lineare-strukturen.md` (abgenommen), `fachliches/kernlehrplan-nrw.md`,
Vorgaben zum Zentralabitur NRW (bereitgestellte Klassen `List`, `Queue`, `Stack`)
Werkzeuge: Playwright/Chromium headless (Zustandsmodell, Aufgaben-Engine, Druckansicht),
Python-Nachrechnungen aller Zahlenwerte, Zeile-für-Zeile-Lesung der Simulations-IIFE (1322 bis 1928)

## Urteil

**Nacharbeit nötig.**

Fachlich ist das Modul tragfähig: Das Zustandsmodell der Simulation ist echt, alle drei harten
Prüfkriterien werden exakt getroffen, sämtliche Zahlenwerte stimmen, die drei Abitur-Randfälle der
`List`-Schnittstelle sind korrekt umgesetzt, und die beiden AB-III-Aufgaben sind echte Begründungs-
und Bewertungsaufgaben. Drei Befunde müssen aber vor dem Einsatz behoben werden: eine falsche
Fußzeile aus dem Referenzmodul, ein Widerspruch zwischen dem Kostenmodell in Abschnitt 4 und den
Zählern der Simulation, und eine sachlich falsche Aussage im Beobachtungsauftrag. Alle drei sind
kleine, klar umgrenzte Änderungen.

## Schwere Fehler

### S1 · Fußzeile nennt Fach und Thema des Referenzmoduls — Zeile 1146

Dort steht: „Physik LK Q1 · Elektromagnetische Induktion · erstellt für den Unterricht nach dem
Kernlehrplan NRW für die gymnasiale Oberstufe." Das ist wörtlich die Fußzeile aus
`module/physik-q1-induktion.html:577`, beim Kopieren nicht ausgetauscht.

Der Fehler ist nicht kosmetisch: Der `footer` wird im `@media print`-Block nicht ausgeblendet — per
`emulate_media(media="print")` verifiziert —, das ausgedruckte Arbeitsblatt trägt also
„Physik LK Q1 · Elektromagnetische Induktion" unter einer Informatikaufgabe. Verstößt zugleich gegen
„Keine Platzhalterinhalte" aus `CLAUDE.md`.

*Korrektur:* „Informatik LK Q1 · Lineare Datenstrukturen · erstellt für den Unterricht nach dem
Kernlehrplan NRW für die gymnasiale Oberstufe."

### S2 · Das Kostenmodell in Abschnitt 4 widerspricht den Zählern der Simulation — Zeile 692/694 gegen 1691 bis 1716

Abschnitt 4.5 sagt: „kostet der Weg zum Element mit Index k genau k+1 Knotenbesuche: einen für
`toFirst()` und k weitere für die `next()`-Aufrufe" und leitet daraus den Mittelwert 600,5 ab.
Aufgabe a3 definiert den Knotenbesuch operativ (Zeile 903): „jede Auswertung, die den Hilfszeiger
`lauf` auf einen Knoten setzt, `lauf = anfang` eingeschlossen."

Die Simulation zählt bei `toFirst` (1691 bis 1699) und `next` (1701 bis 1716) jedoch
**2 Referenzänderungen und 0 Knotenbesuche**. Gemessen (Playwright, Liste, Schrittmodus aus):

| Aktion | Referenzänderungen | besuchte Knoten |
|---|---|---|
| 5 mal `append` aus dem leeren Zustand | 5 | 10 |
| danach `toFirst()` | 7 | **10 (unverändert)** |
| danach 3 mal `next()` | 13 | **10 (unverändert)** |

Nach Abschnitt 4.5 müsste der Zugriff auf das Element mit Index 3 vier Knotenbesuche kosten; die
Simulation zeigt null. Damit ist die zentrale Aussage von 4.5 — der Grund für das O(n) in der
Laufzeittabelle Zeile 653 und für den Wert 600,5 — am interaktiven Kern nicht überprüfbar, sondern
wird dort scheinbar widerlegt. Dasselbe Wandern eines Zeigers entlang der Kette zählt in `append`
(1727 bis 1736) als Knotenbesuch, in `next` als Referenzänderung.

*Korrektur (minimal, im Quelltext):* in `bauSchritte` bei `op === "toFirst"` im `tu` des ersten
Schritts `if(S.kopf) zBes++;` ergänzen und bei `op === "next"` im `tu` des Schritts
`aktuell = aktuell.gibNachfolger();` ein `zBes++;`. Dann liefert `toFirst()` plus 3 mal `next()`
genau 4 Besuche, wie Abschnitt 4.5 es behauptet. Alternativ Abschnitt 4.5 umformulieren — dann
müsste aber auch die Definition in a3 nachgezogen werden, was die schlechtere Lösung wäre.

*Hinweis:* Die abgenommene Inhaltsdatei trägt denselben Widerspruch (Zeilen 821/829 gegen
1108/1120). Das Modul folgt der Vorgabe korrekt; die Vorgabe ist an dieser Stelle in sich
widersprüchlich und sollte mitkorrigiert werden.

### S3 · Der Beobachtungsauftrag behauptet eine Eindeutigkeit, die es nicht gibt — Zeile 761

Dort steht: „Zwei der drei Ketten sehen am Ende gleich aus, eine nicht. Und **genau** die Struktur
mit der abweichenden Kette hat den Zähler ‚besuchte Knoten' auf null."

Die abweichende Kette hat der Stapel (E, D, C, B, A). Der Zähler steht dort auf 0 — aber bei der
**Schlange ebenfalls auf 0** (gemessen, siehe Tabelle unter „Nachgerechnet"). Die Formulierung
„genau die Struktur" ist damit falsch, und Lernende, die den Auftrag gewissenhaft ausführen, stoßen
unmittelbar auf den Widerspruch.

Schwerer wiegt: Der Satz lenkt vom didaktischen Kern weg. Der eigentliche Ertrag der Übung ist,
dass **Schlange und Liste dieselbe Kette A, B, C, D, E erzeugen, aber 0 gegen 10 Knotenbesuche
kosten** — gleiches Ergebnis, völlig verschiedener Aufwand. Genau das trägt Abschnitt 4 und
Aufgabe a3. Der jetzige Auftrag führt stattdessen auf eine Aussage über den Stapel.

*Korrektur:* „Zwei der drei Ketten sehen am Ende gleich aus, eine nicht. Vergleiche für die beiden
gleich aussehenden Ketten den Zähler ‚besuchte Knoten' — er unterscheidet sich um 10. Schreibe
einen Satz auf, der erklärt, wie dasselbe Ergebnis zu so verschiedenen Kosten kommen kann."
Die Verständnisfrage `sim2` (Zeile 832) trägt diesen Kern bereits richtig und bleibt unverändert.

## Mängel

### M1 · Toleranz bei a4 zu großzügig — Zeile 1258

`trefferAlt = Math.abs(v - 4.8) <= 4.8 * 0.03` lässt 4,656 bis 4,944 kB durchgehen. Gemessen:
**4,7 kB und 4,9 kB werden als „Richtig" gewertet.** Der gesuchte Wert ist exakt, eine
3-Prozent-Spanne ist hier unbegründet und lässt Rechenfehler durch.
*Korrektur:* ein Feld `d.alt.tol = 0.05` einführen und statt der Relativspanne verwenden.

### M2 · Das treffendste Feedback bei a4 ist unerreichbar — Zeile 1265/1267

Der `nah`-Text ist eigens für den häufigsten Fehler geschrieben: „Vermutlich hast du den
Gesamtbedarf der Kette statt des Mehrbedarfs angegeben — das wären 9600 B." Für die Eingabe 9600 B
ist `faktor = 9600/4800 = 2,0`; die Bedingung `faktor > 0.5 && faktor < 2` ist damit **falsch**, und
der Lernende erhält den unpassenden `weit`-Text. Gemessen und bestätigt.
*Korrektur:* `faktor < 2.05` statt `faktor < 2` in Zeile 1267.

### M3 · `insert` in die leere Liste weicht vom gedruckten Java-Code ab — 1743 bis 1768 gegen 537 bis 547

Der Java-Block in Abschnitt 3 macht in diesem Zweig genau **eine** Referenzänderung
(`anfang = new Knoten(pInhalt); return;`) und lässt `vorgaenger` unberührt. Die Simulation läuft
stattdessen in den allgemeinen Zweig: Sie zeigt die Zeilen `neu.setzeNachfolger(aktuell);`,
`anfang = neu;` und `vorgaenger = neu;`, zählt **3 Referenzänderungen** (gemessen) und hinterlässt
den Zustand „aktuell: null; vorgaenger: A" — ein Vorgänger ohne aktuelles Objekt. Zeile 757
verspricht ausdrücklich, pro Klick werde „genau eine Java-Zeile" ausgeführt; hier sind es Zeilen,
die in diesem Zweig des abgedruckten Codes nicht vorkommen. Kette und `hasAccess()` bleiben korrekt,
der Schaden ist also begrenzt — aber es ist genau der Randfall, den der Hinweiskasten Zeile 358 als
prüfungsrelevant heraushebt.
*Korrektur:* in `bauSchritte` bei `op === "insert"` einen dritten Zweig für `!S.aktuell && !S.kopf`
mit einem einzigen Schritt `anfang = new Knoten("x");` und `zRef++`.

### M4 · Zeitbedarf im Lehrerteil unterschlägt a7 und a8 — Zeile 1139

„Übungen 20" Minuten für acht Aufgaben, darunter zwei Aufsätze im AB III. Die abgenommene
Inhaltsdatei legt in 1985 bis 1989 ausdrücklich fest, dass a7 und a8 **nicht** in den 135 Minuten
enthalten und als Hausaufgabe mit je etwa 20 Minuten Bearbeitung gedacht sind. Dieser Satz fehlt im
Modul; der Kopfchip „ca. 135 Minuten" wirkt dadurch zu optimistisch. Abweichung von der Vorgabe.
*Korrektur:* einen Satz nach der Minutenaufstellung ergänzen: „Die beiden Aufgaben im
Anforderungsbereich III (a7, a8) sind darin nicht enthalten; sie sind als Hausaufgabe mit je etwa
20 Minuten und anschließender Besprechung gedacht."

### M5 · `sim1` und `sim2` als AB II ausgezeichnet — Zeile 822 und 833

Beide Fragen verlangen, eine unmittelbar zuvor am Bildschirm abgelesene Beobachtung wiederzugeben
(wo steht der Kopfzeiger; welche drei Zahlen zeigt ein Zähler). Das ist Anforderungsbereich I.
Kein Etikettenschwindel im Sinne eines aufgeblähten AB III, aber eine Stufe zu hoch. Der Wert der
Fragen ist unbestritten — sie sind ohne die Simulation nicht beantwortbar, wie die Vorgabe es
verlangt.
*Korrektur:* beide auf „Anforderungsbereich I" setzen.

### M6 · Eingabefeld springt im Schrittmodus zu früh weiter — Zeile 1824

`naechsterBuchstabe()` wird am Ende von `bauSchritte` aufgerufen, also beim **Bauen** der
Schrittfolge. Im Schrittmodus zeigt das Feld schon „B", während der Knoten „A" noch gar nicht
angelegt ist. Rein kosmetisch, aber irritierend beim Vorführen von Schritt 1.
*Korrektur:* den Aufruf in das `tu` des letzten Schritts verschieben.

### M7 · Uneinheitliche Generics in der Schnittstellentabelle — Zeile 352

`void concat(List pList)` steht ohne Typparameter, während dieselbe Tabelle sonst `ContentType`
verwendet und Zeile 311 die generische Schreibweise korrekt mit `Stack&lt;Auftrag&gt;` einführt.
*Korrektur:* `void concat(List&lt;ContentType&gt; pList)`.

### M8 · Statuseintrag steht noch auf „in Arbeit" — `fachliches/modulliste.md:44`

Punkt 7 der Definition of Done verlangt „fertig". Nicht von mir geändert (Arbeitsteilung).

## Nachgerechnet

Alle Werte mit Python bzw. per Playwright gegen die laufende Seite geprüft.

| Fundstelle | Größe | mein Wert | Wert der Datei | Urteil |
|---|---|---|---|---|
| Sim, harte Vorgabe | 5 mal `push` aus leer: Kette | E, D, C, B, A | E, D, C, B, A | ok |
| Sim | 5 mal `push`: Referenzänderungen / Besuche | 10 / 0 | 10 / 0 | ok |
| Sim | 5 mal `enqueue`: Kette | A, B, C, D, E | A, B, C, D, E | ok |
| Sim | 5 mal `enqueue`: Referenzänderungen / Besuche | 10 / 0 | 10 / 0 | ok |
| Sim | 5 mal `append`: Kette | A, B, C, D, E | A, B, C, D, E | ok |
| Sim | 5 mal `append`: Referenzänderungen / Besuche | 5 / 10 (0+1+2+3+4) | 5 / 10 | ok |
| 1691–1716 | `toFirst()` + 3 mal `next()`: Besuche | 4 (nach Text 692) | 0 | **falsch, S2** |
| 761 | Struktur(en) mit Zähler „besuchte Knoten" = 0 | Stapel **und** Schlange | „genau" eine | **falsch, S3** |
| 672 | Aufbau mit n = 1200 mal `append` | 1200·1199/2 = 719 400 | 719 400 | ok |
| 670 | Kosten eines `append` bei n Knoten | n = 1 + (n−1) | n | ok |
| 694 | mittlerer Zugriff, 1200 Elemente | (1+1200)/2 = 600,5 | 600,5 | ok |
| 680 | S_Kette = 1200 · (4 B + 4 B) | 9600 B = 9,6 kB | 9600 B = 9,6 kB | ok |
| 682 | S_Array = 1200 · 4 B | 4800 B = 4,8 kB | 4800 B = 4,8 kB | ok |
| 684/948 | Mehrbedarf und Faktor | 4800 B = 4,8 kB, Faktor 2 | 4,8 kB, Faktor 2 | ok |
| 730/731 | Breitensuche im 6×6-Gitter | 10 Schritte, Weg identisch | 10 Schritte | ok |
| 735/736 | Tiefensuche, Nachbarn rechts/unten/links/oben | 14 Schritte, Weg identisch | 14 Schritte | ok |
| 1085/1090 | Umweg der Tiefensuche | 4 Schritte = 40 % | 4 Schritte = 40 % | ok |
| a1 (873/1221) | Stapel nach 8 Befehlen | A, E → 2 Elemente, `top()` = E | 2 Elemente, E | ok |
| a2 (898/1226) | Referenzänderungen durch `insert` | 3; Ergebnis A, X, B, C, aktuell = B | 3 | ok |
| a3 (923/1231) | 3 mal `append` ab 1200 Knoten | 1200+1201+1202 = 3603 = 3·1201 | 3603 | ok |
| a4 (948/1236) | Speicher-Mehrbedarf | 4800 B bzw. 4,8 kB | 4800 B / 4,8 kB | ok |
| a4 Toleranz | akzeptierter kB-Bereich | soll etwa 4,80 | 4,656 bis 4,944 | **zu weit, M1** |
| a4 Feedback | Eingabe 9600 B | `nah` erwartet | `weit` ausgegeben | **falsch, M2** |
| a7 (1067) | `([])` mit Schlange | fälschlich abgelehnt | fälschlich abgelehnt | ok |
| a7 (1068) | `([)]` mit Schlange | fälschlich angenommen | fälschlich angenommen | ok |
| `insert` leere Liste | Referenzänderungen laut Java 537–547 | 1 | Sim zählt 3 | **abweichend, M3** |
| `insert` vor aktuell | `toFirst(); insert("B")` bei Kette A | B, A · aktuell = A | B, A · aktuell = A | ok |
| `insert` ohne aktuell | nicht leere Liste | unverändert | unverändert | ok |
| `remove` | A, B, C mit aktuell = B | A, C · aktuell = C | A, C · aktuell = C | ok |
| `remove` letzter Knoten | `hasAccess()` danach | false, `getContent()` = null | aktuell null, Rückgabe null | ok |
| MC-Lösungen | vw1 / vw2 / vw3 / sim1 / sim2 / a5 | 1 / 2 / 0 / 1 / 0 / 1 | identisch | ok |
| a6 | Zuordnung der vier Anwendungen | A, D, C, B | A, D, C, B | ok |
| KaTeX | Formeln mit `data-plain` | 79 von 79 gerendert, alle mit `data-plain` | — | ok |
| Konsole | Fehler beim Laden und bei allen Klicks | keine | — | ok |
| Druck | Lehrerteil / Steuerung / Hilfebuttons | ausgeblendet | ausgeblendet | ok |
| Druck | Aufgabenstellungen | sichtbar | sichtbar | ok |
| Druck | Fußzeile | „Physik LK Q1 · Induktion" | — | **falsch, S1** |

## Gut gelöst

**Das Zustandsmodell ist echt — der zentrale Prüfpunkt ist bestanden.** `Knoten` (1345 bis 1349) ist
ein Objekt mit `inhalt` und `nachfolger`; der gesamte Zustand liegt in
`S = {kopf, ende, aktuell, vorgaenger}` (1350). `kette()` (1358 bis 1362) erzeugt die
Zeichenreihenfolge **ausschließlich** durch `n = n.nachfolger` ab `S.kopf`, `layout()` (1366 bis
1379) leitet die x-Positionen erst daraus ab. Es existiert kein paralleles Array, das die
Reihenfolge vorgäbe; der Sicherheitszähler `sicher++ < 60` fängt lediglich Zyklen ab. Alle
Operationen manipulieren echte Referenzen, kein `splice`, kein `sort`. Das ist genau die Bauart, die
das Thema verlangt.

**Die drei Abitur-Randfälle sind korrekt implementiert und ausdrücklich benannt.** Der Hinweiskasten
Zeile 358 formuliert alle drei sauber, die Java-Klasse 537 bis 573 setzt sie um, und die Simulation
verhält sich messbar genauso (Ausnahme: der Zählerwert im Leerlisten-Zweig, M3). Dass `insert` das
aktuelle Objekt unverändert lässt und `remove` den Nachfolger zum aktuellen Objekt macht, wird nicht
behauptet, sondern ist am Modell vorführbar.

**Jeder Distraktor benennt einen Denkfehler, keiner sagt nur „falsch".** `mcDaten` 1171 bis 1201.
Am stärksten `a5`, Option 2 (Zeile 1200): Sie erklärt nicht nur, warum die Antwort falsch ist,
sondern unter welcher Bedingung sie richtig wäre — „Fragte `enqueue` stattdessen `ende == null`
ab […], liefe die Methode in den Else-Zweig". Auch `vw3`, Option 2 (1185) trennt sauber zwischen
Übersetzungs- und Laufzeitfehler.

**a7 und a8 sind echte AB-III-Aufgaben.** Keine verlängerte Rechnung: a7 verlangt eine Stellungnahme
plus zwei selbst konstruierte Gegenbeispiele in beide Fehlerrichtungen, a8 eine Abwägung zweier
begründeter Positionen. Beide haben Bewertungskriterien, die auf die Argumentationsstruktur zielen
(„benennt LIFO als die Reihenfolge, die Schachtelung überhaupt ausmacht"), nicht auf das Ergebnis.
a8 lässt die Gegenentscheidung ausdrücklich als vollwertig zu, wenn die Abwägung explizit gemacht
wird (1092) — das ist genau die Offenheit, die eine Bewertungsaufgabe braucht.

**Die Modellrechnung sagt selbst, was sie nicht kann.** Der Kasten Zeile 687 nennt Objektkopf und
8-Byte-Ausrichtung, beziffert den realen Faktor auf vier bis fünf und gibt den Lernenden die
Formulierung „in diesem Modell" mit. Vorbildlich für eine Modellierungsaufgabe.

**Das Labyrinth-Beispiel hält der Nachrechnung stand.** Beide Wege stimmen Feld für Feld mit meiner
Nachrechnung überein — bei Nachbarreihenfolge rechts, unten, links, oben, wie Zeile 723 sie angibt.
Dass diese Reihenfolge überhaupt genannt wird, ist entscheidend: ohne sie wäre der Tiefensuchweg
nicht reproduzierbar. Das ist die Sorgfalt, an der solche Beispiele meist scheitern.

**Der Lehrerteil ist brauchbar, nicht dekorativ.** Fünf konkret benannte Hürden mit Anhaltepunkten,
Differenzierung in beide Richtungen und das Menschenmodell (1142) — sechs Lernende als Knoten, eine
Hand auf der Schulter, der zu Löschende kann sich nicht selbst aushängen. Das ist eine echte
Handlungserfahrung für ein Thema ohne Realexperiment.

**Die drei Hilfestufen sind wirklich abgestuft.** Bei a1 bis a4 gibt Stufe 1 nur ein Verfahren vor
(„Schreibe den Stapel nach jedem einzelnen Befehl auf"), Stufe 2 den Ansatz mit Formel, Stufe 3 die
gerechnete Lösung. Kein Tipp verrät das Ergebnis. Bei a7 nennt Stufe 3 die beiden Testausdrücke,
verlangt aber weiterhin die eigene Argumentation; die Musterlösung liegt getrennt hinter einem
eigenen Knopf.

**Kopfchip, Sprache, Technik.** Das Inhaltsfeld „Daten und ihre Strukturierung" ist wörtlich aus
`fachliches/kernlehrplan-nrw.md:58` übernommen — keine erfundene Zuordnung, kein erfundenes Zitat,
und die Aussage zu den im Zentralabitur bereitgestellten Klassen (310, 1115) ist korrekt und nicht
überdehnt. Das Thema gehört laut Kernlehrplandatei (Zeile 68) in die Q1. Durchgehend geduzt; die
Treffer auf „Sie" sind ausnahmslos Personalpronomen zu femininen Substantiven. Komma als
Dezimaltrennzeichen in allen angezeigten Zahlen (`fmt()`, Zeile 1337). Alle 79 Formeln haben
`data-plain`. Der Java-Code ist von Hand geprüft und BlueJ-übersetzbar, einschließlich des Zugriffs
auf private Attribute eines anderen Objekts derselben Klasse in `concat`; `<` und `>` sind an der
einzigen nötigen Stelle korrekt als `&lt;`/`&gt;` maskiert (Zeile 311). Keine externe Abhängigkeit
außer KaTeX, kein `localStorage`.

## Fazit

Das Modul kann in den Unterricht, sobald drei Stellen geändert sind, und die Änderungen sind klein.
Fachlich trägt es: Die Simulation ist ein echtes Zeigermodell und kein nachgestelltes Array, alle
harten Prüfkriterien werden auf den Punkt getroffen, jeder nachgerechnete Zahlenwert stimmt, und die
beiden AB-III-Aufgaben sind das, was ihr Etikett verspricht. Die drei schweren Befunde sind eine
vergessene Fußzeile aus dem Referenzmodul, ein Widerspruch zwischen dem Kostenbegriff in Abschnitt 4
und den Zählern für `toFirst` und `next`, und ein Beobachtungsauftrag, dessen Kernsatz an der
eigenen Simulation scheitert und dabei den didaktisch wichtigsten Vergleich verschenkt. Der zweite
und der dritte Befund stecken bereits in der abgenommenen Inhaltsdatei und sollten dort
mitkorrigiert werden, damit sie nicht in Folgemodule wandern. Rechnet man einen Arbeitsdurchgang für
S1 bis S3 und die Kleinigkeiten M1 bis M7 ein, ist das Modul danach ohne Vorbehalt einsetzbar.

## Gegenprüfung nach der Nacharbeit

Prüfdatum: 2026-09-08. Gegenstand ist ausschließlich die Nacharbeit: die Befunde S1 bis S3 und
M1 bis M8, die fachliche Konsequenz der Zählerkorrektur und die zweimal geänderte gemeinsame
Aufgaben-Engine. Keine erneute Vollprüfung. Werkzeuge: Quelltextlesung, Playwright/Chromium,
Python-Nachrechnung.

### Abgearbeitete Befunde im Quelltext

- **S1 · behoben** — Zeile 1146. Die Fußzeile lautet jetzt „Informatik LK Q1 · Lineare
  Datenstrukturen · erstellt für den Unterricht nach dem Kernlehrplan NRW für die gymnasiale
  Oberstufe." Fach, Thema und Wortlaut stimmen; kein Rest des Referenzmoduls mehr.
- **S3 · behoben** — Zeile 761. Der falsche Satz „genau die Struktur mit der abweichenden Kette"
  ist ersetzt durch den Vergleich der beiden gleich aussehenden Ketten mit der Differenz 10 im
  Zähler „besuchte Knoten" und dem Auftrag, den Unterschied in einem Satz zu erklären. Die
  Aussage ist an der Simulation nachprüfbar (Schlange 0, Liste 10, siehe Messtabelle) und trifft
  jetzt den didaktischen Kern, den `sim2` und Abschnitt 4 tragen. Beobachtungsauftrag beantwortbar.
- **M2 · behoben** — Zeile 1281: `(faktor > 0.5 && faktor < 2.05) ? d.nah : d.weit`. Die Eingabe
  9600 B liegt mit faktor = 2,0 jetzt innerhalb der Schranke und erhält den passenden `nah`-Text.
- **M4 · behoben** — Zeile 1141. Der geforderte Satz zu a7 und a8 als Hausaufgabe mit je etwa
  20 Minuten steht wörtlich hinter der Minutenaufstellung.
- **M5 · behoben** — Zeilen 821 und 833: beide Simulationsfragen jetzt „Anforderungsbereich I".
  Die Zuordnung ist richtig: Beide verlangen die Wiedergabe einer unmittelbar abgelesenen
  Beobachtung.
- **M6 · behoben** — Zeilen 1846 bis 1856. `naechsterBuchstabe()` wird nicht mehr beim Bauen der
  Schrittfolge aufgerufen, sondern in das `tu` des letzten Schritts eingehängt, und nur wenn
  `rueckt` gesetzt ist. Der Kommentar benennt den Grund.
- **M7 · behoben** — Zeile 352: `void concat(List&lt;ContentType&gt; pList)`. Die
  Schnittstellentabelle ist jetzt durchgehend generisch.
- **M8 · nicht behoben** — `fachliches/modulliste.md:44` steht weiterhin auf „in Arbeit".
  Punkt 7 der Definition of Done ist damit formal offen. Liegt außerhalb der Moduldatei.

### S2 · behoben — die Zähler und Abschnitt 4 stimmen jetzt überein

Quelltext: `toFirst` zählt in Zeile 1709 `zRef++; if(S.kopf) zBes++;`, `next` in Zeile 1729
`zRef++; if(S.aktuell) zBes++;`. Eigene Messung (Playwright, Schrittmodus aus, Zähler vor jedem
Durchgang zurückgesetzt):

| Aktion | Referenzänderungen | besuchte Knoten | erwartet |
|---|---|---|---|
| Stapel, 5 mal `push` | 10 | 0 | 10 / 0 · ok |
| Schlange, 5 mal `enqueue` | 10 | 0 | 10 / 0 · ok |
| Liste, 5 mal `append` | 5 | 10 | 5 / 10 · ok |
| danach `toFirst()` | 7 (+2) | 11 (**+1**) | +1 · ok |
| danach 3 mal `next()` | 13 (+6) | 14 (**+3**) | +3 · ok |
| `toFirst()` + 3 mal `next()` zusammen | +8 | **+4** | k+1 = 4 für k = 3 · ok |
| 4. `next()` (auf den letzten Knoten E) | +2 | +1 | ok |
| 5. `next()` (über das Kettenende hinaus) | +2 | **+0** | ok |
| 6. `next()` (ohne aktuelles Objekt) | +0 | +0 | ok |

Die drei Abnahmekriterien sind unverändert, und Abschnitt 4.5 („einen für `toFirst()` und k
weitere für die `next()`-Aufrufe") ist am interaktiven Kern jetzt exakt nachvollziehbar. Keine
Konsolenmeldung bei keinem der Läufe.

**Der Wächter `if(S.aktuell)` bei `next` ist im Sinne der Definition aus a3 richtig.** a3 (Zeile
903) definiert den Knotenbesuch als „jede Auswertung, die den Hilfszeiger `lauf` **auf einen
Knoten** setzt". Läuft `next()` über das Kettenende hinaus, landet `aktuell` auf `null` und damit
gerade nicht auf einem Knoten — kein Besuch. Der Schritttext ist eigens konditional formuliert
(„Landet es auf einem Knoten, zählt das als Knotenbesuch"), deckt den Fall also mit ab. Auch
fachlich richtig: Ein Schritt ins Leere erreicht kein Element und darf in einer Kostenrechnung,
die den Weg zu Index k misst, nicht mitzählen — sonst wäre der Zugriff auf das letzte Element
teurer als k+1. Die zwei Referenzänderungen zählen dabei zu Recht weiter, denn beide Zuweisungen
werden ausgeführt.

**Die Unterscheidung zu `remove` ist begründbar — und das Argument steht sogar im Modul.** Gemessen:
Liste A, B, C; `toFirst()`, `next()` (aktuell = B), dann `remove()` → 2 Referenzänderungen,
**0 Knotenbesuche**, Kette A, C. `remove` besteht aus zwei Zuweisungen an bereits bekannte Zeiger:
`vorgaenger.setzeNachfolger(aktuell.gibNachfolger())` nutzt den beim `next()` mitgeführten
Vorgänger, und `aktuell = aktuell.gibNachfolger()` rückt den Cursor auf einen Knoten nach, den die
vorige Zeile ohnehin schon in der Hand hatte. Es wird keine Kette entlanggelaufen, um eine Stelle
zu finden — genau das trägt die Laufzeittabelle in Zeile 640 selbst vor: „`pop` / `dequeue` /
`remove`: es werden nur Referenzen umgebogen". Die Zählweise ist damit textlich gedeckt und
zugleich die einzige, die das O(1) dieser Zeile stützt. `dequeue` (Zeile 1696) und `pop`
(Zeile 1653) sind identisch behandelt, die Konvention ist also über alle drei Strukturen
einheitlich. Ich folge dem Urteil der Projektleitung.

### Weitere nachgeprüfte Korrekturen an der Simulation

- **M3 · behoben** — Zeilen 1761 bis 1768. `insert` in die leere Liste hat jetzt einen eigenen
  Zweig mit einem einzigen Schritt `anfang = new Knoten("A");`. Gemessen: 1 Referenzänderung,
  0 Knotenbesuche, Kette mit einem Knoten, `aktuell` bleibt `null`. Das stimmt mit dem gedruckten
  Java-Code (Zeilen 537 bis 547) und mit dem Versprechen „genau eine Java-Zeile pro Klick"
  überein; der Schritttext benennt zusätzlich, dass man danach `toFirst()` braucht. Der
  Regelzweig ist unberührt: `insert` vor `aktuell` zählt weiterhin 3 Referenzänderungen und
  0 Knotenbesuche, passend zu a2.
- **M6 · behoben, im Browser bestätigt** — Schrittmodus, Liste, `append`: Das Eingabefeld zeigt
  nach dem Klick auf `append(x)` noch „A", während Schritt 1 aussteht, und springt erst nach dem
  letzten Schritt (Knoten hängt, n = 1, 1 Referenzänderung) auf „B".

### Regressionsprüfung der gemeinsamen Aufgaben-Engine

Zeilen 1257 bis 1283. Beide Änderungen sind korrekt umgesetzt und im Browser bestätigt.
`altTol` übernimmt eine eigene `tol` aus `alt`, sonst skaliert es die Haupttoleranz mit
`d.tol * d.alt.wert / d.wert` — mathematisch derselbe Faktor wie beim Sollwert, mit Schutz gegen
`d.wert === 0`. Das `eps = 1e-9` wirkt multiplikativ auf die Toleranz und rettet den
Fließkomma-Grenzfall, ohne die Schranke praktisch aufzuweichen. In diesem Modul hat nur a4 ein
`alt`; die skalierende Variante kommt hier nicht zum Tragen (sie bleibt für andere Module
relevant).

| Aufgabe | Eingabe | Erwartung | Ergebnis |
|---|---|---|---|
| a4 | 4800 B | richtig | richtig |
| a4 | 4,8 kB | richtig | richtig |
| a4 | 4,75 / 4,85 kB (Toleranzrand) | richtig | richtig |
| a4 | 4,74 / 4,86 kB | abgelehnt | abgelehnt |
| a4 | 4,7 kB / 4,9 kB (früher fälschlich „richtig") | abgelehnt | abgelehnt · **M1 behoben** |
| a4 | 4800 kB bzw. 4,8 B | Einheitenhinweis | Einheitenhinweis |
| a4 | 9600 B | `nah` | `nah` · **M2 behoben** |
| a4 | 9,6 kB | `nah` | `nah` · Weiche auf die Antworteinheit wirkt |
| a4 | 2,4 kB / 1200 Knoten | `weit` | `weit` |
| a1 | 2 Elemente / 3 Elemente / 8 Elemente | ok / `nah` / `weit` | wie erwartet |
| a2 | 3 / 2 / 12 Referenzänderungen | ok / `nah` / `weit` | wie erwartet |
| a3 | 3603 / 3600 / 3 Knotenbesuche | ok / `nah` / `weit` | wie erwartet |
| a1–a3 | richtige Zahl, falsche Einheit | Einheitenhinweis | Einheitenhinweis |

Die Toleranzen von a1 bis a3 (`tol: 0.5`) sind unverändert und nicht zu streng geworden; die
richtige Antwort wird in jeder zugelassenen Einheit korrekt bewertet. Die Kommaeingabe „4,8" wird
vom Zahlenfeld angenommen und als 4.8 ausgewertet.

### Stimmen Abschnitt 4.5, Laufzeittabelle, a3 und Simulation zusammen?

Ja, nach der Änderung ohne Bruch:

| Aussage | Fundstelle | Simulation (gemessen) |
|---|---|---|
| Zugriff auf Index k kostet k+1 Besuche | 692 | `toFirst()` + 3 mal `next()` = 4 Besuche für k = 3 · ok |
| Mittelwert 600,5 bei 1200 Elementen | 694 | folgt aus (1+1200)/2, Modell durch die Messung gedeckt · ok |
| Zugriff auf das k-te Element: O(n) | 653 | jedes `next()` kostet genau 1 Besuch · ok |
| Entnehmen O(1), „nur Referenzen umgebogen" | 640 | `remove` 2 Referenzänderungen, 0 Besuche · ok |
| `append` an n Knoten kostet n Besuche | 670 | 5 `append` aus dem leeren Zustand = 0+1+2+3+4 = 10 · ok |
| a3: 1200+1201+1202 = 3603 | 903/923/1231 | Wachstumsgesetz der Simulation identisch · ok |
| `sim2`: Liste 10, Schlange 0, Stapel 0 | 833 | 10 / 0 / 0 · ok |
| Beobachtungsauftrag: Unterschied 10 | 761 | Schlange 0, Liste 10 · ok |

### Nichts Neues kaputtgegangen

Generischer Modulcheck der Projektleitung: **0 Blocker, 0 Mängel**, 79 Formeln, 6 MC-Blöcke,
7 Zahleneingaben, Selbstcheck 6. Eigene Läufe: keine Konsolen- oder `pageerror`-Meldung bei rund
60 Simulationsklicks und 32 Zahleneingaben. Die drei Abnahmekriterien, die Referenzzählung aller
übrigen Operationen, `insert` im Regelzweig (3 Referenzänderungen) und die Werte von a1 bis a4 sind
unverändert.

### Restliche Beanstandungen

- **Neu entstanden (klein) · Schritttext von `toFirst` bei leerer Liste — Zeile 1707.** Der Text
  lautet unverändert „Das aktuelle Objekt wird auf den ersten Knoten gesetzt. Dieser Zugriff ist
  zugleich der erste Knotenbesuch." Auf der leeren Liste ist beides falsch: Es gibt keinen ersten
  Knoten, der Wächter `if(S.kopf)` zählt richtigerweise keinen Besuch, und der Zähler bleibt
  gemessen auf 0 — der Text behauptet trotzdem einen. Der Fall ist mit zwei Klicks erreichbar
  (Zurücksetzen, Liste, `toFirst()`). Beim `next`-Schritt ist derselbe Fall vorbildlich gelöst
  („Landet es auf einem Knoten, zählt das als Knotenbesuch"); `sch()` akzeptiert für den Text auch
  eine Funktion, die Korrektur ist also einzeilig: `function(){ return S.kopf ? "… erste
  Knotenbesuch." : "Die Liste ist leer, aktuell wird auf null gesetzt — kein Knoten, also kein
  Knotenbesuch."; }`.
- **Teilweise behoben · `nah`-Text bei a4 passt nur zu einem der Fehler — Zeile 1246.** Er ist auf
  die Eingabe 9600 B zugeschnitten und trifft dort jetzt auch (M2). Durch die verschärfte Toleranz
  (M1) landen aber Antworten wie 4,7 kB, 4,74 kB oder 4,9 kB, die vorher fälschlich als richtig
  durchgingen, nun ebenfalls im `nah`-Band und bekommen die unpassende Auskunft „Vermutlich hast du
  den Gesamtbedarf der Kette statt des Mehrbedarfs angegeben — das wären 9600 B." Vorschlag: einen
  Satz voranstellen, der beide Fälle deckt, etwa „Knapp daneben. Gefragt ist die Differenz
  9600 B − 4800 B; rechne sie noch einmal genau nach. Hast du 9600 B angegeben, ist das der
  Gesamtbedarf der Kette, nicht der Mehrbedarf." Kein Rechenfehler, nur ein Formulierungspunkt.
- **Nicht behoben (außerhalb der Moduldatei) · M8** — `fachliches/modulliste.md:44` steht auf
  „in Arbeit"; für Punkt 7 der Definition of Done muss der Eintrag auf „fertig".
- **Beobachtung, kein neuer Befund · Zeile 621.** Die Einführung definiert den Knotenbesuch als
  „wie oft muss das Programm einem Nachfolgerzeiger folgen, bis es an der Stelle ist, an der es
  arbeiten will". Wörtlich genommen zählt das `toFirst()` nicht mit und ergäbe k statt k+1. Die
  operative Regel steht dreimal richtig und ausdrücklich im Text (670, 692, 903: „`lauf = anfang`
  eingeschlossen"), und die Zweckklausel „bis es an der Stelle ist" ist zugleich genau die
  Begründung dafür, dass `remove` keinen Besuch zählt. Die Stelle war schon vor der Nacharbeit so
  formuliert; wer sie einmal anfasst, könnte „jede Auswertung, die einen Zeiger auf einen Knoten
  setzt — das Setzen auf den Anfang eingeschlossen" schreiben und hätte alle vier Stellen unter
  einer Definition.

### Gesamturteil der Gegenprüfung

**Bestanden** — alle drei schweren Fehler sind sachlich richtig behoben, M1 bis M7 ebenfalls, die
Zählerkorrektur ist mit der Definition in a3, mit Abschnitt 4.5 und mit der Laufzeittabelle
konsistent und im Browser nachgemessen, und es sind keine Regressionen entstanden; offen bleiben
nur der Schritttext von `toFirst` auf der leeren Liste, eine Textschärfung beim `nah`-Feedback von
a4 und der Statuseintrag in der Modulliste.
