# Gegenprüfung nach Nacharbeit: module/mathe-q1-ableitungsregeln.html

Erstbefund: `pruefung/fach-mathe-q1-ableitungsregeln.md` (Urteil: Nacharbeit nötig, 12 Mängel)
Bauprotokoll: `inhalte/_bauprotokoll-ableitungsregeln.md` — laut FORTSCHRITT-Zeilen sind M1–M10
eingearbeitet, M11 bewusst offen, M12 (Modulliste) nicht gesetzt.
Gegenprüfung: 18.09.2026 · Alle Werte erneut mit sympy nachgerechnet. Modul nicht verändert.

Hinweis: M11 (zusätzliche Simulationsaufgabe) wird parallel von einem anderen Agenten gebaut und
ist am Ende dieses Berichts getrennt ausgewiesen.

---

## Stand der Prüfpunkte

### M6 · „Faktor 17" gekennzeichnet — **behoben**
Z. 209: „ein Vorzeichen und ein Faktor von rund 17 (10,00 gegen 0,60, genauer 16,7)".
Nachgerechnet: 10/0,6 = 16,6667 → „rund 17 … genauer 16,7" ist korrekt und als Rundung kenntlich.

### M7 · Momentanrate vs. Tageszuwachs — **behoben**
Z. 209: „steigt der Umsatz zu Beginn **mit** 10 € pro Tag – das ist die Momentanrate U′(0). Der
tatsächliche Zuwachs des ersten Tages liegt mit U(1) − U(0) = 9,40 € etwas darunter; warum, klärt
Abschnitt 4." Nachgerechnet: U(1) = 5,10 · 394 = 2009,40 €; U(0) = 2000,00 €; Differenz 9,40 € ✓.
Der Vorgriff auf Abschnitt 4 ist genau die im Erstbefund vorgeschlagene Lösung.

### M8 · Beweislücke Reziprokenregel benannt — **behoben**
Z. 366: „Vorausgesetzt ist dabei allerdings, dass w = 1/v an dieser Stelle differenzierbar ist; das
zeigt man separat über den Differenzenquotienten von 1/v, der sich auf einen Bruch mit dem Nenner
v(x+h)·v(x) bringen lässt. Der Weg über die Kettenregel liefert diese Existenzaussage mit, hat
dafür aber die Potenzregel für negative Exponenten als Voraussetzung." Fachlich korrekt und
abgewogen; der zuvor einseitige „Vorzug" ist jetzt beidseitig dargestellt.

### M9 · Voraussetzungen im Kettenregel-Merksatz — **behoben**
Z. 325: „Für u differenzierbar an der Stelle x und v differenzierbar an der Stelle u(x) gilt: …".
Damit tragen alle drei Merksätze ihre Voraussetzungen (Produktregel Z. 271, Quotientenregel Z. 380
mit v(x) ≠ 0).

### M3 · Beobachtungsauftrag Simulation 1 — **behoben**
Z. 453-454: (1) fordert jetzt Δt = 4,00; 2,00; 1,00 **und 0,50** Tage; (2) lautet „Sage vorher,
welchen Eckanteil du für Δt = 0,25 Tage erwartest (der kleinste einstellbare Wert), und stelle ihn
erst dann ein." Damit ist genau die im Erstbefund vorgeschlagene Umkehrung umgesetzt; der Regler
`rDt` (Z. 484, min=1, max=16, Δt = Wert·0,25) deckt 0,25 … 4,00 Tage ab, jeder geforderte Wert ist
einstellbar. Die Formulierung „der kleinste einstellbare Wert" macht die Grenze zusätzlich
transparent. Nebenbefund: t + Δt = 21 + 4 = 25 bleibt im Achsenbereich.

### M2 · Relativer Fehler in der richtigen Option — **behoben**
Z. 594 (sim3, Option 0): „…, der relative Fehler halbiert sich **nahezu** (3,23 % → 1,64 % →
0,83 % → **0,41 %**)." Beide Beanstandungen sind erledigt: 0,42 → 0,41 und das fehlende „nahezu".
Nachrechnung folgt unten in der Tabelle.

### M1 (Teil 1) · Anzeige t* = 25/3 ≈ 8,33 im Fragetext — **behoben**
Z. 518 (sim2): „drücke „Zum Umsatzmaximum" (t* = 25/3 ≈ 8,33 Tage)". Zuvor stand dort 8,3.
Ob die Zeitanzeige `anzT` beim gesetzten t* ebenfalls zwei Nachkommastellen zeigt, wird beim
Skript geprüft (siehe unten).

### M5 (Teil 1) · Sichtbare Aufgabennummern — **eingebaut**
Z. 612: `<span class="ab">Aufgabe 1 · Anforderungsbereich I</span>`. Die Nummer steht jetzt im
Chip über dem Kasten. Vollständigkeit und Übereinstimmung mit Text- und Exportverweisen folgt.

### M5 · Sichtbare Aufgabennummern, Export, Textverweise — **vollständig behoben**
Alle zehn Übungskästen tragen jetzt die Nummer im Chip (Z. 612, 637, 662, 674, 699, 724, 749, 774,
794, 818): „Aufgabe 1 · Anforderungsbereich I" … „Aufgabe 10 · Anforderungsbereich III".
Die Exportnamen (Z. 1495-1501) tragen dieselbe Zählung (a1→1, a2→2, mc1→3, a3→4, a4→5, z1→6,
a5→7). Die drei offenen Aufgaben werden im Export über `"Aufgabe " + (i + 8)` gezählt (Z. 1517);
in `#uebungen` liegen genau drei `<textarea>` (Z. 776, 796, 820) in genau dieser Reihenfolge, also
Aufgabe 8, 9, 10 — deckungsgleich mit dem Schülertext („in den Aufgaben 8, 9 und 10 bearbeitet",
Z. 871) und dem Lehrerteil (Z. 902, 944). Die drei MC-Aufgaben in Abschnitt 4 behalten bewusst
nur den AB-Chip (Z. 505, 517, 591) — richtig so, sie gehören nicht zur Übungszählung, und die
Exportnamen nennen sie „Simulation 1/2".

### M1 · Anzeige und Rechnung am Umsatzmaximum — **behoben (mit einem Rest, siehe N1)**
Skript Z. 1209/1211: `set("lT", tExakt !== null ? fmt(w.t, 2) : fmt(Math.round(w.t*10)/10, 1))`
— bei gesetztem t* werden jetzt zwei Nachkommastellen ausgegeben, sonst wie bisher eine.
Feedbacktext Z. 1000: „Preisbeitrag 0,10 · 350 = +35,00 €/Tag, Mengenbeitrag p(t*)·(−6) =
35/6 · (−6) = −35,00 €/Tag (mit p(t*) = 35/6 € ≈ 5,83 €)" — genau die vorgeschlagene Fassung.
Fragetext Z. 518: t* = 25/3 ≈ 8,33.

Nachgerechnet (sympy, exakt): U(t) = −3t²/5 + 10t + 2000; U′(t) = 10 − 6t/5; t* = 25/3 = 8,3333…;
p(t*) = 35/6 = 5,8333… €; n(t*) = 350; b·n(t*) = +35 exakt; p(t*)·d = −35 exakt; U(t*) = 2041,67 €.
Entscheidend für den Mangel war die Kontrollrechnung der Lernenden. Mit der **neuen** Anzeige
t = 8,33: n = 400 − 6·8,33 = 350,02 → 0,10·350,02 = 35,002 → angezeigt 35,00 ✓;
p = 5 + 0,10·8,33 = 5,833 → 5,833·(−6) = −34,998 → angezeigt −35,00 ✓. Die Nachrechnung geht
jetzt auf die zweite Nachkommastelle auf; der Widerspruch aus dem Erstbefund (35,02/−34,98) ist
weg.

### M10 · Widerspruch am Rand des Reglerbereichs — **behoben (Textvariante)**
Z. 1244 lautet jetzt: „Im einstellbaren Zeitraum bis 21 Tage gibt es kein Maximum — der Umsatz ist
durchgehend monoton." Das ist die im Erstbefund als zulässig genannte erste Korrekturvariante.
Die Hilfslinie wird weiterhin bis t* ≤ TMAX_D = 25 gezeichnet (Z. 1352/1371), aber die Aussage des
Knopfes widerspricht dem Bild nicht mehr, sondern präzisiert den Geltungsbereich.
Nachgerechnet: Für bd < 0 ist t* ein Maximum; für bd > 0 ein Minimum, und dort gilt
t* = 200/|d| + 2,5/|b| ≥ 200/12 + 2,5/0,15 = 33,3 Tage — außerhalb 0…21, der Knopf kann also nie
ein Minimum als „Maximum" anfahren (vollständiger Reglerscan unten).

### M2 · Nachrechnung des relativen Fehlers — **bestätigt**
`rel = fe/ex` exakt: Δt = 2,00 → π/(31π) = 3,2258 % ; 1,00 → 1,6393 % ; 0,50 → 0,8264 % ;
0,25 → 0,125/30,125 = **0,41494 %**. Auf zwei Stellen gerundet: 3,23 / 1,64 / 0,83 / **0,41** —
die Option (Z. 594) stimmt jetzt. Die Verhältnisse aufeinanderfolgender relativer Fehler sind
1,968 / 1,983 / 1,992, also tatsächlich „nahezu" halbiert — das eingefügte Wort ist sachlich
geboten und nicht bloß Kosmetik. Absolute Fehler π·Δr²: 3,14159 / 0,78540 / 0,19635 / 0,04909 m²,
exakt Faktor 4 — die Option („viertelt sich jedes Mal") ist ohne Einschränkung richtig.

### Vollständiger Reglerscan Simulation 1 (46 × 21 Kombinationen, b·d ≠ 0)
- 156 Kombinationen mit Maximum in 0 ≤ t* ≤ 21 → Knopf feuert, immer ein echtes Maximum.
- **0** Kombinationen mit einem Minimum in 0 ≤ t* ≤ 21 → der Knopf kann nie ein Minimum anfahren.
- 20 Kombinationen mit 21 < t* ≤ 25 → Hilfslinie sichtbar, Knopf lehnt ab. Mit der neuen
  Formulierung (Z. 1244) ist das kein Widerspruch mehr, sondern eine korrekte Einschränkung.
- Die Identität ΔU/Δt = p′n + pn′ + Δp·Δn/Δt wurde für drei weitere Zustände exakt geprüft
  (Rest 0 in exakter Rationalarithmetik), u. a. b = 0,22, d = −9, t = 12, Δt = 0,50:
  p = 7,64 €; n = 292,0; U = 2230,88 €; p′n = 64,24; pn′ = −68,76; U′ = −4,52; Sekante −5,51;
  Eck −0,99 — und −5,51 = −4,52 + (−0,99) ✓.

### Beobachtungsauftrag 1, erwartete Werte — **stimmen mit dem Lehrerteil überein**
Δt = 4,00 / 2,00 / 1,00 / 0,50 / 0,25 → Sekante 7,60 / 8,80 / 9,40 / 9,70 / 9,85;
Eckanteil −2,40 / −1,20 / −0,60 / −0,30 / −0,15; U′ = 10,00 konstant.
Das ist genau die Tabelle Z. 921-926. Teil (1) des Auftrags (bis 0,50) und Teil (2) (Vorhersage
für 0,25) sind damit beide abgedeckt; die Lehrertabelle musste nicht geändert werden und ist
weiterhin vollständig. Die Frage „Welche Zahl ändert sich dabei nicht?" ist mit U′ = 10,00
eindeutig beantwortbar.

### Simulation 2, Startzustand und t = 40 s — **unverändert richtig**
r = 15,000 m; A = 706,858 m²; 2πr = 94,2478 m; dA/dt = 47,1239 m²/s; Ring exakt 47,90929 m²;
genähert 47,12389 m²; Differenz 0,78540 m² (1,639 %) — alle Anzeigewerte Z. 555-562 bestätigt.
t = 40 s: r = 25 m, A = 1963,4954 → 1963,50 m² (Faktor 2,7778), dA/dt = 78,5398 (Faktor 1,6667 =
25/15) — Lehrerteil Z. 929 bestätigt.

### M4 · Feedbacktexte an den Schwellen der Engine — **behoben**
Die Engine (Z. 1084-1100) ist unverändert (Referenzmodul), die Texte sind jetzt auf sie
zugeschnitten. Z. 1038 (a1) beginnt der „weit"-Text mit „Liegt dein Wert bei etwa der Hälfte von
155 (75 oder 80)? Dann fehlt ein Summand: …" und schiebt die 6 erst danach nach; Z. 1058 (a5)
beginnt mit „Kommt bei dir t = 40 heraus? Dann ist beim Ausmultiplizieren ein Term verloren
gegangen (40 − t statt 40 − 2t) …".

Nachgebildete Verzweigung für alle im Modul benannten Fehlwerte (Faktor = |Antwort/Sollwert|):

| Aufgabe | Fehlwert | Faktor | Zweig | Text passt? |
|---|---|---|---|---|
| a1 | 75 (nur 1. Summand) | 0,484 | weit | ja — jetzt als erster Satz |
| a1 | 80 (nur 2. Summand) | 0,516 | nah | ja |
| a1 | 6 (u′·v′) | 0,039 | weit | ja |
| a2 | 201,06 (64π) | 2,000 | weit | ja |
| a2 | 25,13 (r = 2) | 0,250 | weit | ja |
| a2 | 76,97 (r = 3,5) | 0,766 | nah | ja |
| a3 | −2,4 (vertauscht) | 1,000 | nah | ja |
| a3 | 10 (u′/v′) | 4,167 | weit | ja |
| a3 | 12 (Nenner nicht quadriert) | 5,000 | weit | ja |
| a4 | 87,96 (28π) | 1,400 | nah | ja |
| a4 | 414,69 (132π) | 6,600 | weit | ja |
| a4 | −25,13 (−8π) | 0,400 | weit | ja |
| a5 | 40 (aus 40 − t) | 2,000 | weit | ja — jetzt als erster Satz |
| a5 | 30 (aus 60 − 2t) | 1,500 | nah | ja |
| a5 | 60 (Nullstelle von n) | 3,000 | weit | ja |
| a5 | 80 (Konstante) | 4,000 | weit | ja |

Jeder benannte Denkfehler landet jetzt in dem Zweig, dessen Text ihn bespricht. Der Befund M4 ist
damit erledigt.

---

## Neue bzw. offen gebliebene Befunde nach der Nacharbeit

### N1 · Lehrerteil widerspricht der korrigierten Anzeige — Z. 929 (Nacharbeit nötig, klein)
Der Satz lautet weiterhin: „Der Knopf „Zum Umsatzmaximum" setzt die Zeit exakt auf t* = 8,333 Tage
**(angezeigt als 8,3)**, damit sich die Beiträge auf +35,00 und −35,00 €/Tag aufheben."
Seit der M1-Korrektur (Z. 1209/1211) wird bei gesetztem t* mit **zwei** Nachkommastellen angezeigt,
also **8,33**. Der Klammerzusatz ist damit falsch; er beschreibt den Zustand vor der Nacharbeit.
Die Lehrkraft, die danach vor der Klasse steht, sucht eine Anzeige, die es nicht mehr gibt.
*Korrektur:* „(angezeigt als 8,33)" oder den Klammerzusatz ersatzlos streichen; der übrige Satz
bleibt richtig. Im selben Absatz steht t* bereits korrekt als 25/3 ≈ 8,33.

### N2 · M6 nur an einer von zwei Fundstellen korrigiert — Z. 844 (Nacharbeit nötig, klein)
Der Erstbefund M6 nannte zwei Fundstellen (Einstieg und Kernaussage 1). Korrigiert wurde nur der
Einstieg (Z. 209: „ein Faktor von rund 17 (10,00 gegen 0,60, genauer 16,7)"). Kernaussage 1 in
Abschnitt 6 sagt unverändert: „… unterscheiden sich beide Ergebnisse um ein Vorzeichen und **den
Faktor 17**: +10,00 €/Tag gegenüber −0,60." Nachgerechnet: 10,00/0,60 = 16,667 — der bestimmte
Artikel behauptet Exaktheit, die nicht vorliegt, und ausgerechnet in der Zusammenfassung, die
Lernende auswendig mitnehmen sollen. *Korrektur:* „um ein Vorzeichen und rund den Faktor 17".

### N3 · `tExakt` wird beim Verstellen von b, d und Δt nicht zurückgesetzt — Z. 1223-1225 (Mangel, klein)
Die Listener für `rDt`, `rB`, `rD` rufen nur `lesen(); zeichne();` auf, ohne `tExakt = null` zu
setzen (anders als der `rT`-Listener Z. 1227, das Ziehen Z. 1264/1268 und `bPlay` Z. 1233).
Folge: Wer den Knopf „Zum Umsatzmaximum" gedrückt hat und danach nur b oder d verstellt, bleibt
auf der **alten** Maximumszeit stehen, während die gestrichelte „Maximum"-Linie zur neuen Stelle
springt. Die Zeitanzeige zeigt dabei weiterhin zwei Nachkommastellen — nach der M1-Korrektur ist
genau das aber das Signal „wir stehen auf t*". Beispiel: Beobachtungsauftrag (3) drücken (d = −6,
t* = 8,33), dann d auf −8 stellen: neues t* = 0, angezeigt bleibt „8,33 Tage".
Kein falscher Zahlenwert — alle Anzeigen gehören konsistent zu t = 8,33 —, aber eine irreführende
Zustandsdarstellung. *Korrektur:* in Z. 1224 `tExakt = null;` ergänzen.

### N4 · `\text{Euro}` statt € in einer einzigen Formel — Z. 770 (Mangel, sehr klein)
Die Musterlösung zu Aufgabe 7 rendert „U(20) = 8,00 Euro · 200 = 1600 Euro", während `data-plain`
und der gesamte Rest der Datei das Zeichen € benutzen. Laut Bauprotokoll (Z. 26) war das ein
Notbehelf, weil € in KaTeX Probleme machte. An 1 von 462 Formelspannen bleibt so eine
Uneinheitlichkeit. *Korrektur:* `\text{\euro}` vermeiden und stattdessen die Einheit aus der
Formel herausziehen: `U(20) = 8{,}00\cdot 200 = 1600` mit dem Zusatz „in €" im Fließtext.

### N5 · Restfälle der Zweizweig-Rückmeldung (kein Nacharbeitspunkt)
Zwei plausible, im Modul selbst genannte Falschantworten landen im „nah"-Zweig, dessen Text zu
ihnen nicht passt: a1 mit **161** (= A(1) − A(0), steht in Hilfestufe 3; Faktor 1,039 → „nah",
Text spricht vom fehlenden Summanden) und a3 mit **4** (= c(1), steht im Einheitenfeedback;
Faktor 1,667 → „nah", Text spricht vom Vorzeichen). Das ist eine strukturelle Grenze der
Zweizweig-Engine aus dem Referenzmodul und kein Fehler dieses Moduls; alle im Modul als typisch
benannten Denkfehler sind korrekt zugeordnet (siehe Tabelle zu M4). Nur zur Kenntnis.

### M12 · Modulliste — **weiterhin offen**
`fachliches/modulliste.md` Z. 28 steht auf „in Arbeit". Das Bauprotokoll weist den Punkt bewusst
als offen aus. Nach N1–N4 und einem erneuten `modulcheck.py`-Lauf auf „fertig" setzen.

### Erneut geprüft und weiterhin ohne Befund
- **Lehrplanbezug.** Chip Z. 194 „Inhaltsfeld: Funktionen und Analysis" — wörtlich wie
  `fachliches/kernlehrplan-nrw.md` Z. 38. Die Q1-Einordnung ist durch Z. 42-44 gedeckt
  („Q1 umfasst die Fortführung der Analysis (Ableitungsregeln, …)"). Kein erfundenes Zitat; der
  Zentralabitur-Kasten Z. 870 verweigert die Zitation ausdrücklich. Von den fünf prozessbezogenen
  Kompetenzbereichen des Kernlehrplans nennt der Lehrerteil Z. 902 vier (Argumentieren,
  Problemlösen, Modellieren, Werkzeuge nutzen) und belegt sie mit Aufgaben — Kommunizieren fehlt,
  das ist kein Fehler, nur eine Auslassung.
- **Anforderungsniveau.** Eigene Zuordnung unverändert: 1 → AB I; 2 → AB I/II; 3-7 → AB II;
  8, 9, 10 → AB III. Die drei AB-III-Aufgaben sind echte Bewertungs- und Begründungsaufgaben mit
  je eigenen Bewertungskriterien (Z. 789, 813, 833) — der übliche Befund „AB III ist in Wahrheit
  eine lange Rechnung" trifft hier nicht zu.
- **Sprache und Form.** Durchgehend geduzt (die sechs Treffer für „Sie/Ihre" sind sämtlich
  Pronomen, im Kontext geprüft). Durchgehend Deutsch, auch in den Codekommentaren. Alle **462**
  Formelspannen tragen ein nichtleeres `data-plain`. Dezimalkomma über `fmt()` in jeder
  Skriptausgabe. Farbtokens `#0d7a52 / #e7f6ef / #b5e0cd` — korrekt für Mathematik.
- **Hilfestufen.** Fünf Zahleneingaben und drei offene Aufgaben haben je drei echte Stufen
  (Tipp begrifflich → Ansatz mit Formel ohne Werte → Lösungsweg bzw. Gliederung); die
  Musterlösungen der AB-III-Aufgaben liegen hinter einem eigenen Knopf (`data-stufe="9"`).
  Dass die MC- und die Zuordnungsaufgabe keine Hilfen haben, entspricht dem Referenzmodul
  (dort 2 Hilfesysteme auf 10 Aufgabenkästen) und ist keine Beanstandung.
- **Fachliche Nachrechnung Abschnitt 1-3, 5, 6** (sympy, exakt): f′ = 12x³ − 10x + 2 · (1/x³)′ =
  −3x⁻⁴ · 16x³ + 15x² − 16x − 10 mit f′(1) = 5, f′(2) = 146 · 6(2x−1)², f′(2) = 54 ·
  x/√(x²+1), f′(2) = 0,8944 · (x²−4x−1)/(x−2)², f′(3) = −4, f′(0) = −0,25 · x(5x+2)/√(2x+1),
  f(4) = 48, f′(4) = 88/3 ≈ 29,33, Tangente y = (88/3)x − 208/3 · 9x√(3x²+1), f′(2) = 18√13 ≈
  64,90 · A′(0) = 155, A(t) = 6t² + 155t + 1000, A(1) − A(0) = 161 · V′(4) = 32π ≈ 100,53,
  V(4) = 256π/3 ≈ 268,08 · c′ = (80 − 20t²)/(t²+4)², c′(1) = 2,4, Maximum t = 2 mit c(2) = 5 ·
  V′(5) = 20π ≈ 62,83, V(5) = 280π ≈ 879,65 · f′ = 8(2x−3)³ · Zuordnung D/C/B/A alle vier
  bestätigt · U′ = 40 − 2t, t* = 20, U(20) = 1600 € · (uv)′(1) = −8, Scheitel t = 5,
  U′(12) = −4,40 €/Tag. **Alle Werte stimmen.**
- **Toleranzen.** a1 155 ± 0,5 · a2 100,53 ± 0,15 · a3 2,4 ± 0,02 · a4 62,83 ± 0,1 ·
  a5 20 ± 0,2 Tage bzw. 480 ± 4,8 Stunden. Kein benannter Fehlwert liegt innerhalb einer Toleranz.

---

## Getrennte Meldung: M11 (parallel eingebaute Simulationsaufgaben)

Die Datei wurde um 22:51 Uhr ein zweites Mal gelesen. Das Bauprotokoll meldet
„M11 abgeschlossen (sim1/sim2 ersetzt, modulcheck leer, inhalte-md gespiegelt). sim3 unveraendert."
Das deckt sich mit dem Befund: `sim3` (Z. 590-600) ist unverändert und trägt die M2-Korrektur
weiterhin; die Beobachtungsaufträge (Z. 450-457, Z. 546-549) sind unverändert und tragen die
M3-Korrektur weiterhin. **Ersetzt wurden `sim1` und `sim2`** samt Rückmeldungen und Exporttiteln.

### Urteil zu M11: **abnahmefähig**

**sim1 neu (Z. 504-514).** „Stelle ein: b = 0,20 €/Tag, d = −8 Personen/Tag, t = 6,0 Tage und
Δt = 2,00 Tage. Welche Sekantensteigung ΔU/Δt zeigt die Anzeige?"
Alle vier Werte sind einstellbar: rB = 20 (Bereich −15…30), rD = −8 (−12…8), rT = 60 (0…210),
rDt = 8 (1…16). Exakt nachgerechnet:

| Größe | Rechnung | Wert |
|---|---|---|
| p(6) | 5 + 0,20·6 | 6,20 € |
| n(6) | 400 − 8·6 | 352 |
| U(6) | 6,20 · 352 | 2182,40 € |
| U(8) | 6,60 · 336 | 2217,60 € |
| **Sekante** | 35,20 / 2 | **17,60 €/Tag** = Option 1 ✓ (`r:1`) |
| U′(6) | 0,20·352 + 6,20·(−8) = 70,4 − 49,6 | 20,80 €/Tag = Distraktor 0 |
| Eckanteil | 0,20·(−8)·2 | −3,20 €/Tag |
| Probe | 20,80 + (−3,20) | 17,60 ✓ |
| Distraktor 2 | 20,80 − (−3,20), Vorzeichen des Eckanteils vertauscht | 24,00 |
| Distraktor 3 | nur p′·n = 0,20·352 | 70,40 |

Jeder Distraktor ist ein rekonstruierbarer Denkfehler und bekommt ein Feedback, das ihn benennt
(Z. 992, 994, 995) — die Rechnungen in den Feedbacktexten habe ich alle nachgerechnet, sie
stimmen (2182,40 · 2217,60 · 35,20 · 17,60 · −3,20 · −49,60).

**sim2 neu (Z. 516-526).** „Setze die Regler zurück und stelle dann nur die Besucheränderung auf
d = −7 (b = 0,10 bleibt). Drücke „Zum Umsatzmaximum". Welche Zeit und welchen Umsatz zeigt die
Anzeige?" Exakt nachgerechnet mit t* = −(b·400 + 5d)/(2bd):

| Option | Behauptung | Nachrechnung | Urteil |
|---|---|---|---|
| 0 | t = 8,33, U = 1993,06 € | t* für d = −6; bei d = −7 ist U(25/3) = 1993,0556 → 1993,06 | Distraktor korrekt beziffert |
| 1 | t = 7,14, U = 2000,00 € | U(t) = 2000 bei t = 50/7 = 7,1429; Faktor 2 im Nenner vergessen | Distraktor korrekt beziffert |
| **2** | **t = 3,57, U = 2008,93 €** | t* = 25/7 = 3,571428…; p = 75/14 = 5,3571; n = 375 exakt; U = 28125/14 = 2008,9286 → **2008,93** | **richtig** (`r:2`) ✓ |
| 3 | t = 0,00, U = 2000,00 € | gilt für d = −8: U′(0) = 40 − 40 = 0 | Distraktor korrekt beziffert |

Die Feedbacktexte (Z. 998-1001) sind ebenfalls nachgerechnet: „t* = 25/7 ≈ 3,57", „U′(t) =
0,10·(400 − 7t) + (5 + 0,10t)·(−7) = 5 − 1,4t" ✓, „p = 5,36 €, n = 375" ✓, „bei d = −7 ist
U′(0) = 0,10·400 + 5·(−7) = +5 €/Tag" ✓, „Das Maximum am Start gilt für d = −8" ✓.

**Beide Fragen erfüllen jetzt die Forderung aus `CLAUDE.md`**, sich nur mit der Simulation
beantworten zu lassen — jedenfalls praktisch: Man muss vier bzw. einen Regler verstellen und ein
Anzeigefeld ablesen; die Zahlen 17,60 und 2008,93 stehen nirgends im Text und sind ohne
Taschenrechner nicht nebenbei zu gewinnen. Der Beobachtungsauftrag deckt weiterhin die
begriffliche Seite ab, die neuen Fragen die Ablesekompetenz. Das ist eine echte Verbesserung
gegenüber dem Erstbefund M11.

**Zwei Dinge, die zu M11 noch anzumerken sind (beide klein):**

1. **sim2 hängt an der M1-Korrektur.** Die richtige Option nennt „t = 3,57 Tage". Angezeigt wird
   das nur, weil `anzT` bei gesetztem `tExakt` seit der M1-Korrektur zwei Nachkommastellen
   ausgibt (Z. 1211); vorher hätte dort „3,6 Tage" gestanden und keine Option gepasst. Die beiden
   Nacharbeiten greifen also ineinander — wer M1 später zurückdreht, zerschießt sim2. Gehört in
   den Lehrerteil oder ins Bauprotokoll, nicht in die Datei.
2. **N3 wird durch M11 wahrscheinlicher.** Der Ablauf von sim2 lautet „zurücksetzen → d ändern →
   Knopf drücken" und ist unkritisch. Wer die Reihenfolge jedoch umdreht (erst Knopf, dann d),
   bleibt wegen des nicht zurückgesetzten `tExakt` (Z. 1224) auf der alten Zeit stehen und liest
   8,33 statt 3,57 ab — also ausgerechnet Distraktor 0. Die eine Zeile `tExakt = null;` im
   b/d/Δt-Listener würde das ausschließen.

**Exporttitel** wurden mitgezogen (Z. 1492: „Simulation 1 – Sekantensteigung ablesen", Z. 1493:
„Simulation 1 – Umsatzmaximum bei d = −7") und passen zu den neuen Fragen. Der Lehrerteil nennt
in Z. 912 weiterhin „drei MC-Fragen" — bleibt richtig.

---

## Gesamturteil: **Nacharbeit nötig (klein) — danach abnahmefähig**

Von den zwölf Befunden des Erstberichts sind **M1 bis M10 sauber und nachprüfbar behoben**;
M11 ist durch den parallel arbeitenden Agenten sogar besser erledigt als vorgeschlagen, M12
(Modulliste) ist bewusst offen. Alle geänderten Zahlen wurden mit sympy in exakter Arithmetik
nachgerechnet und stimmen ausnahmslos; besonders zu würdigen ist, dass die M1-Korrektur nicht nur
die Anzeige, sondern auch die Kontrollrechnung der Lernenden trägt (35,002 und −34,998 runden auf
die angezeigten 35,00 und −35,00) und dass der vollständige Reglerscan über 966 Kombinationen
keinen Zustand findet, in dem der Maximum-Knopf ein Minimum anfährt. Offen bleiben vier kleine
Punkte, von denen nur zwei überhaupt sichtbar werden: der Lehrerteil behauptet in Z. 929 noch die
alte Anzeige „8,3" (N1), und die Zusammenfassung nennt in Z. 844 unverändert „den Faktor 17"
statt „rund den Faktor 17" (N2, zweite Fundstelle von M6, die bei der Nacharbeit übersehen
wurde); dazu kommen die fehlende `tExakt`-Rücksetzung (N3) und die eine Formel mit „Euro" statt
„€" (N4). Das sind vier Einzeiler; sobald sie eingearbeitet und `modulcheck.py` noch einmal
durchgelaufen ist, kann der Eintrag in `fachliches/modulliste.md` auf „fertig" und das Modul
ohne Vorbehalt in den Unterricht.
