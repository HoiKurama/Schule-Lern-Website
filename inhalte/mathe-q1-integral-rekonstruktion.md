# Modulinhalt: Rekonstruktion von Beständen — der Weg zum bestimmten Integral

**Dateiname des Moduls:** `module/mathe-q1-integral-rekonstruktion.html`
**Fach:** Mathematik · **Kursniveau:** Leistungskurs Q1
**Inhaltsfeld (Chip im Seitenkopf, wörtlich nach `fachliches/kernlehrplan-nrw.md`):** Funktionen und Analysis
**Farbtokens:** `--akzent: #0d7a52` · `--akzent-hell: #e7f6ef` · `--akzent-rand: #b5e0cd`
**Kopfzeit-Chip:** ca. 90 Minuten

**Aufbau:** sechs `<section>`-Blöcke mit nummeriertem `.stufe`-Kopf, Reihenfolge wie unten.
**Kontrollskript:** `scratchpad/vorarbeit/mathe/kontrolle_integral.py` (alle Zahlen dieser Datei sind damit geprüft).

---

## 0 · Kontrollrechnungen (Sammelstelle)

Alle Zahlenwerte, die im Modul erscheinen, mit Rechenweg. Der Bauagent muss hier nichts nachrechnen,
aber er darf jede Zahl gegen diese Liste prüfen.

**K1 — Vorwissensfrage 1, mittlere Änderungsrate**
(54 m³ − 30 m³) / (6 h − 2 h) = 24 m³ / 4 h = **6 m³/h**.
Distraktorwerte: 54 − 30 = 24 (nur Differenz), 54/6 = 9 (Endbestand durch Endzeit).

**K2 — Vorwissensfrage 3, Weg aus konstanter Geschwindigkeit**
20 min = 1200 s; s = 15 m/s · 1200 s = 18 000 m = **18 km**.

**K3 — Einstieg/Aufgabe a1, Wallbox als Produktsumme**
11,0 kW · 1,5 h = 16,50 kWh
7,4 kW · 1,0 h = 7,40 kWh
3,7 kW · 0,5 h = 1,85 kWh
Summe = 16,50 + 7,40 + 1,85 = **25,75 kWh** = 25 750 Wh.

**K4 — Treppenrate im Erklärteil (ungleich breite Streifen)**
2,0 m³/h · 2 h = 4,0 m³
3,5 m³/h · 1 h = 3,5 m³
4,5 m³/h · 2 h = 9,0 m³
2,5 m³/h · 1 h = 2,5 m³
Summe = 4,0 + 3,5 + 9,0 + 2,5 = **19,0 m³**.
Mittlere Rate über die 6 h: 19,0 m³ / 6 h = 3,1666… ≈ **3,17 m³/h**.

**K5 — f(x) = x² auf [0; 3], Unter- und Obersumme**
n = 3, Δx = 1: U₃ = 1·(0² + 1² + 2²) = 0 + 1 + 4 = **5**; O₃ = 1·(1² + 2² + 3²) = 1 + 4 + 9 = **14**; O₃ − U₃ = **9**.
n = 6, Δx = 0,5: U₆ = 0,5·(0 + 0,25 + 1 + 2,25 + 4 + 6,25) = 0,5 · 13,75 = **6,875**;
O₆ = 0,5·(0,25 + 1 + 2,25 + 4 + 6,25 + 9) = 0,5 · 22,75 = **11,375**; O₆ − U₆ = **4,5**.
Allgemein (Herleitung im Modul): U_n = 9 − 13,5/n + 4,5/n², O_n = 9 + 13,5/n + 4,5/n², O_n − U_n = 27/n.
Probe n = 3: 9 − 4,5 + 0,5 = 5 ✓; 9 + 4,5 + 0,5 = 14 ✓. Probe n = 6: 9 − 2,25 + 0,125 = 6,875 ✓; 9 + 2,25 + 0,125 = 11,375 ✓.
Probe n = 100: U = 8,86545; O = 9,13545; Differenz 0,27 = 27/100 ✓. Grenzwert **9**.

**K6 — Simulationsfunktion f(t) = −0,2 t² + 1,6 t + 1,8 (Zuflussrate in m³/h, t in h)**
Scheitel: t_S = −1,6 / (2·(−0,2)) = **4,0 h**, f(4) = −0,2·16 + 6,4 + 1,8 = −3,2 + 8,2 = **5,0 m³/h**.
Nullstellen: t₁ = −1,0 (außerhalb), t₂ = **9,0 h**.
Wertetabelle: f(0)=1,8 · f(1)=3,2 · f(2)=4,2 · f(3)=4,8 · f(4)=5,0 · f(4,5)=4,95 · f(5)=4,8 · f(6)=4,2 ·
f(7)=3,2 · f(8)=1,8 · f(9)=0 · f(10)=−2,2 · f(11)=−4,8 · f(12)=−7,8.
Grenzwertfunktion (nur intern für die Anzeige, siehe Warnhinweis in Abschnitt 4):
I(b) = −b³/15 + 0,8 b² + 1,8 b. Ableitungsprobe: I′(t) = −3t²/15 + 1,6 t + 1,8 = −0,2 t² + 1,6 t + 1,8 = f(t) ✓.
I(3) = −27/15 + 7,2 + 5,4 = −1,8 + 12,6 = **10,8** · I(6) = −216/15 + 28,8 + 10,8 = −14,4 + 39,6 = **25,2** ·
I(9) = −729/15 + 64,8 + 16,2 = −48,6 + 81,0 = **32,4** · I(12) = −1728/15 + 115,2 + 21,6 = −115,2 + 136,8 = **21,6**.

**K7 — Startanzeige der Simulation, b = 6,0 h, n = 4, Δt = 1,5 h**
| Streifen | Intervall | f(links) | f(rechts) | Minimum | Maximum | U-Beitrag | O-Beitrag |
|---|---|---|---|---|---|---|---|
| 1 | [0; 1,5] | 1,80 | 3,75 | 1,80 | 3,75 | 2,700 | 5,625 |
| 2 | [1,5; 3,0] | 3,75 | 4,80 | 3,75 | 4,80 | 5,625 | 7,200 |
| 3 | [3,0; 4,5] | 4,80 | 4,95 | 4,80 | **5,00** (Scheitel!) | 7,200 | 7,500 |
| 4 | [4,5; 6,0] | 4,95 | 4,20 | 4,20 | 4,95 | 6,300 | 7,425 |

U₄ = 2,700 + 5,625 + 7,200 + 6,300 = **21,825 m³**
O₄ = 5,625 + 7,200 + 7,500 + 7,425 = **27,750 m³**
O₄ − U₄ = **5,925 m³**; Grenzwert I(6) = **25,2 m³**; Bestand V(6) = 12 + 25,2 = **37,2 m³**.
Streifen 3 ist der Grund, warum der Bauagent den Scheitel gesondert behandeln muss: das Maximum
liegt dort **im Inneren** des Streifens, nicht am Rand.

**K8 — Konvergenz bei b = 6,0 h (für Beobachtungsauftrag und sim1)**
| n | Δt | U_n | O_n | O_n − U_n | Quotient zum vorigen |
|---|---|---|---|---|---|
| 1 | 6,000 | 10,800 | 30,000 | 19,200 | — |
| 2 | 3,000 | 18,000 | 29,400 | 11,400 | 1,68 |
| 4 | 1,500 | 21,825 | 27,750 | 5,925 | 1,92 |
| 8 | 0,750 | 23,597 | 26,588 | 2,991 | 1,981 |
| 12 | 0,500 | 24,150 | 26,150 | 2,000 | — |
| 16 | 0,375 | 24,423 | 25,922 | 1,499 | 1,995 |
| 32 | 0,1875 | 24,818 | 25,568 | 0,750 | 1,999 |
| 40 | 0,150 | 24,896 | 25,496 | 0,600 | — |

Beim Verdoppeln von n **halbiert** sich die Differenz (Quotienten 1,981 · 1,995 · 1,999 → 2).

**K9 — Rekonstruktionsband im Bestandsdiagramm, b = 6,0 h, n = 4, V₀ = 12 m³**
| t | untere Linie V_u | obere Linie V_o | Bandbreite |
|---|---|---|---|
| 0,0 | 12,000 | 12,000 | 0,000 |
| 1,5 | 14,700 | 17,625 | 2,925 |
| 3,0 | 20,325 | 24,825 | 4,500 |
| 4,5 | 27,525 | 32,325 | 4,800 |
| 6,0 | 33,825 | 39,750 | 5,925 |

Die Bandbreite bei t = b ist genau O₄ − U₄ = 5,925 m³ ✓.

**K10 — Vorzeichen: b = 9,0 h gegenüber b = 12,0 h (für sim2 und a6)**
b = 9,0, n = 12, Δt = 0,75: U = 29,166 · O = 35,306 · Grenzwert I(9) = **32,4 m³** · V = 44,4 m³.
b = 12,0, n = 12, Δt = 1,00: U = 13,200 · O = 29,200 · Grenzwert I(12) = **21,6 m³** · V = 33,6 m³.
Änderung zwischen t = 9 und t = 12: I(12) − I(9) = 21,6 − 32,4 = **−10,8 m³**.
Insgesamt bewegte Wassermenge (Beträge): 32,4 + 10,8 = **43,2 m³**.

**K11 — Aufgabe a2/a3, q(t) = 0,5 t² + 1 auf [0; 4], q monoton wachsend**
q(0) = 1,0 · q(1) = 1,5 · q(2) = 3,0 · q(3) = 5,5 · q(4) = 9,0.
n = 4, Δt = 1 h: U₄ = 1·(1,0 + 1,5 + 3,0 + 5,5) = **11,0 m³** = 11 000 L;
O₄ = 1·(1,5 + 3,0 + 5,5 + 9,0) = **19,0 m³**; O₄ − U₄ = **8,0 m³** = Δt·(q(4) − q(0)) = 1·8 ✓.
Grenzwert (nur zur Kontrolle, nicht Lösungsweg): 0,5·4³/3 + 1·4 = 32/3 + 4 = 14,667 m³ — liegt korrekt zwischen 11 und 19.
Kleinstes n mit O_n − U_n ≤ 0,10 m³: O_n − U_n = (4/n)·8 = 32/n ≤ 0,10 ⟺ n ≥ 320, also **n = 320**.
Probe: n = 319 → 32/319 = 0,10031 > 0,10 ✗; n = 320 → 32/320 = 0,10000 ≤ 0,10 ✓ (beide direkt nachsummiert bestätigt).

**K12 — Aufgabe a5, Gegenbeispiel zum Mittelwert**
f(x) = x² auf [0; 2], n = 2, Δx = 1: U₂ = 1·(0 + 1) = **1**; O₂ = 1·(1 + 4) = **5**;
Mittelwert (U₂ + O₂)/2 = **3**; exakter Grenzwert 2³/3 = 8/3 = **2,6667**; Abweichung **1/3 ≈ 0,333**.
Halbe Schere (O₂ − U₂)/2 = 2 ≥ 0,333 — die Fehlerschranke hält, die Gleichheit gilt nicht.
Kontrolle n = 4: U₄ = 1,75; O₄ = 3,75; Mittel = 2,75; Abweichung 0,0833 — kleiner, aber immer noch ≠ 0.

**K13 — Aufgabe a7, wann O_n − U_n = Δx·(f(b) − f(a)) gilt**
Monotoner Fall (b = 3,0, f auf [0; 3] streng wachsend):
n = 2 → O−U = 4,500 = Δt·(f(3) − f(0)) = 1,5·3,0 ✓
n = 4 → 2,250 = 0,75·3,0 ✓ · n = 6 → 1,500 ✓ · n = 8 → 1,125 ✓
Nicht monotoner Fall (b = 6,0, Scheitel t = 4 liegt innen):
n = 4 → O−U = 5,925, aber Δt·(f(6) − f(0)) = 1,5·2,4 = 3,600 ✗ (Formel unterschätzt).
Richtige Schranke: Δt · Variation mit Variation = (5,0 − 1,8) + (5,0 − 4,2) = 3,2 + 0,8 = **4,0**;
n = 4 → 1,5·4,0 = 6,000 ≥ 5,925 ✓ · n = 8 → 0,75·4,0 = 3,000 ≥ 2,991 ✓ · n = 16 → 0,375·4,0 = 1,500 ≥ 1,499 ✓.

---

## 1 · Einstieg

`<section id="einstieg">`, `.stufe`-Kopf: Nr. **1**, Überschrift **Einstieg**.

### 1.1 Aufhängertext (wörtlich)

> An einer Ladesäule steht groß die Leistung: 11 kW, 22 kW, 150 kW. Bezahlen musst du am Ende
> aber keine Kilowatt, sondern Kilowattstunden. Die Säule zeigt dir also die ganze Zeit über
> etwas anderes an, als hinterher auf der Rechnung steht — und zwischen beidem liegt genau die
> Frage, um die es in dieser Einheit geht.

> Du kennst die Änderungsrate: wie schnell geladen wird, wie schnell Wasser zuläuft, wie schnell
> sich etwas bewegt. Gesucht ist der **Bestand**: wie viel insgesamt zusammengekommen ist. Solange
> die Rate konstant bleibt, ist das eine einzige Multiplikation. Sobald sie sich laufend ändert,
> reicht das nicht mehr — und am Ende dieser Einheit steht dafür ein neuer Begriff und ein neues
> Zeichen.

### 1.2 Vorwissen prüfen

Karte `.karte` mit Überschrift „Vorwissen prüfen" und dem Vorspann:
*„Drei Fragen aus der Einführungsphase und der Sekundarstufe I. Wenn du hier hängst, lohnt sich ein
Blick zurück, bevor du weitermachst."*

Drei MC-Aufgaben ohne Rahmen (`style="border:none;padding:0"` wie im Referenzmodul).

---

**MC `vw1`** — richtige Option: Index **2**

Frage: *In einem Regenrückhaltebecken stehen bei <span class="m" data-tex="t = 2\,\mathrm{h}" data-plain="t = 2 h"></span> genau 30 m³ Wasser, bei <span class="m" data-tex="t = 6\,\mathrm{h}" data-plain="t = 6 h"></span> sind es 54 m³. Wie groß war die mittlere Zuflussrate in diesem Zeitraum?*

| Index | Option (Anzeigetext) |
|---|---|
| 0 | 24 m³/h |
| 1 | 9 m³/h |
| 2 | 6 m³/h |

Feedback:
- 0: „Du hast nur die Bestandsdifferenz 54 − 30 = 24 gebildet und nicht durch die Zeitspanne geteilt. Das Ergebnis wäre dann eine Wassermenge in m³, keine Rate in m³/h — die Einheit verrät den Fehler."
- 1: „54 geteilt durch 6 — du hast den Endbestand durch die Endzeit geteilt. Das wäre nur richtig, wenn das Becken bei t = 0 leer gewesen wäre und die Rate die ganze Zeit konstant. Gefragt ist die mittlere Rate im Intervall von 2 h bis 6 h."
- 2: „Richtig. Der Differenzenquotient ist (54 m³ − 30 m³)/(6 h − 2 h) = 24 m³ / 4 h = 6 m³/h."

---

**MC `vw2`** — richtige Option: Index **1**

Frage: *<span class="m" data-tex="V(t)" data-plain="V(t)"></span> gibt den Wasserbestand in m³ an, <span class="m" data-tex="t" data-plain="t"></span> die Zeit in Stunden. Welche Einheit hat dann <span class="m" data-tex="V'(t)" data-plain="V′(t)"></span>?*

| Index | Option |
|---|---|
| 0 | m³ · h |
| 1 | m³/h |
| 2 | m³ |

Feedback:
- 0: „Du hast multipliziert statt dividiert. Die Ableitung ist der Grenzwert von Differenzenquotienten ΔV/Δt — dort steht die Zeit im Nenner, also wird durch Stunden geteilt."
- 1: „Richtig. Die Ableitung des Bestands ist die Änderungsrate: Volumen pro Zeit, hier m³ pro Stunde."
- 2: „m³ ist die Einheit des Bestands selbst. Die Ableitung misst aber nicht, wie viel drin ist, sondern wie schnell sich das ändert — dafür braucht es die Zeit im Nenner."

---

**MC `vw3`** — richtige Option: Index **2**

Frage: *Ein Fahrzeug fährt 20 Minuten lang mit konstant 15 m/s. Was entspricht im <span class="m" data-tex="v\text{-}t" data-plain="v-t"></span>-Diagramm dem zurückgelegten Weg?*

| Index | Option |
|---|---|
| 0 | Die Steigung des Graphen. |
| 1 | Der Funktionswert bei <span class="m" data-tex="t = 20\,\mathrm{min}" data-plain="t = 20 min"></span>. |
| 2 | Der Inhalt des Rechtecks zwischen Graph und <span class="m" data-tex="t" data-plain="t"></span>-Achse. |

Feedback:
- 0: „Die Steigung im v-t-Diagramm ist die Beschleunigung. Bei konstanter Geschwindigkeit ist sie null — der zurückgelegte Weg ist aber ganz sicher nicht null."
- 1: „Der Funktionswert ist die Geschwindigkeit selbst, also 15 m/s. Eine Geschwindigkeit ist kein Weg; es fehlt die Multiplikation mit der Zeitspanne."
- 2: „Richtig. s = v · Δt = 15 m/s · 1200 s = 18 000 m = 18 km — und genau das ist der Inhalt des Rechtecks mit Höhe 15 und Breite 1200. Dieses Rechteck ist der Ausgangspunkt der ganzen Einheit."

## 2 · Erklärteil

`<section id="rekonstruktion">`, `.stufe`-Kopf: Nr. **2**, Überschrift **Vom Bestand zur Rate — und zurück**.

### 2.1 Konstante Rate: eine Multiplikation

Text (wörtlich):

> In der bisherigen Analysis bist du immer in dieselbe Richtung gelaufen: Gegeben war ein Bestand
> <span class="m" data-tex="V(t)" data-plain="V(t)"></span>, gesucht war seine Änderungsrate
> <span class="m" data-tex="V'(t)" data-plain="V′(t)"></span>. Jetzt drehst du die Richtung um.
> Gegeben ist die Rate, gesucht ist der Bestand. Diesen Vorgang nennt man **Rekonstruktion**.

> Beim Laden eines E-Autos ist die Rate die Ladeleistung
> <span class="m" data-tex="P" data-plain="P"></span>, der Bestand die geladene Energie
> <span class="m" data-tex="E" data-plain="E"></span>. Solange die Leistung konstant bleibt, ist
> die Sache einfach:

Blockformel:
`data-tex="E = P \cdot \Delta t"` · `data-plain="E = P · Δt"`

> Ein Ladevorgang mit 11 kW über 1,5 Stunden liefert also
> <span class="m" data-tex="11\,\mathrm{kW}\cdot 1{,}5\,\mathrm{h} = 16{,}5\,\mathrm{kWh}" data-plain="11 kW · 1,5 h = 16,5 kWh"></span>.
> Im <span class="m" data-tex="P\text{-}t" data-plain="P-t"></span>-Diagramm ist das der Inhalt eines
> Rechtecks mit der Höhe 11 und der Breite 1,5. Merk dir diese Übersetzung, sie trägt die gesamte
> Einheit: **Rate mal Zeit ist ein Rechteckinhalt, und dieser Rechteckinhalt ist der Zuwachs des Bestands.**

`.hinweis`-Kasten:
> **Achte auf die Einheiten.** Das „Rechteck" im Ratendiagramm hat keine Flächeneinheit im
> geometrischen Sinn. Seine Höhe wird in kW gemessen, seine Breite in h — das Produkt ist eine
> Energie in kWh. Beim Wasserbecken: m³/h mal h ergibt m³. Die Einheit des Ergebnisses ist immer
> das Produkt der beiden Achseneinheiten, nie „Kästchen".

### 2.2 Stückweise konstante Rate: die Produktsumme

Text (wörtlich):

> In Wirklichkeit lädt kaum ein Auto durchgehend mit voller Leistung. Realistischer ist eine Rate,
> die in Stufen springt. Genau so verhält sich auch der Zufluss in ein Regenrückhaltebecken
> während eines Gewitters, wenn man ihn stündlich mittelt.

> Betrachte ein Becken, in das über sechs Stunden hinweg Wasser läuft. Die Zuflussrate
> <span class="m" data-tex="f" data-plain="f"></span> ist auf jedem Abschnitt konstant, springt
> aber an den Abschnittsgrenzen:

Tabelle (in `<div class="tabelle">` einwickeln!):

| Zeitabschnitt | Dauer <span class="m" data-tex="\Delta t_k" data-plain="Δt_k"></span> | Rate <span class="m" data-tex="f_k" data-plain="f_k"></span> | Beitrag <span class="m" data-tex="f_k\cdot\Delta t_k" data-plain="f_k · Δt_k"></span> |
|---|---|---|---|
| 0 h bis 2 h | 2 h | 2,0 m³/h | 4,0 m³ |
| 2 h bis 3 h | 1 h | 3,5 m³/h | 3,5 m³ |
| 3 h bis 5 h | 2 h | 4,5 m³/h | 9,0 m³ |
| 5 h bis 6 h | 1 h | 2,5 m³/h | 2,5 m³ |
| **gesamt** | **6 h** | — | **19,0 m³** |

> Jeder Abschnitt liefert für sich ein Rechteck, und die Rechtecke werden addiert. Man nennt eine
> solche Summe eine **Produktsumme**:

Blockformel:
`data-tex="\Delta V = \sum_{k=1}^{n} f_k \cdot \Delta t_k"` · `data-plain="ΔV = Σ (k=1 bis n) f_k · Δt_k"`

> Beachte, dass die Abschnitte hier **unterschiedlich breit** sind. Es wird also nicht einfach die
> Summe der Raten gebildet und am Ende mit einer Zeit multipliziert — jede Rate wird mit *ihrer
> eigenen* Dauer gewichtet. Wer das übersieht, rechnet hier 2,0 + 3,5 + 4,5 + 2,5 = 12,5 und liegt
> um mehr als ein Drittel daneben.

> Ein Nebenprodukt: Teilt man den Gesamtzuwachs wieder durch die Gesamtdauer, erhält man die
> mittlere Rate <span class="m" data-tex="\bar f = \frac{19{,}0\,\mathrm{m^3}}{6\,\mathrm{h}} \approx 3{,}17\,\frac{\mathrm{m^3}}{\mathrm{h}}" data-plain="f̄ = 19,0 m³ / 6 h ≈ 3,17 m³/h"></span>.
> Ein Becken mit dieser konstanten Rate hätte in denselben sechs Stunden exakt dieselbe Menge
> aufgenommen.

`.merksatz`:
> **Kernaussage**
> Eine Änderungsrate rekonstruierst du zum Bestand, indem du auf jedem Abschnitt Rate mal Dauer
> rechnest und alle Beiträge aufsummierst. Der Bestand selbst ergibt sich erst, wenn du den
> Anfangsbestand dazuzählst: <span class="m" data-tex="V(b) = V(a) + \Delta V" data-plain="V(b) = V(a) + ΔV"></span>.

### 2.3 Beliebig veränderliche Rate: Streifen mit Fehlerkontrolle

Text (wörtlich):

> Jetzt der eigentliche Schritt. Was, wenn die Rate sich in jedem Augenblick ändert — wenn sie
> also durch eine glatte Funktion <span class="m" data-tex="f" data-plain="f"></span> beschrieben
> wird und auf keinem noch so kleinen Abschnitt konstant ist?

> Die Idee ist, so zu tun, *als ob*. Zerlege das Intervall
> <span class="m" data-tex="[a;b]" data-plain="[a; b]"></span> in
> <span class="m" data-tex="n" data-plain="n"></span> gleich breite Streifen der Breite

Blockformel:
`data-tex="\Delta x = \frac{b-a}{n}, \qquad x_k = a + k\cdot\Delta x \quad (k = 0,1,\dots,n)"` ·
`data-plain="Δx = (b − a)/n,   x_k = a + k · Δx   (k = 0, 1, …, n)"`

> und ersetze die Rate auf jedem Streifen durch eine Konstante. Damit du weißt, wie weit du
> danebenliegen kannst, machst du das **zweimal**: einmal so klein wie irgend möglich und einmal so
> groß wie irgend möglich.

Blockformel (Definition):
`data-tex="U_n = \sum_{k=1}^{n} m_k \cdot \Delta x, \qquad O_n = \sum_{k=1}^{n} M_k \cdot \Delta x"` ·
`data-plain="U_n = Σ m_k · Δx     O_n = Σ M_k · Δx"`

> Dabei ist <span class="m" data-tex="m_k" data-plain="m_k"></span> der **kleinste** und
> <span class="m" data-tex="M_k" data-plain="M_k"></span> der **größte** Funktionswert, den
> <span class="m" data-tex="f" data-plain="f"></span> auf dem <span class="m" data-tex="k" data-plain="k"></span>-ten
> Streifen annimmt. <span class="m" data-tex="U_n" data-plain="U_n"></span> heißt **Untersumme**,
> <span class="m" data-tex="O_n" data-plain="O_n"></span> **Obersumme**.

> Weil die echte Rate auf jedem Streifen zwischen
> <span class="m" data-tex="m_k" data-plain="m_k"></span> und
> <span class="m" data-tex="M_k" data-plain="M_k"></span> liegt, liegt der echte Zuwachs zwischen
> den beiden Summen. Du kennst den gesuchten Wert also nicht — aber du kennst ein Intervall, in dem
> er sicher liegt:

Blockformel:
`data-tex="U_n \;\le\; \Delta V \;\le\; O_n"` · `data-plain="U_n ≤ ΔV ≤ O_n"`

`.hinweis`-Kasten (**typische Fehlvorstellung, gezielt benennen**):
> **Häufiger Fehler.** „Untersumme heißt: linker Randwert, Obersumme heißt: rechter Randwert."
> Das stimmt **nur bei monoton wachsenden** Funktionen. Gefordert sind Minimum und Maximum *auf
> dem ganzen Streifen*. Liegt ein Hoch- oder Tiefpunkt mitten im Streifen, wird der zugehörige
> Wert weder links noch rechts angenommen — du musst ihn dort suchen, wo er wirklich ist. In der
> Simulation weiter unten passiert genau das, und du kannst es beobachten.

### 2.4 Rechenbeispiel: <span class="m" data-tex="f(x) = x^2" data-plain="f(x) = x²"></span> auf [0; 3]

Text (wörtlich):

> Rechne das einmal von Hand durch, an einer Funktion, bei der du jeden Schritt kontrollieren
> kannst. Nimm <span class="m" data-tex="f(x) = x^2" data-plain="f(x) = x²"></span> auf dem
> Intervall <span class="m" data-tex="[0;3]" data-plain="[0; 3]"></span>. Die Funktion wächst dort
> streng monoton, also liegt das Minimum jedes Streifens am linken und das Maximum am rechten Rand.

> Mit <span class="m" data-tex="n = 3" data-plain="n = 3"></span> ist
> <span class="m" data-tex="\Delta x = 1" data-plain="Δx = 1"></span>:

Blockformel:
`data-tex="U_3 = 1\cdot(0^2 + 1^2 + 2^2) = 5, \qquad O_3 = 1\cdot(1^2 + 2^2 + 3^2) = 14"` ·
`data-plain="U₃ = 1·(0² + 1² + 2²) = 5     O₃ = 1·(1² + 2² + 3²) = 14"`

> Das Ergebnis liegt also irgendwo zwischen 5 und 14 — eine ziemlich schlappe Aussage. Verdopple
> die Streifenzahl auf <span class="m" data-tex="n = 6" data-plain="n = 6"></span>, dann ist
> <span class="m" data-tex="\Delta x = 0{,}5" data-plain="Δx = 0,5"></span>:

Blockformel:
`data-tex="U_6 = 0{,}5\cdot 13{,}75 = 6{,}875, \qquad O_6 = 0{,}5\cdot 22{,}75 = 11{,}375"` ·
`data-plain="U₆ = 0,5 · 13,75 = 6,875     O₆ = 0,5 · 22,75 = 11,375"`

(Bauagent: Zwischenwerte für den Fließtext —
<span class="m" data-tex="U_6" data-plain="U₆"></span>-Klammer
`0 + 0{,}25 + 1 + 2{,}25 + 4 + 6{,}25 = 13{,}75`,
<span class="m" data-tex="O_6" data-plain="O₆"></span>-Klammer
`0{,}25 + 1 + 2{,}25 + 4 + 6{,}25 + 9 = 22{,}75`.)

> Die Schere hat sich von 9 auf 4,5 geschlossen, also genau halbiert. Das ist kein Zufall:

Blockformel:
`data-tex="O_n - U_n = \Delta x \cdot \big(f(b) - f(a)\big) \quad \text{(nur für monotone } f\text{)}"` ·
`data-plain="O_n − U_n = Δx · (f(b) − f(a))   (nur für monotone f)"`

> Bei monotonem <span class="m" data-tex="f" data-plain="f"></span> heben sich beim Subtrahieren
> alle inneren Terme weg — es bleibt der erste und der letzte übrig. Für
> <span class="m" data-tex="f(x)=x^2" data-plain="f(x) = x²"></span> auf
> <span class="m" data-tex="[0;3]" data-plain="[0; 3]"></span> heißt das
> <span class="m" data-tex="O_n - U_n = \frac{3}{n}\cdot 9 = \frac{27}{n}" data-plain="O_n − U_n = (3/n)·9 = 27/n"></span>,
> und dieser Ausdruck lässt sich durch Wahl von <span class="m" data-tex="n" data-plain="n"></span>
> **beliebig klein** machen. Bei <span class="m" data-tex="n = 100" data-plain="n = 100"></span>
> ist die Schere schon auf 0,27 zusammengeschrumpft
> (<span class="m" data-tex="U_{100} = 8{,}86545" data-plain="U₁₀₀ = 8,86545"></span>,
> <span class="m" data-tex="O_{100} = 9{,}13545" data-plain="O₁₀₀ = 9,13545"></span>).

`.merksatz`:
> **Kernaussage**
> Unter- und Obersumme geben dir nicht nur eine Näherung, sondern eine **garantierte Einschachtelung**
> mit einem berechenbaren Fehler. Ihre Differenz ist die Genauigkeit, die du in der Hand hast:
> Du kannst <span class="m" data-tex="n" data-plain="n"></span> so wählen, dass sie jede vorgegebene
> Schranke unterschreitet.

## 3 · Vertiefung

`<section id="grenzwert">`, `.stufe`-Kopf: Nr. **3**, Überschrift **Der Grenzübergang und das bestimmte Integral**.

### 3.1 Der Grenzwert

Text (wörtlich):

> Bisher hast du für jedes einzelne <span class="m" data-tex="n" data-plain="n"></span> zwei Zahlen
> ausgerechnet und festgestellt, dass sie sich annähern. Das ist noch keine Definition. Für eine
> Definition brauchst du die Aussage, dass beide Folgen gegen **denselben** Wert streben — und den
> musst du bestimmen können, ohne zu raten.

`<details>` mit `<summary>`: *Herleitung: <span class="m" data-tex="U_n" data-plain="U_n"></span> und <span class="m" data-tex="O_n" data-plain="O_n"></span> für <span class="m" data-tex="f(x)=x^2" data-plain="f(x) = x²"></span> auf [0; 3] in geschlossener Form*

Inhalt des Details-Blocks (wörtlich, Formeln als `.m`-Elemente):

> Mit <span class="m" data-tex="\Delta x = \frac{3}{n}" data-plain="Δx = 3/n"></span> und
> <span class="m" data-tex="x_k = k\cdot\frac{3}{n}" data-plain="x_k = k · 3/n"></span> ist die
> Untersumme (linke Randwerte, weil <span class="m" data-tex="f" data-plain="f"></span> wächst):

Blockformel:
`data-tex="U_n = \sum_{k=0}^{n-1} \left(\frac{3k}{n}\right)^{2}\cdot\frac{3}{n} = \frac{27}{n^{3}}\sum_{k=0}^{n-1} k^{2}"` ·
`data-plain="U_n = Σ (k=0..n−1) (3k/n)² · (3/n) = (27/n³) · Σ (k=0..n−1) k²"`

> Für die Summe der Quadratzahlen gibt es eine geschlossene Formel, die du mit vollständiger
> Induktion beweisen kannst:

Blockformel:
`data-tex="\sum_{k=1}^{m} k^{2} = \frac{m(m+1)(2m+1)}{6}"` ·
`data-plain="Σ (k=1..m) k² = m·(m+1)·(2m+1)/6"`

> Eingesetzt mit <span class="m" data-tex="m = n-1" data-plain="m = n − 1"></span>:

Blockformel:
`data-tex="U_n = \frac{27}{n^{3}}\cdot\frac{(n-1)\,n\,(2n-1)}{6} = \frac{9}{2}\cdot\frac{2n^{2}-3n+1}{n^{2}} = 9 - \frac{13{,}5}{n} + \frac{4{,}5}{n^{2}}"` ·
`data-plain="U_n = (27/n³) · (n−1)·n·(2n−1)/6 = (9/2)·(2n² − 3n + 1)/n² = 9 − 13,5/n + 4,5/n²"`

> Für die Obersumme läuft dieselbe Rechnung mit
> <span class="m" data-tex="k = 1,\dots,n" data-plain="k = 1, …, n"></span>, also mit
> <span class="m" data-tex="m = n" data-plain="m = n"></span>:

Blockformel:
`data-tex="O_n = \frac{27}{n^{3}}\cdot\frac{n(n+1)(2n+1)}{6} = 9 + \frac{13{,}5}{n} + \frac{4{,}5}{n^{2}}"` ·
`data-plain="O_n = (27/n³) · n·(n+1)·(2n+1)/6 = 9 + 13,5/n + 4,5/n²"`

> Probe mit den von Hand gerechneten Werten:
> <span class="m" data-tex="n=3" data-plain="n = 3"></span> liefert
> <span class="m" data-tex="9 - 4{,}5 + 0{,}5 = 5" data-plain="9 − 4,5 + 0,5 = 5"></span> und
> <span class="m" data-tex="9 + 4{,}5 + 0{,}5 = 14" data-plain="9 + 4,5 + 0,5 = 14"></span>;
> <span class="m" data-tex="n=6" data-plain="n = 6"></span> liefert 6,875 und 11,375. Beides stimmt
> mit Abschnitt 2 überein.

> Jetzt der Grenzübergang: die Terme mit <span class="m" data-tex="n" data-plain="n"></span> im
> Nenner verschwinden.

Blockformel:
`data-tex="\lim_{n\to\infty} U_n = 9 = \lim_{n\to\infty} O_n"` ·
`data-plain="lim (n→∞) U_n = 9 = lim (n→∞) O_n"`

> Beide Folgen streben gegen dieselbe Zahl 9. Da der gesuchte Wert für jedes
> <span class="m" data-tex="n" data-plain="n"></span> zwischen ihnen eingeschlossen ist, bleibt ihm
> nichts anderes übrig, als selbst 9 zu sein.

Ende des `<details>`-Blocks.

Weiter im Fließtext:

> Was hier an einem Beispiel gelingt, ist allgemein möglich: Ist
> <span class="m" data-tex="f" data-plain="f"></span> auf
> <span class="m" data-tex="[a;b]" data-plain="[a; b]"></span> stetig, so streben Unter- und
> Obersumme für <span class="m" data-tex="n\to\infty" data-plain="n → ∞"></span> gegen denselben
> Grenzwert. Man nennt <span class="m" data-tex="f" data-plain="f"></span> dann **integrierbar**
> über <span class="m" data-tex="[a;b]" data-plain="[a; b]"></span>. Dieser gemeinsame Grenzwert
> bekommt einen eigenen Namen und ein eigenes Zeichen.

### 3.2 Das bestimmte Integral

Blockformel (Definition):
`data-tex="\int_{a}^{b} f(x)\,\mathrm{d}x \;:=\; \lim_{n\to\infty} U_n \;=\; \lim_{n\to\infty} O_n"` ·
`data-plain="∫ von a bis b f(x) dx  :=  lim (n→∞) U_n = lim (n→∞) O_n"`

Text (wörtlich):

> Gelesen wird das als „Integral von <span class="m" data-tex="a" data-plain="a"></span> bis
> <span class="m" data-tex="b" data-plain="b"></span> über
> <span class="m" data-tex="f(x)" data-plain="f(x)"></span>
> <span class="m" data-tex="\mathrm{d}x" data-plain="dx"></span>". Die Bezeichnungen:

Tabelle (in `<div class="tabelle">`):

| Bestandteil | Name | Bedeutung |
|---|---|---|
| <span class="m" data-tex="\int" data-plain="∫"></span> | Integralzeichen | ein zu einem langen S gezogenes „Summe" — die Produktsumme steckt noch drin |
| <span class="m" data-tex="a,\;b" data-plain="a, b"></span> | untere und obere Integrationsgrenze | der Bereich, über den rekonstruiert wird |
| <span class="m" data-tex="f(x)" data-plain="f(x)"></span> | Integrand | die Änderungsrate |
| <span class="m" data-tex="\mathrm{d}x" data-plain="dx"></span> | Differential | das, was aus <span class="m" data-tex="\Delta x" data-plain="Δx"></span> im Grenzfall wird — die Integrationsvariable steht darin |

> Damit lässt sich das Ergebnis aus Abschnitt 2 in einer Zeile aufschreiben:
> <span class="m" data-tex="\int_{0}^{3} x^{2}\,\mathrm{d}x = 9" data-plain="∫ von 0 bis 3 x² dx = 9"></span>.

> Und die Rekonstruktion, mit der alles anfing, sieht so aus:

Blockformel:
`data-tex="V(b) = V(a) + \int_{a}^{b} f(t)\,\mathrm{d}t"` ·
`data-plain="V(b) = V(a) + ∫ von a bis b f(t) dt"`

`.merksatz`:
> **Kernaussage**
> Das bestimmte Integral ist kein neues Rechenverfahren, sondern ein **Name für einen Grenzwert**.
> Was du damit erhältst, ist der Zuwachs des Bestands im Intervall — nicht der Bestand selbst.
> Den Anfangsbestand liefert das Integral nicht mit; er muss aus der Aufgabe kommen.

### 3.3 Vorzeichen: der orientierte Flächeninhalt

Text (wörtlich):

> Bis hierher war die Rate immer positiv. Was passiert, wenn sie negativ wird — wenn also mehr
> abfließt als zufließt?

> An der Definition ändert sich kein Zeichen. Auf einem Streifen mit negativer Rate sind
> <span class="m" data-tex="m_k" data-plain="m_k"></span> und
> <span class="m" data-tex="M_k" data-plain="M_k"></span> beide negativ, das Produkt
> <span class="m" data-tex="m_k\cdot\Delta x" data-plain="m_k · Δx"></span> ist negativ, und der
> Streifen zieht von der Summe ab. Sachlich ist das genau richtig: Bei negativer Zuflussrate
> **sinkt** der Bestand.

> Deshalb heißt das, was das Integral misst, **orientierter Flächeninhalt**. Flächenstücke über der
> <span class="m" data-tex="x" data-plain="x"></span>-Achse zählen positiv, Flächenstücke darunter
> negativ. Ein Integral kann null sein, obwohl die Rate nicht durchgehend null ist — dann heben
> sich Zufluss und Abfluss über das Intervall genau auf. Damit das geschehen kann, muss die Rate
> ihr Vorzeichen wechseln; sie hat dann nach dem Zwischenwertsatz mindestens eine Nullstelle.
> Genau an solchen Nullstellen zerlegst du später das Intervall.

`.hinweis`-Kasten (**zweite typische Fehlvorstellung**):
> **Häufiger Fehler.** „Das Integral ist der Flächeninhalt unter dem Graphen." Zwei Dinge stimmen
> daran nicht. Erstens ist es der *orientierte* Inhalt, negative Anteile werden abgezogen. Zweitens
> ist „Fläche" hier nur ein Bild: Was du wirklich berechnest, ist eine rekonstruierte Menge in m³
> oder kWh. Wer nach der *insgesamt geflossenen* Wassermenge gefragt wird, darf deshalb nicht
> einfach <span class="m" data-tex="\int_a^b f" data-plain="∫ f"></span> hinschreiben, sondern muss
> an den Nullstellen der Rate zerlegen und die Beträge addieren.

> Zwei Rechenregeln, die unmittelbar aus der Definition folgen und die du im Umgang mit Vorzeichen
> ständig brauchst:

Blockformel:
`data-tex="\int_{a}^{a} f(x)\,\mathrm{d}x = 0 \qquad\text{und}\qquad \int_{a}^{c} f(x)\,\mathrm{d}x = \int_{a}^{b} f(x)\,\mathrm{d}x + \int_{b}^{c} f(x)\,\mathrm{d}x"` ·
`data-plain="∫ von a bis a f(x) dx = 0     und     ∫ von a bis c = ∫ von a bis b + ∫ von b bis c"`

> Die zweite Regel (**Intervalladditivität**) ist der Schlüssel zur Zerlegung an Nullstellen: Du
> zerschneidest das Intervall dort, wo die Rate ihr Vorzeichen wechselt, und behandelst die Stücke
> einzeln.

### 3.4 Ausblick

`.hinweis`-Kasten:
> **Wohin das führt.** Du hast jetzt einen Begriff, aber noch kein bequemes Rechenverfahren — bisher
> musst du für jedes Integral Summenformeln aufstellen und Grenzwerte bilden. Dass es dafür eine
> Abkürzung gibt, und zwar ausgerechnet über die Umkehrung des Ableitens, ist der Inhalt des
> **Hauptsatzes der Differential- und Integralrechnung**. Der kommt als eigenes Thema. In dieser
> Einheit löst du bewusst alles über Produktsummen, Ober- und Untersummen und geometrische
> Zerlegung — nur so wird nachher klar, welches Problem der Hauptsatz eigentlich löst.

## 4 · Interaktiver Kern

`<section id="simulation">`, `.stufe`-Kopf: Nr. **4**, Überschrift **Streifen schieben: die Schere schließt sich**.

Kontrollskript für alles in diesem Abschnitt: `scratchpad/vorarbeit/mathe/kontrolle_sim.py`.
Jede Zahl unten ist damit nachgerechnet.

### 4.0 Warnhinweis an den Bauagenten (zuerst lesen)

1. **Die Funktion ist auf dem Intervall nicht monoton.** Der Scheitel liegt bei
   <span class="m" data-tex="t = 4{,}0\,\mathrm{h}" data-plain="t = 4,0 h"></span>. Wer je Streifen
   einfach den linken Wert als Minimum und den rechten als Maximum nimmt, baut die Simulation
   **falsch**. Der Testfall dafür steht in 4.4.
2. **Der Grenzwert wird intern über die Stammfunktion berechnet, aber nirgends als Verfahren
   gezeigt.** Der Hauptsatz ist in diesem Modul noch nicht eingeführt. Im Skript steht
   <span class="m" data-tex="I(b)" data-plain="I(b)"></span> als Kommentar
   „Vergleichswert, im Modul noch nicht herleitbar"; in der Anzeige heißt das Feld
   **„Grenzwert (exakt)"** und im Fließtext wird gesagt, dass er hier vorweggenommen ist.
   Kein Text auf der Seite darf `∫ f = F(b) − F(a)` behaupten.
3. Kein `requestAnimationFrame`, keine Animationsschleife. Die Darstellung ist statisch und wird
   bei jedem `input`-Ereignis der Regler komplett neu gezeichnet.

### 4.1 Kontext und Ratenfunktion

Einleitungstext (wörtlich):

> Zurück zum Regenrückhaltebecken. Bei <span class="m" data-tex="t = 0" data-plain="t = 0"></span>
> stehen <span class="m" data-tex="V_0 = 12\,\mathrm{m^3}" data-plain="V₀ = 12 m³"></span> darin. Ein
> Gewitter zieht auf, der Zufluss steigt, erreicht nach vier Stunden sein Maximum und geht dann
> zurück. Ab der neunten Stunde läuft mehr ab als zu — die Rate wird negativ. Modelliert wird das
> durch

Blockformel:
`data-tex="f(t) = -0{,}2\,t^{2} + 1{,}6\,t + 1{,}8 \qquad \text{für } 0 \le t \le 12"` ·
`data-plain="f(t) = −0,2 t² + 1,6 t + 1,8   für 0 ≤ t ≤ 12"`

> mit <span class="m" data-tex="t" data-plain="t"></span> in Stunden und
> <span class="m" data-tex="f(t)" data-plain="f(t)"></span> in
> <span class="m" data-tex="\mathrm{m^3/h}" data-plain="m³/h"></span>. Du kannst die obere Grenze
> <span class="m" data-tex="b" data-plain="b"></span> und die Streifenzahl
> <span class="m" data-tex="n" data-plain="n"></span> einstellen. Die Simulation rechnet Unter- und
> Obersumme — nicht mit Randwerten, sondern mit dem echten Minimum und Maximum auf jedem Streifen.

Festwerte für den Bauagenten:

| Größe | Wert | Bedeutung |
|---|---|---|
| Ratenfunktion | `f(t) = -0.2*t*t + 1.6*t + 1.8` | Zuflussrate in m³/h |
| Definitionsbereich | <span class="m" data-tex="0 \le t \le 12" data-plain="0 ≤ t ≤ 12"></span> | Zeit in h |
| Scheitel | `T_SCHEITEL = 4.0` | <span class="m" data-tex="f(4{,}0) = 5{,}0\,\mathrm{m^3/h}" data-plain="f(4,0) = 5,0 m³/h"></span>, Hochpunkt |
| Nullstelle im Bereich | <span class="m" data-tex="t = 9{,}0\,\mathrm{h}" data-plain="t = 9,0 h"></span> | ab hier <span class="m" data-tex="f < 0" data-plain="f < 0"></span> |
| Anfangsbestand | `V0 = 12` | in m³, für das Bestandsdiagramm |
| Wertebereich von <span class="m" data-tex="f" data-plain="f"></span> | −7,8 … 5,0 m³/h | <span class="m" data-tex="f(12) = -7{,}8" data-plain="f(12) = −7,8"></span> |

**Achsen im Ratendiagramm:** waagerecht die Zeit <span class="m" data-tex="t" data-plain="t"></span>
in Stunden (Beschriftung „t in h", Teilstriche alle 1 h, Zahlen alle 2 h), senkrecht die Zuflussrate
<span class="m" data-tex="f(t)" data-plain="f(t)"></span> in m³ pro Stunde (Beschriftung
„f(t) in m³/h", Teilstriche alle 1 m³/h, Zahlen alle 2 m³/h). Die Nulllinie wird durchgezogen
gezeichnet, nicht nur als Gitterlinie — sie trennt Zufluss von Abfluss.

### 4.2 Regler

Beide in `.regler`, `<input type="range">`, Beschriftung links, aktueller Wert rechts daneben.

| Schlüssel | Größe | Min | Max | Schrittweite | Startwert | Anzeigeformat |
|---|---|---|---|---|---|---|
| `regN` | Streifenzahl <span class="m" data-tex="n" data-plain="n"></span> | 1 | 40 | 1 | **4** | ganze Zahl |
| `regB` | obere Grenze <span class="m" data-tex="b" data-plain="b"></span> in h | 1,0 | 12,0 | 0,5 | **6,0** | eine Nachkommastelle, Komma |

Untere Grenze ist fest <span class="m" data-tex="a = 0" data-plain="a = 0"></span>.

In `.knopfleiste` zwei Knöpfe:
- **„n verdoppeln"** — setzt `n = Math.min(40, 2*n)`. Er ist didaktisch der wichtigste Knopf, weil
  der Beobachtungsauftrag genau diese Bewegung verlangt.
- **„Zurücksetzen"** — stellt <span class="m" data-tex="n = 4" data-plain="n = 4"></span> und
  <span class="m" data-tex="b = 6{,}0" data-plain="b = 6,0"></span> wieder her.

### 4.3 Rechenvorschrift für Unter- und Obersumme

Streifenbreite und Stützstellen:

Blockformel:
`data-tex="\Delta t = \frac{b-0}{n}, \qquad t_k = k\cdot\Delta t \quad (k = 0,1,\dots,n)"` ·
`data-plain="Δt = b/n,   t_k = k · Δt   (k = 0, 1, …, n)"`

Für jeden Streifen <span class="m" data-tex="[t_{k-1};\,t_k]" data-plain="[t_(k−1); t_k]"></span>
werden **Minimum** <span class="m" data-tex="m_k" data-plain="m_k"></span> und **Maximum**
<span class="m" data-tex="M_k" data-plain="M_k"></span> so bestimmt:

Blockformel:
`data-tex="m_k = \min\!\big(S_k\big), \qquad M_k = \max\!\big(S_k\big), \qquad S_k = \{\, f(t_{k-1}),\; f(t_k) \,\} \cup \{\, f(4{,}0) \;\big|\; t_{k-1} < 4{,}0 < t_k \,\}"` ·
`data-plain="m_k = min(S_k),  M_k = max(S_k)  mit  S_k = { f(t_(k−1)), f(t_k) }, ergänzt um f(4,0), falls t_(k−1) < 4,0 < t_k"`

Blockformel:
`data-tex="U_n = \sum_{k=1}^{n} m_k\cdot\Delta t, \qquad O_n = \sum_{k=1}^{n} M_k\cdot\Delta t"` ·
`data-plain="U_n = Σ (k=1..n) m_k · Δt     O_n = Σ (k=1..n) M_k · Δt"`

**Umsetzung, verbindlich (Pseudocode):**

```
KONST T_SCHEITEL = 4.0
dt = b / n
U = 0; O = 0
für k = 0 … n-1:
    tl = k*dt;  tr = (k+1)*dt
    werte = [ f(tl), f(tr) ]
    wenn tl < T_SCHEITEL und T_SCHEITEL < tr:      // echt kleiner, beidseitig!
        werte.push( f(T_SCHEITEL) )                // = 5.0
    U += Math.min(...werte) * dt
    O += Math.max(...werte) * dt
```

Drei Punkte, an denen es schiefgeht:

- **Der Vergleich muss beidseitig echt sein** (`tl < 4.0 && 4.0 < tr`). Fällt der Scheitel genau auf
  eine Streifengrenze — etwa bei <span class="m" data-tex="b = 6{,}0" data-plain="b = 6,0"></span>,
  <span class="m" data-tex="n = 3" data-plain="n = 3"></span> mit Grenzen 0, 2, 4, 6 — dann ist
  <span class="m" data-tex="f(4{,}0)" data-plain="f(4,0)"></span> bereits Randwert zweier Streifen
  und wird ohnehin erfasst. Mit `<=` würde er doppelt geprüft, was zwar nichts verfälscht, aber die
  Absicht verschleiert.
- **Minimum und Maximum werden getrennt bestimmt.** Der Scheitel ist hier ein Hochpunkt, also kann er
  nur das Maximum verändern — der Code darf sich darauf trotzdem nicht verlassen und muss beide
  Extrema aus derselben Werteliste ziehen. Nur so bleibt er richtig, wenn die Funktion später
  ausgetauscht wird.
- **Kein Abschneiden bei negativen Werten.** Für
  <span class="m" data-tex="b > 9{,}0" data-plain="b > 9,0"></span> sind
  <span class="m" data-tex="m_k" data-plain="m_k"></span> und
  <span class="m" data-tex="M_k" data-plain="M_k"></span> negativ, die Beiträge ziehen von der Summe
  ab. Kein `Math.abs`, kein `Math.max(0, …)`.

**Vergleichswert (nur intern):**
`data-tex="I(b) = -\frac{b^{3}}{15} + 0{,}8\,b^{2} + 1{,}8\,b"` ·
`data-plain="I(b) = −b³/15 + 0,8 b² + 1,8 b"` — im Code als `exakt(b)` mit dem Kommentar aus 4.0.

### 4.4 Testfall für die Umsetzung (Streifen mit Scheitel)

Der Bauagent prüft seine Implementierung an der Startkonfiguration
<span class="m" data-tex="b = 6{,}0\,\mathrm{h}" data-plain="b = 6,0 h"></span>,
<span class="m" data-tex="n = 4" data-plain="n = 4"></span>,
<span class="m" data-tex="\Delta t = 1{,}5\,\mathrm{h}" data-plain="Δt = 1,5 h"></span>:

| <span class="m" data-tex="k" data-plain="k"></span> | Streifen | <span class="m" data-tex="f(t_{k-1})" data-plain="f(links)"></span> | <span class="m" data-tex="f(t_k)" data-plain="f(rechts)"></span> | Scheitel drin? | <span class="m" data-tex="m_k" data-plain="m_k"></span> | <span class="m" data-tex="M_k" data-plain="M_k"></span> | <span class="m" data-tex="m_k\Delta t" data-plain="m_k · Δt"></span> | <span class="m" data-tex="M_k\Delta t" data-plain="M_k · Δt"></span> |
|---|---|---|---|---|---|---|---|---|
| 1 | [0,0; 1,5] | 1,80 | 3,75 | nein | 1,80 | 3,75 | 2,700 | 5,625 |
| 2 | [1,5; 3,0] | 3,75 | 4,80 | nein | 3,75 | 4,80 | 5,625 | 7,200 |
| 3 | [3,0; 4,5] | 4,80 | 4,95 | **ja** | 4,80 | **5,00** | 7,200 | **7,500** |
| 4 | [4,5; 6,0] | 4,95 | 4,20 | nein | 4,20 | 4,95 | 6,300 | 7,425 |

Der dritte Streifen ist der Prüfstein, ausgerechnet:

- <span class="m" data-tex="f(3{,}0) = -0{,}2\cdot 9 + 4{,}8 + 1{,}8 = 4{,}80" data-plain="f(3,0) = −0,2·9 + 4,8 + 1,8 = 4,80"></span>
- <span class="m" data-tex="f(4{,}5) = -0{,}2\cdot 20{,}25 + 7{,}2 + 1{,}8 = -4{,}05 + 9{,}0 = 4{,}95" data-plain="f(4,5) = −0,2·20,25 + 7,2 + 1,8 = −4,05 + 9,00 = 4,95"></span>
- <span class="m" data-tex="f(4{,}0) = -0{,}2\cdot 16 + 6{,}4 + 1{,}8 = -3{,}2 + 8{,}2 = 5{,}00" data-plain="f(4,0) = −0,2·16 + 6,4 + 1,8 = −3,20 + 8,20 = 5,00"></span>

<span class="m" data-tex="4{,}0" data-plain="4,0"></span> liegt echt zwischen 3,0 und 4,5, also ist
<span class="m" data-tex="M_3 = 5{,}00\,\mathrm{m^3/h}" data-plain="M₃ = 5,00 m³/h"></span> und der
Beitrag <span class="m" data-tex="5{,}00\cdot 1{,}5 = 7{,}500\,\mathrm{m^3}" data-plain="5,00 · 1,5 = 7,500 m³"></span>.

Ergebnisse der Startkonfiguration:

- <span class="m" data-tex="U_4 = 2{,}700 + 5{,}625 + 7{,}200 + 6{,}300 = 21{,}825\,\mathrm{m^3}" data-plain="U₄ = 2,700 + 5,625 + 7,200 + 6,300 = 21,825 m³"></span>
- <span class="m" data-tex="O_4 = 5{,}625 + 7{,}200 + 7{,}500 + 7{,}425 = 27{,}750\,\mathrm{m^3}" data-plain="O₄ = 5,625 + 7,200 + 7,500 + 7,425 = 27,750 m³"></span>
- <span class="m" data-tex="O_4 - U_4 = 5{,}925\,\mathrm{m^3}" data-plain="O₄ − U₄ = 5,925 m³"></span>
- Grenzwert <span class="m" data-tex="I(6) = 25{,}200\,\mathrm{m^3}" data-plain="I(6) = 25,200 m³"></span>,
  Bestand <span class="m" data-tex="V(6) = 12 + 25{,}2 = 37{,}200\,\mathrm{m^3}" data-plain="V(6) = 12 + 25,2 = 37,200 m³"></span>

**Abnahmekriterium:** Zeigt die fertige Simulation bei
<span class="m" data-tex="b = 6{,}0" data-plain="b = 6,0"></span>,
<span class="m" data-tex="n = 4" data-plain="n = 4"></span> die Obersumme **27,675** statt **27,750**,
dann wurde der Scheitel nicht behandelt (naives Maximum
<span class="m" data-tex="\max(4{,}80;\,4{,}95) = 4{,}95" data-plain="max(4,80; 4,95) = 4,95"></span>,
Fehlbetrag <span class="m" data-tex="0{,}075\,\mathrm{m^3}" data-plain="0,075 m³"></span>). Die
Untersumme ist in diesem Fall zufällig richtig, weil der Scheitel ein Hoch- und kein Tiefpunkt ist —
sie taugt deshalb **nicht** als Prüfgröße.

### 4.5 Zweiter Testfall (negative Rate)

<span class="m" data-tex="b = 12{,}0" data-plain="b = 12,0"></span>,
<span class="m" data-tex="n = 12" data-plain="n = 12"></span>,
<span class="m" data-tex="\Delta t = 1{,}0" data-plain="Δt = 1,0"></span>:
<span class="m" data-tex="U_{12} = 13{,}200" data-plain="U₁₂ = 13,200"></span>,
<span class="m" data-tex="O_{12} = 29{,}200" data-plain="O₁₂ = 29,200"></span>,
Grenzwert <span class="m" data-tex="I(12) = 21{,}600" data-plain="I(12) = 21,600"></span> (alles in m³).
Die Einschachtelung <span class="m" data-tex="13{,}2 \le 21{,}6 \le 29{,}2" data-plain="13,2 ≤ 21,6 ≤ 29,2"></span>
muss auch hier gelten. Tut sie es nicht, wurden negative Beiträge abgeschnitten.

### 4.6 Was gezeichnet wird

**Canvas 1 — Ratendiagramm.** `width="1000" height="490"`, per CSS `width:100%`.

Zeichenreihenfolge (von hinten nach vorn, damit nichts verdeckt wird, was gebraucht wird):

1. **Gitter** in `#e2e8f0`, 1 px: senkrecht alle 1 h, waagerecht alle 1 m³/h.
2. **Obersummen-Rechtecke** über die volle Höhe
   <span class="m" data-tex="M_k" data-plain="M_k"></span>: Füllung `rgba(217,119,6,0.18)`,
   Rand `#b45309`, 1 px. Sie werden **zuerst** gezeichnet.
3. **Untersummen-Rechtecke** der Höhe <span class="m" data-tex="m_k" data-plain="m_k"></span>
   darüber: Füllung `rgba(13,122,82,0.28)`, Rand `#0d7a52`, 1 px. Sichtbar bleibt so oben ein
   schmaler Saum in Bernstein — das ist genau die Differenz
   <span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span>, und der Beobachtungsauftrag
   verlangt, dass die Schülerinnen und Schüler ihn schrumpfen sehen.
   Ein Rechteck spannt immer zwischen der Nulllinie und dem Wert; bei negativem Wert liegt es
   **unterhalb** der Achse. Umsetzung mit
   `ctx.fillRect(x(t_links), Math.min(y(0), y(wert)), Δt·PX_PRO_H, Math.abs(y(wert) − y(0)))`.
4. **Nulllinie und Achsen** in `#334155`, 1,5 px, mit Pfeilspitzen; Teilstriche und Zahlen in
   `#475569`, 13 px. Achsentitel „t in h" rechts unter der waagerechten Achse, „f(t) in m³/h"
   über der senkrechten. Dezimaltrennzeichen ist das Komma.
5. **Graph von <span class="m" data-tex="f" data-plain="f"></span>** über den ganzen
   Definitionsbereich 0 bis 12 h, in Schritten von 0,05 h ausgewertet.
   Im markierten Bereich <span class="m" data-tex="0 \le t \le b" data-plain="0 ≤ t ≤ b"></span>:
   `#0d7a52`, 2,5 px. Außerhalb (<span class="m" data-tex="t > b" data-plain="t > b"></span>):
   `#94a3b8`, 1,5 px — so ist auf einen Blick zu sehen, welches Stück gerade rekonstruiert wird.
6. **Grenzmarke bei <span class="m" data-tex="t = b" data-plain="t = b"></span>**: senkrechte
   gestrichelte Linie `#0d7a52` (`setLineDash([5,4])`) mit der Beschriftung „b = 6,0 h" am oberen Rand.
7. **Scheitelmarke**: kleiner ausgefüllter Punkt (r = 4 px) bei
   <span class="m" data-tex="(4{,}0\,|\,5{,}0)" data-plain="(4,0 | 5,0)"></span> in `#0d7a52` mit
   dem Text „Scheitel (4,0 h | 5,0 m³/h)". Nur sichtbar, solange
   <span class="m" data-tex="b \ge 4{,}0" data-plain="b ≥ 4,0"></span>. Sie ist kein Schmuck: Sie
   zeigt, warum ein Streifen manchmal höher ist, als seine Ränder vermuten lassen.

**Canvas 2 — Bestandsdiagramm.** `width="1000" height="310"`, direkt darunter.

Zeichnet zwei Streckenzüge, die beide bei
<span class="m" data-tex="(0\,|\,12)" data-plain="(0 | 12)"></span> starten und sich stufenweise um
<span class="m" data-tex="m_k\cdot\Delta t" data-plain="m_k · Δt"></span> beziehungsweise
<span class="m" data-tex="M_k\cdot\Delta t" data-plain="M_k · Δt"></span> erhöhen. Die Fläche
zwischen ihnen wird als **Rekonstruktionsband** in `rgba(13,122,82,0.12)` gefüllt: Links ist es
null breit, rechts ist es genau
<span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span> hoch. Achsen: „t in h"
waagerecht, „V(t) in m³" senkrecht, Zahlen alle 10 m³.

Kontrollwerte für <span class="m" data-tex="b = 6{,}0" data-plain="b = 6,0"></span>,
<span class="m" data-tex="n = 4" data-plain="n = 4"></span>,
<span class="m" data-tex="V_0 = 12" data-plain="V₀ = 12"></span> (identisch mit K9):

| <span class="m" data-tex="t" data-plain="t"></span> in h | untere Linie in m³ | obere Linie in m³ | Bandbreite in m³ |
|---|---|---|---|
| 0,0 | 12,000 | 12,000 | 0,000 |
| 1,5 | 14,700 | 17,625 | 2,925 |
| 3,0 | 20,325 | 24,825 | 4,500 |
| 4,5 | 27,525 | 32,325 | 4,800 |
| 6,0 | 33,825 | 39,750 | **5,925** |

Die Bandbreite ganz rechts ist genau
<span class="m" data-tex="O_4 - U_4" data-plain="O₄ − U₄"></span> — daran erkennt der Bauagent, dass
beide Canvas dieselbe Rechnung benutzen.

### 4.7 Umrechnung Pixel ↔ Achsenwerte (dokumentierte Konstanten)

Beide Blöcke stehen als Konstanten oben in der IIFE, mit genau diesem Kommentar.

**Canvas 1, Ratendiagramm (1000 × 490):**

```js
// Zeichenfläche: x von 70 bis 970 px (900 px breit), y von 20 bis 440 px (420 px hoch).
// Links 70 px für die Achsenbeschriftung, unten 50 px für die Zeitachse.
var X_LINKS = 70, X_RECHTS = 970;      // px
var Y_OBEN  = 20, Y_UNTEN  = 440;      // px
var T_MAX   = 12.0;                    // h  – volle Achsenbreite, unabhängig von b
var F_MAX   =  6.0, F_MIN  = -8.0;     // m³/h – umschließt f(12) = -7,8
var PX_PRO_H    = (X_RECHTS - X_LINKS) / T_MAX;          // = 75 px je Stunde
var PX_PRO_RATE = (Y_UNTEN  - Y_OBEN ) / (F_MAX-F_MIN);  // = 30 px je m³/h
function x(t){ return X_LINKS + t * PX_PRO_H; }
function y(v){ return Y_OBEN + (F_MAX - v) * PX_PRO_RATE; }
```

Proben (nachgerechnet):
<span class="m" data-tex="x(0) = 70" data-plain="x(0) = 70"></span> ·
<span class="m" data-tex="x(4{,}0) = 370" data-plain="x(4,0) = 370"></span> ·
<span class="m" data-tex="x(6{,}0) = 520" data-plain="x(6,0) = 520"></span> ·
<span class="m" data-tex="x(12{,}0) = 970" data-plain="x(12,0) = 970"></span> ·
<span class="m" data-tex="y(5{,}0) = 50" data-plain="y(5,0) = 50"></span> ·
<span class="m" data-tex="y(0) = 200" data-plain="y(0) = 200"></span> ·
<span class="m" data-tex="y(-7{,}8) = 434" data-plain="y(−7,8) = 434"></span>.
Ein Streifen der Breite <span class="m" data-tex="\Delta t" data-plain="Δt"></span> ist
<span class="m" data-tex="\Delta t \cdot 75" data-plain="Δt · 75"></span> px breit; bei
<span class="m" data-tex="n = 40" data-plain="n = 40"></span> und
<span class="m" data-tex="b = 1{,}0" data-plain="b = 1,0"></span> sind das 1,875 px — Rechtecke werden
deshalb ohne Rand gezeichnet, sobald die Streifenbreite unter 3 px fällt, sonst frisst der Rand die
Füllung auf.

**Canvas 2, Bestandsdiagramm (1000 × 310):**

```js
// Gleiche x-Abbildung wie oben (X_LINKS, PX_PRO_H), damit beide Diagramme untereinander passen.
var Y_OBEN2 = 20, Y_UNTEN2 = 260;   // px  (240 px hoch)
var V_MAX   = 80.0;                 // m³  – deckt den größten möglichen Wert der oberen Linie ab
var PX_PRO_M3 = (Y_UNTEN2 - Y_OBEN2) / V_MAX;   // = 3 px je m³
function y2(v){ return Y_OBEN2 + (V_MAX - v) * PX_PRO_M3; }
```

Proben: <span class="m" data-tex="y_2(0) = 260" data-plain="y₂(0) = 260"></span> ·
<span class="m" data-tex="y_2(12) = 224" data-plain="y₂(12) = 224"></span> ·
<span class="m" data-tex="y_2(37{,}2) = 148{,}4" data-plain="y₂(37,2) = 148,4"></span> ·
<span class="m" data-tex="y_2(80) = 20" data-plain="y₂(80) = 20"></span>.
Der ungünstigste Fall im gesamten Reglerbereich ist
<span class="m" data-tex="b = 12{,}0" data-plain="b = 12,0"></span>,
<span class="m" data-tex="n = 2" data-plain="n = 2"></span>: obere Linie
<span class="m" data-tex="12 + 55{,}2 = 67{,}2\,\mathrm{m^3}" data-plain="12 + 55,2 = 67,2 m³"></span>
— liegt unter 80, die Achse muss also nie mitwachsen.

### 4.8 Anzeigefeld `.anzeige`

Sechs Werte, alle über `fmt(zahl, stellen)` mit Komma. Die ersten vier sind Pflicht, die letzten
beiden ergänzen das Bestandsdiagramm.

| Beschriftung | Wert | Nachkommastellen | Startwert (b = 6,0 · n = 4) |
|---|---|---|---|
| Streifenbreite <span class="m" data-tex="\Delta t" data-plain="Δt"></span> | `b/n`, in h | 4 | 1,5000 h |
| **Untersumme <span class="m" data-tex="U_n" data-plain="U_n"></span>** | in m³ | 3 | 21,825 m³ |
| **Obersumme <span class="m" data-tex="O_n" data-plain="O_n"></span>** | in m³ | 3 | 27,750 m³ |
| **Schere <span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span>** | in m³ | 3 | 5,925 m³ |
| **Grenzwert (exakt)** | `exakt(b)`, in m³ | 3 | 25,200 m³ |
| Bestand <span class="m" data-tex="V(b) = 12\,\mathrm{m^3} + \text{Grenzwert}" data-plain="V(b) = 12 m³ + Grenzwert"></span> | in m³ | 2 | 37,20 m³ |

Drei Nachkommastellen sind Absicht: Bei
<span class="m" data-tex="n = 32" data-plain="n = 32"></span> ist die Schere 0,750 m³, mit nur zwei
Stellen wäre die Halbierung von 1,499 auf 0,750 nicht mehr sauber ablesbar.

Die Zeile „Schere" bekommt zusätzlich einen waagerechten Balken, dessen Breite proportional zu
<span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span> ist (volle Breite bei 20 m³,
Farbe `#b45309`). Er macht die Halbierung sichtbar, bevor jemand die Zahlen vergleicht.

### 4.9 Beobachtungsauftrag (wörtlich in den `.auftrag`-Kasten)

> **Beobachtungsauftrag**
> Lass <span class="m" data-tex="b = 6{,}0\,\mathrm{h}" data-plain="b = 6,0 h"></span> fest stehen und
> beginne bei <span class="m" data-tex="n = 2" data-plain="n = 2"></span>. Notiere dir die Schere
> <span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span>. Drücke jetzt viermal
> hintereinander auf „n verdoppeln" — also <span class="m" data-tex="n = 4,\,8,\,16,\,32" data-plain="n = 4, 8, 16, 32"></span>
> — und notiere jedes Mal den neuen Wert. Teile anschließend jede Zahl durch die nächste.
> Beantworte danach schriftlich: **Um welchen Faktor fällt die Schere bei jeder Verdopplung, und
> woran liegt das?** Sieh dir für die Begründung die Rechtecke an: Was passiert beim Verdoppeln mit
> der *Breite* eines Streifens, und was passiert mit der *Höhe* des bernsteinfarbenen Saums über den
> grünen Rechtecken? Formuliere einen Satz der Form: „Beim Verdoppeln von
> <span class="m" data-tex="n" data-plain="n"></span> … , weil … ."
>
> Stell danach <span class="m" data-tex="n = 4" data-plain="n = 4"></span> wieder her und sieh dir den
> dritten Streifen genau an, den von 3,0 h bis 4,5 h. Vergleiche die Höhe seines Obersummen-Rechtecks
> mit den Funktionswerten an seinen beiden Rändern.

Erwartete Notizen (zur Kontrolle im Lehrerteil, alle nachgerechnet):

| <span class="m" data-tex="n" data-plain="n"></span> | 2 | 4 | 8 | 16 | 32 |
|---|---|---|---|---|---|
| <span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span> in m³ | 11,400 | 5,925 | 2,991 | 1,499 | 0,750 |
| Quotient zum vorigen | — | 1,924 | 1,981 | 1,995 | 1,999 |

Die Quotienten streben gegen 2. Begründung: Die Schere ist
<span class="m" data-tex="O_n - U_n = \Delta t \cdot \sum_{k=1}^{n} (M_k - m_k)" data-plain="O_n − U_n = Δt · Σ (M_k − m_k)"></span>.
Beim Verdoppeln von <span class="m" data-tex="n" data-plain="n"></span> halbiert sich
<span class="m" data-tex="\Delta t" data-plain="Δt"></span>, während die Summe der Höhenunterschiede
gegen die feste Gesamtschwankung von
<span class="m" data-tex="f" data-plain="f"></span> auf [0; 6] strebt:
<span class="m" data-tex="(5{,}0 - 1{,}8) + (5{,}0 - 4{,}2) = 4{,}0\,\mathrm{m^3/h}" data-plain="(5,0 − 1,8) + (5,0 − 4,2) = 4,0 m³/h"></span>.
Also fällt das Produkt auf die Hälfte. Kontrolle der Schranke:
<span class="m" data-tex="\Delta t\cdot 4{,}0" data-plain="Δt · 4,0"></span> ergibt bei
<span class="m" data-tex="n = 8" data-plain="n = 8"></span> den Wert 3,000 ≥ 2,991 und bei
<span class="m" data-tex="n = 16" data-plain="n = 16"></span> den Wert 1,500 ≥ 1,499 — die Schranke
hält und wird immer schärfer.

### 4.10 Verständnisfragen

Direkt unter dem Canvas-Block, beide als MC-Aufgaben mit Rahmen.

---

**MC `sim1`** — richtige Option: Index **1**

Frage: *Du hast bei <span class="m" data-tex="b = 6{,}0\,\mathrm{h}" data-plain="b = 6,0 h"></span>
die Streifenzahl mehrfach verdoppelt. Was passiert dabei mit der Schere
<span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span>, und warum?*

| Index | Option (Anzeigetext) |
|---|---|
| 0 | Sie viertelt sich, weil bei doppelter Streifenzahl sowohl die Breite als auch die Höhe der Restrechtecke halbiert werden. |
| 1 | Sie halbiert sich, weil sich die Streifenbreite halbiert, während die Summe der Höhenunterschiede <span class="m" data-tex="M_k - m_k" data-plain="M_k − m_k"></span> nahezu gleich bleibt. |
| 2 | Sie bleibt ungefähr gleich, weil doppelt so viele Streifen auch doppelt so viele Fehler beisteuern. |
| 3 | Sie fällt zuerst, bleibt aber ab <span class="m" data-tex="n = 16" data-plain="n = 16"></span> bei etwa 1,5 m³ stehen, weil der Scheitel sich nicht genauer erfassen lässt. |

Feedback:
- 0: „Du hast beide Faktoren halbiert. Halbiert wird aber nur die Breite Δt. Die Höhenunterschiede M_k − m_k werden zwar einzeln kleiner, dafür gibt es doppelt so viele davon — ihre Summe bleibt fast unverändert und strebt gegen die Gesamtschwankung 4,0 m³/h. Die Messung bestätigt das: 5,925 → 2,991 ist der Faktor 1,98, nicht 4."
- 1: „Richtig. Es gilt O_n − U_n = Δt · Σ(M_k − m_k). Beim Verdoppeln von n halbiert sich Δt, die Summe der Höhenunterschiede läuft gegen den festen Wert (5,0 − 1,8) + (5,0 − 4,2) = 4,0 m³/h. Also halbiert sich das Produkt: 11,400 → 5,925 → 2,991 → 1,499 → 0,750, Quotienten 1,924 · 1,981 · 1,995 · 1,999."
- 2: „Die Zahl der Streifen stimmt, die Schlussfolgerung nicht. Jeder einzelne Streifen wird nicht nur zusätzlich, sondern auch schmaler — und das schlägt stärker durch. Die abgelesenen Werte fallen eindeutig: von 11,400 m³ bei n = 2 auf 0,750 m³ bei n = 32."
- 3: „Genau der Scheitel ist der Punkt, den die Simulation exakt behandelt: Liegt t = 4,0 h im Inneren eines Streifens, wird f(4,0) = 5,0 m³/h als Maximum verwendet. Es bleibt also kein Sockel übrig. Bei n = 32 steht dort 0,750 m³ — die Hälfte des Werts bei n = 16."

---

**MC `sim2`** — richtige Option: Index **1**

Frage: *Stell <span class="m" data-tex="b = 6{,}0\,\mathrm{h}" data-plain="b = 6,0 h"></span> und
<span class="m" data-tex="n = 4" data-plain="n = 4"></span> ein. Der dritte Streifen reicht von
3,0 h bis 4,5 h; dort ist
<span class="m" data-tex="f(3{,}0) = 4{,}80" data-plain="f(3,0) = 4,80"></span> und
<span class="m" data-tex="f(4{,}5) = 4{,}95" data-plain="f(4,5) = 4,95"></span>. Sein
Obersummen-Rechteck ist aber 5,00 m³/h hoch. Warum?*

| Index | Option (Anzeigetext) |
|---|---|
| 0 | Weil die Obersumme grundsätzlich den rechten Randwert nimmt und 4,95 auf 5,00 gerundet wird. |
| 1 | Weil der Scheitel <span class="m" data-tex="t = 4{,}0\,\mathrm{h}" data-plain="t = 4,0 h"></span> im Inneren dieses Streifens liegt und <span class="m" data-tex="f" data-plain="f"></span> dort ihren größten Wert 5,00 m³/h annimmt — er wird an keinem der beiden Ränder erreicht. |
| 2 | Weil jedes Obersummen-Rechteck bis zum größten Funktionswert des ganzen Intervalls reicht. |
| 3 | Weil bei nicht monotonen Funktionen der Mittelwert der beiden Randwerte verwendet wird. |

Feedback:
- 0: „Zwei Fehler auf einmal. Gerundet wird nirgends: f(4,5) = −0,2·20,25 + 7,2 + 1,8 = 4,95 ist exakt. Und der rechte Randwert ist nur bei monoton wachsendem f das Maximum — sieh dir den vierten Streifen an, dort ist f(6,0) = 4,20 der kleinste Wert, nicht der größte."
- 1: „Richtig. Gefordert ist das Maximum auf dem ganzen Streifen. Wegen 3,0 < 4,0 < 4,5 gehört f(4,0) = 5,00 m³/h dazu, und das ist mehr als beide Randwerte. Der Beitrag ist deshalb 5,00 · 1,5 = 7,500 m³ statt 4,95 · 1,5 = 7,425 m³ — genau diese 0,075 m³ unterscheiden eine richtige von einer schlampigen Obersumme."
- 2: „Dann wäre jedes Rechteck 5,00 m³/h hoch und die Obersumme 4 · 1,5 · 5,00 = 30,000 m³ — das ist der Wert für n = 1, nicht für n = 4. Angezeigt werden 27,750 m³. Minimum und Maximum werden immer nur auf dem jeweiligen Streifen gesucht; der erste Streifen kommt zum Beispiel nur auf 3,75 m³/h."
- 3: „Der Mittelwert (4,80 + 4,95)/2 = 4,875 wäre kleiner als der tatsächlich vorkommende Wert 5,00. Damit wäre die Obersumme keine obere Schranke mehr, und die Einschachtelung U_n ≤ ΔV ≤ O_n — der ganze Sinn der Konstruktion — wäre kaputt."

---

`.hinweis`-Kasten unter den beiden Fragen:

> **Was die Simulation nicht beweist.** Du hast gesehen, dass sich die Schere bei jeder Verdopplung
> halbiert, und du kannst daraus jede gewünschte Genauigkeit erreichen. Beweisen lässt sich damit
> nicht, dass beide Folgen gegen *denselben* Wert streben — dafür brauchst du die Rechnung aus
> Abschnitt 3. Das Feld „Grenzwert (exakt)" nimmt hier etwas vorweg, das du erst mit dem Hauptsatz
> selbst ausrechnen kannst.

## 5 · Übungen

`<section id="uebungen">`, `.stufe`-Kopf: Nr. **5**, Überschrift **Übungen**.

Kontrollskript für diesen Abschnitt: `scratchpad/vorarbeit/mathe/kontrolle_uebungen.py`.
Jede Zahl unten ist damit nachgerechnet; die Kontrollrechnungen stehen jeweils direkt bei der Aufgabe.

**Fachlicher Zuschnitt — verbindlich.** Dieses Modul steht *vor* dem Hauptsatz. Keine einzige
Aufgabe darf über eine Stammfunktion gelöst werden. Erlaubte Werkzeuge: Produktsumme, Unter- und
Obersumme, Zerlegung an Nullstellen, Intervalladditivität, Einheitenbetrachtung und das Ablesen des
Feldes „Grenzwert (exakt)" aus der Simulation. Wo ein Vergleichswert gebraucht wird, wird er als
*abgelesen* oder *gegeben* eingeführt, nie als gerechnet.

Vorspann der Sektion (wörtlich):

> In dieser Einheit gibt es noch keine Stammfunktionen. Jede Aufgabe hier löst du mit dem, was du
> bis hierher hast: Rate mal Dauer, Summen von Streifen, Zerlegen an den Nullstellen der Rate und
> ein wacher Blick auf die Einheiten. Wenn du irgendwo nach der einen Formel suchst, die „das
> Integral ausrechnet" — die gibt es hier absichtlich noch nicht. Genau deshalb merkst du später,
> was der Hauptsatz dir abnimmt.

**Reihenfolge auf der Seite** (die Schlüssel folgen der Nummerierung aus Abschnitt 0, die
Anordnung folgt der Schwierigkeit — beides stimmt bewusst nicht überein):

| Platz | Schlüssel | Typ | AB | Kern |
|---|---|---|---|---|
| 1 | `a1` | Zahleneingabe | I | Produktsumme aus einer Ratentabelle |
| 2 | `a2u` | Zahleneingabe | I | Untersumme <span class="m" data-tex="U_4" data-plain="U₄"></span> bei monotoner Rate |
| 3 | `a2o` | Zahleneingabe | I | Obersumme <span class="m" data-tex="O_4" data-plain="O₄"></span> und Einschachtelung |
| 4 | `a3` | Zahleneingabe | II | benötigte Streifenzahl für eine vorgegebene Genauigkeit |
| 5 | `a4` | Multiple Choice | II | Einheiten: Rate mal Zeit, gemischte Zeiteinheiten |
| 6 | `z1` | Zuordnung | II | Ratengraph → Bestandsverlauf |
| 7 | `a6` | Zahleneingabe | II | Rate mit Vorzeichenwechsel, abgeflossene Menge |
| 8 | `a5` | offen | III | Schüleraussage zum Mittelwert bewerten |
| 9 | `a7` | offen | III | Gültigkeit der Scherenformel begründen |
| 10 | `a8` | offen | III | Zuwachs und Bestand auseinanderhalten |

Hinweis an den Bauagenten: Abschnitt 0 spricht bei K11 von „Aufgabe a2/a3". Die Eingabe ist in zwei
`.aufgabe`-Blöcke aufgeteilt (`a2u` für die Unter-, `a2o` für die Obersumme), weil die Zahlen-Engine
pro Block genau ein Eingabefeld auswertet. Die Zahlen sind unverändert die aus K11.

---

### Aufgabe 1 — `a1` · Zahleneingabe · Anforderungsbereich I

Aufgabentext (wörtlich):

> Ein E-Auto wird an einer Wallbox geladen. Das Ladeprotokoll weist drei Phasen aus, in denen die
> Ladeleistung jeweils konstant war:

Tabelle (in `<div class="tabelle">`):

| Phase | Dauer | Ladeleistung |
|---|---|---|
| 1 | 1,5 h | 11,0 kW |
| 2 | 1,0 h | 7,4 kW |
| 3 | 0,5 h | 3,7 kW |

> Berechne die insgesamt geladene Energie.

**Einheitenliste im `<select>`:** `kWh` · `Wh` · `kW` · `kJ`
(`kW` ist der fachlich falsche Distraktor — eine Leistung, keine Energie.)

**Eintrag in `numDaten`:**

```js
a1:{ wert:25.75, einheit:"kWh", tol:0.05,
     alt:{wert:25750, einheit:"Wh"},
     ok:"Richtig. 11,0 kW · 1,5 h + 7,4 kW · 1,0 h + 3,7 kW · 0,5 h = 16,50 kWh + 7,40 kWh + 1,85 kWh = 25,75 kWh.",
     falschEinheit:"Der Zahlenwert stimmt. Multipliziert werden aber Kilowatt mit Stunden, und das ergibt eine Energie: 25,75 kWh oder 25 750 Wh. kW allein wäre eine Leistung — also die Rate, nicht der Bestand.",
     nah:"Du bist in der richtigen Größenordnung, hast aber vermutlich nicht jede Leistung mit ihrer eigenen Dauer gewichtet. 22,1 kWh bekommt man, wenn man die drei Leistungen addiert (22,1 kW) und pauschal mit einer Stunde multipliziert — dasselbe Ergebnis liefert die mittlere Leistung 7,3667 kW mal 3,0 h. Beide Wege übersehen, dass Phase 1 anderthalb Stunden dauert und Phase 3 nur eine halbe.",
     weit:"Rechne zuerst eine einzige Phase: 11,0 kW über 1,5 h ergeben 16,5 kWh. Danach machst du dasselbe für Phase 2 und 3 und addierst. Die Hilfen führen dich Schritt für Schritt." }
```

**Hilfen:**

1. *Tipp:* „Die Wallbox zeigt dir, wie schnell geladen wird — nicht, wie viel schon drin ist. Jede
   Phase steuert für sich etwas bei, und die Phasen sind unterschiedlich lang."
2. *Ansatz:* „Das ist eine Produktsumme:
   <span class="m" data-tex="\Delta E = \sum_k P_k \cdot \Delta t_k" data-plain="ΔE = Σ P_k · Δt_k"></span>.
   Jede Leistung wird mit *ihrer eigenen* Dauer multipliziert, erst danach wird addiert. Im
   <span class="m" data-tex="P\text{-}t" data-plain="P-t"></span>-Diagramm sind das drei Rechtecke
   nebeneinander."
3. *Lösungsweg:*
   <span class="m" data-tex="11{,}0\,\mathrm{kW}\cdot 1{,}5\,\mathrm{h} = 16{,}50\,\mathrm{kWh}" data-plain="11,0 kW · 1,5 h = 16,50 kWh"></span> ·
   <span class="m" data-tex="7{,}4\,\mathrm{kW}\cdot 1{,}0\,\mathrm{h} = 7{,}40\,\mathrm{kWh}" data-plain="7,4 kW · 1,0 h = 7,40 kWh"></span> ·
   <span class="m" data-tex="3{,}7\,\mathrm{kW}\cdot 0{,}5\,\mathrm{h} = 1{,}85\,\mathrm{kWh}" data-plain="3,7 kW · 0,5 h = 1,85 kWh"></span>.
   Summe: <span class="m" data-tex="16{,}50 + 7{,}40 + 1{,}85 = 25{,}75\,\mathrm{kWh}" data-plain="16,50 + 7,40 + 1,85 = 25,75 kWh"></span>,
   also 25 750 Wh. Zur Probe: Die mittlere Ladeleistung war
   <span class="m" data-tex="25{,}75\,\mathrm{kWh} / 3{,}0\,\mathrm{h} \approx 8{,}58\,\mathrm{kW}" data-plain="25,75 kWh / 3,0 h ≈ 8,58 kW"></span> —
   sie liegt zwischen 3,7 kW und 11,0 kW, wie es sein muss.

**Kontrollrechnung (K3 und `kontrolle_uebungen.py`):** 16,50 + 7,40 + 1,85 = 25,75 kWh = 25 750 Wh;
Distraktorwert 22,1 kWh; mittlere Leistung 25,75/3,0 = 8,5833 kW.

---

### Aufgabe 2 — `a2u` · Zahleneingabe · Anforderungsbereich I

Gemeinsamer Vorspann für `a2u` und `a2o`, als `.karte` über beiden Blöcken (wörtlich):

> In ein Rückhaltebecken läuft Wasser mit der Zuflussrate
> <span class="m" data-tex="q(t) = 0{,}5\,t^{2} + 1" data-plain="q(t) = 0,5 t² + 1"></span>
> (<span class="m" data-tex="q" data-plain="q"></span> in
> <span class="m" data-tex="\mathrm{m^3/h}" data-plain="m³/h"></span>,
> <span class="m" data-tex="t" data-plain="t"></span> in h). Betrachtet wird das Intervall
> <span class="m" data-tex="[0;4]" data-plain="[0; 4]"></span>, zerlegt in
> <span class="m" data-tex="n = 4" data-plain="n = 4"></span> gleich breite Streifen.
> <span class="m" data-tex="q" data-plain="q"></span> ist dort streng monoton wachsend.

Aufgabentext `a2u` (wörtlich):

> Berechne die Untersumme <span class="m" data-tex="U_4" data-plain="U₄"></span>.

**Einheitenliste:** `m³` · `L` · `m³/h` · `h`  (`m³/h` ist der Distraktor: eine Rate, kein Volumen.)

```js
a2u:{ wert:11.0, einheit:"m³", tol:0.05,
      alt:{wert:11000, einheit:"L"},
      ok:"Richtig. Δt = 1 h, und weil q wächst, liegt das Minimum jedes Streifens am linken Rand: U₄ = 1·(1,0 + 1,5 + 3,0 + 5,5) = 11,0 m³.",
      falschEinheit:"Die Zahl stimmt, die Einheit nicht. m³/h mal h ergibt m³ — das Ergebnis ist eine Wassermenge, keine Rate. In Litern wären es 11 000 L.",
      nah:"Vermutlich hast du die falschen vier Stützstellen genommen. Mit den rechten Rändern q(1), q(2), q(3), q(4) bekommst du 19,0 m³ — das ist die Obersumme. Für die Untersumme brauchst du das Minimum jedes Streifens, bei wachsendem q also den linken Rand, und q(4) = 9,0 taucht darin gar nicht auf.",
      weit:"Schreib dir zuerst die fünf Werte q(0) = 1,0 · q(1) = 1,5 · q(2) = 3,0 · q(3) = 5,5 · q(4) = 9,0 auf. Danach entscheidest du für jeden der vier Streifen, welcher der beiden Randwerte der kleinere ist." }
```

**Hilfen:**

1. *Tipp:* „Vier Streifen auf vier Stunden — überleg zuerst, wie breit ein einzelner Streifen ist.
   Weil die Rate durchgehend wächst, liegt der kleinste Wert eines Streifens immer an derselben
   Seite."
2. *Ansatz:* „<span class="m" data-tex="\Delta t = \frac{4-0}{4} = 1\,\mathrm{h}" data-plain="Δt = (4 − 0)/4 = 1 h"></span>,
   Stützstellen <span class="m" data-tex="t_k = 0,1,2,3,4" data-plain="t_k = 0, 1, 2, 3, 4"></span>.
   Für wachsendes <span class="m" data-tex="q" data-plain="q"></span> gilt
   <span class="m" data-tex="m_k = q(t_{k-1})" data-plain="m_k = q(t_(k−1))"></span>, also
   <span class="m" data-tex="U_4 = \Delta t\cdot\big(q(0)+q(1)+q(2)+q(3)\big)" data-plain="U₄ = Δt · (q(0) + q(1) + q(2) + q(3))"></span>.
   Der Wert <span class="m" data-tex="q(4)" data-plain="q(4)"></span> gehört nicht dazu."
3. *Lösungsweg:* Wertetabelle
   <span class="m" data-tex="q(0)=1{,}0" data-plain="q(0) = 1,0"></span> ·
   <span class="m" data-tex="q(1)=0{,}5+1=1{,}5" data-plain="q(1) = 0,5 + 1 = 1,5"></span> ·
   <span class="m" data-tex="q(2)=2+1=3{,}0" data-plain="q(2) = 2 + 1 = 3,0"></span> ·
   <span class="m" data-tex="q(3)=4{,}5+1=5{,}5" data-plain="q(3) = 4,5 + 1 = 5,5"></span> ·
   <span class="m" data-tex="q(4)=8+1=9{,}0" data-plain="q(4) = 8 + 1 = 9,0"></span> (alle in m³/h).
   Damit <span class="m" data-tex="U_4 = 1\,\mathrm{h}\cdot(1{,}0+1{,}5+3{,}0+5{,}5)\,\mathrm{\tfrac{m^3}{h}} = 11{,}0\,\mathrm{m^3}" data-plain="U₄ = 1 h · (1,0 + 1,5 + 3,0 + 5,5) m³/h = 11,0 m³"></span>,
   also 11 000 L.

---

### Aufgabe 3 — `a2o` · Zahleneingabe · Anforderungsbereich I

Aufgabentext (wörtlich):

> Berechne zur selben Rate die Obersumme <span class="m" data-tex="O_4" data-plain="O₄"></span> und
> gib damit an, in welchem Bereich der tatsächliche Zufluss der ersten vier Stunden sicher liegt.

**Einheitenliste:** `m³` · `L` · `m³/h` · `h`

```js
a2o:{ wert:19.0, einheit:"m³", tol:0.05,
      alt:{wert:19000, einheit:"L"},
      ok:"Richtig. O₄ = 1·(1,5 + 3,0 + 5,5 + 9,0) = 19,0 m³. Zusammen mit U₄ = 11,0 m³ ist der Zufluss auf das Intervall 11,0 m³ ≤ ΔV ≤ 19,0 m³ eingeschachtelt.",
      falschEinheit:"Die Zahl stimmt, die Einheit nicht. Aus m³/h mal h wird m³ — die Obersumme ist eine obere Schranke für eine Wassermenge, nicht für eine Rate.",
      nah:"11,0 m³ wäre die Untersumme. Für die Obersumme brauchst du das Maximum jedes Streifens; bei wachsendem q ist das der rechte Rand, und dort steht q(4) = 9,0 m³/h. Der Wert q(0) = 1,0 fällt dafür heraus.",
      weit:"Nimm dieselben fünf Funktionswerte wie eben, aber diesmal von jedem Streifen den größeren der beiden Randwerte. Es sind genau vier Summanden, nicht fünf." }
```

**Hilfen:**

1. *Tipp:* „Es sind dieselben vier Streifen wie eben. Nur die Seite, an der du ablesen musst,
   wechselt."
2. *Ansatz:* „<span class="m" data-tex="O_4 = \Delta t\cdot\big(q(1)+q(2)+q(3)+q(4)\big)" data-plain="O₄ = Δt · (q(1) + q(2) + q(3) + q(4))"></span>.
   Die Einschachtelung schreibst du danach als
   <span class="m" data-tex="U_4 \le \Delta V \le O_4" data-plain="U₄ ≤ ΔV ≤ O₄"></span>."
3. *Lösungsweg:*
   <span class="m" data-tex="O_4 = 1\,\mathrm{h}\cdot(1{,}5+3{,}0+5{,}5+9{,}0)\,\mathrm{\tfrac{m^3}{h}} = 19{,}0\,\mathrm{m^3}" data-plain="O₄ = 1 h · (1,5 + 3,0 + 5,5 + 9,0) m³/h = 19,0 m³"></span>.
   Zusammen mit <span class="m" data-tex="U_4 = 11{,}0\,\mathrm{m^3}" data-plain="U₄ = 11,0 m³"></span>:
   <span class="m" data-tex="11{,}0\,\mathrm{m^3} \le \Delta V \le 19{,}0\,\mathrm{m^3}" data-plain="11,0 m³ ≤ ΔV ≤ 19,0 m³"></span>.
   Die Schere ist <span class="m" data-tex="O_4 - U_4 = 8{,}0\,\mathrm{m^3}" data-plain="O₄ − U₄ = 8,0 m³"></span>
   und stimmt mit der Formel für monotone Funktionen überein:
   <span class="m" data-tex="\Delta t\cdot\big(q(4)-q(0)\big) = 1\cdot(9{,}0-1{,}0) = 8{,}0" data-plain="Δt · (q(4) − q(0)) = 1 · (9,0 − 1,0) = 8,0"></span>.
   Das ist eine ehrliche, aber grobe Auskunft: Die Unsicherheit beträgt fast drei Viertel der
   Untersumme.

**Kontrollrechnung (K11):** U₄ = 11,0 m³ · O₄ = 19,0 m³ · Schere 8,0 m³ = Δt·(q(4) − q(0)) ✓.
Zur internen Kontrolle liegt der Grenzwert bei 14,667 m³ und damit korrekt zwischen beiden — dieser
Wert steht **nicht** auf der Seite, weil er nur über eine Stammfunktion zu bekommen wäre.

---

### Aufgabe 4 — `a3` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Bleib bei derselben Rate <span class="m" data-tex="q(t) = 0{,}5\,t^{2} + 1" data-plain="q(t) = 0,5 t² + 1"></span>
> auf <span class="m" data-tex="[0;4]" data-plain="[0; 4]"></span>. Für eine Planungsrechnung soll
> der Zufluss auf 0,10 m³ genau bekannt sein — die Schere
> <span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span> darf also höchstens 0,10 m³
> betragen. In wie viele Streifen musst du das Intervall mindestens zerlegen?

**Einheitenliste im `<select>`:** `Streifen` · `m³` · `h` · `m³/h`
(Alle drei Alternativen sind falsch: Gesucht ist eine Anzahl, keine Größe mit physikalischer Einheit.)

```js
a3:{ wert:320, einheit:"Streifen", tol:0.5,
     ok:"Richtig. O_n − U_n = (4/n)·(q(4) − q(0)) = 32/n. Aus 32/n ≤ 0,10 folgt n ≥ 320, also n = 320. Probe: 32/320 = 0,100 ✓, 32/319 = 0,10031 ✗.",
     falschEinheit:"Der Zahlenwert stimmt, aber n ist eine Anzahl von Streifen und trägt keine Einheit wie m³ oder h. Die Einheit steckt in Δt = 4 h / n, nicht in n selbst.",
     nah:"Du bist nah dran — vermutlich hast du gerundet statt aufgerundet oder mit einer leicht anderen Schranke gerechnet. n muss ganzzahlig sein und die Ungleichung 32/n ≤ 0,10 erfüllen; 319 Streifen liefern noch 0,10031 m³ und reichen deshalb nicht.",
     weit:"Stell zuerst eine Formel für die Schere in Abhängigkeit von n auf, statt einzelne n auszuprobieren. Weil q auf [0; 4] monoton wächst, gilt O_n − U_n = Δt·(q(4) − q(0)) mit Δt = 4/n. Danach ist es eine einzige Ungleichung." }
```

**Hilfen:**

1. *Tipp:* „Probier nicht einzelne Streifenzahlen durch. Die Schere lässt sich für dieses Beispiel
   in einer Zeile durch <span class="m" data-tex="n" data-plain="n"></span> ausdrücken, weil die
   Rate monoton wächst."
2. *Ansatz:* „<span class="m" data-tex="O_n - U_n = \Delta t\cdot\big(q(4)-q(0)\big)" data-plain="O_n − U_n = Δt · (q(4) − q(0))"></span>
   mit <span class="m" data-tex="\Delta t = \frac{4}{n}" data-plain="Δt = 4/n"></span>. Setze das in
   die Bedingung <span class="m" data-tex="O_n - U_n \le 0{,}10" data-plain="O_n − U_n ≤ 0,10"></span>
   ein und löse nach <span class="m" data-tex="n" data-plain="n"></span> auf. Denk daran, dass
   <span class="m" data-tex="n" data-plain="n"></span> ganzzahlig sein muss."
3. *Lösungsweg:*
   <span class="m" data-tex="O_n - U_n = \frac{4}{n}\cdot(9{,}0-1{,}0) = \frac{32}{n}" data-plain="O_n − U_n = (4/n) · (9,0 − 1,0) = 32/n"></span>
   (in m³). Bedingung:
   <span class="m" data-tex="\frac{32}{n} \le 0{,}10 \iff n \ge 320" data-plain="32/n ≤ 0,10  ⟺  n ≥ 320"></span>.
   Kleinstes ganzzahliges <span class="m" data-tex="n" data-plain="n"></span> ist also **320**.
   Probe: <span class="m" data-tex="32/320 = 0{,}100" data-plain="32/320 = 0,100"></span> ✓,
   <span class="m" data-tex="32/319 = 0{,}10031" data-plain="32/319 = 0,10031"></span> ✗.
   Die Streifenbreite ist dann
   <span class="m" data-tex="\Delta t = 4\,\mathrm{h}/320 = 0{,}0125\,\mathrm{h} = 45\,\mathrm{s}" data-plain="Δt = 4 h / 320 = 0,0125 h = 45 s"></span>.

**Kontrollrechnung (K11 und `kontrolle_uebungen.py`):** Formelweg 32/n; direkt nachsummiert liefert
n = 320 die Schere 0,100000 m³ und n = 319 den Wert 0,100313 m³ ✓.
Merke für den Lehrerteil: 320 Streifen für zwei Nachkommastellen — das ist das Argument dafür, dass
ein besseres Verfahren gebraucht wird.

---

### Aufgabe 5 — `a4` · Multiple Choice · Anforderungsbereich II — richtige Option: Index **1**

Frage (wörtlich):

> Ein Durchflussmesser gibt die Zuflussrate in **Litern pro Minute** aus. Du hast die
> Streifenbreite dagegen in Stunden notiert:
> <span class="m" data-tex="\Delta t = 0{,}25\,\mathrm{h}" data-plain="Δt = 0,25 h"></span>. Auf
> einem Streifen ist der kleinste gemessene Wert
> <span class="m" data-tex="m_k = 12\,\mathrm{L/min}" data-plain="m_k = 12 L/min"></span>. Welchen
> Beitrag liefert dieser Streifen zur Untersumme?

| Index | Option (Anzeigetext) |
|---|---|
| 0 | 3 L |
| 1 | 180 L |
| 2 | 720 L |
| 3 | 3 L/min |

Feedback:
- 0: „Du hast 12 · 0,25 gerechnet und dabei die Einheiten nicht mitgeführt. 12 L/min · 0,25 h ergibt nicht 3 L, sondern 3 L·h/min — ein Ausdruck, den es so nicht gibt. Rate mal Zeit ist nur dann sauber, wenn beide Zeiten dieselbe Einheit tragen: 0,25 h sind 15 min."
- 1: „Richtig. Erst umrechnen: 0,25 h = 15 min. Dann 12 L/min · 15 min = 180 L. Die Minuten kürzen sich weg, übrig bleibt Liter — die Einheit eines Bestands, wie es sein muss."
- 2: „720 L wäre der Beitrag einer ganzen Stunde (12 L/min · 60 min). Der Streifen ist aber nur eine Viertelstunde breit, also kommt ein Viertel davon zusammen: 180 L."
- 3: „Die Einheit verrät den Fehler: L/min ist eine Rate. Ein Streifenbeitrag ist das Produkt aus Rate und Zeit und damit immer ein Bestand — hier ein Volumen in Litern. Genau daran erkennst du in jeder Aufgabe, ob du richtig multipliziert hast."

**Kontrollrechnung:** 0,25 h = 15 min; 12 L/min · 15 min = 180 L. Distraktoren: 12 · 0,25 = 3;
12 · 60 = 720.

---

### Aufgabe 6 — `z1` · Zuordnung · Anforderungsbereich II

Es ist die **einzige** Zuordnungsaufgabe des Moduls (Engine-Vorgabe aus `bausteine.md`, Abschnitt 6).

Aufgabentext (wörtlich):

> Vier Becken, vier Zuflussraten. Die Diagramme zeigen jeweils die Rate
> <span class="m" data-tex="f" data-plain="f"></span> über den Zeitraum von 0 h bis 6 h, nicht den
> Bestand. Ordne jeder Beschreibung des **Bestandsverlaufs** das passende **Ratendiagramm** zu.
> Alle vier Becken sind zu Beginn gleich voll.

**Die vier Inline-SVG-Diagramme** in `.diagramme`, jedes 240 × 150 px, gleiche Achsen
(<span class="m" data-tex="t" data-plain="t"></span> von 0 h bis 6 h waagerecht, Nulllinie
durchgezogen in `#334155`, Graph in `#0d7a52`, 2 px, Beschriftung „A" bis „D" oben links,
Achsentitel „t in h" und „f(t)"):

| Marke | Verlauf der Rate |
|---|---|
| **A** | waagerechte Gerade oberhalb der Achse, konstant positiv über den ganzen Zeitraum |
| **B** | fallende Gerade, startet deutlich oberhalb der Achse, schneidet die Nulllinie bei <span class="m" data-tex="t = 4\,\mathrm{h}" data-plain="t = 4 h"></span>, endet unterhalb |
| **C** | steigende Gerade, durchgehend oberhalb der Achse, am Ende etwa dreimal so hoch wie am Anfang |
| **D** | waagerechte Gerade unterhalb der Achse, konstant negativ über den ganzen Zeitraum |

**Die vier Zeilen** (`data-loesung` in dieser Reihenfolge: `A`, `C`, `D`, `B` — bewusst **nicht** die
Reihenfolge der Diagramme):

| Beschreibung des Bestandsverlaufs | `data-loesung` |
|---|---|
| „Der Bestand wächst gleichmäßig. Sein Graph ist eine steigende Gerade." | `A` |
| „Der Bestand wächst, und zwar immer schneller. Sein Graph ist nach oben gekrümmt." | `C` |
| „Der Bestand nimmt gleichmäßig ab. Sein Graph ist eine fallende Gerade." | `D` |
| „Der Bestand wächst bis <span class="m" data-tex="t = 4\,\mathrm{h}" data-plain="t = 4 h"></span>, erreicht dort sein Maximum und nimmt danach wieder ab." | `B` |

Jedes `<select>` enthält die Optionen `A`, `B`, `C`, `D`.

**Rückmeldung bei Teilerfolg (nennt die Strategie, nicht die Lösung):**
„Ein Teil sitzt. Geh die übrigen mit zwei Fragen an: **Erstens** — hat die Rate ein Vorzeichen, das
wechselt? Dann muss der Bestand einen Hoch- oder Tiefpunkt haben, und zwar genau an der Nullstelle
der Rate. **Zweitens** — ist die Rate konstant oder ändert sie sich? Konstante Rate heißt gerader
Bestandsgraph, wachsende Rate heißt Linkskrümmung. Die Rate ist die *Steigung* des Bestandsgraphen,
nicht seine Höhe."

**Rückmeldung bei voller Lösung:** „Alle vier richtig. Du hast damit die Kernübersetzung dieser
Einheit benutzt: Der Wert der Rate ist die Steigung des Bestandsgraphen, das Vorzeichen der Rate
entscheidet über Wachsen oder Fallen, und die Nullstelle der Rate ist der Extrempunkt des Bestands."

**Fachliche Kontrolle:** A konstant positiv ⇒ Bestand linear steigend ✓. C linear steigend positiv
⇒ Bestand streng wachsend mit wachsender Steigung, also linksgekrümmt ✓. D konstant negativ ⇒
Bestand linear fallend ✓. B positiv bis <span class="m" data-tex="t = 4" data-plain="t = 4"></span>,
danach negativ ⇒ Bestand steigt bis 4 h, Maximum bei 4 h, danach fallend ✓.

---

### Aufgabe 7 — `a6` · Zahleneingabe · Anforderungsbereich II

Aufgabentext (wörtlich):

> Zurück zum Becken aus der Simulation mit
> <span class="m" data-tex="f(t) = -0{,}2\,t^{2} + 1{,}6\,t + 1{,}8" data-plain="f(t) = −0,2 t² + 1,6 t + 1,8"></span>
> (in m³/h) und <span class="m" data-tex="V_0 = 12\,\mathrm{m^3}" data-plain="V₀ = 12 m³"></span>.
> Stell in der Simulation nacheinander
> <span class="m" data-tex="b = 9{,}0\,\mathrm{h}" data-plain="b = 9,0 h"></span> und
> <span class="m" data-tex="b = 12{,}0\,\mathrm{h}" data-plain="b = 12,0 h"></span> ein und lies
> jeweils das Feld „Grenzwert (exakt)" ab. Du erhältst 32,4 m³ und 21,6 m³.
> Berechne daraus, **wie viel Wasser zwischen der 9. und der 12. Stunde aus dem Becken abgeflossen
> ist**.

**Einheitenliste:** `m³` · `L` · `m³/h` · `kWh`
(`m³/h` und `kWh` sind Distraktoren — eine Rate und eine Energie.)

```js
a6:{ wert:10.8, einheit:"m³", tol:0.05,
     alt:{wert:10800, einheit:"L"},
     ok:"Richtig. Nach der Intervalladditivität ist der Zuwachs von 9 h bis 12 h gleich 21,6 m³ − 32,4 m³ = −10,8 m³. Das Minus heißt: Der Bestand sinkt. Abgeflossen sind also 10,8 m³.",
     falschEinheit:"Der Zahlenwert stimmt. Gefragt ist eine Wassermenge — die Differenz zweier rekonstruierter Volumina ist wieder ein Volumen in m³ (oder 10 800 L), keine Rate und schon gar keine Energie.",
     nah:"Prüfe, welche beiden Zahlen du voneinander abziehst. 21,6 m³ ist der Zuwachs von 0 h bis 12 h, 32,4 m³ der von 0 h bis 9 h — beide starten bei t = 0. Für das Stück von 9 h bis 12 h musst du sie subtrahieren, nicht addieren und auch nicht eine der beiden direkt hinschreiben.",
     weit:"Nutze die Zerlegungsregel: Der Zuwachs von 0 bis 12 ist der Zuwachs von 0 bis 9 plus der Zuwachs von 9 bis 12. Nach dem gesuchten Stück lässt sich diese Gleichung in einem Schritt auflösen." }
```

**Hilfen:**

1. *Tipp:* „Beide abgelesenen Zahlen gehören zu Zeiträumen, die bei
   <span class="m" data-tex="t = 0" data-plain="t = 0"></span> beginnen. Gefragt ist aber ein Stück
   mittendrin."
2. *Ansatz:* „Intervalladditivität:
   <span class="m" data-tex="\int_{0}^{12} f = \int_{0}^{9} f + \int_{9}^{12} f" data-plain="∫ von 0 bis 12 f = ∫ von 0 bis 9 f + ∫ von 9 bis 12 f"></span>.
   Löse nach <span class="m" data-tex="\int_{9}^{12} f" data-plain="∫ von 9 bis 12 f"></span> auf.
   Achte auf das Vorzeichen des Ergebnisses und darauf, was die Frage will: die *abgeflossene
   Menge*, also den Betrag."
3. *Lösungsweg:*
   <span class="m" data-tex="\int_{9}^{12} f\,\mathrm{d}t = \int_{0}^{12} f\,\mathrm{d}t - \int_{0}^{9} f\,\mathrm{d}t = 21{,}6\,\mathrm{m^3} - 32{,}4\,\mathrm{m^3} = -10{,}8\,\mathrm{m^3}" data-plain="∫ von 9 bis 12 f dt = 21,6 m³ − 32,4 m³ = −10,8 m³"></span>.
   Das Vorzeichen ist stimmig, denn
   <span class="m" data-tex="f(9) = 0" data-plain="f(9) = 0"></span> und
   <span class="m" data-tex="f(12) = -7{,}8\,\mathrm{m^3/h}" data-plain="f(12) = −7,8 m³/h"></span>:
   Ab der neunten Stunde ist die Rate negativ. **Abgeflossen sind 10,8 m³.**
   Die Bestände: <span class="m" data-tex="V(9) = 12 + 32{,}4 = 44{,}4\,\mathrm{m^3}" data-plain="V(9) = 12 + 32,4 = 44,4 m³"></span>,
   <span class="m" data-tex="V(12) = 12 + 21{,}6 = 33{,}6\,\mathrm{m^3}" data-plain="V(12) = 12 + 21,6 = 33,6 m³"></span> —
   Differenz 10,8 m³, dieselbe Zahl.
   Zusatz für den Vergleich: Die **insgesamt bewegte** Wassermenge über die zwölf Stunden ist die
   Summe der Beträge,
   <span class="m" data-tex="32{,}4 + 10{,}8 = 43{,}2\,\mathrm{m^3}" data-plain="32,4 + 10,8 = 43,2 m³"></span>,
   und damit doppelt so groß wie die Bestandsänderung von 21,6 m³. Wer nach „wie viel Wasser
   insgesamt geflossen ist" gefragt wird, muss an der Nullstelle
   <span class="m" data-tex="t = 9\,\mathrm{h}" data-plain="t = 9 h"></span> zerlegen.

**Kontrollrechnung (K10 und `kontrolle_uebungen.py`):** I(9) = 32,4 · I(12) = 21,6 ·
Differenz −10,8 · V(9) = 44,4 · V(12) = 33,6 · Beträge 32,4 + 10,8 = 43,2 · f(9) = 0 · f(12) = −7,8 ✓.

---

### Aufgabe 8 — `a5` · offen · Anforderungsbereich III

Aufgabentext (wörtlich):

> Jonas behauptet im Unterricht: *„Man braucht das ganze Grenzwertgerede gar nicht. Der exakte Wert
> liegt doch immer genau in der Mitte zwischen Unter- und Obersumme. Man rechnet einmal
> <span class="m" data-tex="U_n" data-plain="U_n"></span> und
> <span class="m" data-tex="O_n" data-plain="O_n"></span>, nimmt den Mittelwert
> <span class="m" data-tex="\tfrac{1}{2}(U_n + O_n)" data-plain="(U_n + O_n)/2"></span> und ist
> fertig."*
>
> Nimm zu Jonas' Behauptung Stellung. Belege deine Antwort an
> <span class="m" data-tex="f(x) = x^{2}" data-plain="f(x) = x²"></span> auf
> <span class="m" data-tex="[0;2]" data-plain="[0; 2]"></span> mit
> <span class="m" data-tex="n = 2" data-plain="n = 2"></span>; der exakte Wert dieses Integrals ist
> <span class="m" data-tex="\tfrac{8}{3}" data-plain="8/3"></span>. Gib außerdem an, was an seinem
> Vorgehen trotzdem brauchbar ist.

**Hilfen:**

1. *Tipp:* „Eine Behauptung mit dem Wort *immer* fällt, sobald du ein einziges Gegenbeispiel hast.
   Du hast eines vorgegeben bekommen — rechne es aus."
2. *Ansatz:* „Bestimme <span class="m" data-tex="U_2" data-plain="U₂"></span> und
   <span class="m" data-tex="O_2" data-plain="O₂"></span> für
   <span class="m" data-tex="f(x)=x^2" data-plain="f(x) = x²"></span> auf
   <span class="m" data-tex="[0;2]" data-plain="[0; 2]"></span> mit
   <span class="m" data-tex="\Delta x = 1" data-plain="Δx = 1"></span>, bilde den Mittelwert und
   vergleiche ihn mit <span class="m" data-tex="8/3" data-plain="8/3"></span>. Überlege danach, was
   der Mittelwert immerhin garantiert: Wie weit kann er im schlimmsten Fall danebenliegen, wenn du
   <span class="m" data-tex="U_n" data-plain="U_n"></span> und
   <span class="m" data-tex="O_n" data-plain="O_n"></span> kennst?"
3. *Strukturhilfe:* „Gliedere deine Antwort in drei Teile: (1) Behauptung widerlegt — das
   Gegenbeispiel mit Zahlen. (2) Warum sie im Allgemeinen scheitert — der Mittelwert wäre nur dann
   exakt, wenn die Abweichungen nach oben und unten sich auf jedem Streifen genau ausglichen. (3)
   Was bleibt — die halbe Schere als Fehlerschranke."

**Musterlösung (`data-stufe="9"`), wörtlich:**

> **Erwartete Argumentation.**
> Die Behauptung ist falsch. Gegenbeispiel:
> <span class="m" data-tex="f(x)=x^2" data-plain="f(x) = x²"></span> auf
> <span class="m" data-tex="[0;2]" data-plain="[0; 2]"></span>,
> <span class="m" data-tex="n = 2" data-plain="n = 2"></span>,
> <span class="m" data-tex="\Delta x = 1" data-plain="Δx = 1"></span>. Die Funktion wächst dort
> monoton, also
> <span class="m" data-tex="U_2 = 1\cdot(0^2 + 1^2) = 1" data-plain="U₂ = 1·(0² + 1²) = 1"></span>
> und <span class="m" data-tex="O_2 = 1\cdot(1^2 + 2^2) = 5" data-plain="O₂ = 1·(1² + 2²) = 5"></span>.
> Der Mittelwert ist <span class="m" data-tex="(1+5)/2 = 3" data-plain="(1 + 5)/2 = 3"></span>, der
> exakte Wert aber <span class="m" data-tex="8/3 \approx 2{,}667" data-plain="8/3 ≈ 2,667"></span>.
> Die Abweichung beträgt <span class="m" data-tex="1/3 \approx 0{,}333" data-plain="1/3 ≈ 0,333"></span>
> und ist damit nicht null. Eine Behauptung mit „immer" ist durch dieses eine Beispiel erledigt.
>
> Der Grund: Der Mittelwert wäre nur dann exakt, wenn sich auf jedem Streifen der zu wenig gezählte
> und der zu viel gezählte Anteil gerade aufhöben. Bei einer gekrümmten Funktion ist das nicht der
> Fall — bei <span class="m" data-tex="f(x)=x^2" data-plain="f(x) = x²"></span> liegt der Graph
> überall unterhalb der Sehne, deshalb schätzt der Mittelwert systematisch zu hoch.
>
> Brauchbar ist Jonas' Vorgehen trotzdem, und zwar als *Näherung mit Fehlerschranke*: Weil der
> exakte Wert zwischen <span class="m" data-tex="U_n" data-plain="U_n"></span> und
> <span class="m" data-tex="O_n" data-plain="O_n"></span> liegt, weicht der Mittelwert um höchstens
> die halbe Schere <span class="m" data-tex="\tfrac{1}{2}(O_n - U_n)" data-plain="(O_n − U_n)/2"></span>
> vom exakten Wert ab. Im Beispiel: halbe Schere 2, tatsächliche Abweichung 0,333 — die Schranke
> hält. Und weil die Schere mit wachsendem <span class="m" data-tex="n" data-plain="n"></span> gegen
> null geht, konvergiert auch der Mittelwert gegen den exakten Wert: bei
> <span class="m" data-tex="n = 4" data-plain="n = 4"></span> ist er 2,750 (Abweichung 0,083), bei
> <span class="m" data-tex="n = 8" data-plain="n = 8"></span> ist er 2,6875 (Abweichung 0,021). Er
> ist also eine gute Näherung, aber kein Ersatz für den Grenzübergang — der Grenzwert steckt nach
> wie vor dahinter.
>
> **Bewertungskriterien**
> · widerlegt die Behauptung ausdrücklich als falsch, statt sie nur zu relativieren
> · rechnet <span class="m" data-tex="U_2 = 1" data-plain="U₂ = 1"></span> und
> <span class="m" data-tex="O_2 = 5" data-plain="O₂ = 5"></span> korrekt
> · vergleicht den Mittelwert 3 mit dem exakten Wert 8/3 und benennt die Abweichung 1/3
> · begründet, warum sich die Fehler bei gekrümmten Funktionen nicht aufheben (Sehne über dem Graphen)
> · nennt die halbe Schere als gültige Fehlerschranke und belegt sie am Beispiel
> · stellt fest, dass der Grenzübergang dadurch nicht überflüssig wird

**Kontrollrechnung (K12 und `kontrolle_uebungen.py`):**
n = 2: U = 1,0000 · O = 5,0000 · Mittel 3,0000 · exakt 2,6667 · Abweichung 0,3333 · halbe Schere 2,0000.
n = 4: U = 1,7500 · O = 3,7500 · Mittel 2,7500 · Abweichung 0,0833.
n = 8: U = 2,1875 · O = 3,1875 · Mittel 2,6875 · Abweichung 0,0208. ✓

---

### Aufgabe 9 — `a7` · offen · Anforderungsbereich III

Aufgabentext (wörtlich):

> Im Erklärteil steht die Formel
> <span class="m" data-tex="O_n - U_n = \Delta x\cdot\big(f(b)-f(a)\big)" data-plain="O_n − U_n = Δx · (f(b) − f(a))"></span>
> mit dem Zusatz „nur für monotone <span class="m" data-tex="f" data-plain="f"></span>".
>
> **a)** Begründe, warum diese Formel bei monotonem
> <span class="m" data-tex="f" data-plain="f"></span> gilt.
> **b)** Zeige an der Simulationsrate
> <span class="m" data-tex="f(t) = -0{,}2\,t^{2} + 1{,}6\,t + 1{,}8" data-plain="f(t) = −0,2 t² + 1,6 t + 1,8"></span>
> auf <span class="m" data-tex="[0;6]" data-plain="[0; 6]"></span> mit
> <span class="m" data-tex="n = 4" data-plain="n = 4"></span>, dass sie dort **nicht** gilt, und
> erkläre den Grund.
> **c)** Erkläre, warum sich Unter- und Obersumme für wachsendes
> <span class="m" data-tex="n" data-plain="n"></span> trotzdem auf **einen** Wert zusammenziehen.

**Hilfen:**

1. *Tipp:* „Schreib
   <span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span> als **eine** Summe, nicht als
   Differenz zweier Summen. Was steht dann in jedem einzelnen Summanden?"
2. *Ansatz:* „Es gilt immer
   <span class="m" data-tex="O_n - U_n = \Delta x\cdot\sum_{k=1}^{n}(M_k - m_k)" data-plain="O_n − U_n = Δx · Σ (M_k − m_k)"></span>.
   Bei monotonem <span class="m" data-tex="f" data-plain="f"></span> ist
   <span class="m" data-tex="M_k - m_k = f(x_k) - f(x_{k-1})" data-plain="M_k − m_k = f(x_k) − f(x_(k−1))"></span> —
   eine Teleskopsumme. Für Teil b) brauchst du die Werte
   <span class="m" data-tex="f(0)" data-plain="f(0)"></span>,
   <span class="m" data-tex="f(4)" data-plain="f(4)"></span>,
   <span class="m" data-tex="f(6)" data-plain="f(6)"></span> und die Zahl
   <span class="m" data-tex="O_4 - U_4 = 5{,}925" data-plain="O₄ − U₄ = 5,925"></span> aus der Simulation."
3. *Strukturhilfe:* „Für c) genügt es nicht zu sagen „die Streifen werden schmaler". Argumentiere
   über das Produkt: Der eine Faktor
   <span class="m" data-tex="\Delta x" data-plain="Δx"></span> geht gegen null, der andere Faktor —
   die Summe der Höhenunterschiede — bleibt beschränkt. Nenne für die Simulationsrate die konkrete
   Schranke."

**Musterlösung (`data-stufe="9"`), wörtlich:**

> **Erwartete Argumentation.**
>
> **a)** Für jede Zerlegung gilt
> <span class="m" data-tex="O_n - U_n = \sum_{k=1}^{n} (M_k - m_k)\,\Delta x = \Delta x\cdot\sum_{k=1}^{n}(M_k - m_k)" data-plain="O_n − U_n = Σ (M_k − m_k) · Δx = Δx · Σ (M_k − m_k)"></span>.
> Ist <span class="m" data-tex="f" data-plain="f"></span> auf
> <span class="m" data-tex="[a;b]" data-plain="[a; b]"></span> monoton wachsend, so wird das Minimum
> jedes Streifens am linken und das Maximum am rechten Rand angenommen:
> <span class="m" data-tex="M_k - m_k = f(x_k) - f(x_{k-1})" data-plain="M_k − m_k = f(x_k) − f(x_(k−1))"></span>.
> Die Summe teleskopiert — jeder innere Wert kommt einmal positiv und einmal negativ vor —, übrig
> bleibt <span class="m" data-tex="f(x_n) - f(x_0) = f(b) - f(a)" data-plain="f(x_n) − f(x_0) = f(b) − f(a)"></span>.
> Also <span class="m" data-tex="O_n - U_n = \Delta x\,(f(b)-f(a))" data-plain="O_n − U_n = Δx · (f(b) − f(a))"></span>.
> Bei monoton fallendem <span class="m" data-tex="f" data-plain="f"></span> gilt dasselbe mit
> vertauschten Rollen, also mit <span class="m" data-tex="|f(b)-f(a)|" data-plain="|f(b) − f(a)|"></span>.
> Kontrolle an einem Fall, in dem die Rate auf
> <span class="m" data-tex="[0;3]" data-plain="[0; 3]"></span> noch monoton wächst:
> <span class="m" data-tex="n=4" data-plain="n = 4"></span> liefert
> <span class="m" data-tex="O_4-U_4 = 2{,}250" data-plain="O₄ − U₄ = 2,250"></span> und
> <span class="m" data-tex="\Delta t\,(f(3)-f(0)) = 0{,}75\cdot 3{,}0 = 2{,}250" data-plain="Δt · (f(3) − f(0)) = 0,75 · 3,0 = 2,250"></span> — gleich.
>
> **b)** Auf <span class="m" data-tex="[0;6]" data-plain="[0; 6]"></span> ist die Rate nicht
> monoton: Sie steigt bis zum Scheitel
> <span class="m" data-tex="t = 4{,}0\,\mathrm{h}" data-plain="t = 4,0 h"></span> und fällt danach.
> Die Formel liefert
> <span class="m" data-tex="\Delta t\,(f(6)-f(0)) = 1{,}5\cdot(4{,}2-1{,}8) = 3{,}600" data-plain="Δt · (f(6) − f(0)) = 1,5 · (4,2 − 1,8) = 3,600"></span>,
> die Simulation zeigt aber
> <span class="m" data-tex="O_4 - U_4 = 5{,}925" data-plain="O₄ − U₄ = 5,925"></span>. Die Formel
> **unterschätzt** die Schere also deutlich. Der Grund: Das Teleskopieren funktioniert nicht mehr,
> weil sich die Höhenunterschiede nicht mehr paarweise wegheben — das Anwachsen bis 4 h und das
> Fallen danach zählen beide zur Schwankung, statt sich gegenseitig aufzuzehren. Richtig ist
> stattdessen die Gesamtschwankung
> <span class="m" data-tex="(f(4)-f(0)) + (f(4)-f(6)) = 3{,}2 + 0{,}8 = 4{,}0\,\mathrm{m^3/h}" data-plain="(f(4) − f(0)) + (f(4) − f(6)) = 3,2 + 0,8 = 4,0 m³/h"></span>,
> und damit <span class="m" data-tex="O_n - U_n \le \Delta t\cdot 4{,}0" data-plain="O_n − U_n ≤ Δt · 4,0"></span>:
> bei <span class="m" data-tex="n=4" data-plain="n = 4"></span> ergibt das 6,000 ≥ 5,925 ✓, bei
> <span class="m" data-tex="n=8" data-plain="n = 8"></span> 3,000 ≥ 2,991 ✓, bei
> <span class="m" data-tex="n=16" data-plain="n = 16"></span> 1,500 ≥ 1,499 ✓.
>
> **c)** In
> <span class="m" data-tex="O_n - U_n = \Delta x\cdot\sum_k (M_k - m_k)" data-plain="O_n − U_n = Δx · Σ (M_k − m_k)"></span>
> geht der erste Faktor
> <span class="m" data-tex="\Delta x = \frac{b-a}{n}" data-plain="Δx = (b − a)/n"></span> gegen null,
> während der zweite Faktor durch die Gesamtschwankung von
> <span class="m" data-tex="f" data-plain="f"></span> nach oben beschränkt bleibt (hier durch
> 4,0 m³/h). Ein Produkt aus einer Nullfolge und einer beschränkten Folge ist eine Nullfolge, also
> <span class="m" data-tex="O_n - U_n \to 0" data-plain="O_n − U_n → 0"></span>. Da außerdem
> <span class="m" data-tex="U_n" data-plain="U_n"></span> wächst und
> <span class="m" data-tex="O_n" data-plain="O_n"></span> fällt und der gesuchte Wert für jedes
> <span class="m" data-tex="n" data-plain="n"></span> dazwischen eingeschlossen ist, bleibt ihm nur
> ein einziger möglicher Wert: der gemeinsame Grenzwert. Genau dieser Wert bekommt den Namen
> <span class="m" data-tex="\int_a^b f(x)\,\mathrm{d}x" data-plain="∫ von a bis b f(x) dx"></span>.
>
> **Bewertungskriterien**
> · schreibt die Schere als eine Summe mit dem gemeinsamen Faktor
> <span class="m" data-tex="\Delta x" data-plain="Δx"></span>
> · benennt für a) das Teleskopieren als tragendes Argument und knüpft es ausdrücklich an die Monotonie
> · rechnet in b) beide Zahlen aus (3,600 gegen 5,925) und stellt fest, dass die Formel unterschätzt
> · erklärt in b) den Scheitel als Ursache, statt nur „die Funktion ist nicht monoton" zu behaupten
> · argumentiert in c) über das Produkt aus Nullfolge und beschränktem Faktor, nicht nur über
> „immer schmalere Streifen"
> · nennt in c) die Einschachtelung als Grund dafür, dass nur *ein* Wert übrig bleibt

**Kontrollrechnung (K13 und `kontrolle_uebungen.py`):**
monoton, b = 3: n = 2 → 4,5000 = 1,5·3,0 ✓ · n = 4 → 2,2500 = 0,75·3,0 ✓ · n = 6 → 1,5000 ✓ · n = 8 → 1,1250 ✓.
nicht monoton, b = 6: n = 4 → O−U = 5,9250, Formel 3,6000 ✗, Schranke Δt·4,0 = 6,0000 ✓ ·
n = 8 → 2,9906 gegen 3,0000 ✓ · n = 16 → 1,4988 gegen 1,5000 ✓.

---

### Aufgabe 10 — `a8` · offen · Anforderungsbereich III

Aufgabentext (wörtlich):

> Mira liest in der Simulation bei
> <span class="m" data-tex="b = 6{,}0\,\mathrm{h}" data-plain="b = 6,0 h"></span> das Feld
> „Grenzwert (exakt)" ab und notiert 25,2 m³. Sie schreibt in ihr Heft:
> *„Die Fläche unter dem Ratengraphen ist 25,2 m³. Nach sechs Stunden stehen also 25,2 m³ im
> Becken."*
>
> **a)** Beurteile Miras Schlussfolgerung und gib den richtigen Bestand an.
> **b)** Ihre Klassenkameradin entgegnet: *„Und außerdem darf man das gar nicht ausrechnen, weil die
> Simulation ja nur Streifen zeichnet — 25,2 ist bloß geraten."* Nimm auch dazu Stellung, indem du
> angibst, was die Simulation bei
> <span class="m" data-tex="n = 4" data-plain="n = 4"></span> über den Wert 25,2 m³ tatsächlich
> beweist.

**Hilfen:**

1. *Tipp:* „Frag dich, ob das Becken bei
   <span class="m" data-tex="t = 0" data-plain="t = 0"></span> leer war. Steht das irgendwo?"
2. *Ansatz:* „Das Integral über die Rate liefert die **Änderung** des Bestands, nicht den Bestand:
   <span class="m" data-tex="V(b) = V(0) + \int_0^b f(t)\,\mathrm{d}t" data-plain="V(b) = V(0) + ∫ von 0 bis b f(t) dt"></span>.
   Für b) nimm die angezeigten Werte
   <span class="m" data-tex="U_4 = 21{,}825" data-plain="U₄ = 21,825"></span> und
   <span class="m" data-tex="O_4 = 27{,}750" data-plain="O₄ = 27,750"></span> und überlege, welche
   Aussage über 25,2 daraus zwingend folgt."
3. *Strukturhilfe:* „Trenne sauber zwischen drei Dingen: der *Rate*
   <span class="m" data-tex="f" data-plain="f"></span> (m³/h), dem *Zuwachs*
   <span class="m" data-tex="\Delta V" data-plain="ΔV"></span> (m³) und dem *Bestand*
   <span class="m" data-tex="V" data-plain="V"></span> (m³). Zwei davon haben dieselbe Einheit und
   sind trotzdem nicht dasselbe — genau hier liegt Miras Fehler."

**Musterlösung (`data-stufe="9"`), wörtlich:**

> **Erwartete Argumentation.**
>
> **a)** Der abgelesene Wert ist richtig, die Schlussfolgerung nicht. Das Integral über die
> Zuflussrate liefert den **Zuwachs** des Bestands im betrachteten Zeitraum, nicht den Bestand
> selbst. Es gilt
> <span class="m" data-tex="V(6) = V(0) + \int_0^6 f(t)\,\mathrm{d}t" data-plain="V(6) = V(0) + ∫ von 0 bis 6 f(t) dt"></span>.
> Mit dem in der Aufgabenstellung genannten Anfangsbestand
> <span class="m" data-tex="V(0) = 12\,\mathrm{m^3}" data-plain="V(0) = 12 m³"></span> ergibt sich
> <span class="m" data-tex="V(6) = 12\,\mathrm{m^3} + 25{,}2\,\mathrm{m^3} = 37{,}2\,\mathrm{m^3}" data-plain="V(6) = 12 m³ + 25,2 m³ = 37,2 m³"></span>.
> Mira unterschlägt also 12 m³ — knapp ein Drittel des tatsächlichen Bestands. Das Integral kann den
> Anfangsbestand gar nicht kennen: Es wertet nur die Rate aus, und die ist für ein volles und ein
> leeres Becken dieselbe. Ihre Formulierung „die Fläche ist 25,2 m³" ist zusätzlich schief — das
> Rechteck im Ratendiagramm hat die Achseneinheiten m³/h und h, sein Inhalt ist deshalb ein Volumen
> und keine geometrische Fläche.
>
> **b)** Der Einwand trifft nicht, aber er zielt auf etwas Richtiges. Bei
> <span class="m" data-tex="n = 4" data-plain="n = 4"></span> zeigt die Simulation
> <span class="m" data-tex="U_4 = 21{,}825\,\mathrm{m^3}" data-plain="U₄ = 21,825 m³"></span> und
> <span class="m" data-tex="O_4 = 27{,}750\,\mathrm{m^3}" data-plain="O₄ = 27,750 m³"></span>. Daraus
> folgt zwingend
> <span class="m" data-tex="21{,}825 \le \Delta V \le 27{,}750" data-plain="21,825 ≤ ΔV ≤ 27,750"></span>
> (in m³) — der Wert 25,2 liegt in diesem Intervall, ist damit **nicht widerlegt**, aber durch die
> vier Streifen allein auch nicht bewiesen: Die Aussage ist nur auf 5,925 m³ genau. Bewiesen wird der
> Wert erst durch den Grenzübergang, also dadurch, dass sich die Schere bei wachsendem
> <span class="m" data-tex="n" data-plain="n"></span> beliebig klein machen lässt und beide Folgen
> gegen denselben Wert streben. Für den Bestand heißt das entsprechend: Er liegt bei
> <span class="m" data-tex="n = 4" data-plain="n = 4"></span> gesichert zwischen 33,825 m³ und
> 39,750 m³.
>
> **Bewertungskriterien**
> · unterscheidet ausdrücklich zwischen Zuwachs und Bestand und nennt die Beziehung
> <span class="m" data-tex="V(b) = V(0) + \Delta V" data-plain="V(b) = V(0) + ΔV"></span>
> · gibt den richtigen Bestand 37,2 m³ mit Rechnung an
> · begründet, warum das Integral den Anfangsbestand nicht liefern kann
> · geht auf die Einheit ein: kein geometrischer Flächeninhalt, sondern m³/h mal h
> · nennt in b) die Einschachtelung 21,825 ≤ ΔV ≤ 27,750 mit Zahlen
> · trennt „nicht widerlegt" von „bewiesen" und verweist für den Beweis auf den Grenzübergang

**Kontrollrechnung (K7, K9 und `kontrolle_uebungen.py`):**
I(6) = 25,200 m³ · V(6) = 12 + 25,2 = 37,200 m³ · Anteil des Anfangsbestands 12/37,2 = 32,3 % ·
Einschachtelung 21,825 ≤ 25,200 ≤ 27,750 ✓ · Bestandsschranken 33,825 m³ bis 39,750 m³ ✓.

## 6 · Abschluss

`<section id="abschluss">`, `.stufe`-Kopf: Nr. **6**, Überschrift **Zusammenfassung und Selbstcheck**.

### 6.1 Vier Kernaussagen

Als vier `.merksatz`-Blöcke untereinander, jeweils mit fetter Überschrift.

**Kernaussage 1 — Rate mal Zeit ergibt Bestand.**
> Ein Streifen im Ratendiagramm hat die Höhe einer Rate und die Breite einer Zeitspanne. Sein
> Inhalt trägt deshalb die Einheit des Produkts beider Achsen — m³/h mal h ergibt m³, kW mal h
> ergibt kWh. „Fläche" ist dabei nur ein Bild; gerechnet wird immer eine rekonstruierte Menge. Die
> Einheit ist deine schnellste Kontrolle: Kommt am Ende eine Rate heraus, hast du nicht multipliziert.

**Kernaussage 2 — Unter- und Obersumme sind eine Garantie, keine Schätzung.**
> <span class="m" data-tex="U_n \le \Delta V \le O_n" data-plain="U_n ≤ ΔV ≤ O_n"></span> gilt für
> jedes <span class="m" data-tex="n" data-plain="n"></span>, nicht nur für große. Die Differenz
> <span class="m" data-tex="O_n - U_n = \Delta x\cdot\sum_k (M_k - m_k)" data-plain="O_n − U_n = Δx · Σ (M_k − m_k)"></span>
> ist die Genauigkeit, die du selbst in der Hand hast: Zu jeder geforderten Schranke lässt sich ein
> passendes <span class="m" data-tex="n" data-plain="n"></span> angeben. Minimum und Maximum werden
> auf dem **ganzen** Streifen gesucht — nur bei monotonen Funktionen liegen sie an den Rändern.

**Kernaussage 3 — Das bestimmte Integral ist ein Name für einen Grenzwert.**
> <span class="m block" data-tex="\int_a^b f(x)\,\mathrm{d}x := \lim_{n\to\infty} U_n = \lim_{n\to\infty} O_n" data-plain="∫ von a bis b f(x) dx := lim (n→∞) U_n = lim (n→∞) O_n"></span>
> Es ist kein Rechenverfahren, sondern die Zahl, auf die sich die Einschachtelung zusammenzieht.
> Dass beide Folgen denselben Wert erreichen, ist der eigentliche Inhalt der Definition — und der
> Grund, warum stetige Funktionen integrierbar heißen.

**Kernaussage 4 — Zuwachs ist nicht Bestand, und Vorzeichen zählen mit.**
> Das Integral über die Rate liefert die **Änderung**
> <span class="m" data-tex="\Delta V" data-plain="ΔV"></span>; der Bestand ergibt sich erst als
> <span class="m" data-tex="V(b) = V(a) + \int_a^b f(t)\,\mathrm{d}t" data-plain="V(b) = V(a) + ∫ von a bis b f(t) dt"></span>.
> Wird die Rate negativ, ziehen ihre Streifen ab — das Integral misst den *orientierten* Inhalt. Wer
> nach der insgesamt bewegten Menge gefragt wird, zerlegt an den Nullstellen der Rate und addiert
> die Beträge.

### 6.2 Hinweis zum Zentralabitur

`.hinweis`-Kasten (wörtlich):

> **Im Zentralabitur.** Die Rekonstruktion aus einem Ratengraphen ist ein Klassiker und taucht in
> mehreren Gestalten auf:
>
> · Ein Graph zeigt eine **Zufluss-, Zuwachs- oder Leistungsrate**, gefragt ist die zugehörige
> Gesamtmenge in einem Zeitraum. Der erste Satz deiner Lösung sollte immer klarstellen, welche Größe
> der Graph zeigt und welche Einheit dein Ergebnis bekommt.
> · Der Anfangsbestand steht **im Text, nicht im Graphen**. Wer ihn vergisst, verliert Punkte,
> obwohl das Integral stimmt.
> · Es wird nach dem **Zeitpunkt des größten Bestands** gefragt. Das ist die Nullstelle der Rate mit
> Vorzeichenwechsel von Plus nach Minus — nicht der Hochpunkt des Ratengraphen.
> · Es wird zwischen **Bestandsänderung** und **insgesamt geflossener Menge** unterschieden. Für die
> zweite Größe zerlegst du an den Nullstellen und addierst die Beträge.
> · Abschätzungen mit **Ober- und Untersumme** werden verlangt, wenn nur eine Wertetabelle oder ein
> abgelesener Graph vorliegt, für den es keine Funktionsgleichung gibt. Dann ist die Produktsumme
> das einzige Werkzeug — und die Angabe der Schere gehört zur vollständigen Antwort.
> · Im Leistungskurs kommt regelmäßig eine **Begründungsaufgabe** dazu: Warum ist der Wert
> eingeschachtelt, warum wird die Näherung mit wachsendem
> <span class="m" data-tex="n" data-plain="n"></span> besser, warum reicht ein einzelnes
> <span class="m" data-tex="n" data-plain="n"></span> für einen Beweis nicht aus.

### 6.3 Selbstcheck

`.karte` mit Überschrift „Selbstcheck" und dem Vorspann:
*„Hak ehrlich ab. Was du hier nicht ankreuzen kannst, holst du besser jetzt nach als in der Klausur."*
Sechs Zeilen als Liste mit Kästchen (`<input type="checkbox">`, kein Speichern, reine Sitzung):

1. Ich kann den Zusammenhang zwischen einer Änderungsrate und dem zugehörigen Bestand in beide
   Richtungen beschreiben und erklären, warum Rate mal Zeit die Einheit des Bestands ergibt.
2. Ich kann aus einer stückweise konstanten Rate den Zuwachs als Produktsumme berechnen und dabei
   jede Rate mit ihrer eigenen Dauer gewichten.
3. Ich kann zu einer gegebenen Funktion und Streifenzahl Unter- und Obersumme bestimmen — auch dann,
   wenn ein Extrempunkt im Inneren eines Streifens liegt.
4. Ich kann begründen, warum die Einschachtelung
   <span class="m" data-tex="U_n \le \Delta V \le O_n" data-plain="U_n ≤ ΔV ≤ O_n"></span> gilt, und
   zu einer geforderten Genauigkeit eine ausreichende Streifenzahl angeben.
5. Ich kann das bestimmte Integral als gemeinsamen Grenzwert von Unter- und Obersumme definieren,
   die Schreibweise mit ihren Bestandteilen erläutern und den orientierten Flächeninhalt am
   Vorzeichen der Rate erklären.
6. Ich kann in einem Sachzusammenhang zwischen Bestandsänderung, Bestand und insgesamt bewegter
   Menge unterscheiden und meine Wahl der Rechnung begründen.

### 6.4 Export

`.knopfleiste` mit `<button id="bExport" class="primaer">Ergebnisse kopieren</button>` und der
Zeile darunter (wörtlich):

> Der Knopf legt deine Antworten als Text in die Zwischenablage. Nichts davon wird gespeichert —
> lädst du die Seite neu, ist alles weg.

Die Namensliste am Skriptende steht in Abschnitt 8.

### 6.5 Ausblick auf die nächste Einheit

`.hinweis`-Kasten (wörtlich):

> **Wie es weitergeht.** Du hast in Aufgabe 4 ausgerechnet, dass du 320 Streifen brauchst, um den
> Zufluss auf 0,10 m³ genau zu kennen. Von Hand ist das nicht zu machen. Der **Hauptsatz der
> Differential- und Integralrechnung** liefert dafür eine Abkürzung, und zwar über die Umkehrung des
> Ableitens: Er verbindet den Grenzwert, den du hier kennengelernt hast, mit einer Funktion, deren
> Ableitung die Rate ist. Erst dadurch wird aus dem Begriff ein Rechenverfahren. Dass du den Begriff
> vorher hattest, ist kein Umweg — sonst bliebe der Hauptsatz eine Formel ohne Frage.

## 7 · Lehrerteil

`<details class="lehrer">` am Ende der Seite, `<summary>`: **Für die Lehrkraft**.
Verschwindet in der Druckansicht (`@media print` unverändert übernehmen).

### 7.1 Einordnung

- **Inhaltsfeld:** Funktionen und Analysis (Kernlehrplan Mathematik, gymnasiale Oberstufe NRW).
  Q1 umfasst die Fortführung der Analysis bis zur Integralrechnung; dieses Modul deckt den
  Einstieg in die Integralrechnung ab — **Rekonstruktion von Beständen, Produktsummen, Unter- und
  Obersummen, bestimmtes Integral als Grenzwert**. Der Hauptsatz ist ausdrücklich **nicht** Teil
  dieses Moduls.
- **Prozessbezogene Schwerpunkte:** Modellieren (Rate ↔ Bestand in Sachkontexten), Argumentieren
  (Aufgaben 8 bis 10 im Anforderungsbereich III), Werkzeuge nutzen (Simulation als
  Erkenntnisinstrument, nicht als Illustration).
- **Stellung in der Reihe:** unmittelbar nach der Funktionsuntersuchung und **vor** dem Hauptsatz.
  Wird das Modul nach dem Hauptsatz eingesetzt, verliert es seinen Zweck: Die Lernenden lösen dann
  jede Aufgabe über eine Stammfunktion und die Notwendigkeit des Grenzübergangs bleibt unsichtbar.
- **Vorausgesetzt wird:** mittlere und lokale Änderungsrate, Ableitung als Grenzwert von
  Differenzenquotienten, Umgang mit Summenzeichen, quadratische Funktionen samt Scheitel und
  Nullstellen. Die drei Vorwissensfragen im Einstieg prüfen genau das ab.
- **Offen markiert:** Die Feingliederung „Rekonstruktion vor Integralbegriff" ist eine fachdidaktisch
  übliche, aber im Kernlehrplan nicht wörtlich festgelegte Reihenfolge. Sie wird hier als
  Unterrichtsentscheidung gesetzt, nicht als Vorgabe zitiert.

### 7.2 Zeitbedarf

Ausgelegt auf eine Doppelstunde von 90 Minuten. Die Aufteilung ist so gerechnet, dass Abschnitt 4
nicht unter Zeitdruck gerät — er trägt den Erkenntnisschritt.

| Abschnitt | Zeit | Sozialform |
|---|---|---|
| 1 Einstieg (Ladesäule, drei Vorwissensfragen) | 8 min | Plenum, Fragen in Einzelarbeit |
| 2 Erklärteil (konstante Rate → Produktsumme → Streifen) | 20 min | lehrergelenkt mit Sicherungsphasen |
| 3 Vertiefung (Grenzübergang, Integralbegriff, Vorzeichen) | 17 min | Plenum; Details-Block je nach Kurs |
| 4 Simulation mit Beobachtungsauftrag und zwei MC-Fragen | 20 min | Partnerarbeit am Gerät |
| 5 Übungen (Auswahl, siehe 7.4) | 19 min | Einzel- oder Partnerarbeit |
| 6 Abschluss, Selbstcheck, Export | 6 min | Plenum |

**Realistisch in 90 Minuten schaffbar:** Abschnitte 1 bis 4 vollständig, dazu die Aufgaben 1, 2, 3
und eine der Begründungsaufgaben. Die restlichen Übungen sind Hausaufgabe oder Material für eine
Folgestunde. Wer den Details-Block in 3.1 (geschlossene Form von
<span class="m" data-tex="U_n" data-plain="U_n"></span> und
<span class="m" data-tex="O_n" data-plain="O_n"></span> über die Summenformel) im Plenum entwickelt,
braucht dafür allein 12 bis 15 Minuten — dann ist Abschnitt 5 in der Stunde nicht mehr unterzubringen.

### 7.3 Typische Schülerfehler — und wo anzuhalten ist

**(1) Bestand und Rate werden verwechselt.** Der häufigste Fehler überhaupt: „Nach 6 Stunden sind
25,2 m³ drin" statt 37,2 m³. Ursache ist, dass das Integral als *Ergebnis* gelesen wird, obwohl es
eine *Änderung* liefert.
→ **Anhalten am Ende von 2.2**, direkt nach dem Merksatz. Eine Minute genügt: „Das Becken war
vorher schon nicht leer — wo steht das im Diagramm?" Antwort: nirgends. Der Ratengraph ist für ein
volles und ein leeres Becken identisch. Aufgabe 10 greift genau das wieder auf.

**(2) Unter- und Obersumme werden mit linkem und rechtem Randwert gleichgesetzt.** Solange nur
monotone Beispiele gerechnet werden, funktioniert die falsche Regel und verfestigt sich.
→ **Anhalten in Abschnitt 4, bei
<span class="m" data-tex="n = 4" data-plain="n = 4"></span> und
<span class="m" data-tex="b = 6{,}0" data-plain="b = 6,0"></span>**, und den dritten Streifen (3,0 h
bis 4,5 h) gemeinsam ansehen: Die Randwerte sind 4,80 und 4,95, das Rechteck ist aber 5,00 hoch.
Das ist der Moment, in dem die Simulation etwas leistet, was eine Tafelzeichnung nicht leistet.
Die Frage an den Kurs lautet: „Welchen Wert nimmt die Rate auf diesem Streifen tatsächlich an, und
wo?" MC `sim2` sichert es ab.

**(3) Ungleich breite Abschnitte werden gleich gewichtet.** In der Tabelle in 2.2 addieren viele die
Raten (2,0 + 3,5 + 4,5 + 2,5 = 12,5) und multiplizieren erst am Schluss.
→ **Anhalten vor der Summenzeile der Tabelle in 2.2.** Erst die Spalte „Beitrag" von den Lernenden
ausfüllen lassen, dann summieren. Wer 12,5 stehen hat, sieht sofort, dass die Einheit nicht aufgeht.

**(4) Einheiten werden fallengelassen.** 12 L/min mal 0,25 h ergibt bei vielen „3". Der Fehler ist
in Klausuren teuer, weil er als Folgefehler durchschlägt.
→ **Anhalten beim Hinweiskasten in 2.1.** Regel als Merksatz an die Tafel: *Die Einheit des
Ergebnisses ist das Produkt der beiden Achseneinheiten.* Aufgabe 5 prüft es einzeln.

**(5) „Mehr Streifen ist genauer" bleibt ohne Begründung stehen.** Beliebt ist die Antwort „viermal
so genau", weil zwei Faktoren halbiert würden.
→ **Anhalten nach dem Beobachtungsauftrag in 4.9**, bevor die MC-Fragen kommen. Die Messreihe
11,400 → 5,925 → 2,991 → 1,499 → 0,750 an die Tafel; die Quotienten 1,924 · 1,981 · 1,995 · 1,999
selbst bilden lassen. Erst dann die Erklärung über
<span class="m" data-tex="O_n - U_n = \Delta t\cdot\sum_k (M_k - m_k)" data-plain="O_n − U_n = Δt · Σ (M_k − m_k)"></span>.

**(6) Der Grenzwert wird für „bewiesen" gehalten, weil die Zahlen sich annähern.** Numerische
Annäherung ist kein Beweis, dass beide Folgen denselben Wert haben.
→ **Anhalten beim Übergang von Abschnitt 4 zu 3.1** beziehungsweise beim Hinweiskasten „Was die
Simulation nicht beweist". Im Leistungskurs ist das der Punkt, an dem der Details-Block mit der
Summenformel seine Berechtigung bekommt.

**(7) Negative Raten werden „weggemacht".** Beträge werden gebildet oder negative Streifen einfach
ausgelassen, weil „eine Fläche ja positiv ist".
→ **Anhalten in 3.3 nach dem ersten Absatz.** Frage an den Kurs: „Was macht das Wasser zwischen der
9. und der 12. Stunde?" Danach in der Simulation
<span class="m" data-tex="b = 12{,}0" data-plain="b = 12,0"></span> einstellen und die Rechtecke
unterhalb der Achse zeigen. Aufgabe 7 rechnet es durch.

### 7.4 Differenzierung

**Für Lernende, die schneller fertig sind:**
- Aufgabe 4 (`a3`) allgemein lösen: Streifenzahl in Abhängigkeit von einer beliebigen Schranke
  <span class="m" data-tex="\varepsilon" data-plain="ε"></span> statt für 0,10 m³ —
  <span class="m" data-tex="n \ge 32/\varepsilon" data-plain="n ≥ 32/ε"></span>. Das ist der
  Übergang zur Epsilon-Sprache und bereitet die Definition der Integrierbarkeit vor.
- In der Simulation
  <span class="m" data-tex="b" data-plain="b"></span> systematisch variieren und
  <span class="m" data-tex="I(b)" data-plain="I(b)"></span> als Funktion tabellieren
  (I(3) = 10,8 · I(6) = 25,2 · I(9) = 32,4 · I(12) = 21,6). Die Frage „Wo ist
  <span class="m" data-tex="I" data-plain="I"></span> maximal, und was hat das mit
  <span class="m" data-tex="f" data-plain="f"></span> zu tun?" führt direkt auf den Hauptsatz zu,
  ohne ihn vorwegzunehmen.
- Aufgabe 9 c) verschärfen: Für welche Funktionen bricht das Argument zusammen? (Antwort in
  Stichworten: wenn die Gesamtschwankung nicht beschränkt ist. Nur andiskutieren, nicht ausführen.)
- Den Details-Block in 3.1 für
  <span class="m" data-tex="f(x)=x^3" data-plain="f(x) = x³"></span> auf
  <span class="m" data-tex="[0;1]" data-plain="[0; 1]"></span> nachbauen (benötigte Summenformel:
  <span class="m" data-tex="\sum_{k=1}^m k^3 = \big(\tfrac{m(m+1)}{2}\big)^2" data-plain="Σ (k=1..m) k³ = (m(m+1)/2)²"></span>,
  Grenzwert 1/4).

**Für Lernende, die mehr Zeit brauchen:**
- Aufgabe 2 und 3 (`a2u`, `a2o`) genügen als Pflichtteil. Sie sind bewusst mit
  <span class="m" data-tex="\Delta t = 1\,\mathrm{h}" data-plain="Δt = 1 h"></span> gebaut, damit die
  Multiplikation nicht zum Hindernis wird und der Blick auf die Auswahl der Stützstellen fällt.
- Vor Aufgabe 2 die fünf Funktionswerte
  <span class="m" data-tex="q(0)" data-plain="q(0)"></span> bis
  <span class="m" data-tex="q(4)" data-plain="q(4)"></span> gemeinsam an der Tafel tabellieren; der
  Rest ist dann reines Auswählen und Addieren.
- Die Zuordnungsaufgabe (`z1`) ist der niedrigschwellige Zugang zum Zusammenhang Rate ↔ Bestand und
  eignet sich als Einstieg in die Übungsphase für alle, auch vor Aufgabe 1.
- Von den drei Begründungsaufgaben genügt Aufgabe 10 (`a8`); sie ist die konkreteste, weil sie an
  einer einzelnen falschen Aussage hängt und Zahlen aus der Simulation benutzt.
- Wer in Abschnitt 2 hängt, arbeitet mit der Tabelle in 2.2 statt mit der allgemeinen Formel weiter:
  Die Produktsumme ist ohne Summenzeichen genauso richtig.

### 7.5 Bezug zu realen Daten und Experimenten

- **Wallbox oder Haushaltszähler.** Ein moderner Stromzähler zeigt Momentanleistung (kW) und
  Zählerstand (kWh) nebeneinander an — Rate und Bestand auf demselben Display. Ein Foto davon ist
  der beste Einstieg, den es zu diesem Thema gibt. Alternativ ein Ladeprotokoll aus einer
  Wallbox-App: Es liefert exakt die Tabelle aus Aufgabe 1, nur mit unrunden Zahlen.
- **Durchflussmessung im Klassenraum.** Ein Eimer, eine Stoppuhr und ein Wasserhahn, dessen Öffnung
  während des Versuchs verändert wird. Alle 15 Sekunden wird die Rate abgeschätzt (Messbecher pro
  Zeit), am Ende wird der Eimerinhalt gewogen oder gemessen. Der Vergleich zwischen der Produktsumme
  aus den Messwerten und der tatsächlichen Füllmenge ist der ehrlichste Zugang zu Unter- und
  Obersumme, den ein Klassenraum hergibt — samt der Erfahrung, dass die Schere real ist.
- **Fahrtenschreiber oder Fitness-Tracker.** Ein
  <span class="m" data-tex="v\text{-}t" data-plain="v-t"></span>-Diagramm aus einer Lauf- oder
  Radfahr-App und die dazu angezeigte Streckenlänge. Die Lernenden schätzen die Strecke aus dem
  Graphen mit fünf bis sechs Streifen ab und vergleichen mit dem angezeigten Wert. Der Bezug zur
  Physik (Weg als Fläche im
  <span class="m" data-tex="v\text{-}t" data-plain="v-t"></span>-Diagramm) ist hier greifbar und
  knüpft an Vorwissensfrage `vw3` an.
- **Pegelstände.** Die Landesbehörden veröffentlichen Abflussdaten von Flüssen in
  <span class="m" data-tex="\mathrm{m^3/s}" data-plain="m³/s"></span>. Ein Hochwasserereignis liefert
  eine Rate mit deutlichem Anstieg und Abfall — und die Frage nach der insgesamt abgeflossenen
  Wassermenge ist genau Aufgabe 7 mit echten Zahlen. Zeitaufwand für die Aufbereitung: etwa 20
  Minuten, weil die Werte typischerweise in Viertelstundenschritten vorliegen und für die
  Produktsumme zusammengefasst werden müssen.
- **Anschluss an die Physik.** Kraft-Weg-Diagramm und Arbeit, Stromstärke-Zeit-Diagramm und Ladung,
  Leistung-Zeit-Diagramm und Energie: dreimal dieselbe Struktur. Eine Absprache mit der Physik-
  Fachschaft lohnt sich, weil die Lernenden dort dieselbe Rekonstruktion unter anderem Namen
  wiederfinden.

## 8 · Checkliste der Bausteine

Inventar aller Bausteine dieser Datei. Es spiegelt nur, was oben steht — kommt beim Bauen etwas
hinzu, wird es hier nachgetragen.

### 8.1 Multiple Choice (`mcDaten`)

| Schlüssel | Abschnitt | AB | Optionen | richtiger Index `r` | Feedback-Einträge |
|---|---|---|---|---|---|
| `vw1` | 1.2 Vorwissen | — | 3 | **2** | 3 |
| `vw2` | 1.2 Vorwissen | — | 3 | **1** | 3 |
| `vw3` | 1.2 Vorwissen | — | 3 | **2** | 3 |
| `sim1` | 4.10 Verständnisfragen | II | 4 | **1** | 4 |
| `sim2` | 4.10 Verständnisfragen | II | 4 | **1** | 4 |
| `a4` | 5 Aufgabe 5 | II | 4 | **1** | 4 |

Sechs MC-Aufgaben, insgesamt 22 Feedbacktexte. Jedes `fb`-Array hat genau so viele Einträge wie
Optionen; kein Eintrag ist ein Allgemeinplatz. Der `name` der Radios ist jeweils identisch mit dem
`data-mc`-Wert. Die drei Vorwissensfragen stehen ohne Rahmen
(`style="border:none;padding:0"`) und ohne `.ab`-Chip, die drei übrigen mit Rahmen und Chip.

### 8.2 Zahleneingaben (`numDaten`)

| Schlüssel | Abschnitt | AB | Sollwert | Hauptheinheit | `tol` | Alternativeinheit | Einheitenliste (Distraktor **fett**) |
|---|---|---|---|---|---|---|---|
| `a1` | 5 Aufgabe 1 | I | 25,75 | kWh | 0,05 | 25 750 Wh | kWh · Wh · **kW** · **kJ** |
| `a2u` | 5 Aufgabe 2 | I | 11,0 | m³ | 0,05 | 11 000 L | m³ · L · **m³/h** · **h** |
| `a2o` | 5 Aufgabe 3 | I | 19,0 | m³ | 0,05 | 19 000 L | m³ · L · **m³/h** · **h** |
| `a3` | 5 Aufgabe 4 | II | 320 | Streifen | 0,5 | — | Streifen · **m³** · **h** · **m³/h** |
| `a6` | 5 Aufgabe 7 | II | 10,8 | m³ | 0,05 | 10 800 L | m³ · L · **m³/h** · **kWh** |

Fünf Zahleneingaben, jede mit vier Rückmeldetexten (`ok` · `falschEinheit` · `nah` · `weit`) und
dreistufiger Hilfe (Tipp → Ansatz → Lösungsweg). `tol` ist absolut und in der Hauptheinheit
angegeben. Bei `a3` ist `tol:0.5` so gewählt, dass ausschließlich 320 zählt: 319 und 321 liegen
außerhalb.

### 8.3 Zuordnung

| Schlüssel | Abschnitt | AB | Diagramme | Zeilen | Lösungsfolge |
|---|---|---|---|---|---|
| `z1` | 5 Aufgabe 6 | II | 4 Inline-SVG (A · B · C · D), je 240 × 150 px | 4 | `A` · `C` · `D` · `B` |

Die **einzige** Zuordnungsaufgabe des Moduls — die Engine läuft über einen festen Selektor
(`[data-check="zuordnung"]`), eine zweite würde einen Umbau der Engine erfordern. Die Reihenfolge
der Zeilen entspricht bewusst nicht der Reihenfolge der Diagramme.

### 8.4 Offene Aufgaben (`data-loesung`, Musterlösung in `.hilfe-text[data-stufe="9"]`)

| Schlüssel | Abschnitt | AB | Teilaufgaben | Bewertungskriterien |
|---|---|---|---|---|
| `a5` | 5 Aufgabe 8 | III | eine (Stellungnahme mit Gegenbeispiel) | 6 |
| `a7` | 5 Aufgabe 9 | III | drei (a · b · c) | 6 |
| `a8` | 5 Aufgabe 10 | III | zwei (a · b) | 6 |

Alle drei sind Begründungs- beziehungsweise Bewertungsaufgaben ohne längere Rechnung. Jede hat
Stufe 1 (Tipp), Stufe 2 (Ansatz) und Stufe 3 als **Strukturhilfe** — Stufe 3 gliedert die erwartete
Argumentation, rechnet aber nichts vor; die vollständige Musterlösung liegt in Stufe 9 hinter dem
`data-loesung`-Knopf. Jede Musterlösung besteht aus zwei Teilen: erwartete Argumentation, darunter
fett **Bewertungskriterien** als Aufzählung mit `·` getrennt.

### 8.5 Namensliste für den Export (`var namen = {…}`)

```js
var namen = {
  vw1:"Vorwissen 1 – mittlere Änderungsrate",
  vw2:"Vorwissen 2 – Einheit der Ableitung",
  vw3:"Vorwissen 3 – Weg im v-t-Diagramm",
  sim1:"Simulation 1 – Verhalten der Schere",
  sim2:"Simulation 2 – Scheitel im Streifen",
  a1: "Aufgabe 1 – Produktsumme Wallbox",
  a2u:"Aufgabe 2 – Untersumme U₄",
  a2o:"Aufgabe 3 – Obersumme O₄",
  a3: "Aufgabe 4 – benötigte Streifenzahl",
  a4: "Aufgabe 5 – Einheiten Rate mal Zeit",
  z1: "Aufgabe 6 – Zuordnung Rate zu Bestand",
  a6: "Aufgabe 7 – Vorzeichenwechsel",
  a5: "Aufgabe 8 – Stellungnahme Mittelwert",
  a7: "Aufgabe 9 – Gültigkeit der Scherenformel",
  a8: "Aufgabe 10 – Zuwachs und Bestand"
};
```

Fünfzehn Schlüssel: 5 Multiple Choice aus Einstieg und Simulation, 1 Multiple Choice aus den
Übungen, 5 Zahleneingaben, 1 Zuordnung, 3 offene Aufgaben. **Zu prüfen beim Bauen:** Ob die aus dem Referenzmodul kopierte Engine
für offene Aufgaben (`a5`, `a7`, `a8`) überhaupt einen Eintrag in `ergebnisse` erzeugt. Tut sie das
nicht, bleiben diese drei Zeilen ohne Wirkung und werden aus `namen` entfernt — ein Schlüssel in
`namen` ohne Eintrag in `ergebnisse` ist kein Fehler, aber toter Code. Umgekehrt gilt streng: Jeder
Schlüssel, der in `ergebnisse` landet, **muss** hier stehen, sonst fehlt die Aufgabe im Export.

### 8.6 Canvas und Simulation

| Element | ID | Maße | Inhalt |
|---|---|---|---|
| Canvas 1 | `cvRate` | `width="1000" height="490"`, CSS `width:100%` | Ratendiagramm mit Ober- und Untersummen-Rechtecken, Graph, Nulllinie, Grenzmarke, Scheitelmarke |
| Canvas 2 | `cvBestand` | `width="1000" height="310"`, CSS `width:100%` | Bestandsdiagramm mit Rekonstruktionsband zwischen unterer und oberer Linie |

Beide in **einer** IIFE, kein globaler Zustand außer `ergebnisse`. Keine Animationsschleife: Neu
gezeichnet wird ausschließlich im `input`-Ereignis der Regler und beim Klick auf die beiden Knöpfe
(siehe Warnhinweis 4.0). Die Pixelkonstanten stehen wörtlich wie in 4.7 oben in der IIFE.

### 8.7 Regler, Knöpfe und Anzeigefelder

| ID | Typ | Bereich | Schritt | Startwert |
|---|---|---|---|---|
| `regN` | `input[type=range]` | 1 … 40 | 1 | **4** |
| `regB` | `input[type=range]` | 1,0 … 12,0 | 0,5 | **6,0** |

| ID | Typ | Wirkung |
|---|---|---|
| `bVerdoppeln` | Knopf in `.knopfleiste` | `n = Math.min(40, 2*n)`, danach neu zeichnen |
| `bReset` | Knopf in `.knopfleiste` | setzt `n = 4` und `b = 6,0` zurück |
| `bExport` | Knopf im Abschluss | Ergebnisse in die Zwischenablage (aus dem Referenzmodul übernommen) |

Sechs Anzeigefelder in `.anzeige`, alle über `fmt(zahl, stellen)` mit Komma
(Startwerte bei <span class="m" data-tex="b = 6{,}0" data-plain="b = 6,0"></span>,
<span class="m" data-tex="n = 4" data-plain="n = 4"></span>):

| ID | Größe | Stellen | Startwert |
|---|---|---|---|
| `anzDt` | Streifenbreite <span class="m" data-tex="\Delta t" data-plain="Δt"></span> | 4 | 1,5000 h |
| `anzU` | Untersumme <span class="m" data-tex="U_n" data-plain="U_n"></span> | 3 | 21,825 m³ |
| `anzO` | Obersumme <span class="m" data-tex="O_n" data-plain="O_n"></span> | 3 | 27,750 m³ |
| `anzSchere` | <span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span> | 3 | 5,925 m³ |
| `anzGrenz` | Grenzwert (exakt) | 3 | 25,200 m³ |
| `anzBestand` | <span class="m" data-tex="V(b)" data-plain="V(b)"></span> | 2 | 37,20 m³ |

Dazu der Balken `balkenSchere` in der Schere-Zeile: Breite proportional zu
<span class="m" data-tex="O_n - U_n" data-plain="O_n − U_n"></span>, volle Breite bei 20 m³, Farbe
`#b45309`.

### 8.8 Sektionen, Kästen und Sonstiges

| Baustein | Vorkommen |
|---|---|
| `<section>`-IDs | `einstieg` · `rekonstruktion` · `grenzwert` · `simulation` · `uebungen` · `abschluss` |
| `.stufe`-Köpfe | 6, durchnummeriert 1 bis 6 |
| `.merksatz` | **7** — je einer in 2.2, 2.4 und 3.2, dazu die vier Kernaussagen im Abschluss (6.1) |
| `.hinweis` | **7** — Einheiten (2.1), Fehlvorstellung Randwerte (2.3), Fehlvorstellung Fläche (3.3), Ausblick Hauptsatz (3.4), „Was die Simulation nicht beweist" (4.10), Zentralabitur (6.2), Ausblick nächste Einheit (6.5) |
| `.auftrag` | 1 — Beobachtungsauftrag in 4.9 |
| `<details>` fachlich | 1 — Herleitung der geschlossenen Form in 3.1 |
| `<details class="lehrer">` | 1 — Lehrerteil (Abschnitt 7), verschwindet im Druck |
| `<div class="tabelle">`-Wrapper | um **jede** `<table>`: Treppenrate (2.2), Bezeichnungen des Integrals (3.2), Festwerte (4.1), Regler (4.2), Testfall (4.4), Bestandskontrollwerte (4.6), Anzeigefelder (4.8), Erwartete Notizen (4.9), Ladeprotokoll (5, Aufgabe 1), Zuordnungsübersicht (5, Aufgabe 6) |
| Selbstcheck | 6 Zeilen „Ich kann …" mit Kästchen, ohne Speicherung |
| KaTeX-Formeln | jede mit `data-tex` **und** `data-plain`; `.m.block` für abgesetzte Formeln |

**Farbtokens (nur diese drei tauschen):** `--akzent: #0d7a52` · `--akzent-hell: #e7f6ef` ·
`--akzent-rand: #b5e0cd`, dazu der Verlauf in `header.kopf`. Sonst bleibt der `<style>`-Block des
Referenzmoduls unverändert.

**Kontrollskripte:** `scratchpad/vorarbeit/mathe/kontrolle_integral.py` (Abschnitte 0 bis 3),
`scratchpad/vorarbeit/mathe/kontrolle_sim.py` (Abschnitt 4),
`scratchpad/vorarbeit/mathe/kontrolle_uebungen.py` (Abschnitt 5).
