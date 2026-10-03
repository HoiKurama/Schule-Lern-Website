# Modulinhalt: Magnetisches Feld und Lorentzkraft

Modul: `physik-q1-magnetisches-feld`
Fach: Physik, Leistungskurs Q1
Inhaltsfeld (Chip im Seitenkopf): **Ladungen, Felder und Induktion**
Akzentfarben: `--akzent: #1d4ed8`, `--akzent-hell: #eff6ff`, `--akzent-rand: #bfdbfe`
Titel der Seite: *Magnetisches Feld und Lorentzkraft*
Untertitel im Kopf: *Von der Kraft auf den Leiter zur Kreisbahn des einzelnen Teilchens*

Abgrenzung: Dieses Modul liegt **vor** `module/physik-q1-induktion.html`. Magnetischer Fluss und
Induktionsgesetz werden nur im Ausblick des Abschlusses genannt, nicht behandelt.

---

## 0 · Vorzeichen- und Richtungskonvention (gilt im ganzen Modul)

**Diese Festlegungen gelten für jede Abbildung, jede Simulation, jede Aufgabe und jede
Musterlösung des Moduls. Der Bauagent weicht davon nicht ab.**

### 0.1 Bildebene und Koordinaten

Alle Darstellungen zeigen die Bildebene als *x-y-Ebene*:

| Achse | Richtung im Bild | Positive Richtung |
|---|---|---|
| x | waagerecht | nach **rechts** |
| y | senkrecht | nach **oben** |
| z | senkrecht zur Bildebene | aus der Bildebene **heraus** zum Betrachter |

Damit ist das Koordinatensystem rechtshändig: x × y = z.

**Achtung Canvas.** Die Canvas-Koordinate wächst nach unten. Der Bauagent rechnet physikalisch
in y-nach-oben und rechnet erst beim Zeichnen um: `y_canvas = y_0 − k · y_physik`. In keiner
Formel des Moduls taucht ein Vorzeichen auf, das nur aus dieser Umrechnung stammt.

### 0.2 Symbole für das Magnetfeld

Das Magnetfeld steht in diesem Modul **immer senkrecht zur Bildebene**, nie schräg. Es gibt
genau zwei Fälle, und sie bekommen die üblichen Symbole:

| Symbol | Bedeutung | Merkbild | Verwendung |
|---|---|---|---|
| **⊗** | B zeigt **in die Bildebene hinein** (−z) | das Federende eines wegfliegenden Pfeils | **Standardfall** in allen Abbildungen dieses Moduls |
| **⊙** | B zeigt **aus der Bildebene heraus** (+z) | die Spitze eines herankommenden Pfeils | nur, wenn die Aufgabe die Umkehrung ausdrücklich verlangt |

Der Standardfall ist ⊗. Wo im Text nichts anderes steht, gilt: **B in die Bildebene hinein**,
also <span class="m">B⃗ = (0; 0; −B)</span> mit B > 0.

Formeln dafür:
- `data-tex`: `\vec{B} = (0;\,0;\,-B),\ B>0 \quad (\otimes)`
- `data-plain`: `B = (0; 0; −B), B > 0   (⊗, in die Bildebene hinein)`

### 0.3 Bewegungsrichtung

Das Teilchen tritt im **Standardfall von links ein und fliegt nach rechts**, also
<span class="m">v⃗ = (v; 0; 0)</span> mit v > 0. Der Eintrittspunkt liegt am linken Bildrand
auf halber Höhe.

- `data-tex`: `\vec{v} = (v;\,0;\,0),\ v>0`
- `data-plain`: `v = (v; 0; 0), v > 0  (nach rechts)`

### 0.4 Vorzeichen der Ladung

**q ist eine vorzeichenbehaftete Größe.** Das ist die Stelle, an der im LK am meisten
verlorengeht, deshalb wird sie hier hart festgelegt:

| Größe | Bedeutung | Vorzeichen |
|---|---|---|
| q | Ladung des Teilchens, **mit Vorzeichen** | positiv oder negativ |
| e | Elementarladung, **immer positiv**: e = 1,602 · 10⁻¹⁹ C | > 0 |
| Elektron | q = −e | negativ |
| Positron, Proton | q = +e | positiv |
| Alphateilchen, einfach geladenes Ion | q = +2e bzw. q = +e | positiv |

**Schreibregel.** In Betragsformeln — also überall dort, wo nur der Betrag der Kraft, des
Radius oder der Umlaufdauer gefragt ist — steht **|q|**, nicht q. Also
<span class="m">F = |q| · v · B</span> und <span class="m">r = m·v/(|q|·B)</span>. Wer dort q
schreibt, bekommt für Elektronen einen negativen Radius, und das ist keine Physik, sondern
ein Vorzeichenfehler.

- `data-tex`: `F = |q| \cdot v \cdot B \qquad r = \dfrac{m \cdot v}{|q| \cdot B}`
- `data-plain`: `F = |q| · v · B     r = m · v / (|q| · B)`

Das **Vorzeichen von q entscheidet ausschließlich über die Richtung** der Kraft, nie über
ihren Betrag. Das wird in Abschnitt 2 gesondert behandelt.

### 0.5 Welche Hand für welchen Fall

Im Modul wird **ausschließlich die rechte Hand** benutzt. Die Linke-Hand-Regel kommt nicht
vor — sie führt erfahrungsgemäß dazu, dass Schülerinnen und Schüler im Abitur raten, welche
Hand gemeint war. Statt zwei Regeln gibt es eine Regel und eine Vorzeichenprüfung.

**Die Regel (rechte Hand, Drei-Finger-Regel):**

| Finger der **rechten** Hand | Zeigt in Richtung von |
|---|---|
| **Daumen** | der **technischen Stromrichtung** I, das heißt der Bewegungsrichtung **positiver** Ladung |
| **Zeigefinger** | dem **Magnetfeld** B⃗ |
| **Mittelfinger** | der resultierenden **Kraft** F⃗ |

Die drei Finger stehen dabei paarweise senkrecht aufeinander (UVW-Regel: **U**rsache Strom,
**V**ermittlung Feld, **W**irkung Kraft).

**Die Vorzeichenprüfung — der eigentliche Kern:**

> Der Daumen zeigt in die Bewegungsrichtung **positiver** Ladung.
> Bei einem **negativ** geladenen Teilchen zeigt der Daumen deshalb **entgegen** dessen
> Flugrichtung — oder du drehst am Ende die gefundene Kraftrichtung **um 180°**.
> Beides ergibt dasselbe. Entscheide dich für eine Variante und bleib dabei.

**Verbindliche Standardsituation des Moduls** (wird in Text, Abbildungen und Simulation
immer wieder als Referenz benutzt):

| Größe | Festlegung | Ergebnis |
|---|---|---|
| B⃗ | ⊗, in die Bildebene hinein | — |
| v⃗ | nach rechts | — |
| **positive** Ladung (q = +e) | Daumen nach rechts, Zeigefinger ins Bild | **F⃗ zeigt nach oben**, Kreisbahn **gegen** den Uhrzeigersinn |
| **negative** Ladung (q = −e) | Daumen nach links (entgegen v⃗) | **F⃗ zeigt nach unten**, Kreisbahn **im** Uhrzeigersinn |

Diese Tabelle ist der Prüfstein: Jede Abbildung und jeder Simulationslauf muss sie
reproduzieren. Ein Elektron, das von links kommt bei ⊗-Feld, wird **nach unten** abgelenkt.

*Kontrolle über das Kreuzprodukt (für die Herleitung im Details-Block, nicht für die Tafel):*
mit <span class="m">F⃗ = q · (v⃗ × B⃗)</span>, v⃗ = (v; 0; 0), B⃗ = (0; 0; −B) folgt
v⃗ × B⃗ = (0 · (−B) − 0 · 0; 0 · 0 − v · (−B); 0) = (0; +v·B; 0), also **in +y-Richtung**.
Für q = +e ist F⃗ nach oben, für q = −e nach unten. Das bestätigt die Tabelle.

- `data-tex`: `\vec{F} = q \cdot (\vec{v} \times \vec{B})`
- `data-plain`: `F = q · (v × B)`

### 0.6 Umlaufsinn und Farbcode

| Ladung | Umlaufsinn im ⊗-Feld | Farbe in Abbildungen und Simulation |
|---|---|---|
| negativ (Elektron) | im Uhrzeigersinn | Blau `#1d4ed8` (Akzentfarbe) |
| positiv (Proton, Positron, Alpha, Ion) | gegen den Uhrzeigersinn | Rot `#b91c1c` |

Der Feldvektor B wird in allen SVG- und Canvas-Grafiken grau `#64748b` gezeichnet,
der Kraftvektor F grün `#0d7a52`, der Geschwindigkeitsvektor v schwarz `#0f172a`.

### 0.7 Einheiten und Schreibweise

- Flussdichte B in **Tesla (T)**, in Aufgaben meist in **Millitesla (mT)**: 1 mT = 10⁻³ T.
- Geschwindigkeiten werden in **m/s** gerechnet, in Ergebnissen zusätzlich in **km/s** genannt,
  wenn der Zahlenwert sonst unlesbar wird.
- Alle angezeigten Zahlen mit **Komma** als Dezimaltrennzeichen.
- Zehnerpotenzen in `data-plain` als Unicode-Hochzahlen: 10⁻¹⁹, 10⁷, 10¹¹.

## 1 · Einstieg

### 1.1 Aufhänger (zwei Absätze, gehen so in `<section id="einstieg">`)

**Absatz 1:**

> Röhrenfernseher haben früher geflimmert, wenn man einen Lautsprecher zu nah danebenstellte, und
> in der Farbe gekippt, wenn man mit einem Magneten davorging. Der Grund liegt hinter dem Glas:
> Dort flogen Elektronen quer durch eine leergepumpte Röhre auf den Bildschirm zu, und ein
> Magnetfeld hat sie von ihrer Bahn geschoben. Genau dieselbe Ablenkung nutzt heute jedes
> Massenspektrometer im Labor, jede Dopingprobe und jeder Teilchenbeschleuniger — nur eben
> absichtlich und mit gerechneten Feldstärken.
>
> Bemerkenswert daran ist, dass sich dabei die **Schnelligkeit** der Elektronen überhaupt nicht
> ändert. Nur ihre Richtung. Das Magnetfeld schiebt sie ständig zur Seite, macht sie aber weder
> schneller noch langsamer.

**Absatz 2:**

> In dieser Einheit klärst du, warum das so ist und was daraus folgt. Die Antwort steckt in einer
> einzigen geometrischen Eigenschaft der Kraft, und aus ihr ergibt sich zwingend die Bahnform:
> ein Kreis. Aus dem Radius dieses Kreises kannst du anschließend etwas herauslesen, was du sonst
> nicht messen kannst — das Verhältnis von Ladung zu Masse eines Teilchens, das viel zu klein zum
> Wiegen ist.
>
> Am Ende wirst du erklären können, warum ein Zyklotron mit einer festen Frequenz arbeitet,
> obwohl die Teilchen darin immer schneller werden, und warum ein Geschwindigkeitsfilter genau
> eine Geschwindigkeit durchlässt und alle anderen aussortiert — unabhängig davon, welches
> Teilchen hindurchfliegt.

*Ton-Hinweis für den Bauagenten: kein Absatz beginnt mit „In der Physik…" oder „Man betrachte…".
Die beiden Absätze stehen als reine `<p>` vor der Karte mit den Vorwissensfragen, so wie im
Referenzmodul.*

### 1.2 Vorwissensfragen

Drei Fragen, je drei Optionen, in einer `<div class="karte">` mit der Überschrift
*Vorwissen prüfen*. Einleitungssatz darunter in Grau:
*„Drei Fragen aus der EF und der Mittelstufe. Wenn du hier hängst, lohnt sich ein Blick zurück,
bevor du weitermachst."*

---

#### vw1 — Magnetfeld und Feldlinien (Sek I)

**Frage:** Wie verlaufen die magnetischen Feldlinien eines Stabmagneten außerhalb des Magneten,
und was bedeutet ihre Dichte?

| `data-i` | Option |
|---|---|
| 0 | Vom Nordpol zum Südpol; je dichter die Linien liegen, desto stärker ist das Feld. |
| 1 | Vom Südpol zum Nordpol; je dichter die Linien liegen, desto stärker ist das Feld. |
| 2 | Vom Nordpol zum Südpol; die Dichte der Linien sagt nichts über die Feldstärke aus, sie ist nur eine Zeichenkonvention. |

**`mcDaten`-Eintrag:**

```js
vw1:{ r:0, fb:[
  "Richtig. Außerhalb des Magneten laufen die Feldlinien vom Nord- zum Südpol, im Inneren schließen sie sich zurück zum Nordpol — Feldlinien sind immer geschlossen. Und die Liniendichte ist keine Willkür: Sie ist das Bild für den Betrag der Flussdichte B. Genau daran erkennst du im nächsten Abschnitt, wo ein Feld stark ist.",
  "Die Richtung ist vertauscht. Merkhilfe: Die Feldlinie zeigt dort hin, wohin der Nordpol einer kleinen Probenadel zeigt — und der wird vom Südpol des großen Magneten angezogen. Außerhalb laufen die Linien deshalb vom Nord- zum Südpol. Innen im Magneten laufen sie umgekehrt, sonst wären sie nicht geschlossen.",
  "Die Richtung stimmt, aber die Dichte ist keine Zeichenkonvention. Wo die Linien eng zusammenrücken, ist das Feld stark; wo sie auseinanderlaufen, schwach. Deshalb ist das Feld zwischen zwei Polschuhen eines Hufeisenmagneten nahezu homogen — die Linien laufen dort parallel und in gleichem Abstand."
]}
```

---

#### vw2 — Kraft auf einen stromdurchflossenen Leiter (Sek I / EF)

**Frage:** Ein gerader Leiter hängt waagerecht zwischen den Polschuhen eines Hufeisenmagneten.
Wovon hängt der **Betrag** der Kraft auf diesen Leiter ab?

| `data-i` | Option |
|---|---|
| 0 | Nur von der Stromstärke I und der Flussdichte B — die Länge des Leiters im Feld spielt keine Rolle, weil das Feld überall gleich stark ist. |
| 1 | Von der Stromstärke I, der Flussdichte B und der Länge l des Leiterstücks, das sich im Feld befindet. |
| 2 | Von der Stromstärke I, der Flussdichte B und der **gesamten** Leiterlänge, auch außerhalb des Magneten. |

**`mcDaten`-Eintrag:**

```js
vw2:{ r:1, fb:[
  "Die Leiterlänge fällt nicht heraus. Denk an das Bild dahinter: Die Kraft greift an den bewegten Ladungen an, und je länger das Leiterstück im Feld ist, desto mehr bewegte Ladungen stecken darin. Ein doppelt so langes Stück im selben Feld erfährt die doppelte Kraft. Genau deshalb steht l in der Formel.",
  "Richtig. Es gilt F = B · I · l, und l ist ausdrücklich die *wirksame* Länge — der Teil des Leiters, der im Feld liegt. Diese Beziehung ist im nächsten Abschnitt die Definitionsgleichung für B.",
  "Fast. Die Formel F = B · I · l stimmt, aber l ist nur der Teil des Leiters, der tatsächlich im Feld steckt. Außerhalb der Polschuhe ist B ≈ 0, dort wirkt keine Kraft. Ein zehn Meter langes Kabel, von dem 12 cm zwischen den Polen liegen, erfährt dieselbe Kraft wie ein 12 cm kurzes Stück."
]}
```

---

#### vw3 — Elektrisches Feld im Plattenkondensator (EF)

**Frage:** An einem Plattenkondensator mit dem Plattenabstand d liegt die Spannung U. Welche
Aussage über das Feld zwischen den Platten trifft zu?

| `data-i` | Option |
|---|---|
| 0 | Das Feld ist nahezu homogen; für seinen Betrag gilt E = U / d, und die Kraft auf eine Ladung q ist F = q · E — unabhängig davon, wo zwischen den Platten sie sitzt. |
| 1 | Das Feld ist nahezu homogen; es gilt E = U · d, und die Kraft F = q · E ist an der positiven Platte am größten. |
| 2 | Das Feld nimmt von der positiven zur negativen Platte gleichmäßig ab; für die Kraft muss man deshalb den Mittelwert von E einsetzen. |

**`mcDaten`-Eintrag:**

```js
vw3:{ r:0, fb:[
  "Richtig. E = U/d, das Feld ist im Innenraum überall gleich groß und gleich gerichtet, und die Kraft F = q · E hängt nicht vom Ort ab. Genau diese Kraft stellst du im Vertiefungsteil der magnetischen Kraft gegenüber — daraus wird der Geschwindigkeitsfilter.",
  "Der Zusammenhang ist umgedreht. Prüfe es über die Einheiten: [E] = V/m, und aus U · d würden V·m. Richtig ist E = U/d — bei gleicher Spannung wird das Feld stärker, wenn du die Platten näher zusammenschiebst. Die Kraft ist außerdem im ganzen Innenraum gleich groß, nicht an einer Platte größer.",
  "Das ist die Vorstellung vom Feld einer Punktladung, die mit dem Abstand abnimmt. Beim Plattenkondensator ist es anders: Die beiden Platten überlagern sich zu einem homogenen Feld — überall gleicher Betrag, überall gleiche Richtung. Nur an den Rändern beult es aus, und das wird in der Schulphysik vernachlässigt. Ein Mittelwert ist deshalb nicht nötig."
]}
```

---

**Hinweis zur Schlüsselvergabe:** `data-mc` und das `name`-Attribut der Radios sind identisch
(`vw1`, `vw2`, `vw3`). Die Karte bekommt dieselbe Struktur wie im Referenzmodul, die drei
Aufgaben-Divs tragen `style="border:none;padding:0"`.

## 2 · Erklärteil

Überschrift der Section: **Von der Kraft auf den Leiter zur Kraft auf ein Teilchen**
(`<section id="grundlagen">`, `.stufe`-Nummer 2)

### 2.1 Die magnetische Flussdichte B

**Fließtext:**

> Ein Magnetfeld kann man nicht sehen und nicht direkt messen. Was man messen kann, ist seine
> **Wirkung** — und die einfachste messbare Wirkung ist die Kraft auf einen stromdurchflossenen
> Leiter. Hängt ein gerades Leiterstück der Länge l senkrecht zum Feld zwischen den Polschuhen
> und fließt der Strom I hindurch, so misst eine Waage die Kraft
>
> **Formel (Block):**
> - `data-tex`: `F = B \cdot I \cdot l`
> - `data-plain`: `F = B · I · l`
>
> Diese Beziehung dreht man um und macht sie zur **Definition** der magnetischen Flussdichte:
>
> **Formel (Block):**
> - `data-tex`: `B = \dfrac{F}{I \cdot l} \qquad [B] = 1\,\dfrac{\mathrm{N}}{\mathrm{A\cdot m}} = 1\,\mathrm{T}\ \text{(Tesla)}`
> - `data-plain`: `B = F / (I · l)     [B] = 1 N/(A·m) = 1 T (Tesla)`
>
> B ist also nicht „die Stärke des Magneten", sondern die Kraft pro Stromstärke und pro
> wirksamer Länge. Das l in der Formel ist ausdrücklich nur der Teil des Leiters, der im Feld
> liegt; außerhalb der Polschuhe ist B praktisch null und es wirkt keine Kraft.

**Größenordnungen (als kleine Tabelle im `.tabelle`-Wrapper):**

| Feld | B |
|---|---|
| Erdmagnetfeld in Deutschland | ≈ 4,8 · 10⁻⁵ T = 0,048 mT |
| Hufeisen-Schulmagnet zwischen den Polschuhen | 0,1 T bis 0,5 T |
| Helmholtz-Spulenpaar im Fadenstrahlrohr | 0,5 mT bis 4 mT |
| Kernspintomograph in der Klinik | 1,5 T bis 3 T |

*Diese Tabelle ist nicht Schmuck: Sie liefert das Augenmaß, mit dem später Ergebnisse auf
Plausibilität geprüft werden. Ein ausgerechnetes B von 400 T ist ein Rechenfehler, kein Befund.*

**Zahlenbeispiel im Fließtext** (Kontrollrechnung siehe Abschnitt 9, K-1):

> Ein 12 cm langes Leiterstück liegt senkrecht in einem Feld von B = 0,25 T, es fließen
> I = 3,5 A. Dann ist F = 0,25 T · 3,5 A · 0,120 m = 0,105 N = 105 mN — etwa das Gewicht einer
> Tafel Schokolade. Magnetische Kräfte im Schulversuch sind klein, aber gut messbar.

**Nebenbedingung, die sofort genannt wird:**

> F = B · I · l gilt nur, wenn Leiter und Feld **senkrecht** aufeinander stehen. Läuft der
> Leiter unter dem Winkel α zum Feld, zählt nur die Komponente senkrecht dazu:
> - `data-tex`: `F = B \cdot I \cdot l \cdot \sin\alpha`
> - `data-plain`: `F = B · I · l · sin α`
>
> Liegt der Leiter **parallel** zum Feld (α = 0°), wirkt gar keine Kraft. In allen Aufgaben
> dieses Moduls ist α = 90°, wenn nichts anderes dasteht.

### 2.2 Übergang zur einzelnen Ladung: die Lorentzkraft

**Fließtext vor dem Details-Block:**

> Ein Strom ist nichts anderes als bewegte Ladung. Wenn also eine Kraft auf den Leiter wirkt,
> muss sie eigentlich an den bewegten Ladungen *im* Leiter angreifen — der Draht bekommt sie nur
> weitergereicht. Das legt die Frage nahe, wie groß die Kraft auf **ein einzelnes** Teilchen ist,
> das ganz ohne Draht durch das Feld fliegt. Genau das passiert im Fadenstrahlrohr und in der
> Bildröhre.

**Details-Block** (`<details>`), Summary:
*„Herleitung: von F = B · I · l zur Lorentzkraft F = |q| · v · B"*

Inhalt des Details-Blocks, in vier Schritten:

> **Schritt 1 — Was ist Stromstärke?** Die Stromstärke ist die pro Zeit durch den Querschnitt
> transportierte Ladung:
> - `data-tex`: `I = \dfrac{q}{t}`
> - `data-plain`: `I = q / t`
>
> **Schritt 2 — Wie lange braucht die Ladung durch das Feld?** Betrachte das Leiterstück der
> Länge l im Feld. Ein Ladungsträger mit der Geschwindigkeit v braucht für diese Strecke die
> Zeit
> - `data-tex`: `t = \dfrac{l}{v}`
> - `data-plain`: `t = l / v`
>
> **Schritt 3 — Einsetzen.** Ist q die gesamte Ladung, die sich gerade im Feldbereich befindet,
> so gilt
> - `data-tex`: `I = \dfrac{q}{t} = \dfrac{q \cdot v}{l}`
> - `data-plain`: `I = q / t = (q · v) / l`
>
> Das setzt du in F = B · I · l ein:
> - `data-tex`: `F = B \cdot I \cdot l = B \cdot \dfrac{q \cdot v}{l} \cdot l = q \cdot v \cdot B`
> - `data-plain`: `F = B · I · l = B · (q · v / l) · l = q · v · B`
>
> Das l kürzt sich vollständig heraus. Das ist der entscheidende Punkt: Die Kraft auf das
> einzelne Teilchen hängt **nicht** davon ab, wie lang der Feldbereich ist, den es durchquert.
>
> **Schritt 4 — Auf ein Teilchen herunterbrechen.** Steckt die Ladung q in N Teilchen mit je der
> Ladung q₁, so verteilt sich die Kraft gleichmäßig auf sie, und auf jedes einzelne wirkt
> F₁ = q₁ · v · B. Der Index fällt weg, weil die Form für jedes Teilchen dieselbe ist.
>
> **Warum diese Herleitung trägt:** Sie verbindet eine Größe, die man im Schulversuch mit einer
> Waage messen kann (die Kraft auf den Leiter), mit einer Größe, die man nur an der Bahnform
> ablesen kann (die Kraft auf ein einzelnes Elektron). Beide Beschreibungen meinen dieselbe
> Physik — das ist dasselbe Argument, das dir bei der Bewegungsinduktion wieder begegnet.

**Ergebnis, als Blockformel im Haupttext:**

> - `data-tex`: `F_L = |q| \cdot v \cdot B \qquad \text{(für } \vec{v} \perp \vec{B}\text{)}`
> - `data-plain`: `F_L = |q| · v · B     (für v senkrecht zu B)`
>
> Für den allgemeinen Fall, in dem v und B den Winkel α einschließen:
> - `data-tex`: `F_L = |q| \cdot v \cdot B \cdot \sin\alpha`
> - `data-plain`: `F_L = |q| · v · B · sin α`
>
> Ein Teilchen, das **längs** der Feldlinien fliegt (α = 0°), erfährt überhaupt keine Kraft und
> fliegt geradeaus weiter. In diesem Modul ist stets α = 90°.

**Der Betragsstrich ist Absicht** (eigener Absatz, nicht in Klammern versteckt):

> Beachte die Betragsstriche um q. Der Betrag der Kraft hängt nur davon ab, **wie viel** Ladung
> unterwegs ist, nicht davon, ob sie positiv oder negativ ist. Ein Elektron und ein Positron mit
> gleicher Geschwindigkeit erfahren im selben Feld **denselben Kraftbetrag** — nur in
> entgegengesetzter Richtung. Wenn du q mit Vorzeichen in eine Betragsformel einsetzt, kommen
> negative Kräfte, negative Radien und negative Umlaufdauern heraus. Das Vorzeichen von q wird
> nicht gerechnet, es wird **gedacht**: Es legt die Richtung fest.

### 2.3 Die Richtung: Drei-Finger-Regel der rechten Hand

Hier wird Abschnitt 0.5 im Schülertext ausformuliert. Der Bauagent übernimmt die Tabelle aus
0.5 wörtlich und stellt diesen Text davor:

> Die Kraft steht **senkrecht auf v⃗ und gleichzeitig senkrecht auf B⃗**. Damit sind nur noch
> zwei Richtungen möglich — vor oder zurück auf dieser gemeinsamen Senkrechten — und welche es
> ist, klärt die Drei-Finger-Regel der rechten Hand.
>
> | Finger (rechte Hand) | Richtung |
> |---|---|
> | Daumen | technische Stromrichtung, also Bewegungsrichtung **positiver** Ladung |
> | Zeigefinger | Magnetfeld B⃗ |
> | Mittelfinger | Kraft F⃗ |
>
> **Und jetzt die Stelle, an der die meisten Punkte verlorengehen.** Der Daumen zeigt in die
> Bewegungsrichtung *positiver* Ladung. Ein Elektron ist negativ geladen. Sein
> Geschwindigkeitsvektor zeigt also **entgegen** der technischen Stromrichtung. Du hast zwei
> Möglichkeiten, damit umzugehen:
>
> 1. Du legst den Daumen **entgegen** der Flugrichtung des Elektrons an. Der Mittelfinger zeigt
>    dann direkt die richtige Kraftrichtung.
> 2. Du legst den Daumen in Flugrichtung an und **drehst das Ergebnis am Ende um 180°**.
>
> Beides führt zum selben Ergebnis. Such dir eines aus und mach es immer gleich — das
> Hin-und-Her zwischen beiden Varianten ist der eigentliche Fehlerherd.

**Merksatz 1** (`.merksatz`, mit `<b>Kernaussage</b>`):

> **Kernaussage**
> Der **Betrag** der Lorentzkraft interessiert sich nicht für das Vorzeichen der Ladung, die
> **Richtung** interessiert sich für nichts anderes. Deshalb steht in der Formel |q|, und deshalb
> gehört das Vorzeichen in die Handregel und nicht in den Taschenrechner.

**Standardsituation als Abbildung** (Inline-SVG, Beschreibung für den Bauagenten):

Ein Rechteck als Feldbereich, gefüllt mit einem Raster aus ⊗-Symbolen (grau `#64748b`,
5 × 3 Symbole reichen). Von links tritt auf halber Höhe ein Teilchen ein, v⃗ als schwarzer
Pfeil nach rechts. Zwei Fälle nebeneinander:
- links: rote Kugel „+q", F⃗ grüner Pfeil **nach oben**, gestrichelter Bahnbogen nach oben
- rechts: blaue Kugel „−q", F⃗ grüner Pfeil **nach unten**, gestrichelter Bahnbogen nach unten

Beschriftung unter der Grafik: *„B in die Bildebene hinein (⊗), v nach rechts. Gleicher Betrag
der Kraft, entgegengesetzte Richtung."*

### 2.4 Die Fehlvorstellung: „Das Magnetfeld beschleunigt die Teilchen"

Dieser Abschnitt bekommt eine eigene Zwischenüberschrift `<h3>` und steht **vor** der
Kreisbahn — die Kreisbahn ist seine Folgerung, nicht sein Nachbar.

**Fließtext:**

> Wenn eine Kraft wirkt, wird ein Körper schneller — das ist die Grundintuition aus der
> Mechanik, und sie ist hier **falsch**. Genauer: Sie ist unvollständig. Schneller wird ein
> Körper nur, wenn die Kraft eine Komponente **in Bewegungsrichtung** hat. Und genau die hat die
> Lorentzkraft nie.
>
> Denn F⃗ steht per Konstruktion senkrecht auf v⃗. Und für die Arbeit gilt
> - `data-tex`: `W = \vec{F} \cdot \vec{s} = F \cdot s \cdot \cos\varphi`
> - `data-plain`: `W = F · s · cos φ`
>
> Der Winkel φ zwischen Kraft und Weg ist hier immer 90°, und cos 90° = 0. Also
> - `data-tex`: `W_{\text{magn}} = 0 \quad \text{für jedes Wegstück, immer.}`
> - `data-plain`: `W_magn = 0   für jedes Wegstück, immer.`
>
> Kein Zwischenschritt, keine Näherung, kein „fast null". Die magnetische Kraft verrichtet an
> einer frei fliegenden Ladung **exakt keine Arbeit**.

**Was daraus folgt — als Kette, damit der Zwang sichtbar wird:**

> 1. W = 0 ⟹ die kinetische Energie ½ m v² bleibt konstant.
> 2. E_kin konstant ⟹ der **Betrag** v der Geschwindigkeit bleibt konstant.
> 3. v konstant, aber F⃗ ≠ 0 ⟹ es ändert sich ausschließlich die **Richtung** von v⃗.
> 4. Die Kraft steht dauernd senkrecht auf v⃗ und hat den konstanten Betrag |q| · v · B ⟹ das
>    ist genau die Definition einer **gleichförmigen Kreisbewegung**.
>
> Die Kreisbahn ist also kein Zufall und kein Versuchsergebnis, das man hinnehmen muss. Sie ist
> die einzige Bahn, die mit einer konstant großen, dauernd senkrechten Kraft verträglich ist.

**Gegenprobe, die die Fehlvorstellung endgültig erledigt:**

> Prüfe es an einem Fall, bei dem man es sieht: Im Fadenstrahlrohr bleibt der Kreis, den die
> Elektronen zeichnen, über Minuten gleich groß. Würde das Feld die Elektronen beschleunigen,
> müsste der Radius r = m·v/(|q|·B) mit wachsendem v ständig größer werden — die Bahn wäre eine
> nach außen laufende Spirale. Genau das sieht man nicht.
>
> Schneller werden die Elektronen einzig in der Beschleunigungsstrecke davor, und die arbeitet
> mit einem **elektrischen** Feld. Merke dir die Arbeitsteilung: Das elektrische Feld macht
> schnell, das magnetische Feld lenkt ab.

**Merksatz 2** (`.merksatz`, mit `<b>Kernaussage</b>`):

> **Kernaussage**
> Ein Magnetfeld kann an einer frei bewegten Ladung keine Arbeit verrichten, weil seine Kraft
> immer senkrecht auf der Bewegung steht. Es ändert die Richtung, nie den Betrag der
> Geschwindigkeit — und deshalb bleibt der Radius der Bahn konstant, statt aufzuspiralen.

**Merksatz 3, als Abgrenzung E-Feld / B-Feld** (kleine Tabelle, `.tabelle`-Wrapper):

| | elektrisches Feld | magnetisches Feld |
|---|---|---|
| Kraft | F = q · E | F = |q| · v · B |
| wirkt auf | jede Ladung, auch ruhende | nur **bewegte** Ladung |
| Richtung der Kraft | **parallel** zu E⃗ (bei q > 0) | **senkrecht** zu v⃗ und zu B⃗ |
| verrichtet Arbeit? | ja | **nein, nie** |
| ändert | Betrag und Richtung von v⃗ | nur die Richtung von v⃗ |

*Hinweis an den Bauagenten: In der HTML-Tabelle wird `|q|` als `<span class="m"
data-tex="|q|" data-plain="|q|">` gesetzt, nicht als roher Text — sonst kollidieren die
Striche mit der Markdown-Tabellensyntax der Vorlage.*

**Ausblick-Satz am Ende von Abschnitt 2** (eine Zeile, keine Vorwegnahme):

> Dass eine Ladung, die sich durch ein Magnetfeld bewegt, im Leiter eine Spannung aufbaut, ist
> die Brücke zur Induktion — die baust du im Modul *Elektromagnetische Induktion*. Hier bleibt
> es bei der freien Ladung ohne Draht.

## 3 · Vertiefung

Überschrift der Section: **Die Kreisbahn — und was man aus ihr herausliest**
(`<section id="vertiefung">`, `.stufe`-Nummer 3)

### 3.1 Der Bahnradius

**Fließtext:**

> In Abschnitt 2 hast du erschlossen, *dass* die Bahn ein Kreis sein muss. Jetzt rechnest du
> aus, *wie groß* er ist. Der Ansatz ist eine Kraftaussage, kein neues Gesetz: Die Lorentzkraft
> ist die Kraft, die das Teilchen auf der Kreisbahn hält. Sie **ist** also die Radialkraft — es
> gibt keine zweite Kraft daneben, und die Lorentzkraft ist auch keine Zusatzkraft, die die
> Radialkraft überwinden müsste. Beide Namen beschreiben dieselbe Kraft aus zwei Blickwinkeln:
> „Lorentzkraft" sagt, woher sie kommt, „Radialkraft" sagt, was sie bewirkt.

**Ansatz als Blockformel:**
- `data-tex`: `F_L = F_r \qquad\Longleftrightarrow\qquad |q| \cdot v \cdot B = \dfrac{m \cdot v^2}{r}`
- `data-plain`: `F_L = F_r   ⟺   |q| · v · B = m · v² / r`

**Auflösen (im Fließtext, ein Schritt sichtbar):**

> Auf beiden Seiten steht ein Faktor v. Kürzen und nach r auflösen:
> - `data-tex`: `r = \dfrac{m \cdot v}{|q| \cdot B}`
> - `data-plain`: `r = m · v / (|q| · B)`

**Lesart der Formel** (das ist der didaktisch wichtige Teil, nicht die Herleitung):

> Lies die Formel als Kräftespiel zwischen Trägheit und Ablenkung:
>
> | Größe größer | Radius | Warum |
> |---|---|---|
> | Masse m | **größer** | Ein trägeres Teilchen lässt sich schlechter aus der Bahn drücken. |
> | Geschwindigkeit v | **größer** | Es ist schneller wieder aus dem Bereich heraus, in dem die Kraft es krümmen konnte. |
> | Ladung |q| | **kleiner** | Mehr Ladung bedeutet mehr Kraft bei gleicher Trägheit. |
> | Flussdichte B | **kleiner** | Stärkeres Feld, stärkere Ablenkung, engere Kurve. |
>
> Zwei Größen stehen dabei nie einzeln, sondern immer als Paar: m und q tauchen ausschließlich
> als Quotient m/|q| auf. Das ist kein Zufall der Umformung, sondern der Grund, warum man aus
> einer Bahnmessung nie die Masse allein bestimmen kann — sondern nur das Verhältnis. Darauf
> kommt Abschnitt 3.5 zurück.

**Details-Block**, Summary: *„Wie kommt v ins Spiel? Die Beschleunigungsspannung"*

> In fast jedem Aufbau werden die Teilchen zuerst durch ein elektrisches Feld beschleunigt und
> treten erst danach ins Magnetfeld ein. Beim Durchlaufen der Spannung U wird die Arbeit
> W = |q| · U vollständig in kinetische Energie umgesetzt (im Vakuum, ohne Stöße):
> - `data-tex`: `|q| \cdot U = \tfrac{1}{2} m v^2 \quad\Longrightarrow\quad v = \sqrt{\dfrac{2 \cdot |q| \cdot U}{m}}`
> - `data-plain`: `|q| · U = ½ · m · v²   ⟹   v = √(2 · |q| · U / m)`
>
> Setzt du das in r = m·v/(|q|·B) ein, so fällt v heraus und es bleibt eine Formel, die nur noch
> Größen enthält, die du am Aufbau einstellst:
> - `data-tex`: `r = \dfrac{1}{B}\sqrt{\dfrac{2 \cdot m \cdot U}{|q|}}`
> - `data-plain`: `r = (1/B) · √(2 · m · U / |q|)`
>
> Beachte, dass r hier nur mit **√U** wächst, nicht mit U. Die vierfache Beschleunigungsspannung
> gibt den doppelten Radius. Diese Form ist die Rechengrundlage der Simulation in Abschnitt 4.

**Zahlenbeispiel** (Kontrollrechnung K-2):

> Ein Elektron wird mit U = 1000 V beschleunigt und tritt in ein Feld von B = 3,00 mT ein.
> - v = √(2 · 1,602 · 10⁻¹⁹ C · 1000 V / 9,109 · 10⁻³¹ kg) = 1,876 · 10⁷ m/s ≈ 18 755 km/s
> - r = 9,109 · 10⁻³¹ kg · 1,876 · 10⁷ m/s / (1,602 · 10⁻¹⁹ C · 3,00 · 10⁻³ T) = 3,55 · 10⁻² m
> - also **r ≈ 3,55 cm**, ein Kreis von rund 7,1 cm Durchmesser — passt genau in ein
>   Fadenstrahlrohr.
>
> Die Geschwindigkeit ist mit rund 6 % der Lichtgeschwindigkeit hoch, aber noch klar im Bereich,
> in dem die klassische Rechnung trägt. Oberhalb von etwa 10 % der Lichtgeschwindigkeit müsste
> man relativistisch rechnen; im Zentralabitur bleibt es bei der klassischen Form.

### 3.2 Die Umlaufdauer — und warum sie nicht von v abhängt

**Fließtext:**

> Für eine gleichförmige Kreisbewegung gilt der Zusammenhang zwischen Umfang, Geschwindigkeit
> und Umlaufdauer:
> - `data-tex`: `T = \dfrac{2\pi r}{v}`
> - `data-plain`: `T = 2 · π · r / v`
>
> Setz den Radius aus 3.1 ein:
> - `data-tex`: `T = \dfrac{2\pi}{v} \cdot \dfrac{m \cdot v}{|q| \cdot B} = \dfrac{2\pi \cdot m}{|q| \cdot B}`
> - `data-plain`: `T = (2 · π / v) · (m · v / (|q| · B)) = 2 · π · m / (|q| · B)`
>
> **Und jetzt schau genau hin, was verschwunden ist: das v.** Die Umlaufdauer hängt nicht von der
> Geschwindigkeit ab. Und weil r ebenfalls von v abhängt, hängt sie auch nicht vom Radius ab.
> Übrig bleiben nur zwei Dinge, die man dem Teilchen mitgibt (m und q) und eines, das man am
> Aufbau einstellt (B).

**Der Grund, in einem Satz** (wichtig — die Formel allein überzeugt niemanden):

> Ein doppelt so schnelles Teilchen läuft zwar auf einem doppelt so großen Kreis, muss also die
> doppelte Strecke zurücklegen — aber es legt sie eben auch mit doppelter Geschwindigkeit
> zurück. Beides hebt sich exakt auf.

**Zahlenprobe** (Kontrollrechnung K-3), als kleine Tabelle im `.tabelle`-Wrapper.
Elektron, B = 3,00 mT konstant:

| U | v | r | T |
|---|---|---|---|
| 200 V | 8 388 km/s | 1,59 cm | **11,91 ns** |
| 800 V | 16 775 km/s | 3,18 cm | **11,91 ns** |
| 2000 V | 26 524 km/s | 5,03 cm | **11,91 ns** |

> Die Geschwindigkeit verdreifacht sich, der Radius verdreifacht sich — die Umlaufdauer bleibt
> auf allen Nachkommastellen dieselbe.

**Zyklotronfrequenz:**

> Man gibt den Zusammenhang meist als Frequenz an. Sie heißt **Zyklotronfrequenz**:
> - `data-tex`: `f_c = \dfrac{1}{T} = \dfrac{|q| \cdot B}{2\pi \cdot m}`
> - `data-plain`: `f_c = 1/T = |q| · B / (2 · π · m)`
>
> Für das Elektron bei B = 3,00 mT sind das f_c = 84,0 MHz (Kontrollrechnung K-3), für ein
> Proton im selben Feld nur f_c = 45,7 kHz — das Proton ist rund 1836-mal träger.

**Merksatz 4** (`.merksatz`):

> **Kernaussage**
> Die Umlaufdauer eines geladenen Teilchens im Magnetfeld ist von seiner Geschwindigkeit
> unabhängig. Genau deshalb funktioniert ein Zyklotron: Man kann die Teilchen mit einer
> **festen** Wechselspannungsfrequenz immer weiter beschleunigen, obwohl sich ihr Bahnradius
> mit jedem Umlauf vergrößert. Sie kommen trotzdem stets im Takt an der Beschleunigungslücke an.

**Details-Block**, Summary: *„Das Zyklotron — und wo seine Grenze liegt"*

> Ein Zyklotron besteht aus zwei halbkreisförmigen, flachen Hohlkammern (den *Dees*) in einem
> starken, senkrecht stehenden Magnetfeld. Zwischen ihnen liegt ein schmaler Spalt, an dem eine
> Wechselspannung anliegt. Im Inneren der Dees ist das elektrische Feld abgeschirmt: Dort fliegt
> das Teilchen auf einem Halbkreis, ohne schneller zu werden. Nur im Spalt wird es beschleunigt.
>
> Damit das jedes Mal in die richtige Richtung geschieht, muss die Wechselspannung genau dann
> umpolen, wenn das Teilchen einen Halbkreis hinter sich hat. Weil die Umlaufdauer konstant ist,
> reicht dafür eine feste Frequenz f = f_c — man muss nichts nachregeln. Der Radius wächst mit
> jedem Durchgang, die Zeit pro Halbkreis bleibt gleich.
>
> **Die Grenze:** Sobald das Teilchen merklich relativistisch wird, wächst seine Masse, T wird
> größer, und es fällt aus dem Takt. Deshalb baut man für hohe Energien Synchrotrons, bei denen
> Frequenz und Feld während der Beschleunigung nachgeführt werden. Für Protonen liegt die
> praktische Grenze des klassischen Zyklotrons bei etwa 20 bis 25 MeV.

### 3.3 Der Wien'sche Geschwindigkeitsfilter

**Fließtext:**

> Aus einer Ionenquelle kommen Teilchen mit sehr unterschiedlichen Geschwindigkeiten. Für eine
> Messung des Bahnradius wäre das fatal, denn r hängt von v ab — eine Streuung in v verschmiert
> jedes Ergebnis. Man braucht also ein Bauteil, das aus dem Gemisch genau **eine**
> Geschwindigkeit heraussiebt. Das leistet der Geschwindigkeitsfilter nach Wien, und zwar mit
> einem Trick: Er lässt ein elektrisches und ein magnetisches Feld **gegeneinander** arbeiten.

**Aufbau (Beschreibung für die Inline-SVG-Abbildung):**

Waagerechter Kanal, links Eintrittsblende, rechts Austrittsblende. Oben und unten je eine
Kondensatorplatte (obere Platte „+", untere „−", damit E⃗ nach unten zeigt). Im gesamten Kanal
das ⊗-Raster für B in die Bildebene hinein. Ein Teilchen fliegt von links nach rechts. Zwei
Kraftpfeile am Teilchen, entgegengesetzt, grün: F_el und F_L.

**Die Bedingung:**

> Beide Kräfte stehen senkrecht zur Flugrichtung und einander entgegen. Ein Teilchen fliegt
> genau dann geradeaus durch, wenn sie sich aufheben:
> - `data-tex`: `F_{el} = F_L \qquad\Longleftrightarrow\qquad |q| \cdot E = |q| \cdot v \cdot B`
> - `data-plain`: `F_el = F_L   ⟺   |q| · E = |q| · v · B`
>
> Auf beiden Seiten steht |q|. Kürzen:
> - `data-tex`: `v = \dfrac{E}{B}`
> - `data-plain`: `v = E / B`

**Was daran bemerkenswert ist** (eigener Absatz, wird oft überlesen):

> Mit dem |q| ist **alles** verschwunden, was das Teilchen ausmacht: seine Ladung, ihr
> Vorzeichen und seine Masse. Übrig bleibt eine Bedingung, die nur noch die beiden
> Feldeinstellungen enthält. Ein Elektron, ein Proton und ein dreifach geladenes Uran-Ion werden
> von **derselben** Filtereinstellung durchgelassen, sofern sie gleich schnell sind.
>
> Und bei einem Teilchen mit umgekehrtem Vorzeichen? Dann kehren sich **beide** Kräfte um — die
> elektrische und die magnetische. Sie heben sich weiterhin auf. Der Filter arbeitet für positive
> und negative Ladungen mit derselben Einstellung.
>
> Praktisch stellt man E über die Plattenspannung ein: mit E = U_P/d wird die Durchlassbedingung
> zu
> - `data-tex`: `v = \dfrac{U_P}{d \cdot B}`
> - `data-plain`: `v = U_P / (d · B)`

**Zahlenbeispiel** (Kontrollrechnung K-4):

> Bei E = 1,2 · 10⁴ V/m und B = 4,0 mT läuft der Filter auf
> v = 1,2 · 10⁴ V/m / (4,0 · 10⁻³ T) = 3,0 · 10⁶ m/s = 3000 km/s.
> Alles, was schneller ist, hat eine zu große Lorentzkraft und wird zur einen Seite abgelenkt;
> alles Langsamere folgt der elektrischen Kraft zur anderen. Nur das Passende trifft die
> Austrittsblende.

**Merksatz 5** (`.merksatz`):

> **Kernaussage**
> Im Geschwindigkeitsfilter kürzt sich die Ladung heraus. Deshalb sortiert er nicht nach
> Teilchensorte, sondern **ausschließlich nach Geschwindigkeit** — und liefert damit erst die
> saubere Ausgangslage, in der eine Radiusmessung überhaupt etwas über die Teilchen aussagen
> kann.

### 3.4 Das Massenspektrometer

**Fließtext:**

> Setz die beiden Bauteile hintereinander, und du hast ein Messgerät:
>
> | Stufe | Bauteil | Leistung |
> |---|---|---|
> | 1 | Ionenquelle | erzeugt geladene Teilchen |
> | 2 | **Geschwindigkeitsfilter** (E ⊥ B) | lässt nur v = E/B durch — alle Teilchen jetzt gleich schnell |
> | 3 | **Ablenkkammer** (nur B₂) | Halbkreis mit r = m·v/(|q|·B₂) |
> | 4 | Detektor | misst den Auftreffabstand 2r vom Eintrittsspalt |
>
> Weil Stufe 2 die Geschwindigkeit festnagelt, ist der in Stufe 4 gemessene Abstand jetzt ein
> direktes Maß für m/|q|. Auflösen nach der Masse:
> - `data-tex`: `m = \dfrac{|q| \cdot r \cdot B_2}{v} = \dfrac{|q| \cdot r \cdot B_2 \cdot B_1}{E}`
> - `data-plain`: `m = |q| · r · B₂ / v = |q| · r · B₂ · B₁ / E`
>
> Wird statt des Filters eine Beschleunigungsspannung U verwendet (die häufigere
> Abituraufgabe), lautet die Auswertung
> - `data-tex`: `m = \dfrac{|q| \cdot r^2 \cdot B^2}{2U}`
> - `data-plain`: `m = |q| · r² · B² / (2 · U)`

**Warum das Gerät gebaut wird — Isotopentrennung** (Kontrollrechnung K-5):

> Der eigentliche Wert liegt in der Trennschärfe. Neon kommt in der Natur überwiegend als
> Ne-20 und Ne-22 vor. Beide Ionen sind chemisch nicht unterscheidbar und tragen dieselbe Ladung
> +e. Ihr Massenverhältnis ist 22/20 = 1,100 — ihre Radienverhältnis aber nur
> √(22/20) = 1,0488, denn bei fester Beschleunigungsspannung gilt r ∝ √m.
>
> Bei U = 2,00 kV und B = 600 mT bedeutet das:
>
> | Ion | Auftreffabstand 2r |
> |---|---|
> | Ne-20 | 9,598 cm |
> | Ne-22 | 10,067 cm |
> | **Differenz** | **0,469 cm ≈ 4,7 mm** |
>
> Knapp fünf Millimeter — messbar, aber knapp. Genau das ist der Grund, warum ein
> Massenspektrometer präzise Felder, gute Blenden und eine scharfe Geschwindigkeitsauswahl
> braucht. Es ist die Wurzel im Zusammenhang, die das Leben schwer macht: Ein Massenunterschied
> von 10 % erzeugt nur 4,9 % Unterschied im Radius.

### 3.5 Die spezifische Ladung q/m

**Fließtext:**

> Ein einzelnes Elektron kann man nicht auf eine Waage legen und seine Ladung nicht mit einem
> Amperemeter abzählen. Was man messen kann, ist die Bahn — und aus ihr fällt immer nur der
> **Quotient** heraus. Diese Größe heißt **spezifische Ladung**:
> - `data-tex`: `\dfrac{|q|}{m} \qquad \left[\dfrac{|q|}{m}\right] = 1\,\dfrac{\mathrm{C}}{\mathrm{kg}}`
> - `data-plain`: `|q| / m     [|q|/m] = 1 C/kg`
>
> Stell r = (1/B)·√(2·m·U/|q|) nach ihr um:
> - `data-tex`: `\dfrac{|q|}{m} = \dfrac{2U}{r^2 \cdot B^2}`
> - `data-plain`: `|q| / m = 2 · U / (r² · B²)`
>
> Auf der rechten Seite steht nur noch Messbares: die Beschleunigungsspannung am Netzgerät, die
> Flussdichte des Helmholtz-Spulenpaares und der Bahnradius, den du im Fadenstrahlrohr mit einem
> Spiegelmaßstab abliest. **Das ist eine Schulmessung**, und sie liefert eine
> Naturkonstante — das ist der Grund, warum das Fadenstrahlrohr in fast jeder Sammlung steht.

**Werte** (Kontrollrechnung K-6), als Tabelle im `.tabelle`-Wrapper:

| Teilchen | Ladung q | Masse m | |q|/m in C/kg |
|---|---|---|---|
| Elektron | −e | 9,109 · 10⁻³¹ kg | 1,759 · 10¹¹ |
| Positron | +e | 9,109 · 10⁻³¹ kg | 1,759 · 10¹¹ |
| Proton | +e | 1,673 · 10⁻²⁷ kg | 9,579 · 10⁷ |
| Alphateilchen (He-4²⁺) | +2e | 6,645 · 10⁻²⁷ kg | 4,822 · 10⁷ |
| Ne-20-Ion (einfach) | +e | 3,321 · 10⁻²⁶ kg | 4,824 · 10⁶ |
| Ne-22-Ion (einfach) | +e | 3,653 · 10⁻²⁶ kg | 4,386 · 10⁶ |

**Drei Beobachtungen, die der Text ausdrücklich zieht** (nicht dem Leser überlassen):

> 1. Die spezifische Ladung des Elektrons ist rund **1836-mal größer** als die des Protons —
>    genau das Verhältnis ihrer Massen, denn die Ladungsbeträge sind gleich. Ein Elektron wird im
>    gleichen Feld also viel enger auf die Kreisbahn gezwungen.
> 2. Das **Alphateilchen** trägt die doppelte Ladung, hat aber auch fast die vierfache
>    Protonenmasse. Seine spezifische Ladung liegt deshalb **unter** der des Protons, ungefähr
>    bei der Hälfte. Mehr Ladung heißt nicht automatisch stärkere Ablenkung.
> 3. **Elektron und Positron** haben dieselbe spezifische Ladung — der Betrag verrät das
>    Vorzeichen nicht. Unterscheiden kann man sie nur am **Umlaufsinn**: im ⊗-Feld läuft das
>    Elektron im Uhrzeigersinn, das Positron dagegen. Genau daran hat Carl Anderson 1932 in einer
>    Nebelkammer das Positron erkannt.

**Merksatz 6** (`.merksatz`):

> **Kernaussage**
> Aus einer Bahnmessung im Magnetfeld bekommst du niemals die Masse und niemals die Ladung
> einzeln — immer nur ihr Verhältnis. Wer die Masse eines Teilchens angeben will, braucht eine
> zweite, unabhängige Messung der Ladung. Genau diese Rolle spielt der Millikan-Versuch neben
> dem Fadenstrahlrohr.

## 4 · Interaktiver Kern

Überschrift der Section: **Teilchen im Feld — Kreisbahn und Geschwindigkeitsfilter**
(`<section id="simulation">`, `.stufe`-Nummer 4)

Einleitungssatz über der Simulation:

> Bis hierher hast du gerechnet. Jetzt schickst du selbst Teilchen ins Feld und prüfst, ob sich
> die Formeln so verhalten, wie du es hergeleitet hast. Die Simulation rechnet nichts anderes als
> die drei Beziehungen aus den Abschnitten 2 und 3 — sie zeigt sie nur gleichzeitig.

**Der Bauagent erfindet in diesem Abschnitt nichts.** Jede Konstante, jeder Reglerbereich, jede
Rundungsstelle und jede Zeichengröße steht unten. Was nicht dasteht, wird nachgefragt.

### 4.1 Verbindliche Konstanten

Alle Konstanten stehen als benannte Konstanten am Anfang der Simulations-IIFE, mit den hier
angegebenen Stellen. Gerundet wird ausschließlich in der Anzeige, nie in der Rechnung.

```js
// --- Naturkonstanten (CODATA 2018; e ist per SI-Definition exakt) ---
var E_LAD   = 1.602176634e-19;   // Elementarladung e in C   (exakt)
var M_E     = 9.1093837015e-31;  // Elektronenmasse in kg
var M_P     = 1.67262192369e-27; // Protonenmasse in kg
var U_ATOM  = 1.66053906660e-27; // atomare Masseneinheit u in kg
var M_ALPHA = 6.6446573357e-27;  // Masse des Alphateilchens (He-4-Kern) in kg
var C_LICHT = 2.99792458e8;      // Lichtgeschwindigkeit in m/s (nur für die v/c-Warnung)
```

### 4.2 Der Maßstab Pixel ↔ Meter

**Genau eine Umrechnungskonstante für die ganze Simulation, beide Modi, alle Teilchen:**

```js
var CANVAS_B = 1000;      // interne Canvas-Breite  in px  (CSS: width:100%)
var CANVAS_H = 640;       // interne Canvas-Höhe    in px
var SKALA    = 4.00e-4;   // Meter pro Pixel  ->  1 cm = 25 px
```

Damit bildet die Leinwand einen realen Ausschnitt von **40,0 cm × 25,6 cm** ab — ungefähr die
Grundfläche eines Fadenstrahlrohrs mit Spulen. Umrechnung in beide Richtungen:

- `data-tex`: `x_{\text{px}} = \dfrac{x_{\text{m}}}{\texttt{SKALA}} \qquad x_{\text{m}} = x_{\text{px}} \cdot \texttt{SKALA}`
- `data-plain`: `x_px = x_m / SKALA     x_m = x_px · SKALA`

**Maßstabsbalken (Pflicht, keine Zier):** unten links im Canvas ein waagerechter Balken von
**125 px Länge** mit der Beschriftung **„5 cm"**, Farbe `#64748b`, darüber die Endstriche.
125 px · 4,00 · 10⁻⁴ m/px = 0,0500 m ✓. Ohne diesen Balken ist keine der angezeigten Längen
im Bild nachprüfbar.

**Canvas-Umrechnung y:** wie in Abschnitt 0.1 festgelegt rechnet der Bauagent physikalisch mit
y nach oben und setzt beim Zeichnen `y_canvas = Y_QUELLE − y_physik / SKALA`.

### 4.3 Teilchenauswahl

Aufklappliste `#selTeilchen` mit vier Einträgen. Masse und Ladungsbetrag stehen fest, das
**Vorzeichen** kommt aus dem getrennten Schalter `#selVorzeichen` (4.4).

| `value` | Anzeigetext in der Liste | Masse m | Ladungsbetrag | q-Betrag/m in C/kg |
|---|---|---|---|---|
| `elektron` | Elektron / Positron | 9,1093837015 · 10⁻³¹ kg | 1 e | 1,759 · 10¹¹ |
| `proton` | Proton | 1,67262192369 · 10⁻²⁷ kg | 1 e | 9,579 · 10⁷ |
| `alpha` | Alphateilchen (He-4, 2+) | 6,6446573357 · 10⁻²⁷ kg | 2 e | 4,822 · 10⁷ |
| `neon` | Ne-20-Ion (einfach geladen) | 20,0 u = 3,3210781332 · 10⁻²⁶ kg | 1 e | 4,824 · 10⁶ |

Für das Neon-Ion wird ausdrücklich mit **20,0 u** gerechnet, nicht mit der exakten Isotopenmasse
19,99244 u. Das steht so auch unter der Simulation als Fußnote, damit niemand die vierte Stelle
sucht. Der Wert q-Betrag/m wird angezeigt (4.6) und ist die Brücke zu Abschnitt 3.5.

### 4.4 Regler und Bedienelemente — vollständige Liste

Alle Regler sind `<input type="range">` in `.regler`, jeweils mit Beschriftung links und
Zahlenwert rechts. Die Zahlenwerte werden mit `fmt()` und Komma ausgegeben.

| Element-ID | Größe | Min | Max | Schritt | Startwert | Anzeigeformat |
|---|---|---|---|---|---|---|
| `#rU` | Beschleunigungsspannung U | 200 V | 1800 V | 10 V | **450 V** | ganzzahlig, „ V" |
| `#rB` | Flussdichte B | teilchenabhängig, Tabelle unten | | | | siehe Tabelle |
| `#rUP` | Plattenspannung U_P (nur Modus 2) | 0 V | 4000 V | 2 V | **754 V** | ganzzahlig, „ V" |

**Der B-Regler wird beim Wechsel der Teilchenart umgesetzt.** Das ist Absicht und wird der
Klasse gesagt: Ein Neon-Ion braucht bei gleicher Spannung ein rund 190-mal stärkeres Feld, um
auf denselben Kreis gezwungen zu werden. Genau das ist die Aussage von r ∝ √(m/q-Betrag).

| Teilchen | B min | B max | Schritt | Startwert | Rasterprobe |
|---|---|---|---|---|---|
| Elektron / Positron | 2,5 mT | 7,0 mT | 0,1 mT | **3,0 mT** | 45 Schritte, Start auf Raster ✓ |
| Proton | 110 mT | 300 mT | 5 mT | **130 mT** | 38 Schritte, Start auf Raster ✓ |
| Alphateilchen | 150 mT | 420 mT | 5 mT | **185 mT** | 54 Schritte, Start auf Raster ✓ |
| Ne-20-Ion | 480 mT | 1300 mT | 10 mT | **580 mT** | 82 Schritte, Start auf Raster ✓ |

Verhalten beim Teilchenwechsel: `min`, `max`, `step` und `value` des B-Reglers werden auf die
Zeile der neuen Teilchenart gesetzt (also auf den **Startwert**, nicht auf einen geklemmten alten
Wert). Der U-Regler und der U_P-Regler bleiben stehen. Die Rasterprobe steht in Kontrollrechnung
K-14.

**Weitere Bedienelemente:**

| Element-ID | Art | Wirkung |
|---|---|---|
| `#selTeilchen` | `<select>` | Teilchenart, Tabelle 4.3 |
| `#selVorzeichen` | `<select>` mit `negativ` / `positiv` | setzt das Vorzeichen von q |
| `#modKreis` / `#modWien` | zwei Radios `name="modus"` | Modusumschaltung |
| `#bStart` | Knopf `.primaer` | startet / pausiert die Animation (Beschriftung wechselt „Start" ↔ „Pause") |
| `#bReset` | Knopf | setzt Teilchen an den Startpunkt zurück, Regler bleiben |

Der Vorzeichenschalter startet abhängig von der Teilchenart: `elektron` → **negativ**,
alle anderen → **positiv**. Er wird beim Teilchenwechsel auf diesen Vorgabewert gesetzt, kann
danach aber frei umgestellt werden. Der angezeigte Name folgt dieser Tabelle:

| Teilchenart | q < 0 | q > 0 |
|---|---|---|
| `elektron` | Elektron | Positron |
| `proton` | Antiproton | Proton |
| `alpha` | Anti-Alphateilchen | Alphateilchen |
| `neon` | Ne-20-Ion (negativ) | Ne-20-Ion (positiv) |

Der Name steht in der Anzeigezeile, damit „Vorzeichen umschalten" nicht als Rechentrick
durchgeht, sondern als Wechsel des Teilchens gelesen wird.

### 4.5 Modus 1 — Kreisbahn

**Bild.** Die gesamte Leinwand ist Feldbereich: ein Raster aus ⊗-Symbolen, 9 Spalten × 6 Zeilen,
Abstand 110 px waagerecht und 100 px senkrecht, Farbe `#64748b`, Kreisdurchmesser 14 px mit
eingezeichnetem Kreuz. B zeigt also überall in die Bildebene hinein (Abschnitt 0.2).

**Quellpunkt** `Q = (500 px; 320 px)`, also die Mitte der Leinwand. Dort sitzt eine kleine
Blende (zwei kurze schwarze Striche) und ein waagerechter Pfeil nach rechts als v⃗. Das Teilchen
startet in Q mit v⃗ = (v; 0; 0).

**Rechnung** (analytisch, nicht integriert — die Kreisbahn ist exakt bekannt):

- `data-tex`: `v = \sqrt{\dfrac{2 \cdot |q| \cdot U}{m}} \qquad r = \dfrac{m \cdot v}{|q| \cdot B} \qquad T = \dfrac{2\pi \cdot m}{|q| \cdot B}`
- `data-plain`: `v = √(2 · |q| · U / m)     r = m · v / (|q| · B)     T = 2 · π · m / (|q| · B)`

**Mittelpunkt der Bahn.** Nach Abschnitt 0.5: B ⊗, v⃗ nach rechts.

| Vorzeichen von q | Kraft am Start | Mittelpunkt | Umlaufsinn im Bild | Farbe |
|---|---|---|---|---|
| q < 0 | nach unten | `(500; 320 + r/SKALA)` px | im Uhrzeigersinn | Blau `#1d4ed8` |
| q > 0 | nach oben | `(500; 320 − r/SKALA)` px | gegen den Uhrzeigersinn | Rot `#b91c1c` |

Gezeichnet wird: der volle Bahnkreis als dünne gestrichelte Linie in der Teilchenfarbe, darauf
der bereits durchlaufene Bogen als kräftige durchgezogene Linie, das Teilchen als gefüllter
Kreis mit 7 px Radius, dazu am Teilchen zwei Pfeile — v⃗ tangential in Schwarz `#0f172a`
(feste Länge 55 px) und F⃗ zum Mittelpunkt in Grün `#0d7a52` (feste Länge 40 px). Beide Pfeile
haben **feste** Länge; sie zeigen Richtungen, nicht Beträge, und das steht als Bildunterschrift
darunter.

**Winkel des Teilchens.** Startwinkel so, dass das Teilchen in Q sitzt und nach rechts fliegt;
Fortschreiten mit der Winkelgeschwindigkeit ω = 2π/T, Drehsinn nach der Tabelle oben.

**Zeitlupe.** Reale Umlaufdauern liegen zwischen 5,10 ns und 2713 ns; ohne Zeitlupe sieht man
nichts. Deshalb ein fester Zeitlupenfaktor Z je Teilchenart:

- `data-tex`: `\Delta t_{\text{phys}} = \dfrac{\Delta t_{\text{Bild}}}{Z}`
- `data-plain`: `Δt_phys = Δt_Bild / Z`

| Teilchen | Z | Bildschirm-Umlaufdauer bei B min / Start / B max |
|---|---|---|
| Elektron / Positron | 2,0 · 10⁸ | 2,86 s / 2,38 s / 1,02 s |
| Proton | 5,0 · 10⁶ | 2,98 s / 2,52 s / 1,09 s |
| Alphateilchen | 5,0 · 10⁶ | 4,34 s / 3,52 s / 1,55 s |
| Ne-20-Ion | 1,0 · 10⁶ | 2,71 s / 2,25 s / 1,00 s |

Z hängt **nicht** von U ab. Das ist der Kern des Beobachtungsauftrags: Wenn U vervierfacht wird,
läuft das Teilchen sichtbar doppelt so schnell auf einem doppelt so großen Kreis und braucht auf
dem Bildschirm exakt gleich lange für einen Umlauf. Kontrollrechnung K-9 und K-10.

Der Bildzeitschritt wird nach `bausteine.md` mit `Math.min(0.05, (t - tAlt)/1000)` begrenzt.

### 4.6 Anzeigefeld (beide Modi)

Ein `.anzeige`-Block unter dem Canvas, jeder Wert in einer eigenen Zelle mit Beschriftung.
**Rundungsstellen sind verbindlich** und über den ganzen Reglerbereich geprüft (K-15):

| ID | Beschriftung | Formel | Einheit und Stellen | Bereich über alle Regler |
|---|---|---|---|---|
| `#aTeilchen` | Teilchen | Name nach 4.4 | Text, dazu `q = +e` / `q = −2e` … | — |
| `#aV` | Geschwindigkeit v | √(2·q-Betrag·U/m) | **km/s, 1 Nachkommastelle** | 43,9 … 25 163,0 km/s |
| `#aR` | Bahnradius r | m·v/(q-Betrag·B) | **cm, 2 Nachkommastellen** | 0,68 … 5,76 cm |
| `#aT` | Umlaufdauer T | 2π·m/(q-Betrag·B) | **ns mit 2 NKS, falls T < 1000 ns; sonst µs mit 3 NKS** | 5,10 ns … 2,713 µs |
| `#aF` | Zyklotronfrequenz f_c | 1/T | MHz mit 2 NKS, falls ≥ 1 MHz; sonst kHz mit 1 NKS | 0,37 MHz … 196,08 MHz |
| `#aQm` | spezifische Ladung | q-Betrag/m | C/kg in der Form `4,82 · 10⁷` | 4,824 · 10⁶ … 1,759 · 10¹¹ |

Zusätzlich eine graue Fußzeile unter der Anzeige mit dem Verhältnis v/c:
`v/c = 4,20 %` bei den Startwerten, größter Wert über alle Regler **8,393 %** (Elektron,
1800 V). Sobald v/c > 8 % steigt, wird der Text orange `#b45309` und ergänzt:
*„über 10 % müsste relativistisch gerechnet werden"*. Das ist keine Fehlermeldung, sondern die
Einordnung aus Abschnitt 3.1.

In Modus 2 werden `#aR`, `#aT` und `#aF` ausgeblendet (der Begriff Umlaufdauer trägt dort nicht)
und stattdessen der Block aus 4.7 eingeblendet.

### 4.7 Modus 2 — Wien'scher Geschwindigkeitsfilter

**Geometrie**, alles in derselben Leinwand 1000 × 640 px und demselben Maßstab
SKALA = 4,00 · 10⁻⁴ m/px:

| Bauteil | Canvas | real |
|---|---|---|
| Eintrittsblende / Startpunkt | `(100; 320)` px | — |
| Plattenlänge L | x = 100 … 350 px, also 250 px | **L = 0,100 m** |
| Plattenabstand d | y = 295 … 345 px, also 50 px | **d = 0,020 m** |
| obere Platte | y = 295 px, Beschriftung `+` | E⃗ zeigt nach unten |
| untere Platte | y = 345 px, Beschriftung `−` | |
| Driftstrecke D (feldfrei) | x = 350 … 930 px, also 580 px | **D = 0,232 m** |
| Schirm mit Austrittsblende | x = 930 px, senkrechte Linie | Blende y = 310 … 330 px |
| halbe Blendenöffnung | 10 px | **4,0 mm** |

Das ⊗-Raster wird in Modus 2 **nur zwischen den Platten** gezeichnet (3 Spalten × 2 Zeilen), und
die Feldpfeile für E⃗ als drei kurze graue Pfeile von der oberen zur unteren Platte. Außerhalb
der Platten ist die Fläche leer — dort sind **beide** Felder null. Das ist keine
Zeichenvereinfachung, sondern Voraussetzung für die Auswertung: Nach den Platten fliegt das
Teilchen geradeaus.

**Rechnung.**

- `data-tex`: `E = \dfrac{U_P}{d} \qquad v_d = \dfrac{E}{B} = \dfrac{U_P}{d \cdot B} \qquad \varepsilon = \dfrac{v_d - v}{v}`
- `data-plain`: `E = U_P / d     v_d = E / B = U_P / (d · B)     ε = (v_d − v) / v`

v_d ist die **Durchlassgeschwindigkeit** des Filters, v die tatsächliche Geschwindigkeit aus der
Beschleunigungsspannung. Für ε = 0 fliegt das Teilchen exakt geradeaus.

**Ablenkung.** Die y-Kraft im Plattenbereich ist

- `data-tex`: `F_y = q \cdot (v \cdot B - E) = q \cdot B \cdot (v - v_d)`
- `data-plain`: `F_y = q · (v · B − E) = q · B · (v − v_d)`

mit **vorzeichenbehaftetem q**. Daraus die Ablenkung am Schirm (Kontrollformel, siehe K-21):

- `data-tex`: `y_{\text{Schirm}} = \dfrac{q}{m} \cdot B \cdot (v - v_d) \cdot \dfrac{L \cdot \left(\frac{L}{2} + D\right)}{v^{2}}`
- `data-plain`: `y_Schirm = (q/m) · B · (v − v_d) · L · (L/2 + D) / v²`

Positives y bedeutet Ablenkung **nach oben**. Zahlenwerte in K-21. Der Hebelarm
L·(L/2 + D) = 0,02820 m² ist eine Konstante der Geometrie.

**Wie die Bahn gezeichnet wird.** Bei jeder Reglerbewegung wird die Bahn **einmal** numerisch
integriert und als Polygonzug gespeichert; die Animation schiebt das Teilchen anschließend nur
noch an diesem Polygonzug entlang. Das entkoppelt die Genauigkeit von der Bildrate.

- Integrator: Boris-Verfahren (halber E-Stoß, magnetische Drehung, halber E-Stoß), weil es die
  Energie im reinen B-Feld exakt erhält.
- Zeitschritt: `dt = t_ges / 4000` mit `t_ges = 1,2 · (L + D) / v`.
- Abbruch, sobald `x > 930 px` (Schirm erreicht) **oder** `|y_physik| > d/2` innerhalb der
  Platten. Im zweiten Fall endet die Bahn dort mit einem kleinen Kreuz auf der Platte.
- Abnahmeprobe: Solange `|y_Schirm| ≤ 2 cm` bleibt, muss der integrierte Endwert mit der
  Kontrollformel oben auf **besser als 1 %** übereinstimmen. Diese Probe gehört in die
  Abnahme der Simulation.

**Statusanzeige.** Drei Zustände, mit Farbe und Klartext:

| Bedingung | Text in `#aStatus` | Farbe |
|---|---|---|
| `\|y\| > d/2` schon zwischen den Platten | „von der Platte verschluckt" | Rot `#b91c1c` |
| Schirm erreicht, `\|y_Schirm\| > 4,0 mm` | „verfehlt die Blende" | Orange `#b45309` |
| Schirm erreicht, `\|y_Schirm\| ≤ 4,0 mm` | „**kommt durch**" | Grün `#0d7a52` |

**Zusätzliche Anzeigen in Modus 2:**

| ID | Beschriftung | Einheit und Stellen |
|---|---|---|
| `#aE` | elektrische Feldstärke E | kV/m, 2 Nachkommastellen (Bereich 20,83 … 176,17 kV/m bei passender Einstellung) |
| `#aVd` | Durchlassgeschwindigkeit v_d = E/B | km/s, 1 Nachkommastelle |
| `#aEps` | Abweichung ε | %, 3 Nachkommastellen, mit Vorzeichen |
| `#aY` | Ablenkung am Schirm | mm, 2 Nachkommastellen, mit Vorzeichen |
| `#aStatus` | Status | Text nach Tabelle oben |

**Bedienung, Schritt für Schritt** — genau so steht es als grauer Hinweistext unter den
Reglern des Modus 2:

> 1. Stell Teilchen, U und B ein. Die Anzeige nennt dir v.
> 2. Schieb U_P so lange, bis **v_d gleich v** ist. Die Anzeige ε zeigt dir, wie weit du noch
>    daneben liegst; bei ε = 0 ist der Filter genau auf dieses Teilchen eingestellt.
> 3. Ist ε klein genug, geht das Teilchen durch die Blende. Wie klein „klein genug" ist, findest
>    du selbst heraus — der Filter verzeiht ungefähr ein Drittel Prozent.
> 4. Und dann die eigentliche Frage: Was passiert, wenn du **das Teilchen wechselst**, ohne am
>    Filter etwas zu verstellen?

**Auflösung des Filters** (K-17): Die halbe Blendenöffnung von 4,0 mm entspricht
ε_max = 0,26 % bis 0,34 % — über alle Teilchen und alle Reglerstellungen nahezu gleich, weil
sie nur vom Bahnradius im Filterfeld abhängt:

- `data-tex`: `\varepsilon_{\max} = \dfrac{y_{\text{Blende}} \cdot r}{L \cdot \left(\frac{L}{2}+D\right)}`
- `data-plain`: `ε_max = y_Blende · r / (L · (L/2 + D))`

Bei den Startwerten (Elektron, B = 3,0 mT, U = 450 V) ist ε_max = 0,338 %, das entspricht einem
U_P-Fenster von ± 2,55 V — also gut zwei Rasterschritten des Reglers. Der Filter ist damit
scharf genug, um etwas zu zeigen, und grob genug, um ihn von Hand zu treffen.

### 4.8 Kontrollrechnung: Bleiben alle Bahnen im Bild?

Geprüft wurden **alle 16 Kombinationen** aus B min / B max × U min / U max × vier Teilchenarten
(Skript `ergaenzung_4_9.py`, Ausgabe K-8). Sichtbarkeitsfenster: Der Kreis passt ins Bild, wenn
2 · r_px ≤ 300 px (Abstand Quellpunkt zum oberen bzw. unteren Rand minus 20 px Rand), und er ist
noch erkennbar, wenn r_px ≥ 16 px.

| Teilchen | B | U | r | r in px | im Bild |
|---|---|---|---|---|---|
| Elektron / Positron | 2,5 mT | 200 V | 1,908 cm | 47,7 | ja |
| Elektron / Positron | 2,5 mT | 1800 V | 5,723 cm | 143,1 | ja |
| Elektron / Positron | 7,0 mT | 200 V | 0,681 cm | 17,0 | ja |
| Elektron / Positron | 7,0 mT | 1800 V | 2,044 cm | 51,1 | ja |
| Proton | 110 mT | 200 V | 1,858 cm | 46,4 | ja |
| Proton | 110 mT | 1800 V | 5,573 cm | 139,3 | ja |
| Proton | 300 mT | 200 V | 0,681 cm | 17,0 | ja |
| Proton | 300 mT | 1800 V | 2,043 cm | 51,1 | ja |
| Alphateilchen | 150 mT | 200 V | 1,920 cm | 48,0 | ja |
| Alphateilchen | 150 mT | 1800 V | 5,760 cm | 144,0 | ja |
| Alphateilchen | 420 mT | 200 V | 0,686 cm | 17,1 | ja |
| Alphateilchen | 420 mT | 1800 V | 2,057 cm | 51,4 | ja |
| Ne-20-Ion | 480 mT | 200 V | 1,897 cm | 47,4 | ja |
| Ne-20-Ion | 480 mT | 1800 V | 5,691 cm | 142,3 | ja |
| Ne-20-Ion | 1300 mT | 200 V | 0,700 cm | 17,5 | ja |
| Ne-20-Ion | 1300 mT | 1800 V | 2,101 cm | 52,5 | ja |

**Kleinster Radius 17,0 px, größter 144,0 px — beide innerhalb des Fensters 16 … 150 px.**
Der größte Kreis hat 288 px Durchmesser und passt mit 32 px Luft zwischen Quellpunkt und Rand.
Die B-Bereiche der vier Teilchen sind genau darauf zugeschnitten worden; die Physik wurde dafür
an keiner Stelle angefasst.

### 4.9 Beobachtungsauftrag

Kasten `<div class="auftrag">` direkt über der Simulation, Wortlaut verbindlich:

> **Beobachtungsauftrag**
>
> **Teil A — Kreisbahn.** Wähle *Elektron*, stelle **B = 3,0 mT** und **U = 450 V** ein und
> starte. Notiere v, r und T. Stelle jetzt **U = 1800 V** ein, also den **vierfachen** Wert,
> und lass B unverändert. Notiere wieder v, r und T.
>
> Beantworte schriftlich: Um welchen Faktor ändert sich v? Um welchen Faktor r? Und was macht T?
> Formuliere einen Satz, der erklärt, **warum** T sich so verhält, obwohl das Teilchen doppelt so
> schnell ist. Der Satz muss die Wörter *Umfang* und *Geschwindigkeit* enthalten.
>
> **Teil B — Gegenprobe.** Geh zurück auf U = 450 V und **verdopple stattdessen B** auf 6,0 mT.
> Was ändert sich jetzt an v, r und T — und was nicht? Ergänze deinen Satz um die Rolle von B.
>
> **Teil C — Filter.** Schalte auf *Wien-Filter*. Stelle *Proton*, **B = 200 mT**, **U = 450 V**
> ein und schiebe U_P, bis das Proton durch die Blende geht. Ändere jetzt **nichts** am Filter,
> sondern wechsle auf *Alphateilchen*. Es wird von der Platte verschluckt. Finde durch Probieren
> die Spannung U, bei der auch das Alphateilchen durchkommt, und erkläre, was diese beiden
> Teilchen in diesem Moment gemeinsam haben — und was nicht.

Die Zahlen, die dabei herauskommen müssen, stehen in K-10 (Teil A und B) und K-21 (Teil C):
U_P = 1174 V lässt das Proton bei 450 V durch (ε = −0,039 %, y = +0,72 mm) und das
Alphateilchen bei **890 V** (ε = +0,176 %, y = −1,64 mm). Bei 450 V trifft das Alphateilchen
die Platte (ε = +40,9 %).

### 4.10 Verständnisfragen zur Simulation

Zwei Multiple-Choice-Aufgaben unmittelbar unter der Simulation, Schlüssel `sim1` und `sim2`,
beide `<span class="ab">Anforderungsbereich II</span>`.

---

#### sim1 — Warum bleibt T gleich?

**Frage:** In Teil A hast du U von 450 V auf 1800 V vervierfacht. Dabei verdoppelte sich v,
der Radius verdoppelte sich ebenfalls, die Umlaufdauer T blieb bei 11,91 ns stehen. Welche
Begründung trifft zu?

| `data-i` | Option |
|---|---|
| 0 | T bleibt gleich, weil das Magnetfeld unverändert war und T nur von B, m und q abhängt: Der doppelte Weg wird mit doppelter Geschwindigkeit zurückgelegt, beides kürzt sich heraus. |
| 1 | T bleibt gleich, weil die Lorentzkraft keine Arbeit verrichtet und deshalb keine Größe der Bewegung sich ändern kann. |
| 2 | T bleibt nur scheinbar gleich, weil die Anzeige auf zwei Nachkommastellen rundet; bei mehr Stellen sähe man, dass T mit wachsendem v kleiner wird. |

**`mcDaten`-Eintrag:**

```js
sim1:{ r:0, fb:[
  "Richtig. In T = 2·π·m/(|q|·B) kommt v überhaupt nicht vor. Anschaulich: Der Umfang 2πr wächst um denselben Faktor wie v, deshalb bleibt der Quotient 2πr/v konstant. Genau darauf beruht das Zyklotron mit seiner festen Frequenz.",
  "Die Aussage über die Arbeit stimmt, die Folgerung nicht. Aus W = 0 folgt nur, dass der Betrag von v konstant bleibt, solange das Teilchen im Feld ist. Geändert hast du v aber vorher, in der Beschleunigungsstrecke mit dem elektrischen Feld — und trotzdem blieb T gleich. Der Grund liegt woanders: v kürzt sich in T = 2πr/v heraus.",
  "Das lässt sich in der Simulation widerlegen: Bei U = 450 V steht T = 11,91 ns, bei U = 1800 V ebenfalls 11,91 ns, und die Bildschirm-Umlaufdauer von 2,38 s ändert sich sichtbar nicht. Es ist kein Rundungseffekt, sondern exakt: Setzt man r = m·v/(|q|·B) in T = 2πr/v ein, fällt v heraus."
]}
```

---

#### sim2 — Was der Filter sortiert

**Frage:** In Teil C ließ dieselbe Filtereinstellung (B = 200 mT, U_P = 1174 V) sowohl das
Proton bei U = 450 V als auch das Alphateilchen bei U = 890 V durch, obwohl das Alphateilchen
rund viermal so schwer ist und die doppelte Ladung trägt. Was folgt daraus?

| `data-i` | Option |
|---|---|
| 0 | Der Filter lässt Teilchen mit gleicher **kinetischer Energie** durch; 890 V und 450 V ergeben bei doppelter Ladung dieselbe Energie. |
| 1 | Der Filter lässt Teilchen mit gleicher **Geschwindigkeit** durch, unabhängig von Masse und Ladung — bei U = 890 V hat das Alphateilchen fast genau die Geschwindigkeit des Protons bei 450 V. |
| 2 | Der Filter lässt Teilchen mit gleichem **Verhältnis q/m** durch; Proton und Alphateilchen liegen darin zufällig nahe beieinander. |

**`mcDaten`-Eintrag:**

```js
sim2:{ r:1, fb:[
  "Die Energien sind tatsächlich verschieden: Das Proton bekommt E = e · 450 V = 450 eV, das Alphateilchen E = 2e · 890 V = 1780 eV, fast das Vierfache. Prüf es in der Anzeige nach — gleich ist dort nur v: 293,6 km/s gegen 293,0 km/s. Die Durchlassbedingung |q|·E = |q|·v·B kürzt die Ladung heraus, es bleibt v = E/B.",
  "Richtig. Aus |q| · E = |q| · v · B folgt v = E/B — die Ladung kürzt sich, die Masse taucht gar nicht erst auf. Der Filter kennt nur eine Größe des Teilchens: seine Geschwindigkeit. Proton bei 450 V: 293,6 km/s, Alphateilchen bei 890 V: 293,0 km/s — Abweichung 0,18 %, das liegt innerhalb der Blende.",
  "Die spezifischen Ladungen liegen keineswegs nahe beieinander: Für das Proton sind es 9,58 · 10⁷ C/kg, für das Alphateilchen 4,82 · 10⁷ C/kg, also gut das Doppelte. Genau das siehst du in Modus 1, wo beide bei gleichem U und gleichem B völlig verschiedene Radien haben. Im Filter dagegen kürzt sich q heraus, und m kommt in v = E/B überhaupt nicht vor."
]}
```

---

**Hinweis an den Bauagenten:** Beide Fragen setzen voraus, dass der Beobachtungsauftrag
tatsächlich ausgeführt wurde. Sie stehen deshalb **unter** der Simulation, nicht darüber, und
die Karte trägt die Überschrift *Ausgewertet*.

## 5 · Übungen

Überschrift der Section: **Übungen — vom Einsetzen zum Beurteilen**
(`<section id="uebungen">`, `.stufe`-Nummer 5)

Einleitungssatz über der ersten Aufgabe:

> Zehn Aufgaben, aufsteigend. Die ersten drei prüfen, ob du die drei Formeln sicher bedienst.
> Danach wird es messtechnisch: Du wertest Bahnen aus, statt sie vorherzusagen. Die letzten drei
> Aufgaben rechnest du gar nicht mehr — du begründest und beurteilst. Genau in dieser Reihenfolge
> kommen sie auch im Abitur.

**Verbindlich für alle Aufgaben dieses Abschnitts:** Es gilt durchgehend die Konvention aus
Abschnitt 0 — B⃗ steht senkrecht auf der Bildebene, im Standardfall ⊗; das Teilchen tritt von
links nach rechts ein; in Betragsformeln steht **|q|**. Alle Rechnungen sind klassisch, ohne
relativistische Korrektur; die größte auftretende Geschwindigkeit ist 6,3 % von c (Aufgabe ue1),
und der Fehler bleibt damit unter 0,3 %.

Zahlenwerte, Toleranzen und Rückmeldetexte sind unten vollständig angegeben. Jede Zahl ist in
5.11 nachgerechnet (K-22 bis K-30); der Bauagent rechnet nichts nach und erfindet nichts.

**Übersicht für den Bauagenten:**

| Schlüssel | Typ | Anforderungsbereich | Thema |
|---|---|---|---|
| `ue1` | Zahleneingabe | I | Bahnradius eines Elektrons aus U und B |
| `ue2` | Zahleneingabe | I | Umlaufdauer eines Protons — ohne v |
| `ue3` | Zahleneingabe | I / II | Geschwindigkeit aus gemessenem Bahnradius |
| `zuordnung` | Zuordnung | II | vier Bahnbilder zu vier Versuchsbedingungen |
| `ue5` | Zahleneingabe | II | spezifische Ladung q/m im Fadenstrahlrohr |
| `ue6` | Zahleneingabe | II | Wien-Filter auslegen |
| `ue7` | Zahleneingabe | II | Neon-20 gegen Neon-22: Abstand der Auftreffpunkte |
| `ue8` | offen | III | Beurteilung: Trennt der Detektor die beiden Isotope? |
| `ue9` | offen | III | Bewertung einer Schüleraussage zur „Beschleunigung" |
| `ue10` | offen | III | Begründung: Warum hängt T nicht von v ab — und das Zyklotron |

---

### 5.1 ue1 — Bahnradius im Fadenstrahlrohr

`<div class="aufgabe" data-num="ue1">`, `<span class="ab">Anforderungsbereich I</span>`

**Aufgabentext:**

> In einem Fadenstrahlrohr werden Elektronen durch die Spannung **U = 1,00 kV** beschleunigt und
> treten dann senkrecht in ein Magnetfeld der Flussdichte **B = 3,00 mT** ein (⊗, in die
> Bildebene hinein).
>
> Berechne den **Radius r** der Kreisbahn.

**Eingabe:** `type="number"`, Einheitenliste in dieser Reihenfolge:
`Einheit…` (leer) · `mm` · `cm` · `m` · `m/s`
Die Einheit **m/s** ist der fachliche Distraktor — sie fängt die Verwechslung von Zwischen- und
Endergebnis ab, denn v ist der Wert, den man auf dem Weg dorthin ausrechnet.

**`numDaten`-Eintrag:**

```js
ue1:{ wert:3.55, einheit:"cm", tol:0.06,
      alt:{wert:35.5, einheit:"mm"},
      ok:"Richtig. v = √(2·e·U/m_e) = 1,876 · 10⁷ m/s, damit r = m_e·v/(e·B) = 3,55 cm. Das ist genau die Startstellung der Simulation — stell sie ein und miss den Kreis am Maßstabsbalken nach.",
      falschEinheit:"Der Zahlenwert stimmt, die Einheit nicht. r ist eine Länge. Wenn du m/s gewählt hast, hast du das Zwischenergebnis v abgegeben; wenn du dich zwischen mm, cm und m vertan hast, prüfe die Zehnerpotenz: 3,55 cm = 35,5 mm = 0,0355 m.",
      nah:"Größenordnung stimmt, der Wert nicht. Zwei Stellen, an denen es typischerweise klemmt: Steht unter der Wurzel wirklich 2·e·U/m_e und nicht e·U/m_e? Und hast du B in Tesla eingesetzt, also 3,00 mT = 3,00 · 10⁻³ T?",
      weit:"Das liegt um mehr als den Faktor zwei daneben — da ist eine Zehnerpotenz verrutscht. Häufigste Ursache: mT nicht in T umgerechnet (Faktor 1000) oder kV nicht in V (Faktor 1000). Rechne mit dem Ansatz aus Hilfe 2 noch einmal von vorn und schreibe jede Zahl mit ihrer Einheit auf." }
```

**Hilfe 1 (Tipp, eine Zeile, keine Formel):**

> Das ist keine Aufgabe, sondern zwei: Erst musst du wissen, wie schnell das Elektron ins Feld
> eintritt, und diese Information steckt in der Beschleunigungsspannung.

**Hilfe 2 (Ansatz, Formel und Weg, ohne Zahlen):**

> Schritt 1 — Energiesatz in der Beschleunigungsstrecke: die gesamte Arbeit des elektrischen
> Feldes wird kinetische Energie, also |q|·U = ½·m·v², daraus
> - `data-tex`: `v = \sqrt{\dfrac{2 \cdot |q| \cdot U}{m}}`
> - `data-plain`: `v = √(2 · |q| · U / m)`
>
> Schritt 2 — im Magnetfeld ist die Lorentzkraft die Zentripetalkraft, also |q|·v·B = m·v²/r und
> damit
> - `data-tex`: `r = \dfrac{m \cdot v}{|q| \cdot B}`
> - `data-plain`: `r = m · v / (|q| · B)`
>
> Für das Elektron ist |q| = e und m = m_e. Rechne U und B vorher in Volt und Tesla um.

**Hilfe 3 (Lösungsweg, vollständig):**

> **Gegeben:** U = 1,00 kV = 1000 V · B = 3,00 mT = 3,00 · 10⁻³ T ·
> e = 1,602 · 10⁻¹⁹ C · m_e = 9,109 · 10⁻³¹ kg
>
> **Schritt 1 — Eintrittsgeschwindigkeit.**
> - `data-tex`: `v = \sqrt{\dfrac{2 \cdot 1{,}602 \cdot 10^{-19}\,\mathrm{C} \cdot 1000\,\mathrm{V}}{9{,}109 \cdot 10^{-31}\,\mathrm{kg}}} = 1{,}876 \cdot 10^{7}\,\dfrac{\mathrm{m}}{\mathrm{s}}`
> - `data-plain`: `v = √(2 · 1,602·10⁻¹⁹ C · 1000 V / 9,109·10⁻³¹ kg) = 1,876 · 10⁷ m/s`
>
> Einheitenprobe: C·V/kg = J/kg = m²/s², die Wurzel daraus ist m/s. ✓
>
> **Schritt 2 — Bahnradius.**
> - `data-tex`: `r = \dfrac{9{,}109 \cdot 10^{-31}\,\mathrm{kg} \cdot 1{,}876 \cdot 10^{7}\,\frac{\mathrm{m}}{\mathrm{s}}}{1{,}602 \cdot 10^{-19}\,\mathrm{C} \cdot 3{,}00 \cdot 10^{-3}\,\mathrm{T}} = 3{,}554 \cdot 10^{-2}\,\mathrm{m}`
> - `data-plain`: `r = (9,109·10⁻³¹ kg · 1,876·10⁷ m/s) / (1,602·10⁻¹⁹ C · 3,00·10⁻³ T) = 3,554 · 10⁻² m`
>
> Einheitenprobe: kg·m/s pro (C·T) = kg·m/s pro (kg/s) = m. ✓
>
> **Ergebnis: r = 3,55 cm**, der Kreisdurchmesser also 7,11 cm.
>
> **Abkürzung für später.** Setzt man Schritt 1 in Schritt 2 ein, fällt v heraus:
> - `data-tex`: `r = \dfrac{1}{B}\sqrt{\dfrac{2 \cdot m \cdot U}{|q|}}`
> - `data-plain`: `r = (1/B) · √(2 · m · U / |q|)`
>
> Damit kommst du in einem Schritt auf dieselben 3,554 cm. Diese Form brauchst du in ue5 wieder.

---

### 5.2 ue2 — Umlaufdauer ohne Umweg

`<div class="aufgabe" data-num="ue2">`, `<span class="ab">Anforderungsbereich I</span>`

**Aufgabentext:**

> Ein **Proton** läuft in einem Magnetfeld der Flussdichte **B = 130 mT** auf einer Kreisbahn.
> Über die Beschleunigungsspannung ist nichts bekannt — sie wurde nicht protokolliert.
>
> Berechne die **Umlaufdauer T**. Begründe in der Rückmeldung für dich selbst, warum die fehlende
> Spannung kein Hindernis ist.

**Eingabe:** Einheitenliste `Einheit…` · `ns` · `µs` · `ms` · `MHz`
**MHz** ist der Distraktor: Wer 1/T statt T abgibt, landet bei der Zyklotronfrequenz.

**`numDaten`-Eintrag:**

```js
ue2:{ wert:504.6, einheit:"ns", tol:6,
      alt:{wert:0.5046, einheit:"µs"},
      ok:"Richtig. T = 2·π·m_p/(e·B) = 504,6 ns. Beachte, was du nicht gebraucht hast: weder U noch v noch r. Die Umlaufdauer hängt allein von m, |q| und B ab — deshalb konnte die Spannung fehlen.",
      falschEinheit:"Zahlenwert und Größenordnung passen, die Einheit nicht. T ist eine Zeit. MHz ist eine Frequenz — du hast vermutlich 1/T angegeben, das wäre die Zyklotronfrequenz f_c = 1,98 MHz. Zwischen ns, µs und ms liegen jeweils drei Zehnerpotenzen: 504,6 ns = 0,5046 µs = 5,046 · 10⁻⁴ ms.",
      nah:"Der Wert liegt in der richtigen Größenordnung, stimmt aber nicht. Prüfe zwei Dinge: Steht im Zähler 2·π·m und nicht π·m (der Faktor 2 kommt aus dem vollen Umfang, nicht aus dem Halbkreis)? Und hast du die Protonenmasse 1,673 · 10⁻²⁷ kg benutzt und nicht versehentlich die Elektronenmasse?",
      weit:"Mehr als Faktor zwei daneben. Wenn dein Wert rund 1836-mal kleiner ist, hast du mit der Elektronenmasse gerechnet. Wenn er um den Faktor 1000 danebenliegt, steckt B noch in Millitesla in der Formel: 130 mT = 0,130 T. Öffne Hilfe 2 und setze noch einmal sauber ein." }
```

**Hilfe 1 (Tipp):**

> Schau dir an, welche Größen in der Formel für T überhaupt vorkommen — und welche eben nicht.

**Hilfe 2 (Ansatz):**

> Die Umlaufdauer ist Umfang durch Geschwindigkeit, T = 2πr/v. Setzt du darin r = m·v/(|q|·B)
> ein, kürzt sich v vollständig heraus:
> - `data-tex`: `T = \dfrac{2\pi r}{v} = \dfrac{2\pi}{v} \cdot \dfrac{m \cdot v}{|q| \cdot B} = \dfrac{2\pi \cdot m}{|q| \cdot B}`
> - `data-plain`: `T = 2πr/v = (2π/v) · m·v/(|q|·B) = 2 · π · m / (|q| · B)`
>
> Für das Proton ist |q| = e und m = m_p. Die Beschleunigungsspannung wird nicht gebraucht.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** B = 130 mT = 0,130 T · m_p = 1,673 · 10⁻²⁷ kg · e = 1,602 · 10⁻¹⁹ C
>
> - `data-tex`: `T = \dfrac{2\pi \cdot 1{,}673 \cdot 10^{-27}\,\mathrm{kg}}{1{,}602 \cdot 10^{-19}\,\mathrm{C} \cdot 0{,}130\,\mathrm{T}} = \dfrac{1{,}0510 \cdot 10^{-26}}{2{,}0828 \cdot 10^{-20}}\,\mathrm{s} = 5{,}046 \cdot 10^{-7}\,\mathrm{s}`
> - `data-plain`: `T = 2π · 1,673·10⁻²⁷ kg / (1,602·10⁻¹⁹ C · 0,130 T) = 1,0510·10⁻²⁶ / 2,0828·10⁻²⁰ s = 5,046 · 10⁻⁷ s`
>
> Einheitenprobe: kg/(C·T) = kg/(kg/s) = s. ✓
>
> **Ergebnis: T = 5,046 · 10⁻⁷ s = 504,6 ns = 0,5046 µs.**
> Die zugehörige Zyklotronfrequenz ist f_c = 1/T = 1,982 MHz.
>
> **Gegenprobe über den Umweg** — zweimal derselbe Wert bei völlig verschiedener Spannung:
>
> | U | v | r | T = 2πr/v |
> |---|---|---|---|
> | 1000 V | 4,377 · 10⁵ m/s | 3,515 cm | 5,046 · 10⁻⁷ s |
> | 200 V | 1,957 · 10⁵ m/s | 1,572 cm | 5,046 · 10⁻⁷ s |
>
> Die Bahn ist bei 200 V weniger als halb so groß — und die Umlaufdauer stimmt bis auf die
> letzte angegebene Stelle überein. Genau das war der Grund, warum U fehlen durfte.

---

### 5.3 ue3 — Rückwärts: aus der Bahn auf die Geschwindigkeit

`<div class="aufgabe" data-num="ue3">`, `<span class="ab">Anforderungsbereich I</span>` — der Bauagent
setzt hier zusätzlich den Hinweis `(mit Auswertungsschritt)` hinter die Bereichsangabe, weil die
Aufgabe eine Formel umstellen verlangt und damit am oberen Rand von AB I liegt.

**Aufgabentext:**

> Im Fadenstrahlrohr misst du mit dem Spiegelmaßstab den **Durchmesser** des leuchtenden Kreises
> zu **2r = 8,40 cm**. Das Helmholtz-Spulenpaar erzeugt **B = 1,80 mT**. Das Netzgerät für die
> Beschleunigungsspannung ist defekt und zeigt nichts an.
>
> Berechne die **Geschwindigkeit v** der Elektronen aus diesen beiden Messwerten.

**Eingabe:** Einheitenliste `Einheit…` · `km/s` · `m/s` · `cm/s` · `m/s²`
**m/s²** ist der Distraktor: Verwechslung von Geschwindigkeit und Beschleunigung, die auf der
Kreisbahn ja beide auftreten.

**`numDaten`-Eintrag:**

```js
ue3:{ wert:13297, einheit:"km/s", tol:200,
      alt:{wert:1.3297e7, einheit:"m/s"},
      ok:"Richtig. v = e·B·r/m_e = 1,330 · 10⁷ m/s = 13 297 km/s, also rund 4,4 % der Lichtgeschwindigkeit. Aus v lässt sich die defekte Anzeige sogar rekonstruieren: U = m_e·v²/(2e) = 503 V.",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. v ist eine Geschwindigkeit, also Länge pro Zeit. m/s² wäre eine Beschleunigung — auf der Kreisbahn gibt es die zwar auch (die Zentripetalbeschleunigung), gefragt war sie aber nicht. Umrechnung: 13 297 km/s = 1,3297 · 10⁷ m/s.",
      nah:"Nah dran, aber nicht richtig — und die häufigste Ursache steht in der Aufgabe: Gemessen wurde der Durchmesser, in die Formel gehört der Radius. Mit 2r statt r bekommst du genau den doppelten Wert (26 593 km/s). Prüfe auch, ob B in Tesla eingesetzt ist.",
      weit:"Das ist um mehr als Faktor zwei daneben. Stell die Formel r = m·v/(|q|·B) sauber nach v um, bevor du Zahlen einsetzt: v = |q|·B·r/m. Wer stattdessen dividiert, wo multipliziert gehört, landet um viele Zehnerpotenzen daneben. Hilfe 3 zeigt jeden Schritt." }
```

**Hilfe 1 (Tipp):**

> Zwei Fallen in einem Satz: Der Maßstab misst den Durchmesser, nicht den Radius — und die
> Beschleunigungsspannung brauchst du für diesen Weg überhaupt nicht.

**Hilfe 2 (Ansatz):**

> Ausgangspunkt ist wieder die Kreisbahnbedingung |q|·v·B = m·v²/r, also r = m·v/(|q|·B).
> Stelle sie nach v um:
> - `data-tex`: `v = \dfrac{|q| \cdot B \cdot r}{m}`
> - `data-plain`: `v = |q| · B · r / m`
>
> Halbiere vorher den gemessenen Durchmesser zu r = 4,20 cm und rechne B in Tesla um. Für das
> Elektron ist |q| = e und m = m_e.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** 2r = 8,40 cm ⟹ r = 4,20 cm = 4,20 · 10⁻² m · B = 1,80 mT = 1,80 · 10⁻³ T ·
> e = 1,602 · 10⁻¹⁹ C · m_e = 9,109 · 10⁻³¹ kg
>
> - `data-tex`: `v = \dfrac{1{,}602 \cdot 10^{-19}\,\mathrm{C} \cdot 1{,}80 \cdot 10^{-3}\,\mathrm{T} \cdot 4{,}20 \cdot 10^{-2}\,\mathrm{m}}{9{,}109 \cdot 10^{-31}\,\mathrm{kg}} = \dfrac{1{,}2112 \cdot 10^{-23}}{9{,}109 \cdot 10^{-31}}\,\dfrac{\mathrm{m}}{\mathrm{s}}`
> - `data-plain`: `v = (1,602·10⁻¹⁹ C · 1,80·10⁻³ T · 4,20·10⁻² m) / 9,109·10⁻³¹ kg = 1,2112·10⁻²³ / 9,109·10⁻³¹ m/s`
>
> **Ergebnis: v = 1,330 · 10⁷ m/s = 13 297 km/s.**
>
> Einheitenprobe: C·T·m/kg = C · (kg/(C·s)) · m/kg = m/s. ✓
>
> **Zwei Proben, die sich lohnen:**
> 1. v/c = 1,330 · 10⁷ / 3,00 · 10⁸ = **4,4 %** — klassisch rechnen ist zulässig.
> 2. Rückrechnung auf die defekte Anzeige: U = m_e·v²/(2e) = 9,109 · 10⁻³¹ · (1,330 · 10⁷)² /
>    (2 · 1,602 · 10⁻¹⁹) V = **503 V**. Setzt man diese Spannung wieder in ue1s Formel
>    r = (1/B)·√(2·m·U/|q|) ein, kommt exakt 4,20 cm heraus — der Kreis schließt sich.

---

### 5.4 zuordnung — Vier Bahnen, vier Bedingungen

Die **einzige** Zuordnungsaufgabe des Moduls (`bausteine.md`, Abschnitt 6: pro Modul ist genau
eine vorgesehen). Schlüssel `zuordnung`, `<span class="ab">Anforderungsbereich II</span>`.

**Aufgabentext über den Diagrammen:**

> Vier Aufnahmen aus derselben Versuchsanordnung. Jedes Mal tritt das Teilchen am **linken Rand
> in Bildmitte** ein und fliegt zunächst **nach rechts**; eingezeichnet ist der Anfang seiner
> Bahn. Teilchenmasse und Ladungsbetrag sind in allen vier Fällen dieselben — es handelt sich
> um Elektronen beziehungsweise um deren Antiteilchen, das Positron.
>
> Als **Bezugsfall** gilt: Elektron, Beschleunigungsspannung U₀, Flussdichte B₀ (⊗), daraus
> ergibt sich der Bahnradius R. Ordne jeder Bedingung ihr Bahnbild zu.

#### Die vier Diagramme (Inline-SVG, `<div class="diagramme">`)

Alle vier SVG sind **gleich aufgebaut**, damit nur die zwei gemeinten Unterschiede ins Auge
fallen. Verbindliche Vorgaben für jedes Einzelbild:

- `viewBox="0 0 260 220"`, `width:100%`, Rahmen `#cbd5e1`, Hintergrund weiß.
- Buchstabe **A**, **B**, **C** oder **D** oben links, `font-weight:700`, Farbe `#0f172a`.
- Eintrittspunkt **P = (30; 110)**, davor ein kurzer waagerechter Pfeil nach rechts
  (von (10;110) nach (28;110)) mit der Beschriftung `v` in `#0f172a`.
- Feldsymbole als **3 × 3-Raster** über die Fläche verteilt, Farbe `#64748b`:
  in A, B und C sind es **⊗** (Kreis mit Kreuz), in **D** sind es **⊙** (Kreis mit Punkt).
  Unter dem Raster steht in jedem Bild klein die Angabe `B ⊗` bzw. `B ⊙`.
- Die Bahn ist ein **Kreisbogen von 120°**, der in P tangential nach rechts startet,
  gezeichnet als `<path>` mit `stroke="#1d4ed8"`, `stroke-width="2.5"`, `fill="none"`.
  Am Ende des Bogens ein kleiner gefüllter Kreis (r = 4) in derselben Farbe.
- **Kein** Zahlenwert, **keine** Radiusbemaßung im Bild. Der Größenvergleich soll aus dem Bild
  abgelesen werden, nicht aus einer Beschriftung.

| Bild | Krümmung ab P | Bahnradius im Bild | Feldsymbole |
|---|---|---|---|
| **A** | nach **oben** (Mittelpunkt über P), Umlauf **gegen** den Uhrzeigersinn | 60 px | ⊗ |
| **B** | nach **unten** (Mittelpunkt unter P), Umlauf **im** Uhrzeigersinn | 60 px | ⊗ |
| **C** | nach **unten**, Umlauf **im** Uhrzeigersinn | **120 px** (doppelt) | ⊗ |
| **D** | nach **oben**, Umlauf **gegen** den Uhrzeigersinn | **30 px** (halb) | ⊗ |

Damit unterscheiden sich A und B **nur** im Drehsinn, B und C **nur** im Radius, A und D **nur**
im Radius. Das ist Absicht: Wer nur auf „groß oder klein" achtet, verwechselt A mit B; wer nur
auf den Drehsinn achtet, verwechselt B mit C.

*Hinweis an den Bauagenten:* Bild C mit r = 120 px passt bei einem 120°-Bogen ab (30;110) noch
vollständig in die Fläche 260 × 220 (tiefster Punkt der Bahn y ≈ 194). Prüfe das beim Zeichnen
nach; falls du den Bogen kürzen musst, kürze ihn auf 90°, aber ändere **nicht** den Radius —
er trägt die Aussage.

#### Die vier Zeilen (`<div class="zuordnung">`)

Die Reihenfolge der Situationen ist bewusst **nicht** A, B, C, D (Vorgabe aus `bausteine.md`).
Die Lösungsfolge lautet **B – C – D – A**.

| Reihenfolge im Markup | Situationsbeschreibung (`<span>`) | `data-loesung` |
|---|---|---|
| 1 | **Elektron**, Spannung U₀, Flussdichte B₀, Feld ⊗ *(der Bezugsfall)* | `B` |
| 2 | **Elektron**, Spannung **4·U₀**, Flussdichte B₀, Feld ⊗ | `C` |
| 3 | **Positron**, Spannung U₀, Flussdichte **2·B₀**, Feld ⊗ | `D` |
| 4 | **Elektron**, Spannung U₀, Flussdichte B₀, Feld **⊙** (aus der Bildebene heraus) | `A` |

Jede Zeile bekommt ein `<select>` mit den Optionen `…` (leer), `A`, `B`, `C`, `D`.

#### Begründung jeder Zuordnung (gehört in die Rückmeldung bei vollständiger Lösung)

> **Zeile 1 → B.** Bezugsfall. Das Elektron ist negativ; nach der Konvention aus Abschnitt 0.5
> zeigt der Daumen der rechten Hand entgegen der Flugrichtung, also nach links, der Zeigefinger
> ins Bild — die Kraft weist **nach unten**. Also Krümmung nach unten, Umlauf im Uhrzeigersinn,
> Radius R. Das ist Bild B.
>
> **Zeile 2 → C.** Vervierfachte Spannung: Wegen v = √(2·|q|·U/m) ist v ∝ √U, die Geschwindigkeit
> **verdoppelt** sich. Wegen r = m·v/(|q|·B) ist r ∝ v, also **verdoppelt sich auch der Radius**.
> Am Vorzeichen der Ladung und an der Feldrichtung hat sich nichts geändert, der Drehsinn bleibt
> im Uhrzeigersinn. Das ist Bild C — dieselbe Drehrichtung wie B, doppelter Radius.
>
> **Zeile 3 → D.** Zwei Änderungen auf einmal. Erstens: Das Positron ist **positiv**, damit dreht
> sich die Kraftrichtung gegenüber dem Elektron um 180° — Krümmung nach oben, Umlauf gegen den
> Uhrzeigersinn. Zweitens: verdoppeltes B bei unveränderter Spannung. Da v allein von U abhängt,
> bleibt v gleich, und wegen r ∝ 1/B **halbiert** sich der Radius. Das ist Bild D.
>
> **Zeile 4 → A.** Nur die Feldrichtung ist umgekehrt (⊙ statt ⊗). Das dreht die Lorentzkraft um
> 180°, genau wie es ein Vorzeichenwechsel der Ladung täte: Krümmung nach oben, Umlauf gegen den
> Uhrzeigersinn. Beträge von v und B sind unverändert, also bleibt der Radius R. Das ist Bild A.
>
> **Was du an diesem Vierer siehst:** Über den **Drehsinn** entscheiden nur zwei Dinge — das
> Vorzeichen der Ladung und die Richtung von B⃗. Kehrst du **beide** um, ändert sich gar nichts.
> Über den **Radius** entscheiden nur die Beträge: r ∝ √U und r ∝ 1/B. Die Umlaufdauer übrigens
> unterscheidet sich nur in Zeile 3 — dort ist sie halb so groß, in allen anderen Zeilen gleich.

**Rückmeldung bei Teilerfolg** (nennt die Strategie, nicht die Lösung):

> Ein Teil sitzt. Geh die restlichen Zeilen in zwei getrennten Durchgängen an, statt beides
> gleichzeitig zu entscheiden:
>
> 1. **Erst der Drehsinn.** Frage nur: Zeigt die Kraft im Eintrittspunkt nach oben oder nach
>    unten? Dafür brauchst du zwei Angaben — das Vorzeichen der Ladung und die Richtung von B⃗.
>    Das halbiert die Auswahl auf zwei Bilder.
> 2. **Dann der Radius.** Frage nur: größer, gleich oder kleiner als im Bezugsfall? Denk daran,
>    dass die Spannung über v wirkt (r ∝ √U), das Feld dagegen direkt (r ∝ 1/B). Damit ist die
>    Entscheidung eindeutig.
>
> Und die Kontrollfrage, wenn du unsicher bist: Zwei Zeilen unterscheiden sich vom Bezugsfall nur
> durch eine einzige Umkehrung. Welche sind das — und führen sie zum selben Bild oder zu
> verschiedenen?

---

### 5.5 ue5 — Die spezifische Ladung des Elektrons messen

`<div class="aufgabe" data-num="ue5">`, `<span class="ab">Anforderungsbereich II</span>`

**Aufgabentext:**

> Der klassische Fadenstrahlrohr-Versuch. Du protokollierst:
>
> | Größe | Messwert |
> |---|---|
> | Beschleunigungsspannung U | 250 V |
> | Flussdichte des Spulenpaares B | 1,60 mT |
> | Durchmesser des Elektronenkreises 2r | 6,66 cm |
>
> Bestimme daraus die **spezifische Ladung** |q|/m des Elektrons. Die Elektronenmasse ist dir
> dabei **nicht** gegeben — und du brauchst sie auch nicht.
>
> *Eingabehinweis: Schreib den Wert wissenschaftlich, zum Beispiel `1.76e11`.*

**Eingabe:** Einheitenliste `Einheit…` · `C/kg` · `kg/C` · `C` · `N/kg`
`kg/C` fängt den Kehrwert ab, `C` die Verwechslung mit der Ladung selbst, `N/kg` die
Verwechslung mit einer Feldstärke.

**`numDaten`-Eintrag:**

```js
ue5:{ wert:1.761e11, einheit:"C/kg", tol:4e9,
      ok:"Richtig. |q|/m = 2·U/(r²·B²) = 1,761 · 10¹¹ C/kg. Der Literaturwert für das Elektron ist 1,7588 · 10¹¹ C/kg — deine Messung liegt 0,14 % daneben, das ist für einen Schulversuch ausgezeichnet. Beachte, was du gemessen hast: nicht die Ladung und nicht die Masse, sondern ausschließlich ihr Verhältnis.",
      falschEinheit:"Der Zahlenwert stimmt, die Einheit nicht. Gesucht war eine Ladung pro Masse, also C/kg. kg/C wäre der Kehrwert (dann müsste der Zahlenwert 5,68 · 10⁻¹² lauten), C allein wäre eine Ladung, N/kg eine Feldstärke beziehungsweise Beschleunigung.",
      nah:"Größenordnung richtig, Wert nicht. Die mit Abstand häufigste Ursache: Gemessen wurde der Durchmesser 6,66 cm, in die Formel gehört der Radius 3,33 cm. Mit r = 6,66 cm bekommst du ein Viertel des richtigen Werts, weil r quadratisch eingeht. Prüfe außerdem den Faktor 2 im Zähler — er stammt aus |q|·U = ½·m·v².",
      weit:"Um mehr als Faktor zwei daneben, meist eine Zehnerpotenz. Setze konsequent in SI-Einheiten ein: U in Volt, r in Metern (3,33 cm = 0,0333 m), B in Tesla (1,60 mT = 1,60 · 10⁻³ T). Wenn dein Ergebnis bei rund 10⁷ statt 10¹¹ liegt, steckt der Radius noch in Zentimetern. Hilfe 3 zeigt jeden Zwischenwert." }
```

**Hilfe 1 (Tipp):**

> Du kennst zwei Gleichungen, in denen |q| und m vorkommen — die eine für die Beschleunigung, die
> andere für die Kreisbahn. Kombiniere sie so, dass beide Größen nur noch als Quotient auftreten.

**Hilfe 2 (Ansatz):**

> Aus dem Energiesatz folgt v = √(2·|q|·U/m), aus der Kreisbahnbedingung r = m·v/(|q|·B).
> Setze das eine ins andere ein; das liefert die schon in ue1 benutzte Form
> - `data-tex`: `r = \dfrac{1}{B}\sqrt{\dfrac{2 \cdot m \cdot U}{|q|}}`
> - `data-plain`: `r = (1/B) · √(2 · m · U / |q|)`
>
> Quadriere und stelle nach |q|/m um:
> - `data-tex`: `\dfrac{|q|}{m} = \dfrac{2 \cdot U}{r^{2} \cdot B^{2}}`
> - `data-plain`: `|q| / m = 2 · U / (r² · B²)`
>
> Rechts steht nur Messbares. Halbiere vorher den Durchmesser.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** U = 250 V · B = 1,60 mT = 1,60 · 10⁻³ T · 2r = 6,66 cm ⟹ r = 3,33 cm = 0,0333 m
>
> **Zwischenwerte:**
> - r² = (0,0333 m)² = 1,1089 · 10⁻³ m²
> - B² = (1,60 · 10⁻³ T)² = 2,560 · 10⁻⁶ T²
> - r²·B² = 2,8388 · 10⁻⁹ m²·T²
>
> **Einsetzen:**
> - `data-tex`: `\dfrac{|q|}{m} = \dfrac{2 \cdot 250\,\mathrm{V}}{2{,}8388 \cdot 10^{-9}\,\mathrm{m^2 T^2}} = \dfrac{500}{2{,}8388 \cdot 10^{-9}}\,\dfrac{\mathrm{C}}{\mathrm{kg}} = 1{,}761 \cdot 10^{11}\,\dfrac{\mathrm{C}}{\mathrm{kg}}`
> - `data-plain`: `|q|/m = 2 · 250 V / (2,8388·10⁻⁹ m²T²) = 500 / 2,8388·10⁻⁹ C/kg = 1,761 · 10¹¹ C/kg`
>
> Einheitenprobe: V/(m²·T²) = V/(m² · (V·s/m²)²) = m²/(V·s²) … kürzer über
> V·s²/m² = kg/C ⟹ der Kehrwert davon ist C/kg. ✓
>
> **Ergebnis: |q|/m = 1,761 · 10¹¹ C/kg.**
>
> **Bewertung der Messung.** Der Literaturwert ist e/m_e = 1,7588 · 10¹¹ C/kg; die Abweichung
> beträgt **+0,14 %**. Das ist bemerkenswert gut, hat aber eine Ursache, die man kennen muss:
> Der Radius geht **quadratisch** ein. Ein Ablesefehler von 1 mm beim Durchmesser (also 0,5 mm
> beim Radius, das sind 1,5 %) verschiebt das Ergebnis bereits um rund 3 %. Die
> Beschleunigungsspannung dagegen geht nur linear ein und ist am Netzgerät ohnehin genauer
> abzulesen. **Wer diesen Versuch verbessern will, verbessert die Radiusmessung.**
>
> **Und was man daraus nicht bekommt** (Merksatz 6 aus Abschnitt 3.5): weder e noch m_e einzeln.
> Erst der Millikan-Versuch liefert e unabhängig; zusammen mit dieser Messung folgt daraus
> m_e = e / (|q|/m) = 1,602 · 10⁻¹⁹ C / 1,761 · 10¹¹ C/kg = 9,10 · 10⁻³¹ kg.

---

### 5.6 ue6 — Einen Wien-Filter auslegen

`<div class="aufgabe" data-num="ue6">`, `<span class="ab">Anforderungsbereich II</span>`

**Aufgabentext:**

> Du sollst einen Geschwindigkeitsfilter so einstellen, dass er **Protonen** durchlässt, die
> zuvor mit **U = 450 V** beschleunigt wurden. Die Anordnung entspricht der Simulation:
> Plattenkondensator mit dem Plattenabstand **d = 2,00 cm**, darin ein Magnetfeld der
> Flussdichte **B = 200 mT** senkrecht zur Zeichenebene und senkrecht zur Flugrichtung.
>
> Berechne die **elektrische Feldstärke E**, die dafür zwischen den Platten herrschen muss.
>
> *(Die Plattenspannung, die du dafür einstellen musst, findest du im Lösungsweg — mit ihr kannst
> du das Ergebnis anschließend in der Simulation nachstellen.)*

**Eingabe:** Einheitenliste `Einheit…` · `kV/m` · `V/m` · `V` · `T`
`V` fängt die Verwechslung von Feldstärke und Spannung ab, `T` die Verwechslung der beiden
Felder.

**`numDaten`-Eintrag:**

```js
ue6:{ wert:58.7, einheit:"kV/m", tol:0.8,
      alt:{wert:58723, einheit:"V/m"},
      ok:"Richtig. v = √(2·e·U/m_p) = 2,936 · 10⁵ m/s, daraus E = v·B = 58,7 kV/m. Die zugehörige Plattenspannung ist U_P = E·d = 1174 V — stell das in der Simulation ein, das Proton geht durch die Blende.",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. E ist eine Feldstärke, also Spannung pro Länge: V/m oder kV/m. V allein wäre die Plattenspannung (die beträgt hier 1174 V), T wäre eine magnetische Flussdichte. Umrechnung: 58,7 kV/m = 58 700 V/m.",
      nah:"Der Ansatz E = v·B stimmt offenbar, aber v nicht ganz. Prüfe: Steht unter der Wurzel 2·e·U/m_p? Hast du die Protonenmasse benutzt (1,673 · 10⁻²⁷ kg) und nicht die Elektronenmasse? Mit m_e käme v um den Faktor 43 zu groß heraus.",
      weit:"Mehr als Faktor zwei daneben. Zwei typische Fehler: Erstens die Bedingung falsch herum — für das Kräftegleichgewicht gilt E = v·B, nicht E = v/B oder E = B/v. Zweitens die Einheiten: B muss in Tesla stehen (200 mT = 0,200 T) und U in Volt. Öffne Hilfe 2 und arbeite die zwei Schritte getrennt ab." }
```

**Hilfe 1 (Tipp):**

> Der Filter lässt genau die Teilchen geradeaus durch, bei denen sich die beiden Kräfte
> gegenseitig aufheben. Schreib zuerst hin, wie groß die beiden Kräfte einzeln sind.

**Hilfe 2 (Ansatz):**

> Im Filter wirken auf das Teilchen zwei Kräfte in entgegengesetzter Richtung: die elektrische
> Kraft F_el = |q|·E und die Lorentzkraft F_L = |q|·v·B. Geradeaus fliegt es, wenn beide gleich
> groß sind:
> - `data-tex`: `|q| \cdot E = |q| \cdot v \cdot B \quad \Longrightarrow \quad E = v \cdot B`
> - `data-plain`: `|q| · E = |q| · v · B   ⟹   E = v · B`
>
> Die Ladung kürzt sich heraus — deshalb hängt die Durchlassbedingung weder von |q| noch von m ab.
> Die Geschwindigkeit v holst du dir wie in ue1 aus der Beschleunigungsspannung.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** U = 450 V · B = 200 mT = 0,200 T · d = 2,00 cm = 0,0200 m ·
> m_p = 1,673 · 10⁻²⁷ kg · e = 1,602 · 10⁻¹⁹ C
>
> **Schritt 1 — Eintrittsgeschwindigkeit des Protons.**
> - `data-tex`: `v = \sqrt{\dfrac{2 \cdot 1{,}602 \cdot 10^{-19}\,\mathrm{C} \cdot 450\,\mathrm{V}}{1{,}673 \cdot 10^{-27}\,\mathrm{kg}}} = 2{,}936 \cdot 10^{5}\,\dfrac{\mathrm{m}}{\mathrm{s}}`
> - `data-plain`: `v = √(2 · 1,602·10⁻¹⁹ C · 450 V / 1,673·10⁻²⁷ kg) = 2,936 · 10⁵ m/s = 293,6 km/s`
>
> **Schritt 2 — Kräftegleichgewicht.**
> - `data-tex`: `E = v \cdot B = 2{,}936 \cdot 10^{5}\,\dfrac{\mathrm{m}}{\mathrm{s}} \cdot 0{,}200\,\mathrm{T} = 5{,}872 \cdot 10^{4}\,\dfrac{\mathrm{V}}{\mathrm{m}}`
> - `data-plain`: `E = v · B = 2,936·10⁵ m/s · 0,200 T = 5,872 · 10⁴ V/m`
>
> Einheitenprobe: (m/s)·T = (m/s)·(V·s/m²) = V/m. ✓
>
> **Ergebnis: E = 5,87 · 10⁴ V/m = 58,7 kV/m.**
>
> **Schritt 3 — die Größe, die du am Netzgerät einstellst.** Im Plattenkondensator ist das Feld
> homogen, also E = U_P/d und damit
> - `data-tex`: `U_P = E \cdot d = 5{,}872 \cdot 10^{4}\,\dfrac{\mathrm{V}}{\mathrm{m}} \cdot 0{,}0200\,\mathrm{m} = 1174\,\mathrm{V}`
> - `data-plain`: `U_P = E · d = 5,872·10⁴ V/m · 0,0200 m = 1174 V`
>
> **Probe am Zahlenwert der Kräfte:**
> F_el = e·E = 1,602 · 10⁻¹⁹ C · 5,872 · 10⁴ V/m = 9,408 · 10⁻¹⁵ N und
> F_L = e·v·B = 1,602 · 10⁻¹⁹ C · 2,936 · 10⁵ m/s · 0,200 T = 9,408 · 10⁻¹⁵ N. Gleich. ✓
>
> **Was daran das Bemerkenswerte ist.** In deinem Ergebnis kommt weder die Protonenmasse noch die
> Protonenladung vor — sie wurden nur gebraucht, um v zu bestimmen. Der Filter selbst kennt nur
> eine Eigenschaft des Teilchens: seine Geschwindigkeit. Ein **Alphateilchen** mit derselben
> Geschwindigkeit (das wäre bei U = 890 V der Fall, denn es hat die doppelte Ladung und die
> vierfache Masse) geht bei genau derselben Einstellung ebenfalls durch — obwohl es viermal so
> schwer ist und die vierfache kinetische Energie mitbringt.

---

### 5.7 ue7 — Neon-20 gegen Neon-22: Wie weit liegen die Spuren auseinander?

`<div class="aufgabe" data-num="ue7">`, `<span class="ab">Anforderungsbereich II</span>`

Diese Aufgabe und ue8 bilden ein Paar: hier wird gerechnet, dort beurteilt. Der Bauagent setzt
sie unmittelbar untereinander und gibt ue8 die Überschrift *Fortsetzung von Aufgabe 7*.

**Aufgabentext:**

> Natürliches Neon besteht fast ausschließlich aus den Isotopen **Ne-20** und **Ne-22**. Beide
> werden in der Ionenquelle **einfach positiv** geladen (q = +e) und mit **U = 2,00 kV**
> beschleunigt. Danach treten sie durch einen Spalt in eine Kammer mit **B = 600 mT** ein und
> laufen dort einen **Halbkreis**, bis sie auf den Detektor treffen, der in derselben Ebene wie
> der Eintrittsspalt liegt.
>
> Rechne mit den Massen 20,0 u und 22,0 u (u = 1,6605 · 10⁻²⁷ kg).
>
> Berechne den **Abstand der beiden Auftreffpunkte** auf dem Detektor.

**Eingabe:** Einheitenliste `Einheit…` · `mm` · `cm` · `m` · `mm²`
`mm²` fängt ab, wer eine Fläche statt einer Strecke abgibt — die Ortsauflösung eines Detektors
wird gelegentlich fälschlich als Fläche gedacht.

**`numDaten`-Eintrag:**

```js
ue7:{ wert:4.68, einheit:"mm", tol:0.15,
      alt:{wert:0.468, einheit:"cm"},
      ok:"Richtig. r₂₀ = 4,799 cm, r₂₂ = 5,033 cm, Radiendifferenz Δr = 2,342 mm — und weil beide einen Halbkreis laufen, ist der Abstand der Auftreffpunkte das Doppelte: 2·Δr = 4,68 mm. Halte den Vergleich fest: 10 % Massenunterschied ergeben nur 4,9 % Radiusunterschied.",
      falschEinheit:"Der Zahlenwert stimmt, die Einheit nicht. Gefragt war ein Abstand, also eine Länge: 4,68 mm = 0,468 cm = 4,68 · 10⁻³ m. mm² wäre eine Fläche.",
      nah:"Du bist nah dran — vermutlich fehlt der Faktor 2. Δr = r₂₂ − r₂₀ = 2,34 mm ist der Unterschied der Radien; der Detektor liegt aber nach einem Halbkreis, und dort ist der Abstand vom Eintrittsspalt jeweils der Durchmesser 2r. Der gemessene Abstand ist deshalb 2·Δr. Zweite mögliche Ursache, wenn du bei rund 4,0 mm gelandet bist: zu früh gerundet. Aus 4,8 cm und 5,0 cm wird eine Differenz von 0,2 cm — bei einer Differenz zweier fast gleich großer Zahlen musst du die Zwischenwerte mit vier Stellen mitführen.",
      weit:"Um mehr als Faktor zwei daneben. Der häufigste schwere Fehler: mit r ∝ m gerechnet statt mit r ∝ √m. Weil v = √(2eU/m) selbst von der Masse abhängt, ist r = m·v/(eB) = √(2mU/e)/B — die Masse steht also unter der Wurzel. Wer linear rechnet, kommt auf rund 9,6 mm, also gut das Doppelte. Hilfe 2 zeigt die Herleitung." }
```

**Hilfe 1 (Tipp):**

> Das schwerere Ion ist nicht nur träger, es ist auch langsamer — beide Effekte hängen an
> derselben Masse und wirken auf den Radius in dieselbe Richtung. Und: Der Detektor sieht nicht
> die Radien, sondern die Durchmesser.

**Hilfe 2 (Ansatz):**

> Setze v = √(2·|q|·U/m) in r = m·v/(|q|·B) ein; das ergibt die Form, in der die Masse nur noch
> einmal vorkommt:
> - `data-tex`: `r = \dfrac{1}{B}\sqrt{\dfrac{2 \cdot m \cdot U}{|q|}} \qquad \text{also} \qquad r \propto \sqrt{m}`
> - `data-plain`: `r = (1/B) · √(2 · m · U / |q|)   also   r ∝ √m`
>
> Berechne r₂₀ und r₂₂ getrennt. Nach dem Halbkreis liegt der Auftreffpunkt im Abstand 2r vom
> Eintrittsspalt, der gesuchte Abstand der beiden Punkte ist also
> - `data-tex`: `\Delta s = 2 r_{22} - 2 r_{20} = 2 \cdot \Delta r`
> - `data-plain`: `Δs = 2·r₂₂ − 2·r₂₀ = 2 · Δr`

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** U = 2,00 kV = 2000 V · B = 600 mT = 0,600 T · q = +e = 1,602 · 10⁻¹⁹ C ·
> u = 1,6605 · 10⁻²⁷ kg
>
> **Massen:**
> - m₂₀ = 20,0 · 1,6605 · 10⁻²⁷ kg = 3,3211 · 10⁻²⁶ kg
> - m₂₂ = 22,0 · 1,6605 · 10⁻²⁷ kg = 3,6532 · 10⁻²⁶ kg
>
> **Geschwindigkeiten** (v = √(2·e·U/m)):
> - v₂₀ = √(2 · 1,602 · 10⁻¹⁹ · 2000 / 3,3211 · 10⁻²⁶) m/s = 1,3891 · 10⁵ m/s = 138,9 km/s
> - v₂₂ = √(2 · 1,602 · 10⁻¹⁹ · 2000 / 3,6532 · 10⁻²⁶) m/s = 1,3245 · 10⁵ m/s = 132,4 km/s
>
> Das schwerere Ion ist um den Faktor √(20/22) = 0,9535 langsamer — 4,7 % weniger.
>
> **Radien** (r = m·v/(e·B)):
> - r₂₀ = 3,3211 · 10⁻²⁶ kg · 1,3891 · 10⁵ m/s / (1,602 · 10⁻¹⁹ C · 0,600 T) = 4,799 · 10⁻² m = **4,799 cm**
> - r₂₂ = 3,6532 · 10⁻²⁶ kg · 1,3245 · 10⁵ m/s / (1,602 · 10⁻¹⁹ C · 0,600 T) = 5,033 · 10⁻² m = **5,033 cm**
>
> **Differenz und Abstand:**
> - Δr = 5,033 cm − 4,799 cm = 0,2342 cm = **2,342 mm**
> - `data-tex`: `\Delta s = 2 \cdot \Delta r = 4{,}68\,\mathrm{mm}`
> - `data-plain`: `Δs = 2 · Δr = 4,68 mm`
>
> **Ergebnis: Die Auftreffpunkte liegen 4,68 mm auseinander.**
>
> **Zwei Proben:**
> 1. **Verhältnisprobe.** r₂₂/r₂₀ = 5,033/4,799 = 1,0488 — und √(22/20) = 1,0488. ✓
>    Der Radius folgt also tatsächlich der Wurzel aus der Masse.
> 2. **Kurzweg ohne Einzelradien.** Δs = 2·r₂₀·(√(22/20) − 1) = 2 · 4,799 cm · 0,0488 =
>    0,4685 cm = 4,68 mm. ✓ Denselben Weg kannst du für jedes Isotopenpaar benutzen.
>
> **Der Satz, den du dir merken solltest:** Ein Massenunterschied von **10,0 %** erzeugt einen
> Radiusunterschied von nur **4,88 %**. Die Wurzel macht das Gerät unempfindlicher, als man
> erwartet — und genau darum geht es in der nächsten Aufgabe.

---

### 5.8 ue8 — Beurteilung: Reicht der Detektor?

Offene Aufgabe, `<div class="aufgabe">` mit `<button data-loesung="ue8">Musterlösung</button>`
und `.hilfe-text[data-stufe="9"]`. `<span class="ab">Anforderungsbereich III</span>`
Überschrift: *Fortsetzung von Aufgabe 7*

**Aufgabentext:**

> Für die Anordnung aus Aufgabe 7 steht ein **Streifendetektor** zur Verfügung: eine Zeile aus
> nebeneinanderliegenden Messstreifen von je **2,0 mm** Breite. Jeder Streifen meldet nur, wie
> viele Ionen ihn getroffen haben — nicht, wo innerhalb des Streifens.
>
> Der Ionenstrahl ist beim Eintritt in die Ablenkkammer etwa **1 mm** breit.
>
> **Beurteile**, ob sich Ne-20 und Ne-22 mit diesem Aufbau als zwei getrennte Signale nachweisen
> lassen. Gib an, welche Größe du dafür mit welcher vergleichst, und nenne **eine** konkrete
> Maßnahme, mit der sich die Trennung verbessern ließe — mit Begründung, warum gerade sie wirkt.

**Erwartete Argumentation** (`data-stufe="9"`, erster Teil):

> **Vergleich der beiden maßgeblichen Größen.** Zu vergleichen ist der berechnete Abstand der
> Auftreffpunkte, Δs = 4,68 mm, mit dem, was der Detektor räumlich auseinanderhalten kann. Ein
> Streifendetektor mit 2,0 mm Streifenbreite kann zwei Signale dann sicher trennen, wenn
> zwischen ihnen mindestens ein Streifen liegt, der von keinem der beiden Strahlen getroffen
> wird — sonst laufen die Signale in benachbarten oder gar demselben Streifen zusammen.
>
> **Auswertung.** Δs = 4,68 mm entspricht 4,68 mm / 2,0 mm = **2,3 Streifenbreiten**. Die beiden
> Auftreffpunkte landen also nicht im selben und auch nicht zwangsläufig im unmittelbar
> benachbarten Streifen, sondern mit rund zwei Streifen Abstand. Rechnet man die Strahlbreite von
> etwa 1 mm hinzu, ist jedes der beiden Signale rund 1 mm breit; zwischen den belegten Bereichen
> bleibt eine freie Lücke von 4,68 mm − 1 mm = **3,7 mm**.
>
> **Hier lohnt eine genauere Überlegung, und sie entscheidet das Urteil.** Damit *in jeder Lage*
> mindestens ein vollständig unbelegter Streifen zwischen den Signalen liegt, müsste die Lücke
> **4,0 mm** breit sein — im ungünstigsten Fall fällt eine Streifengrenze so, dass zwei Streifen
> je zur Hälfte in die Lücke ragen und beide von je einem Signal angeschnitten werden. Mit 3,7 mm
> ist das knapp verfehlt. Bei günstiger Justierung bleibt ein Streifen frei, bei ungünstiger
> grenzen die beiden belegten Streifen unmittelbar aneinander. Zwei getrennte Maxima sieht man in
> beiden Fällen, ein sauber leerer Streifen dazwischen ist aber nicht garantiert.
>
> **Urteil.** Die Trennung gelingt, aber **ohne große Reserve**. Der Aufbau ist brauchbar, um die
> Existenz zweier Isotope zu zeigen und ihr Häufigkeitsverhältnis grob abzuschätzen. Er ist
> **nicht** komfortabel: Schon eine Verdopplung der Strahlbreite auf 2 mm oder eine Justierung,
> bei der ein Auftreffpunkt genau auf eine Streifengrenze fällt, drückt die Signale in
> benachbarte Streifen und macht die Zuordnung unsicher. Für eine quantitative Häufigkeitsmessung
> wäre der Aufbau zu knapp bemessen.
>
> **Verbesserungsmaßnahme — eine, mit Begründung.** Die wirksamste Größe ist die
> **Beschleunigungsspannung**: Wegen r ∝ √U wächst mit U auch Δs = 2·r₂₀·(√(22/20) − 1)
> proportional zu √U. Eine Erhöhung von 2,00 kV auf **8,00 kV** verdoppelt alle Radien und damit
> auch den Abstand der Auftreffpunkte auf **9,37 mm**, also fast fünf Streifenbreiten. Die
> Trennung ist dann komfortabel.
>
> Genauso gut wäre eine **Verkleinerung von B**, denn r ∝ 1/B; halbiert man B auf 300 mT,
> verdoppelt sich Δs ebenfalls. Beide Maßnahmen wirken über dieselbe Stelle: Sie vergrößern den
> **absoluten** Radius, und weil der relative Unterschied mit 4,88 % festliegt, wächst der
> absolute Abstand mit. Beide haben denselben Preis — die Bahnen werden größer, die Kammer muss
> größer sein.
>
> **Was ausdrücklich nicht hilft:** einen feineren Detektor mit 0,5 mm Streifen einzubauen, wenn
> der Strahl 1 mm breit bleibt. Die Auflösung wird dann nicht mehr vom Detektor begrenzt, sondern
> von der Strahlbreite; mehr Streifen liefern nur eine feinere Abtastung desselben unscharfen
> Flecks. Ebenso wenig hilft es, das **Magnetfeld zu erhöhen** — das verkleinert alle Radien und
> schrumpft Δs bei B = 900 mT auf 3,12 mm.

**Bewertungskriterien** (fett, Aufzählung mit `·` getrennt):

> **Bewertungskriterien**
> · nennt Δs = 4,68 mm und die Streifenbreite 2,0 mm ausdrücklich als die beiden zu
>   vergleichenden Größen
> · bildet das Verhältnis (rund 2,3 Streifen) oder argumentiert gleichwertig über die Zahl der
>   dazwischenliegenden Streifen
> · bezieht die Strahlbreite von 1 mm in die Betrachtung ein, statt die Auftreffpunkte als
>   mathematische Punkte zu behandeln
> · kommt zu einem **abgestuften** Urteil („trennbar, aber ohne Reserve") statt zu einem bloßen
>   Ja oder Nein
> · Zusatzpunkt, wenn erkannt wird, dass die Lage der Streifengrenzen mitentscheidet und ein
>   vollständig freier Streifen erst ab 4,0 mm Lücke garantiert wäre
> · nennt eine Maßnahme, die den absoluten Radius vergrößert (U erhöhen **oder** B verringern),
>   und begründet sie über r ∝ √U beziehungsweise r ∝ 1/B
> · rechnet die Wirkung der Maßnahme wenigstens abschätzend vor (etwa: vierfache Spannung ⟹
>   doppelter Abstand)
> · **kein Punkt** für „einen besseren Detektor nehmen" ohne Bezug zur Strahlbreite; **Abzug**,
>   wenn ein stärkeres Magnetfeld als Verbesserung genannt wird — es verschlechtert die Trennung

---

### 5.9 ue9 — Eine Aussage aus dem Unterrichtsgespräch bewerten

Offene Aufgabe, `<button data-loesung="ue9">Musterlösung</button>`,
`<span class="ab">Anforderungsbereich III</span>`

**Aufgabentext:**

> In der Auswertung des Fadenstrahlrohr-Versuchs sagt eine Mitschülerin:
>
> > *„Auf das Elektron wirkt im Magnetfeld dauernd eine Kraft. Nach dem zweiten Newtonschen
> > Gesetz ist F = m·a, also wird es dauernd beschleunigt. Und beschleunigt heißt schneller.
> > Deshalb wird das Elektron auf seiner Bahn immer schneller — man sieht es nur nicht, weil
> > alles so schnell geht."*
>
> **Bewerte diese Aussage.** Sag ausdrücklich, welcher Teil zutrifft und welcher nicht, führe
> den entscheidenden Grund an und nenne eine Beobachtung am Fadenstrahlrohr, die die Aussage
> unmittelbar widerlegt.

**Erwartete Argumentation** (`data-stufe="9"`, erster Teil):

> **Was an der Aussage stimmt.** Die ersten beiden Schritte sind korrekt und sollen ausdrücklich
> anerkannt werden: Es wirkt tatsächlich dauernd eine Kraft, und aus F = m·a folgt tatsächlich
> eine von null verschiedene Beschleunigung. Die Mitschülerin rechnet richtig; sie stolpert erst
> im dritten Schritt.
>
> **Wo der Fehler liegt.** Der Fehler steckt in der Gleichsetzung „beschleunigt heißt schneller".
> Beschleunigung ist die zeitliche Änderung des Geschwindigkeits**vektors**, nicht die seines
> Betrags. Ein Vektor ändert sich auch dann, wenn nur seine **Richtung** wechselt. Genau dieser
> Fall liegt hier vor: Die Lorentzkraft steht in jedem Augenblick senkrecht auf v⃗, sie ist eine
> reine **Zentripetal**beschleunigung. Eine Tangentialkomponente, die den Betrag von v ändern
> könnte, existiert nicht — sie wäre die einzige, die „schneller" bewirken würde.
>
> **Der entscheidende Grund — über die Arbeit.** Nur eine Kraft mit einer Komponente in
> Bewegungsrichtung kann die kinetische Energie ändern. Für die Arbeit gilt W = F·s·cos φ, und
> der Winkel zwischen Lorentzkraft und Weg beträgt in jedem Bahnpunkt 90°. Wegen cos 90° = 0 ist
> die vom Magnetfeld an der freien Ladung verrichtete Arbeit **exakt null** — nicht klein,
> nicht vernachlässigbar, sondern null. Damit bleibt ½·m·v² konstant und mit ihm der Betrag v.
> Die Kette lautet: F⃗ ⊥ v⃗ ⟹ W = 0 ⟹ E_kin konstant ⟹ v konstant ⟹ nur die Richtung ändert
> sich.
>
> **Die Beobachtung, die es entscheidet.** Der Leuchtkreis im Fadenstrahlrohr bleibt über die
> gesamte Versuchsdauer **gleich groß**. Träfe die Behauptung zu, müsste wegen r = m·v/(|q|·B)
> mit wachsendem v auch der Radius wachsen — sichtbar wäre eine nach außen laufende Spirale,
> kein geschlossener Kreis. Man sieht die Spirale nicht, und das ist kein Auflösungsproblem: Ein
> Elektron durchläuft bei B = 3,0 mT rund 84 Millionen Umläufe pro Sekunde; selbst ein
> Geschwindigkeitszuwachs von einem Promille pro Umlauf hätte den Strahl längst gegen die
> Glaswand getrieben.
>
> **Wo die Vorstellung herkommt — und wie man sie richtigstellt.** Die Erfahrung „Kraft macht
> schneller" stammt aus der geradlinigen Mechanik, wo Kraft und Bewegung meist parallel liegen.
> Sobald sie senkrecht stehen, trägt sie nicht mehr; dasselbe gilt für die Seilkraft beim
> Hammerwurf oder die Gravitationskraft auf einer Kreisbahn. Schneller wird das Elektron im
> Versuch tatsächlich — aber ausschließlich in der Beschleunigungsstrecke davor, und die arbeitet
> mit einem **elektrischen** Feld. Die Arbeitsteilung lautet: Das elektrische Feld ändert den
> Betrag, das magnetische Feld die Richtung.

**Bewertungskriterien:**

> **Bewertungskriterien**
> · erkennt an, dass Kraft und Beschleunigung vorhanden sind, und benennt den Fehler genau an der
>   Stelle „beschleunigt = schneller"
> · unterscheidet ausdrücklich zwischen der Änderung des Geschwindigkeits**vektors** und der
>   Änderung seines **Betrags**
> · führt als tragenden Grund die Senkrechtstellung von F⃗ zu v⃗ an — nicht nur behauptet, sondern
>   mit der Folgerung W = F·s·cos 90° = 0
> · schließt daraus über die Konstanz der kinetischen Energie auf die Konstanz von v
> · nennt eine **Beobachtung**, nicht bloß eine weitere Formel: der Kreis bleibt gleich groß,
>   statt aufzuspiralen — mit dem Bezug r ∝ v
> · ordnet die Beschleunigung dem elektrischen Feld der Beschleunigungsstrecke zu
> · **kein voller Punktwert**, wenn nur „das Magnetfeld verrichtet keine Arbeit" behauptet wird,
>   ohne die Senkrechtstellung als Begründung zu nennen — das ist die Aussage, nicht ihr Grund

---

### 5.10 ue10 — Warum die Umlaufdauer nicht von der Geschwindigkeit abhängt

Offene Aufgabe, `<button data-loesung="ue10">Musterlösung</button>`,
`<span class="ab">Anforderungsbereich III</span>`

**Aufgabentext:**

> Im Zyklotron laufen Protonen zwischen zwei halbkreisförmigen Elektroden („Duanten") im
> homogenen Magnetfeld. Bei jedem Durchgang durch den Spalt zwischen den Duanten werden sie von
> einer Wechselspannung ein Stück beschleunigt; ihre Bahn wird dadurch von Halbkreis zu Halbkreis
> größer.
>
> a) **Begründe**, warum die Umlaufdauer trotzdem bei jedem Umlauf dieselbe bleibt.
> b) **Erläutere**, welche technische Folge das für den Bau des Zyklotrons hat.
> c) **Beurteile**, unter welchen Umständen diese Beschreibung ihre Gültigkeit verliert.

**Erwartete Argumentation** (`data-stufe="9"`, erster Teil):

> **zu a) Die Begründung.** Zwei Größen wachsen gleichzeitig und im selben Verhältnis. Wird das
> Proton schneller, so wächst nach r = m·v/(|q|·B) der Bahnradius **proportional zu v** — und
> mit ihm der Umfang 2πr. Für die Umlaufdauer gilt
> - `data-tex`: `T = \dfrac{2\pi r}{v} = \dfrac{2\pi}{v} \cdot \dfrac{m \cdot v}{|q| \cdot B} = \dfrac{2\pi \cdot m}{|q| \cdot B}`
> - `data-plain`: `T = 2πr/v = (2π/v) · m·v/(|q|·B) = 2 · π · m / (|q| · B)`
>
> Der Weg wird länger, aber genau in dem Maß, in dem auch die Geschwindigkeit steigt; im
> Quotienten kürzt sich v vollständig heraus. Übrig bleibt ein Ausdruck, der **nur** die
> Teilcheneigenschaften m und |q| und die Feldstärke B enthält — drei Größen, die sich während
> des Betriebs nicht ändern. Das Proton legt bei doppelter Geschwindigkeit den doppelten Umfang
> in derselben Zeit zurück.
>
> Wichtig für die Begründung: Der **Zuwachs** an Geschwindigkeit stammt nicht aus dem Magnetfeld,
> sondern aus dem elektrischen Feld im Spalt. Innerhalb eines Duanten ist v konstant, der
> Halbkreis dort exakt gleichförmig. Das Magnetfeld sorgt allein für die Krümmung.
>
> **zu b) Die technische Folge.** Weil T von v unabhängig ist, ist auch die Frequenz
> - `data-tex`: `f_c = \dfrac{1}{T} = \dfrac{|q| \cdot B}{2\pi \cdot m}`
> - `data-plain`: `f_c = 1/T = |q| · B / (2 · π · m)`
>
> eine feste Zahl. Man kann die Wechselspannung zwischen den Duanten deshalb mit einer
> **konstanten Frequenz** betreiben und muss sie während der Beschleunigung nicht nachregeln:
> Das Teilchen kommt immer im richtigen Moment am Spalt an, egal ob es beim zweiten oder beim
> zweihundertsten Umlauf ist. Genau darauf beruht die Bauart. Ein Zahlenwert zur Einordnung:
> Für Protonen in B = 1,5 T ist f_c = 22,9 MHz, T = 43,7 ns — ein handelsüblicher
> Hochfrequenzsender, fest eingestellt.
>
> Zweite Folge: Die Frequenz muss beim Wechsel der Teilchensorte angepasst werden, denn f_c
> hängt über |q|/m an der spezifischen Ladung. Für Alphateilchen, deren spezifische Ladung rund
> halb so groß ist wie die des Protons, ist auch f_c etwa halb so groß.
>
> **zu c) Die Grenze.** Die Rechnung setzt m = konstant voraus. Das gilt nur, solange v klein
> gegen die Lichtgeschwindigkeit ist. Relativistisch wächst die träge Masse mit dem Faktor
> γ = 1/√(1 − v²/c²), und damit wächst auch T = 2πγm₀/(|q|·B) mit der Energie — das Teilchen
> kommt **zu spät** am Spalt an, gerät außer Takt und wird schließlich nicht mehr beschleunigt,
> sondern abgebremst.
>
> Zahlen für Protonen (Ruheenergie 938 MeV):
>
> | kinetische Energie | γ | v/c | Zuwachs von T |
> |---|---|---|---|
> | 1 MeV | 1,0011 | 0,046 | +0,11 % |
> | 10 MeV | 1,0107 | 0,145 | +1,07 % |
> | 20 MeV | 1,0213 | 0,203 | +2,13 % |
>
> Ein klassisches Zyklotron ist damit auf **etwa 20 MeV** Protonenenergie begrenzt; darüber ist
> der Phasenfehler nicht mehr zu tolerieren. Die Auswege sind bekannt und benennen jeweils die
> verletzte Voraussetzung: Das **Synchrozyklotron** senkt die Frequenz während des Zyklus
> passend ab, das **Isochronzyklotron** lässt B nach außen hin wachsen, sodass B/m konstant
> bleibt, und das **Synchrotron** hält den Radius fest und fährt stattdessen B und f hoch.
>
> Eine zweite, praktische Grenze ist geometrisch: Der Radius wächst mit √E_kin, und irgendwann
> ist der Magnetpol zu Ende. Für 20-MeV-Protonen bei B = 1,5 T ist r = 43 cm — das ist der
> Grund, warum Zyklotrone tonnenschwere Magnete haben.

**Bewertungskriterien:**

> **Bewertungskriterien**
> · zu a): führt T = 2πr/v und r = m·v/(|q|·B) zusammen und zeigt **rechnerisch**, dass sich v
>   herauskürzt — nicht nur die Behauptung, T hänge nicht von v ab
> · zu a): erklärt den Sachverhalt zusätzlich anschaulich (längerer Weg bei entsprechend höherer
>   Geschwindigkeit), also nicht rein formal
> · zu a): ordnet den Geschwindigkeitszuwachs dem elektrischen Feld im Spalt zu und hält fest,
>   dass v innerhalb eines Duanten konstant ist
> · zu b): nennt die **feste** Frequenz der Wechselspannung als Folge und begründet sie mit
>   f_c = |q|·B/(2π·m)
> · zu b): stellt fest, dass die Frequenz nicht nachgeregelt werden muss — das ist der Kern der
>   technischen Aussage
> · zu c): nennt die relativistische Massenzunahme als die verletzte Voraussetzung und beschreibt
>   die Folge (Teilchen gerät außer Takt / Phasenfehler)
> · zu c): stützt das Urteil mit wenigstens einer Größenordnung (v vergleichbar mit c, Energien
>   im Bereich einiger 10 MeV) statt nur qualitativ
> · Zusatzpunkt für die geometrische Grenze (endlicher Magnetdurchmesser) oder für die Nennung
>   eines der Auswege mit Begründung, welche Voraussetzung er repariert

---

### 5.11 Kontrollrechnungen zu Abschnitt 5 (K-22 bis K-30)

Skript: `vorarbeit/physik/uebungen_abschnitt5.py`, Ausgabe in `ausgabe_abschnitt5.txt`.
Konstanten wie in Abschnitt 4.1 (CODATA 2018), Alphamasse 6,6446573357 · 10⁻²⁷ kg.

| Nr. | Aufgabe | geprüfte Größe | Ergebnis | in der Aufgabe angegeben |
|---|---|---|---|---|
| K-22 | ue1 | v (Elektron, 1000 V) | 1,875537 · 10⁷ m/s | 1,876 · 10⁷ m/s |
| K-22 | ue1 | r (B = 3,00 mT) | 3,554537 · 10⁻² m | **3,55 cm**, tol 0,06 cm |
| K-22 | ue1 | Gegenprobe r = √(2mU/e)/B | 3,5545 cm | identisch ✓ |
| K-22 | ue1 | T zur Gegenprobe mit der Simulation | 11,908 ns | Anzeige 11,91 ns ✓ |
| K-22 | ue1 | v/c | 6,256 % | klassisch zulässig |
| K-23 | ue2 | T (Proton, B = 130 mT) | 5,045729 · 10⁻⁷ s | **504,6 ns**, tol 6 ns |
| K-23 | ue2 | f_c = 1/T | 1,9819 MHz | 1,982 MHz |
| K-23 | ue2 | Umweg U = 1000 V: v, r, 2πr/v | 4,3769 · 10⁵ m/s, 3,5149 cm, 5,045729 · 10⁻⁷ s | Tabelle ✓ |
| K-23 | ue2 | Umweg U = 200 V: v, r, 2πr/v | 1,9574 · 10⁵ m/s, 1,5719 cm, 5,045729 · 10⁻⁷ s | Tabelle ✓ |
| K-24 | ue3 | v = e·B·r/m_e (r = 4,20 cm, B = 1,80 mT) | 1,329668 · 10⁷ m/s | **13 297 km/s**, tol 200 km/s |
| K-24 | ue3 | v/c | 4,435 % | „rund 4,4 %" |
| K-24 | ue3 | Rückrechnung U = m·v²/(2e) | 502,61 V | „503 V" |
| K-24 | ue3 | Gegenprobe: r aus diesem U | 4,2000 cm | Ringschluss ✓ |
| K-25 | ue5 | r² · B² | 2,838758 · 10⁻⁹ | 2,8388 · 10⁻⁹ |
| K-25 | ue5 | q/m = 2U/(r²B²) | 1,761333 · 10¹¹ C/kg | **1,761 · 10¹¹**, tol 4 · 10⁹ |
| K-25 | ue5 | Literaturwert e/m_e | 1,758820 · 10¹¹ C/kg | 1,7588 · 10¹¹ |
| K-25 | ue5 | Abweichung der Messung | +0,14 % | „+0,14 %" |
| K-25 | ue5 | exakter Sollradius bei 250 V / 1,60 mT | 3,33238 cm ⟹ 2r = 6,6648 cm | auf 6,66 cm abgelesen ✓ |
| K-26 | ue6 | v (Proton, 450 V) | 2,936145 · 10⁵ m/s | 2,936 · 10⁵ m/s = 293,6 km/s |
| K-26 | ue6 | E = v·B (B = 200 mT) | 5,872291 · 10⁴ V/m | **58,7 kV/m**, tol 0,8 kV/m |
| K-26 | ue6 | U_P = E·d (d = 2,00 cm) | 1174,46 V | „1174 V" — deckt sich mit 4.9 ✓ |
| K-26 | ue6 | Kräfteprobe q·E gegen q·v·B | beide 9,408447 · 10⁻¹⁵ N | gleich ✓ |
| K-26 | ue6 | Alphateilchen bei 890 V | 2,929840 · 10⁵ m/s, Abweichung 0,215 % | „dieselbe Geschwindigkeit" ✓ |
| K-27 | ue7 | v₂₀, v₂₂ | 1,389139 · 10⁵ / 1,324492 · 10⁵ m/s | 138,9 / 132,4 km/s |
| K-27 | ue7 | r₂₀, r₂₂ | 4,7991 cm / 5,0334 cm | 4,799 cm / 5,033 cm |
| K-27 | ue7 | Δr | 2,3424 mm | 2,342 mm |
| K-27 | ue7 | Δs = 2·Δr | 4,6848 mm | **4,68 mm**, tol 0,15 mm |
| K-27 | ue7 | r₂₂/r₂₀ gegen √(22/20) | 1,048809 gegen 1,048809 | identisch ✓ |
| K-27 | ue7 | Kurzformel 2·r₂₀·(√1,1 − 1) | 4,6848 mm | identisch ✓ |
| K-27 | ue7 | relative Radiendifferenz | 4,881 % bei 10,0 % Massenunterschied | „4,88 %" |
| K-27 | ue7 | Kontrolle mit **exakten** Isotopenmassen (19,99244 / 21,99139 u) | Δs = 4,6832 mm | weicht nur um 0,03 % von 4,6848 mm ab — die Nennmassen sind zulässig ✓ |
| K-27 | ue7 | Rundungsfalle: Radien auf 4,8 / 5,0 cm gerundet | Δs = 4,0 mm | Grundlage der `nah`-Rückmeldung ✓ |
| K-27 | ue7 | Fehlerfall r ∝ m statt r ∝ √m | Δs = 9,598 mm | Grundlage der `weit`-Rückmeldung („rund 9,6 mm") ✓ |
| K-28 | ue8 | Δs in Streifenbreiten (2,0 mm) | 2,342 | „rund 2,3 Streifenbreiten" |
| K-28 | ue8 | freie Lücke bei 1 mm Strahlbreite | 4,685 − 1 = 3,68 mm | „3,7 mm" |
| K-28 | ue8 | für garantiert freien Streifen nötige Lücke (ungünstigste Lage der Streifengrenzen) | 2 · 2,0 mm = 4,0 mm | 3,7 mm < 4,0 mm ⟹ nicht garantiert ✓ |
| K-28 | ue8 | Δs bei B = 900 mT | 3,123 mm | „3,12 mm — schlechter" |
| K-28 | ue8 | Δs bei U = 8,00 kV | 9,370 mm | „9,37 mm — fast fünf Streifen" |
| K-29 | zuordnung | Bezugsfall U₀ = 450 V, B₀ = 3,00 mT | v = 12 581,5 km/s, R = 2,3845 cm | nur als Bezug, keine Zahl im Bild |
| K-29 | zuordnung | 4·U₀ | v-Faktor 2,0000, r-Faktor 2,0000 | Bild C: doppelter Radius ✓ |
| K-29 | zuordnung | 2·B₀ | v unverändert, r-Faktor 0,5000 | Bild D: halber Radius ✓ |
| K-29 | zuordnung | T(B₀) gegen T(2B₀) | 11,908 ns gegen 5,954 ns | „nur Zeile 3 hat halbe Umlaufdauer" ✓ |
| K-30 | ue10 | f_c, T (Proton, B = 1,5 T) | 22,8678 MHz, 43,73 ns | „22,9 MHz, 43,7 ns" |
| K-30 | ue10 | γ und ΔT bei 1 / 10 / 20 MeV | 1,00107 / 1,01066 / 1,02132 ⟹ +0,11 / +1,07 / +2,13 % | Tabelle ✓ |
| K-30 | ue10 | v/c bei 1 / 10 / 20 MeV | 0,0461 / 0,1448 / 0,2032 | Tabelle ✓ |
| K-30 | ue10 | Ruheenergie des Protons | 938,27 MeV | „938 MeV" |
| K-30 | ue10 | Bahnradius eines 20-MeV-Protons bei B = 1,5 T (relativistisch, p·c = 194,76 MeV) | 0,4331 m | „r = 43 cm" |
| K-30 | ue9 | Umlauffrequenz des Elektrons bei B = 3,0 mT | 8,3977 · 10⁷ Hz | „rund 84 Millionen Umläufe pro Sekunde" |
| K-30 | ue5 | m_e = e / (q/m) aus dem Messwert | 9,097 · 10⁻³¹ kg | „9,10 · 10⁻³¹ kg" |

**Zwei Anmerkungen zu den Toleranzen.**

1. Alle Toleranzen sind so gewählt, dass die auf drei signifikante Stellen gerundete Rechnung
   angenommen wird, der jeweils typische Fehler aber nicht. Beispiel ue7: tol = 0,15 mm nimmt
   4,68 mm und 4,7 mm an, weist aber 2,34 mm (Faktor 2 vergessen) und 9,37 mm (linear statt
   Wurzel) zurück — beide liegen im `weit`-Bereich und bekommen dort ihre eigene Rückmeldung.
2. Bei ue5 ist tol = 4 · 10⁹ C/kg gleich 2,3 % des Sollwerts. Das nimmt sowohl den mit dem
   Literaturwert gerechneten 1,7588 · 10¹¹ als auch den aus den Messwerten folgenden
   1,7613 · 10¹¹ an. Das ist beabsichtigt: Beide Wege sind fachlich richtig, und die Aufgabe
   soll nicht an einer Rundung der vierten Stelle scheitern.

## 6 · Abschluss

Überschrift der Section: **Zusammenfassung und Selbstcheck**
(`<section id="abschluss">`, `.stufe`-Nummer 6)

Aufbau: erst die vier Kernaussagen als Karte, dann der Abiturhinweis, dann der Selbstcheck,
dann der Export-Knopf, dann der Lehrerteil (Abschnitt 7). Die Reihenfolge ist die des
Referenzmoduls und wird nicht verändert.

### 6.1 Die vier Kernaussagen des Moduls

`<div class="karte">` mit der Überschrift *Was du mitnimmst*. Einleitungssatz darunter in Grau:
*„Vier Sätze. Wenn du sie im Kopf hast, kannst du jede Aufgabe dieses Inhaltsfelds anfangen —
alles Weitere ist Einsetzen."*

Danach vier nummerierte Blöcke. Jeder besteht aus einer fetten Überschriftzeile, zwei bis drei
Sätzen und der zugehörigen Formel als `.m.block`.

---

**1 — Betrag und Richtung sind zwei getrennte Fragen.**

> Der Betrag der Lorentzkraft hängt nur von Beträgen ab; über die Richtung entscheiden allein
> das Vorzeichen der Ladung und die Richtung von B⃗. Deshalb steht in jeder Betragsformel
> **|q|**, und deshalb wird das Vorzeichen nicht eingesetzt, sondern in der Handregel
> berücksichtigt. Wer beides vermischt, bekommt negative Radien.

- `data-tex`: `F = |q| \cdot v \cdot B \quad (\vec{v} \perp \vec{B}) \qquad \vec{F} \perp \vec{v},\ \vec{F} \perp \vec{B}`
- `data-plain`: `F = |q| · v · B   (v ⊥ B)     F steht senkrecht auf v und auf B`

Kehrst du **nur** das Ladungsvorzeichen um oder **nur** die Feldrichtung, dreht sich der
Umlaufsinn. Kehrst du **beides** um, bleibt alles wie es war (Aufgabe `zuordnung`, Zeilen 1 und 4).

---

**2 — Das Magnetfeld verrichtet an einer freien Ladung keine Arbeit.**

> Die Kraft steht in jedem Bahnpunkt senkrecht auf dem Weg, also ist W = F·s·cos 90° = 0. Damit
> bleiben die kinetische Energie und mit ihr der **Betrag** von v⃗ konstant; nur die Richtung
> ändert sich. Das Ergebnis ist ein geschlossener Kreis, keine Spirale. Schneller wird ein
> Teilchen ausschließlich im **elektrischen** Feld der Beschleunigungsstrecke davor.

- `data-tex`: `W = \vec{F} \cdot \vec{s} = F \cdot s \cdot \cos 90^\circ = 0 \quad \Longrightarrow \quad E_{\text{kin}} = \text{konst.} \quad \Longrightarrow \quad |\vec{v}| = \text{konst.}`
- `data-plain`: `W = F · s · cos 90° = 0   ⟹   E_kin konstant   ⟹   Betrag von v konstant`

Die Arbeitsteilung in einem Satz: **Das elektrische Feld ändert den Betrag, das magnetische
Feld die Richtung.**

---

**3 — Radius und Umlaufdauer hängen an völlig verschiedenen Größen.**

> Der Radius wächst mit der Wurzel aus Spannung und Masse und fällt mit B. Die Umlaufdauer
> dagegen kennt die Geschwindigkeit überhaupt nicht: Wird das Teilchen schneller, wird sein Kreis
> im selben Maß größer, und der Quotient Umfang durch Geschwindigkeit bleibt derselbe.

- `data-tex`: `r = \dfrac{m \cdot v}{|q| \cdot B} = \dfrac{1}{B}\sqrt{\dfrac{2 \cdot m \cdot U}{|q|}} \qquad T = \dfrac{2\pi \cdot m}{|q| \cdot B} \qquad f_c = \dfrac{|q| \cdot B}{2\pi \cdot m}`
- `data-plain`: `r = m·v/(|q|·B) = (1/B)·√(2·m·U/|q|)     T = 2·π·m/(|q|·B)     f_c = |q|·B/(2·π·m)`

Daraus die vier Proportionalitäten, die im Abitur ohne Rechnung abgefragt werden:
**r ∝ √U · r ∝ √m · r ∝ 1/B · T unabhängig von v und von U.**

---

**4 — Eine Bahnmessung liefert nie m und nie q, sondern immer nur q/m.**

> In r und T stehen Masse und Ladung ausschließlich als Quotient. Deshalb misst das
> Fadenstrahlrohr die **spezifische Ladung** und nicht die Elektronenmasse; für die braucht es
> eine zweite, unabhängige Messung (Millikan). Und deshalb trennt ein Massenspektrometer Isotope,
> ohne je eine einzelne Masse zu wiegen — es vergleicht Radien.

- `data-tex`: `\dfrac{|q|}{m} = \dfrac{2 \cdot U}{r^{2} \cdot B^{2}} \qquad m = \dfrac{|q| \cdot r^{2} \cdot B^{2}}{2 \cdot U}`
- `data-plain`: `|q|/m = 2·U/(r²·B²)     m = |q|·r²·B²/(2·U)`

Der Geschwindigkeitsfilter ist der Gegenpol dazu: In v = E/B kürzt sich q heraus und m kommt
gar nicht vor. Er sortiert **nur** nach Geschwindigkeit — und schafft damit erst die Lage, in
der eine Radiusmessung eindeutig ist.

---

### 6.2 Blick aufs Zentralabitur

`<div class="hinweis">` mit `<strong>Blick aufs Zentralabitur.</strong>`, Wortlaut verbindlich:

> **Blick aufs Zentralabitur.** Geladene Teilchen im Magnetfeld erscheinen im LK zuverlässig in
> drei Zuschnitten, und alle drei hast du hier bearbeitet.
>
> **Erstens: Fadenstrahlrohr und spezifische Ladung.** Gegeben sind U, B und ein abgelesener
> Kreis**durchmesser**, gesucht ist |q|/m — oft mit anschließender Fehlerbetrachtung, weil r
> quadratisch eingeht. Die beiden Stolpersteine sind immer dieselben: Durchmesser statt Radius
> eingesetzt und der Faktor 2 aus |q|·U = ½·m·v² vergessen (Aufgabe ue5).
>
> **Zweitens: Massenspektrometer und Isotopentrennung.** Häufig zweiteilig — erst der Abstand
> zweier Auftreffpunkte über r ∝ √m, dann die Beurteilung, ob eine gegebene Detektorauflösung
> dafür ausreicht, samt Vorschlag zur Verbesserung. Der Filter davor ist Teil der Anordnung und
> wird gern mitverlangt (Aufgaben ue6, ue7, ue8).
>
> **Drittens: Bewertungsaufgaben zur Arbeit des Magnetfeldes.** Eine Aussage aus einem
> Unterrichtsgespräch soll beurteilt werden — fast immer läuft sie auf „Kraft bedeutet schneller
> werden" hinaus. Erwartet wird nicht nur das Urteil, sondern die Kette F⃗ ⊥ v⃗ ⟹ W = 0 ⟹
> E_kin konstant, dazu eine **Beobachtung**, die die Aussage widerlegt (Aufgaben ue9, ue10).
>
> Ein Hinweis zur Bearbeitungsform: Der Anforderungsbereich III wird in diesem Inhaltsfeld fast
> nie durch längeres Rechnen bedient, sondern durch Begründen und Bewerten. Wer dort eine
> Rechnung abliefert, wo eine Begründung verlangt ist, verschenkt die Punkte.
>
> **Was direkt anschließt:** Bewegt sich statt der freien Ladung ein ganzer Leiter durch das
> Feld, sammeln sich die Ladungen an seinen Enden, und es entsteht eine Spannung. Das ist der
> Einstieg ins Modul *Elektromagnetische Induktion* — dort wird aus derselben Lorentzkraft
> U = B·l·v.

### 6.3 Selbstcheck

`<div class="karte">`, Überschrift *Selbstcheck*, darunter `<div class="check">` mit sechs
`<label><input type="checkbox"><span>…</span></label>`. Formulierung nah an den
Kompetenzerwartungen des Kernlehrplans (Umgang mit Fachwissen, Erkenntnisgewinnung, Bewertung),
Einleitungszeile in Grau: *„Hak nur ab, was du ohne Nachschlagen kannst. Was offen bleibt, sagt
dir, wohin du zurückgehst."*

Die sechs Sätze, Wortlaut verbindlich (jeder beginnt mit `… `):

1. … die Lorentzkraft nach Betrag **und** Richtung bestimmen, auch für negative Ladungen, und
   dabei die Drei-Finger-Regel der rechten Hand richtig anwenden.
2. … begründen, warum ein Magnetfeld an einer frei bewegten Ladung keine Arbeit verrichtet, und
   daraus die Kreisbahn statt einer Spirale herleiten.
3. … die Bahngleichungen r = m·v/(|q|·B) und T = 2π·m/(|q|·B) herleiten und angeben, von welchen
   Größen r und T jeweils abhängen — und von welchen nicht.
4. … aus Beschleunigungsspannung und Flussdichte den Bahnradius berechnen und die Rechnung
   umkehren, um aus einem gemessenen Radius auf v oder auf |q|/m zu schließen.
5. … die Wirkungsweise eines Wien'schen Geschwindigkeitsfilters und eines Massenspektrometers
   erklären und beurteilen, ob eine gegebene Anordnung zwei Isotope trennen kann.
6. … eine Aussage über geladene Teilchen im Magnetfeld fachlich bewerten und meine Begründung
   auf eine Beobachtung oder eine Rechnung stützen, statt sie zu behaupten.

Die Sätze 1 bis 3 gehören zum Kompetenzbereich *Umgang mit Fachwissen*, 4 und 5 zu
*Erkenntnisgewinnung*, Satz 6 zu *Bewertung*. Der Bauagent schreibt diese Zuordnung **nicht**
in die Seite — sie steht hier für den Lehrerteil.

Für die `data-plain`-Fassungen in den Sätzen 3 und 4: `r = m · v / (|q| · B)` und
`T = 2 · π · m / (|q| · B)` beziehungsweise `|q|/m`.

### 6.4 Export

Unter dem Selbstcheck der Knopf aus dem Referenzmodul, unverändert:

```html
<div class="knopfleiste" style="margin-top:18px">
  <button class="primaer" id="bExport">Ergebnis als Text kopieren</button>
</div>
```

Darunter eine Zeile in Grau: *„Kopiert deine Antworten, die Rückmeldungen und deine
Selbsteinschätzung als Text. Nichts davon wird gespeichert — schließt du die Seite, ist alles
weg."* Die Namensliste `var namen = {…}` steht in Abschnitt 8.4.

## 7 · Lehrerteil

`<details class="lehrer">` am Ende der Seite, Summary: **Für die Lehrkraft — Einordnung,
Zeitbedarf, typische Fehler, Differenzierung, Experimente**. Der Block verschwindet beim
Drucken (`@media print` aus dem Referenzmodul, unverändert übernommen).

Innerhalb des `<details>` fünf `<h4>`-Abschnitte in dieser Reihenfolge.

### 7.1 Einordnung

> **Inhaltsfeld.** *Ladungen, Felder und Induktion* (Kernlehrplan NRW, Physik LK, Q1). Bedient
> werden die Kompetenzbereiche *Umgang mit Fachwissen* (Abschnitte 2 und 3), *Erkenntnisgewinnung*
> (Simulation, ue3, ue5, ue7) und *Bewertung* (ue8, ue9, ue10).
>
> **Stellung in der Reihe.** Dieses Modul steht **vor** der Induktion. Die Reihenfolge ist nicht
> beliebig, sie ist die Voraussetzungskette:
>
> 1. Elektrisches Feld und Plattenkondensator (EF, hier nur als Vorwissen abgefragt, `vw3`)
> 2. **Magnetisches Feld und Lorentzkraft — dieses Modul**
> 3. Elektromagnetische Induktion (`module/physik-q1-induktion.html`)
> 4. Selbstinduktion, Schwingkreis
>
> Der Übergang zu Schritt 3 ist inhaltlich eine einzige Drehung: Dieselbe Lorentzkraft, die hier
> ein freies Teilchen auf den Kreis zwingt, trennt in einem **bewegten Leiter** die Ladungen und
> erzeugt damit U = B·l·v. Das Induktionsmodul leitet genau so her (dort im `<details>`
> „Herleitung von U = −B·l·v über die Lorentzkraft"). Wer die Induktion vorzieht, muss diese
> Herleitung entweder auslassen oder die Lorentzkraft nebenbei einführen — beides kostet mehr
> Zeit, als die richtige Reihenfolge spart.
>
> **Was dieses Modul ausdrücklich nicht behandelt:** magnetischer Fluss, Induktionsgesetz,
> Lenzsche Regel. Sie tauchen nur im Ausblicksatz am Ende von Abschnitt 2 und im Abiturhinweis
> auf. Das ist Absicht — der Fluss braucht den Begriff der durchsetzten Fläche, und der gehört
> ins Folgemodul.
>
> **Voraussetzungen aus der EF:** Energiesatz und Arbeit (W = F·s·cos φ), Kreisbewegung mit
> Zentripetalkraft F_Z = m·v²/r, homogenes Feld im Plattenkondensator mit E = U/d. Die drei
> Vorwissensfragen prüfen genau diese drei Punkte. Fällt `vw3` reihenweise durch, ist der
> Wien-Filter in Abschnitt 3.3 verfrüht; dann besser erst den Kondensator wiederholen.

### 7.2 Zeitbedarf

Chip im Seitenkopf: **ca. 135 Minuten** — drei Unterrichtsstunden, nicht zwei.

| Abschnitt | Zeit | Sozialform / Hinweis |
|---|---|---|
| 1 Einstieg mit Vorwissensfragen | 10 min | Einzelarbeit, Auswertung im Plenum |
| 2 Erklärteil (Lorentzkraft, Richtung, Fehlvorstellung) | 30 min | **hier wird angehalten**, siehe 7.3 |
| 3 Vertiefung (Radius, Umlaufdauer, Filter, Spektrometer, q/m) | 30 min | Herleitungen in den `<details>` selbst lesen lassen |
| 4 Simulation mit Beobachtungsauftrag | 25 min | Partnerarbeit an einem Gerät, Ergebnisse schriftlich |
| 5 Übungen ue1 bis ue7 | 30 min | Einzelarbeit, Hilfen selbstständig |
| 6 Abschluss und Selbstcheck | 10 min | Plenum |
| **Summe** | **135 min** | |

Die drei offenen Aufgaben **ue8, ue9 und ue10 sind nicht eingerechnet.** Sie brauchen zusammen
noch einmal rund 40 Minuten und eignen sich besser als Hausaufgabe mit anschließender
Besprechung — ihr Ertrag liegt im Vergleich verschiedener Formulierungen, und der lebt davon,
dass mehrere Fassungen vorliegen.

**Eine sinnvolle Dreiteilung:**

| Stunde | Inhalt |
|---|---|
| 1 | Abschnitte 1 und 2, Realexperiment Leiterschaukel (7.5), Hausaufgabe: Abschnitt 3 lesen |
| 2 | Abschnitt 3 sichern, dann Simulation mit Beobachtungsauftrag, `sim1` und `sim2` |
| 3 | Übungen ue1 bis ue7, Abschluss; ue8 bis ue10 als Hausaufgabe |

Wer nur **90 Minuten** hat: Abschnitt 3.4 (Massenspektrometer) und die Aufgaben ue6 bis ue8
streichen, den Filter auf Merksatz 5 zusammenziehen und Modus 2 der Simulation nur vorführen.
Der Kern — Lorentzkraft, keine Arbeit, r und T — bleibt vollständig erhalten.

### 7.3 Typische Schülerfehler und wo im Gespräch anzuhalten ist

**Der wichtigste Fehler zuerst.**

> **1 — „Das Magnetfeld beschleunigt das Teilchen."** Diese Vorstellung ist keine Nachlässigkeit,
> sondern eine saubere, aber unvollständige Anwendung von F = m·a: Kraft ist da, also
> Beschleunigung, also schneller. Der Fehler sitzt in der Alltagsbedeutung von „beschleunigen".
>
> **Hier wird angehalten** — nach Abschnitt 2.3 (Richtung der Kraft) und **vor** Abschnitt 3.1
> (Bahnradius). Wer die Radiusformel schon kennt, kann die Frage nicht mehr unbefangen
> beantworten. Die Anhaltefrage lautet:
>
> > *„Das Teilchen läuft eine Sekunde lang im Feld. Ist es danach schneller, langsamer oder gleich
> > schnell? Und woran würdet ihr das im Fadenstrahlrohr sehen?"*
>
> Die zweite Hälfte der Frage ist die wichtige. Sie zwingt von der Formel zur **Beobachtung**:
> Wäre das Teilchen schneller, müsste der Radius wachsen, der Leuchtkreis also eine nach außen
> laufende Spirale sein. Man sieht einen geschlossenen Kreis, und der steht sekundenlang still.
> Das Argument über W = F·s·cos 90° = 0 kommt erst danach — es überzeugt nur den, der die Frage
> schon als Frage empfunden hat. Aufgabe ue9 greift genau dieses Gespräch wieder auf; wer es
> nicht geführt hat, bekommt dort eine Musterlösung ohne vorherige Irritation, und das wirkt
> nicht.
>
> Zwei Anschlussfragen, wenn Zeit ist: *„Wo im Versuch wird das Elektron denn schneller?"*
> (in der Beschleunigungsstrecke, elektrisches Feld) und *„Kennt ihr eine andere Kraft, die
> dauernd wirkt und trotzdem nicht schneller macht?"* (Seil beim Hammerwurf, Gravitation auf der
> Kreisbahn).

Die weiteren Fehler, nach Häufigkeit geordnet:

> **2 — Durchmesser statt Radius.** Der klassische Punktverlust im Fadenstrahlrohr-Versuch.
> Gemessen wird immer der Durchmesser, gerechnet wird immer mit dem Radius. Bei q/m geht der
> Radius **quadratisch** ein, der Fehler wird also zum Faktor 4. Anhalten bei ue5, bevor die
> Klasse rechnet: *„Was steht im Protokoll, und was steht in der Formel?"*
>
> **3 — Das Vorzeichen der Ladung in die Betragsformel eingesetzt.** Ergibt für Elektronen einen
> negativen Radius. Ursache ist meist der Wunsch, das Vorzeichen „irgendwo unterzubringen".
> Gegenmittel ist die Regel aus Abschnitt 0.4, konsequent durchgehalten: **Betrag rechnen,
> Richtung zeichnen.**
>
> **4 — Linke Hand, rechte Hand, Drei-Finger, UVW.** Wer im Unterricht zwei Regeln nebeneinander
> hört, rät im Abitur, welche gemeint war. Das Modul benutzt **ausschließlich die rechte Hand**
> mit der Vorzeichenprüfung (Abschnitt 0.5). Wenn im Kollegium oder im Buch die Linke-Hand-Regel
> steht, das ausdrücklich ansprechen und **eine** Variante zur verbindlichen erklären — nicht
> beide anbieten.
>
> **5 — „r ist proportional zur Masse."** Der Trugschluss in ue7. Er übersieht, dass v selbst
> von m abhängt: Das schwerere Ion ist träger **und** langsamer, und beides zusammen ergibt
> r ∝ √m. Wer linear rechnet, kommt bei Neon auf 9,6 mm statt 4,68 mm. Anhalten vor ue7 mit der
> Frage: *„Beide Ionen bekommen dieselbe Spannung. Sind sie dann auch gleich schnell?"*
>
> **6 — „T hängt doch von v ab, das Teilchen ist schneller."** Wird durch die Simulation
> zuverlässig erledigt, aber nur, wenn Teil A des Beobachtungsauftrags wirklich ausgeführt und
> **notiert** wird. Das bloße Zusehen genügt nicht; die Zahlen müssen nebeneinanderstehen
> (11,91 ns bei 450 V und 11,91 ns bei 1800 V).
>
> **7 — Einheiten.** mT nicht in T, kV nicht in V, cm nicht in m. Das ist kein Verständnisfehler,
> sondern der häufigste Grund für die `weit`-Rückmeldung. Wirksames Gegenmittel: die Angabe
> verlangen, dass in Hilfe 3 jeder Zwischenwert **mit Einheit** notiert wird.
>
> **8 — „Der Filter sortiert nach Masse."** Hartnäckig, weil „Filter" nach Sieb klingt. Die
> Simulation widerlegt es in einem Zug: dieselbe Einstellung lässt Proton und Alphateilchen
> durch. Aufgabe `sim2` sichert das ab.

### 7.4 Differenzierung

> **Nach unten.** Die dreistufigen Hilfen sind so gebaut, dass Stufe 2 die vollständige Rechnung
> noch nicht vorwegnimmt; Schülerinnen und Schüler, die dort einsteigen, rechnen selbst. Für
> deutlich schwächere Lerngruppen ein reduzierter Pflichtteil: **vw1 bis vw3, Abschnitt 2 ganz,
> 3.1 und 3.2, Simulation Modus 1, ue1, ue2, `zuordnung`, ue9.** Das ist eine geschlossene
> Einheit von rund 90 Minuten ohne Filter und Spektrometer.
>
> Zwei Stützen, die sich bewährt haben: Erstens den Maßstabsbalken der Simulation aktiv nutzen —
> den berechneten Radius aus ue1 am Bildschirm **nachmessen** lassen, statt ihn nur zu glauben.
> Zweitens die Aufgabe `zuordnung` in zwei Durchgängen bearbeiten lassen (erst nur Drehsinn, dann
> nur Radius); genau diese Strategie steht in der Rückmeldung bei Teilerfolg.
>
> **Nach oben.** Drei Angebote, die kein neues Material brauchen:
>
> 1. **Aus der Simulation eine Messreihe machen.** Bei festem B fünf Spannungen einstellen, r
>    ablesen, r gegen √U auftragen. Die Steigung ist (1/B)·√(2m/|q|); daraus q/m bestimmen und mit
>    der Anzeige `#aQm` vergleichen. Das ist Abiturniveau der Auswertung und dauert 15 Minuten.
> 2. **Teilaufgabe c) von ue10 vertiefen.** Die relativistische Grenze quantitativ: Ab welcher
>    Energie beträgt der Phasenfehler eine halbe Periode? Warum hilft ein Isochronzyklotron, und
>    welche Voraussetzung repariert es genau?
> 3. **Den Wien-Filter selbst auslegen.** Vorgegeben wird nur die Blendenöffnung; gesucht ist die
>    erreichbare Auflösung ε_max = y_Blende·r/(L·(L/2+D)) und die Frage, ob ein **größeres** oder
>    ein **kleineres** B den Filter schärfer macht. Die Antwort — kleineres B, weil r und damit
>    ε_max mitwächst, allerdings auf Kosten der Baugröße — ist nicht offensichtlich und eine gute
>    Diskussion.
>
> **Für alle sinnvoll:** ue8 im Vergleich besprechen. Es gibt kein richtiges Ja und kein richtiges
> Nein, sondern nur ein begründetes „trennbar, aber ohne Reserve". Zwei bis drei Schülerfassungen
> nebeneinanderlegen und an den Bewertungskriterien prüfen lassen zeigt schneller als jede
> Erklärung, was im AB III erwartet wird.

### 7.5 Bezug zu Realexperimenten

> **Das Fadenstrahlrohr ist das Leitexperiment dieses Moduls.** Wenn eines der Experimente
> gezeigt wird, dann dieses — und zwar **vor** Abschnitt 3, nicht danach.
>
> Aufbau: Glaskolben mit Wasserstoff-Restgas bei etwa 10⁻⁵ bar, Elektronenkanone mit
> Beschleunigungsspannung 150 bis 300 V, außen ein Helmholtz-Spulenpaar. Die Elektronen regen die
> Gasatome an, der Weg wird als schmale leuchtende Bahn sichtbar. Gemessen wird der
> **Durchmesser** mit dem Spiegelmaßstab.
>
> Die Zahlen des Moduls sind mit einer Schulausstattung reproduzierbar. Für ein
> Helmholtz-Spulenpaar mit **N = 130** Windungen je Spule und **R = 0,150 m** Radius gilt
> - `data-tex`: `B = \mu_0 \cdot \left(\dfrac{4}{5}\right)^{3/2} \cdot \dfrac{N \cdot I}{R}`
> - `data-plain`: `B = μ₀ · (4/5)^(3/2) · N · I / R`
>
> Damit liefert I = 2,05 A gerade **B = 1,60 mT** — die Flussdichte aus Aufgabe ue5. Bei
> U = 250 V ergibt sich dort ein Kreisdurchmesser von 6,66 cm, also genau der Messwert der
> Aufgabe (Kontrollrechnung K-31). Die Aufgabe ist damit kein Papierszenario, sondern das
> Protokoll eines Versuchs, den die Klasse selbst durchführen kann. I = 1,0 A ergibt 13,7 cm
> Durchmesser — bequem ablesbar, aber schon nah am Kolbenrand.
>
> **Was am Fadenstrahlrohr didaktisch trägt**, in dieser Reihenfolge:
>
> 1. Der Kreis ist **geschlossen und steht still**. Das ist die Beobachtung gegen die
>    Fehlvorstellung aus 7.3, und sie kostet keine Sekunde Vorbereitung.
> 2. Spannung erhöhen ⟹ Kreis wird größer (r ∝ √U). Vervierfachen der Spannung verdoppelt den
>    Durchmesser — das lässt sich am Maßstab vorführen.
> 3. Spulenstrom erhöhen ⟹ Kreis wird kleiner (r ∝ 1/B). Zwei Regler, zwei verschiedene
>    Wirkungen — genau das übt die Aufgabe `zuordnung`.
> 4. **Polung der Spulen umkehren** ⟹ der Kreis kippt auf die andere Seite. Das ist die
>    Vorzeichenfrage aus Abschnitt 0.5 zum Anfassen und der beste Moment, die Rechte-Hand-Regel
>    an einem echten Aufbau durchzuspielen.
>
> **Weitere Experimente, nach Aufwand geordnet:**
>
> | Experiment | Zeit | Wozu, und an welcher Stelle |
> |---|---|---|
> | Leiterschaukel im Hufeisenmagneten | 5 min | Einstieg zu Abschnitt 2.1: F = B·I·l, Stromrichtung umpolen, Feld umdrehen — die Handregel, bevor sie formalisiert wird |
> | Elektronenstrahl-Ablenkröhre mit Stabmagnet | 5 min | zwischen 2.3 und 2.4: Der Strahl wird abgelenkt, aber nicht heller oder schneller |
> | Braunsche Röhre, Magnet seitlich ans Gehäuse | 2 min | spontan, als Ergänzung — dasselbe Prinzip in einem Alltagsgerät |
> | Nebelkammeraufnahme (Bild oder Video) | 5 min | zu Abschnitt 3.5: entgegengesetzt gekrümmte Spuren von Elektron und Positron, Andersons Befund von 1932 |
> | Massenspektrometer | — | in der Schule nicht durchführbar. Ersatz: Abbildung eines Isotopenspektrums von Neon und die Frage, welche Größe dort auf der Achse steht |
>
> **Ein Hinweis zur Reihenfolge von Experiment und Simulation.** Die Simulation ersetzt das
> Fadenstrahlrohr nicht — sie kann etwas, das der Versuch nicht kann: die **Umlaufdauer** zeigen.
> Am realen Rohr sieht man den Kreis, aber nie das umlaufende Teilchen; T bleibt dort eine reine
> Rechengröße. Deshalb steht das Realexperiment vorn (Beobachtung, Kreis statt Spirale) und die
> Simulation dahinter (Umlaufdauer, Vorzeichenumkehr, Filter). Umgekehrt verliert der Versuch
> seinen Reiz, weil die Klasse das Ergebnis schon kennt.

## 8 · Checkliste der Bausteine

Vollständiges Inventar. Der Bauagent arbeitet diese Liste ab und hakt sie ab; was hier nicht
steht, steht auch nicht in der Datei. Fundstellen sind Abschnittsnummern **dieser** Datei.

### 8.1 Sechs Sections

| `.stufe`-Nr. | `id` | Überschrift | Fundstelle |
|---|---|---|---|
| 1 | `einstieg` | Einstieg | 1 |
| 2 | `grundlagen` | Von der Kraft auf den Leiter zur Kraft auf ein Teilchen | 2 |
| 3 | `vertiefung` | Die Kreisbahn — und was man aus ihr herausliest | 3 |
| 4 | `simulation` | Teilchen im Feld — Kreisbahn und Geschwindigkeitsfilter | 4 |
| 5 | `uebungen` | Übungen — vom Einsetzen zum Beurteilen | 5 |
| 6 | `abschluss` | Zusammenfassung und Selbstcheck | 6 |

Seitenkopf: Titel *Magnetisches Feld und Lorentzkraft*, Untertitel *Von der Kraft auf den Leiter
zur Kreisbahn des einzelnen Teilchens*, Chips **Physik LK · Q1**, **Ladungen, Felder und
Induktion**, **ca. 135 Minuten** (7.2).

### 8.2 Multiple-Choice-Aufgaben — fünf Stück

Alle mit `data-mc="<schlüssel>"`, `name="<schlüssel>"` an den Radios, `data-i` an den Optionen,
`<div class="rueck"></div>` am Ende. `fb` hat immer genau so viele Einträge wie es Optionen gibt.

| Schlüssel | Optionen | richtig (`r`) | Anforderungsbereich | Fundstelle |
|---|---|---|---|---|
| `vw1` | 3 | **0** | Vorwissen (Sek I) | 1.2 |
| `vw2` | 3 | **1** | Vorwissen (Sek I / EF) | 1.2 |
| `vw3` | 3 | **0** | Vorwissen (EF) | 1.2 |
| `sim1` | 3 | **0** | II | 4.10 |
| `sim2` | 3 | **1** | II | 4.10 |

Summe: 5 Aufgaben, 15 Optionen, 15 Rückmeldetexte. Kein Text lautet „Leider falsch"; jeder
Distraktor benennt seinen Denkfehler.

### 8.3 Zahleneingaben — sechs Stück

Alle mit `data-num="<schlüssel>"`, Eingabefeld `type="number"`, `<select>` mit der
Einheitenliste, erster Eintrag `Einheit…` (leer). Die **fett** gesetzte Einheit ist die
fachlich falsche Distraktoreinheit.

| Schlüssel | Sollwert | Einheit | `tol` | `alt` | Einheitenliste | Fundstelle |
|---|---|---|---|---|---|---|
| `ue1` | 3,55 | cm | 0,06 | 35,5 mm | mm · cm · m · **m/s** | 5.1 |
| `ue2` | 504,6 | ns | 6 | 0,5046 µs | ns · µs · ms · **MHz** | 5.2 |
| `ue3` | 13297 | km/s | 200 | 1,3297 · 10⁷ m/s | km/s · m/s · cm/s · **m/s²** | 5.3 |
| `ue5` | 1,761 · 10¹¹ | C/kg | 4 · 10⁹ | — | C/kg · **kg/C** · **C** · **N/kg** | 5.5 |
| `ue6` | 58,7 | kV/m | 0,8 | 58723 V/m | kV/m · V/m · **V** · **T** | 5.6 |
| `ue7` | 4,68 | mm | 0,15 | 0,468 cm | mm · cm · m · **mm²** | 5.7 |

Jede der sechs hat genau vier Rückmeldetexte: `ok` · `falschEinheit` · `nah` · `weit`.
Summe: 24 Rückmeldetexte. `ue5` hat als einzige **kein** `alt` — die alternative Einheit wäre
der Kehrwert und damit fachlich falsch.

### 8.4 Zuordnung — eine

| Schlüssel | Zeilen | Auswahlwerte je Zeile | Lösungsfolge (`data-loesung` in Markup-Reihenfolge) | Fundstelle |
|---|---|---|---|---|
| `zuordnung` | 4 | `…` (leer) · A · B · C · D | **B – C – D – A** | 5.4 |

Dazu vier Inline-SVG in `<div class="diagramme">`, je `viewBox="0 0 260 220"`:

| Bild | Bogenradius | Krümmung / Umlauf | Feldsymbole |
|---|---|---|---|
| A | 60 px | nach oben, gegen den Uhrzeigersinn | ⊗ |
| B | 60 px | nach unten, im Uhrzeigersinn | ⊗ |
| C | 120 px | nach unten, im Uhrzeigersinn | ⊗ |
| D | 30 px | nach oben, gegen den Uhrzeigersinn | ⊗ |

Prüfknopf `<button class="primaer" data-check="zuordnung">Prüfen</button>` in einer
`<div class="knopfleiste">`. Es ist die einzige Zuordnungsaufgabe des Moduls.

### 8.5 Offene Aufgaben — drei

Kein Eingabefeld, kein Ergebnis im Export. Jeweils ein
`<button data-loesung="<schlüssel>">Musterlösung</button>` und ein zugehöriger
`<div class="hilfe-text" data-stufe="9">`, der die erwartete Argumentation **und** die
Bewertungskriterien enthält.

| Schlüssel | `data-stufe` | Anforderungsbereich | Thema | Fundstelle |
|---|---|---|---|---|
| `ue8` | `9` | III | Beurteilung: Trennt der Streifendetektor Ne-20 von Ne-22? | 5.8 |
| `ue9` | `9` | III | Bewertung der Schüleraussage „beschleunigt heißt schneller" | 5.9 |
| `ue10` | `9` | III | Begründung T ≠ f(v), Zyklotron, relativistische Grenze (a/b/c) | 5.10 |

`ue8` trägt die Überschrift *Fortsetzung von Aufgabe 7* und steht unmittelbar unter `ue7`.

### 8.6 Dreistufige Hilfen

Sechs Aufgaben mit vollständigem Hilfesystem (`data-hilfe`, Stufen 1 · 2 · 3):
`ue1` · `ue2` · `ue3` · `ue5` · `ue6` · `ue7` — das sind 18 Hilfetexte.
Rollen strikt getrennt: Stufe 1 eine Zeile ohne Formel, Stufe 2 Formel und Weg ohne Zahlen,
Stufe 3 vollständige Rechnung mit Zwischenschritten und Einheitenprobe.

`zuordnung` hat statt der Hilfen eine **Rückmeldung bei Teilerfolg** (5.4), die offenen Aufgaben
`ue8` bis `ue10` haben statt der Hilfen die Musterlösung auf `data-stufe="9"`.

### 8.7 Namensliste für den Export

`var namen = {…}` am Skriptende. Reihenfolge = Reihenfolge auf der Seite. Nur Aufgaben mit
auswertbarem Ergebnis stehen darin; die offenen Aufgaben `ue8`, `ue9`, `ue10` **nicht**.

```js
var namen = {
  vw1:"Vorwissen 1 (Feldlinien)",
  vw2:"Vorwissen 2 (Kraft auf den Leiter)",
  vw3:"Vorwissen 3 (Plattenkondensator)",
  sim1:"Simulation 1 (Umlaufdauer)",
  sim2:"Simulation 2 (Geschwindigkeitsfilter)",
  ue1:"Aufgabe 1 (Bahnradius)",
  ue2:"Aufgabe 2 (Umlaufdauer)",
  ue3:"Aufgabe 3 (Geschwindigkeit aus der Bahn)",
  zuordnung:"Aufgabe 4 (Zuordnung der Bahnen)",
  ue5:"Aufgabe 5 (spezifische Ladung)",
  ue6:"Aufgabe 6 (Wien-Filter)",
  ue7:"Aufgabe 7 (Neon-Isotope)"
};
```

Zwölf Einträge. Kopfzeile des Exports: `"Magnetisches Feld und Lorentzkraft – Physik LK Q1"`.

### 8.8 Canvas

Genau **ein** Canvas für beide Modi.

| ID | `width` | `height` | Maßstab | Inhalt |
|---|---|---|---|---|
| `cvSim` | `1000` | `640` | `SKALA = 4,00 · 10⁻⁴` m/px, also 1 cm = 25 px | Modus 1 Kreisbahn (4.5), Modus 2 Wien-Filter (4.7) |

CSS: `width:100%`, interne Maße fest. Realer Bildausschnitt 40,0 cm × 25,6 cm (K-7).
Pflichtelement im Bild: Maßstabsbalken unten links, 125 px lang, Beschriftung „5 cm",
Farbe `#64748b`.

Feste Punkte in Canvas-Koordinaten:

| Punkt | Modus 1 | Modus 2 |
|---|---|---|
| Quell-/Eintrittspunkt | `(500; 320)` | `(100; 320)` |
| Platten | — | oben y = 295, unten y = 345, x = 100 … 350 |
| Schirm | — | x = 930, Blende y = 310 … 330 |

### 8.9 Bedienelemente

**Regler** (`<input type="range">` in `.regler`):

| ID | Größe | min | max | step | value | Wertanzeige |
|---|---|---|---|---|---|---|
| `rU` | Beschleunigungsspannung U | 200 | 1800 | 10 | 450 | `lU` |
| `rB` | Flussdichte B | teilchenabhängig (4.4) | | | | `lB` |
| `rUP` | Plattenspannung U_P (nur Modus 2) | 0 | 4000 | 2 | 754 | `lUP` |

Die vier Belegungen des B-Reglers (min / max / step / value in mT):
Elektron **2,5 / 7,0 / 0,1 / 3,0** · Proton **110 / 300 / 5 / 130** ·
Alphateilchen **150 / 420 / 5 / 185** · Ne-20-Ion **480 / 1300 / 10 / 580**.
Alle vier Startwerte liegen auf dem Raster (K-14).

**Weitere Bedienelemente:**

| ID | Art | Wirkung |
|---|---|---|
| `selTeilchen` | `<select>`, 4 Optionen: `elektron` · `proton` · `alpha` · `neon` | Teilchenart (4.3) |
| `selVorzeichen` | `<select>`, 2 Optionen: `negativ` · `positiv` | Vorzeichen von q (4.4) |
| `modKreis` | `<input type="radio" name="modus">` | Modus 1 Kreisbahn (Vorauswahl) |
| `modWien` | `<input type="radio" name="modus">` | Modus 2 Wien-Filter |
| `bStart` | `<button class="primaer">` | Start / Pause |
| `bReset` | `<button>` | Teilchen zurücksetzen, Regler bleiben |
| `bExport` | `<button class="primaer">` | Ergebnis in die Zwischenablage (8.7) |

**Anzeigefelder** (`.anzeige`):

| ID | beide Modi | nur Modus 2 | Einheit und Stellen |
|---|---|---|---|
| `aTeilchen` | × | | Text |
| `aV` | × | | km/s, 1 NKS |
| `aR` | Modus 1 | | cm, 2 NKS |
| `aT` | Modus 1 | | ns 2 NKS / µs 3 NKS |
| `aF` | Modus 1 | | MHz 2 NKS / kHz 1 NKS |
| `aQm` | × | | C/kg, Form `4,82 · 10⁷` |
| `aVc` | × | | Fußzeile v/c in %, 2 NKS |
| `aE` | | × | kV/m, 2 NKS |
| `aVd` | | × | km/s, 1 NKS |
| `aEps` | | × | %, 3 NKS, mit Vorzeichen |
| `aY` | | × | mm, 2 NKS, mit Vorzeichen |
| `aStatus` | | × | Text, drei Zustände (4.7) |

### 8.10 Weitere Bausteine

| Baustein | Anzahl | Fundstelle |
|---|---|---|
| `.merksatz` mit `<b>Kernaussage</b>` | 5 | Merksatz 1 in 2.3 · Merksatz 2 in 2.4 · Merksatz 4 in 3.2 · Merksatz 5 in 3.3 · Merksatz 6 in 3.5 |
| Merksatz 3 als Abgrenzungstabelle E-Feld / B-Feld (kein `.merksatz`, sondern `.tabelle`) | 1 | 2.4 |
| `<details>` im Fließtext | 3 | 2.2 („Herleitung: von F = B·I·l zur Lorentzkraft") · 3.1 („Wie kommt v ins Spiel?") · 3.2 („Das Zyklotron — und wo seine Grenze liegt") |
| `<details class="lehrer">` | 1 | 7 |
| `.auftrag` (Beobachtungsauftrag, Teile A/B/C) | 1 | 4.9 |
| `.hinweis` (Blick aufs Zentralabitur) | 1 | 6.2 |
| Inline-SVG außerhalb der Zuordnung | 2 | 2.3 (Standardsituation ±q) · 3.3 (Aufbau Wien-Filter) |
| Inline-SVG der Zuordnung | 4 | 5.4 |
| `.check`-Sätze im Selbstcheck | 6 | 6.3 |
| `.tabelle`-Wrapper um `<table>` | jede Tabelle | Vorgabe `bausteine.md` |

### 8.11 Auffälligkeiten

Beim Durchgehen der Abschnitte 0 bis 7 gefunden. **Nichts davon wurde stillschweigend geändert**
— die Abschnitte 0 bis 5 sind abgenommen und stehen unverändert.

1. **`#aF`: Obergrenze der Zyklotronfrequenz.** Abschnitt 4.6 gibt den Bereich mit
   „0,37 MHz … 196,08 MHz" an. Nachgerechnet ergibt der kleinste Wert von T
   (Elektron, B = 7,0 mT: T = 5,1034 ns) die Frequenz **195,95 MHz**, nicht 196,08 MHz
   (Abweichung 0,07 %, Kontrollrechnung K-15). Der Untergrenzwert 0,37 MHz stimmt. Vorschlag:
   in 4.6 „196,08" durch „195,95" ersetzen. Betrifft nur die Bereichsangabe im Fließtext, keine
   Rechnung der Simulation.

2. **ε_max ist nicht über alle Reglerstellungen nahezu konstant.** Abschnitt 4.7 schreibt:
   „ε_max = 0,26 % bis 0,34 % — über alle Teilchen und alle Reglerstellungen nahezu gleich".
   Wegen ε_max = y_Blende·r/(L·(L/2+D)) ist ε_max **proportional zu r**, und r läuft über die
   Regler von 0,68 cm bis 5,76 cm. Nachgerechnet (K-17): über alle Reglerstellungen von
   **0,097 % bis 0,817 %**. Nahezu gleich ist ε_max nur beim Vergleich der **vier Teilchenarten
   bei ihren Startwerten** — dort 0,331 % bis 0,338 %, und das ist offensichtlich der Ursprung
   der Angabe. Der Startwert 0,338 % und das U_P-Fenster ± 2,55 V sind **richtig** und werden
   bestätigt. Vorschlag: den Satzteil „und alle Reglerstellungen" streichen und auf „bei den
   Startwerten der vier Teilchenarten" ändern.

3. **Canvas-ID fehlt.** Abschnitt 4 legt Breite (1000), Höhe (640) und Maßstab fest, nennt aber
   keine `id`. In 8.8 ist **`cvSim`** eingetragen, passend zum Referenzmodul
   (`module/physik-q1-induktion.html` benutzt `cvSim`, `cvPhi`, `cvU`). Wenn ein anderer Name
   gewünscht ist, gehört er nach 4.5.

4. **Drei IDs waren nicht vergeben** und sind in 8.9 ergänzt worden, weil das Markup sie braucht:
   die Wertanzeigen der drei Regler (`lU`, `lB`, `lUP`, analog zu `lV`/`lB` im Referenzmodul)
   und die v/c-Fußzeile (`aVc`, in 4.6 beschrieben, aber ohne ID).

5. **Zwei Werte für die Alphamasse.** Abschnitt 4.1 setzt
   `M_ALPHA = 6.6446573357e-27`, die von der Projektleitung gelieferte Konstantenliste nennt
   6,6446573450 · 10⁻²⁷ kg. Der relative Unterschied beträgt 1,4 · 10⁻⁹ und ist für jede Zahl
   dieses Moduls belanglos — alle Kontrollrechnungen sind mit dem Wert aus 4.1 gerechnet und
   stimmen mit den ausgewiesenen Stellen überein. Zur Vermeidung späterer Rückfragen: **der Wert
   in 4.1 gilt.**

6. **Keine doppelt vergebenen Schlüssel.** Geprüft wurden alle zwölf Schlüssel aus 8.7 sowie
   `ue8`, `ue9`, `ue10`. Jeder Schlüssel kommt genau einmal als `data-mc`, `data-num`,
   `data-check` oder `data-loesung` vor. Die Nummerierung springt bewusst von `ue3` zu `ue5` —
   an vierter Stelle steht `zuordnung`, das im Aufgabentext als „Aufgabe 4" geführt wird
   (siehe Namensliste 8.7). Das ist kein Fehler, aber der Bauagent soll nicht nach einem
   fehlenden `ue4` suchen.

7. **Startwert des U_P-Reglers.** 4.4 nennt 754 V. Exakt wäre 754,89 V (K-12); 754 V ist der
   nächstniedrige Rasterwert bei Schrittweite 2 V und liegt damit **innerhalb** des
   Durchlassfensters von ± 2,55 V. Der Filter steht beim Laden der Seite also bereits auf
   „kommt durch". Das ist beabsichtigt und wird hier nur festgehalten, damit der Bauagent den
   Wert nicht „korrigiert".

## 9 · Kontrollrechnungen

### K-7 bis K-21 und K-31 (Abschnitte 4, 6, 7 und 8)

Prüfskripte: `scratchpad/vorarbeit/physik/abschnitte_4_8.py` und
`scratchpad/vorarbeit/physik/nachtrag_4_8.py`,
Ausgabe beider: `scratchpad/vorarbeit/physik/ausgabe_abschnitte_4_8.txt`.
Konstanten wie in Abschnitt 4.1 (CODATA 2018): e = 1,602176634 · 10⁻¹⁹ C ·
m_e = 9,1093837015 · 10⁻³¹ kg · m_p = 1,67262192369 · 10⁻²⁷ kg ·
m_α = 6,6446573357 · 10⁻²⁷ kg · u = 1,66053906660 · 10⁻²⁷ kg · c = 2,99792458 · 10⁸ m/s ·
μ₀ = 4π · 10⁻⁷ T·m/A. Verwendete Beziehungen durchgehend
v = √(2·|q|·U/m) · r = m·v/(|q|·B) · T = 2π·m/(|q|·B).
Die Kontrollrechnungen K-22 bis K-30 zu Abschnitt 5 stehen in 5.11 und werden hier nicht
wiederholt.

---

**K-7 — Maßstab und Bildausschnitt (Abschnitt 4.2)**
SKALA = 4,00 · 10⁻⁴ m/px auf einer Leinwand von 1000 × 640 px:
Breite 1000 · 4,00·10⁻⁴ m = 0,4000 m = **40,0 cm**, Höhe 640 · 4,00·10⁻⁴ m = 0,2560 m =
**25,6 cm**. ✓ (Angabe in 4.2: 40,0 cm × 25,6 cm)
Umrechnung 1 cm = 0,01 m / 4,00·10⁻⁴ m/px = **25,0 px**. ✓
Maßstabsbalken 125 px · 4,00·10⁻⁴ m/px = **0,0500 m = 5 cm**. ✓ Die Beschriftung „5 cm" ist
damit korrekt, der Balken ist genau fünf Zentimeter im Bildmaßstab.

---

**K-8 — Bleiben alle Bahnen im Bild? (Abschnitt 4.8)**
Alle 16 Kombinationen aus B min / B max × U min / U max × vier Teilchenarten, r in px = r/SKALA:

| Teilchen | B | U = 200 V | | U = 1800 V | |
|---|---|---|---|---|---|
| | | r in cm | r in px | r in cm | r in px |
| Elektron | 2,5 mT | 1,9076 | 47,69 | 5,7227 | 143,07 |
| Elektron | 7,0 mT | 0,6813 | 17,03 | 2,0438 | 51,10 |
| Proton | 110 mT | 1,8577 | 46,44 | 5,5732 | 139,33 |
| Proton | 300 mT | 0,6812 | 17,03 | 2,0435 | 51,09 |
| Alphateilchen | 150 mT | 1,9200 | 48,00 | 5,7600 | 144,00 |
| Alphateilchen | 420 mT | 0,6857 | 17,14 | 2,0572 | 51,43 |
| Ne-20-Ion | 480 mT | 1,8970 | 47,43 | 5,6911 | 142,28 |
| Ne-20-Ion | 1300 mT | 0,7004 | 17,51 | 2,1013 | 52,53 |

Kleinster Radius **17,03 px** (Proton bei 300 mT / 200 V), größter **144,00 px**
(Alphateilchen bei 150 mT / 1800 V). Beide liegen im Fenster 16 … 150 px. ✓
Größter Bahndurchmesser 2 · 144,00 px = **288,0 px**; der Quellpunkt liegt bei y = 320 px,
bis zum Rand sind es 320 px, also bleiben 320 − 288 = **32 px Luft**. ✓ Beide Angaben aus 4.8
bestätigt.

---

**K-9 — Zeitlupenfaktoren und Bildschirm-Umlaufdauern (Abschnitt 4.5)**
Bildschirm-Umlaufdauer = T · Z, mit T = 2π·m/(|q|·B):

| Teilchen | Z | B min | Startwert | B max |
|---|---|---|---|---|
| Elektron / Positron | 2,0 · 10⁸ | 2,86 s | 2,38 s | 1,02 s |
| Proton | 5,0 · 10⁶ | 2,98 s | 2,52 s | 1,09 s |
| Alphateilchen | 5,0 · 10⁶ | 4,34 s | 3,52 s | 1,55 s |
| Ne-20-Ion | 1,0 · 10⁶ | 2,71 s | 2,25 s | 1,00 s |

Alle zwölf Werte stimmen mit der Tabelle in 4.5 überein. ✓
Reale Umlaufdauern: kleinste **5,1034 ns** (Elektron, 7,0 mT), größte **2713,36 ns = 2,7134 µs**
(Ne-20-Ion, 480 mT). Angabe in 4.5 („zwischen 5,10 ns und 2713 ns"). ✓
Der Startwert des Alphateilchens ist **185 mT** (nicht 180 mT); nur damit ergibt sich die in
4.5 genannte Bildschirm-Umlaufdauer von 3,52 s. Gegenprobe: T(150 mT)·150/185 · Z = 3,521 s. ✓

---

**K-10 — Beobachtungsauftrag Teile A und B (Abschnitt 4.9)**
Elektron, B = 3,00 mT:

| U | v in km/s | r in cm | T in ns | f_c in MHz |
|---|---|---|---|---|
| 450 V | 12 581,5 | 2,3845 | 11,9080 | 83,977 |
| 1800 V | 25 163,0 | 4,7689 | 11,9080 | 83,977 |

Faktoren beim Vervierfachen von U: v · **2,000000**, r · **2,000000**, T · **1,000000**.
Das ist die geforderte Antwort auf Teil A: v verdoppelt sich (v ∝ √U), r verdoppelt sich
(r ∝ v), T bleibt unverändert (T = 2π·m/(|q|·B) enthält weder v noch U). ✓

Teil B, U = 450 V, B von 3,00 mT auf 6,00 mT verdoppelt:
v = 12 581,5 km/s **unverändert** (v hängt nur von U ab), r = **1,1922 cm**, also Faktor
**0,500000**, T = **5,9540 ns**, ebenfalls Faktor **0,500000**, f_c = 167,955 MHz.
Das ist der Unterschied, auf den Teil B zielt: U wirkt nur auf r, B wirkt auf r **und** auf T. ✓

---

**K-11 — Spezifische Ladungen der Auswahlliste (Abschnitt 4.3)**

| Teilchen | |q|/m gerechnet | Angabe in 4.3 |
|---|---|---|
| Elektron / Positron | 1,758820 · 10¹¹ C/kg | 1,759 · 10¹¹ ✓ |
| Proton | 9,578833 · 10⁷ C/kg | 9,579 · 10⁷ ✓ |
| Alphateilchen | 4,822451 · 10⁷ C/kg | 4,822 · 10⁷ ✓ |
| Ne-20-Ion | 4,824267 · 10⁶ C/kg | 4,824 · 10⁶ ✓ |

Masse des Ne-20-Ions: 20,0 · 1,66053906660 · 10⁻²⁷ kg = **3,3210781332 · 10⁻²⁶ kg**,
identisch mit der Angabe in 4.3. ✓
Nebenbefund für die Aussage in 4.4 („rund 190-mal stärkeres Feld"): Bei gleichem U und gleichem
r verhalten sich die nötigen Flussdichten wie √(m/|q|); für Ne-20 gegen Elektron ist
√((3,32108·10⁻²⁶/1,602177·10⁻¹⁹)/(9,109384·10⁻³¹/1,602177·10⁻¹⁹)) = √(3,6457·10⁴) = **190,9**. ✓

---

**K-12 — Startanzeige der Simulation (Abschnitte 4.4 und 4.6)**
Elektron, U = 450 V, B = 3,00 mT, q = −e:
v = **1,258149 · 10⁷ m/s = 12 581,5 km/s** · r = **2,384456 · 10⁻² m = 2,3845 cm** ·
T = **1,190796 · 10⁻⁸ s = 11,91 ns** · f_c = **83,98 MHz** · |q|/m = 1,76 · 10¹¹ C/kg ·
v/c = **4,1967 % ⟹ Anzeige „4,20 %"**. ✓ (Angabe in 4.6: v/c = 4,20 % bei den Startwerten)
Zugehörige Durchlassspannung des Filters: U_P = v · B · d = 1,258149·10⁷ · 3,00·10⁻³ · 0,0200 V
= **754,89 V**. Der Reglerstartwert 754 V liegt 0,89 V darunter, das Durchlassfenster ist
± 2,55 V (K-17) — der Filter steht beim Laden also auf „kommt durch". ✓

---

**K-13 und K-14 — Rasterprobe aller Regler (Abschnitt 4.4)**
Geprüft wird, ob (max − min)/step und (value − min)/step ganze Zahlen sind:

| Regler | (max − min)/step | (value − min)/step |
|---|---|---|
| `rU` (200 … 1800 V, 10 V) | 160 | 25 |
| `rB` Elektron (2,5 … 7,0 mT, 0,1 mT) | **45** | 5 |
| `rB` Proton (110 … 300 mT, 5 mT) | **38** | 4 |
| `rB` Alphateilchen (150 … 420 mT, 5 mT) | **54** | 7 |
| `rB` Ne-20-Ion (480 … 1300 mT, 10 mT) | **82** | 10 |
| `rUP` (0 … 4000 V, 2 V) | 2000 | 377 |

Alle acht Werte sind ganzzahlig; die Schrittzahlen 45, 38, 54 und 82 stimmen mit der Tabelle in
4.4 überein, und jeder Startwert liegt exakt auf dem Raster. ✓ Kein Regler springt beim ersten
Anfassen auf einen anderen Wert.

---

**K-15 — Anzeigebereiche und Rundungsstellen (Abschnitt 4.6)**
Extremwerte über alle Teilchen und alle Reglerstellungen:

| Anzeige | gerechneter Bereich | Angabe in 4.6 |
|---|---|---|
| `aV` Geschwindigkeit | 43,9 … 25 163,0 km/s | 43,9 … 25 163,0 km/s ✓ |
| `aR` Bahnradius | 0,68 … 5,76 cm | 0,68 … 5,76 cm ✓ |
| `aT` Umlaufdauer | 5,10 ns … 2,713 µs | 5,10 ns … 2,713 µs ✓ |
| `aF` Zyklotronfrequenz | 0,37 … **195,95 MHz** | 0,37 … 196,08 MHz ✗ |
| `aQm` spezifische Ladung | 4,824267 · 10⁶ … 1,758820 · 10¹¹ C/kg | 4,824 · 10⁶ … 1,759 · 10¹¹ ✓ |

**Eine Abweichung.** Die Obergrenze von `aF` ergibt sich aus der kleinsten Umlaufdauer:
f_c = 1/T = 1/5,1034 · 10⁻⁹ s = **1,9595 · 10⁸ Hz = 195,95 MHz**, nicht 196,08 MHz. Die
Abweichung beträgt 0,07 % und betrifft ausschließlich die Bereichsangabe im erläuternden Text,
nicht die Rechnung der Simulation. Eingetragen als Auffälligkeit 1 in 8.11.

Die gewählten Rundungsstellen tragen über den ganzen Bereich: v mit 1 NKS unterscheidet noch
43,9 von 44,0 km/s; r mit 2 NKS löst 0,68 cm noch in Hundertstel auf; die Umschaltung von ns auf
µs bei 1000 ns liegt zwischen den Extremwerten 5,10 ns und 2713 ns, wird also tatsächlich
benutzt; die Umschaltung von MHz auf kHz bei 1 MHz ebenso (0,37 MHz = 370 kHz). ✓

---

**K-16 — Das Verhältnis v/c (Abschnitt 4.6)**
Größte Geschwindigkeit über alle Regler: Elektron bei U = 1800 V,
v = **2,516297 · 10⁷ m/s**, also v/c = **8,3935 % ⟹ Anzeige „8,393 %"**. ✓ (Angabe in 4.6:
größter Wert 8,393 %)
Bei den Startwerten v/c = 4,1967 %. ✓
Die Schwelle für die orange Einfärbung liegt bei 8 %; sie wird nur vom Elektron und nur oberhalb
von U = 1635 V erreicht (v/c = 8 % ⟹ U = m_e·c²·0,08²/(2e) = 1635,2 V). Alle anderen Teilchen
bleiben über den ganzen Reglerbereich unter 0,1 % von c. Der relativistische Fehler in E_kin
beträgt bei 8,4 % von c rund 0,53 % — die klassische Rechnung ist zulässig, und der Hinweistext
„über 10 % müsste relativistisch gerechnet werden" ist als Einordnung richtig. ✓

---

**K-17 — Auflösung des Wien-Filters (Abschnitt 4.7)**
Herleitung der Formel: Mit y = (q/m)·B·(v − v_d)·L·(L/2 + D)/v² und ε = (v_d − v)/v folgt
|y| = ε · L·(L/2 + D) · (|q|·B)/(m·v) = ε · L·(L/2 + D)/r, also

> ε_max = y_Blende · r / (L · (L/2 + D)).

Mit y_Blende = 4,0 mm und L·(L/2 + D) = 0,02820 m² (K-18) ergibt sich bei den Startwerten
U = 450 V und der jeweiligen Start-Flussdichte:

| Teilchen | r bei Startwerten | ε_max | U_P-Fenster |
|---|---|---|---|
| Elektron | 2,3845 cm | **0,3382 %** | ± 2,553 V |
| Proton | 2,3579 cm | 0,3345 % | ± 2,553 V |
| Alphateilchen | 2,3352 cm | 0,3312 % | ± 2,553 V |
| Ne-20-Ion | 2,3549 cm | 0,3340 % | ± 2,553 V |

Der in 4.7 genannte Startwert **0,338 %** und das Fenster **± 2,55 V** sind damit bestätigt. ✓
Dass das U_P-Fenster für alle vier Teilchen dieselbe Breite hat, ist kein Zufall: Aus
ΔU_P = ε_max · v · B · d und ε_max = y_Blende·r/(L(L/2+D)) mit r = m·v/(|q|B) folgt
ΔU_P = y_Blende · d · m · v²/(|q| · L(L/2+D)) = y_Blende · d · 2U/(L(L/2+D)) — es hängt nur von
der Beschleunigungsspannung ab, nicht von Teilchen und nicht von B.
ΔU_P = 0,0040 m · 0,0200 m · 2 · 450 V / 0,02820 m² = **2,553 V**. ✓

**Eine Abweichung.** Die Angabe in 4.7, ε_max liege „über alle Teilchen und alle
Reglerstellungen" zwischen 0,26 % und 0,34 %, trifft nicht zu: ε_max ist proportional zu r, und
r läuft über die Regler von 0,68 cm bis 5,76 cm (K-8). Nachgerechnet ergibt sich über alle
Reglerstellungen ein Bereich von **0,097 % bis 0,817 %**. Nahezu konstant ist ε_max nur beim
Vergleich der vier Teilchenarten **bei ihren Startwerten**, dort 0,331 % … 0,338 %. Eingetragen
als Auffälligkeit 2 in 8.11.

---

**K-18 — Geometrie des Wien-Filters (Abschnitt 4.7)**
Umrechnung der Canvas-Maße mit SKALA = 4,00 · 10⁻⁴ m/px:

| Größe | Canvas | real | Angabe in 4.7 |
|---|---|---|---|
| Plattenlänge L | 350 − 100 = 250 px | 0,1000 m | L = 0,100 m ✓ |
| Plattenabstand d | 345 − 295 = 50 px | 0,0200 m | d = 0,020 m ✓ |
| Driftstrecke D | 930 − 350 = 580 px | 0,2320 m | D = 0,232 m ✓ |
| halbe Blendenöffnung | 10 px | 0,0040 m | 4,0 mm ✓ |

Hebelarm L · (L/2 + D) = 0,1000 m · (0,0500 m + 0,2320 m) = 0,1000 m · 0,2820 m =
**0,02820 m²**. ✓ (Angabe in 4.7)

---

**K-19 — Nötige Feldstärke und Reichweite des U_P-Reglers (Abschnitt 4.7)**
Für ε = 0 muss E = v · B eingestellt werden. Über alle Teilchen und alle Reglerstellungen:

- kleinster Wert **20,83 kV/m** — Alphateilchen bei U = 200 V und B = 150 mT
- größter Wert **176,17 kV/m** — Proton bei U = 1800 V und B = 300 mT

Beides deckt sich mit der Bereichsangabe „20,83 … 176,17 kV/m" in 4.7. ✓
Reicht der U_P-Regler? U_P = E · d = 176,17 · 10³ V/m · 0,0200 m = **3523,4 V**, das liegt unter
dem Reglermaximum von 4000 V. ✓ Der Filter lässt sich also für **jede** Reglerstellung des
Modus 2 auf Durchlass einstellen — der Beobachtungsauftrag kann an keiner Stelle in eine
Sackgasse laufen.

---

**K-20 — Neon mit 20,0 u statt exakter Isotopenmasse (Abschnitte 4.3 und 5.7)**
Rechenmasse 20,0 u = 3,3210781332 · 10⁻²⁶ kg, exakte Isotopenmasse 19,99244 u =
3,3198228 · 10⁻²⁶ kg. Relativer Unterschied **0,0378 %**; auf den Radius wirkt die halbe
relative Abweichung (r ∝ √m), also **0,0189 %**. Bei einem Bahnradius von 4,8 cm sind das
9,1 µm — das liegt weit unter jeder Ablesegenauigkeit und unter der Anzeigegenauigkeit von
2 Nachkommastellen in Zentimetern. Die Vereinfachung ist zulässig, und der Fußnotenhinweis unter
der Simulation ist damit sachlich begründet. ✓ (Vergleiche K-5 und K-27, wo dasselbe für den
Isotopenabstand gezeigt wird.)

---

**K-21 — Ablenkung am Schirm, Teil C des Beobachtungsauftrags (Abschnitte 4.7 und 4.9)**
Kontrollformel y = (q/m) · B · (v − v_d) · L·(L/2 + D)/v², positives y = Ablenkung nach oben.
Filtereinstellung durchgehend B = 200 mT und U_P = 1174 V, also v_d = U_P/(d·B) =
1174 V/(0,0200 m · 0,200 T) = **293 500 m/s = 293,5 km/s**:

| Fall | v | ε = (v_d − v)/v | y am Schirm | Status |
|---|---|---|---|---|
| Proton, U = 450 V | 293,6 km/s | **−0,0390 %** | **+0,718 mm** | kommt durch |
| Alphateilchen, U = 890 V | 293,0 km/s | **+0,1761 %** | **−1,635 mm** | kommt durch |
| Alphateilchen, U = 450 V | 208,3 km/s | **+40,881 %** | −533,7 mm (rechnerisch) | von der Platte verschluckt |

Alle Werte aus 4.9 bestätigt: −0,039 % und +0,72 mm für das Proton, +0,176 % und −1,64 mm für
das Alphateilchen bei 890 V, +40,9 % bei 450 V. ✓
Der dritte Fall zeigt, warum die Statusanzeige nötig ist: Die Kontrollformel liefert dort
−533,7 mm, während der Plattenabstand nur ± 10 mm zulässt. Das Teilchen erreicht den Schirm gar
nicht, sondern trifft nach kurzer Strecke die untere Platte; die integrierte Bahn bricht dort ab,
und der Text lautet „von der Platte verschluckt". Die Kontrollformel gilt ausdrücklich nur im
Bereich |y_Schirm| ≤ 2 cm (Abnahmeprobe in 4.7). ✓

Zwei Nebenrechnungen zur Genauigkeit der im Auftrag genannten Spannungen:
- exakter Durchlasswert für das Proton bei 450 V: U_P = v·B·d = **1174,46 V**; der genannte
  Wert 1174 V weicht um 0,46 V ab und liegt damit innerhalb des Fensters ± 2,55 V (K-17). ✓
- die Spannung, bei der das Alphateilchen **exakt** die Protonengeschwindigkeit erreicht, ist
  U = m_α·v_p²/(2·2e) = **893,8 V**. Der im Auftrag genannte Wert 890 V ergibt eine Abweichung
  von 0,176 % und damit y = −1,635 mm — betragsmäßig unter der halben Blendenöffnung von
  4,0 mm, das Alphateilchen kommt also durch. ✓ Genau diese 0,18 % Abweichung wird in der
  Rückmeldung zu `sim2` genannt („293,6 km/s gegen 293,0 km/s — Abweichung 0,18 %"). ✓

---

**K-31 — Helmholtz-Spulenpaar für den Realversuch (Abschnitt 7.5)**
Für ein Spulenpaar im Helmholtz-Abstand gilt auf der Achse

> B = μ₀ · (4/5)^(3/2) · N · I / R,

mit N Windungen je Spule und R als Spulen- und zugleich Abstandsradius. Für eine typische
Schulausstattung N = 130 und R = 0,150 m:

| I | B | 2r beim Elektron bei U = 250 V |
|---|---|---|
| 0,5 A | 0,3896 mT | 27,37 cm |
| 1,0 A | 0,7793 mT | 13,68 cm |
| 1,5 A | 1,1689 mT | 9,12 cm |
| 2,0 A | 1,5586 mT | 6,84 cm |

Umgekehrt gerechnet: Für **B = 1,60 mT** — die Flussdichte aus Aufgabe ue5 — ist
I = B·R/(μ₀·(4/5)^(3/2)·N) = **2,053 A**, für B = 1,80 mT aus Aufgabe ue3 sind es **2,310 A**.
Beide Ströme sind mit einem üblichen Schulnetzgerät erreichbar.
Der Kreisdurchmesser bei B = 1,60 mT und U = 250 V beträgt 2r = **6,66 cm** und stimmt damit
mit dem Messwert der Aufgabe ue5 überein (dort exakt 6,6648 cm, K-25). ✓ Die Aufgabe bildet
also einen real durchführbaren Versuch ab, keine erfundene Zahlenkombination.

---

**Was damit geprüft ist.** K-1 bis K-6 decken die Abschnitte 2 und 3 ab, K-7 bis K-21 den
Abschnitt 4, K-22 bis K-30 (in 5.11) den Abschnitt 5, K-31 den Abschnitt 7. Abschnitt 6 enthält
keine eigenen Zahlenwerte — die dort genannten Beziehungen sind Zusammenfassungen der bereits
geprüften Formeln, Abschnitt 8 ist ein reines Inventar ohne Rechnung. Zwei Abweichungen wurden
gefunden und stehen unverändert als Auffälligkeit 1 und 2 in 8.11; beide betreffen erläuternde
Bereichsangaben in Abschnitt 4, keine Formel und keinen Aufgabenwert.

### Bereits geprüft: K-1 bis K-6 (Abschnitte 2 und 3)

Prüfskripte:
`scratchpad/vorarbeit/physik/magnetfeld_pruefung.py` und
`scratchpad/vorarbeit/physik/abschnitte_0_3.py`
Konstanten: e = 1,602176634 · 10⁻¹⁹ C · m_e = 9,1093837015 · 10⁻³¹ kg ·
m_p = 1,67262192369 · 10⁻²⁷ kg · u = 1,66053906660 · 10⁻²⁷ kg

**K-1 — Kraft auf den Leiter (Abschnitt 2.1)**
F = B · I · l = 0,25 T · 3,5 A · 0,120 m = **0,105 N = 105 mN**.
Einheitenprobe: T · A · m = (N/(A·m)) · A · m = N. ✓

**K-2 — Elektron bei U = 1000 V, B = 3,00 mT (Abschnitt 3.1)**
v = √(2 · 1,602176634·10⁻¹⁹ · 1000 / 9,1093837015·10⁻³¹) = **1,875537 · 10⁷ m/s** (18 755,37 km/s)
r = m·v/(e·B) = 9,1093837·10⁻³¹ · 1,875537·10⁷ / (1,602176634·10⁻¹⁹ · 3,00·10⁻³)
= **3,554537 · 10⁻² m = 3,5545 cm**, also 2r = 7,109 cm.
Gegenprobe über r = (1/B)·√(2mU/q): identisch auf 7 Stellen. ✓
Plausibilität: v/c = 6,26 % — klassische Rechnung zulässig. ✓

**K-3 — Umlaufdauer und Zyklotronfrequenz (Abschnitt 3.2)**
T = 2π·m/(e·B) = 2π · 9,1093837·10⁻³¹ / (1,602176634·10⁻¹⁹ · 3,00·10⁻³)
= **1,190796 · 10⁻⁸ s = 11,908 ns**; f_c = 1/T = **8,3977 · 10⁷ Hz = 84,0 MHz**.
Unabhängigkeit von U, Elektron bei B = 3,00 mT:

| U | v in km/s | r in cm | T in ns |
|---|---|---|---|
| 200 V | 8 387,66 | 1,5896 | 11,9080 |
| 800 V | 16 775,32 | 3,1793 | 11,9080 |
| 2000 V | 26 524,10 | 5,0269 | 11,9080 |

T identisch auf allen ausgegebenen Stellen. ✓
Probe r = v·T/(2π) bei U = 1000 V: 0,035545370 m gegen r = 0,035545370 m, Abweichung 0. ✓
Proton bei B = 3,00 mT: T = 2,186482 · 10⁻⁵ s = 21,865 µs, f_c = **45,74 kHz**;
Verhältnis f_c(e)/f_c(p) = 1836,15 = m_p/m_e. ✓

**K-4 — Wien-Filter (Abschnitt 3.3)**
v = E/B = 1,2·10⁴ V/m / (4,0·10⁻³ T) = **3,000 · 10⁶ m/s = 3000 km/s**.
Einheitenprobe: (V/m)/T = (V/m)·(A·m/N) = V·A/N = W/N = (J/s)/N = m/s. ✓
Variante über Plattenspannung: U_P = 100 V, d = 4,0 cm ⟹ E = 2500 V/m;
bei B = 0,50 mT folgt v = 5,000 · 10⁶ m/s. ✓ (deckt sich mit Block E der Vorarbeit)

**K-5 — Isotopentrennung Ne-20 / Ne-22 (Abschnitt 3.4)**
Massen wie in der Vorarbeit mit 20,0 u bzw. 22,0 u:
bei U = 2,00 kV und B = 600 mT ist 2r(Ne-20) = **9,5983 cm**, 2r(Ne-22) = **10,0668 cm**,
Differenz **0,4685 cm ≈ 4,7 mm**.
Verhältnis 2r(22)/2r(20) = 1,048809 gegen √(22/20) = 1,048809 — Abweichung 0. ✓
Gegenrechnung mit den exakten Isotopenmassen (19,99244 u / 21,99139 u):
9,5965 cm und 10,0648 cm, Verhältnis 1,048802 — Unterschied erst in der vierten Stelle,
für die Aufgabenstellung ohne Belang. Im Modul wird mit 20 u und 22 u gerechnet;
das wird im Aufgabentext ausdrücklich gesagt.
Massenspektrometer-Auswertung m = q·r²·B²/(2U) mit U = 1,50 kV, B = 0,420 T, 2r = 12,7 cm:
m = 3,798702 · 10⁻²⁶ kg = **22,876 u**; Kontrolle mit m = 23 u exakt ergäbe 2r = 12,7343 cm,
die Messung passt also zu Na-23 innerhalb der Ablesegenauigkeit. ✓

**K-6 — Spezifische Ladungen (Abschnitt 3.5)**
e/m_e = **1,758820 · 10¹¹ C/kg** · e/m_p = **9,578833 · 10⁷ C/kg** ·
2e/m_α = **4,822451 · 10⁷ C/kg** · e/m(Ne-20) = **4,824267 · 10⁶ C/kg** ·
e/m(Ne-22) = **4,385697 · 10⁶ C/kg**.
Verhältnis (e/m_e)/(e/m_p) = **1836,153** ✓ (Literaturwert des Massenverhältnisses 1836,15).
Alphateilchen gegen Proton: 4,822·10⁷ / 9,579·10⁷ = 0,5034, also gut die Hälfte — die im Text
behauptete Aussage „liegt unter der des Protons, ungefähr bei der Hälfte" ist damit belegt. ✓
