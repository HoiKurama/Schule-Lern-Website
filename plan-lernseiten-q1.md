# Plan: Interaktive Lernseiten Q1 (NRW)

Stand: 31.08.2026 · Projekt "Schule" · Fächer: Mathematik, Physik, Informatik, Mathematik-Erweiterungskurs

---

## 1. Grundidee

Jedes Thema bekommt eine eigenständige HTML-Datei, die ohne Installation im Browser läuft – auf dem Schulrechner, am iPad, zu Hause. Alle Dateien folgen demselben Aufbau und demselben Design, damit die Schülerinnen und Schüler sich nicht bei jedem neuen Blatt neu orientieren müssen. Die Module hängen nicht voneinander ab: Jede Datei funktioniert allein, eine `index.html` verlinkt sie als Übersicht.

Einsatzszenario, von dem der Plan ausgeht: Einzel- oder Partnerarbeit im Unterricht, dazu Selbstlernen zu Hause. Kein Login, keine Serverkomponente, keine gespeicherten Schülerdaten.

---

## 2. Einheitliches Seitengerüst

Jede Seite durchläuft dieselben sechs Abschnitte:

**1 · Kopf**
Fach, Thema, Kursniveau (GK/LK), Bezug zum Inhaltsfeld des Kernlehrplans, geschätzte Bearbeitungszeit.

**2 · Einstieg**
Eine konkrete Frage oder Beobachtung, die das Thema motiviert. Dazu ein kurzer Vorwissen-Check (3–4 Fragen), der zurückmeldet, was vorher noch mal angeschaut werden sollte.

**3 · Erklärteil**
Schrittweiser Aufbau, keine Textwüste. Herleitungen stehen in aufklappbaren Blöcken, damit die Seite nicht erschlägt. Merksätze und Formeln optisch abgesetzt.

**4 · Interaktiver Kern**
Das Herzstück, fachabhängig: Simulation mit Schiebereglern, Visualisierung zum Mitziehen, Schritt-für-Schritt-Animation eines Algorithmus, Rechner mit Zwischenschritten. Immer mit Beobachtungsauftrag – nicht nur "hier kannst du rumschieben", sondern eine Frage, die man nur durch Ausprobieren beantwortet.

**5 · Übungsteil**
Gestufte Aufgaben nach Anforderungsbereichen I–III, mit direktem Feedback. Dreistufiges Hilfesystem: Tipp → Ansatz → vollständiger Lösungsweg. Falsche Antworten bekommen einen inhaltlichen Hinweis, kein bloßes rotes Kreuz.

**6 · Abschluss**
Zusammenfassung, Abiturbezug (welcher Aufgabentyp taucht dazu im Zentralabitur auf), Selbsteinschätzung. Optional ein aufklappbarer Lehrerteil mit didaktischen Hinweisen und Lösungen, der beim Ausdruck wegfällt.

---

## 3. Wiederverwendbare Aufgabenbausteine

Sieben Komponenten, die in allen Fächern gleich funktionieren und in jede Datei kopiert werden:

| Baustein | Einsatz |
|---|---|
| Multiple Choice mit Distraktor-Feedback | jede falsche Option bekommt einen eigenen Hinweis auf den typischen Denkfehler |
| Zahleneingabe mit Toleranz und Einheit | Physik, Rechenaufgaben – prüft auch die Einheit |
| Termeingabe | Mathe – Vergleich über Auswertung an Stützstellen statt Zeichenkettenvergleich, damit `2x+1` und `1+2x` beide gelten |
| Zuordnung / Drag & Drop | Graph ↔ Ableitungsgraph, UML ↔ Java-Code, Formel ↔ Situation |
| Schieberegler-Experiment | Parameter verändern, Wirkung beobachten, Vermutung eintragen |
| Schrittweise Codeausführung | Informatik – Variablenzustände sichtbar machen |
| Freitext mit Musterlösung | offene Aufgaben, Musterlösung plus Bewertungskriterien zum Aufklappen |

---

## 4. Technische Festlegungen

- **Eine Datei pro Thema**, CSS und JavaScript inline. Keine Build-Tools, keine Ordnerstruktur, die kaputtgehen kann.
- **Grafik über SVG und Canvas**, keine Bibliotheken. Läuft auch offline.
- **Formeln**: KaTeX per CDN, mit lesbarem Unicode-Fallback, falls das Schul-WLAN blockt. Alternativ komplett ohne CDN – zu klären.
- **Touch-tauglich**: Schieberegler und Drag & Drop funktionieren auch am Tablet.
- **Druckansicht** über `@media print`: Die Seite lässt sich als Arbeitsblatt ausdrucken, interaktive Elemente werden zu statischen Abbildungen.
- **Kein Datenspeicher**: Fortschritt lebt nur in der aktuellen Sitzung. Wer sein Ergebnis abgeben soll, kopiert es über einen Button als Text heraus.
- **Dateibenennung** nach Projektvorgabe: `fach-q1-thema.html`, also z. B. `physik-q1-induktion.html`.
- **Farbcode pro Fach**: Physik blau, Mathematik grün, Informatik orange, Erweiterungskurs violett. Gleiches Layout, unterscheidbare Akzente.

---

## 5. Modulplan Physik Q1

Inhaltsfelder Q1: GK "Klassische Wellen und geladene Teilchen in Feldern" sowie "Elektrodynamik und Energieübertragung", LK "Ladungen, Felder und Induktion" sowie "Schwingende Systeme und Wellen".

| Datei | Thema | Interaktiver Kern |
|---|---|---|
| `physik-q1-elektrisches-feld.html` | Feldbegriff, Feldlinien, Plattenkondensator | Probeladung im Feld ziehen, Feldlinienbild live |
| `physik-q1-geladene-teilchen-e-feld.html` | Beschleunigung und Ablenkung, Millikan | Ablenkröhre mit regelbarer Spannung, Bahnkurve |
| `physik-q1-magnetisches-feld.html` | Lorentzkraft, Leiterschaukel, Kreisbahn | Massenspektrometer bzw. Wien-Filter zum Einstellen |
| `physik-q1-induktion.html` | Induktionsgesetz, Lenzsche Regel | Leiterschleife durchs Feld ziehen, U-t-Diagramm entsteht mit |
| `physik-q1-generator-transformator.html` | Energieübertragung, Wechselstrom (GK-Schwerpunkt) | Generator drehen, Übersetzungsverhältnis testen |
| `physik-q1-schwingungen.html` | Feder- und Fadenpendel, Dämpfung, Resonanz | Pendel mit einstellbarer Masse, Federkonstante, Dämpfung |
| `physik-q1-schwingkreis.html` | Elektromagnetischer Schwingkreis (LK) | Analogie mechanisch ↔ elektrisch nebeneinander |
| `physik-q1-wellen.html` | Ausbreitung, Überlagerung, Interferenz | zwei Erreger, Interferenzmuster live |
| `physik-q1-doppelspalt-gitter.html` | Beugung, Wellenlängenbestimmung | Spaltabstand und Wellenlänge regeln, Maxima ausmessen |

---

## 6. Modulplan Mathematik Q1

Inhaltsfelder: Funktionen und Analysis, Analytische Geometrie und Lineare Algebra. Stochastik erst in Q2, deshalb hier noch nicht.

| Datei | Thema | Interaktiver Kern |
|---|---|---|
| `mathe-q1-ableitungsregeln.html` | Produkt-, Ketten-, Quotientenregel | Regeltrainer mit Zufallsaufgaben, Schrittkontrolle |
| `mathe-q1-funktionsuntersuchung.html` | Kurvendiskussion ganzrationaler Funktionen | Parameter schieben, Extrem- und Wendestellen wandern mit |
| `mathe-q1-exponentialfunktionen.html` | Wachstum, Zerfall, e-Funktion, Modellierung | Datensatz anpassen, Modell und Realdaten vergleichen |
| `mathe-q1-integral-rekonstruktion.html` | Vom Bestand zur Änderungsrate und zurück | Ober- und Untersumme, Streifenzahl regelbar |
| `mathe-q1-hauptsatz.html` | Stammfunktion, Hauptsatz, Flächenberechnung | Integralfunktion baut sich beim Ziehen der oberen Grenze auf |
| `mathe-q1-flaechen-zwischen-graphen.html` | Flächen zwischen Kurven, uneigentliche Fälle | zwei Graphen verschieben, Fläche wird schraffiert und berechnet |
| `mathe-q1-vektoren-grundlagen.html` | Vektorbegriff, Rechnen, Linearkombination | 3D-Ansicht zum Drehen, Vektoren addieren |
| `mathe-q1-geraden-ebenen.html` | Parameter-, Normalen-, Koordinatenform | Ebene über Stützvektor und Richtungsvektoren aufspannen |
| `mathe-q1-lagebeziehungen.html` | Gerade/Gerade, Gerade/Ebene, Ebene/Ebene | Fälle durchspielen, Schnittmenge wird angezeigt |
| `mathe-q1-abstaende-winkel.html` | Skalarprodukt, Lotfußpunkt, Hesse (LK-Vertiefung) | Punkt bewegen, Abstand und Lotfußpunkt aktualisieren sich |

---

## 7. Modulplan Informatik Q1

Fünf Inhaltsfelder verteilen sich über die gesamte Q-Phase. Typische Q1-Verteilung: objektorientierte Modellierung und Datenstrukturen zuerst, dann Sortier- und Suchverfahren, Datenbanken je nach schulinternem Lehrplan in Q1 oder Q2. Automaten, formale Sprachen und Kryptologie liegen meist in Q2.

Programmiersprache: Java, passend zu BlueJ.

| Datei | Thema | Interaktiver Kern |
|---|---|---|
| `info-q1-objekte-klassen.html` | Objekte, Klassen, Attribute, Methoden, Vererbung | UML-Diagramm und Java-Code nebeneinander, Zuordnungsübung |
| `info-q1-lineare-strukturen.html` | Liste, Schlange, Stapel | Operationen schrittweise animiert, Referenzen sichtbar |
| `info-q1-baeume.html` | Binärbaum, binärer Suchbaum, Traversierungen | Knoten einfügen und löschen, Traversierung Schritt für Schritt |
| `info-q1-sortieralgorithmen.html` | Sortierverfahren im Vergleich | nebeneinander laufende Animation, Vergleichs- und Tauschzähler |
| `info-q1-suchalgorithmen.html` | lineare und binäre Suche, Komplexität | Suchvorgang im Array, Aufwand mitzählen |
| `info-q1-er-modell.html` | Datenmodellierung, ER-Diagramm, Normalisierung | Modell bauen, Normalformverstöße aufdecken |
| `info-q1-sql.html` | SQL-Abfragen auf einer Beispieldatenbank | echte SQL-Konsole im Browser, Ergebnistabelle live |

---

## 8. Mathematik-Erweiterungskurs

Hier fehlt mir die Grundlage: In den NRW-Vorgaben gibt es keinen Kernlehrplan unter diesem Namen, das ist offenbar ein schulinternes Angebot. Drei denkbare Zuschnitte:

- **Vertiefung des Q1-Stoffs** – dieselben Themen, höhere Anforderungsstufe, mehr Modellierung und Begründung
- **Abiturvorbereitung** – Aufgabenformate des Zentralabiturs, hilfsmittelfreier Teil, Trainingsparcours
- **Eigenständige Themen** – Beweisverfahren, Zahlentheorie, Matrizen, Näherungsverfahren, also Stoff jenseits des Pflichtcurriculums

Sobald klar ist, was gemeint ist, ergänze ich den Modulplan. Bis dahin bleibt dieser Block offen.

---

## 9. Umsetzungsreihenfolge

**Phase 1 – Vorlage festzurren**
Ein einziges Pilotmodul, an dem Layout, Aufgabenbausteine, Hilfesystem und Druckansicht durchgespielt werden. Danach Feedback einholen und nachschärfen. Erst wenn diese Vorlage sitzt, geht es in die Breite – sonst müssen später zwanzig Dateien nachgezogen werden.

**Phase 2 – Übersichtsseite**
`index.html` als Hub mit Kacheln nach Fach und Thema, dazu Filter für GK/LK.

**Phase 3 – Fachweiser Ausbau**
Pro Fach in der Reihenfolge des Schuljahres, damit die Module dann fertig sind, wenn das Thema dran ist. Analysis und E-Feld also vor Wellen und Vektorgeometrie.

**Phase 4 – Erweiterungskurs**
Sobald der Zuschnitt geklärt ist.

---

## 10. Offene Entscheidungen

1. Welches Pilotmodul zuerst?
2. GK, LK oder beides in einer Datei mit ausklappbaren LK-Zusatzblöcken?
3. Was umfasst der Mathematik-Erweiterungskurs?
4. Schülerseiten duzen oder siezen?
5. Formeln mit KaTeX über CDN, oder muss alles komplett offline laufen?
