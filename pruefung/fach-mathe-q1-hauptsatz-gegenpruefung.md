# Gegenprüfung `mathe-q1-hauptsatz.html` (nach Nacharbeit)

Erstbefund: `pruefung/fach-mathe-q1-hauptsatz.md` (Blocker S1, Mängel M1–M10).
Bauprotokoll meldet: Nacharbeit komplett, Modulcheck blocker [], maengel [].
Datum: 2026-09-18. Prüfung erfolgt lesend, Modul wird nicht geändert.

## 1 Blocker S1 und Mängel M1–M10: Status

| Nr. | Befund Erstprüfung | Stand jetzt | Fundstelle | Bewertung |
| --- | --- | --- | --- | --- |
| S1 | „Zehntelliter … 320 Streifen" (Faktor 1000) | „Für eine Genauigkeit von einem Zehntel Kubikmeter waren es dort dreihundertzwanzig Streifen" | Z. 206; konsistent mit Z. 403 und Z. 811 | **behoben** |
| M1 | Kernaussage 1 „Umkehrung des Ableitens" zu stark | „Ableiten macht das Integrieren rückgängig." | Z. 301 | **behoben**, deckungsgleich mit Z. 339 |
| M2 | a6-Beweis trug nicht; Probe außerhalb des Intervalls | Maximum-Argument `M < 0`, `I_a(x) ≤ M·(x−a) < 0`; Fall `x < a` ausdrücklich über die Fortsetzung `f ≡ −1` auf ℝ, `I₀(−3) = 3` | Z. 727 | **behoben** (Rest­nitpick unten) |
| M3 | sim1/sim2 ohne Simulation beantwortbar | beide Fragen neu: sim1 = Nullstellen von `I₂` bei Rate B, sim2 = Rate C mit Grenzwert | Z. 546–566 | **behoben**, mit Einschränkung (Punkt 4) |
| M4 | Beobachtungsauftrag lief am Tiefpunkt vorbei | „setze a = 0,0 und x = 0,00" ergänzt | Z. 502 | **behoben** |
| M5 | Rate-C-Achsen 4,5/−0,5/±14,5 falsch beschriftet | `fMin:-1, fMax:5, iMin:-15, iMax:15` | Z. 1064 | **behoben**, Bereiche umschließen weiter alle Werte (nachgerechnet) |
| M6 | Tangente nutzte `f(x)` statt gemessener Steigung | `var m = (Isum(f,a,x+0.02)-Isum(f,a,x-0.02))/0.04;` | Z. 1239 | **behoben** |
| M7 | Alternativeinheit m³ bei a4 unerreichbar | `alt:{wert:0.01036, einheit:"m³", tol:0.0005}` | Z. 931 | **behoben** (0,01 m³ liegt 3,6·10⁻⁴ daneben und wird jetzt angenommen) |
| M8 | Gültigkeitsbedingungen fehlten | `n ≠ −1; x ≠ 0 für n < 0; x > 0 für nicht ganzzahliges n`; `k ≠ 0` bei `e^{kx}` und bei der linearen Substitution | Z. 416, 419, 429 | **behoben** |
| M9 | sim1/sim2 als AB II ausgewiesen, sim2 war AB I | beide Fragen sind inhaltlich neu, AB II jetzt vertretbar | Z. 547, 558 | **behoben**, sim2 bleibt am unteren Rand von AB II |
| M10 | Export „Offene Aufgabe 1/2"; Iₐ vs. I_a | `"Aufgabe " + (i + 6) + " (offen)"` → Aufgabe 6/7; `data-plain` durchgehend „Iₐ" | Z. 1398; Z. 259 u. a. | **behoben** (Ausnahme `I_b`, siehe Mängel) |

Zum Nachweis M2: Der Beweisgang ist jetzt lückenlos. `f` ist auf dem kompakten `[a; x]` stetig, nimmt
also nach dem Satz vom Minimum und Maximum ein Maximum `M` an; aus `f < 0` folgt `M < 0`; aus
`f(t) ≤ M` für alle `t ∈ [a; x]` folgt über die Monotonie des Integrals `I_a(x) ≤ M·(x − a) < 0`
für `x > a`. Der früher fehlende Fall `x < a` ist ergänzt und die Probe `I₀(−3) = 3` liegt nun im
ausdrücklich auf ℝ fortgesetzten Gegenbeispiel.

Zum Nachweis M8: Die Bedingungsspalte ist fachlich korrekt. `x ≠ 0 für n < 0` deckt die ganzzahlig
negativen Exponenten, `x > 0 für nicht ganzzahliges n` die reellen. `n ≠ −1` steht separat.

## 2 Nachgerechnet (Python, unabhängig vom Modul)

Nachgebaut wurden `Isum` (Simpson, n = 200), `kurveBauen` und `fmt` aus dem Modul, zusätzlich alle
Musterlösungen geschlossen.

| Fundstelle | Größe | mein Wert | Datei | Urteil |
| --- | --- | --- | --- | --- |
| Z. 548–551 | sim1, Rate B, a = 2: Nullstellen von `I₂` | `I₂(x) = 0,4x² − 3,2x + 4,8`, Nullstellen x = 2 und x = 6 | „x = 2,00 und x = 6,00" | ✓ |
| Z. 893–895 | `I₂(4,00)` | −1,60 m³ (Anzeige „−1,60") | −1,60 m³ | ✓ |
| Z. 894 | `I₂(0)` | +4,80 m³ | +4,80 m³ | ✓ |
| Z. 563, 900 | sim2, Rate C, `I₀(12)` | 12,96902 → Anzeige „12,97" | 12,97 m³ | ✓ |
| Z. 563, 900 | `f(12)` und gemessene Steigung bei x = 12 | 0,109295 → beide „0,11" | 0,11 m³/h | ✓ |
| Z. 899 | Steigung bei x = 6,00 (Rate C) | 0,661196 → „0,66" | 0,66 m³/h | ✓ |
| Z. 900, 688 | Grenzwert `40/3` | 13,3333 | 40/3 ≈ 13,33 | ✓ |
| Z. 512–517 | Startanzeige A, a = 0, x = 6 | f 4,20 · I 25,20 · m 4,20 · D 0,000 | identisch | ✓ |
| Z. 498 | A, a = 9, x = 3 | −21,60 m³ | −21,60 m³ | ✓ |
| Z. 502 | Auftrag B, a = 0: Tiefpunkt | x = 4,00, `I₀ = −6,40`, f = 0,00 | (Ablesung) | ✓ erreichbar |
| Z. 503 | Auftrag A, a = 0: Hochpunkt | x = 9,00, `I₀ = 32,40`, f = 0,00 | (Ablesung) | ✓ erreichbar |
| Z. 274–276 | Wertetabelle f und `I₀` | 1,80/4,80/4,20/0,00/−7,80 und 0,00/10,80/25,20/32,40/21,60 | identisch | ✓ |
| Z. 289–293 | Differenzenquotienten bei x = 3 | 4,93333 · 4,88333 · 4,81933 · 4,80199 · 4,80020 | identisch | ✓ |
| Z. 345–347 | `f(10,5)`, `I₀(10,5)` | −3,45 m³/h; 29,925 m³ | identisch | ✓ |
| Z. 467 | `I₃`-Tabelle | −10,80/0,00/14,40/21,60/10,80, Differenz konstant 10,80 | identisch | ✓ |
| Z. 449 | `I₀(4)`, Steigung | 15,7333 → 15,73; 5,00 | identisch | ✓ |
| Z. 595 | a1 | F(3) = 24, F(1) = 4, Integral 20 FE | identisch | ✓ |
| Z. 620–623 | a2 | 434/15 = 28,9333; 94/15 = 6,2667; 68/3 = 22,6667 | identisch | ✓ |
| Z. 623 | a2 Plausibilität | mittlere Rate 4,5333; f(7) = 3,20; f(4) = 5,00 | 4,53 / 3,20 / 5,00 | ✓ |
| Z. 929 | a2 Distraktor Trapez | (4,20 + 3,20)/2 · 5 = 18,50 | 18,50 | ✓ |
| Z. 930 | a2 Distraktor f(7) − f(2) | −1,00 | −1,0 | ✓ |
| Z. 686–688 | a4 | e^(−1,5) = 0,2231302; F(5) = −2,975069; Integral 10,358265 → 10,36 L | identisch | ✓ |
| Z. 934–935 | a4 Distraktoren | 13,33 (Grenzwert); 20,00 = f(0)·5; 4,46 = f(5)·5; −3,107 ohne 1/k | 13,33 / 20,00 / 4,46 / −3,11 | ✓ |
| Z. 713–716 | a5 | t = 9 (und −1); f(8) = 1,80; f(10) = −2,20; V(9) = 40,90; V(0) = 8,50; V(12) = 30,10 | identisch | ✓ |
| Z. 939 | a5 Distraktor V(4) | 24,2333 → 24,23 | 24,23 | ✓ |
| Z. 727 | a6 Gegenbeispiel | F(0)=100, F(2)=98, F(5)=95, F(10)=90; `I₀(x) = −x`; `I₀(−3) = 3` | identisch | ✓ |
| Z. 746 | a7 `a = ln 0,5` | −0,693147; e^(−0,6931) = 0,50000 | −0,6931 / 0,5000 | ✓ |
| Z. 434 | Produktregel-Gegenbeispiel | 1/3 ≈ 0,3333 gegen 1/4 = 0,25 | identisch | ✓ |
| Z. 632–646 | a3, Diagramme A–D | A pos. fallend; B Nullstelle bei t ≈ 4,01, VZW −→+; C konstant negativ; D Hochpunkt bei t = 3,00, f(0)=f(6)=0 | Zuordnung A/D/B/C | ✓ eindeutig in beiden Richtungen |
| Z. 1058–1064 | Achsenbereiche | A: f ∈ [−7,80; 5,00] ⊂ [−9; 6], I ∈ [−32,40; 32,40] ⊂ [−36; 36] · B: f ∈ [−3,20; 6,40] ⊂ [−4; 7], I ∈ [−25,60; 25,60] ⊂ [−28; 28] · C: f ∈ [0,11; 4,00] ⊂ [−1; 5], I ∈ [−12,97; 12,97] ⊂ [−15; 15] | Achsen wie angegeben | ✓ kein Wert außerhalb |
| Z. 966–981 | Toleranzen | a1 ±0,05 von 20 · a2 ±0,05 von 22,67, alt 22 670 L ±50 L · a4 ±0,05 von 10,36, alt 0,01036 m³ ±0,0005 · a5 ±0,05 von 40,90, alt 40 900 L ±50 L | – | ✓ kein Distraktorwert fällt in ein Toleranzfenster |

**Kein einziger Rechenfehler.** Alle 24 Distraktor- und Musterlösungszahlen sind exakt reproduzierbar.
Die „nah"/„weit"-Schwelle (Faktor 0,5 … 2) ordnet jeden im Feedback genannten Fehlwert dem Text zu,
in dem er auch besprochen wird — auch den Grenzfall 10 FE bei a1 (Faktor exakt 0,5 ⇒ „weit", und
dort steht er).

## 3 Neue Widersprüche zwischen Text, Rückmeldung, Lehrerteil und Simulation

Die Nacharbeit hat sim1 und sim2 inhaltlich **ausgetauscht**. Der Lehrerteil wurde dabei nicht
mitgezogen; zwei Querverweise dort zeigen jetzt ins Leere. Das sind die einzigen neuen Befunde.

- **N1 · Z. 830 (Lehrerteil, Fehlerliste).** „«f negativ, also I negativ.» … **Simulationsfrage 2
  sichert es ab**, Aufgabe 6 prüft es." Simulationsfrage 2 arbeitet jetzt mit **Rate C**, und die
  ist auf ganz [0; 12] positiv (kleinster Wert 0,11 m³/h). Zum Vorzeichenfehler sagt sie nichts;
  sie prüft die davon verschiedene Verwechslung „f fällt ⇒ I fällt".
  → Korrektur: „Der Fehlerkasten in Abschnitt 2 und Aufgabe 6 prüfen es; Simulationsfrage 2 sichert
  die verwandte Verwechslung «sinkende Rate ⇒ sinkender Bestand» ab."
- **N2 · Z. 835 (Lehrerteil, Fehlerliste).** „Extremstelle der Rate wird mit Extremstelle des
  Bestands verwechselt (t = 4 gegen t = 9). In **Simulationsfrage 1** und Aufgabe 5 direkt geprüft."
  Das Paar t = 4 / t = 9 gehört zu **Rate A**. Simulationsfrage 1 läuft jetzt über Rate B mit a = 2
  und prüft, ob die Nullstelle der Rate mit der Nullstelle der Integralfunktion verwechselt wird —
  ein anderer Denkfehler. Das Paar t = 4 / t = 9 steckt im **Beobachtungsauftrag** (Z. 503) und in
  Aufgabe 5.
  → Korrektur: „Im Beobachtungsauftrag und in Aufgabe 5 direkt geprüft; Simulationsfrage 1 prüft
  zusätzlich die Verwechslung «Nullstelle der Rate = Nullstelle des Integrals»."

Geprüft und **ohne Befund** blieben:

- Beobachtungsauftrag (Z. 500–506) gegen Simulation: Rate B, a = 0, x = 0 — Tiefpunkt bei x = 4,00
  mit `I₀ = −6,40` und `f = 0,00`; „Abspielen" setzt x von 12,00 wieder auf 0, also wird der
  Tiefpunkt beim Wechsel zu Rate A tatsächlich durchlaufen (Z. 1312). Rate A: Hochpunkt bei
  x = 9,00 mit `f = 0,00`. Die Probe an Rate C ist beantwortbar: keine Nullstelle von f ⇒ kein
  Extrempunkt ⇒ I steigt durchgehend — genau das zeigt die Simulation.
- Vererbungstabelle Z. 445–451 gegen Simulation: alle sieben Belegzellen stimmen mit den
  angezeigten Werten überein, auch „Rate B … x = 4" (der Ort des Tiefpunkts hängt nicht von a ab).
- Z. 494/496 gegen den Quelltext: Füllfarben nach Vorzeichen, durchgezogen bis x, dahinter
  gestrichelt, `f(x)` aus der Funktionsgleichung, Steigung aus der Streifensumme — alles wie
  beschrieben umgesetzt.
- Z. 472 („untere Kurve wandert als Ganzes") gegen `gA = Isum(f, T_MIN, a)`: korrekt, der Graph
  wird um die Konstante `I₀(a)` verschoben.
- Lehrerteil Z. 846: Rate C ist tatsächlich `4·e^(−0,3t)`, der Bezug zur Kondensatorentladung mit
  `1/RC = 0,3` trägt.
- Startwerte der Anzeige im Markup (Z. 512–517) stimmen mit dem ersten `aktualisieren()` überein.
- Kein `@@NEU@@`, kein `TODO`, kein `localStorage`, keine `mousedown`-Handler, KaTeX als einzige
  externe Quelle, 558 von 558 `.m`-Elementen mit `data-plain`, kein Dezimalpunkt in einer
  angezeigten Zahl, durchgehend geduzt (die Treffer auf „Sie" in Z. 370, 387, 725 sind
  Personalpronomen am Satzanfang, kein Siezen).
- Die Zahleneingabe-Engine (Z. 943–985) ist **zeichengleich** mit der des Referenzmoduls.

## 4 Sind die Simulationsfragen nur mit der Simulation lösbar?

**sim1 (Z. 546–555) — ja, praktisch.** Um zwischen den drei Optionen zu entscheiden, braucht man
`I₂(4,00) = −1,60` und `I₂(6,00) = 0,00`. Wer das ohne Simulation will, muss
`I₂(x) = 0,4x² − 3,2x + 4,8` aufstellen und dessen Nullstellen bestimmen — das ist mehr Arbeit als
das Ablesen und setzt genau den Hauptsatz voraus, um den es geht. Alle drei Optionen tragen eine
Begründung und eine Zahl, die Länge ist ausgeglichen, jeder Distraktor benennt seinen Denkfehler
(Option 0: „Iₐ(a) = 0 ist die einzige Nullstelle"; Option 2: „Nullstelle der Rate = Nullstelle des
Integrals"). Als AB II korrekt eingestuft. **Gut gelöst.**

**sim2 (Z. 557–566) — nur eingeschränkt.** Zwei Schwächen:

- **Beide Distraktoren sind ohne Simulation widerlegbar**, allein aus Abschnitt 2/3: „die Kurve
  fällt" scheitert an `f > 0 ⇒ I steigt` (Kernaussage 2), „ab x = 6 waagerecht" scheitert daran,
  dass die e-Funktion keine Nullstelle hat (steht wörtlich in der Rückmeldung Z. 899). Die
  Simulation liefert nur die Bestätigung, nicht die Entscheidung.
- **Die richtige Option ist die einzige mit Zahlen und mit Abstand die längste** (133 gegen 80 und
  78 Zeichen). Wer rät, rät richtig. Das ist ein Formfehler, kein fachlicher.

→ Vorschlag ohne Eingriff in die Zahlen: die Werte aus Option 2 in die Frage verschieben („Lies bei
x = 12,00 Integral und Steigung ab.") und die Optionen auf die *Deutung* umstellen — etwa
„12,97 m³ ist der Endwert, mehr läuft nie aus" gegen „12,97 m³ ist noch nicht der Endwert; der liegt
bei 40/3 ≈ 13,33 m³ und wird nie erreicht" gegen „die Kurve wird ab x ≈ 12 waagerecht". Dann
entscheidet die Ablesung, und die drei Optionen sind gleich lang.

Der **Beobachtungsauftrag** (Z. 500–506) ist dagegen vorbildlich: er ist nur am Gerät zu erledigen,
verlangt zwei Messungen, eine selbst formulierte Regel und eine Vorhersage mit Prüfung an einem
dritten Fall.

## 5 Lehrplanbezug und Anforderungsniveau

- Chip Z. 193 „Inhaltsfeld: Funktionen und Analysis" — **wörtlich** wie in
  `fachliches/kernlehrplan-nrw.md` Z. 38. Kein erfundenes Zitat, kein Wortlaut, der dort nicht steht.
- Q1-Verortung korrekt: der Kernlehrplanauszug nennt für Q1 ausdrücklich „Integralrechnung bis zum
  Hauptsatz und zu Flächen zwischen Graphen" — das Modul deckt genau dieses Stück ab und verweist
  am Ende (Z. 799) auf die Fläche zwischen zwei Graphen als Anschluss.
- Die im Lehrerteil (Z. 811) genannten prozessbezogenen Bereiche *Argumentieren*, *Werkzeuge
  nutzen*, *Modellieren* existieren in der Liste der fünf Kompetenzbereiche wirklich. Die
  didaktische Setzung „Integralfunktion vor Stammfunktion" ist Z. 812 als **offen markiert** — genau
  das verlangt die Projektregel.
- Anforderungsbereiche: eigene Einstufung gegen die Auszeichnung in der Datei

  | Aufgabe | Datei | meine Einstufung | Bemerkung |
  | --- | --- | --- | --- |
  | sim1 | II | II | Ablesen **und** Deuten der Kompensation zweier Flächen |
  | sim2 | II | I–II | siehe Punkt 4; nach der dort vorgeschlagenen Umstellung klar II |
  | a1 | I | I | Standardintegral, Reproduktion |
  | a2 | II | II | Sachkontext, Grenzen ≠ 0 |
  | a3 | II | II | Zuordnung mit Argumentationskette, in beiden Richtungen eindeutig |
  | a4 | II | II | lineare Substitution im Sachkontext |
  | a5 | II | II | Modellieren, Extremwert **mit** Randvergleich |
  | a6 | III | III | echte Stellungnahme: Gegenbeispiel, Begründung, Sonderfall, Bewertungskriterien |
  | a7 | III | III | „genau dann, wenn" in beiden Richtungen zu beweisen, Bewertungskriterien vorhanden |

  Keine als AB III ausgewiesene Aufgabe ist in Wahrheit eine lange Rechnung — a6 und a7 verlangen
  Begründung und Bewertung und tragen jeweils eine eigene Kriterienliste. Das entspricht dem
  LK-Niveau. Einziger Vorbehalt bleibt sim2.
- Die Hilfestufen sind sauber abgestuft: Stufe 1 gibt eine Denkrichtung ohne Formel (a5: „Was macht
  die Zuflussrate genau in diesem Moment? Und: Wie viel war zu Beginn schon da?"), Stufe 2 die
  Stammfunktion samt Aufforderung zur Ableitungsprobe, Stufe 3 die Rechnung. Kein Tipp verrät die
  Lösung. Dass a6/a7 statt drei Stufen nur die Musterlösung tragen, entspricht dem Referenzmodul
  (dort ebenso bei a4/a5) und ist kein Abweichen.

## 6 Verbleibende Mängel

Schwere Fehler: **keine.** Kein fachlich falscher Satz, keine falsche Zahl, kein erfundener
Lehrplanbezug.

| Nr. | Fundstelle | Befund | Korrekturvorschlag |
| --- | --- | --- | --- |
| **N1** | Z. 830 | Lehrerteil verweist für den Vorzeichenfehler auf Simulationsfrage 2; die arbeitet nach der Nacharbeit mit der durchgehend positiven Rate C und prüft ihn nicht mehr | Satz wie in Punkt 3 umformulieren |
| **N2** | Z. 835 | Lehrerteil verweist für „t = 4 gegen t = 9" auf Simulationsfrage 1; die läuft jetzt über Rate B. Das Paar steckt im Beobachtungsauftrag | Verweis auf Beobachtungsauftrag umstellen |
| **N3** | Z. 557–566 | sim2: beide Distraktoren rein theoretisch widerlegbar, richtige Option als einzige mit Zahlen und 70 % länger | Zahlen in die Frage ziehen, Optionen auf die Deutung des Grenzwerts umstellen (Punkt 4) |
| **N4** | Z. 496 | „die beiden mittleren Zahlen der Anzeige" — verglichen werden das dritte und das **fünfte** Feld („Rate f(x)" und „Steigung von Iₐ bei x"); im responsiven Raster ist „mittlere" ohnehin nicht stabil | Felder beim Namen nennen |
| **N5** | Z. 929 | „weil der Graph zwischen t = 2 und t = 7 nach oben gewölbt ist" — das Modul führt in Z. 450/451 die Begriffe *links-/rechtsgekrümmt* ein und benutzt sie hier nicht | „weil der Graph dort rechtsgekrümmt ist" |
| **N6** | Z. 727 | a6: „Jeder Streifen der Breite Δt liegt dann **unter** M·Δt" — richtig ist „höchstens M·Δt"; die Formel selbst trägt korrekt „≤" | Wort tauschen |
| **N7** | Z. 636 | a3, Diagramm B: die gezeichnete Nullstelle liegt bei t = 4,013 statt 4,000 (Endpunkte 72,9 und 42,4 px passen nicht exakt zum Verhältnis 2 : 1) | Haarrisse, 0,3 px — nur bei einem Neusatz des SVG mitkorrigieren: `18.0,72.9 150.0,42.3` |
| **N8** | Z. 496 | „Die Seite summiert Streifen wie in der letzten Einheit" — tatsächlich Simpson-Regel (gewichtete Streifensumme), nicht Ober-/Untersumme | „summiert schmale Streifen" genügt |

Bewusst **nicht** beanstandet:

- `alt:{wert:0.01036, tol:0.0005}` bei a4 ist mit ±4,8 % weiter als die Haupttoleranz (±0,48 %),
  aber zwingend: auf zwei Nachkommastellen gerundet sind 10,36 L eben 0,01 m³. Kein Distraktorwert
  fällt in dieses Fenster, ein Rechenfehler geht dadurch nicht durch.
- `data-plain="I_b(x) …"` in Z. 459 statt „I_b" mit Tiefstellung: Unicode kennt kein tiefgestelltes
  b. Unvermeidbar, „Iₐ" und „I₃" sind korrekt gesetzt.
- Die Rückmeldung „Der Zahlenwert stimmt", wenn jemand 22 670 **m³** eingibt, ist streng genommen
  schief. Der Code dafür ist zeichengleich mit dem Referenzmodul und damit nicht Sache dieses Moduls.
- Die x-Achse der Simulation beschriftet nur bis t = 10 (Z. 1131), damit die Beschriftung nicht mit
  „t in h" kollidiert; x = 12,00 steht in der Anzeige als Zahl. Ohne Folgen.

## 7 Gut gelöst — bitte übernehmen

- **Der a6-Beweis in seiner neuen Fassung.** Maximum-Argument statt „alle Summanden negativ",
  Gegenbeispiel ausdrücklich auf ℝ fortgesetzt, bevor `I₀(−3) = 3` als Probe dient. So gehört ein
  AB-III-Erwartungshorizont geschrieben.
- **Die Gültigkeitsbedingungen in der Grundintegraltabelle** (Z. 416): drei Bedingungen für `xⁿ`,
  sauber getrennt nach `n = −1`, `n < 0` und nicht ganzzahligem `n`. Das sieht man in Schulmaterial
  selten vollständig.
- **sim1** in der neuen Fassung: gleich lange Optionen, jede mit Zahl und Begründung, und die
  Entscheidung fällt erst nach dem Ablesen.
- **Der Beobachtungsauftrag**: zwei Messungen, eine selbst zu formulierende Regel, eine Vorhersage
  mit Prüfung an einem dritten Fall — und seit der Nacharbeit mit `x = 0,00` auch wirklich
  durchführbar.
- **Die Simulation misst, statt zu illustrieren.** `lM` entsteht aus einem Differenzenquotienten der
  Streifensumme, nicht aus `f(x)`; seit der Korrektur von M6 gilt das auch für die gezeichnete
  Tangente. Das Feld „Unterschied" macht die Behauptung des Hauptsatzes prüfbar.
- **Das Distraktor-Feedback durchgehend**: 15 Wege, jeder mit Zahl widerlegt, jeder mit dem Namen
  des Denkfehlers. Auch die „nah"/„weit"-Texte der Zahleneingaben nennen jeweils drei bis vier
  konkrete Fehlwerte samt Ursache.
- **Der Lehrerteil** im Übrigen: Zeittabelle mit Sozialform, ehrliche Aussage darüber, was in
  90 Minuten *nicht* zu schaffen ist, Differenzierung in beide Richtungen, als offen markierte
  didaktische Setzung, Kondensator-Bezug für die Fachschaft Physik.

## Urteil

**Abnahmefähig**, mit zwei Pflichtkorrekturen von je einem Satz (N1, N2 im Lehrerteil).

Blocker S1 und alle zehn Mängel M1–M10 sind tatsächlich behoben, nicht nur laut Protokoll: der
a6-Beweis trägt jetzt über das Maximum `M < 0` lückenlos, die Gültigkeitsbedingungen bei `xⁿ`,
`e^{kx}` und der linearen Substitution stehen vollständig da, die Rate-C-Achsen sind ganzzahlig und
umschließen weiterhin alle Werte, die Tangente nutzt die gemessene Steigung, und die
Alternativeinheit bei a4 ist erreichbar. Sämtliche 24 nachgerechneten Zahlen — darunter die neuen
Werte `I₂(2) = I₂(6) = 0,00`, `I₂(4) = −1,60`, `I₂(0) = 4,80`, `I₀(12) = 12,97` bei `f(12) = 0,11`
und der Grenzwert `40/3` — stimmen exakt mit der Datei überein; ein Rechenfehler ist nirgends
geblieben. Der Lehrplanbezug ist wörtlich und echt, das Anforderungsniveau entspricht dem
Leistungskurs, und beide AB-III-Aufgaben sind echte Begründungsaufgaben mit Bewertungskriterien.
Was offen bleibt, ist kein Fachfehler, sondern Aufräumarbeit: Der Lehrerteil verweist noch auf die
alten Simulationsfragen, und sim2 ist in seiner Form zu leicht zu erraten. Mit den beiden
Satzkorrekturen kann das Modul in den Unterricht; die Umstellung von sim2 gehört in den nächsten
Durchgang.
