# Modulinhalt: Das elektrische Feld — Plattenkondensator und Kapazität

Modul: `physik-q1-elektrisches-feld`
Fach: Physik, Leistungskurs Q1
Inhaltsfeld (Chip im Seitenkopf, **wörtlich**): **Ladungen, Felder und Induktion**
Akzentfarben: `--akzent: #1d4ed8`, `--akzent-hell: #eff6ff`, `--akzent-rand: #bfdbfe`
Titel der Seite: *Das elektrische Feld*
Untertitel im Kopf: *Vom Feldbegriff über die Feldlinie zum Kondensator und seiner Kapazität*
Chips: `Physik LK · Q1` · `Inhaltsfeld: Ladungen, Felder und Induktion` · `ca. 135 Minuten`

**Abgrenzung — verbindlich.**

| Gehört in dieses Modul | Gehört **nicht** hierher |
|---|---|
| Feldbegriff, Nahwirkung, Probeladung | Beschleunigung geladener Teilchen im Feld (Energiesatz `q·U = ½mv²`) |
| Feldstärke <span class="m">E = F/q</span>, Feld der Punktladung, Superposition | Waagerechter Wurf im Querfeld, Ablenkung im Kondensator |
| Feldlinien und Äquipotentialflächen | Millikan-Versuch, Elementarladung als Messgröße |
| Homogenes Feld, <span class="m">E = U/d</span> | Braunsche Röhre, Elektronenstrahloszilloskop |
| Kapazität, <span class="m">C = ε₀·ε_r·A/d</span>, Energie und Energiedichte | Lade- und Entladevorgang mit <span class="m">RC</span>-Zeitkonstante |

Die rechte Spalte ist Stoff des Folgemoduls `physik-q1-geladene-teilchen-e-feld`. Wo dieses Modul
darauf zeigt, geschieht das ausdrücklich als **Ausblick in einem Satz** und ohne Rechnung.

**Stellung im Curriculum.** Dieses Modul liegt **vor** `module/physik-q1-magnetisches-feld.html`
(Lorentzkraft, Wien-Filter) und vor `module/physik-q1-induktion.html`. Der Wien-Filter benutzt
<span class="m">E = U/d</span> und den Begriff des homogenen Feldes als bekannt — beides wird
hier erarbeitet. Das Magnetfeldmodul setzt genau diese Vorkenntnis in seiner dritten
Vorwissensfrage voraus; die Formulierungen bleiben deshalb deckungsgleich.

---

## 0 · Konventionen, Konstanten und Formelzeichen

**Diese Festlegungen gelten für jede Abbildung, jede Simulation, jede Aufgabe und jede
Musterlösung des Moduls. Der Bauagent weicht davon nicht ab.**

### 0.1 Konstanten (überall mit genau diesen Werten rechnen)

| Größe | Zeichen | Wert | Einheit |
|---|---|---|---|
| elektrische Feldkonstante | ε₀ | 8,854 · 10⁻¹² | F/m = C/(V·m) |
| Coulomb-Konstante | 1/(4πε₀) | 8,988 · 10⁹ | N·m²/C² |
| Elementarladung | e | 1,602 · 10⁻¹⁹ | C |
| Durchschlagsfeldstärke trockener Luft | E_max | ≈ 3 · 10⁶ | V/m |

Formeln dafür:
- `data-tex`: `\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\dfrac{\mathrm{F}}{\mathrm{m}}`
  · `data-plain`: `ε₀ = 8,854 · 10⁻¹² F/m`
- `data-tex`: `\dfrac{1}{4\pi\varepsilon_0} = 8{,}988 \cdot 10^{9}\,\dfrac{\mathrm{N\,m^2}}{\mathrm{C^2}}`
  · `data-plain`: `1/(4π·ε₀) = 8,988 · 10⁹ N·m²/C²`

**Achtung Schreibweise.** In `data-tex` heißt die Feldkonstante `\varepsilon_0`, niemals
`\epsilon_0` (optisch zu ähnlich zum Element-Zeichen) und niemals als roher Unicode im TeX-String.
In `data-plain` steht das Unicode-Zeichen `ε₀`.

### 0.2 Formelzeichen

| Zeichen | Bedeutung | Einheit | Anmerkung |
|---|---|---|---|
| <span class="m">Q</span> | felderzeugende Ladung, Ladung auf einer Kondensatorplatte | C | in diesem Modul stets als Betrag |
| <span class="m">q</span> | Probeladung | C | vorzeichenbehaftet |
| <span class="m">E</span> | Betrag der elektrischen Feldstärke | V/m = N/C | Vektor: <span class="m">E⃗</span> |
| <span class="m">U</span> | Spannung zwischen zwei Punkten bzw. den Platten | V | |
| <span class="m">d</span> | Plattenabstand | m | **nicht** Abstand von einer Platte |
| <span class="m">A</span> | Plattenfläche (einer Platte) | m² | |
| <span class="m">σ</span> | Flächenladungsdichte <span class="m">σ = Q/A</span> | C/m² | |
| <span class="m">C</span> | Kapazität | F = C/V | |
| <span class="m">ε_r</span> | Permittivitätszahl des Dielektrikums | 1 | dimensionslos, ≥ 1 |
| <span class="m">W</span> | im Feld gespeicherte Energie | J | |
| <span class="m">w</span> | Energiedichte <span class="m">w = W/V</span> | J/m³ | |

**Kollisionswarnung an den Bauagenten.** Das Zeichen `C` steht in diesem Modul für zwei Dinge:
die **Kapazität** (kursiv, <span class="m">C</span>) und die **Einheit Coulomb** (aufrecht, `\mathrm{C}`).
In jedem `data-tex` gehört die Einheit in `\mathrm{...}`, die Größe nicht. In `data-plain` wird
die Einheit immer mit einem schmalen Abstand und im Kontext geschrieben (`4,0 nC`, nie `4,0C`).

### 0.3 Richtungen und Farben

| Objekt | Festlegung |
|---|---|
| positive Ladung / positive Platte | rot `#dc2626`, Symbol `+` |
| negative Ladung / negative Platte | blau `#1d4ed8`, Symbol `−` (U+2212) |
| Feldlinie | dunkelgrau `#334155`, **Pfeilspitze in der Mitte** der Linie |
| Äquipotentiallinie | gestrichelt, grün `#0d7a52` |
| Dielektrikum | Fläche `#e0f2fe` mit Rand `#7dd3fc`, Beschriftung `ε_r = …` |

Feldlinien laufen **von Plus nach Minus**, also von der positiven zur negativen Platte.
In allen Abbildungen dieses Moduls liegt die **positive Platte links**, die negative rechts;
die Feldlinien zeigen damit nach rechts. Diese Festlegung gilt auch in der Simulation.

### 0.4 Vorzeichenkonvention bei der Probeladung

<span class="m">E⃗ = F⃗/q</span> wird mit **vorzeichenbehaftetem** q gelesen: Für <span class="m">q > 0</span>
ist <span class="m">F⃗</span> parallel zu <span class="m">E⃗</span>, für <span class="m">q < 0</span>
antiparallel. In Betragsrechnungen steht <span class="m">F = |q| · E</span>.

- `data-tex`: `\vec{E} = \dfrac{\vec{F}}{q} \qquad F = |q| \cdot E`
- `data-plain`: `E = F/q     F = |q| · E`

### 0.5 Einheiten und Zahlendarstellung

- Dezimaltrennzeichen **Komma**, auch in jeder Simulationsanzeige (`fmt()`).
- Vorsätze so wählen, dass der Zahlenwert zwischen 0,1 und 1000 liegt: **pF, nF, µF** für die
  Kapazität, **nC, µC** für die Ladung, **kV/m, MV/m** für die Feldstärke, **µJ, mJ, J** für
  die Energie.
- Die Einheit der Feldstärke wird im Modul durchgehend als **V/m** angegeben; dass
  <span class="m">1 V/m = 1 N/C</span> gilt, wird in 2.2 einmal gezeigt und danach benutzt.

---

## 1 · Einstieg

Geht so in `<section id="einstieg">`, `.stufe`-Nummer **1**, Überschrift **Einstieg**.

### 1.1 Aufhänger (zwei Absätze, kein Lehrbuchton)

**Absatz 1:**

> Ein Rettungswagen hat einen Defibrillator an Bord, und der wiegt keine zwanzig Kilo. Wenn er
> auslöst, gibt er rund 200 Joule in etwa zehn Millisekunden ab — das sind 20 Kilowatt, kurzzeitig
> mehr als ein Kleinwagen leistet. Der Akku im Gerät speichert ein Vielfaches dieser Energie, rund
> 40 Kilojoule, also das Zweihundertfache. Er kann sie nur nicht schnell genug loswerden. Die
> Energie für den Schock kommt deshalb aus einem Bauteil, das gar nichts chemisch speichert,
> sondern nur Ladung auf zwei getrennten Flächen hält: einem Kondensator.

**Absatz 2:**

> Dasselbe Bauteil steckt in dem Gerät, auf dem du das hier vermutlich liest. Dein Finger und eine
> hauchdünne Elektrode unter dem Deckglas bilden zusammen einen winzigen Kondensator von etwa zehn
> Pikofarad; das Display misst nichts weiter als dessen Veränderung, wenn du es berührst. Mit
> Handschuh passiert nichts — es fehlt der leitende Finger. Bleiben zwei Fragen, und um die geht es
> auf dieser Seite: Wovon hängt ab, wie viel Ladung und wie viel Energie so ein Gebilde fasst?
> Und wo genau steckt die Energie eigentlich, wenn sich die beiden Platten gar nicht berühren?

**Rechnerische Deckung der Zahlen im Aufhänger** (Kontrollrechnung K-1 bis K-3, Abschnitt 9):

| Aussage im Text | Rechnung | Ergebnis |
|---|---|---|
| „rund 200 Joule" | W = ½ · 100 µF · (2,0 kV)² | 200 J |
| „zehn Millisekunden → 20 kW" | P = 200 J / 10 ms | 20 000 W |
| „Akku rund 40 Kilojoule" | 3000 mAh = 10 800 C, W = 10 800 C · 3,7 V | 39 960 J ≈ 40 kJ |
| „Zweihundertfache" | 39 960 J / 200 J | 199,8 |
| „etwa zehn Pikofarad" | C = ε₀ · 6,0 · 1,0 cm² / 0,50 mm | 10,6 pF |

Der Bauagent schreibt in den Fließtext nur die gerundeten Werte, nennt aber in einem
`<details>`-Block direkt darunter die Abschätzung des Touchscreen-Werts:

> **Woher die zehn Pikofarad?**
> Fingerkuppe <span class="m">A ≈ 1,0 cm²</span>, Deckglas <span class="m">d ≈ 0,50 mm</span>,
> Glas mit <span class="m">ε_r ≈ 6,0</span>. Mit der Formel, die du in Abschnitt 3 herleitest,
> ergibt das <span class="m">C = 10,6 pF</span> — gut ein Zehnmillionstel der Kapazität im
> Defibrillator. Dass ein Bauteil über knapp sieben Zehnerpotenzen dieselbe Physik zeigt, ist kein Zufall,
> sondern der Grund, warum sich der Aufwand lohnt, diese Physik sauber aufzuschreiben.
> - `data-tex`: `C = \dfrac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d} = \dfrac{8{,}854\cdot10^{-12}\,\frac{\mathrm F}{\mathrm m} \cdot 6{,}0 \cdot 1{,}0\cdot10^{-4}\,\mathrm{m^2}}{0{,}50\cdot10^{-3}\,\mathrm m} = 1{,}06\cdot10^{-11}\,\mathrm F`
> - `data-plain`: `C = ε₀·ε_r·A/d = (8,854·10⁻¹² F/m · 6,0 · 1,0·10⁻⁴ m²) / (0,50·10⁻³ m) = 1,06·10⁻¹¹ F = 10,6 pF`

### 1.2 Vorwissensfragen

Kopf der Karte wie im Referenzmodul:
`<div class="karte"><h3>Vorwissen prüfen</h3>` mit dem grauen Hinweissatz
*„Drei Fragen aus der Sekundarstufe I und der Einführungsphase. Wenn du hier hängst, lohnt sich ein
Blick zurück, bevor du weitermachst."*

Alle drei als `<div class="aufgabe" data-mc="…" style="border:none;padding:0;…">`.

---

#### vw1 — Coulombgesetz (Sek I / EF)

**Frage:**

> Zwei kleine geladene Kugeln ziehen sich im Abstand <span class="m">r</span> mit der Kraft
> <span class="m">F</span> an. Du vergrößerst den Abstand auf <span class="m">3r</span> und lässt
> beide Ladungen unverändert. Wie groß ist die Kraft jetzt?

| `data-i` | Option |
|---|---|
| 0 | <span class="m">F/3</span> |
| 1 | <span class="m">F/9</span> |
| 2 | <span class="m">F/6</span> |

`r: 1`

**Feedback (`fb`), je Eintrag ein eigener Denkfehler:**

- `fb[0]`: „Das wäre richtig, wenn die Kraft proportional zu 1/r wäre. Im Coulombgesetz steht der
  Abstand aber im Quadrat: F = 1/(4π·ε₀) · |q₁|·|q₂|/r². Aus dem dreifachen Abstand wird deshalb der
  neunfache Nenner."
- `fb[1]`: „Richtig. F ~ 1/r², aus r wird 3r, also wird F auf 1/3² = 1/9 herabgesetzt. Dieselbe
  Abstandsabhängigkeit findest du gleich beim Feld einer Punktladung wieder."
- `fb[2]`: „Hier sind zwei Dinge vermischt: Der Faktor 3 aus dem Abstand wurde verdoppelt statt
  quadriert. Quadrieren heißt 3 · 3 = 9, nicht 3 + 3 = 6."

---

#### vw2 — Spannung als Energie pro Ladung (Sek I / EF)

**Frage:**

> Zwischen zwei Punkten liegt die Spannung <span class="m">U = 1 V</span>. Was bedeutet das?

| `data-i` | Option |
|---|---|
| 0 | Pro Sekunde fließt 1 Coulomb Ladung von einem Punkt zum anderen. |
| 1 | Verschiebt man die Ladung 1 C zwischen den beiden Punkten, so wird dabei die Energie 1 J umgesetzt. |
| 2 | Auf eine Ladung von 1 C wirkt zwischen den beiden Punkten die Kraft 1 N. |

`r: 1`

**Feedback:**

- `fb[0]`: „Das beschreibt die Stromstärke: 1 C pro Sekunde ist 1 Ampere. Die Spannung sagt nichts
  darüber, ob überhaupt Ladung fließt — sie liegt auch an einem offenen Stromkreis an."
- `fb[1]`: „Richtig. U = W/q, also 1 V = 1 J/C. Genau diese Definition brauchst du gleich, um
  E = U/d herzuleiten."
- `fb[2]`: „Kraft pro Ladung ist die elektrische **Feldstärke**, nicht die Spannung — und sie hat
  die Einheit N/C. Die beiden Größen hängen zusammen (E = U/d), sind aber nicht dasselbe: Die
  Spannung ist eine Energiegröße, die Feldstärke eine Kraftgröße."

---

#### vw3 — Hubarbeit und Wegunabhängigkeit (EF Mechanik)

**Frage:**

> Eine Kiste der Masse <span class="m">m</span> wird um die Höhe <span class="m">h</span> angehoben —
> einmal senkrecht, einmal reibungsfrei über eine schiefe Ebene, deren Weglänge doppelt so groß ist.
> Wie verhalten sich die verrichteten Arbeiten zueinander?

| `data-i` | Option |
|---|---|
| 0 | Über die schiefe Ebene ist die Arbeit halb so groß, weil die nötige Kraft nur halb so groß ist. |
| 1 | Über die schiefe Ebene ist die Arbeit doppelt so groß, weil der Weg doppelt so lang ist. |
| 2 | Beide Arbeiten sind gleich groß: <span class="m">W = m·g·h</span>, unabhängig vom Weg. |

`r: 2`

**Feedback:**

- `fb[0]`: „Die Kraft ist tatsächlich nur halb so groß — aber der Weg ist doppelt so lang, und in
  W = F · s steht das Produkt. Halbe Kraft mal doppelter Weg ergibt dieselbe Arbeit."
- `fb[1]`: „Der Weg ist doppelt so lang, das stimmt. Übersehen ist die Hangabtriebskraft: Entlang
  der schiefen Ebene muss nur die halbe Kraft aufgebracht werden. Das Produkt F · s bleibt gleich."
- `fb[2]`: „Richtig. Das Schwerefeld ist konservativ: Die Arbeit hängt nur von Anfangs- und
  Endhöhe ab. Für das elektrische Feld gilt genau dasselbe — darauf beruht, dass man jedem Punkt
  ein Potential zuordnen kann."

---

## 2 · Erklärteil — vom Kraftgesetz zum Feldbegriff

`<section id="grundlagen">`, `.stufe`-Nummer **2**,
Überschrift **Vom Kraftgesetz zum Feldbegriff**.

### 2.1 Das Problem, das den Feldbegriff nötig macht

**Fließtext:**

> Das Coulombgesetz beschreibt die Kraft zwischen zwei Punktladungen:
>
> - `data-tex` (Blockformel): `F = \dfrac{1}{4\pi\varepsilon_0}\cdot\dfrac{|q_1| \cdot |q_2|}{r^2}`
> - `data-plain`: `F = 1/(4π·ε₀) · |q₁|·|q₂| / r²`
>
> Das trägt, solange man zwei Ladungen hat und wissen will, wie stark sie sich anziehen. Zwei Fragen
> beantwortet es aber nicht. Erstens: Was ist eigentlich zwischen den beiden Ladungen? Nach dem
> Coulombgesetz *nichts* — die Kraft würde über die Entfernung hinweg wirken, sofort und ohne
> Vermittler. Zweitens: Was passiert, wenn man eine der beiden Ladungen ruckartig verschiebt? Merkt
> die andere das augenblicklich? Die Antwort ist nein; die Wirkung breitet sich mit
> Lichtgeschwindigkeit aus. Eine Beschreibung, in der zwischen den Ladungen nichts ist, kann das
> nicht erklären.
>
> Der Ausweg ist ein Zwischenschritt, und der ist die eigentliche Idee dieses Kapitels: Eine Ladung
> verändert den Raum um sich herum. Diese Veränderung heißt **elektrisches Feld**. Eine zweite
> Ladung spürt dann nicht mehr die erste, sondern nur noch das Feld an ihrem eigenen Ort. Aus einer
> Fernwirkung über beliebige Entfernung wird eine **Nahwirkung** an Ort und Stelle.

**Merksatz 1** (`<div class="merksatz">`, Titel *Warum Feld und nicht nur Kraft*):

> Das Feld ist kein zweiter Name für die Kraft. Es ist die Behauptung, dass der Raum um eine Ladung
> herum verändert ist — auch dann, wenn weit und breit keine zweite Ladung da ist, an der man es
> merken könnte. Diese Behauptung ist prüfbar, und sie hält stand: Felder tragen Energie und
> brauchen Zeit, um sich auszubreiten.

### 2.2 Die elektrische Feldstärke

**Fließtext:**

> Um das Feld messbar zu machen, bringt man eine **Probeladung** <span class="m">q</span> an die
> Stelle, die einen interessiert, und misst die Kraft auf sie. Verdoppelt man die Probeladung,
> verdoppelt sich die Kraft. Der **Quotient** aus beidem bleibt gleich — und weil er nicht mehr von
> der Probeladung abhängt, beschreibt er nur noch die Stelle im Raum. Er heißt elektrische
> Feldstärke.
>
> - `data-tex` (Blockformel): `\vec{E} = \dfrac{\vec{F}}{q} \qquad [E] = 1\,\dfrac{\mathrm{N}}{\mathrm{C}} = 1\,\dfrac{\mathrm{V}}{\mathrm{m}}`
> - `data-plain`: `E = F/q     [E] = 1 N/C = 1 V/m`
>
> Die Feldstärke ist ein **Vektor**: Ihre Richtung ist definitionsgemäß die Richtung der Kraft auf
> eine **positive** Probeladung. Auf eine negative Ladung wirkt die Kraft dann entgegengesetzt zum
> Feld; ihr Betrag ist <span class="m">F = |q| · E</span>.
>
> An die Probeladung stellt man eine Bedingung: Sie muss so klein sein, dass sie das Feld, das sie
> messen soll, nicht merklich verändert. Streng schreibt man deshalb
> <span class="m">E⃗ = lim(q→0) F⃗/q</span>. Im Unterricht rechnet man mit einer kleinen Ladung und
> behält im Kopf, warum das nötig ist.
>
> - `data-tex`: `\vec{E} = \lim_{q \to 0} \dfrac{\vec{F}}{q}`
> - `data-plain`: `E = lim(q→0) F/q`

**Details-Block 1** — Zusammenfassung *Warum 1 N/C dasselbe ist wie 1 V/m*:

> Beide Einheiten beschreiben dieselbe Größe; man sieht es durch Zurückführen auf Basiseinheiten:
> - `data-tex`: `1\,\dfrac{\mathrm V}{\mathrm m} = \dfrac{1\,\mathrm{J/C}}{1\,\mathrm m} = \dfrac{1\,\mathrm{N\cdot m}}{1\,\mathrm{C}\cdot 1\,\mathrm m} = 1\,\dfrac{\mathrm N}{\mathrm C}`
> - `data-plain`: `1 V/m = (1 J/C) / (1 m) = (1 N·m) / (1 C · 1 m) = 1 N/C`
>
> Welche Schreibweise man wählt, ist eine Frage des Zusammenhangs: **N/C** betont, dass die
> Feldstärke eine Kraftgröße ist; **V/m** betont, dass man sie im Kondensator als Spannung pro
> Länge misst. In diesem Modul steht überwiegend V/m, weil dort gerechnet wird.

**Beispielrechnung im Fließtext** (Kontrollrechnung K-4):

> Eine Punktladung <span class="m">Q = 1,0 nC</span> erzeugt im Abstand
> <span class="m">r = 5,0 cm</span> die Feldstärke
> - `data-tex`: `E = \dfrac{1}{4\pi\varepsilon_0}\cdot\dfrac{Q}{r^2} = 8{,}988\cdot10^{9}\,\dfrac{\mathrm{N\,m^2}}{\mathrm{C^2}}\cdot\dfrac{1{,}0\cdot10^{-9}\,\mathrm C}{(0{,}050\,\mathrm m)^2} = 3{,}6\cdot10^{3}\,\dfrac{\mathrm V}{\mathrm m}`
> - `data-plain`: `E = 1/(4π·ε₀) · Q/r² = 8,988·10⁹ N·m²/C² · 1,0·10⁻⁹ C / (0,050 m)² = 3,6·10³ V/m`
>
> Auf eine Probeladung von 1,0 nC wirkt dort die Kraft <span class="m">F = q·E = 3,6 µN</span>; auf
> eine doppelt so große Probeladung die doppelte Kraft — und der Quotient <span class="m">F/q</span>
> liefert wieder dieselben 3,6 kV/m. Genau das ist gemeint, wenn man sagt, die Feldstärke gehöre
> zum Ort und nicht zur Probeladung.

### 2.3 Das Feld einer Punktladung und die Superposition

**Fließtext:**

> Setzt man das Coulombgesetz in die Definition ein, erhält man das Feld einer einzelnen
> Punktladung:
>
> - `data-tex` (Blockformel): `E(r) = \dfrac{1}{4\pi\varepsilon_0}\cdot\dfrac{|Q|}{r^2}`
> - `data-plain`: `E(r) = 1/(4π·ε₀) · |Q| / r²`
>
> Das Feld zeigt bei positivem <span class="m">Q</span> radial nach außen, bei negativem radial nach
> innen. Sind mehrere Ladungen vorhanden, addieren sich ihre Felder **vektoriell**:
>
> - `data-tex` (Blockformel): `\vec{E}_{\text{ges}} = \vec{E}_1 + \vec{E}_2 + \ldots + \vec{E}_n`
> - `data-plain`: `E_ges = E₁ + E₂ + … + E_n`
>
> Dieses **Superpositionsprinzip** ist der Grund, warum man aus wenigen Grundbildern beliebig
> komplizierte Felder zusammensetzen kann — und warum das Feld zwischen zwei großen, entgegengesetzt
> geladenen Platten so übersichtlich ist: Jede Platte erzeugt für sich ein Feld; zwischen den Platten
> zeigen beide Beiträge in dieselbe Richtung und addieren sich, außerhalb heben sie sich auf. Warum
> jeder einzelne Beitrag vom Abstand unabhängig ist, klärt Abschnitt 3.1.

**Merksatz 2** (Titel *Superposition*):

> Felder addieren sich wie Vektoren, nicht wie Zahlen. Zwei gleich starke Felder können sich an
> einer Stelle zu null aufheben und an einer anderen verdoppeln. Wer nur Beträge addiert, bekommt
> beides falsch.

### 2.4 Feldlinien — was sie zeigen und was nicht

**Fließtext:**

> Ein Vektorfeld lässt sich nicht hinschreiben, ohne an jedem Punkt einen Pfeil zu zeichnen. Michael
> Faraday hat dafür die Feldlinie erfunden: eine Kurve, die überall in Richtung des Feldes verläuft.
> Aus dieser Definition folgen fünf Regeln, und jede davon ist eine Aussage über Physik, nicht über
> Zeichenstil.

**Tabelle** (Pflicht: in `<div class="tabelle">` kapseln):

| Regel | Begründung |
|---|---|
| Die **Tangente** an die Feldlinie gibt die Richtung von <span class="m">E⃗</span> und damit die Kraftrichtung auf eine positive Probeladung an. | Das ist die Definition der Feldlinie. |
| Feldlinien **beginnen an positiven und enden an negativen Ladungen** (oder im Unendlichen). | Ladungen sind Quellen und Senken des elektrostatischen Feldes. |
| Feldlinien **schneiden sich nie**. | In einem Schnittpunkt hätte das Feld zwei Richtungen; die Kraft auf eine Probeladung wäre nicht eindeutig. |
| Die **Liniendichte** ist ein Maß für den Betrag von <span class="m">E</span>: dichter heißt stärker. | Beim Radialfeld verteilen sich dieselben Linien auf die Kugelfläche <span class="m">4π·r²</span> — die Dichte fällt mit <span class="m">1/r²</span>, genau wie <span class="m">E</span>. |
| Feldlinien stehen im statischen Fall **senkrecht auf Leiteroberflächen**. | Eine Tangentialkomponente würde die frei beweglichen Ladungen im Leiter verschieben, und zwar so lange, bis sie verschwunden ist. Steht nichts mehr in Bewegung, ist auch die Tangentialkomponente null. |

**Zusatz im Fließtext:**

> Aus der letzten Regel folgt nebenbei, dass das Innere eines Leiters im statischen Fall feldfrei
> ist — das ist der faradaysche Käfig, der dich im Auto beim Gewitter schützt. Und aus der vierten
> Regel folgt, dass die Zahl der gezeichneten Linien willkürlich ist, ihr **Verhältnis** aber nicht:
> Doppelt so dichte Linien bedeuten die doppelte Feldstärke. In der Simulation in Abschnitt 4 ist
> genau das umgesetzt — dort wächst die Liniendichte proportional zur Feldstärke.

**Details-Block 2** — Zusammenfassung *Äquipotentiallinien: das zweite Bild desselben Feldes*:

> Verschiebt man eine Probeladung senkrecht zu den Feldlinien, so steht die Kraft senkrecht zum Weg
> und verrichtet **keine Arbeit**. Alle Punkte, die man auf diese Weise erreicht, haben dasselbe
> Potential; die Kurven, die sie verbinden, heißen Äquipotentiallinien (räumlich:
> Äquipotentialflächen).
>
> Daraus folgt sofort: **Äquipotentiallinien stehen überall senkrecht auf den Feldlinien.** Beim
> Radialfeld sind es konzentrische Kreise, im Plattenkondensator Parallelen zu den Platten. Und weil
> die Oberfläche eines Leiters im statischen Fall von Feldlinien senkrecht getroffen wird, ist sie
> selbst eine Äquipotentialfläche — deshalb darf man von *der* Spannung einer Platte sprechen, ohne
> zu sagen, an welcher Stelle der Platte man misst.
>
> Das Potential selbst ist die Energie pro Ladung:
> - `data-tex`: `\varphi = \dfrac{W}{q}, \qquad U_{12} = \varphi_1 - \varphi_2`
> - `data-plain`: `φ = W/q,   U₁₂ = φ₁ − φ₂`
>
> Eine Spannung ist also immer eine Potential*differenz* zwischen zwei Punkten. Den Nullpunkt des
> Potentials darf man frei wählen — üblich ist die Erde oder die negative Platte.

**Fehlvorstellung 1** (`<div class="hinweis">`, fett beginnend mit *Häufiger Fehler.*):

> **„Die Feldlinie zeigt, wohin sich die Ladung bewegt."** Das ist die verbreitetste Fehlvorstellung
> zum Feldlinienbild — und sie ist falsch. Die Tangente gibt die Richtung der **Kraft** an, nicht die
> der Geschwindigkeit. Eine Ladung, die mit einer Anfangsgeschwindigkeit quer ins Feld eintritt,
> folgt keiner Feldlinie, genauso wenig wie ein waagerecht geworfener Stein senkrecht nach unten
> fliegt. Nur ein einziger Fall ist harmlos: Startet die Ladung **aus der Ruhe** und sind die
> Feldlinien **gerade**, dann fällt die Bahn mit der Feldlinie zusammen. Genau das ist im
> Plattenkondensator der Fall — und es ist der Grund, warum sich die Fehlvorstellung so hartnäckig
> hält. Was bei schrägem Eintritt passiert, ist Thema des Folgemoduls.

**Fehlvorstellung 2** (zweiter `<div class="hinweis">` am Ende von Abschnitt 2):

> **Häufiger Fehler.** „Wo mehr Feldlinien gezeichnet sind, ist mehr Ladung." Nicht die absolute Zahl
> zählt, sondern die Dichte — und die Zahl selbst legt der Zeichner fest. Ein Feldlinienbild mit acht
> Linien und eines mit sechzehn können dasselbe Feld darstellen. Aussagekräftig ist immer nur der
> Vergleich **innerhalb eines Bildes**.

---

## 3 · Vertiefung — der Plattenkondensator

`<section id="vertiefung">`, `.stufe`-Nummer **3**,
Überschrift **Der Plattenkondensator: homogenes Feld, Kapazität, Energie**.

### 3.1 Das homogene Feld

**Fließtext:**

> Zwei parallele, entgegengesetzt geladene Metallplatten im Abstand <span class="m">d</span> erzeugen
> zwischen sich ein Feld, das überall dieselbe Richtung und denselben Betrag hat. Ein solches Feld
> heißt **homogen**, und sein Feldlinienbild besteht aus parallelen, gleichabständigen Linien von
> der positiven zur negativen Platte.
>
> Das gilt streng genommen nur im Innenbereich. An den Rändern wölben sich die Linien nach außen —
> das **Streufeld**. Die Näherung „homogen" ist gut, solange der Plattenabstand klein gegen die
> Plattenausdehnung ist, als Faustregel <span class="m">d ≲ L/10</span>. In der Simulation in
> Abschnitt 4 kannst du diesen Bereich bewusst verlassen; das Bild weist dann darauf hin.

**Merksatz 3** (Titel *Homogenes Feld*):

> Im homogenen Feld ist die Feldstärke an jeder Stelle gleich groß — dicht an der Platte genauso wie
> in der Mitte. In die Formel geht nicht der Abstand **von** einer Platte ein, sondern der Abstand
> **der** Platten voneinander.

**Fehlvorstellung 3** (`<div class="hinweis">`, direkt darunter):

> **Häufiger Fehler.** „Nahe an der geladenen Platte muss das Feld doch stärker sein — da sind die
> Ladungen ja." Beim Radialfeld einer Punktladung stimmt diese Intuition, beim Plattenkondensator
> nicht. Der Grund: Eine große geladene Platte erzeugt für sich das Feld <span class="m">E = σ/(2·ε₀)</span>,
> und das hängt vom Abstand zur Platte gar nicht ab. Entfernt man sich, wirkt zwar jedes einzelne
> Flächenelement schwächer (∼ 1/r²), dafür tragen entsprechend mehr Flächenelemente bei (∼ r²) —
> beides hebt sich exakt auf. Beide Platten zusammen ergeben zwischen sich überall
> <span class="m">E = σ/ε₀</span> und außerhalb null. Nur am Rand, wo die Platte nicht mehr groß gegen
> den Abstand ist, bricht dieses Argument zusammen — das ist das Streufeld.

### 3.2 Herleitung von E = U/d

Das ist die **erste vollständige Herleitung** des Moduls. Sie steht **nicht** im Fließtext, sondern
in einem `<details>`-Block mit der Zusammenfassung *Herleitung: warum E = U/d gilt*. Im Fließtext
steht davor nur das Ergebnis als Blockformel und ein Satz, dass die Begründung im Details-Block liegt.

**Blockformel im Fließtext:**

- `data-tex`: `E = \dfrac{U}{d}`
- `data-plain`: `E = U/d`

**Inhalt des Details-Blocks:**

> **Schritt 1 — Arbeit im homogenen Feld.**
> Wir schieben eine positive Probeladung <span class="m">q</span> von der negativen zur positiven
> Platte, also entgegen der Feldkraft, auf geradem Weg über die Strecke <span class="m">d</span>.
> Die Feldstärke ist unterwegs konstant, also ist auch die Kraft
> <span class="m">F = q·E</span> konstant, und die Arbeit ist Kraft mal Weg:
> - `data-tex`: `W = F \cdot d = q \cdot E \cdot d`
> - `data-plain`: `W = F · d = q · E · d`
>
> **Schritt 2 — Definition der Spannung.**
> Die Spannung zwischen zwei Punkten ist die pro Ladung umgesetzte Energie (das war Vorwissensfrage
> vw2):
> - `data-tex`: `U = \dfrac{W}{q}`
> - `data-plain`: `U = W/q`
>
> **Schritt 3 — Zusammensetzen.**
> Einsetzen von Schritt 1 in Schritt 2:
> - `data-tex`: `U = \dfrac{q \cdot E \cdot d}{q} = E \cdot d \quad \Longrightarrow \quad E = \dfrac{U}{d}`
> - `data-plain`: `U = (q · E · d)/q = E · d   ⟹   E = U/d`
>
> Die Probeladung kürzt sich heraus — das muss so sein, denn sonst hinge die Feldstärke davon ab,
> womit man sie misst.
>
> **Schritt 4 — Einheitenprobe.**
> <span class="m">[U]/[d] = V/m</span>, und in 2.2 wurde gezeigt, dass
> <span class="m">1 V/m = 1 N/C</span> ist. Die Einheit passt also zur Definition
> <span class="m">E = F/q</span>. ✓
>
> **Warum die Wegunabhängigkeit wichtig ist.** In Schritt 1 wurde der gerade Weg senkrecht zu den
> Platten gewählt. Nimmt man stattdessen einen schrägen Weg, so ist die Wegstrecke länger, aber es
> zählt nur die Komponente längs der Kraft — dasselbe Argument wie bei der schiefen Ebene in
> Vorwissensfrage vw3. Das Ergebnis ist identisch. Genau deshalb darf man jedem Punkt im Feld ein
> Potential zuordnen.

**Zahlenbeispiel direkt hinter dem Details-Block:**

> Ein Plattenkondensator mit <span class="m">d = 20 mm</span> liegt an
> <span class="m">U = 200 V</span>. Dann ist
> <span class="m">E = 200 V / 0,020 m = 10 000 V/m = 10 kV/m</span>. Zum Vergleich: Ab etwa
> <span class="m">3 · 10⁶ V/m</span> wird trockene Luft leitend und es schlägt ein Funke über. Bei
> 20 mm Abstand wäre das bei rund 60 kV der Fall — der Aufbau ist also weit im sicheren Bereich.

### 3.3 Die Kapazität

**Fließtext:**

> Lädt man einen Kondensator mit verschiedenen Spannungen auf und misst jedes Mal die Ladung auf den
> Platten, so liegen die Messpunkte im <span class="m">Q</span>-<span class="m">U</span>-Diagramm auf
> einer **Ursprungsgeraden**. Ladung und Spannung sind zueinander proportional. Die Steigung dieser
> Geraden ist eine Eigenschaft des Bauteils und heißt **Kapazität**:
>
> - `data-tex` (Blockformel): `C = \dfrac{Q}{U} \qquad [C] = 1\,\dfrac{\mathrm C}{\mathrm V} = 1\,\mathrm F\ \text{(Farad)}`
> - `data-plain`: `C = Q/U     [C] = 1 C/V = 1 F (Farad)`
>
> Ein Farad ist eine gewaltige Kapazität: Ein Kondensator mit 1 F trüge bei 1 V die Ladung 1 C, also
> rund 6 · 10¹⁸ Elementarladungen. Übliche Bauteile liegen bei **pF** (Hochfrequenztechnik,
> Touchscreen), **nF** (Folienkondensatoren) und **µF bis mF** (Elektrolytkondensatoren im Netzteil).

**Fehlvorstellung 4 — die zentrale Fehlvorstellung dieses Moduls**
(`<div class="hinweis">`, direkt hinter der Definition):

> **Häufiger Fehler.** „In <span class="m">C = Q/U</span> stehen <span class="m">Q</span> und
> <span class="m">U</span> — also hängt die Kapazität davon ab, wie viel Ladung drauf ist und welche
> Spannung anliegt." Nein, und zwar aus demselben Grund, aus dem der elektrische Widerstand
> <span class="m">R = U/I</span> nicht von der Stromstärke abhängt: Die Formel ist eine
> **Messvorschrift** für eine Größe, die bei diesem Bauteil **konstant** ist. Verdoppelst du die
> Spannung, verdoppelt sich die Ladung mit — der Quotient bleibt derselbe. Genau das ist die Aussage
> der Ursprungsgeraden im <span class="m">Q</span>-<span class="m">U</span>-Diagramm. Was die
> Kapazität wirklich festlegt, ist die **Geometrie** des Bauteils, und das steht im nächsten Absatz.
>
> Prüf es an dir selbst: Wenn <span class="m">C</span> mit <span class="m">U</span> wachsen würde,
> wäre die Q-U-Kennlinie keine Gerade — und die Energieformel
> <span class="m">W = ½·C·U²</span> aus 3.5 wäre falsch.

### 3.4 Die Kapazität des Plattenkondensators

**Fließtext:**

> Was genau die Kapazität festlegt, zeigt eine Messreihe mit verschiebbaren Platten. Zwei Befunde:
>
> 1. Verdoppelt man die **Plattenfläche** <span class="m">A</span>, verdoppelt sich
>    <span class="m">C</span>: <span class="m">C ∼ A</span>.
> 2. Verdoppelt man den **Plattenabstand** <span class="m">d</span>, halbiert sich
>    <span class="m">C</span>: <span class="m">C ∼ 1/d</span>.
>
> Zusammen also <span class="m">C ∼ A/d</span>. Die Proportionalitätskonstante ist eine
> Naturkonstante, die elektrische Feldkonstante <span class="m">ε₀</span>. Füllt man den Zwischenraum
> mit einem Isolator (einem **Dielektrikum**), steigt die Kapazität noch einmal um dessen
> Permittivitätszahl <span class="m">ε_r</span>:
>
> - `data-tex` (Blockformel): `C = \varepsilon_0 \cdot \varepsilon_r \cdot \dfrac{A}{d}`
> - `data-plain`: `C = ε₀ · ε_r · A/d`

**Tabelle Permittivitätszahlen** (in `<div class="tabelle">` kapseln; Werte sind Richtwerte bei
Zimmertemperatur und niedriger Frequenz):

| Stoff im Plattenzwischenraum | <span class="m">ε_r</span> |
|---|---|
| Vakuum (exakt), trockene Luft (auf drei Stellen) | 1,00 |
| Papier, Hartpapier | 2,0 bis 2,5 |
| Polyethylen (PE-Folie) | 2,3 |
| Glas | 5 bis 10 |
| destilliertes Wasser | ≈ 80 |

**Details-Block 3** — Zusammenfassung *Herleitung: Warum im Kondensator E = σ/ε₀ gilt — und warum
das die wichtigste Nebenformel des Kapitels ist*:

> Aus den beiden Formeln <span class="m">C = ε₀·ε_r·A/d</span> und <span class="m">E = U/d</span>
> lässt sich ein Ausdruck gewinnen, in dem der Plattenabstand **nicht mehr vorkommt**:
>
> **Schritt 1.** Aus <span class="m">C = Q/U</span> folgt <span class="m">U = Q/C</span>.
>
> **Schritt 2.** Einsetzen in <span class="m">E = U/d</span>:
> - `data-tex`: `E = \dfrac{U}{d} = \dfrac{Q}{C \cdot d}`
> - `data-plain`: `E = U/d = Q/(C · d)`
>
> **Schritt 3.** Für <span class="m">C</span> die Plattenkondensatorformel einsetzen:
> - `data-tex`: `E = \dfrac{Q}{\dfrac{\varepsilon_0 \varepsilon_r A}{d} \cdot d} = \dfrac{Q}{\varepsilon_0 \varepsilon_r A}`
> - `data-plain`: `E = Q / ((ε₀·ε_r·A/d) · d) = Q / (ε₀·ε_r·A)`
>
> **Schritt 4.** Mit der Flächenladungsdichte <span class="m">σ = Q/A</span>:
> - `data-tex`: `E = \dfrac{\sigma}{\varepsilon_0 \varepsilon_r}`
> - `data-plain`: `E = σ / (ε₀·ε_r)`
>
> **Was daran wichtig ist:** Der Plattenabstand ist herausgefallen. Solange die **Ladung** auf den
> Platten festliegt, ändert ein Verschieben der Platten die Feldstärke **nicht**. Das klingt
> zunächst paradox — <span class="m">E = U/d</span> hat doch ein <span class="m">d</span> im Nenner.
> Der Widerspruch löst sich auf, sobald man dazusagt, *was* festgehalten wird: Bei konstanter
> Spannung ist <span class="m">E ∼ 1/d</span>, bei konstanter Ladung ist <span class="m">E</span>
> konstant, weil dann <span class="m">U</span> proportional zu <span class="m">d</span> mitwächst.
> Genau diesen Unterschied zeigt die Simulation, und genau daran scheitern im Abitur die meisten
> Punkte.
>
> Probe mit den Startwerten der Simulation: <span class="m">Q = 3,5416 nC</span>,
> <span class="m">A = 400 cm² = 0,0400 m²</span>, <span class="m">ε_r = 1</span>:
> <span class="m">σ = 8,854 · 10⁻⁸ C/m²</span> und
> <span class="m">E = σ/ε₀ = 8,854·10⁻⁸ / 8,854·10⁻¹² = 10 000 V/m</span> — derselbe Wert wie über
> <span class="m">U/d = 200 V / 0,020 m</span>. ✓

### 3.5 Die Energie des geladenen Kondensators

Das ist die **zweite vollständige Herleitung**, ebenfalls in einem `<details>`-Block mit der
Zusammenfassung *Herleitung: Woher der Faktor ½ in W = ½·C·U² kommt*.

**Blockformel im Fließtext (alle drei Formen):**

- `data-tex`: `W = \tfrac{1}{2} \cdot C \cdot U^2 = \tfrac{1}{2} \cdot Q \cdot U = \dfrac{Q^2}{2 \cdot C}`
- `data-plain`: `W = ½ · C · U² = ½ · Q · U = Q² / (2 · C)`

Im Fließtext steht dazu der Hinweis, welche Form wann praktisch ist:

| Form | Praktisch, wenn … |
|---|---|
| <span class="m">W = ½·C·U²</span> | die **Spannung** festgehalten wird (Quelle bleibt angeschlossen) |
| <span class="m">W = Q²/(2C)</span> | die **Ladung** festgehalten wird (Quelle abgetrennt) |
| <span class="m">W = ½·Q·U</span> | beide Größen bekannt sind und man schnell rechnen will |

**Inhalt des Details-Blocks:**

> **Der naive Ansatz und warum er scheitert.** Man könnte meinen, die Energie sei
> <span class="m">W = Q·U</span>: Ladung mal Spannung, so wie Arbeit gleich Kraft mal Weg. Das ist
> zu viel, und zwar genau um den Faktor 2. Der Grund: Beim Aufladen ist die Spannung **nicht die
> ganze Zeit über** <span class="m">U</span>. Am Anfang ist der Kondensator leer, die Spannung ist
> null, die erste Ladungsportion kostet praktisch keine Arbeit. Je voller er wird, desto mehr
> Gegenspannung ist zu überwinden.
>
> **Schritt 1 — Arbeit für eine kleine Ladungsportion.**
> Sitzt bereits die Ladung <span class="m">q</span> auf den Platten, so liegt die Spannung
> <span class="m">u = q/C</span> an. Um die kleine Portion <span class="m">dq</span>
> nachzuschieben, ist die Arbeit
> - `data-tex`: `\mathrm{d}W = u \cdot \mathrm{d}q = \dfrac{q}{C}\,\mathrm{d}q`
> - `data-plain`: `dW = u · dq = (q/C) · dq`
>
> nötig.
>
> **Schritt 2 — Aufsummieren von 0 bis Q.**
> - `data-tex`: `W = \int_0^{Q} \dfrac{q}{C}\,\mathrm{d}q = \dfrac{1}{C}\left[\dfrac{q^2}{2}\right]_0^{Q} = \dfrac{Q^2}{2C}`
> - `data-plain`: `W = ∫₀^Q (q/C) dq = (1/C) · [q²/2]₀^Q = Q²/(2C)`
>
> **Schritt 3 — Umformen mit Q = C·U.**
> - `data-tex`: `W = \dfrac{Q^2}{2C} = \dfrac{(C \cdot U)^2}{2C} = \tfrac{1}{2}\,C\,U^2 = \tfrac{1}{2}\,Q\,U`
> - `data-plain`: `W = Q²/(2C) = (C·U)²/(2C) = ½·C·U² = ½·Q·U`
>
> **Der Faktor ½ ohne Integral.** Wer das Integral nicht benutzen will, liest dieselbe Rechnung im
> <span class="m">Q</span>-<span class="m">U</span>-Diagramm ab: Die Arbeit ist die **Fläche unter
> der Q-U-Geraden**, und die Fläche unter einer Ursprungsgeraden ist ein **Dreieck**, nicht ein
> Rechteck — daher <span class="m">½·Q·U</span> statt <span class="m">Q·U</span>. Der Faktor ½ ist
> nichts anderes als „mittlere Spannung ist die halbe Endspannung". In der Simulation ist diese
> Dreiecksfläche eingezeichnet und wächst mit.
>
> **Wo die fehlende Hälfte bleibt.** Lädt man einen Kondensator über einen Widerstand an einer
> Spannungsquelle mit konstanter Spannung <span class="m">U</span> auf, so liefert die Quelle die
> Energie <span class="m">Q·U</span>. Im Kondensator landet nur <span class="m">½·Q·U</span>; die
> andere Hälfte wird im Widerstand in Wärme umgesetzt — unabhängig davon, wie groß der Widerstand
> ist. Diese Aussage ist berühmt und wird im Modul zur RC-Schaltung nachgerechnet; hier genügt sie
> als Beleg, dass die halbe Energie nicht „verschwindet".

**Zahlenbeispiel im Fließtext** (Kontrollrechnung K-6):

> Die Startwerte der Simulation: <span class="m">C = 17,7 pF</span> bei
> <span class="m">U = 200 V</span> ergeben
> <span class="m">W = ½ · 17,708 · 10⁻¹² F · (200 V)² = 3,54 · 10⁻⁷ J = 0,354 µJ</span>. Das ist
> verschwindend wenig — der Defibrillator aus dem Einstieg speichert mit 200 J das
> Sechshundertmillionenfache. Der Unterschied steckt fast vollständig in der Kapazität: 100 µF statt
> 17,7 pF ist ein Faktor von rund 5,6 Millionen, und die zehnfache Spannung bringt noch einmal
> hundert.

### 3.6 Wo sitzt die Energie?

**Fließtext:**

> Naheliegende Antwort: auf den Platten, bei der Ladung. Die Physik gibt eine andere: **im Feld
> dazwischen**. Man sieht das, wenn man die Energie durch das Volumen des Feldraums teilt, das beim
> Plattenkondensator <span class="m">V = A · d</span> beträgt:
>
> - `data-tex` (Blockformel): `w = \dfrac{W}{A \cdot d} = \dfrac{\frac{1}{2}\,\varepsilon_0 \varepsilon_r \frac{A}{d}\,(E d)^2}{A\,d} = \tfrac{1}{2}\,\varepsilon_0\,\varepsilon_r\,E^2`
> - `data-plain`: `w = W/(A·d) = [½·ε₀·ε_r·(A/d)·(E·d)²] / (A·d) = ½·ε₀·ε_r·E²`
>
> Die Geometrie ist vollständig herausgefallen. Übrig bleibt eine Größe, die nur noch von der
> Feldstärke an der betrachteten Stelle abhängt: die **Energiedichte** in J/m³. Das ist mehr als
> eine Umformung — es ist die Aussage, dass man der Energie einen **Ort** geben kann, nämlich den
> Raum, in dem das Feld steht. Dieselbe Rechnung führt später beim Magnetfeld auf
> <span class="m">w = B²/(2µ₀)</span>, und beide zusammen ergeben die Energie einer
> elektromagnetischen Welle, die sich durch den leeren Raum bewegt, ganz ohne Ladung in der Nähe.

**Merksatz 4** (Titel *Die Energie sitzt im Feld*):

> Ein geladener Kondensator speichert seine Energie nicht „auf den Platten", sondern im Feldraum
> zwischen ihnen, mit der Dichte <span class="m">w = ½·ε₀·ε_r·E²</span>. Deshalb ist die Energie
> weg, sobald das Feld zusammenbricht — und deshalb ist das Feld mehr als eine Rechenhilfe.

**Zahlenbeispiel** (K-6): Startwerte der Simulation, <span class="m">E = 10 kV/m</span>:
<span class="m">w = ½ · 8,854·10⁻¹² F/m · (10⁴ V/m)² = 4,43 · 10⁻⁴ J/m³</span>. Mal dem
Feldvolumen <span class="m">V = 0,0400 m² · 0,020 m = 8,0 · 10⁻⁴ m³</span> ergibt das
<span class="m">3,54 · 10⁻⁷ J</span> — genau die Energie aus 3.5. ✓

### 3.7 Die entscheidende Fallunterscheidung: angeschlossen oder abgetrennt

**Fließtext:**

> Fast jede Kondensatoraufgabe, die über das Einsetzen hinausgeht, hängt an einer einzigen Frage:
> **Was wird festgehalten?** Es gibt genau zwei Fälle, und sie führen bei derselben mechanischen
> Handlung zu entgegengesetzten Ergebnissen.

**Tabelle** (Pflicht: `<div class="tabelle">`; das ist eine Fünfspaltentabelle, sie **muss**
gekapselt werden):

| Größe | **Quelle angeschlossen** (<span class="m">U</span> fest) | **Quelle abgetrennt** (<span class="m">Q</span> fest) |
|---|---|---|
| Spannung <span class="m">U</span> | bleibt | <span class="m">U = Q/C</span>, ändert sich mit |
| Ladung <span class="m">Q</span> | <span class="m">Q = C·U</span>, fließt nach oder ab | bleibt (kein Stromweg) |
| Feldstärke <span class="m">E</span> | <span class="m">E = U/d</span> | <span class="m">E = σ/(ε₀ε_r)</span>, hängt **nicht** von <span class="m">d</span> ab |
| Energie <span class="m">W</span> | <span class="m">W = ½·C·U²</span>, wächst mit <span class="m">C</span> | <span class="m">W = Q²/(2C)</span>, fällt mit <span class="m">C</span> |
| Woher/wohin die Energie | Quelle liefert bzw. nimmt zurück | mechanische Arbeit von außen bzw. Arbeit des Feldes |

**Konkretes Beispiel, das im Beobachtungsauftrag wiederkehrt** (K-9):

> Ausgangslage in beiden Fällen: <span class="m">A = 400 cm²</span>,
> <span class="m">d = 20 mm</span>, <span class="m">U = 200 V</span>, Luft. Also
> <span class="m">C = 17,7 pF</span>, <span class="m">Q = 3,54 nC</span>,
> <span class="m">E = 10,0 kV/m</span>, <span class="m">W = 0,354 µJ</span>.
> Nun wird der Plattenabstand auf 40 mm verdoppelt:

| nach dem Verdoppeln von <span class="m">d</span> | angeschlossen | abgetrennt |
|---|---|---|
| <span class="m">C</span> | 8,85 pF | 8,85 pF |
| <span class="m">U</span> | 200 V (fest) | 400 V |
| <span class="m">Q</span> | 1,77 nC | 3,54 nC (fest) |
| <span class="m">E</span> | 5,00 kV/m | 10,0 kV/m (unverändert!) |
| <span class="m">W</span> | 0,177 µJ (halbiert) | 0,708 µJ (verdoppelt) |

**Details-Block 4** — Zusammenfassung *Woher die Energie kommt, wenn man die Platten auseinanderzieht*:

> Bei abgetrennter Quelle verdoppelt sich die gespeicherte Energie, obwohl niemand Ladung nachliefert.
> Die Energie kommt aus der **mechanischen Arbeit**, die man gegen die Anziehung der beiden
> entgegengesetzt geladenen Platten verrichtet. Man kann das nachrechnen:
>
> **Kraft auf eine Platte.** Eine Platte spürt nicht das Gesamtfeld, sondern nur das Feld der
> *anderen* Platte, und das ist halb so groß wie das Gesamtfeld. Deshalb gilt
> - `data-tex`: `F = \tfrac{1}{2}\,Q\,E = \dfrac{Q^2}{2\,\varepsilon_0 \varepsilon_r A}`
> - `data-plain`: `F = ½ · Q · E = Q² / (2 · ε₀ · ε_r · A)`
>
> Dieser Ausdruck hängt **nicht** vom Abstand ab — die Kraft ist beim Auseinanderziehen konstant.
> Mit den Zahlen von oben: <span class="m">F = ½ · 3,5416 nC · 10 000 V/m = 17,7 µN</span>.
>
> **Arbeit über 20 mm:** <span class="m">W = F · Δd = 17,708 µN · 0,020 m = 0,354 µJ</span>. Und
> genau um diesen Betrag ist die Feldenergie gestiegen (von 0,354 µJ auf 0,708 µJ). Die Energiebilanz
> geht exakt auf — das ist die Kontrolle, an der man merkt, dass die Formeln zusammenpassen.
>
> Denselben Ausdruck bekommt man auch ohne Kraftbetrachtung, direkt aus der Energie: Mit
> <span class="m">W(d) = Q²·d / (2·ε₀·ε_r·A)</span> ist
> <span class="m">F = dW/dd = Q² / (2·ε₀·ε_r·A)</span>. Kraft ist die Ableitung der Energie nach dem
> Weg — derselbe Zusammenhang wie zwischen Hubarbeit und Gewichtskraft.

---

## 4 · Interaktiver Kern — der Plattenkondensator als Simulation

`<section id="simulation">`, `.stufe`-Nummer **4**,
Überschrift **Der Plattenkondensator im Griff**.

Einleitender Absatz über der Simulation:

> Die Simulation zeigt einen Plattenkondensator im Querschnitt: links die positive, rechts die
> negative Platte, dazwischen die Feldlinien. Du kannst Spannung, Plattenabstand, Plattengröße und
> das Material zwischen den Platten einstellen — und vor allem entscheiden, ob die Spannungsquelle
> angeschlossen bleibt oder abgetrennt wird. Darunter laufen zwei Diagramme mit: die Kapazität in
> Abhängigkeit vom Plattenabstand und die Kennlinie <span class="m">Q(U)</span>, deren
> Dreiecksfläche die gespeicherte Energie ist.

### 4.1 Was die Simulation rechnet

Alle Rechnungen intern in **SI-Einheiten**, Umrechnung erst bei der Anzeige.

| Schritt | Formel | Bemerkung |
|---|---|---|
| Fläche | <span class="m">A = (L/100)²</span> | L in cm vom Regler, A in m² |
| Kapazität | <span class="m">C = ε₀·ε_r·A/d</span> | d in m (Regler liefert mm) |
| Modus **Quelle angeschlossen** | <span class="m">U = U_Regler</span>, <span class="m">Q = C·U</span> | |
| Modus **Quelle abgetrennt** | <span class="m">Q = Q_fest</span>, <span class="m">U = Q/C</span> | Q_fest wird beim Umschalten eingefroren |
| Feldstärke | <span class="m">E = U/d</span> | gleichwertig <span class="m">E = Q/(ε₀·ε_r·A)</span> |
| Energie | <span class="m">W = ½·C·U²</span> | gleichwertig <span class="m">W = Q²/(2C)</span> |
| Flächenladungsdichte | <span class="m">σ = Q/A</span> | nur intern, für die Kontrolle |

Formeln für den Seitentext über der Simulation:
- `data-tex`: `C = \varepsilon_0\varepsilon_r\dfrac{A}{d}, \quad Q = C\,U, \quad E = \dfrac{U}{d}, \quad W = \tfrac{1}{2}CU^2`
- `data-plain`: `C = ε₀·ε_r·A/d,  Q = C·U,  E = U/d,  W = ½·C·U²`

**Selbstkontrolle für den Bauagenten** (muss nach dem Bau stichprobenartig stimmen, K-6):
Startwerte <span class="m">U = 200 V</span>, <span class="m">d = 20 mm</span>,
<span class="m">L = 20 cm</span>, Luft liefern **exakt**
<span class="m">C = 17,708 pF</span> · <span class="m">Q = 3,5416 nC</span> ·
<span class="m">E = 10,00 kV/m</span> · <span class="m">W = 0,3542 µJ</span>.
Weicht die Anzeige in der zweiten Nachkommastelle ab, ist ein Umrechnungsfaktor falsch.

### 4.2 Regler und Bedienelemente — vollständige Liste

Alle Regler in `<div class="regler">`, alle Knöpfe in `<div class="knopfleiste">`.

| Element | `id` | Bereich | Schritt | Startwert | Beschriftung |
|---|---|---|---|---|---|
| Spannung <span class="m">U</span> | `rU` | 0 … 500 | 10 | **200** | `Spannung U <b><span id="lU">200</span> V</b>` |
| Plattenabstand <span class="m">d</span> | `rD` | 5 … 50 | 1 | **20** | `Plattenabstand d <b><span id="lD">20</span> mm</b>` |
| Kantenlänge <span class="m">L</span> | `rL` | 10 … 30 | 1 | **20** | `Kantenlänge L <b><span id="lL">20</span> cm</b> (A = <span id="lA">400</span> cm²)` |

Der Regler `rL` steuert die **Kantenlänge einer quadratischen Platte**, nicht die Fläche. Die
Fläche wird daneben mitangezeigt, damit der quadratische Zusammenhang sichtbar bleibt
(<span class="m">L = 10 cm → A = 100 cm²</span>, <span class="m">L = 30 cm → A = 900 cm²</span>).

**Knöpfe:**

| Knopf | `data-`Attribut | Wirkung |
|---|---|---|
| „Luft (ε_r = 1,00)" | `data-eps="1.00"` | Dielektrikum wechseln, Knopf wird aktiv markiert |
| „Papier (ε_r = 2,20)" | `data-eps="2.20"` | " |
| „Glas (ε_r = 6,00)" | `data-eps="6.00"` | " |
| „Quelle angeschlossen" | `data-modus="quelle"` | U fest, Q folgt |
| „Quelle abgetrennt" | `data-modus="isoliert"` | Q wird eingefroren, U folgt |
| „Zurücksetzen" | `id="bReset"` | alle Startwerte, Modus `quelle` |

Der jeweils aktive Knopf jeder Gruppe bekommt die Klasse `primaer`, die anderen verlieren sie.

**Modus-Logik — verbindlich:**

1. Beim Wechsel auf `isoliert` wird <span class="m">Q_fest = C · U</span> **einmal** gespeichert.
2. Solange `isoliert` gilt, folgt <span class="m">U = Q_fest / C</span> aus der Geometrie. Die
   Beschriftung des Spannungsreglers zeigt dann den **gerechneten** Wert und dahinter in Klammern
   *(folgt aus Q)*.
3. **Bewegt der Nutzer den Spannungsregler im Modus `isoliert`, springt die Simulation automatisch
   zurück in den Modus `quelle`** und zeigt im Hinweisfeld: *„Du hast die Quelle wieder
   angeschlossen — ab jetzt ist U fest und die Ladung folgt."* Kein Regler wird jemals `disabled`
   gesetzt; ein totes Bedienelement wäre ein Mangel im Modulcheck.
4. `Zurücksetzen` stellt Modus `quelle`, U = 200 V, d = 20 mm, L = 20 cm, Luft wieder her.

### 4.3 Anzeigefeld

`<div class="anzeige">` mit fünf Feldern, alle Zahlen über `fmt(zahl, stellen)` mit Komma:

| Beschriftung | `id` | Einheit | Stellen | Startwert |
|---|---|---|---|---|
| Kapazität C | `aC` | pF | 2 | 17,71 pF |
| Ladung Q | `aQ` | nC | 3 | 3,542 nC |
| Spannung U | `aU` | V | 1 | 200,0 V |
| Feldstärke E | `aE` | kV/m | 2 | 10,00 kV/m |
| Energie W | `aW` | µJ | 4 | 0,3542 µJ |

**Umschaltung der Einheit bei großen Werten** (Codeformel der HTML-Datei):
`aE` zeigt ab <span class="m">E ≥ 10⁶ V/m</span> die Feldstärke als `fmt(E/10⁶, 2)` in **MV/m**, sonst
`fmt(E/1000, 2)` in kV/m; `aW` zeigt ab <span class="m">W ≥ 10⁻³ J</span> die Energie als
`fmt(W·10³, 3)` in **mJ**, sonst `fmt(W·10⁶, 4)` in µJ. Kontrolle (Python, ε₀ = 8,854·10⁻¹² F/m):
größter Wert im Modus `quelle` ist E = 500 V/0,005 m = 100 kV/m und
W = ½·(8,854·10⁻¹²·6·0,09/0,005 F)·(500 V)² = 119,5 µJ, bleibt also in kV/m und µJ; die Umschaltung
greift erst im Modus `isoliert` (Beispiel: Q = 500 V·C_max, danach Luft und L = 10 cm:
E = Q/(ε₀·A) ≈ 5,4 MV/m, Anzeige „5,40 MV/m").

Zusätzlich ein Hinweisfeld `<p id="simHinweis">` unter der Knopfleiste für die drei Meldungen aus
4.5 (Randfeld, Durchschlag, Moduswechsel). Es ist leer, solange nichts zu melden ist.

### 4.4 Canvas 1 — der Kondensator im Querschnitt

`<canvas id="cvKond" width="1000" height="360">`

**Maßstäbe — hier wird bewusst mit zwei verschiedenen gearbeitet:**

| Richtung | Maßstab | Begründung |
|---|---|---|
| senkrecht (Plattenhöhe <span class="m">L</span>) | **10 px/cm** → 100 px bei L = 10 cm, 300 px bei L = 30 cm | passt in die Canvashöhe |
| waagerecht (Plattenabstand <span class="m">d</span>) | **5 px/mm = 50 px/cm** → 25 px bei d = 5 mm, 250 px bei d = 50 mm | bei gleichem Maßstab wäre der Abstand 5 px breit und man sähe keine Feldlinien |

Das ist eine **fünffache Überhöhung der waagerechten Richtung**. Sie muss im Bild dranstehen:
unten links ein waagerechter Maßstabsbalken von 50 px mit der Beschriftung „10 mm" und daneben ein
senkrechter Balken von 50 px mit „5 cm", darunter in Grau der Satz
*„Plattenabstand fünffach überhöht dargestellt"*. Ohne diese Beschriftung ist die Abbildung
irreführend und gilt als Mangel.

Für die **Feldliniendichte** ist die Überhöhung unschädlich: Die Dichte wird in senkrechter
Richtung abgelesen (Linien pro Höhe), und diese Richtung ist maßstäblich.

**Bildaufbau** (Mittelpunkt <span class="m">x_m = 500</span>, <span class="m">y_m = 175</span>):

| Element | Geometrie | Farbe |
|---|---|---|
| positive Platte | Rechteck, Breite 7 px, Höhe <span class="m">h = 10·L</span> px, rechte Kante bei <span class="m">x_m − 2,5·d</span> | `#dc2626` |
| negative Platte | Rechteck, Breite 7 px, Höhe <span class="m">h</span>, linke Kante bei <span class="m">x_m + 2,5·d</span> | `#1d4ed8` |
| Dielektrikum (nur bei <span class="m">ε_r > 1</span>) | füllt den Raum zwischen den Platten, volle Höhe <span class="m">h</span> | Fläche `#e0f2fe`, Rand `#7dd3fc`, Beschriftung mittig unten `ε_r = 2,20` |
| Feldlinien | <span class="m">n</span> waagerechte Linien, gleichmäßig über <span class="m">h</span> verteilt: <span class="m">y_i = y_m − h/2 + (i + ½)·h/n</span>, jeweils von Plattenkante zu Plattenkante, Pfeilspitze in der Mitte, Richtung **nach rechts** | `#334155`, 2 px |
| Ladungssymbole | je <span class="m">n</span> Stück auf beiden Platten, auf denselben Höhen <span class="m">y_i</span>: links `+`, rechts `−` | Plattenfarbe, 15 px Schrift |
| Äquipotentiallinie | eine gestrichelte senkrechte Linie in der Mitte zwischen den Platten, Beschriftung „Äquipotentiallinie" | `#0d7a52` |
| Beschriftungen | `+U` an der linken Platte, `0 V` an der rechten, `d` als Doppelpfeil unten zwischen den Platten, `L` als Doppelpfeil links neben der positiven Platte | `#475569` |

**Zahl der Feldlinien — die didaktisch entscheidende Festlegung:**

- `data-tex`: `n = \mathrm{clamp}\!\left(\mathrm{round}\!\left(\dfrac{E \cdot L}{400\,\mathrm V}\right),\,1,\,26\right)`
- `data-plain`: `n = clamp(round(E · L / 400 V), 1, 26)`

mit <span class="m">E</span> in V/m und <span class="m">L</span> in m; bei
<span class="m">U = 0</span> ist <span class="m">n = 0</span> (keine Linien, kein Feld).

Damit ist die **Liniendichte** <span class="m">n/L = E/400 V</span> proportional zur Feldstärke —
genau die Regel aus 2.4. Kontrollwerte (K-8):

| U | d | L | E | n |
|---|---|---|---|---|
| 200 V | 20 mm | 20 cm | 10,0 kV/m | **5** |
| 400 V | 20 mm | 20 cm | 20,0 kV/m | **10** |
| 200 V | 10 mm | 20 cm | 20,0 kV/m | **10** |
| 500 V | 5 mm | 20 cm | 100 kV/m | **26** (gedeckelt) |
| 50 V | 50 mm | 10 cm | 1,0 kV/m | **1** |
| 0 V | 20 mm | 20 cm | 0 | **0** |

Die Deckelung bei 26 Linien ist nötig, weil das Bild sonst zuläuft. **Sie muss sichtbar gemacht
werden:** Sobald gedeckelt wird, erscheint im Hinweisfeld
*„Ab hier ist die Zahl der Feldlinien gedeckelt — der angezeigte Zahlenwert von E gilt weiter."*
Sonst zieht jemand den Schluss, die Feldstärke ließe sich nicht weiter steigern.

### 4.5 Die drei Meldungen im Hinweisfeld

| Bedingung | Text |
|---|---|
| <span class="m">d_mm > L_cm</span> (gleichbedeutend mit <span class="m">d > L/10</span>) | „Der Plattenabstand ist jetzt größer als ein Zehntel der Plattenhöhe. Am Rand wölbt sich das Feld nach außen; die angezeigten Werte gelten für den idealisierten homogenen Fall." Zusätzlich werden an den Plattenkanten vier gestrichelte, nach außen gebogene Randlinien gezeichnet. |
| <span class="m">E > 3·10⁶ V/m</span> | „Bei dieser Feldstärke würde in Luft ein Funke überschlagen — der Kondensator wäre in Wirklichkeit entladen." Die Feldlinien werden dann in Orange `#b45309` gezeichnet. |
| Spannungsregler im Modus `isoliert` bewegt | „Du hast die Quelle wieder angeschlossen — ab jetzt ist U fest und die Ladung folgt." |

Die Durchschlagsmeldung ist im Modus `quelle` nie erreichbar (dort ist
<span class="m">E ≤ 500 V / 0,005 m = 100 kV/m</span>), wohl aber im Modus `isoliert`: Friert man
bei kleiner Platte und Glas eine große Ladung ein und wechselt dann auf Luft und kleine Fläche,
steigt <span class="m">E = Q/(ε₀·ε_r·A)</span> um bis zu Faktor 54. Genau dieser Fall ist
physikalisch lehrreich und soll nicht unterdrückt, sondern kommentiert werden.

### 4.6 Canvas 2 — das C-d-Diagramm

`<canvas id="cvCd" width="1000" height="200">`

| Achse | Bereich | Beschriftung |
|---|---|---|
| waagerecht | <span class="m">d</span> von 0 bis 55 mm | „Plattenabstand d in mm" |
| senkrecht | <span class="m">C</span> von 0 bis <span class="m">C_plot</span> | „Kapazität C in pF" |

<span class="m">C_plot</span> ist <span class="m">C(d = 5 mm)</span> für die aktuellen Werte von
<span class="m">A</span> und <span class="m">ε_r</span>, aufgerundet auf die nächste Zahl der Form
1 · 10ⁿ, 2 · 10ⁿ oder 5 · 10ⁿ. Die Kurve <span class="m">C(d) = ε₀·ε_r·A/d</span> wird von
<span class="m">d = 5 mm</span> bis <span class="m">d = 50 mm</span> gezeichnet (außerhalb des
Reglerbereichs nicht), der Arbeitspunkt als gefüllter Kreis mit gestrichelten Hilfslinien zu beiden
Achsen. Über der Kurve steht klein: <span class="m">C ∼ 1/d</span> — Hyperbel.

Beim Ändern von <span class="m">A</span> oder <span class="m">ε_r</span> ändert sich die **ganze
Kurve**, beim Ändern von <span class="m">d</span> nur der Arbeitspunkt. Das ist beabsichtigt und
gehört in den Beobachtungsauftrag.

### 4.7 Canvas 3 — das Q-U-Diagramm mit der Energiefläche

`<canvas id="cvQU" width="1000" height="200">`

| Achse | Bereich | Beschriftung |
|---|---|---|
| waagerecht | <span class="m">U</span> von 0 bis <span class="m">U_plot</span> | „Spannung U in V" |
| senkrecht | <span class="m">Q</span> von 0 bis <span class="m">Q_plot</span> | „Ladung Q in nC" |

<span class="m">U_plot = max(500 V; 1,1 · U)</span>, aufgerundet auf 1-2-5-Raster; im Modus
`isoliert` kann <span class="m">U</span> über 500 V steigen, dann wächst die Achse mit.
<span class="m">Q_plot = C · U_plot</span>, ebenfalls aufgerundet.

**Inhalt:**

1. Die Gerade <span class="m">Q = C·U</span> vom Ursprung bis <span class="m">U_plot</span>;
   ihre **Steigung ist die Kapazität**. Beschriftung an der Geraden:
   *„Steigung = C"*.
2. Der Arbeitspunkt <span class="m">(U | Q)</span> als gefüllter Kreis.
3. Das **Dreieck** zwischen Ursprung, <span class="m">(U | 0)</span> und dem Arbeitspunkt,
   gefüllt mit `--akzent-hell`, Rand `--akzent-rand`. Beschriftung im Dreieck:
   `Fläche = ½·Q·U = W = 0,3542 µJ` (Wert läuft mit).
4. Im Modus `isoliert` zusätzlich eine waagerechte gestrichelte Linie bei
   <span class="m">Q = Q_fest</span> mit der Beschriftung *„Q bleibt fest"*. Ändert man dann
   <span class="m">d</span>, **dreht sich die Gerade** und der Arbeitspunkt wandert auf dieser
   Waagerechten nach rechts oder links. Das ist das Bild, an dem der Unterschied der beiden
   Betriebsarten hängen bleibt.

### 4.8 Beobachtungsauftrag

`<div class="auftrag">`, Text:

> **Beobachtungsauftrag**
> Stell die Startwerte ein: <span class="m">U = 200 V</span>, <span class="m">d = 20 mm</span>,
> <span class="m">L = 20 cm</span>, Luft, Quelle **angeschlossen**. Notiere C, Q, U, E und W.
>
> **Durchgang 1:** Lass die Quelle angeschlossen und zieh den Plattenabstand auf
> <span class="m">40 mm</span>. Notiere dieselben fünf Größen.
>
> **Durchgang 2:** Setz alles zurück, schalte auf **Quelle abgetrennt** und zieh danach wieder auf
> <span class="m">40 mm</span>. Notiere erneut.
>
> Zwei der fünf Größen bleiben in Durchgang 2 gegenüber dem Start exakt gleich. Bei der einen ist das
> die Definition des Abtrennens, bei der anderen das eigentlich Überraschende. Benenne beide und
> schreib auf: erstens, warum die zweite trotz des Ziehens unverändert bleibt; zweitens, warum die
> gespeicherte Energie im einen Durchgang steigt und im anderen sinkt, obwohl du beide Male
> dasselbe getan hast.

**Erwartete Messwerte** (K-9, dient der Lehrkraft zur Kontrolle):

| | Start | Durchgang 1 (angeschlossen, d = 40 mm) | Durchgang 2 (abgetrennt, d = 40 mm) |
|---|---|---|---|
| C | 17,71 pF | 8,85 pF | 8,85 pF |
| Q | 3,542 nC | 1,771 nC | 3,542 nC |
| U | 200,0 V | 200,0 V | 400,0 V |
| **E** | 10,00 kV/m | 5,00 kV/m | **10,00 kV/m** |
| W | 0,3542 µJ | 0,1771 µJ | 0,7083 µJ |

### 4.9 Die beiden Verständnisfragen zur Simulation

Beide direkt unter der Simulation, `<div class="aufgabe" data-mc="…">`, jeweils mit
`<span class="ab">Anforderungsbereich II</span>`. Sie sind **nur mit der Simulation** zu
beantworten, weil sie den Vergleich zweier Durchgänge verlangen.

---

#### sim1

**Frage:**

> Stell **in dieser Reihenfolge** ein: Glas (<span class="m">ε_r = 6,00</span>), Spannung 150 V,
> <span class="m">d = 20 mm</span>, <span class="m">L = 20 cm</span>, Quelle angeschlossen. Trenne dann
> die Quelle ab und zieh den Plattenabstand auf 45 mm. Vergleiche die Anzeigen für
> <span class="m">U</span>, <span class="m">E</span> und <span class="m">Q</span> vor und nach dem
> Ziehen. Welche Aussage passt zur Anzeige?

| `data-i` | Option |
|---|---|
| 0 | Die Spannung bleibt bei 150 V, und die Feldstärke sinkt auf 3,33 kV/m – die Spannung ist beim Abtrennen eingefroren, und <span class="m">E = U/d</span> wird beim größeren Abstand kleiner. |
| 1 | Die Spannung steigt von 150 V auf 337,5 V, die Feldstärke bleibt bei 7,50 kV/m – die Ladung ist festgehalten, und <span class="m">E = Q/(ε₀·ε_r·A)</span> enthält den Plattenabstand nicht. |
| 2 | Die Spannung steigt auf 337,5 V, und die Feldstärke steigt ebenfalls auf 16,88 kV/m, weil in <span class="m">E = U/d</span> die Spannung im Zähler steht. |
| 3 | Die Spannung steigt auf 337,5 V, aber die Ladung sinkt von 15,94 nC auf 7,08 nC, weil die Kapazität mit dem Abstand kleiner wird und <span class="m">Q = C·U</span> gilt. |

`r: 1`

**Feedback:**

- `fb[0]`: „Das wäre der Fall bei angeschlossener Quelle: Dort bleibt U fest und E = U/d sinkt auf
  3,33 kV/m. Nach dem Abtrennen ist aber die Ladung eingefroren, es kann nichts mehr abfließen. Die
  Anzeige zeigt es: Q bleibt bei 15,94 nC, und U steigt."
- `fb[1]`: „Richtig. Mit festem Q ist E = Q/(ε₀·ε_r·A) vom Abstand unabhängig: Beide Male zeigt die
  Anzeige 7,50 kV/m. Über E = U/d gesehen: U wächst von 150 V auf 337,5 V genau im Verhältnis 45 mm
  zu 20 mm, der Quotient bleibt. Das Glas ändert daran nichts – seine Wirkung steckt schon in der
  großen Ladung von 15,94 nC, die bei 150 V aufgenommen wurde."
- `fb[2]`: „Die Spannung steigt tatsächlich auf 337,5 V, aber E = U/d hat im Nenner den Abstand, und
  der ist jetzt 45 mm, nicht mehr 20 mm. Beide Änderungen gleichen sich aus: 337,5 V / 0,045 m =
  7,50 kV/m. Die 16,88 kV/m entstehen nur, wenn du den alten Abstand einsetzt."
- `fb[3]`: „Q = C·U gilt nur, solange U festgehalten wird – das ist bei abgetrennter Quelle nicht der
  Fall. Ohne Verbindung zur Quelle kann keine Ladung abfließen, Q bleibt bei 15,94 nC (die Anzeige
  ändert sich nicht), und stattdessen passt sich U an: U = Q/C = 337,5 V. Die 7,08 nC gehören zur
  angeschlossenen Quelle."

**Kontrollrechnung (Python, ε₀ = 8,854·10⁻¹² F/m; per Playwright aus der Simulation bestätigt):**
C = ε₀·6·0,04 m²/0,020 m = 106,25 pF; Q = C·U = 15,937 nC; E = 150 V/0,020 m = 7,50 kV/m;
nach dem Ziehen C = 47,22 pF, U = Q/C = 337,5 V, E = 337,5 V/0,045 m = 7,50 kV/m.
Option 0: 150 V/0,045 m = 3,33 kV/m; Option 2: 337,5 V/0,020 m = 16,88 kV/m; Option 3:
C₂·150 V = 7,08 nC. Der Sollwert (337,5 V, 7,50 kV/m) steht in keiner Tabelle des Moduls. Die
Reihenfolge ist in der Frage festgelegt: Bei vertauschter Reihenfolge (erst abtrennen, dann Glas)
zeigt die Anzeige andere Werte, die mit keiner Option zusammenfallen.

---

#### sim2

**Frage:**

> Bleib bei Glas, 200 V, 20 mm, 20 cm und lies die Energie <span class="m">W</span> ab. Zieh dann
> den Plattenabstand auf 40 mm – einmal bei abgetrennter, einmal bei angeschlossener Quelle – und
> lies <span class="m">W</span> jeweils erneut ab. Welche Aussage passt zu den Anzeigewerten
> **und** erklärt sie?

| `data-i` | Option |
|---|---|
| 0 | Abgetrennt steigt <span class="m">W</span> von 2,1250 µJ auf 4,2499 µJ, weil du Arbeit gegen die Anziehung der Platten verrichtest; angeschlossen sinkt es auf 1,0625 µJ, weil Ladung in die Quelle zurückfließt und Energie an sie abgibt. |
| 1 | In beiden Fällen sinkt <span class="m">W</span> auf 1,0625 µJ, weil sich die Kapazität halbiert und <span class="m">W = ½·C·U²</span> nur von <span class="m">C</span> abhängt. |
| 2 | Abgetrennt sinkt <span class="m">W</span> auf 1,0625 µJ, angeschlossen steigt es auf 4,2499 µJ: Ohne Quelle geht Energie verloren, mit Quelle wird sie nachgeliefert. |

`r: 0`

**Feedback:**

- `fb[0]`: „Richtig. Bei abgetrennter Quelle ist die einzige mögliche Energiequelle deine Hand: Der
  Zuwachs von 2,1250 µJ auf 4,2499 µJ ist die Arbeit gegen die Anziehung der Platten. Bei
  angeschlossener Quelle kann Ladung zurückfließen, und die Quelle nimmt die Energie wieder auf:
  W = ½·C·U² halbiert sich auf 1,0625 µJ."
- `fb[1]`: „C halbiert sich tatsächlich in beiden Fällen – aber W hängt nicht nur von C ab. Welche
  zweite Größe konstant bleibt, entscheidet über die Richtung: Bei festem U ist W = ½·C·U², also
  halbiert sich W; bei festem Q ist W = Q²/(2C), also verdoppelt es sich. Die Anzeige zeigt einen
  Faktor 4 zwischen beiden Endwerten (1,0625 µJ gegen 4,2499 µJ) – das sind keine
  Rundungseffekte."
- `fb[2]`: „Die Richtung ist vertauscht, und die Begründung stimmt nicht. Abgetrennt kann Energie
  nur durch deine Arbeit zugeführt werden – W steigt also auf 4,2499 µJ, es geht nichts verloren.
  Angeschlossen sinkt W auf 1,0625 µJ, weil bei halber Kapazität und fester Spannung weniger
  Ladung gespeichert wird und der Rest zur Quelle zurückfließt."

**Kontrollrechnung (Python):** W₁ = ½·C·U² = ½·106,248 pF·(200 V)² = 2,12496 µJ (Anzeige 2,1250 µJ);
abgetrennt: Q²/(2C₂) = (21,2496 nC)²/(2·53,124 pF) = 4,24992 µJ (Anzeige 4,2499 µJ), Zuwachs
2,12496 µJ = Arbeit der Hand; angeschlossen: ½·53,124 pF·(200 V)² = 1,06248 µJ (Anzeige 1,0625 µJ).
Verhältnis der Endwerte 4,24992/1,06248 = 4,00.

---

## 5 · Übungen

`<section id="uebungen">`, `.stufe`-Nummer **5**, Überschrift **Übungen — vom Einsetzen zum Beurteilen**.

Neun Aufgaben, verteilt auf die Anforderungsbereiche: **I** (ue1, ue2, ue3) · **II** (ue4, ue5, ue6)
· **III** (ue7, ue8, ue9). Die drei Aufgaben im Anforderungsbereich III sind Begründungs- und
Bewertungsaufgaben mit Musterlösung **und** Bewertungskriterien; gerechnet wird dort nur so viel,
wie das Argument trägt.

Jede Zahleneingabe hat genau vier Rückmeldetexte (`ok`, `falschEinheit`, `nah`, `weit`). Alle
sechs auswertbaren Aufgaben ue1 bis ue6 — also **auch die Multiple-Choice-Aufgabe ue3 und die
Zuordnung ue4** — bekommen die drei Hilfen mit den Rollen aus `vorlage/bausteine.md`: **Tipp**
räumt eine Hürde weg und nennt keine Formel · **Ansatz** gibt Formel und Weg, rechnet aber nicht ·
**Lösungsweg** rechnet vollständig mit Zwischenschritten und Einheiten. Das geht ohne Eingriff in
die Engine, weil das Hilfesystem über `closest(".aufgabe")` pro Aufgabenkasten arbeitet.
Die drei Bewertungsaufgaben ue7 bis ue9 haben stattdessen die Musterlösung in `data-stufe="9"`.

---

### 5.1 ue1 — Kapazität aus der Geometrie

`<div class="aufgabe" data-num="ue1">`, `<span class="ab">Anforderungsbereich I</span>`

**Aufgabentext:**

> Ein Plattenkondensator besteht aus zwei quadratischen Metallplatten der Fläche
> <span class="m">A = 150 cm²</span> im Abstand <span class="m">d = 0,50 mm</span>. Zwischen den
> Platten ist Luft (<span class="m">ε_r = 1,00</span>).
>
> Berechne die Kapazität <span class="m">C</span>.

**Eingabe:** `type="number"`, Einheitenliste in dieser Reihenfolge:
`Einheit…` (leer) · `pF` · `nF` · `µF` · **`pC`**
Die Einheit **pC** ist der fachliche Distraktor: Sie fängt die Verwechslung von Kapazität und
Ladung ab, die beim Buchstaben C besonders naheliegt.

**`numDaten`-Eintrag:**

```js
ue1:{ wert:265.6, einheit:"pF", tol:2,
      alt:{wert:0.2656, einheit:"nF"},
      ok:"Richtig. C = ε₀·A/d = 8,854·10⁻¹² F/m · 0,0150 m² / 5,0·10⁻⁴ m = 2,656·10⁻¹⁰ F = 265,6 pF. Das ist eine typische Größenordnung für einen selbstgebauten Plattenkondensator — Bauteile im Elektroniklabor liegen eher bei nF und µF.",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. Die Kapazität wird in Farad gemessen (1 F = 1 C/V); pC ist eine Ladungseinheit. Und prüfe die Zehnerpotenz: 265,6 pF = 0,2656 nF = 2,656·10⁻¹⁰ F.",
      nah:"Die Größenordnung stimmt, der Wert nicht ganz. Zwei typische Stellen: Ist A wirklich in m² eingesetzt (150 cm² = 150·10⁻⁴ m² = 0,0150 m²) und d in m (0,50 mm = 5,0·10⁻⁴ m)?",
      weit:"Das liegt um mehr als den Faktor zwei daneben — da ist eine Zehnerpotenz verrutscht. Häufigste Ursache: cm² nicht in m² umgerechnet (Faktor 10⁻⁴, nicht 10⁻²) oder mm nicht in m. Nutze die Hilfen und schreib jede Zahl mit ihrer Einheit auf." }
```

**Hilfe 1 (Tipp):**

> Beide Längenangaben stehen in „Bequemlichkeitseinheiten". Bevor du irgendetwas einsetzt, rechne
> Fläche und Abstand in die SI-Einheiten um — und denk daran, dass bei einer Fläche der
> Umrechnungsfaktor quadriert wird.

**Hilfe 2 (Ansatz):**

> Die Kapazität eines Plattenkondensators hängt nur von der Geometrie und vom Material zwischen
> den Platten ab:
> - `data-tex`: `C = \varepsilon_0 \cdot \varepsilon_r \cdot \dfrac{A}{d}`
> - `data-plain`: `C = ε₀ · ε_r · A/d`
>
> Mit Luft ist <span class="m">ε_r = 1,00</span>, der Faktor fällt also weg. Setze
> <span class="m">ε₀ = 8,854 · 10⁻¹² F/m</span>, <span class="m">A</span> in m² und
> <span class="m">d</span> in m ein.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** A = 150 cm² = 150 · 10⁻⁴ m² = 1,50 · 10⁻² m² · d = 0,50 mm = 5,0 · 10⁻⁴ m ·
> ε_r = 1,00 · ε₀ = 8,854 · 10⁻¹² F/m
>
> - `data-tex`: `C = \dfrac{8{,}854 \cdot 10^{-12}\,\frac{\mathrm F}{\mathrm m} \cdot 1{,}50 \cdot 10^{-2}\,\mathrm{m^2}}{5{,}0 \cdot 10^{-4}\,\mathrm m} = 2{,}656 \cdot 10^{-10}\,\mathrm F`
> - `data-plain`: `C = (8,854·10⁻¹² F/m · 1,50·10⁻² m²) / (5,0·10⁻⁴ m) = 2,656·10⁻¹⁰ F`
>
> Einheitenprobe: (F/m) · m² / m = F ✓
>
> **Ergebnis: C = 2,656 · 10⁻¹⁰ F = 265,6 pF ≈ 0,27 nF.**
>
> Zum Einordnen: Um auf 1 µF zu kommen — ein gewöhnlicher Wert im Elektroniklabor — müsste man
> diese Fläche bei gleichem Abstand fast viertausendfach vergrößern. Genau deshalb sind
> Kondensatoren gewickelt und mit dünnster Isolierfolie gebaut; du rechnest das in ue5 nach.

---

### 5.2 ue2 — Ladung auf den Platten

`<div class="aufgabe" data-num="ue2">`, `<span class="ab">Anforderungsbereich I</span>`

**Aufgabentext:**

> Derselbe Kondensator wie in ue1 (<span class="m">A = 150 cm²</span>,
> <span class="m">d = 0,50 mm</span>, Luft, <span class="m">C = 265,6 pF</span>) wird an eine
> Spannungsquelle mit <span class="m">U = 24 V</span> angeschlossen.
>
> Berechne die Ladung <span class="m">Q</span> auf **einer** Platte.

**Eingabe:** `Einheit…` (leer) · `nC` · `pC` · `µC` · **`nF`**
Distraktor **nF**: fängt das Verwechseln von Ladung und Kapazität ab.

**`numDaten`-Eintrag:**

```js
ue2:{ wert:6.375, einheit:"nC", tol:0.05,
      alt:{wert:6375, einheit:"pC"},
      ok:"Richtig. Q = C·U = 2,656·10⁻¹⁰ F · 24 V = 6,375·10⁻⁹ C = 6,375 nC. Das sind rund 4·10¹⁰ Elektronen, die von der einen auf die andere Platte gewandert sind.",
      falschEinheit:"Der Zahlenwert stimmt, die Einheit nicht. Eine Ladung wird in Coulomb gemessen; nF ist die Einheit der Kapazität. Zur Kontrolle der Zehnerpotenz: 6,375 nC = 6375 pC = 6,375·10⁻⁹ C.",
      nah:"Fast. Prüfe, ob du wirklich mit C = 2,656·10⁻¹⁰ F gerechnet hast und nicht mit einem gerundeten Zwischenwert — und ob die Spannung mit 24 V eingesetzt wurde.",
      weit:"Das passt noch nicht. Q = C·U ist eine Multiplikation, keine Division; wer C durch U teilt, kommt auf 1,107·10⁻¹¹ und liegt damit um den Faktor 576 = 24² zu tief. Nutze die Hilfen." }
```

**Hilfe 1 (Tipp):**

> Die Kapazität aus ue1 ist hier ein *gegebener* Wert — du musst sie nicht neu ausrechnen. Gesucht
> ist die Verknüpfung zwischen Kapazität, Spannung und Ladung.

**Hilfe 2 (Ansatz):**

> Die Kapazität ist definiert als <span class="m">C = Q/U</span>. Nach der Ladung umgestellt:
> - `data-tex`: `Q = C \cdot U`
> - `data-plain`: `Q = C · U`
>
> Setze C in Farad ein, nicht in Pikofarad.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** C = 265,6 pF = 2,656 · 10⁻¹⁰ F · U = 24 V
>
> - `data-tex`: `Q = C \cdot U = 2{,}656 \cdot 10^{-10}\,\mathrm F \cdot 24\,\mathrm V = 6{,}375 \cdot 10^{-9}\,\mathrm C`
> - `data-plain`: `Q = C · U = 2,656·10⁻¹⁰ F · 24 V = 6,375·10⁻⁹ C`
>
> Einheitenprobe: F · V = (C/V) · V = C ✓
>
> **Ergebnis: Q = 6,375 nC.**
>
> **Zwei Nebenrechnungen, die das Ergebnis greifbar machen.**
> Feldstärke: <span class="m">E = U/d = 24 V / 5,0·10⁻⁴ m = 4,8 · 10⁴ V/m = 48 kV/m</span> — weit
> unterhalb der Durchschlagsfeldstärke von Luft (3 · 10⁶ V/m), der Aufbau hält also.
> Elektronenzahl: <span class="m">n = Q/e = 6,375·10⁻⁹ C / 1,602·10⁻¹⁹ C = 3,98 · 10¹⁰</span>.
> Rund vierzig Milliarden Elektronen — und trotzdem ist die Ladung so klein, dass man sie mit einem
> gewöhnlichen Amperemeter nicht messen kann.

---

### 5.3 ue3 — Was ein Feldlinienbild aussagt (Multiple Choice)

`<div class="aufgabe" data-mc="ue3">`, `<span class="ab">Anforderungsbereich I</span>`,
`name="ue3"` an allen vier Radios.

**Frage:**

> Welche Aussage über elektrische Feldlinien ist **richtig**?

| `data-i` | Option |
|---|---|
| 0 | Zwei Feldlinien dürfen sich dort schneiden, wo die Felder zweier Ladungen gleich stark sind. |
| 1 | Im statischen Fall stehen Feldlinien senkrecht auf der Oberfläche eines Leiters, weil eine Komponente längs der Oberfläche die frei beweglichen Ladungen so lange verschieben würde, bis sie verschwunden ist. |
| 2 | Die Feldlinie gibt an, auf welcher Bahn sich eine geladene Probeladung im Feld bewegt. |
| 3 | Je länger eine Feldlinie eingezeichnet ist, desto stärker ist das Feld an ihrem Anfangspunkt. |

`r: 1`

**Feedback:**

- `fb[0]`: „In einem Schnittpunkt hätte das Feld zwei Richtungen gleichzeitig — die Kraft auf eine
  Probeladung wäre nicht eindeutig. Wo sich die Beiträge zweier Ladungen gerade aufheben, ist die
  Feldstärke null, und dort verläuft gar keine Feldlinie; sie kreuzen sich auch dort nicht."
- `fb[1]`: „Richtig. Wäre eine Tangentialkomponente übrig, flösse im Leiter so lange Ladung, bis
  sie kompensiert ist — der statische Zustand ist genau der, in dem nichts mehr fließt. Daraus
  folgt auch, dass jede Leiteroberfläche eine Äquipotentialfläche ist."
- `fb[2]`: „Das ist die häufigste Fehlvorstellung zum Feldlinienbild. Die Tangente gibt die
  Richtung der **Kraft** an, nicht die der Geschwindigkeit. Nur wenn eine Ladung **aus der Ruhe**
  startet und die Feldlinien **gerade** sind, fällt die Bahn mit der Linie zusammen — im
  Plattenkondensator also, im Feld einer Punktladung schon nicht mehr bei schrägem Eintritt."
- `fb[3]`: „Die Länge einer gezeichneten Linie ist reine Zeichensache — man kann sie beliebig weit
  verfolgen. Aussagekräftig ist die **Dichte** der Linien, und auch die nur im Vergleich innerhalb
  desselben Bildes."

**Hilfe 1 (Tipp):**

> Lies jede der vier Aussagen als Behauptung über **einen einzelnen Punkt** im Raum: Was genau soll
> dort gelten? Drei der vier scheitern schon daran, dass an einer Stelle immer nur eine einzige
> Kraftrichtung herrschen kann — und daran, dass der Zeichner frei entscheidet, wie viele Linien er
> malt und wie weit er sie verfolgt.

**Hilfe 2 (Ansatz):**

> Es gibt genau drei Leseregeln für ein Feldlinienbild. Prüf jede Option gegen sie:
>
> 1. **Tangente** an die Feldlinie = Richtung der Kraft auf eine **positive** Probeladung, also die
>    Richtung von <span class="m">E⃗</span>. Nicht die Richtung der Geschwindigkeit.
> 2. **Dichte** der Linien (Linien pro durchstoßener Querfläche) ist ein Maß für den Betrag der
>    Feldstärke — und zwar nur im Vergleich **innerhalb desselben Bildes**.
> 3. Feldlinien **schneiden sich nie**, weil <span class="m">E⃗</span> an jeder Stelle eindeutig ist.
>
> Für die Aussage über den Leiter brauchst du ein viertes Argument, das nicht im Bild steckt, sondern
> in der Bedeutung des Wortes *statisch*: Im Leiter sind Ladungen frei beweglich, und „statisch"
> heißt, dass nichts mehr fließt.

**Hilfe 3 (Lösungsweg):**

> **Option 0 — Schnittpunkt zweier Feldlinien.** Regel 3. In einem Schnittpunkt hätte
> <span class="m">E⃗</span> zwei Richtungen zugleich, die Kraft auf eine Probeladung wäre nicht
> eindeutig. Auch das vermutete Gegenbeispiel trägt nicht: Wo sich die Beiträge zweier Ladungen
> gerade aufheben, ist <span class="m">E⃗ = 0⃗</span> — dort verläuft überhaupt keine Linie.
> **Falsch.**
>
> **Option 1 — Feldlinien stehen senkrecht auf einer Leiteroberfläche.** Nimm an, es gäbe eine
> Komponente <span class="m">E_∥</span> längs der Oberfläche. Auf die frei beweglichen
> Leitungselektronen wirkte dann eine Kraft parallel zur Oberfläche, es flösse Ladung — so lange,
> bis die verschobene Ladung ein Gegenfeld aufgebaut hat, das <span class="m">E_∥</span> exakt
> aufhebt. Genau dieser Endzustand heißt „statisch". Übrig bleibt allein die Normalkomponente.
> **Richtig.** Als Nebenergebnis fällt ab: Längs der Oberfläche wird beim Verschieben einer Ladung
> keine Arbeit verrichtet, die Leiteroberfläche ist also eine **Äquipotentialfläche** — dieselbe
> Aussage wie bei den grün gestrichelten Linien in 2.4 und in der Simulation.
>
> **Option 2 — Feldlinie als Bahnkurve.** Regel 1. Die Tangente gibt die Richtung der **Kraft** an,
> und die Kraft bestimmt die Beschleunigung, nicht die Geschwindigkeit. Nur wenn die Ladung **aus
> der Ruhe** startet **und** die Feldlinien **gerade** sind, fällt die Bahn mit der Linie zusammen —
> im Plattenkondensator also, im Radialfeld einer Punktladung bei schrägem Eintritt schon nicht
> mehr. **Falsch**, und zwar die häufigste Fehlvorstellung zum Thema (siehe 2.4).
>
> **Option 3 — Länge der gezeichneten Linie als Maß für die Feldstärke.** Regel 2. Wie weit eine
> Linie gezeichnet wird, entscheidet der Zeichner; im Feld einer Punktladung reicht jede Feldlinie
> im Prinzip bis ins Unendliche. Aussagekräftig ist allein die Dichte. **Falsch.**
>
> **Ergebnis: Option 1 (`data-i="1"`) ist richtig.**

---

### 5.4 ue4 — Zuordnung: vier Abhängigkeiten, vier Diagramme

`<div class="aufgabe" data-num="ue4">`, `<span class="ab">Anforderungsbereich II</span>`
Das ist die **einzige** Zuordnungsaufgabe des Moduls (Engine läuft über einen festen Selektor).

**Aufgabentext:**

> Vier Messreihen an einem Plattenkondensator, vier Diagramme. Ordne jeder Messreihe den passenden
> Kurvenverlauf zu. Die Achsen sind jeweils bei null skaliert; auf Zahlenwerte kommt es nicht an,
> nur auf die Form.

**Die vier Diagramme** als Inline-SVG in `<div class="diagramme">`, jeweils
`viewBox="0 0 170 110"`, Achsen in `#94a3b8`, Kurve in `#1d4ed8` mit `stroke-width="2.5"`,
`fill="none"`. Achsen einheitlich: x-Achse `16,88 158,88`, y-Achse `22,94 22,14`.

| Bild | `figcaption` | Verlauf | `points` |
|---|---|---|---|
| A | A | Hyperbel, fällt | `36,20 40,32 45,41 49,47 54,52 58,56 63,59 67,61 72,64 76,65 81,67 85,68 90,70 94,71 98,72 103,72 107,73 112,74 116,74 121,75 125,76 130,76 134,76 139,77 143,77 148,78 152,78` |
| B | B | Ursprungsgerade | `22,88 152,20` |
| C | C | Parabel durch den Ursprung | `22,88 28,88 35,87 42,86 48,85 54,84 61,82 68,80 74,77 80,74 87,71 94,67 100,64 106,59 113,55 120,50 126,44 132,39 139,33 146,27 152,20` |
| D | D | waagerechte Gerade | `22,48 152,48` |

**Die vier Zeilen** in `<div class="zuordnung">`, in **dieser** Markup-Reihenfolge
(sie entspricht bewusst **nicht** der Diagrammreihenfolge):

| Nr. | Situationsbeschreibung | `data-loesung` |
|---|---|---|
| 1 | Die Spannungsquelle bleibt angeschlossen, <span class="m">U</span> ist fest. Du vergrößerst die Plattenfläche <span class="m">A</span>. Aufgetragen ist die Ladung <span class="m">Q</span> gegen die Fläche <span class="m">A</span>. | **B** |
| 2 | Die Quelle ist abgetrennt, die Ladung <span class="m">Q</span> ist fest. Du veränderst den Plattenabstand <span class="m">d</span>. Aufgetragen ist die Feldstärke <span class="m">E</span> gegen den Abstand <span class="m">d</span>. | **D** |
| 3 | Ein Kondensator fester Kapazität wird nacheinander auf verschiedene Spannungen geladen. Aufgetragen ist die gespeicherte Energie <span class="m">W</span> gegen die Spannung <span class="m">U</span>. | **C** |
| 4 | Die Spannungsquelle bleibt angeschlossen, <span class="m">U</span> ist fest. Du veränderst den Plattenabstand <span class="m">d</span>. Aufgetragen ist die Ladung <span class="m">Q</span> gegen den Abstand <span class="m">d</span>. | **A** |

Lösungsfolge in Markup-Reihenfolge: **B – D – C – A**.
Jedes `<select>` enthält `…` (leer) · A · B · C · D.

**Begründung jeder Zuordnung** (gehört in die Rückmeldung bei vollständiger Lösung):

| Zeile | Rechnung | Form |
|---|---|---|
| 1 | <span class="m">Q = C·U = (ε₀ε_r·U/d) · A</span>, alles außer A fest | proportional → Ursprungsgerade **B** |
| 2 | <span class="m">E = Q/(ε₀ε_r·A)</span>, d kommt nicht vor | konstant → Waagerechte **D** |
| 3 | <span class="m">W = ½·C·U²</span> | quadratisch → Parabel **C** |
| 4 | <span class="m">Q = ε₀ε_r·A·U/d</span>, d im Nenner | umgekehrt proportional → Hyperbel **A** |

**Rückmeldungstext bei Teilerfolg** (nennt die Strategie, nicht die Lösung):

> Noch nicht alles passt. Geh jede Zeile in zwei Schritten durch: **Erstens** — was wird
> festgehalten, die Spannung oder die Ladung? Davon hängt ab, welche Formel du überhaupt benutzen
> darfst. **Zweitens** — steht die veränderte Größe in dieser Formel im Zähler (Gerade), im Nenner
> (Hyperbel), im Quadrat (Parabel) oder gar nicht (Waagerechte)?

**Hilfe 1 (Tipp):**

> Lies jede Zeile in zwei Etappen. Der erste Satz sagt dir, **was festgehalten wird** — und damit,
> welche der beiden Betriebsarten aus 3.7 gilt. Erst der zweite Satz sagt, was verändert und was
> aufgetragen wird. Wer sofort auf die Achsenbeschriftung schaut, greift in der Hälfte der Fälle zur
> falschen Formel.

**Hilfe 2 (Ansatz):**

> **Schritt 1 — passende Formel wählen.** Bei angeschlossener Quelle ist <span class="m">U</span>
> fest, bei abgetrennter Quelle ist <span class="m">Q</span> fest:
> - `data-tex`: `U \text{ fest:}\quad Q = \varepsilon_0\varepsilon_r A \dfrac{U}{d}, \quad E = \dfrac{U}{d}`
> - `data-plain`: `U fest:  Q = ε₀·ε_r·A·U/d,  E = U/d`
> - `data-tex`: `Q \text{ fest:}\quad U = \dfrac{Q\,d}{\varepsilon_0\varepsilon_r A}, \quad E = \dfrac{Q}{\varepsilon_0\varepsilon_r A}`
> - `data-plain`: `Q fest:  U = Q·d/(ε₀·ε_r·A),  E = Q/(ε₀·ε_r·A)`
> - `data-tex`: `W = \tfrac{1}{2} C U^2 = \dfrac{Q^2}{2C}`
> - `data-plain`: `W = ½·C·U² = Q²/(2C)`
>
> **Schritt 2 — Form ablesen.** Stell die Formel so um, dass nur die veränderte Größe als Variable
> übrig bleibt, alles andere ist eine Konstante <span class="m">k</span>:
>
> | Die veränderte Größe steht … | Funktionstyp | Kurve |
> |---|---|---|
> | im Zähler, erste Potenz (<span class="m">y = k·x</span>) | proportional | Ursprungsgerade |
> | im Nenner (<span class="m">y = k/x</span>) | umgekehrt proportional | Hyperbel |
> | im Zähler, quadriert (<span class="m">y = k·x²</span>) | quadratisch | Parabel durch den Ursprung |
> | gar nicht in der Formel (<span class="m">y = k</span>) | konstant | Waagerechte |
>
> Auf Zahlenwerte kommt es nicht an, nur auf diesen Typ.

**Hilfe 3 (Lösungsweg):**

> **Zeile 1 — U fest, A verändert, aufgetragen Q gegen A.**
> - `data-plain`: `Q = C·U = (ε₀·ε_r·U/d) · A = k · A`
>
> <span class="m">U</span>, <span class="m">d</span> und <span class="m">ε_r</span> sind fest, also
> steht <span class="m">A</span> allein und in erster Potenz im Zähler: proportional.
> Kontrollzahlen aus der Simulation (U = 200 V, d = 20 mm, Luft):
> <span class="m">A = 100 cm² → Q = 0,8854 nC</span>, <span class="m">A = 400 cm² → Q = 3,5416 nC</span>,
> <span class="m">A = 900 cm² → Q = 7,9686 nC</span> — vierfache Fläche, vierfache Ladung.
> **→ Diagramm B (Ursprungsgerade).**
>
> **Zeile 2 — Q fest, d verändert, aufgetragen E gegen d.**
> - `data-plain`: `E = Q/(ε₀·ε_r·A) = k`
>
> In dieser Form kommt <span class="m">d</span> überhaupt nicht vor. Über <span class="m">E = U/d</span>
> gesehen: <span class="m">U</span> wächst genau proportional zu <span class="m">d</span>, der
> Quotient bleibt. Kontrollzahlen (Q = 3,5416 nC, A = 400 cm², Luft):
> <span class="m">d = 20 mm → U = 200,0 V, E = 10,00 kV/m</span>;
> <span class="m">d = 40 mm → U = 400,0 V, E = 10,00 kV/m</span>. **→ Diagramm D (Waagerechte).**
>
> **Zeile 3 — C fest, U verändert, aufgetragen W gegen U.**
> - `data-plain`: `W = ½·C·U² = k · U²`
>
> Quadratisch, und wegen <span class="m">W(0) = 0</span> geht die Parabel durch den Ursprung.
> Kontrollzahlen (C = 17,708 pF): <span class="m">100 V → 0,0885 µJ</span>,
> <span class="m">200 V → 0,3542 µJ</span>, <span class="m">400 V → 1,4166 µJ</span> — doppelte
> Spannung, vierfache Energie. **→ Diagramm C (Parabel).**
>
> **Zeile 4 — U fest, d verändert, aufgetragen Q gegen d.**
> - `data-plain`: `Q = C·U = ε₀·ε_r·A·U/d = k/d`
>
> <span class="m">d</span> steht im Nenner: umgekehrt proportional. Kontrollzahlen (U = 200 V,
> A = 400 cm², Luft): <span class="m">d = 10 mm → Q = 7,0832 nC</span>,
> <span class="m">d = 20 mm → Q = 3,5416 nC</span>, <span class="m">d = 40 mm → Q = 1,7708 nC</span>.
> **→ Diagramm A (Hyperbel).**
>
> **Lösungsfolge in Markup-Reihenfolge: B – D – C – A.**
>
> **Merk dir das Muster, nicht die vier Antworten.** Die Zeilen 1 und 4 unterscheiden sich nur darin,
> welche Größe verändert wird — und ergeben trotzdem völlig verschiedene Kurven, weil die eine im
> Zähler und die andere im Nenner steht. Die Zeilen 2 und 4 unterscheiden sich nur in der
> Betriebsart — und ergeben deshalb einmal eine Waagerechte und einmal eine Hyperbel.

---

### 5.5 ue5 — Warum Kondensatoren gewickelt sind

`<div class="aufgabe" data-num="ue5">`, `<span class="ab">Anforderungsbereich II</span>`

**Aufgabentext:**

> Ein Kondensator soll bei der Betriebsspannung <span class="m">U = 50 V</span> die Energie
> <span class="m">W = 1,0 mJ</span> speichern. Als Dielektrikum dient eine Kunststofffolie (etwa
> aus PVC oder Polyamid; der Wert streut je nach Sorte) der Dicke
> <span class="m">d = 0,10 mm</span> mit <span class="m">ε_r = 4,5</span>.
>
> Berechne die Plattenfläche <span class="m">A</span>, die dafür nötig ist.

**Eingabe:** `Einheit…` (leer) · `m²` · `cm²` · **`m`** · **`F`**
Zwei Distraktoreinheiten: **m** (Länge statt Fläche) und **F** (das Zwischenergebnis C).

**`numDaten`-Eintrag:**

```js
ue5:{ wert:2.01, einheit:"m²", tol:0.05,
      alt:{wert:20079, einheit:"cm²"},
      ok:"Richtig. Aus W = ½·C·U² folgt C = 2W/U² = 8,0·10⁻⁷ F = 800 nF, und daraus A = C·d/(ε₀·ε_r) = 2,01 m². Zwei Quadratmeter für einen Kondensator von der Größe eines Daumens — deshalb wird die Folie gewickelt: als 5 cm breiter Streifen wären das gut 40 m Länge.",
      falschEinheit:"Gesucht ist eine Fläche. Wenn du F gewählt hast, hast du beim Zwischenergebnis C aufgehört; wenn du m gewählt hast, vermutlich die Kantenlänge gemeint (die wäre √2,01 m² = 1,42 m). Umrechnung: 2,01 m² = 20 100 cm².",
      nah:"Die Größenordnung stimmt. Prüfe zwei Stellen: Steht in C = 2W/U² wirklich die 2 im Zähler (der Faktor ½ wird beim Umstellen zur 2)? Und ist ε_r = 4,5 im Nenner gelandet und nicht im Zähler?",
      weit:"Das liegt weit daneben. Typische Ursachen: mJ nicht in J umgerechnet (1,0 mJ = 1,0·10⁻³ J), mm nicht in m (0,10 mm = 1,0·10⁻⁴ m) oder U nicht quadriert. Rechne mit dem Ansatz aus Hilfe 2 Schritt für Schritt neu." }
```

**Hilfe 1 (Tipp):**

> Das ist keine Aufgabe, sondern zwei. Die Fläche steht in keiner Energieformel — du brauchst also
> erst eine Zwischengröße, die in beiden Welten vorkommt: in der Energie und in der Geometrie.

**Hilfe 2 (Ansatz):**

> **Schritt 1** — aus der Energie die Kapazität:
> - `data-tex`: `W = \tfrac{1}{2} C U^2 \quad \Longrightarrow \quad C = \dfrac{2W}{U^2}`
> - `data-plain`: `W = ½·C·U²   ⟹   C = 2W/U²`
>
> **Schritt 2** — aus der Kapazität die Fläche:
> - `data-tex`: `C = \varepsilon_0 \varepsilon_r \dfrac{A}{d} \quad \Longrightarrow \quad A = \dfrac{C \cdot d}{\varepsilon_0 \cdot \varepsilon_r}`
> - `data-plain`: `C = ε₀·ε_r·A/d   ⟹   A = C·d / (ε₀·ε_r)`
>
> Rechne W in J und d in m um, bevor du einsetzt.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** W = 1,0 mJ = 1,0 · 10⁻³ J · U = 50 V · d = 0,10 mm = 1,0 · 10⁻⁴ m · ε_r = 4,5
>
> **Schritt 1 — nötige Kapazität.**
> - `data-tex`: `C = \dfrac{2W}{U^2} = \dfrac{2 \cdot 1{,}0 \cdot 10^{-3}\,\mathrm J}{(50\,\mathrm V)^2} = \dfrac{2{,}0 \cdot 10^{-3}}{2500}\,\mathrm F = 8{,}0 \cdot 10^{-7}\,\mathrm F`
> - `data-plain`: `C = 2W/U² = 2 · 1,0·10⁻³ J / (50 V)² = 2,0·10⁻³ / 2500 F = 8,0·10⁻⁷ F = 800 nF`
>
> Einheitenprobe: J/V² = (C·V)/V² = C/V = F ✓
>
> **Schritt 2 — nötige Fläche.**
> - `data-tex`: `A = \dfrac{C \cdot d}{\varepsilon_0 \cdot \varepsilon_r} = \dfrac{8{,}0 \cdot 10^{-7}\,\mathrm F \cdot 1{,}0 \cdot 10^{-4}\,\mathrm m}{8{,}854 \cdot 10^{-12}\,\frac{\mathrm F}{\mathrm m} \cdot 4{,}5} = \dfrac{8{,}0 \cdot 10^{-11}}{3{,}984 \cdot 10^{-11}}\,\mathrm{m^2}`
> - `data-plain`: `A = C·d / (ε₀·ε_r) = (8,0·10⁻⁷ F · 1,0·10⁻⁴ m) / (8,854·10⁻¹² F/m · 4,5) = 8,0·10⁻¹¹ / 3,984·10⁻¹¹ m²`
>
> **Ergebnis: A = 2,01 m².**
>
> **Einordnung.** Eine quadratische Platte dieser Fläche hätte die Kantenlänge
> <span class="m">√2,01 m² = 1,42 m</span>. Als 5,0 cm breiter Folienstreifen gewickelt sind es
> <span class="m">2,0079 m² / 0,050 m = 40,2 m</span> Länge. Genau so werden Folienkondensatoren
> gebaut: zwei Metallfolien und zwei Isolierfolien übereinander, zusammengerollt.
> Die Feldstärke in der Folie beträgt dabei
> <span class="m">E = U/d = 50 V / 1,0·10⁻⁴ m = 5,0 · 10⁵ V/m = 0,50 MV/m</span> — ein Sechstel
> dessen, was trockene Luft gerade noch aushält (3 MV/m), und für Kunststofffolien, die typisch
> über 100 MV/m vertragen, völlig unkritisch.

---

### 5.6 ue6 — Arbeit beim Auseinanderziehen

`<div class="aufgabe" data-num="ue6">`, `<span class="ab">Anforderungsbereich II</span>`

**Aufgabentext:**

> Ein Plattenkondensator mit <span class="m">C₁ = 100 pF</span> wird an
> <span class="m">U₁ = 200 V</span> aufgeladen. Danach wird die **Spannungsquelle abgetrennt** und
> der Plattenabstand auf das **Dreifache** vergrößert. Fläche und Dielektrikum bleiben unverändert.
>
> Berechne die mechanische Arbeit, die beim Auseinanderziehen verrichtet werden muss.

**Eingabe:** `Einheit…` (leer) · `µJ` · `nJ` · `mJ` · **`µW`**
Distraktor **µW**: fängt die Verwechslung von Energie und Leistung ab.

**`numDaten`-Eintrag** (mit `sonder`-Liste für Zwischenwerte und Fehlerwerte):

```js
ue6:{wert:4.0, einheit:"µJ", tol:0.05, alt:{wert:4000, einheit:"nJ"},
      ok:"Richtig. Q bleibt bei 20 nC, C sinkt auf ein Drittel (33,3 pF), also verdreifacht sich W = Q²/(2C) von 2,0 µJ auf 6,0 µJ. Die Differenz von 4,0 µJ ist genau die Arbeit deiner Hand – eine andere Energiequelle gibt es nicht mehr.",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. Gefragt ist eine Arbeit, also eine Energie in Joule. µW wäre eine Leistung – dafür müsste in der Aufgabe eine Zeit stehen, und die steht nicht da.",
      sonder:[
        {wert:2.0, text:"Das ist die Energie W₁ vor dem Auseinanderziehen. Gefragt ist aber die Arbeit beim Ziehen, also die Differenz W₂ − W₁. Berechne W₂ mit W = Q²/(2C) und der neuen Kapazität."},
        {wert:6.0, text:"Das ist die Energie W₂ nach dem Ziehen. Gefragt ist die Arbeit, also der Zuwachs W₂ − W₁: Die Anfangsenergie muss noch abgezogen werden."},
        {wert:-1.33, text:"Hier wurde mit konstanter Spannung weitergerechnet (W₂ = ½·C₂·U₁² = 0,67 µJ). Die Quelle ist aber abgetrennt: Konstant bleibt die Ladung, die Spannung steigt auf 600 V. Ein negatives Ergebnis hätte bedeutet, dass beim Ziehen Energie frei wird – gegen die Anziehung der Platten ist aber Arbeit nötig."},
        {wert:0.67, text:"Das ist W₂ bei konstanter Spannung (½·C₂·U₁²). Nach dem Abtrennen bleibt aber die Ladung konstant, nicht die Spannung. Rechne mit W = Q²/(2C) und bilde die Differenz W₂ − W₁."}
      ],
      nah:"Knapp daneben. Prüfe, welche Größe beim Abtrennen konstant bleibt: Es ist die Ladung, nicht die Spannung. Gefragt ist die Differenz W₂ − W₁ mit W = Q²/(2C).",
      weit:"Das passt noch nicht. Gefragt ist die Differenz W₂ − W₁, nicht einer der beiden Werte allein – und beim Abtrennen ist Q konstant, sodass W = Q²/(2C) die passende Form ist. Nutze die Hilfen."}
```

Hinweis für den Bauagenten: Die Rückmeldetexte `ok`/`falschEinheit`/`nah`/`weit` bleiben;
`sonder` ist ein zusätzliches Feld dieser Aufgabe (Sonderfälle mit eigener Rückmeldung, Vorrang vor
`nah`/`weit`) und wird so umgesetzt, wie es die HTML-Datei in der Engine vorgibt.

**Hilfe 1 (Tipp):**

> Frag dich zuerst: Was kann sich nach dem Abtrennen überhaupt noch ändern? Es gibt keinen Weg mehr,
> über den Ladung zu- oder abfließen könnte. Und: Wo soll die Energie herkommen, wenn keine Quelle
> mehr angeschlossen ist?

**Hilfe 2 (Ansatz):**

> Beim Abtrennen bleibt die **Ladung** <span class="m">Q = C₁·U₁</span> erhalten. Der verdreifachte
> Abstand drittelt die Kapazität, denn <span class="m">C ∼ 1/d</span>. Für die Energie nimmst du
> deshalb die Form, in der Q steht:
> - `data-tex`: `W = \dfrac{Q^2}{2C} \qquad W_{\text{zug}} = W_2 - W_1`
> - `data-plain`: `W = Q²/(2C)     W_zug = W₂ − W₁`
>
> Die Energieerhaltung liefert das Argument: Ohne Quelle kann der Zuwachs nur aus der mechanischen
> Arbeit stammen.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** C₁ = 100 pF = 1,00 · 10⁻¹⁰ F · U₁ = 200 V · Quelle abgetrennt · d → 3d
>
> **Schritt 1 — Ladung (bleibt konstant).**
> - `data-tex`: `Q = C_1 U_1 = 1{,}00 \cdot 10^{-10}\,\mathrm F \cdot 200\,\mathrm V = 2{,}0 \cdot 10^{-8}\,\mathrm C = 20\,\mathrm{nC}`
> - `data-plain`: `Q = C₁·U₁ = 1,00·10⁻¹⁰ F · 200 V = 2,0·10⁻⁸ C = 20 nC`
>
> **Schritt 2 — Energie vorher.**
> - `data-tex`: `W_1 = \tfrac{1}{2} C_1 U_1^2 = \tfrac{1}{2}\cdot 1{,}00\cdot10^{-10}\,\mathrm F \cdot (200\,\mathrm V)^2 = 2{,}0 \cdot 10^{-6}\,\mathrm J`
> - `data-plain`: `W₁ = ½·C₁·U₁² = ½ · 1,00·10⁻¹⁰ F · (200 V)² = 2,0·10⁻⁶ J = 2,0 µJ`
>
> **Schritt 3 — neue Kapazität und neue Spannung.**
> <span class="m">C₂ = C₁/3 = 33,3 pF</span>, damit
> <span class="m">U₂ = Q/C₂ = 2,0·10⁻⁸ C / 3,33·10⁻¹¹ F = 600 V</span>. Die Spannung hat sich
> verdreifacht, obwohl niemand etwas nachgeladen hat.
>
> **Schritt 4 — Energie nachher.**
> - `data-tex`: `W_2 = \dfrac{Q^2}{2 C_2} = \dfrac{(2{,}0\cdot10^{-8}\,\mathrm C)^2}{2 \cdot 3{,}33 \cdot 10^{-11}\,\mathrm F} = \dfrac{4{,}0 \cdot 10^{-16}}{6{,}67\cdot10^{-11}}\,\mathrm J = 6{,}0\cdot10^{-6}\,\mathrm J`
> - `data-plain`: `W₂ = Q²/(2·C₂) = (2,0·10⁻⁸ C)² / (2 · 3,33·10⁻¹¹ F) = 4,0·10⁻¹⁶ / 6,67·10⁻¹¹ J = 6,0·10⁻⁶ J = 6,0 µJ`
>
> **Schritt 5 — Differenz.**
> <span class="m">W_zug = W₂ − W₁ = 6,0 µJ − 2,0 µJ = 4,0 µJ</span>
>
> **Ergebnis: 4,0 µJ mechanische Arbeit.**
>
> **Gegenprobe über die Kraft.** Nimmt man <span class="m">A = 400 cm²</span> an, so gehört zu
> <span class="m">C₁ = 100 pF</span> der Abstand
> <span class="m">d₁ = ε₀A/C₁ = 3,54 mm</span>. Die Feldstärke ist
> <span class="m">E = Q/(ε₀A) = 56,5 kV/m</span>, die Kraft auf eine Platte
> <span class="m">F = ½·Q·E = 565 µN</span> — und diese Kraft ist beim Ziehen konstant. Über die
> zusätzliche Strecke <span class="m">Δd = 2d₁ = 7,08 mm</span> ergibt das
> <span class="m">W = F·Δd = 565 µN · 7,0832·10⁻³ m = 4,0 µJ</span>. Beide Wege führen auf denselben
> Wert; das ist die beste Kontrolle, die es für solche Aufgaben gibt.

**Kontrollrechnung (Python, ε₀ = 8,854·10⁻¹² F/m):** Q = 20,0 nC; W₁ = 2,000 µJ; C₂ = 33,333 pF;
U₂ = 600,0 V; W₂ = 6,000 µJ; W_zug = 4,000 µJ. Kraftweg: d₁ = 3,5416 mm, E = 56 471,7 V/m,
F = ½·Q·E = 564,72 µN, Δd = 7,0832 mm, F·Δd = 4,000 µJ. Fehlwerte: konstante Spannung
W₂ = ½·33,333 pF·(200 V)² = 0,667 µJ, W₂ − W₁ = −1,333 µJ.

---

### 5.7 ue7 — Bewertung: „doppelte Spannung, doppelte Energie"

`<div class="aufgabe" data-num="ue7">`, `<span class="ab">Anforderungsbereich III</span>`,
`<textarea>` und `<button data-loesung="ue7">Musterlösung anzeigen</button>`,
Musterlösung in `.hilfe-text[data-stufe="9"]`.

**Aufgabentext:**

> In der Stunde sagt jemand: *„Ein Kondensator ist wie ein Eimer. Verdopple ich die Spannung, passt
> doppelt so viel Ladung hinein — und damit speichert er auch doppelt so viel Energie."*
>
> Nimm zu beiden Teilen der Aussage physikalisch begründet Stellung. Benutze als Zahlenbeispiel den
> Kondensator aus der Simulation (<span class="m">C = 17,7 pF</span>), einmal bei
> <span class="m">200 V</span> und einmal bei <span class="m">400 V</span>. Beurteile am Ende auch,
> ob der Vergleich mit dem Eimer trägt.

**Musterlösung — erwartete Argumentation:**

> **Erster Teil: richtig.** Die Kapazität hängt nur von Geometrie und Dielektrikum ab, nicht von
> der Spannung. Aus <span class="m">C = Q/U</span> folgt <span class="m">Q = C·U</span>, also ist
> die Ladung proportional zur Spannung. Zahlenbeispiel: bei 200 V ist
> <span class="m">Q = 17,708 pF · 200 V = 3,542 nC</span>, bei 400 V entsprechend
> <span class="m">7,083 nC</span> — tatsächlich das Doppelte.
>
> **Zweiter Teil: falsch.** Für die Energie gilt
> <span class="m">W = ½·C·U²</span>; sie wächst **quadratisch** mit der Spannung. Bei 200 V sind es
> <span class="m">0,3542 µJ</span>, bei 400 V dagegen <span class="m">1,4166 µJ</span>, also das
> **Vierfache**, nicht das Doppelte.
>
> **Begründung des quadratischen Zusammenhangs.** Doppelt so viel Ladung wird nicht gegen dieselbe
> Spannung transportiert: Während des Ladens steigt die Gegenspannung am Kondensator mit der bereits
> gespeicherten Ladung an. Im <span class="m">Q</span>-<span class="m">U</span>-Diagramm ist die
> Energie die Fläche unter der Ursprungsgeraden, also ein Dreieck mit
> <span class="m">W = ½·Q·U</span>. Verdoppelt man <span class="m">U</span>, verdoppeln sich beide
> Kanten des Dreiecks — die Fläche vervierfacht sich.
>
> **Zur Analogie.** Der Vergleich trägt weiter, als der Sprecher vermutet: Füllt man einen
> zylindrischen Eimer, so steigt die eingefüllte Wassermenge proportional zur Füllhöhe, die
> potentielle Energie des Wassers aber quadratisch — denn jeder weitere Liter muss höher gehoben
> werden. Das ist dieselbe Struktur wie beim Kondensator. Der Fehler liegt also nicht im Bild,
> sondern darin, Ladung und Energie gleichzusetzen.

**Bewertungskriterien** (fett, mit `·` getrennt):

> Erster Teil der Aussage als richtig erkannt und mit <span class="m">Q = C·U</span> sowie der
> Unabhängigkeit von <span class="m">C</span> von <span class="m">U</span> begründet ·
> zweiter Teil als falsch erkannt und <span class="m">W = ½·C·U²</span> genannt ·
> Faktor 4 mit Zahlenwerten belegt (0,354 µJ → 1,417 µJ) ·
> quadratische Abhängigkeit physikalisch begründet (wachsende Gegenspannung beim Laden oder
> Dreiecksfläche im Q-U-Diagramm) ·
> Analogie differenziert beurteilt statt pauschal verworfen.

---

### 5.8 ue8 — Bewertung: Glasplatte zwischen den Platten

`<div class="aufgabe" data-num="ue8">`, `<span class="ab">Anforderungsbereich III</span>`,
`<textarea>`, `<button data-loesung="ue8">`, Musterlösung in `data-stufe="9"`.

**Aufgabentext:**

> Ein Plattenkondensator (<span class="m">A = 400 cm²</span>, <span class="m">d = 20 mm</span>,
> Luft) ist auf <span class="m">U = 200 V</span> geladen; es ist
> <span class="m">C = 17,7 pF</span>, <span class="m">Q = 3,54 nC</span>,
> <span class="m">W = 0,354 µJ</span>. Nun schiebt jemand eine Glasplatte
> (<span class="m">ε_r = 6,0</span>) vollständig zwischen die Platten und behauptet:
>
> *„Dadurch steigt die gespeicherte Energie auf jeden Fall — die Kapazität wird ja größer."*
>
> Untersuche die Behauptung für **beide** Betriebsarten (Quelle angeschlossen / Quelle abgetrennt),
> gib jeweils die neuen Werte an und erkläre, woher die Energie kommt beziehungsweise wohin sie geht.

**Musterlösung — erwartete Argumentation:**

> **Gemeinsam für beide Fälle:** Die Kapazität steigt um den Faktor
> <span class="m">ε_r = 6,0</span> auf <span class="m">C' = 106,2 pF</span>, denn
> <span class="m">C = ε₀·ε_r·A/d</span> und die Geometrie bleibt unverändert.
>
> **Fall 1 — Quelle angeschlossen (U = 200 V fest).**
> Die Ladung wächst auf <span class="m">Q' = C'·U = 21,25 nC</span>, die Energie auf
> <span class="m">W' = ½·C'·U² = 2,125 µJ</span>, also auf das **Sechsfache**. Hier stimmt die
> Behauptung. Die Energie stammt aus der Spannungsquelle, die die zusätzliche Ladung
> <span class="m">ΔQ = 17,71 nC</span> gegen 200 V nachliefert.
>
> **Fall 2 — Quelle abgetrennt (Q = 3,542 nC fest).**
> Jetzt ist die passende Form <span class="m">W = Q²/(2C)</span>: Mit sechsfachem
> <span class="m">C</span> sinkt die Energie auf ein Sechstel,
> <span class="m">W' = 0,0590 µJ</span>. Die Spannung fällt auf
> <span class="m">U' = Q/C' = 33,3 V</span>, die Feldstärke auf
> <span class="m">E' = U'/d = 1,67 kV/m</span> — auch sie ein Sechstel des Ausgangswerts, weil das
> Glas im Feld polarisiert wird und das Feld dadurch geschwächt wird. Hier ist die Behauptung
> **falsch**. Die fehlende Energie hat das Feld als Arbeit an der Glasplatte verrichtet: Sie wird
> in den Zwischenraum hineingezogen und müsste festgehalten werden, sonst beschleunigt sie und die
> Energie taucht als Bewegungsenergie und schließlich als Wärme wieder auf.
>
> **Fazit:** Die Behauptung ist nur für die angeschlossene Quelle richtig. Ohne Angabe der
> Randbedingung ist sie nicht entscheidbar — und genau diese Angabe fehlt in der Aussage.
>
> *Zusatz für eine besonders vollständige Antwort (Fall 1):* Die Quelle gibt insgesamt
> <span class="m">ΔQ·U = 17,708 nC · 200 V = 3,542 µJ</span> ab, im Feld landet aber nur der
> Zuwachs <span class="m">2,125 µJ − 0,354 µJ = 1,771 µJ</span>. Die andere Hälfte wird beim
> Einziehen der Glasplatte mechanisch frei. Auch hier geht die Bilanz exakt auf.

**Bewertungskriterien:**

> Erkannt, dass die Antwort von der Randbedingung abhängt, und beide Fälle sauber getrennt ·
> je Fall die passende Energieform gewählt (<span class="m">W = ½·C·U²</span> bei fester Spannung,
> <span class="m">W = Q²/(2C)</span> bei fester Ladung) ·
> Faktoren 6 bzw. 1/6 mit Zahlenwerten belegt ·
> Energiebilanz benannt (Quelle liefert nach · Feld verrichtet Arbeit am Dielektrikum) ·
> abschließendes Urteil, dass die Behauptung ohne Angabe der Betriebsart unentscheidbar ist.

---

### 5.9 ue9 — Bewertung: „Das Feld ist nur ein Rechentrick"

`<div class="aufgabe" data-num="ue9">`, `<span class="ab">Anforderungsbereich III</span>`,
`<textarea>`, `<button data-loesung="ue9">`, Musterlösung in `data-stufe="9"`.

**Aufgabentext:**

> In einer Diskussion fällt der Satz: *„Das elektrische Feld ist nur ein Rechentrick. Gemessen wird
> immer eine Kraft zwischen zwei Ladungen — solange keine zweite Ladung da ist, auf die etwas wirken
> könnte, existiert auch kein Feld."*
>
> Nimm dazu Stellung. Nenne mindestens zwei Argumente, die für die physikalische Eigenständigkeit
> des Feldbegriffs sprechen, und gehe darauf ein, welche Rolle die Probeladung in der Definition
> <span class="m">E⃗ = F⃗/q</span> tatsächlich spielt.

**Musterlösung — erwartete Argumentation:**

> **Zum Kern der Aussage.** Richtig ist, dass man ein Feld immer über eine Wirkung nachweist — mit
> einer Probeladung. Falsch ist der Schluss daraus. Die Definition
> <span class="m">E⃗ = F⃗/q</span> ist eine **Messvorschrift**, kein Existenzkriterium: Verdoppelt
> man die Probeladung, verdoppelt sich die Kraft, der Quotient bleibt gleich. Gerade weil die
> Probeladung herausfällt, beschreibt <span class="m">E⃗</span> nicht mehr das Paar aus zwei
> Ladungen, sondern allein die Stelle im Raum. Die Probeladung ist das Messgerät, nicht die Ursache
> — genauso wenig, wie ein Thermometer die Temperatur erzeugt.
>
> **Argument 1 — das Feld trägt Energie.** Die Energiedichte
> <span class="m">w = ½·ε₀·ε_r·E²</span> ist an jeder Stelle des Feldraums von null verschieden,
> ganz unabhängig davon, ob dort eine Probeladung sitzt. Beim Plattenkondensator summiert sie sich
> exakt zur gespeicherten Energie <span class="m">W = ½·C·U²</span> auf. Etwas, das Energie
> enthält, ist kein Rechentrick.
>
> **Argument 2 — die endliche Ausbreitungsgeschwindigkeit.** Verschiebt man die felderzeugende
> Ladung, so ändert sich das Feld an einem entfernten Ort erst nach der Laufzeit
> <span class="m">r/c</span>. In der Zwischenzeit „weiß" die zweite Ladung noch nichts davon.
> Eine reine Fernwirkungsbeschreibung kann das nicht abbilden — sie bräuchte eine augenblickliche
> Wirkung über beliebige Entfernung. Das Feld ist genau das, was die Wirkung während dieser
> Laufzeit trägt.
>
> **Argument 3 — elektromagnetische Wellen.** Eine Radiowelle transportiert Energie durch einen
> Raum, in dem überhaupt keine Ladung sitzt. Wenn das Feld nur ein Rechentrick wäre, müsste man
> sagen können, wo diese Energie zwischen Sender und Empfänger steckt — und die einzige verfügbare
> Antwort ist: im Feld.
>
> **Fazit.** Der Feldbegriff ist mehr als eine bequeme Schreibweise für das Coulombgesetz: Er ist
> der Übergang von der Fernwirkung zur **Nahwirkung** und damit die Grundlage der gesamten
> Elektrodynamik. Zuzugestehen ist der Aussage allerdings, dass man ein Feld nie „direkt" sieht,
> sondern immer über eine Wirkung erschließt — das gilt aber für fast jede physikalische Größe.

**Bewertungskriterien:**

> <span class="m">E = F/q</span> als Quotient erkannt, der von der Probeladung unabhängig ist ·
> Rolle der Probeladung als Messgerät (und die Forderung <span class="m">q → 0</span>) benannt ·
> mindestens zwei tragfähige Argumente für die Eigenständigkeit des Feldes, davon eines quantitativ
> (Energiedichte) ·
> Nahwirkung gegen Fernwirkung ausdrücklich gegenübergestellt ·
> begründetes Gesamturteil, das den berechtigten Kern der Aussage benennt, statt sie nur zu verwerfen.

---

## 6 · Abschluss

`<section id="abschluss">`, `.stufe`-Nummer **6**,
Überschrift **Zusammenfassung und Selbstcheck**.

### 6.1 Vier Kernaussagen (je ein `<div class="merksatz">`)

**Kernaussage 1 — Das Feld gehört der Stelle, nicht dem Ladungspaar.**
Titel: *Vom Kraftgesetz zum Feld.* Das Coulombgesetz beschreibt immer **zwei** Ladungen
gleichzeitig. Die Feldstärke <span class="m">E⃗ = F⃗/q</span> beschreibt **eine** Stelle im Raum:
Verdoppelt man die Probeladung, verdoppelt sich die Kraft, der Quotient bleibt. Weil die
Probeladung herausfällt, ist <span class="m">E⃗</span> eine Eigenschaft des Raumes. Das ist der
Übergang von der Fernwirkung zur **Nahwirkung** — und er ist keine Geschmacksfrage, denn Felder
tragen Energie (<span class="m">w = ½·ε₀·ε_r·E²</span>) und brauchen Zeit, um sich auszubreiten.

- `data-tex`: `\vec E = \dfrac{\vec F}{q}, \qquad F = |q|\cdot E, \qquad [E] = 1\,\tfrac{\mathrm N}{\mathrm C} = 1\,\tfrac{\mathrm V}{\mathrm m}`
- `data-plain`: `E = F/q,   F = |q| · E,   [E] = 1 N/C = 1 V/m`

**Kernaussage 2 — Im homogenen Feld ist die Feldstärke das Spannungsgefälle.**
Titel: *E = U/d — und was darin nicht steht.* Zwischen zwei Platten ist
<span class="m">E</span> überall gleich groß; in der Formel steht der Abstand **der Platten
voneinander**, nicht der Abstand **von** einer Platte. Die Formel ist keine Definition, sondern
folgt aus der Arbeit: Verschiebt man <span class="m">q</span> von Platte zu Platte, ist
<span class="m">W = F·d = q·E·d</span> und zugleich <span class="m">W = q·U</span> — gleichsetzen,
<span class="m">q</span> kürzen, fertig. Dass die Arbeit dabei wegunabhängig ist, ist dieselbe
Eigenschaft, die im Schwerefeld die Hubarbeit wegunabhängig macht.

- `data-tex`: `q\,U = q\,E\,d \quad \Longrightarrow \quad E = \dfrac{U}{d}`
- `data-plain`: `q·U = q·E·d   ⟹   E = U/d`

**Kernaussage 3 — Die Kapazität ist reine Geometrie.**
Titel: *C = Q/U ist eine Messvorschrift, keine Abhängigkeit.* Aus
<span class="m">C = Q/U</span> folgt **nicht**, dass <span class="m">C</span> von
<span class="m">Q</span> oder <span class="m">U</span> abhinge — genauso wenig, wie
<span class="m">R = U/I</span> den Widerstand von der Stromstärke abhängig macht. Verdoppelt man
<span class="m">U</span>, verdoppelt sich <span class="m">Q</span> mit; der Quotient bleibt, und
genau das ist die Aussage der Ursprungsgeraden im <span class="m">Q</span>-<span class="m">U</span>-Diagramm.
Was <span class="m">C</span> wirklich festlegt, sind Fläche, Abstand und Dielektrikum.

- `data-tex`: `C = \dfrac{Q}{U} = \varepsilon_0\,\varepsilon_r\,\dfrac{A}{d}`
- `data-plain`: `C = Q/U = ε₀ · ε_r · A/d`

**Kernaussage 4 — Erst die Randbedingung, dann die Energieformel.**
Titel: *Angeschlossen oder abgetrennt?* Die gespeicherte Energie ist die Dreiecksfläche unter der
Kennlinie <span class="m">Q(U)</span>, deshalb der Faktor ½: Die Spannung wächst beim Laden von
null an mit. Welche der beiden gleichwertigen Formen du brauchst, entscheidet allein die Frage,
welche Größe festgehalten wird. Bleibt die Quelle angeschlossen, ist <span class="m">U</span> fest
und <span class="m">W = ½·C·U²</span> die richtige Wahl; ist die Quelle abgetrennt, ist
<span class="m">Q</span> fest und <span class="m">W = Q²/(2C)</span> die richtige. Dieselbe Handlung
— Platten auseinanderziehen — halbiert im einen Fall die Energie und verdoppelt sie im anderen.

- `data-tex`: `W = \tfrac{1}{2}\,Q\,U = \tfrac{1}{2}\,C\,U^{2} = \dfrac{Q^{2}}{2C}`
- `data-plain`: `W = ½·Q·U = ½·C·U² = Q²/(2C)`

### 6.2 Blick aufs Zentralabitur (`<div class="hinweis">`)

**Im Zentralabitur.** Das elektrische Feld steht im Inhaltsfeld *Ladungen, Felder und Induktion*
und kommt fast nie als reine Kondensatoraufgabe vor, sondern als Baustein größerer Aufgaben.
Diese Gestalten begegnen dir regelmäßig:

- **Kapazität und Ladung aus der Geometrie**, meist als Einstiegsteil im Anforderungsbereich I.
  Die Punkte fallen dort selten wegen der Formel, sondern wegen der Einheiten: cm² → m² ist der
  Faktor <span class="m">10⁻⁴</span>, nicht <span class="m">10⁻²</span>.
- **Die Fallunterscheidung „Quelle angeschlossen / abgetrennt"** als Begründungsteil. Erkennbar an
  Formulierungen wie *„der Kondensator wird von der Spannungsquelle getrennt"* oder *„bei
  angeschlossener Quelle"*. Wer diesen Halbsatz überliest, rechnet die ganze Teilaufgabe konsistent
  falsch — und bekommt dafür keine Folgefehlerpunkte, weil der Ansatz selbst falsch ist.
- **Energiebilanzen**: Woher kommt die Energie beim Auseinanderziehen? Wohin geht sie beim
  Einschieben eines Dielektrikums? Verlangt wird eine Bilanz mit benannter Quelle und benanntem
  Empfänger, nicht der bloße Vergleich zweier Zahlen.
- **Auswertung von Diagrammen**: aus einer <span class="m">Q(U)</span>-Kennlinie die Kapazität als
  **Steigung** und die Energie als **Fläche** bestimmen; aus einer <span class="m">C(d)</span>-Kurve
  auf den <span class="m">1/d</span>-Zusammenhang schließen. Linearisieren (also
  <span class="m">C</span> gegen <span class="m">1/d</span> auftragen) ist eine gängige Teilaufgabe.
- **Feldlinien- und Äquipotentialbilder beurteilen**, oft mit einem vorgegebenen, fehlerhaften
  Schülerbild: sich schneidende Linien, Linien, die schräg auf einen Leiter treffen, oder eine
  Zahlenangabe aus der Liniendichte zwischen zwei verschiedenen Bildern.
- **Anschluss**: Im Folgemodul kommt die Bewegung geladener Teilchen im Feld dazu
  (<span class="m">q·U = ½·m·v²</span>, Ablenkung im Querfeld). Dort wird
  <span class="m">E = U/d</span> als bekannt vorausgesetzt — ebenso im Wien-Filter des
  Magnetfeldmoduls.

### 6.3 Selbstcheck (`.karte` mit `<h3>Selbstcheck</h3>`, sechs `.check`-Zeilen)

Vorspann: *Hak ehrlich ab. Was du hier nicht ankreuzen kannst, holst du besser jetzt nach als in
der Klausur.*

1. Ich kann die elektrische Feldstärke über <span class="m">E⃗ = F⃗/q</span> definieren, erklären,
   warum der Wert nicht von der Probeladung abhängt, und begründen, warum das Feld mehr ist als eine
   andere Schreibweise für das Coulombgesetz.
2. Ich kann Feldlinienbilder lesen und beurteilen: Tangente als Kraftrichtung, Dichte als Maß für
   die Feldstärke, keine Schnittpunkte, senkrechter Auftreffwinkel auf Leiteroberflächen — und ich
   kann sagen, warum eine Feldlinie im Allgemeinen **keine** Bahnkurve ist.
3. Ich kann das homogene Feld des Plattenkondensators beschreiben und
   <span class="m">E = U/d</span> über die Arbeit an einer Probeladung herleiten, statt die Formel
   nur zu benutzen.
4. Ich kann die Kapazität aus Fläche, Plattenabstand und <span class="m">ε_r</span> berechnen,
   Ergebnisse in pF, nF und µF sicher umrechnen und begründen, warum
   <span class="m">C</span> **nicht** von der angelegten Spannung abhängt.
5. Ich kann die gespeicherte Energie mit <span class="m">W = ½·C·U² = Q²/(2C)</span> berechnen, den
   Faktor ½ über die Dreiecksfläche im <span class="m">Q</span>-<span class="m">U</span>-Diagramm
   begründen und die Energie über die Energiedichte <span class="m">w = ½·ε₀·ε_r·E²</span>
   gegenrechnen.
6. Ich kann bei einer Veränderung am Kondensator zuerst entscheiden, ob die Spannung oder die
   Ladung festgehalten wird, daraus die richtige Formel wählen und die Energiebilanz mit benannter
   Quelle angeben — auch bei eingeschobenem Dielektrikum.

### 6.4 Export und Druck

Knopfleiste wie im Referenzmodul: `Ergebnisse kopieren` (`id="bExport"`) und
`Als Arbeitsblatt drucken`. Darunter der graue Hinweis, dass nichts gespeichert wird und die
Ergebnisse die Seite nur über den Kopieren-Knopf verlassen.

`var namen = {…}` am Skriptende — **jeder** automatisch ausgewertete Schlüssel muss hier stehen,
sonst fehlt die Aufgabe im Export:

```
vw1: "Vorwissen 1 – Coulombgesetz, Abstandsabhängigkeit"
vw2: "Vorwissen 2 – Spannung als Energie pro Ladung"
vw3: "Vorwissen 3 – Wegunabhängigkeit der Arbeit"
sim1:"Simulation 1 – Was beim Abtrennen konstant bleibt"
sim2:"Simulation 2 – Energiebilanz in beiden Betriebsarten"
ue1: "Aufgabe 1 – Kapazität aus der Geometrie"
ue2: "Aufgabe 2 – Ladung auf den Platten"
ue3: "Aufgabe 3 – Aussagen über Feldlinien"
ue4: "Aufgabe 4 – Zuordnung Abhängigkeit zu Diagramm"
ue5: "Aufgabe 5 – nötige Plattenfläche eines Folienkondensators"
ue6: "Aufgabe 6 – Arbeit beim Auseinanderziehen"
```

Die offenen Aufgaben `ue7`, `ue8` und `ue9` werden nicht automatisch ausgewertet und erscheinen —
wie im Referenzmodul — nicht im Export. Der Exporttext nennt sie am Ende trotzdem in einer Zeile:
*„Drei Bewertungsaufgaben (ue7–ue9) wurden nicht automatisch ausgewertet."*

### 6.5 Anschlusshinweis (`<div class="hinweis">`)

**Wie es weitergeht.** Bis hierher ist jede Ladung brav an ihrem Platz geblieben: Die Platten sind
geladen, das Feld steht, und die Probeladung war ein gedachtes Messgerät. Im nächsten Schritt lässt
du sie los. Eine Ladung, die im Feld beschleunigt wird, nimmt die Energie
<span class="m">q·U</span> auf und wird dabei schnell — die Verbindung
<span class="m">q·U = ½·m·v²</span> ist der Einstieg ins Folgemodul. Tritt sie dagegen **quer** ins
Feld ein, bekommst du dieselbe Mathematik wie beim waagerechten Wurf aus der Einführungsphase,
nur mit <span class="m">a = q·E/m</span> statt <span class="m">g</span>. Und dann ist auch die
Frage aus 2.4 fällig, die hier offengeblieben ist: Warum eine Feldlinie im Allgemeinen eben doch
keine Flugbahn ist.

---

## Lehrerteil

`<details class="lehrer">` mit `<summary>Für die Lehrkraft</summary>`, am Ende von Abschnitt 6,
verschwindet beim Drucken (`@media print` aus dem Referenzmodul, unverändert übernommen).

### Einordnung

Inhaltsfeld **„Ladungen, Felder und Induktion"** (Kernlehrplan Physik, gymnasiale Oberstufe NRW,
Leistungskurs). Dieses Modul deckt den ersten Teil des Inhaltsfelds ab: Feldbegriff, elektrische
Feldstärke, Feldlinien und Äquipotentialflächen, das homogene Feld des Plattenkondensators,
Kapazität und Energie des elektrischen Feldes.

Kompetenzbereiche mit Schwerpunkt: **Umgang mit Fachwissen** (Feldbegriff, Kapazität, Energie),
**Erkenntnisgewinnung** (die Herleitung von <span class="m">E = U/d</span> in 3.2, das Auswerten
der beiden Diagramme in der Simulation), **Kommunikation** (Feldlinienbilder lesen und beurteilen,
ue3 und ue4) und **Bewertung** (ue7, ue8, ue9). Die drei Aufgaben im Anforderungsbereich III sind
kein Zusatz, sondern der Ort, an dem der Leistungskurs sich vom Grundkurs unterscheidet.

Vorausgesetzt werden: Coulombgesetz und Ladungsbegriff aus der Sekundarstufe I, Spannung als
Energie pro Ladung (<span class="m">U = W/q</span>), Arbeit als
<span class="m">W = F·s</span> und die Wegunabhängigkeit der Hubarbeit im Schwerefeld aus der
Mechanik der Einführungsphase. Genau diese drei Punkte prüfen die Vorwissensfragen vw1 bis vw3.

**Stellung in der Reihe:** Dieses Modul liegt **vor** `physik-q1-magnetisches-feld.html` und
`physik-q1-induktion.html`. Der Wien-Filter im Magnetfeldmodul benutzt
<span class="m">E = U/d</span> und den Begriff des homogenen Feldes als bekannt; die dritte
Vorwissensfrage dort ist wortgleich auf dieses Modul abgestimmt. Unmittelbar anschließen sollte
`physik-q1-geladene-teilchen-e-feld` — die Abgrenzungstabelle im Kopf dieses Dokuments hält fest,
was dorthin gehört und hier ausdrücklich **nicht** gerechnet wird.

*Offen markiert und als didaktische Setzung zu lesen, nicht als Vorgabe des Kernlehrplans:*

- die Reihenfolge „Feldbegriff → Feldlinien → homogenes Feld → Kapazität" (der Kernlehrplan nennt
  die Inhalte, nicht ihre Abfolge);
- die Aufteilung des Inhaltsfelds auf dieses und die beiden Folgemodule;
- die Behandlung des Dielektrikums über <span class="m">ε_r</span> als Materialkonstante, ohne die
  Polarisation mikroskopisch zu modellieren. Für den LK ist das vertretbar, aber es ist eine
  Auswahl — wo die Fachschaft die Polarisation behandeln will, gehört sie an das Ende von 3.4.

### Zeitbedarf

Ausgelegt auf **135 Minuten**, also eine Doppelstunde plus eine Einzelstunde oder drei
Einzelstunden (Tabelle im Modul in `<div class="tabelle">` kapseln):

| Abschnitt | Zeit | Sozialform |
|---|---|---|
| 1 Einstieg (Aufhänger, drei Vorwissensfragen) | 10 min | Plenum, Fragen in Einzelarbeit |
| 2 Feldbegriff, Feldstärke, Superposition, Feldlinien | 25 min | lehrergelenkt, Merksätze sichern |
| 3 Plattenkondensator: homogenes Feld, <span class="m">E = U/d</span>, Kapazität, Energie, Fallunterscheidung | 35 min | Plenum mit zwei Sicherungsphasen, Details-Blöcke je nach Kurs |
| 4 Simulation mit Beobachtungsauftrag und den zwei MC-Fragen | 25 min | Partnerarbeit am Gerät |
| 5 Übungen (Auswahl, siehe Differenzierung) | 30 min | Einzel- oder Partnerarbeit |
| 6 Abschluss, Selbstcheck, Export | 10 min | Plenum |

**Schnittstellen für die Aufteilung.** Bei einer Doppelstunde plus Einzelstunde ist der natürliche
Schnitt **nach 3.4** (Kapazität aus der Geometrie): Die erste Einheit endet mit einer rechenbaren
Formel, die zweite beginnt mit der Energie und läuft über die Simulation in die Übungen. Bei drei
Einzelstunden liegen die Schnitte nach Abschnitt 2 und nach Abschnitt 3.

**Realistisch in einer Doppelstunde** schaffbar sind die Abschnitte 1 bis 3 vollständig sowie ue1
und ue2. Wer die Herleitung in 3.2 im Plenum entwickelt, statt sie im Details-Block lesen zu
lassen, braucht dafür allein 12 bis 15 Minuten. Die drei Bewertungsaufgaben ue7 bis ue9 sind
bewusst als Material für Hausaufgabe, Vertretungsstunde oder Klausurvorbereitung angelegt — für die
Stunde reicht **eine** davon.

### Typische Schülerfehler — und wo im Unterrichtsgespräch anzuhalten ist

**(1) „Die Kapazität hängt von der Spannung ab."** Der Leitfehler dieses Moduls, ausgelöst durch
die Form <span class="m">C = Q/U</span>. Er ist deshalb so hartnäckig, weil die Formel den Fehler
optisch nahelegt.
→ **Anhalten** direkt nach der Definition in 3.3, bevor die Geometrieformel kommt. Analogie an die
Tafel: <span class="m">R = U/I</span> — hängt der Widerstand einer Glühlampe von der Stromstärke
ab? Danach die Gegenfrage: *„Wenn C mit U wüchse, wäre die Q-U-Kennlinie dann noch eine Gerade?"*
Die Simulation zeigt es in zehn Sekunden: Spannungsregler bewegen, die Gerade im
<span class="m">Q</span>-<span class="m">U</span>-Diagramm bleibt dieselbe, nur der Arbeitspunkt
wandert.

**(2) „Nahe an der Platte ist das Feld stärker."** Die Intuition stammt vom Radialfeld und ist dort
richtig — im Plattenkondensator nicht.
→ **Anhalten** bei Merksatz 3 in 3.1. Das Argument gemeinsam entwickeln lassen, nicht vorsagen: Jede
Platte für sich erzeugt <span class="m">E = σ/(2·ε₀)</span> unabhängig vom Abstand (jedes Flächenelement wirkt mit 1/r²
schwächer, dafür tragen ∼ r² mehr Elemente bei); zwischen den Platten addieren sich beide Beiträge
zu <span class="m">σ/ε₀</span>, außerhalb heben sie sich auf. Vorsicht: Das Kompensationsargument „eigener
Beitrag wächst, fremder schrumpft“ ist falsch, denn beide Beiträge sind einzeln abstandsunabhängig. Als
Sichtbeleg die Feldlinien in der Simulation: Sie sind über die ganze Strecke gleich dicht.
Direkt daran anschließen: In <span class="m">E = U/d</span> ist <span class="m">d</span> der
Abstand **der Platten**, nicht der Abstand **von** einer Platte.

**(3) „Die Feldlinie ist die Flugbahn."** Wird in ue3 direkt geprüft.
→ **Anhalten** in 2.4 bei Fehlvorstellung 1. Der schnellste Weg ist die Analogie zum waagerechten
Wurf: Die Gewichtskraft zeigt nach unten, der Stein fliegt trotzdem nicht senkrecht. Wichtig ist,
den harmlosen Sonderfall mitzunennen (Start aus der Ruhe **und** gerade Feldlinien) — sonst wirkt
der Hinweis wie eine Spitzfindigkeit, weil im Plattenkondensator ja scheinbar alles passt.

**(4) Flächen- und Längeneinheiten.** <span class="m">150 cm² = 0,015 m²</span>, nicht
<span class="m">1,5 m²</span>; <span class="m">0,50 mm = 5,0·10⁻⁴ m</span>. In ue1 kostet dieser
Fehler zwei Zehnerpotenzen.
→ **Anhalten** beim ersten gemeinsamen Einsetzen. Regel für den Kurs: **Erst alles in SI, dann
einsetzen — und jede Zahl mit ihrer Einheit hinschreiben.** Die Einheitenprobe
<span class="m">(F/m)·m²/m = F</span> einmal vormachen und danach verlangen.

**(5) Der vergessene Faktor ½.** <span class="m">W = Q·U</span> statt
<span class="m">W = ½·Q·U</span>.
→ **Anhalten** in 3.5 am <span class="m">Q</span>-<span class="m">U</span>-Diagramm. Die Frage
*„Gegen welche Spannung wird die erste Ladungsportion transportiert?"* führt von selbst auf die
Dreiecksfläche. Das Bild in der Simulation (gefülltes Dreieck mit mitlaufendem Zahlenwert) ist
genau dafür gebaut — es lohnt sich, hier zwei Minuten stehenzubleiben.

**(6) Die Randbedingung wird überlesen.** *„Die Quelle wird abgetrennt"* ist ein Halbsatz, der die
ganze Aufgabe umdreht. Wer ihn übersieht, rechnet mit fester Spannung weiter und bekommt in ue6 das
Ergebnis −1,3 µJ statt +4,0 µJ, also sogar das falsche Vorzeichen.
→ **Anhalten** in 3.7 und die Zweispaltentabelle gemeinsam ausfüllen lassen, nicht vorlesen.
Arbeitsauftrag für die Klausur: **Unterstreiche in jeder Kondensatoraufgabe zuerst den Satz, der
sagt, ob die Quelle dranbleibt.** Danach den Beobachtungsauftrag der Simulation durchführen —
er ist genau auf diesen Punkt gebaut.

**(7) „Mehr Feldlinien heißt mehr Ladung."** Die absolute Linienzahl wird zwischen zwei Bildern
verglichen.
→ **Anhalten** bei Fehlvorstellung 2 am Ende von Abschnitt 2 und dort ausdrücklich die
Deckelungsmeldung der Simulation vorwegnehmen: Bei 26 Linien ist Schluss, obwohl
<span class="m">E</span> weiter steigt. Sonst zieht der Kurs genau den Schluss, den die Meldung
verhindern soll.

**(8) Superposition mit Beträgen.** Zwei Feldbeiträge werden addiert, ohne auf die Richtung zu
achten.
→ **Anhalten** bei Merksatz 2 in 2.3. Eine Minute an der Tafel: zwei gleiche positive Ladungen,
Feld in der Mitte — null; zwei entgegengesetzte Ladungen, Feld in der Mitte — doppelt. Dieselbe
Anordnung, zwei völlig verschiedene Ergebnisse.

**(9) <span class="m">ε_r</span> landet im Nenner.** In ue5 führt das auf einen Faktor
<span class="m">4,5² = 20,25</span> daneben.
→ **Anhalten** in 3.4, wo <span class="m">ε_r</span> eingeführt wird. Merkfrage: *„Macht ein
Dielektrikum den Kondensator besser oder schlechter?"* Wer weiß, dass <span class="m">C</span>
größer wird, kann die Formel selbst kontrollieren, ohne sie auswendig zu können.

### Differenzierung

**Für schnellere Lernende:**

- **Feldstärke zwischen den Platten aus der Flächenladungsdichte herleiten.** Eine einzelne
  geladene Ebene erzeugt <span class="m">E = σ/(2ε₀)</span>; zwei entgegengesetzt geladene Ebenen
  ergeben zwischen sich <span class="m">E = σ/ε₀</span> und außerhalb null. Daraus folgt
  <span class="m">C = ε₀A/d</span> ohne Umweg — und nebenbei das Argument für den Faktor ½ in der
  Plattenkraft <span class="m">F = ½·Q·E</span> aus Details-Block 4: Eine Platte spürt nur das Feld
  der anderen.
- **Die Kraft über die Energie bestimmen.** <span class="m">F = dW/dd</span> mit
  <span class="m">W(d) = Q²d/(2ε₀ε_rA)</span> nachrechnen und mit der Kraftbetrachtung vergleichen.
  Das ist ein sauberer Anschluss an die Ableitung aus der Analysis und zugleich die Kontrollrechnung
  aus ue6.
- **Teilweise gefülltes Dielektrikum.** Eine Glasplatte der Dicke <span class="m">d/2</span>
  zwischen den Platten: Reihenschaltung zweier Kondensatoren, <span class="m">1/C = 1/C₁ + 1/C₂</span>.
  Mit den Simulationswerten (<span class="m">C_Luft = 17,708 pF</span>,
  <span class="m">ε_r = 6,0</span>) ergibt das <span class="m">C = 30,36 pF</span> statt
  <span class="m">106,25 pF</span> bei voller Füllung — die Hälfte des Raums bringt eben nicht die
  halbe Wirkung.
- **Größenordnungen abschätzen:** Wie groß müsste ein Plattenkondensator sein, um die Energie einer
  AA-Batterie (rund 10 kJ) zu speichern? Der Vergleich mit einem Superkondensator (mehrere hundert
  Farad, aber nur wenige Volt) trägt eine ganze Diskussionsrunde und bereitet die Bewertungsaufgabe
  ue7 vor.
- **Zusatz zu ue8:** Bei welcher Betriebsart wird die Glasplatte **hineingezogen**? (Antwort: in
  beiden, denn das Feld verrichtet in beiden Fällen Arbeit an ihr — der Unterschied liegt allein in
  der Bilanz der Quelle.)

**Für Lernende, die mehr Zeit brauchen:**

- Pflichtteil sind **ue1, ue2 und ue4**. ue1 und ue2 sind reines Handwerk mit Einheiten, ue4
  verlangt keine Rechnung und trägt trotzdem die zentrale Einsicht des Moduls.
- Die Details-Blöcke in 3.2 (Herleitung <span class="m">E = U/d</span>) und 3.5 (Herleitung des
  Faktors ½) können übersprungen werden; die Merksätze 2 und 4 tragen das Ergebnis auch allein.
  Was **nicht** entfallen darf, ist die Fallunterscheidung in 3.7 — ohne sie ist die Hälfte der
  Aufgaben nicht entscheidbar.
- Die Tabelle aus 3.7 als Merkblatt (eine halbe DIN-A5-Seite: links „Quelle angeschlossen: U fest",
  rechts „Quelle abgetrennt: Q fest", darunter je drei Formeln) austeilen und in den Übungen
  benutzen lassen. Damit sind ue4 und ue6 ohne weitere Hilfe lösbar.
- Von den drei Bewertungsaufgaben genügt **ue7**. Sie hängt an einer einzigen Aussage und braucht
  nur zwei Zahlenpaare, während ue8 zwei Fälle sauber trennen muss und ue9 eine offene
  wissenschaftstheoretische Argumentation verlangt.
- Der Beobachtungsauftrag lässt sich halbieren: nur Durchgang 1 und 2 für die Größe
  <span class="m">E</span>, ohne die Energiefrage. Die Energiefrage kommt dann über sim2 im Plenum.

### Bezug zu Realexperimenten

- **Plattenkondensator mit Elektrometer — das Kernexperiment.** Zwei Metallplatten auf
  Isolierstativen, Ladung über eine Hochspannungsquelle oder einen Bandgenerator, Anzeige über ein
  statisches Elektrometer (Messverstärker mit hohem Eingangswiderstand). Quelle **abtrennen**, dann
  die Platten auseinanderziehen: Die angezeigte Spannung steigt sichtbar, obwohl niemand nachlädt.
  Das ist Durchgang 2 des Beobachtungsauftrags in echt und der überzeugendste Beleg dafür, dass beim
  Abtrennen die Ladung und nicht die Spannung festgehalten wird. Danach eine Glasplatte
  einschieben: Die Spannung fällt — Fall 2 aus ue8. **Aufwand:** 10 Minuten, sofern das Elektrometer
  vorhanden ist. **Stolperstelle:** Bei feuchter Luft läuft die Ladung über die Isolatoren ab;
  Platten vorher abföhnen.
- **Kapazitätsmessung mit dem Multimeter.** Jedes bessere Vielfachmessgerät hat einen
  Kapazitätsbereich bis einige hundert nF. Zwei Aluminiumfolien (Haushaltsfolie) mit einem Blatt
  Papier dazwischen, aufeinandergelegt und mit einem Buch beschwert, liefern direkt messbare Werte.
  Die Lernenden messen <span class="m">C</span>, messen Fläche und Papierdicke (Mikrometerschraube
  oder „100 Blatt messen und teilen") und bestimmen daraus <span class="m">ε_r</span> des Papiers —
  Sollwert rund 2,2. Das ist ue5 rückwärts und eine sehr gute Fehlerdiskussion, weil der Kontakt
  zwischen Folie und Papier nie perfekt ist und der gemessene Wert deshalb zu klein ausfällt.
- **Feldlinienbilder sichtbar machen.** Grießkörner oder kurze Fasern in Rizinus- oder Speiseöl,
  darin zwei Elektroden (Punkt–Punkt, Punkt–Platte, Platte–Platte) an Hochspannung. Die Körner
  richten sich längs der Feldlinien aus. Wichtig für die Nachbesprechung: Man sieht die
  **Richtung**, aber keine Pfeilspitze — die Orientierung steckt nicht im Bild, sondern in der
  Vorzeichenkonvention. Genau das ist der Punkt aus 2.4.
- **Durchschlag in Luft.** Mit Bandgenerator oder Funkeninduktor den Überschlag zeigen und aus der
  gemessenen Schlagweite die Feldstärke abschätzen: rund 3 kV pro Millimeter. Der Bezug zur
  Simulation ist direkt — die Durchschlagsmeldung erscheint bei
  <span class="m">E > 3·10⁶ V/m</span>. Danach die Frage, warum ein Blitz mehrere Kilometer
  überbrückt, obwohl das rechnerisch Milliarden Volt bräuchte (Antwort: Vorentladungskanal, das
  Feld ist nicht homogen) — eine gute Brücke zwischen Modell und Wirklichkeit.
- **Faradayscher Käfig.** Ein Handy in einer geschlossenen Blechdose verliert den Empfang, ein
  Radio in einem Drahtnetz verstummt. Zusammen mit der Aussage aus ue3, dass Feldlinien senkrecht
  auf Leiteroberflächen stehen, ergibt das die Abschirmung als Anwendung — und den Anschluss an das
  Thema Äquipotentialflächen.
- **Kondensator als Bauteil.** Eine Handvoll ausgelöteter Bauteile herumgeben: Keramik (pF bis nF),
  Folie (nF bis µF), Elektrolyt (µF bis mF), Superkondensator (F). Die Lernenden ordnen sie nach
  Kapazität und begründen die Bauform aus <span class="m">C = ε₀ε_rA/d</span>. Ein aufgeschnittener
  Folienkondensator zeigt den gewickelten Aufbau aus ue5 unmittelbar. **Aufwand:** null, wenn die
  Sammlung Altbauteile hat.
- **Messwerterfassung (falls vorhanden).** Mit einem Ladungsverstärker und einem beweglichen
  Plattenpaar lässt sich <span class="m">C(d)</span> punktweise aufnehmen und gegen
  <span class="m">1/d</span> auftragen. Die Linearisierung ist eine typische Abiturteilaufgabe und
  liefert aus der Steigung <span class="m">ε₀·A</span> — also eine echte Messung der elektrischen
  Feldkonstante. Erfahrungsgemäß liegt das Ergebnis 10 bis 20 % zu hoch, weil das Streufeld am Rand
  mitmisst; das ist keine Panne, sondern der beste Anlass, über die Idealisierung „homogenes Feld"
  zu sprechen.

---

## Checkliste für den Bauagenten

### Benötigte Bausteine und ihre Schlüssel

| Schlüssel | Baustein | `data`-Attribut | Optionen / Besonderheit | AB | Fundstelle |
|---|---|---|---|---|---|
| `vw1` | Multiple Choice | `data-mc="vw1"` | 3 Optionen, `r: 1` | — | 1.2 |
| `vw2` | Multiple Choice | `data-mc="vw2"` | 3 Optionen, `r: 1` | — | 1.2 |
| `vw3` | Multiple Choice | `data-mc="vw3"` | 3 Optionen, `r: 2` | — | 1.2 |
| `sim1` | Multiple Choice | `data-mc="sim1"` | **4** Optionen, `r: 1` | II | 4.9 |
| `sim2` | Multiple Choice | `data-mc="sim2"` | 3 Optionen, `r: 0` | II | 4.9 |
| `ue1` | Zahleneingabe | `data-num="ue1"` | `wert: 265.6`, `"pF"`, `tol: 2`, `alt: 0.2656 "nF"`, Distraktoreinheit `pC` | I | 5.1 |
| `ue2` | Zahleneingabe | `data-num="ue2"` | `wert: 6.375`, `"nC"`, `tol: 0.05`, `alt: 6375 "pC"`, Distraktoreinheit `nF` | I | 5.2 |
| `ue3` | Multiple Choice | `data-mc="ue3"` | **4** Optionen, `r: 1`, **mit** Hilfen 1–3 | I | 5.3 |
| `ue4` | Zuordnung | `data-check="zuordnung"` | 4 SVG-Diagramme, Lösung **B · D · C · A**, **mit** Hilfen 1–3 | II | 5.4 |
| `ue5` | Zahleneingabe | `data-num="ue5"` | `wert: 2.01`, `"m²"`, `tol: 0.05`, `alt: 20079 "cm²"`, Distraktoreinheiten `m`, `F` | II | 5.5 |
| `ue6` | Zahleneingabe | `data-num="ue6"` | `wert: 4.0`, `"µJ"`, `tol: 0.05`, `alt: 4000 "nJ"`, Distraktoreinheit `µW`, **`sonder`-Liste** (2,0 · 6,0 · −1,33 · 0,67) | II | 5.6 |
| `ue7` | offene Aufgabe | `data-loesung="ue7"` | `<textarea>`, Lösung in `.hilfe-text[data-stufe="9"]` | III | 5.7 |
| `ue8` | offene Aufgabe | `data-loesung="ue8"` | `<textarea>`, Lösung in `.hilfe-text[data-stufe="9"]` | III | 5.8 |
| `ue9` | offene Aufgabe | `data-loesung="ue9"` | `<textarea>`, Lösung in `.hilfe-text[data-stufe="9"]` | III | 5.9 |

**Hilfestufen 1–3** (`<button data-hilfe="1|2|3">` plus `.hilfe-text[data-stufe="1|2|3"]`) bekommen:
`ue1`, `ue2`, **`ue3`**, **`ue4`**, `ue5`, `ue6` — also **alle sechs** auswertbaren Übungsaufgaben.

> **Abweichung vom Referenzmodul, bewusst so gewollt.** Dort haben nur die Zahleneingaben Hilfen.
> `CLAUDE.md` verlangt für Abschnitt 5 aber „jede mit dreistufigem Hilfesystem". Die Hilfe-Engine
> ist dafür ohne Änderung geeignet: Sie sucht den Hilfetext über
> `btn.closest(".aufgabe").querySelector('.hilfe-text[data-stufe="…"]')`, arbeitet also pro
> Aufgabenkasten und nicht pro Aufgabentyp. Für `ue3` und `ue4` werden die Hilfen genau wie bei den
> Zahleneingaben unter die Rückmeldung gesetzt.

`ue7`, `ue8` und `ue9` bekommen **keine** Stufen 1–3, sondern nur `data-stufe="9"` mit erwarteter
Argumentation **und** fetten Bewertungskriterien (mit `·` getrennt), wie in `bausteine.md` § 5.

### Zwei Stellen, an denen generischer Code angefasst werden muss

1. **Zuordnungs-Engine.** Im Referenzmodul steht dort hart `ergebnisse.a3 = …`. Für dieses Modul
   muss daraus `ergebnisse.ue4 = …` werden. Ebenso sind die beiden Rückmeldungstexte
   modulspezifisch: der Erfolgstext aus der Begründungstabelle in 5.4, der Teilerfolgstext wörtlich
   aus 5.4 („Noch nicht alles passt. Geh jede Zeile in zwei Schritten durch …").
2. **`var namen = {…}`** am Skriptende: die elf Einträge aus 6.4. Fehlt ein Schlüssel, fällt die
   Aufgabe stillschweigend aus dem Export.

Alles Übrige — `<style>`-Block, `formelnRendern()`, MC-Engine, Zahlen-Engine, Hilfesystem,
Export, Druck-CSS — wird unverändert übernommen. Einzige erlaubte CSS-Änderung sind die drei
Akzent-Tokens; für Physik bleiben sie ohnehin, wie sie im Referenzmodul stehen
(`#1d4ed8` · `#eff6ff` · `#bfdbfe`).

### Simulationsbausteine

| Element | `id` bzw. `data`-Attribut | Bereich / Werte |
|---|---|---|
| Canvas Kondensator | `cvKond` | `width="1000" height="360"` |
| Canvas C-d-Diagramm | `cvCd` | `width="1000" height="200"` |
| Canvas Q-U-Diagramm | `cvQU` | `width="1000" height="200"` |
| Regler Spannung `U` | `rU` | 0 … 500, Schritt 10, Start **200** (V), Anzeige `lU` |
| Regler Plattenabstand `d` | `rD` | 5 … 50, Schritt 1, Start **20** (mm), Anzeige `lD` |
| Regler Kantenlänge `L` | `rL` | 10 … 30, Schritt 1, Start **20** (cm), Anzeigen `lL` und `lA` |
| Dielektrikum | `data-eps="1.00" \| "2.20" \| "6.00"` | Luft (Start) · Papier · Glas, aktiver Knopf `primaer` |
| Betriebsart | `data-modus="quelle" \| "isoliert"` | Start `quelle`, aktiver Knopf `primaer` |
| Zurücksetzen | `bReset` | Modus `quelle`, U = 200 V, d = 20 mm, L = 20 cm, Luft |
| Anzeige Kapazität | `aC` | pF, 2 Stellen, Start `17,71` |
| Anzeige Ladung | `aQ` | nC, 3 Stellen, Start `3,542` |
| Anzeige Spannung | `aU` | V, 1 Stelle, Start `200,0` |
| Anzeige Feldstärke | `aE` | kV/m, 2 Stellen, Start `10,00` |
| Anzeige Energie | `aW` | µJ, 4 Stellen, Start `0,3542` |
| Hinweisfeld | `simHinweis` | leer, solange keine der drei Meldungen aus 4.5 greift |

Kein Regler wird jemals `disabled`; die Modus-Logik aus 4.2 (Punkt 3) fängt den Konflikt ab,
indem sie bei Bewegung des Spannungsreglers in den Modus `quelle` zurückspringt und das meldet.

### Prüfpunkte vor der Abnahme

1. **Startwerte der Simulation** (Luft, Modus `quelle`): `C = 17,71 pF` · `Q = 3,542 nC` ·
   `U = 200,0 V` · `E = 10,00 kV/m` · `W = 0,3542 µJ`. Weicht eine Anzeige in der zweiten
   Nachkommastelle ab, ist ein Umrechnungsfaktor falsch.
2. **Beobachtungsauftrag nachfahren** (Tabelle in 4.8): Bei `d = 40 mm` mit angeschlossener Quelle
   `C = 8,85 pF`, `Q = 1,771 nC`, `E = 5,00 kV/m`, `W = 0,1771 µJ`; nach Abtrennen bei `d = 40 mm`
   `U = 400,0 V`, `Q = 3,542 nC`, `E = 10,00 kV/m`, `W = 0,7083 µJ`. Die Feldstärke muss im zweiten
   Durchgang **exakt** auf 10,00 kV/m stehen bleiben — daran hängen `sim1` und der ganze Auftrag.
3. **Feldlinienzahl** gegen die Tabelle in 4.4 prüfen: 5 · 10 · 10 · 26 (gedeckelt) · 1 · 0. Bei
   der Deckelung muss die Meldung im Hinweisfeld erscheinen.
4. **Meldungen**: Randfeld bei `d_mm > L_cm` (Test: d = 25 mm, L = 20 cm) · Durchschlag nur im
   Modus `isoliert` erreichbar (Test: Glas, L = 10 cm, d = 5 mm einfrieren, dann Luft und
   L = 10 cm) · Moduswechsel bei Bewegung von `rU` im Modus `isoliert`.
5. **Maßstabsbeschriftung** im Kondensator-Canvas vorhanden: waagerechter Balken „10 mm",
   senkrechter Balken „5 cm", Satz *„Plattenabstand fünffach überhöht dargestellt"*. Ohne ihn ist
   die Abbildung irreführend und die Abnahme scheitert.
6. **Alle Zahleneingaben in allen vier Fällen** testen (richtig · richtige Zahl mit falscher
   Einheit · nah daneben · weit daneben) und zusätzlich die Alternativeinheit:
   `265,6 pF` ↔ `0,2656 nF` · `6,375 nC` ↔ `6375 pC` · `2,01 m²` ↔ `20079 cm²` ·
   `4,0 µJ` ↔ `4000 nJ`.
7. **Feedbackzahl gegen Optionszahl**: `sim1` und `ue3` haben **vier** Optionen und brauchen
   deshalb **vier** `fb`-Einträge; `vw1`–`vw3` und `sim2` haben drei. `data-i` lückenlos von 0 an,
   `name` jedes Radios gleich dem Wert von `data-mc`.
8. **Zuordnung in beiden Richtungen** testen: vollständig richtig (B · D · C · A) und teilweise
   falsch. Die Reihenfolge der Situationen darf nicht der Diagrammreihenfolge entsprechen — sie tut
   es hier auch nicht.
9. **Jede Hilfestufe** aller sechs Aufgaben `ue1`–`ue6` öffnet und schließt; jede Musterlösung von
   `ue7`–`ue9` schaltet um und der Knopftext wechselt.
10. **Offline-Fallback**: Jede Formel hat ein gefülltes `data-plain` mit Unicode
    (`ε₀`, `ε_r`, `E⃗`, `σ`, `·`, `−`, `⁻¹²`, `∼`, `⟹`, `½`). Stichprobe ohne Netz.
11. **Tabellenkapselung**: Jede `<table>` steht in `<div class="tabelle">`. Dieses Modul hat
    besonders viele — unter anderem in 0.1, 0.2, 0.3, 3.7, 4.8 und im Lehrerteil.
12. **Kein waagerechtes Scrollen** bei 1280, 900 und 390 px; Druckansicht enthält die Aufgaben,
    aber keine Bedienelemente und keinen Lehrerteil.
13. Modulcheck laufen lassen:
    `PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/physik-q1-elektrisches-feld.html"`
    — `blocker` und `maengel` müssen leer sein.
14. Eintrag in `fachliches/modulliste.md` erst danach auf `fertig` setzen.

### Quelle der Kontrollrechnungen

Alle Zahlenwerte dieses Dokuments wurden mit Python nachgerechnet, durchgehend mit den Konstanten
aus 0.1 (<span class="m">ε₀ = 8,854·10⁻¹² F/m</span>,
<span class="m">e = 1,602·10⁻¹⁹ C</span>). Geprüft wurden:

- die vier Zahleneingaben `ue1`, `ue2`, `ue5`, `ue6` samt Alternativeinheiten und samt der in den
  `weit`-Texten genannten Falschergebnisse (Faktor 576 = 24² bei `ue2`, Faktor 20,25 = 4,5² bei
  `ue5`, −1,3 µJ statt +4,0 µJ bei `ue6`);
- `ue6` zusätzlich über einen **zweiten, unabhängigen Weg**: Energiedifferenz
  <span class="m">W₂ − W₁ = 4,0 µJ</span> gegen Kraftrechnung
  <span class="m">F·Δd = 564,7 µN · 7,0832·10⁻³ m = 4,0 µJ</span> — beide Wege stimmen überein;
- die Startwerte und beide Durchgänge des Beobachtungsauftrags (4.8) sowie die Energiedichte-Probe
  aus 3.6: <span class="m">w·V = 4,427·10⁻⁴ J/m³ · 8,0·10⁻⁴ m³ = 3,5416·10⁻⁷ J</span>, identisch
  mit <span class="m">W = ½·C·U²</span>;
- sämtliche Zahlen in `sim1`, `sim2`, `ue7` und `ue8` (Faktor 4 bei Spannungsverdopplung,
  Faktor 6 bzw. 1/6 beim Glaseinschub, die Bilanz
  <span class="m">ΔQ·U = 3,5416 µJ = 2 · 1,7708 µJ</span>);
- die Kontrollzahlen in den neuen Hilfen zu `ue4` (Q gegen A, E gegen d, W gegen U, Q gegen d);
- die Feldlinienzahl <span class="m">n = clamp(round(E·L/400 V), 1, 26)</span> für alle sechs
  Zeilen der Tabelle in 4.4;
- die Zusatzaufgabe im Lehrerteil (Glasplatte der Dicke <span class="m">d/2</span> als
  Reihenschaltung): <span class="m">C = 30,36 pF</span> gegen <span class="m">106,25 pF</span> bei
  voller Füllung.

Abweichungen zwischen den im Text genannten gerundeten Werten und der Rechnung liegen ausnahmslos
in der letzten angegebenen Stelle (größte gefundene Abweichung: 265,62 pF gegen den im
`numDaten`-Eintrag gesetzten Sollwert 265,6 pF, also 0,008 % — weit innerhalb der Toleranz
`tol: 2`).

---

<!-- FORTSCHRITT: Inhaltsdatei vollstaendig: Abschnitte 0-6, Lehrerteil, Checkliste. Alle Zahlenwerte mit Python nachgerechnet. Naechster Schritt liegt beim Bauagenten: module/physik-q1-elektrisches-feld.html als Kopie von module/physik-q1-induktion.html. -->
