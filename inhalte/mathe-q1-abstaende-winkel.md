# Abstände und Winkel — Inhalt

Modul `module/mathe-q1-abstaende-winkel.html`, Mathematik LK Q1, Inhaltsfeld „Analytische Geometrie und
Lineare Algebra“, etwa 120 Minuten. Baut auf `mathe-q1-geraden-ebenen` (Skalarprodukt in Komponenten,
Orthogonalität, Normalen- und Koordinatenform) und `mathe-q1-lagebeziehungen` (Schnittpunkt Gerade/Ebene,
windschiefe Geraden) auf und wiederholt sie nicht.

Schreibweisen wie in den Vorgängermodulen: Skalarprodukt `a∘b`, Koordinatenform `n∘x = d`, Gerade
`x = p + r·u`. Der Punkt, dessen Abstand gesucht ist, heißt immer Q mit Ortsvektor q. Abstände heißen
`d(Q,E)`, `d(Q,g)`, `d(g,h)`. Alle Zahlen stammen aus `output/mathe-q1-abstaende-winkel/zahlen.py`,
Ausgabe in `kontrolle.txt` daneben.

---

## 1 Einstieg (`einstieg`)

**Aufhänger.**
Die Drohne aus den letzten beiden Modulen startet wieder bei S(0|0|10), eine Längeneinheit ist 1 m. Das
Garagendach liegt in der Ebene E: −2x₂ + 5x₃ = 15. Senkrecht unter der Drohne liegt der Dachpunkt
(0|0|3), die Drohne ist also 7 m höher als dieser Punkt. Trotzdem ist sie dem Dach näher als 7 m: Das
Dach ist geneigt, und zur schrägen Fläche hin gibt es einen kürzeren Weg.

Wie weit ist die Drohne wirklich vom Dach entfernt, und in welche Richtung zeigt die kürzeste
Verbindung? Und wenn die Drohne landet: Unter welchem Winkel trifft ihre Flugbahn auf die Dachfläche?
Beides hängt am Skalarprodukt, das du bisher nur als Test auf „senkrecht“ benutzt hast.

(Ergebnis zur Information für den Bau, nicht im Einstieg verraten: Abstand 35/√29 m ≈ 6,50 m.)

**Vorwissensfragen**

`vw1` — Welcher Satz gilt in jedem Dreieck und enthält den Satz des Pythagoras als Sonderfall?
- A: Kosinussatz **(richtig)** — „Richtig. Der Kosinussatz c² = a² + b² − 2ab·cos γ wird für γ = 90° zum Satz des Pythagoras, weil cos 90° = 0 ist. Mit ihm leitest du gleich das Skalarprodukt her.“
- B: Sinussatz — „Der Sinussatz verknüpft Seiten mit den gegenüberliegenden Winkeln (a : sin α = b : sin β). Er enthält kein Quadrat einer Seite und wird deshalb bei 90° nicht zum Pythagoras.“
- C: Satz des Thales — „Der Satz des Thales sagt nur, wann ein Winkel ein rechter ist (Ecke auf dem Halbkreis). Über Seitenlängen sagt er nichts aus.“

`vw2` — Wie lang ist der Vektor (2|−1|2)?
- A: √3 — „Du hast die Koordinaten addiert, statt sie zu quadrieren: 2 − 1 + 2 = 3. Die Länge kommt aus dem Pythagoras im Raum, also aus der Summe der Quadrate.“
- B: 3 **(richtig)** — „Richtig. √(2² + (−1)² + 2²) = √9 = 3. Vektoren mit glatter Länge wie dieser kommen in den Beispielen oft vor.“
- C: 9 — „9 ist die Summe der Quadrate. Die Wurzel fehlt noch: Die Länge ist √9.“

`vw3` — Eine Gerade in der Ebene hat die Steigung m = 1. Welchen Winkel schließt sie mit der x-Achse ein?
- A: 1° — „Steigung und Winkel sind nicht dasselbe. Die Steigung ist der Tangens des Winkels: tan α = m.“
- B: 57,3° — „57,3° ist 1 im Bogenmaß. Du hast m als Winkel im Bogenmaß gelesen. Die Steigung ist aber der Tangens des Winkels, nicht der Winkel selbst.“
- C: 45° **(richtig)** — „Richtig. Aus tan α = 1 folgt α = 45°: Pro Schritt nach rechts geht es einen Schritt nach oben.“

---

## 2 Skalarprodukt und Winkel (`winkel`)

**Vom Rechenausdruck zur Geometrie.**
Aus dem Modul „Geraden und Ebenen“ kennst du das Skalarprodukt als Rechenvorschrift
a∘b = a₁b₁ + a₂b₂ + a₃b₃ und weißt: a∘b = 0 genau dann, wenn a und b senkrecht aufeinander stehen.
Das ist ein Sonderfall einer allgemeineren Beziehung. Das Skalarprodukt misst, wie weit zwei Vektoren
in dieselbe Richtung zeigen:

> a∘b = |a|·|b|·cos φ  (id `f-skalargeo`)

Dabei ist φ der Winkel zwischen den beiden Pfeilen, wenn man sie am selben Punkt ansetzt, mit
0° ≤ φ ≤ 180°.

**Herleitung (Details-Block „Warum gilt a∘b = |a|·|b|·cos φ?“).**
Setze a und b am selben Punkt an. Der Verbindungsvektor der beiden Spitzen ist a − b. Die drei Pfeile
bilden ein Dreieck mit den Seitenlängen |a|, |b| und |a − b|, der Winkel zwischen a und b ist φ.
1. Kosinussatz in diesem Dreieck: |a − b|² = |a|² + |b|² − 2·|a|·|b|·cos φ.
2. In Koordinaten (aus dem Modul „Geraden und Ebenen“):
   |a − b|² = (a₁ − b₁)² + (a₂ − b₂)² + (a₃ − b₃)² = |a|² + |b|² − 2·a∘b.
3. Beide Zeilen beschreiben dieselbe Länge. Gleichsetzen und |a|² + |b|² auf beiden Seiten streichen:
   −2·a∘b = −2·|a|·|b|·cos φ, also a∘b = |a|·|b|·cos φ.
Für φ = 90° ist cos φ = 0, und du erhältst das bekannte Orthogonalitätskriterium zurück.

**Winkel berechnen.** Aufgelöst nach dem Kosinus:

> cos φ = a∘b / (|a|·|b|)  (id `f-winkelvek`)

Beispiel 1: a = (1|1|0), b = (1|0|1). a∘b = 1, |a| = |b| = √2, cos φ = 1/2, also φ = 60°.
Beispiel 2: a = (1|2|2), b = (−2|1|−2). a∘b = −2 + 2 − 4 = −4, |a| = |b| = 3, cos φ = −4/9 ≈ −0,4444,
also φ ≈ 116,39°.

**Was das Vorzeichen verrät.** Die Längen im Nenner sind positiv. Das Vorzeichen von cos φ ist also das
Vorzeichen von a∘b: Ist a∘b > 0, ist der Winkel spitz; ist a∘b < 0, ist er stumpf; ist a∘b = 0,
stehen die Vektoren senkrecht.

**Merksatz.** Das Skalarprodukt ist groß und positiv, wenn zwei Vektoren fast in dieselbe Richtung
zeigen, null bei senkrechten und negativ bei Vektoren, die „gegeneinander“ zeigen. Den Winkel liefert
es erst, wenn du durch beide Längen teilst.

**Schnittwinkel zweier Geraden.**
Schneiden sich zwei Geraden, entstehen vier Winkel, je zwei gleich große. Als Schnittwinkel gilt der
kleinere, also ein Winkel zwischen 0° und 90°. Der Winkel zwischen den Richtungsvektoren kann aber
stumpf sein, denn statt u kann man genauso gut −u als Richtungsvektor nehmen. Der Betrag im Zähler
sorgt dafür, dass immer der spitze Winkel herauskommt:

> cos α = |u∘v| / (|u|·|v|)  (id `f-schnittgg`)

Mit den Richtungen aus Beispiel 2 ergibt sich cos α = 4/9 und α ≈ 63,61° = 180° − 116,39°.

**Gerade und Ebene.**
Der Winkel zwischen einer Geraden g und einer Ebene E ist der Winkel zwischen g und ihrem senkrechten
Schatten in E (Abbildung: Gerade, Normalenvektor, Schatten, Winkel α und 90° − α). Den Schatten muss man
nicht ausrechnen. Es genügt der Normalenvektor: n steht senkrecht auf E, also schließen u und n den
Winkel 90° − α ein (oder 90° + α, wenn n zur anderen Seite zeigt; der Betrag fängt das ab). Wegen
cos(90° − α) = sin α gilt

> sin α = |n∘u| / (|n|·|u|)  (id `f-schnittge`)

Beispiel 3: E: 2x₁ + x₂ + 2x₃ = 6 und eine Gerade mit u = (1|2|2). n∘u = 2 + 2 + 4 = 8, |n| = |u| = 3,
sin α = 8/9 ≈ 0,8889, also α ≈ 62,73°.

**Typische Fehlvorstellung (abgesetzt).** Wer hier aus Gewohnheit den Kosinus nimmt, rechnet mit
denselben Zahlen und bekommt ein glaubwürdiges Ergebnis, im Beispiel 27,27°. Das ist aber der Winkel
zwischen g und dem Normalenvektor, also 90° − α. Kontrolle: Steht g senkrecht auf E, ist u ein Vielfaches
von n. Dann muss α = 90° herauskommen, und genau das liefert der Sinus.

**Zwei Ebenen.**
Zwei sich schneidende Ebenen sind genauso gegeneinander geneigt wie ihre Normalenvektoren. Der
Schnittwinkel ist wieder der spitze:

> cos α = |n₁∘n₂| / (|n₁|·|n₂|)  (id `f-schnittee`)

Beispiel 4: E₁: 2x₁ + x₂ + 2x₃ = 6 und E₂: x₁ − x₂ = 0. n₁∘n₂ = 2 − 1 + 0 = 1, |n₁| = 3, |n₂| = √2,
cos α = 1/(3√2) ≈ 0,2357, also α ≈ 76,37°.

**Übersichtstabelle** (Spalten: Objekte · Vektoren · Funktion · Bereich)
| Winkel zwischen | du brauchst | Formel mit | Winkelbereich |
|---|---|---|---|
| zwei Vektoren | a, b | cos, ohne Betrag | 0° bis 180° |
| zwei Geraden | u, v | cos, mit Betrag | 0° bis 90° |
| Gerade und Ebene | u, n | sin, mit Betrag | 0° bis 90° |
| zwei Ebenen | n₁, n₂ | cos, mit Betrag | 0° bis 90° |

---

## 3 Abstände (`abstaende`)

**Was Abstand heißt.**
Der Abstand eines Punktes Q von einer Ebene E ist die kürzeste Entfernung von Q zu irgendeinem Punkt
von E. Diese kürzeste Verbindung steht senkrecht auf E. Der Punkt F, in dem sie E trifft, heißt
Lotfußpunkt, die Strecke QF heißt Lot.

Begründung über Pythagoras: Ist R irgendein anderer Punkt von E, dann ist das Dreieck QFR bei F
rechtwinklig. Also ist |QR|² = |QF|² + |FR|² > |QF|². Jeder andere Weg ist länger.

**Typische Fehlvorstellung (abgesetzt).** Der Abstand ist weder der Höhenunterschied in x₃-Richtung
noch die Entfernung zum Stützpunkt der Ebene. Bei der Drohne: Der Dachpunkt senkrecht darunter liegt
7 m tiefer, der Abstand zum Dach beträgt aber nur 35/√29 m ≈ 6,50 m. Der Höhenunterschied stimmt nur bei
waagerechten Ebenen (x₃ = c), weil dort das Lot senkrecht nach unten zeigt.

**Verfahren 1: Lotfußpunkt.** Abbildung: Ebene, Punkt Q, Lot mit Fußpunkt F, Normalenvektor, gestrichelt
der senkrechte Weg nach unten.
1. Lotgerade durch Q mit dem Normalenvektor als Richtung aufstellen:

   > x = q + t·n  (id `f-lotgerade`)

2. Lotgerade mit E schneiden (einsetzen, nach t auflösen), das liefert F.
3. d(Q,E) = |QF|.

Beispiel 5: Q(3|3|3), E: 2x₁ + x₂ + 2x₃ = 6. Lotgerade x = (3|3|3) + t·(2|1|2). Einsetzen:
2(3 + 2t) + (3 + t) + 2(3 + 2t) = 6, also 15 + 9t = 6 und t = −1. Damit F(1|2|1) und
|QF| = |(−2|−1|−2)| = 3. Der Abstand beträgt 3 LE.

**Verfahren 2: Hessesche Normalform.** Das Lotfußpunktverfahren lässt sich ein für alle Mal
durchrechnen. Ergebnis:

> d(Q,E) = |n∘q − d| / |n|  (id `f-hnf`)

Im Beispiel: n∘q = 6 + 3 + 6 = 15, also d(Q,E) = |15 − 6| / 3 = 3. Das d in d(Q,E) ist der Name des
Abstands, das d im Zähler ist die rechte Seite der Koordinatenform n∘x = d.

**Herleitung (Details-Block „Woher kommt die Formel?“).**
Setze die Lotgerade x = q + t·n in n∘x = d ein: n∘q + t·n∘n = d. Wegen n∘n = |n|² folgt
t = (d − n∘q) / |n|². Der Lotfußpunkt ist F = q + t·n, die Lotstrecke ist der Vektor t·n mit der Länge
|t|·|n| = |d − n∘q| / |n|² · |n| = |n∘q − d| / |n|.
Den Namen hat die Formel von Otto Hesse. Teilt man die Koordinatengleichung durch |n|, steht links ein
Normalenvektor der Länge 1. Diese Form der Ebenengleichung heißt Hessesche Normalform. Setzt man einen
Punkt ein, liefert sie direkt seinen Abstand, mit Vorzeichen.

**Das Vorzeichen ohne Betrag.** Lässt du die Betragsstriche weg, sagt das Vorzeichen von n∘q − d, auf
welcher Seite von E der Punkt liegt: positiv auf der Seite, in die n zeigt, negativ auf der anderen.
Zwei Punkte liegen genau dann auf derselben Seite, wenn die Werte gleiches Vorzeichen haben.

**Merksatz.** Abstand heißt kürzeste Verbindung, und die kürzeste Verbindung ist immer das Lot. Die
Hessesche Normalform ist kein neuer Gedanke, sondern das Lotfußpunktverfahren, einmal allgemein
ausgerechnet.

**Abstand eines Punktes von einer Geraden.**
Auch hier ist die kürzeste Verbindung das Lot. Der Lotfußpunkt F = p + r·u liegt auf g, und QF steht
senkrecht auf der Richtung u. Diese eine Bedingung legt r fest:

> (p + r·u − q)∘u = 0  (id `f-lotfussg`)

Beispiel 6: g: x = (1|0|2) + r·(2|1|−2), Q(4|3|2). F − q = (2r − 3 | r − 3 | −2r).
(F − q)∘u = 2(2r − 3) + (r − 3) − 2(−2r) = 9r − 9 = 0, also r = 1 und F(3|1|0).
d(Q,g) = |(−1|−2|−2)| = 3 LE.
Eine Hesse-Formel gibt es dafür im Raum nicht: Eine Gerade im Raum hat keinen einzelnen Normalenvektor.
Alternative: Hilfsebene durch Q mit u als Normalenvektor aufstellen und mit g schneiden. Das liefert
denselben Fußpunkt F.

**Parallele Objekte.** Ist eine Gerade parallel zu einer Ebene oder sind zwei Ebenen parallel, haben
alle Punkte denselben Abstand. Du nimmst einen beliebigen Punkt (etwa den Stützpunkt) und rechnest
Punkt–Ebene. Zwei parallele Geraden behandelst du als Punkt–Gerade.

**Windschiefe Geraden (Unterabschnitt, LK).**
Zwei windschiefe Geraden g: x = p + r·u und h: x = q + s·v haben eine kürzeste Verbindung, die auf
beiden senkrecht steht. Ohne sie direkt zu suchen, gehst du so vor:
1. Einen Vektor n bestimmen, der auf u und auf v senkrecht steht: n∘u = 0 und n∘v = 0, eine
   Koordinate frei wählen.
2. Die Ebene H durch den Stützpunkt P von g mit Normalenvektor n enthält g und ist parallel zu h. Jeder
   Punkt von h hat denselben Abstand zu H, also auch ihr Stützpunkt Q.
3. Abstand von Q zu H mit der Hesseschen Normalform:

   > d(g,h) = |n∘(q − p)| / |n|  (id `f-windschief`)

Warum der kürzeste Abstand? g liegt in H, h in der dazu parallelen Ebene durch Q. Jede Verbindungsstrecke
von g nach h verbindet zwei parallele Ebenen und ist mindestens so lang wie deren Abstand. Das gemeinsame
Lot steht auf beiden Ebenen senkrecht und hat genau diese Länge.

Beispiel 7: g: x = (1|0|2) + r·(1|0|−1), h: x = (3|5|2) + s·(1|−2|0).
n∘u = n₁ − n₃ = 0 und n∘v = n₁ − 2n₂ = 0. Mit n₁ = 2: n = (2|1|2), |n| = 3.
q − p = (2|5|0), n∘(q − p) = 4 + 5 + 0 = 9, d(g,h) = 9/3 = 3 LE.
(Kontrolle über das gemeinsame Lot: Fußpunkte L₁(3|0|0) auf g bei r = 2 und L₂(5|1|2) auf h bei s = 2,
|L₁L₂| = 3. Das gehört nicht auf die Seite, nur zur Kontrolle.)

**Überblick (Tabelle)**
| Abstand | Weg |
|---|---|
| Punkt–Ebene | Hessesche Normalform oder Lotfußpunkt |
| Punkt–Gerade | Lotfußpunkt über (F − q)∘u = 0 oder Hilfsebene |
| Gerade–Ebene, Ebene–Ebene (parallel) | ein Punkt, dann Punkt–Ebene |
| zwei parallele Geraden | ein Punkt, dann Punkt–Gerade |
| zwei windschiefe Geraden | n ⊥ u und n ⊥ v, dann Hilfsebene und Hesse |
| sich schneidende Objekte | Abstand 0 |

**Vertiefung:** Abschnitt 3 ist die Vertiefung zu Abschnitt 2. Ein weiterer eigener Block ist nicht
nötig, weil windschiefe Geraden als Unterabschnitt in 3 stehen.

---

## 4 Interaktiver Kern (`simulation`): Ein Punkt wandert an einer Ebene vorbei

**Was die Simulation zeigt.** Schrägbild wie in den Vorgängermodulen (x₂ nach rechts, x₃ nach oben,
x₁ nach links unten, halbe Kästchendiagonale). Ebene E: x₁ + 2x₂ + 2x₃ = 6, also n = (1|2|2), d = 6,
|n| = 3, n₃ = 2. Bewusst nicht die Textebene 2x₁ + x₂ + 2x₃ = 6: Deren Normalenvektor erscheint in diesem
Schrägbild genau senkrecht (x₂ − x₁/2 = 0), dann fallen Lot und senkrechter Weg optisch zusammen. Der
Normalenvektor (1|2|2) erscheint schräg. Gezeichnet wird der Ausschnitt von E über dem Rechteck, das alle
Punkte P und F des Datensatzes in x₁ und x₂ umfasst (Rand 0,25). Ein Punkt P läuft auf einer Geraden g:
P(s) = Q₀ + s·e mit e = u/|u|. Der Regler s ist also der Weg auf g in LE (0 bis 6, Schritt 0,25).
Gezeichnet werden g, P, das Lot von P auf E mit Fußpunkt F und auf Wunsch (Kästchen „Weg in x₃-Richtung
zeigen“) die Strecke von P bis zur Ebene in x₃-Richtung, gestrichelt, je nach Lage nach unten oder oben.

**Diagramm, das sich aufbaut.** Darunter: Abstand d(P,E) über dem Weg s (0 bis 6, y-Achse 0 bis 5).
Bei jeder Reglerstellung wird ein Punkt eingetragen, die Spur bleibt stehen, bis der Datensatz wechselt
oder „Spur löschen“ gedrückt wird. Ist das Kästchen aktiv, wird zusätzlich die Weg in x₃-Richtung in einer zweiten
Farbe eingetragen. Knopf „Weg abfahren“ lässt s in etwa 4 Sekunden von 0 bis 6 laufen.

**Rechenformeln.** n = (1|2|2), d = 6, |n| = 3.
- Wert w = n∘P − d (mit Vorzeichen), Abstand d(P,E) = |w| / 3
- Lotfußpunkt F = P − (w/9)·n
- Weg in x₃-Richtung = |w| / n₃ = |w| / 2 (Strecke von P bis zum Ebenenpunkt mit gleichen x₁, x₂)
- Schnittwinkel α von g und E: sin α = |n∘u| / (|n|·|u|) (in der Simulation α wie im Erklärteil, nicht φ)

**Datensätze** (alle |u| = 3, also e = u/3)
| Datensatz | Q₀ (s = 0) | u | n∘u | α | Lage |
|---|---|---|---|---|---|
| 1 | (0\|2\|−1) | (2\|−1\|2) | 4 | 26,39° | schneidet E bei s = 3 in (2\|1\|1) |
| 2 | (0\|3\|3) | (2\|−2\|1) | 0 | 0° | parallel, Abstand stets 2 |
| 3 | (1\|−1\|−1) | (1\|2\|2) | 9 | 90° | senkrecht, schneidet E bei s = 3 in (2\|1\|1) |

**Anzeigen.** s, P, w = n∘P − d, d(P,E), F, „Weg zu E in x₃-Richtung“, α. Zahlen mit zwei Nachkommastellen, Winkel mit
zwei, Dezimalkomma.

**Sollwerte für die Prüfung** (aus `kontrolle.txt`, im Browser alle bestätigt)
| Datensatz, s | P | w | d(P,E) | F | Weg in x₃-Richtung |
|---|---|---|---|---|---|
| 1, s = 0 | (0,00\|2,00\|−1,00) | −4,00 | 1,33 | (0,44\|2,89\|−0,11) | 2,00 |
| 1, s = 3 | (2,00\|1,00\|1,00) | 0,00 | 0,00 | (2,00\|1,00\|1,00) | 0,00 |
| 1, s = 4,5 | (3,00\|0,50\|2,00) | 2,00 | 0,67 | (2,78\|0,06\|1,56) | 1,00 |
| 1, s = 6 | (4,00\|0,00\|3,00) | 4,00 | 1,33 | (3,56\|−0,89\|2,11) | 2,00 |
| 2, s = 1,5 | (1,00\|2,00\|3,50) | 6,00 | 2,00 | (0,33\|0,67\|2,17) | 3,00 |
| 3, s = 0 | (1,00\|−1,00\|−1,00) | −9,00 | 3,00 | (2,00\|1,00\|1,00) | 4,50 |
| 3, s = 4,5 | (2,50\|2,00\|2,00) | 4,50 | 1,50 | (2,00\|1,00\|1,00) | 2,25 |
Winkel: Datensatz 1 α = 26,39°, 2 α = 0,00°, 3 α = 90,00°.

**Beobachtungsauftrag.**
Wähle Datensatz 1 und lass P mit „Weg abfahren“ einmal die ganze Gerade entlanglaufen. Achte auf die
Form des Graphen und darauf, wo P die Ebene durchstößt. Schalte dann „Weg in x₃-Richtung zeigen“
ein und vergleiche die beiden Graphen. Wiederhole das mit Datensatz 3 und lies ab, um wie viel der
Abstand zunimmt, wenn P eine Längeneinheit weiterläuft. Vergleiche diesen Wert mit dem angezeigten
Winkel α. Schreibe einen Satz: „Läuft P eine LE auf g weiter, ändert sich der Abstand um …“

**sim1** — Wie verläuft in Datensatz 1 der Graph des Abstands d(P,E) über dem Weg s?
- A: Er fällt bis s = 3 auf null und bleibt dann null, weil P danach auf der anderen Seite der Ebene liegt. — „Auf der anderen Seite ist P genauso weit von der Ebene entfernt wie vorher. Nur der Wert n∘P − d wechselt bei s = 3 das Vorzeichen, hier von negativ zu positiv. Der Abstand ist sein Betrag und wächst deshalb wieder. Schau auf die Anzeige n∘P − d.“
- B: Er fällt linear bis auf null bei s = 3 und steigt danach linear wieder an; bei s = 3 hat er einen Knick. **(richtig)** — „Richtig. w = n∘P − d ändert sich linear mit s, weil P linear von s abhängt. Der Abstand ist |w|/3, und der Betrag klappt den negativen Teil nach oben. So entsteht ein V mit Knick im Durchstoßpunkt.“
- C: Er hat bei s = 3 ein glattes, parabelförmiges Minimum. — „Glatt und gerundet ist der Abstand zu einem festen Punkt, weil dort eine Wurzel aus einem quadratischen Term entsteht. Der Abstand zu einer Ebene ist der Betrag eines linearen Ausdrucks. Sieh dir die Spur bei s = 3 genau an: Dort ist eine Spitze.“

**sim2** — Datensatz 1 hat α ≈ 26,39°, Datensatz 3 hat α = 90°. Um wie viel ändert sich der Abstand,
wenn P eine Längeneinheit auf g weiterläuft?
- A: um cos α, also in Datensatz 1 um etwa 0,90 LE und in Datensatz 3 gar nicht — „In Datensatz 3 läuft P genau auf dem Lot, der Abstand ändert sich dort also am stärksten und nicht gar nicht. cos α beschreibt, wie weit P dabei parallel zur Ebene vorankommt (Ankathete). Die Abstandsänderung ist die Gegenkathete.“
- B: um tan α, also in Datensatz 1 um etwa 0,50 LE und in Datensatz 3 unbegrenzt — „Der Tangens wäre richtig, wenn s waagerecht gemessen würde wie bei einem Funktionsgraphen. s ist aber der Weg entlang g, also die schräge Seite des Dreiecks. In Datensatz 3 liest du ab: pro LE genau 1 LE, nicht unbegrenzt viel.“
- C: um sin α, also in Datensatz 1 um etwa 0,44 LE und in Datensatz 3 um 1 LE **(richtig)** — „Richtig. Weg auf g, Lot und Strecke in E bilden ein rechtwinkliges Dreieck. Der Weg ist die Hypotenuse, die Abstandsänderung die Gegenkathete zum Winkel α. Abgelesen: von s = 3 bis s = 4,5 steigt der Abstand in Datensatz 1 um 0,67 LE, das sind 0,44 LE pro LE.“

---

## 5 Übungen (`uebungen`)

Einheiten-Auswahl für Zahleneingaben wie in den Vorgängermodulen: `ohne Einheit`, `LE`, `LE²`, `°`.

### a1 — Winkel zwischen Vektoren (AFB I, Zahleneingabe)
Berechne den Winkel zwischen a = (3|0|4) und b = (2|2|1). Gib das Ergebnis in Grad auf zwei
Nachkommastellen an.
- Tipp: Du brauchst drei Zahlen: das Skalarprodukt und die beiden Längen.
- Ansatz: cos φ = a∘b / (|a|·|b|), danach φ mit der Umkehrfunktion des Kosinus bestimmen. Der Taschenrechner muss auf Grad (DEG) stehen.
- Lösungsweg: a∘b = 3·2 + 0·2 + 4·1 = 10. |a| = √(9 + 0 + 16) = 5, |b| = √(4 + 4 + 1) = 3. cos φ = 10/15 = 2/3 ≈ 0,6667. φ = cos⁻¹(2/3) ≈ 48,19°.
- Sollwert 48,19 °, Toleranz 0,03 (Rundung auf zwei Stellen; Zwischenrundung von cos auf 0,667 ergibt cos⁻¹(0,667) = 48,164° ≈ 48,16° und wird akzeptiert; 0,67 ergibt 47,93° und wird abgelehnt). Keine Alternativeinheit.
- ok: „Richtig. cos φ = 10/(5·3) = 2/3, also φ ≈ 48,19°.“
- falschEinheit: „Der Zahlenwert passt, aber ein Winkel wird in Grad angegeben, nicht in LE.“
- nah: „Knapp daneben. Rechne mit cos φ = 2/3 ungerundet weiter, eine früh gerundete Zwischenzahl verschiebt den Winkel. Hast du 41,81° erhalten, hast du den Sinus benutzt: Für den Winkel zwischen zwei Vektoren gilt cos φ = a∘b / (|a|·|b|).“
- weit: „Das passt nicht. Steht der Taschenrechner auf Bogenmaß? Hast du durch beide Längen geteilt? Die Hilfen führen dich Schritt für Schritt.“

### a2 — Abstand Punkt–Ebene (AFB I, Zahleneingabe)
Berechne den Abstand des Punktes Q(5|−1|4) von der Ebene E: 2x₁ − x₂ + 2x₃ = 4.
- Tipp: Du musst den Lotfußpunkt nicht ausrechnen.
- Ansatz: d(Q,E) = |n∘q − d| / |n| mit n = (2|−1|2) und d = 4.
- Lösungsweg: n∘q = 2·5 + (−1)·(−1) + 2·4 = 10 + 1 + 8 = 19. n∘q − d = 15. |n| = √(4 + 1 + 4) = 3. d(Q,E) = 15/3 = 5 LE.
- Sollwert 5 LE, Toleranz 0,01.
- ok: „Richtig. |19 − 4| / 3 = 5 LE.“
- falschEinheit: „Der Zahlenwert passt. Ein Abstand ist eine Länge, die Einheit ist LE.“
- nah: „Fast. Achte auf das Vorzeichen: Bei −x₂ und q₂ = −1 ergibt sich (−1)·(−1) = +1. Mit −1 kommst du auf |17 − 4| / 3 ≈ 4,33.“
- weit: „Hast du durch |n| geteilt? Ohne Division erhältst du 15. Der Abstand ist |n∘q − d| geteilt durch die Länge des Normalenvektors.“

### a3 — Welcher Rechenweg passt? (AFB II, Zuordnung, einzige Zuordnungsaufgabe)
Vier Skizzen (Inline-SVG):
- A: zwei sich schneidende Geraden mit markiertem Winkel
- B: Gerade, die eine Ebene durchstößt, mit markiertem Winkel zwischen Gerade und Ebene
- C: zwei Ebenen mit Schnittgerade und markiertem Winkel
- D: Punkt über einer Ebene mit Lot und Fußpunkt

Ordne jeder Situation die Skizze zu, die das mathematische Modell zeigt (Zeilenreihenfolge ≠ Skizzen):
- „Eine Solaranlage soll wissen, unter welchem Winkel das Sonnenlicht auf die Modulfläche fällt.“ → **B**
- „Ein Dachdecker will wissen, wie weit die Spitze eines Antennenmasts von der schrägen Dachfläche entfernt ist.“ → **D**
- „Zwei Kondensstreifen kreuzen sich am Himmel in einem Punkt. Gesucht ist der Winkel, unter dem sie sich treffen.“ → **A**
- „Eine Rampe ist gegenüber dem Hallenboden geneigt. Gesucht ist ihr Neigungswinkel.“ → **C**
Rückmeldung bei Teilerfolg (nennt die Strategie, nicht die Lösung): „Frage dich bei jeder Situation zuerst: Welche Objekte kommen vor, ein Punkt, eine Richtung (Gerade) oder eine Fläche (Ebene)? Ein Lichtstrahl ist eine Richtung, eine Dachfläche oder ein Boden eine Ebene.“
Hilfen: Tipp „Übersetze jedes Ding in ein Objekt: Strahl oder Streifen → Gerade, Fläche → Ebene, Spitze → Punkt.“ · Ansatz „Zähle in jeder Skizze, was zu sehen ist: Wie viele Geraden, wie viele Flächen, gibt es einen einzelnen Punkt? Zähle dasselbe in jeder Situation und vergleiche.“ · Lösungsweg „Sonnenlicht ist eine Richtung, die Modulfläche eine Ebene: B. Mastspitze ist ein Punkt, das Dach eine Ebene, gesucht ein Abstand: D. Zwei Kondensstreifen sind zwei Geraden mit Schnittpunkt: A. Rampe und Boden sind zwei Ebenen: C.“ (Keine Stufe 9 bei der Zuordnung, siehe `fallen.md`.)

### a4 — Landeanflug (AFB II, Zahleneingabe)
Die Drohne aus dem Einstieg landet auf dem Garagendach E: −2x₂ + 5x₃ = 15. Im Landeanflug bewegt sie
sich in Richtung u = (4|0|−3). Berechne den Winkel, unter dem ihre Flugbahn auf die Dachfläche trifft.
- Tipp: Gesucht ist der Winkel zwischen einer Geraden und einer Ebene, nicht zwischen zwei Vektoren.
- Ansatz: sin α = |n∘u| / (|n|·|u|) mit n = (0|−2|5).
- Lösungsweg: n∘u = 0·4 + (−2)·0 + 5·(−3) = −15, also |n∘u| = 15. |n| = √(0 + 4 + 25) = √29 ≈ 5,385. |u| = √(16 + 0 + 9) = 5. sin α = 15/(5·√29) = 3/√29 ≈ 0,5571. α ≈ 33,85°.
- Sollwert 33,85 °, Toleranz 0,05 (Zwischenrundung von √29 auf 5,39 ergibt 33,82°).
- ok: „Richtig. sin α = 15/(5·√29) ≈ 0,5571, also α ≈ 33,85°.“
- falschEinheit: „Der Zahlenwert passt, aber ein Winkel wird in Grad angegeben.“
- nah: „Prüfe zwei Dinge. Ist dein Winkel negativ, fehlt der Betrag von n∘u: Ein Schnittwinkel liegt zwischen 0° und 90°. Hast du 56,15° erhalten, hast du den Kosinus benutzt. Das ist der Winkel zwischen Flugbahn und Normalenvektor, zur Dachfläche gehört der Sinus.“ (−33,85° landet wegen |v/Sollwert| = 1 im nah-Bereich.)
- weit: „Prüfe den Normalenvektor: Er besteht aus den Koeffizienten der Koordinatengleichung, also (0|−2|5). Und nimm den Betrag von n∘u.“

### a5 — Abstand Punkt–Gerade (AFB II, Zahleneingabe)
Berechne den Abstand des Punktes Q(8|7|0) von der Geraden g: x = (2|1|0) + r·(1|2|2).
- Tipp: Der Punkt auf g, der Q am nächsten liegt, ist der Lotfußpunkt.
- Ansatz: F = p + r·u. Bestimme r aus (p + r·u − q)∘u = 0, dann d(Q,g) = |QF|.
- Lösungsweg: F − q = (2 + r − 8 | 1 + 2r − 7 | 2r) = (r − 6 | 2r − 6 | 2r). (F − q)∘u = (r − 6) + 2(2r − 6) + 2·2r = 9r − 18 = 0, also r = 2. F(4|5|4), F − q = (−4|−2|4), |QF| = √(16 + 4 + 16) = 6 LE.
- Sollwert 6 LE, Toleranz 0,01.
- ok: „Richtig. r = 2, F(4|5|4), |QF| = 6 LE.“
- falschEinheit: „Der Zahlenwert passt, die Einheit eines Abstands ist LE.“
- nah: „Du hast vermutlich die Entfernung zum Stützpunkt (2|1|0) berechnet, das sind √72 ≈ 8,49 LE. Der Stützpunkt ist aber nicht der nächste Punkt der Geraden. Bestimme zuerst den Lotfußpunkt.“
- weit: „Stelle F − q in Abhängigkeit von r auf und setze das Skalarprodukt mit u gleich null. Die Hilfen zeigen den Weg.“

### a6 — Abstand windschiefer Geraden (AFB II, Zahleneingabe)
Die Geraden g: x = (0|0|1) + r·(1|2|0) und h: x = (5|0|2) + s·(0|2|1) sind windschief. Berechne ihren
Abstand.
- Tipp: Du brauchst einen Vektor, der auf beiden Richtungsvektoren senkrecht steht.
- Ansatz: n∘u = 0 und n∘v = 0 lösen (eine Koordinate frei wählen). Dann d(g,h) = |n∘(q − p)| / |n|.
- Lösungsweg: n₁ + 2n₂ = 0 und 2n₂ + n₃ = 0. Mit n₂ = −1: n₁ = 2, n₃ = 2, also n = (2|−1|2), |n| = 3. q − p = (5|0|1). n∘(q − p) = 10 + 0 + 2 = 12. d(g,h) = 12/3 = 4 LE.
- Sollwert 4 LE, Toleranz 0,01.
- ok: „Richtig. n = (2|−1|2), |12| / 3 = 4 LE.“
- falschEinheit: „Der Zahlenwert passt, die Einheit eines Abstands ist LE.“
- nah: „Fast. Hast du durch |n| geteilt? Hier ist |n| = 3. Oder du hast den Abstand von (5|0|2) zu g bestimmt (≈ 4,58 LE), das ist nicht der kürzeste Abstand der beiden Geraden.“
- weit: „Kontrolliere n: Es muss mit (1|2|0) und mit (0|2|1) das Skalarprodukt 0 ergeben. Teile am Ende durch |n|. Die Hilfen zeigen den Weg.“

Hinweis für den Bau: 12 liegt außerhalb des nah-Bereichs (Faktor 3), deshalb nennt `weit` neben der
Kontrolle von n auch die Division durch |n|. Werte im nah-Bereich: 4,58 (Punkt-Gerade statt Gerade-Gerade), 6 (|n| falsch als 2).

### a7 — Punkt mit gegebenem Abstand (AFB II, Zahleneingabe, Umkehraufgabe)
Der Punkt Q_a(a|1|2) soll von der Ebene E: 2x₁ − x₂ + 2x₃ = 4 den Abstand 3 LE haben. Es gibt zwei
passende Werte für a. Bestimme beide und gib den größeren ein.
- Tipp: Diesmal kennst du den Abstand und suchst den Punkt. Rechne trotzdem mit der Formel für den Abstand, nur rückwärts.
- Ansatz: q = (a|1|2) in die Hessesche Normalform einsetzen und gleich 3 setzen. Eine Gleichung mit Betrag hat zwei Fälle.
- Lösungsweg: n∘q − d = 2a − 1 + 4 − 4 = 2a − 1, |n| = 3. |2a − 1| / 3 = 3, also |2a − 1| = 9. Fall 1: 2a − 1 = 9, a = 5. Fall 2: 2a − 1 = −9, a = −4. Q₅(5|1|2) und Q₋₄(−4|1|2) liegen auf verschiedenen Seiten von E (n∘q − d = 9 bzw. −9). Der größere Wert ist a = 5.
- Sollwert 5 (ohne Einheit), Toleranz 0,01.
- ok: „Richtig. |2a − 1| / 3 = 3 ergibt a = 5 oder a = −4, der größere Wert ist 5.“
- falschEinheit: „Der Zahlenwert passt. Gefragt ist nur die Koordinate a, also eine Zahl ohne Einheit.“
- nah: „Fast. Hast du −4 eingegeben, ist das die zweite Lösung, gefragt ist die größere. Sonst prüfe den Zähler: n∘q − d = 2a − 1 + 4 − 4 = 2a − 1. Ohne Abzug von d erhältst du a = 3.“ (−4 hat Faktor 0,8, a = 3 aus |2a + 3| = 9 Faktor 0,6, beide im nah-Bereich.)
- weit: „Hast du durch |n| = 3 geteilt? Ohne Division wird aus |2a − 1| = 3 der Wert a = 2. Die Hilfen zeigen den Weg.“

### a8 — Lenas Rechnung bewerten (AFB III, offen, Bewertung)
Lena soll den Abstand der parallelen Ebenen E₁: 2x₁ + x₂ + 2x₃ = 6 und E₂: 4x₁ + 2x₂ + 4x₃ = 30
bestimmen. Sie schreibt: „Die Ebenen sind parallel, also ist der Abstand die Differenz der rechten
Seiten: 30 − 6 = 24.“ Beurteile Lenas Vorgehen und bestimme den richtigen Abstand.
- Tipp: Setze in Lenas Idee eine Ebene ein, deren Gleichung du mit 10 multiplizierst. Ändert sich der Abstand?
- Ansatz: Bringe beide Gleichungen auf denselben Normalenvektor und teile die Differenz der rechten Seiten durch |n|. Oder: Punkt aus E₁ wählen und Hesse für E₂ anwenden.
- Lösungsweg: E₂ durch 2 geteilt: 2x₁ + x₂ + 2x₃ = 15, also gleicher Normalenvektor n = (2|1|2) wie E₁. Differenz der rechten Seiten 15 − 6 = 9, |n| = 3, Abstand 9/3 = 3 LE. Kontrolle: (3|0|0) liegt in E₁, d((3|0|0),E₂) = |4·3 − 30| / |(4|2|4)| = 18/6 = 3 LE.
- Musterlösung (Stufe 9): Lenas Idee hat einen richtigen Kern, ihre Rechnung ist aber zweimal falsch. Richtig ist: Bei parallelen Ebenen haben alle Punkte denselben Abstand, und dieser hängt mit dem Unterschied der rechten Seiten zusammen. Falsch ist erstens, dass sie die Gleichungen nicht auf denselben Normalenvektor gebracht hat. E₂ hat den doppelten Normalenvektor. Erst nach dem Teilen durch 2 lautet E₂: 2x₁ + x₂ + 2x₃ = 15, und die Differenz ist 9, nicht 24. Falsch ist zweitens, dass die Differenz der rechten Seiten noch keine Länge ist. Eine Koordinatengleichung lässt sich mit jeder Zahl multiplizieren, ohne dass sich die Ebene ändert. Eine Differenz, die sich dabei mitverändert, kann kein Abstand sein. Erst die Division durch |n| = 3 macht daraus die Länge 3 LE. Kontrolle mit der Hesseschen Normalform am Punkt (3|0|0) aus E₁ bestätigt 3 LE. Urteil: Lenas Ergebnis ist um den Faktor 8 zu groß, ihr Ansatz taugt nur mit gleichem Normalenvektor und anschließender Division durch dessen Länge.
- **Bewertungskriterien:** erkennt den richtigen Kern (paralleler Abstand konstant, Differenz der rechten Seiten) · bemerkt den unterschiedlichen Normalenvektor und normiert E₂ · begründet, warum eine Differenz der rechten Seiten ohne Division durch |n| keine Länge ist (Gleichung beliebig skalierbar) · berechnet 3 LE · formuliert ein klares Urteil

### a9 — Eine Abkürzung für windschiefe Geraden? (AFB III, offen, Bewertung)
Tim behauptet: „Den Abstand zweier windschiefer Geraden g und h bekomme ich einfacher: Ich nehme den
Stützpunkt Q von h und berechne seinen Abstand zu g.“ Prüfe die Behauptung an g: x = (0|0|1) + r·(1|2|0)
und h: x = (5|0|2) + s·(0|2|1) aus Aufgabe a6 und beurteile Tims Verfahren allgemein.
- Tipp: Der Stützpunkt von h ist ein Punkt unter vielen. Ist er der Punkt von h, der g am nächsten kommt?
- Ansatz: Abstand von Q(5|0|2) zu g über den Lotfußpunkt bestimmen und mit dem Ergebnis 4 LE aus a6 vergleichen. Dann überlegen, wann beide Werte übereinstimmen.
- Lösungsweg: F = (r | 2r | 1), F − q = (r − 5 | 2r | −1). (F − q)∘(1|2|0) = r − 5 + 4r = 5r − 5 = 0, also r = 1, F(1|2|1). |QF| = |(−4|2|−1)| = √21 ≈ 4,58 LE. Der tatsächliche Abstand der Geraden ist 4 LE. Tims Verfahren liefert hier einen zu großen Wert.
- Musterlösung (Stufe 9): Tims Verfahren ist im Allgemeinen falsch. Am Beispiel ergibt sich √21 ≈ 4,58 LE, der Abstand der Geraden beträgt aber 4 LE. Der Grund: Der Abstand zweier Geraden ist die kürzeste Entfernung zwischen irgendeinem Punkt von g und irgendeinem Punkt von h. Tim legt den Punkt auf h aber willkürlich fest und sucht nur noch auf g den nächsten Punkt. Er minimiert also nur über eine der beiden Geraden. Sein Wert ist deshalb immer mindestens so groß wie der wahre Abstand und nur dann gleich, wenn der Stützpunkt zufällig der Fußpunkt des gemeinsamen Lots ist. Das gemeinsame Lot steht auf beiden Geraden senkrecht. Tims Strecke QF steht nur auf g senkrecht: (−4|2|−1)∘(0|2|1) = 3 ≠ 0. Urteil: Tims Abkürzung liefert nur eine obere Schranke. Richtig ist das Verfahren mit einem Vektor, der auf beiden Richtungen senkrecht steht.
- **Bewertungskriterien:** berechnet den Abstand von Q zu g korrekt (√21 ≈ 4,58 LE) · vergleicht mit 4 LE und stellt fest, dass der Wert zu groß ist · begründet allgemein (nur über eine Gerade minimiert, Punkt auf h willkürlich) · nennt die Bedingung für Gleichheit (QF steht auch auf v senkrecht) · formuliert ein klares Urteil

---

## 6 Abschluss (`abschluss`)

**Kernaussagen**
1. Das Skalarprodukt verbindet Rechnen und Geometrie: a∘b = |a|·|b|·cos φ. Sein Vorzeichen zeigt, ob der Winkel spitz, recht oder stumpf ist.
2. Schnittwinkel liegen zwischen 0° und 90°. Bei Gerade und Ebene gehört der Sinus dazu, weil der Normalenvektor den Winkel zu 90° ergänzt.
3. Abstand heißt kürzeste Verbindung, und die steht senkrecht: Das Lot führt immer zum Abstand.
4. Die Hessesche Normalform d(Q,E) = |n∘q − d| / |n| ist das Lotfußpunktverfahren in einer Formel. Abstände zu Geraden und zwischen windschiefen Geraden führst du auf Lotfußpunkt oder Hilfsebene zurück.

**Zentralabitur.** In Abituraufgaben zur analytischen Geometrie stecken Winkel und Abstände fast immer
in einem Sachkontext: Dachflächen, Flugbahnen, Lichtstrahlen, Pyramiden. Typisch ist die Folge:
Ebene aufstellen, Abstand eines Punktes oder Winkel bestimmen, Ergebnis im Kontext deuten. Oft kommt
eine Begründungsaufgabe dazu, etwa warum ein Lotfußpunkt im Inneren einer Fläche liegt oder warum ein
Verfahren den kürzesten Abstand liefert. Schreib bei Winkeln immer dazu, welchen Winkel du berechnest,
und bei Abständen, welches Verfahren du nutzt.

**Selbstcheck**
- Ich kann das Skalarprodukt geometrisch deuten und mit dem Kosinussatz begründen, warum a∘b = |a|·|b|·cos φ gilt.
- Ich kann Winkel zwischen Vektoren und Schnittwinkel zwischen Geraden und Ebenen berechnen und weiß, wann Sinus und wann Betrag nötig sind.
- Ich kann den Lotfußpunkt eines Punktes auf einer Ebene und auf einer Geraden bestimmen.
- Ich kann den Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen und die Formel herleiten.
- Ich kann den Abstand windschiefer Geraden bestimmen und begründen, warum das Verfahren den kürzesten Abstand liefert.
- Ich kann Winkel und Abstände in Sachsituationen einsetzen und Lösungswege anderer beurteilen.

**Lehrerteil**
- *Einordnung:* Inhaltsfeld „Analytische Geometrie und Lineare Algebra“, letzter Baustein der Q1-Geometrie nach Vektoren, Geraden und Ebenen, Lagebeziehungen. Voraussetzung: Skalarprodukt in Koordinaten und Orthogonalitätskriterium (Modul „Geraden und Ebenen“), Schnitt Gerade/Ebene (Modul „Lagebeziehungen“).
- *Kompetenzen:* Argumentieren (Herleitungen, Begründung des kürzesten Abstands, a8, a9), Modellieren (Drohnenkontext, a3, a4), Problemlösen (Umkehraufgabe a7), Werkzeuge nutzen (Simulation mit Diagramm).
- *Zeitbedarf:* Einstieg 10 min · Skalarprodukt und Winkel 30 min · Abstände einschließlich windschiefer Geraden 35 min · Simulation 15 min · Übungen 25 min · Abschluss 5 min, zusammen etwa 120 min.
- *Typische Fehler:* (1) Kosinus statt Sinus bei Gerade/Ebene. Anhalten bei Beispiel 3 und die Kontrolle „senkrechte Gerade muss 90° ergeben“ gemeinsam durchführen. (2) Betrag beim Schnittwinkel vergessen, stumpfe Winkel als Schnittwinkel angegeben. (3) Höhenunterschied in x₃-Richtung oder Entfernung zum Stützpunkt als Abstand. Anhalten beim Drohnenbeispiel: 7 m gegen 6,50 m an einer Skizze. (4) Division durch |n| vergessen. Hier hilft das Argument, dass eine Koordinatengleichung beliebig skaliert werden darf. (5) Bei windschiefen Geraden nur über einen Punkt minimiert (Aufgabe a9). (6) Bei Umkehraufgaben nur eine Lösung, weil der Betrag nicht in zwei Fälle aufgelöst wurde. a7 nennt deshalb ausdrücklich zwei Werte, prüft aber nur den größeren: im Unterricht nachfragen, ob beide Fälle gerechnet wurden.
- *Differenzierung:* Schnellere bestimmen in Beispiel 7 zusätzlich die Fußpunkte des gemeinsamen Lots (zwei Bedingungen, zwei Parameter, Ergebnis L₁(3|0|0), L₂(5|1|2)). Langsamere bearbeiten zuerst a1, a2, a4 und nutzen Verfahren 1 statt der Formel, bis die Herleitung verstanden ist.
- *Realexperiment:* Mit einem Brett als Ebene, einem Zollstock und einer Schnur lässt sich zeigen, dass der kürzeste Weg von einer Punktmarke zur geneigten Fläche senkrecht auf ihr steht und kürzer ist als das senkrechte Lot zum Boden. Für Winkel: Neigung einer Rampe mit einer Winkelmesser-App messen und mit der Rechnung vergleichen.

---

## Formelleiste (Datenvertrag, Texte wörtlich übernehmen)

Mathematik: Feld `einheit` entfällt.

**Gruppe `winkel`, Titel „Skalarprodukt und Winkel“**

1. `skalargeo`, Ziel `f-skalargeo`
   - tex `\vec{a}\circ\vec{b} = |\vec{a}|\cdot|\vec{b}|\cdot\cos\varphi` · plain `a→∘b→ = |a→|·|b→|·cos φ`
   - Zeichen: a→, b→ „zwei Vektoren, am selben Punkt angesetzt“ · |a→|, |b→| „Längen (Beträge) der Vektoren“ · φ „Winkel zwischen den beiden Pfeilen“
   - gilt: „Für alle Vektoren ungleich dem Nullvektor im Raum und in der Ebene. φ liegt zwischen 0° und 180°.“
   - fehler: „Das Skalarprodukt als Vektor aufschreiben. Es ist eine Zahl: Aus zwei Vektoren wird ein Skalar.“
2. `winkelvek`, Ziel `f-winkelvek`
   - tex `\cos\varphi = \dfrac{\vec{a}\circ\vec{b}}{|\vec{a}|\cdot|\vec{b}|}` · plain `cos φ = (a→∘b→) / (|a→|·|b→|)`
   - Zeichen: φ „Winkel zwischen a→ und b→“ · a→∘b→ „Skalarprodukt, a₁b₁ + a₂b₂ + a₃b₃“ · |a→|·|b→| „Produkt der Längen“
   - gilt: „Für den Winkel zwischen zwei Vektoren. Ohne Betrag im Zähler, deshalb sind auch stumpfe Winkel möglich.“
   - fehler: „Nur durch eine der beiden Längen teilen. Dann ist der Quotient kein Kosinus mehr und kann sogar größer als 1 werden.“
3. `schnittgg`, Ziel `f-schnittgg`
   - tex `\cos\alpha = \dfrac{|\vec{u}\circ\vec{v}|}{|\vec{u}|\cdot|\vec{v}|}` · plain `cos α = |u→∘v→| / (|u→|·|v→|)`
   - Zeichen: α „Schnittwinkel der Geraden“ · u→, v→ „Richtungsvektoren der beiden Geraden“
   - gilt: „Für zwei Geraden, die sich schneiden. Der Schnittwinkel liegt zwischen 0° und 90°.“
   - fehler: „Den Betrag im Zähler weglassen und einen stumpfen Winkel als Schnittwinkel angeben. Der Richtungsvektor könnte genauso gut −u→ sein.“
4. `schnittge`, Ziel `f-schnittge`
   - tex `\sin\alpha = \dfrac{|\vec{n}\circ\vec{u}|}{|\vec{n}|\cdot|\vec{u}|}` · plain `sin α = |n→∘u→| / (|n→|·|u→|)`
   - Zeichen: α „Winkel zwischen Gerade und Ebene“ · n→ „Normalenvektor der Ebene“ · u→ „Richtungsvektor der Geraden“
   - gilt: „Für eine Gerade, die die Ebene schneidet. α liegt zwischen 0° und 90°. Ist die Gerade parallel zur Ebene, ergibt sich 0°.“
   - fehler: „Den Kosinus nehmen. Damit berechnest du den Winkel zwischen Gerade und Normalenvektor, der α zu 90° ergänzt.“
5. `schnittee`, Ziel `f-schnittee`
   - tex `\cos\alpha = \dfrac{|\vec{n}_1\circ\vec{n}_2|}{|\vec{n}_1|\cdot|\vec{n}_2|}` · plain `cos α = |n→₁∘n→₂| / (|n→₁|·|n→₂|)`
   - Zeichen: α „Schnittwinkel der Ebenen“ · n→₁, n→₂ „Normalenvektoren der beiden Ebenen“
   - gilt: „Für zwei Ebenen, die sich schneiden. Der Schnittwinkel liegt zwischen 0° und 90°.“
   - fehler: „Spannvektoren statt Normalenvektoren nehmen. Der Winkel zwischen zwei beliebigen Spannvektoren hat mit der Neigung der Ebenen nichts zu tun.“

**Gruppe `abstaende`, Titel „Abstände“**

6. `lotgerade`, Ziel `f-lotgerade`
   - tex `\vec{x} = \vec{q} + t\cdot\vec{n}` · plain `x→ = q→ + t·n→`
   - Zeichen: q→ „Ortsvektor des Punktes Q“ · n→ „Normalenvektor der Ebene, Richtung des Lots“ · t „Parameter“
   - gilt: „Gerade durch Q, die senkrecht auf der Ebene steht. Ihr Schnittpunkt mit der Ebene ist der Lotfußpunkt F.“
   - fehler: „Einen Spannvektor der Ebene als Richtung nehmen. Dann läuft die Gerade parallel zur Ebene statt senkrecht auf sie zu.“
7. `hnf`, Ziel `f-hnf`
   - tex `d(Q,E) = \dfrac{|\vec{n}\circ\vec{q} - d|}{|\vec{n}|}` · plain `d(Q,E) = |n→∘q→ − d| / |n→|`
   - Zeichen: d(Q,E) „Abstand des Punktes Q von der Ebene E“ · n→ „Normalenvektor aus der Koordinatenform n→∘x→ = d“ · q→ „Ortsvektor von Q“ · d „rechte Seite der Koordinatenform“
   - gilt: „Für jeden Punkt und jede Ebene in Koordinatenform. Für Punkte in E ergibt sich 0.“
   - fehler: „Den Zähler nicht durch |n→| teilen. Die Koordinatengleichung darf man mit jeder Zahl multiplizieren, der Zähler allein ist deshalb keine Länge.“
8. `lotfussg`, Ziel `f-lotfussg`
   - tex `(\vec{p} + r\cdot\vec{u} - \vec{q})\circ\vec{u} = 0` · plain `(p→ + r·u→ − q→)∘u→ = 0`
   - Zeichen: p→ „Stützvektor der Geraden g“ · u→ „Richtungsvektor von g“ · q→ „Ortsvektor des Punktes Q“ · r „Parameter des Lotfußpunkts F“
   - gilt: „Bestimmt den Lotfußpunkt F = p→ + r·u→ von Q auf g. Der Abstand ist dann d(Q,g) = |QF|.“
   - fehler: „Die Entfernung von Q zum Stützpunkt der Geraden als Abstand nehmen. Der Stützpunkt ist nur zufällig der nächste Punkt.“
9. `windschief`, Ziel `f-windschief`
   - tex `d(g,h) = \dfrac{|\vec{n}\circ(\vec{q} - \vec{p})|}{|\vec{n}|}` · plain `d(g,h) = |n→∘(q→ − p→)| / |n→|`
   - Zeichen: d(g,h) „Abstand der windschiefen Geraden g und h“ · n→ „Vektor, der auf beiden Richtungsvektoren senkrecht steht“ · p→, q→ „Stützvektoren von g und h“
   - gilt: „Für windschiefe Geraden g: x→ = p→ + r·u→ und h: x→ = q→ + s·v→ mit n→∘u→ = 0 und n→∘v→ = 0.“
   - fehler: „Für n→ nur einen Vektor senkrecht zu u→ nehmen. Er muss auf beiden Richtungsvektoren senkrecht stehen.“

Abgleich mit den Fragen: Kein Leisteneintrag nennt die Form des Abstandsgraphen (sim1) oder die
Abstandsänderung pro LE (sim2). Die Leiste erklärt keinen Kosinussatz (vw1), keine Betragsformel (vw2)
und keinen Steigungswinkel (vw3).

---

## Checkliste für den Bau

- Sections: `einstieg`, `winkel`, `abstaende`, `simulation`, `uebungen`, `abschluss` (Nr. 1 bis 6)
- MC: `vw1` (r 0), `vw2` (r 1), `vw3` (r 2), `sim1` (r 1), `sim2` (r 2)
- Zahl: `a1` (48,19 °, tol 0,03), `a2` (5 LE, tol 0,01), `a4` (33,85 °, tol 0,05), `a5` (6 LE, tol 0,01), `a6` (4 LE, tol 0,01), `a7` (5 ohne Einheit, tol 0,01)
- Zuordnung: `a3` (Zeilen B, D, A, C)
- Offen mit Stufe 9 und drei Hilfestufen: `a8`, `a9`
- Export-Namen: vw1 „Vorwissen 1“ … sim2 „Simulation 2“, a1 „Winkel zwischen Vektoren“, a2 „Abstand Punkt–Ebene“, a3 „Welcher Rechenweg passt?“, a4 „Landeanflug“, a5 „Abstand Punkt–Gerade“, a6 „Windschiefe Geraden“, a7 „Punkt mit gegebenem Abstand“
- Abbildungen (Inline-SVG, erzeugt von `output/mathe-q1-abstaende-winkel/fig.py`): FIG1 Vektoren mit Winkel und Verbindungsvektor (Herleitung), FIG2 Gerade/Ebene mit Normalenvektor, α und 90° − α, FIG3 Lot mit Fußpunkt und senkrechtem Weg nach unten, Zuordnung A bis D
- Formelleiste: 9 Einträge, Gruppen `winkel` (5) und `abstaende` (4)
- Simulation: Canvas Schrägbild + Canvas Diagramm, Datensätze 1 bis 3, Regler s, Kästchen Weg in x₃-Richtung, Knöpfe „Weg abfahren“, „Spur löschen“

## Offen

- **Kernlehrplan:** Ob die Hessesche Normalform, der Abstand Punkt–Gerade und der Abstand windschiefer
  Geraden im LK verbindlich sind, ist mit der vorhandenen Lehrplannotiz nicht belegt. Die Notiz nennt nur
  „Skalarprodukt, Abstände und Winkel“ als Teil der Q1-Geometrie. Kein Zitat erfunden. Darren fragen, ob
  der schulinterne Plan windschiefe Geraden vorsieht.
- **Kreuzprodukt:** weiterhin nicht genutzt (offene Frage aus den Vorgängermodulen). Der Normalenvektor
  für windschiefe Geraden kommt aus zwei Gleichungen. Falls der Kurs das Kreuzprodukt kennt, ließe sich
  ein Hinweis ergänzen.
- **Schreibweise d(Q,E):** Das d steht für Abstand und zugleich für die rechte Seite der Koordinatenform.
  Der Text weist darauf hin. Falls der Kurs die Koordinatenform anders schreibt, anpassen.
- **Vertiefung:** kein eigener Block, Abschnitt 3 übernimmt diese Rolle (windschiefe Geraden als
  LK-Unterabschnitt).
- **Kosinussatz:** vw1 und die Herleitung des Skalarprodukts setzen ihn voraus. Ob er im Kurs schon
  behandelt wurde, ist nicht geklärt (Frage aus der Fachprüfung).
- **a4:** Der Startpunkt des Landeanflugs ist nicht genannt. Von S(0|0|10) aus träfe die Bahn die
  Dachebene neben dem Dachstück (x₁ ≈ 9,33). Für die Winkelrechnung unerheblich.
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
