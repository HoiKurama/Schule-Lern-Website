# Modulinhalt: Geladene Teilchen im elektrischen Feld — Beschleunigung, Ablenkung, Millikan-Versuch

Modul: `physik-q1-geladene-teilchen-e-feld`
Fach: Physik, Leistungskurs Q1
Inhaltsfeld (Chip im Seitenkopf, **wörtlich**): **Ladungen, Felder und Induktion**
Akzentfarben: `--akzent: #1d4ed8`, `--akzent-hell: #eff6ff`, `--akzent-rand: #bfdbfe`
Titel der Seite: *Geladene Teilchen im elektrischen Feld*
Untertitel im Kopf: *Vom Energiesatz über die Parabelbahn im Querfeld bis zur Messung der Elementarladung*
Chips: `Physik LK · Q1` · `Inhaltsfeld: Ladungen, Felder und Induktion` · `ca. 135 Minuten`

**Abgrenzung — verbindlich.** Das Modul baut auf `physik-q1-elektrisches-feld` auf (nur gelesen,
nicht verändert). Dort erarbeitet und hier als bekannt vorausgesetzt: <span class="m">E⃗ = F⃗/q</span>,
<span class="m">F = |q|·E</span>, <span class="m">E = U/d</span> im homogenen Feld, Spannung als Energie
pro Ladung, Wegunabhängigkeit der Arbeit.

| Gehört in dieses Modul | Gehört **nicht** hierher |
|---|---|
| Beschleunigung im Längsfeld, Energiesatz <span class="m">|q|·U = ½·m·v²</span>, Einheit Elektronvolt | Lorentzkraft, Kreisbahn, Massenspektrometer, Wien-Filter (Modul `physik-q1-magnetisches-feld`) |
| Grenze der klassischen Rechnung (v/c), nur als Ausblick ohne Herleitung | relativistische Dynamik, Massenzunahme, Herleitung von γ |
| Bahn im homogenen Querfeld (Parabel), Ablenkwinkel, Auslenkung am Schirm | Kondensatorkapazität, Energie im Feld (Vorgängermodul) |
| Ablenkeinheit einer Elektronenstrahlröhre (Oszilloskop, Braunsche Röhre) | Inhomogene Felder, Randfeld-Rechnung, Raumladung |
| Millikan-Versuch: Schwebemethode, Sinkgeschwindigkeit, Stokes-Reibung, Steig-Sink-Methode, Quantelung der Ladung | Cunningham-Korrektur (nur genannt, nicht gerechnet), Brownsche Bewegung |

**Stellung im Curriculum.** Dieses Modul folgt unmittelbar auf `physik-q1-elektrisches-feld` und
liegt in der Modulliste **vor** `physik-q1-magnetisches-feld`. Das Magnetfeldmodul (fertig) benutzt
<span class="m">v = √(2·|q|·U/m)</span> dort bereits als Beschleunigungsstufe, ohne sie herzuleiten, und
verweist für die Elementarladung auf den Millikan-Versuch. Beides wird hier nachgeliefert; die
Schreibweisen und Konstanten sind deshalb mit dem Magnetfeldmodul abgestimmt (siehe 0.1).

**Kernlehrplan — offene Zuordnung, nicht erfunden.** Das Inhaltsfeld ist der Wortlaut aus
`fachliches/kernlehrplan-nrw.md`. Ob der Millikan-Versuch und die Elektronenstrahlablenkung im
schulinternen Lehrplan im Inhaltsfeld 1 oder in einer anderen Reihe stehen, legt die Fachschaft
fest; eine Zuordnung zu einzelnen Kompetenzerwartungen wird hier **nicht** behauptet
(siehe Lehrerteil, Einordnung).

---

## 0 · Konventionen, Konstanten und Formelzeichen

**Diese Festlegungen gelten für jede Abbildung, jede Simulation, jede Aufgabe und jede
Musterlösung des Moduls. Der Bauagent weicht davon nicht ab.**

### 0.1 Konstanten (überall mit genau diesen Werten rechnen, auch in der Simulation)

| Größe | Zeichen | Wert | Einheit |
|---|---|---|---|
| Elementarladung | e | 1,602 · 10⁻¹⁹ | C |
| Elektronenmasse | m_e | 9,109 · 10⁻³¹ | kg |
| Protonenmasse | m_p | 1,673 · 10⁻²⁷ | kg |
| Masse des α-Teilchens | m_α | 6,645 · 10⁻²⁷ | kg |
| Lichtgeschwindigkeit | c | 2,998 · 10⁸ | m/s |
| Fallbeschleunigung | g | 9,81 | m/s² |
| Viskosität von Luft (20 °C) | η | 1,81 · 10⁻⁵ | Pa·s = kg/(m·s) |
| Dichte des Versuchsöls (Richtwert) | ρ | 875 | kg/m³ |
| Dichte von Luft (nur zur Begründung) | ρ_L | 1,20 | kg/m³ |
| Durchschlagsfeldstärke trockener Luft | E_max | ≈ 3 · 10⁶ | V/m |
| Umrechnung | 1 eV | 1,602 · 10⁻¹⁹ | J |

Die Werte für e, m_e, m_p entsprechen dem Magnetfeldmodul (dort 9,109 · 10⁻³¹ kg,
1,673 · 10⁻²⁷ kg, 1,602 · 10⁻¹⁹ C). Die Simulation dort rechnet intern mit CODATA-Werten; hier rechnet
die Simulation **mit den gerundeten Werten der Tabelle**, damit Anzeige und Musterlösungen bis in die
letzte angegebene Stelle übereinstimmen. Der Unterschied ist kleiner als 0,01 %.

**Modellannahme Auftrieb.** Der Auftrieb des Öltröpfchens in Luft beträgt
<span class="m">ρ_L/ρ = 1,20/875 = 0,14 %</span> der Gewichtskraft. Er wird im gesamten Modul
**vernachlässigt**, auch in der Simulation. Das steht im Text, damit niemand wegen 0,1 % rätselt.

Formeln dafür:
- `data-tex`: `e = 1{,}602 \cdot 10^{-19}\,\mathrm{C} \qquad m_{\mathrm e} = 9{,}109 \cdot 10^{-31}\,\mathrm{kg} \qquad m_{\mathrm p} = 1{,}673 \cdot 10^{-27}\,\mathrm{kg}`
- `data-plain`: `e = 1,602 · 10⁻¹⁹ C     m_e = 9,109 · 10⁻³¹ kg     m_p = 1,673 · 10⁻²⁷ kg`

### 0.2 Formelzeichen

| Zeichen | Bedeutung | Einheit | Anmerkung |
|---|---|---|---|
| <span class="m">q</span> | Ladung eines Teilchens oder Tröpfchens | C | **vorzeichenbehaftet**, Elektron: <span class="m">q = −e</span> |
| <span class="m">e</span> | Elementarladung | C | **immer positiv**, <span class="m">e = 1,602·10⁻¹⁹ C</span> |
| <span class="m">n</span> | Zahl der Elementarladungen auf dem Tröpfchen | 1 | ganzzahlig, <span class="m">q = n·e</span> (Betrag) |
| <span class="m">m</span> | Masse des Teilchens bzw. Tröpfchens | kg | |
| <span class="m">U_B</span> | Beschleunigungsspannung | V | immer positiv angegeben |
| <span class="m">U_A</span> | Ablenkspannung am Plattenpaar | V | vorzeichenbehaftet: <span class="m">U_A > 0</span> heißt obere Platte positiv |
| <span class="m">U</span> | Spannung am Millikan-Kondensator | V | |
| <span class="m">U_s</span> | Schwebespannung | V | Tröpfchen ruht |
| <span class="m">E</span> | Betrag der Feldstärke, <span class="m">E = U/d</span> | V/m | |
| <span class="m">d</span> | Plattenabstand | m | **nicht** das Differential (das steht als `\mathrm{d}`) |
| <span class="m">L</span> | Länge der Ablenkplatten in Flugrichtung | m | |
| <span class="m">D</span> | Abstand Plattenende – Schirm | m | |
| <span class="m">v₀</span> | Geschwindigkeit beim Eintritt ins Querfeld | m/s | nach Beschleunigung aus der Ruhe |
| <span class="m">v_y</span> | Quergeschwindigkeit am Plattenende | m/s | |
| <span class="m">y_a</span> | Ablenkung am Plattenende | m | positiv nach oben |
| <span class="m">Y</span> | Auslenkung auf dem Schirm | m | positiv nach oben |
| <span class="m">θ</span> | Ablenkwinkel gegen die Einfallsrichtung | ° | **nicht α**, damit keine Verwechslung mit dem α-Teilchen entsteht |
| <span class="m">r</span> | Radius des Tröpfchens | m | nicht Durchmesser |
| <span class="m">η</span> | Viskosität der Luft | Pa·s | |
| <span class="m">v_s</span> | Sinkgeschwindigkeit ohne Feld | m/s | **Betrag**, positiv |
| <span class="m">v_st</span> | Steiggeschwindigkeit mit Feld | m/s | **Betrag**, positiv |
| <span class="m">β</span> | <span class="m">v/c</span> | 1 | |

**Kollisionswarnung an den Bauagenten.** (1) `e` ist die Elementarladung und steht in `data-tex`
als `e`, in Einheiten als `\mathrm{e}`; die Eulersche Zahl kommt im Modul nicht vor.
(2) `d` ist der Plattenabstand; ein Differential kommt in diesem Modul nicht vor (falls doch, wird es
immer `\mathrm{d}` geschrieben). (3) Das Zeichen `C` steht ausschließlich
für die Einheit Coulomb, also `\mathrm{C}`; Kapazität kommt in diesem Modul nicht vor.
(4) Der Ablenkwinkel heißt <span class="m">θ</span> (`\vartheta`), das α-Teilchen behält α (`\alpha`).

### 0.3 Richtungen, Achsen und Farben (Abweichung vom Vorgängermodul, bewusst)

Im Vorgängermodul liegt die **positive Platte links**, das Feld zeigt nach rechts. In diesem Modul
ist die Flugrichtung die x-Achse und die Ablenkung die y-Achse; die Ablenkplatten liegen deshalb
**waagerecht**. Die Konvention „Feldlinien laufen von Plus nach Minus" bleibt unverändert.

| Objekt | Festlegung |
|---|---|
| Achsen | <span class="m">x</span> nach rechts (Flugrichtung), <span class="m">y</span> **nach oben**; Canvas-y wird beim Zeichnen gespiegelt |
| Ablenkplatten | <span class="m">U_A > 0</span>: obere Platte positiv (rot `#dc2626`), untere negativ (blau `#1d4ed8`); Feld zeigt **nach unten**, <span class="m">E_y = −U_A/d</span> |
| Elektron (<span class="m">q < 0</span>) | Kraft entgegen dem Feld, also nach oben, zur positiven Platte; Teilchenfarbe blau `#1d4ed8` |
| Proton, α-Teilchen (<span class="m">q > 0</span>) | Kraft mit dem Feld, nach unten; Teilchenfarbe rot `#dc2626` |
| Beschleunigungsstrecke (schematisch) | Startplatte links, Zielplatte rechts (mit Loch); die Polung folgt dem Teilchen: Elektron links **−** (blau) / rechts **+** (rot), Proton und α links **+** / rechts **−**. Das Feld läuft wie immer von Plus nach Minus, die Kraft auf das Teilchen zeigt immer nach rechts |
| Teilchenbahn | violett `#7c3aed`, 2,5 px |
| Verlängerung der Austrittsgeraden nach hinten | gestrichelt grau `#94a3b8`, Beschriftung „scheinbarer Ursprung" |
| Feldlinien im Plattenpaar | dunkelgrau `#334155`, Pfeilspitze in der Mitte, parallel zur y-Achse |
| Öltröpfchen (Millikan) | Tröpfchen negativ geladen, obere Platte positiv; Tröpfchenfarbe amber `#ca8a04` mit `−`-Marke |
| Kräfte im Millikan-Modus | Gewichtskraft `#334155` (nach unten), elektrische Kraft `#dc2626` (nach oben), Stokes-Reibung `#0d7a52` (der Bewegung entgegen) |

### 0.4 Vorzeichenregel

Das Modul rechnet Beträge und liest die Richtung aus dem Vorzeichen von <span class="m">q</span>
ab. Der Energiesatz steht immer mit Betrag, die Richtung der Ablenkung nie „nach Gefühl":

- `data-tex`: `|q| \cdot U_B = \tfrac{1}{2}\,m\,v_0^2 \qquad \vec F = q\,\vec E \qquad y_a = -\,\mathrm{sgn}(q)\,\dfrac{U_A\,L^2}{4\,d\,U_B}`
- `data-plain`: `|q| · U_B = ½ · m · v₀²     F = q · E     y_a = −sgn(q) · U_A · L² / (4 · d · U_B)`

Positive Werte von <span class="m">y_a</span> und <span class="m">Y</span> bedeuten Ablenkung nach oben.
Herleitung der letzten Formel in 2.4.

### 0.5 Einheiten und Zahlendarstellung

- Dezimaltrennzeichen **Komma**, auch in jeder Simulationsanzeige (`fmt()`).
- Geschwindigkeiten in **km/s** (Simulation) oder <span class="m">10⁷ m/s</span> (Text), Zeiten in
  **ns**, Ablenkungen in **mm**, Teilchenenergie in **keV** bzw. **eV**, Ladungen in Vielfachen von
  <span class="m">e</span> und in <span class="m">10⁻¹⁹ C</span>, Sinkgeschwindigkeiten in **µm/s**
  (Simulation) bzw. **mm/s** (Text), Radien in **µm**, Massen in <span class="m">10⁻¹⁵ kg</span>.
- Bei Größen im Modul stets Einheit mit schmalem Leerzeichen: `2,5 kV`, nie `2,5kV`.

---

## 1 · Einstieg

Geht so in `<section id="einstieg">`, `.stufe`-Nummer **1**, Überschrift **Einstieg**.

### 1.1 Aufhänger (zwei Absätze, kein Lehrbuchton)

**Absatz 1:**

> Beim Zahnarzt hängt die Röntgenröhre wenige Zentimeter neben deinem Gesicht. Zwischen Glühkathode
> und Anode liegen dort etwa 65 Kilovolt. Jedes Elektron, das von der einen zur anderen fliegt, nimmt
> dabei 65 Kiloelektronvolt Energie auf und prallt danach auf das Anodenmaterial, wo daraus die
> Röntgenstrahlung wird. Rechnest du das mit dem Energiesatz aus der Mechanik durch, kommt eine
> Geschwindigkeit von rund der halben Lichtgeschwindigkeit heraus, und schon dabei stutzt man: Kann
> die Formel, die du für Wagen und Kugeln gelernt hast, hier noch stimmen? Am Ende dieser Seite kannst
> du selbst beurteilen, wie groß der Fehler ist.

**Absatz 2:**

> Dasselbe Prinzip steckt in jedem Röhrenoszilloskop: Der Elektronenstrahl wird erst beschleunigt und
> dann von zwei Plattenpaaren wie ein Wurfgeschoss zur Seite gelenkt. Und es steckt in einem Versuch,
> mit dem Robert Millikan ab 1909 gezeigt hat, dass elektrische Ladung nicht beliebig teilbar ist: Er
> beobachtete ein Öltröpfchen von rund einem Tausendstel Millimeter Radius im Kondensator, hielt es in der Schwebe oder ließ es steigen und sinken, und
> las aus einer Spannung die Ladung ab. Drei Fragen tragen diese Seite: Wie schnell wird ein Teilchen
> im Feld, und was hat die Masse damit zu tun? Wohin lenkt das Feld es ab, und warum ist die Bahn
> keine Feldlinie? Und wie kommt man mit Mikroskop, Stoppuhr und Voltmeter an eine Ladung von
> 10⁻¹⁹ Coulomb?

**Rechnerische Deckung der Zahlen im Aufhänger** (Kontrollrechnung K-1, siehe Ende der Datei):

| Aussage im Text | Rechnung | Ergebnis |
|---|---|---|
| „65 Kiloelektronvolt" | 65 kV · e | 65 keV = 1,041 · 10⁻¹⁴ J |
| „rund die halbe Lichtgeschwindigkeit" | v = √(2·e·65 kV/m_e) | 1,512 · 10⁸ m/s = 0,504 c |
| Fehler der klassischen Rechnung | relativistisch: γ = 1 + 65 keV/511,06 keV = 1,1272, β = 0,4615 | klassisch 9,3 % zu hoch |
| „ein Tausendstel Millimeter Radius" | Tröpfchen mit r = 1,0 µm | 10⁻³ mm ✓ |

Der Bauagent schreibt in den Fließtext nur die gerundeten Werte, nennt aber in einem
`<details>`-Block direkt darunter die Rechnung mit Zusammenfassung *Woher die halbe Lichtgeschwindigkeit?*:

> Elektron, <span class="m">U_B = 65 kV</span>:
> - `data-tex`: `v = \sqrt{\dfrac{2 \cdot 1{,}602\cdot10^{-19}\,\mathrm C \cdot 65\,000\,\mathrm V}{9{,}109\cdot10^{-31}\,\mathrm{kg}}} = 1{,}512\cdot10^{8}\,\dfrac{\mathrm m}{\mathrm s} = 0{,}504\,c`
> - `data-plain`: `v = √(2 · 1,602·10⁻¹⁹ C · 65 000 V / 9,109·10⁻³¹ kg) = 1,512·10⁸ m/s = 0,504 c`
>
> Die Herleitung dieser Formel steht in 2.2. Dass 0,504 c nicht der wahre Wert ist, zeigt 2.3.

### 1.2 Vorwissensfragen

Kopf der Karte wie im Referenzmodul:
`<div class="karte"><h3>Vorwissen prüfen</h3>` mit dem grauen Hinweissatz
*„Drei Fragen aus der Sekundarstufe I und der Einführungsphase. Wenn du hier hängst, lohnt sich ein
Blick zurück, bevor du weitermachst."*

Alle drei als `<div class="aufgabe" data-mc="…" style="border:none;padding:0;…">`.

---

#### vw1 — Arbeit und Bewegungsenergie (EF Mechanik)

**Frage:**

> Ein reibungsfreier Wagen wird aus der Ruhe von einer konstanten Kraft <span class="m">F</span> über
> die Strecke <span class="m">s</span> beschleunigt und erreicht die Geschwindigkeit <span class="m">v</span>.
> Du lässt dieselbe Kraft über die **doppelte** Strecke <span class="m">2s</span> wirken. Welche
> Geschwindigkeit hat der Wagen dann?

| `data-i` | Option |
|---|---|
| 0 | <span class="m">2·v</span> |
| 1 | <span class="m">√2·v ≈ 1,41·v</span> |
| 2 | <span class="m">4·v</span> |

`r: 1`

**Feedback (`fb`), je Eintrag ein eigener Denkfehler:**

- `fb[0]`: „Das würde gelten, wenn die Geschwindigkeit proportional zur Strecke wäre. Die Arbeit
  W = F·s wird aber zur Bewegungsenergie ½·m·v², und die hängt quadratisch von v ab. Doppelte Arbeit
  heißt doppelte Energie, und daraus folgt nur der Faktor √2 bei v."
- `fb[1]`: „Richtig. F·2s = ½·m·v'² und F·s = ½·m·v² ergeben v'² = 2·v², also v' = √2·v. Genau diese
  Wurzel begegnet dir gleich wieder: Verdoppelst du die Beschleunigungsspannung, wird ein Teilchen
  nicht doppelt, sondern √2-mal so schnell."
- `fb[2]`: „Der Faktor 4 gehört zur Bewegungsenergie bei doppelter *Geschwindigkeit*, nicht bei
  doppelter Strecke. Hier verdoppelt sich die zugeführte Arbeit, also die Energie — und die
  Geschwindigkeit steckt im Quadrat in dieser Energie."

---

#### vw2 — Waagerechter Wurf (EF Mechanik)

**Frage:**

> Eine Kugel verlässt einen Tisch der Höhe <span class="m">h = 0,80 m</span> waagerecht mit
> <span class="m">v₀ = 3,0 m/s</span>. Luftreibung ist zu vernachlässigen, <span class="m">g = 9,81 m/s²</span>.
> Wie weit vom Tischrand landet sie?

| `data-i` | Option |
|---|---|
| 0 | 0,86 m |
| 1 | 1,21 m |
| 2 | 0,49 m |

`r: 1`

**Feedback:**

- `fb[0]`: „Die Fallzeit ist hier √(h/g) = 0,29 s statt √(2h/g) = 0,40 s: Der Faktor 2 aus
  h = ½·g·t² fehlt. Die waagerechte Weite ist dann v₀·t = 3,0 m/s · 0,29 s = 0,86 m — zu kurz."
- `fb[1]`: „Richtig. Beide Bewegungen laufen unabhängig: senkrecht freier Fall,
  h = ½·g·t², also t = √(2h/g) = 0,404 s; waagerecht gleichförmig, x = v₀·t = 1,21 m. Diese
  Zerlegung ist der Kern der Ablenkung im Querfeld, nur mit einer anderen Beschleunigung."
- `fb[2]`: „Hier ist t = 2h/g = 0,163 s gerechnet, also die Zeit linear statt aus h = ½·g·t² über eine
  Wurzel. Setze zuerst h = ½·g·t² nach t um, dann v₀·t."

---

#### vw3 — Konstante Geschwindigkeit heißt Kräftegleichgewicht (Sek I / EF)

**Frage:**

> Ein Fallschirmspringer sinkt mit dem geöffneten Schirm gleichförmig mit
> <span class="m">5 m/s</span>. Was gilt für die beiden Kräfte auf ihn, Gewichtskraft nach unten und
> Luftwiderstand nach oben?

| `data-i` | Option |
|---|---|
| 0 | Die Gewichtskraft ist größer als der Luftwiderstand, sonst würde er nicht weitersinken. |
| 1 | Beide Kräfte sind gleich groß, die Summe der Kräfte ist null. |
| 2 | Der Luftwiderstand ist größer als die Gewichtskraft, weil er die Bewegung bremst. |

`r: 1`

**Feedback:**

- `fb[0]`: „Dahinter steckt die Vorstellung, eine Bewegung brauche eine Kraft, die sie 'antreibt'.
  Nach dem Trägheitsprinzip bleibt ein Körper ohne Kraftüberschuss in gleichförmiger Bewegung. Wäre
  die Gewichtskraft größer, würde er noch schneller werden."
- `fb[1]`: „Richtig. Gleichförmige Bewegung bedeutet Beschleunigung null, also Kraftsumme null. Auf
  dieselbe Weise 'schwebt' und 'sinkt' ein Öltröpfchen im Millikan-Versuch: Die Reibung passt sich
  der Geschwindigkeit an, bis sie die Gewichtskraft ausgleicht."
- `fb[2]`: „Wäre der Luftwiderstand größer, würde der Springer abgebremst und würde langsamer. Die
  Reibung wächst mit der Geschwindigkeit nur so lange, bis sie die Gewichtskraft gerade erreicht;
  bei gleichförmiger Bewegung sind beide gleich."

---

## 2 · Erklärteil — Beschleunigung und Ablenkung im homogenen Feld

`<section id="grundlagen">`, `.stufe`-Nummer **2**,
Überschrift **Beschleunigung und Ablenkung im homogenen Feld**.

### 2.1 Was das Feld mit einem freien Teilchen macht

**Fließtext:**

> Im Vorgängermodul war die Probeladung ein gedachtes Messgerät. Hier lässt du sie los. Ein Teilchen der
> Ladung <span class="m">q</span> und der Masse <span class="m">m</span> im homogenen Feld erfährt die
> konstante Kraft <span class="m">F = q·E</span> und damit nach Newton die konstante Beschleunigung
>
> - `data-tex` (Blockformel): `a = \dfrac{|q| \cdot E}{m} = \dfrac{|q| \cdot U}{m \cdot d}`
> - `data-plain`: `a = |q| · E / m = |q| · U / (m · d)`
>
> Für <span class="m">E</span> wurde <span class="m">E = U/d</span> aus dem Vorgängermodul eingesetzt. Das Vorzeichen
> von <span class="m">q</span> legt nur die Richtung fest: Positive Teilchen werden **mit** dem Feld
> beschleunigt, negative **gegen** das Feld.
>
> **Die Schwerkraft spielt bei Elementarteilchen keine Rolle.** Ein Elektron im Feld
> <span class="m">E = 10 kV/m</span> erfährt <span class="m">F = e·E = 1,6 · 10⁻¹⁵ N</span>, seine Gewichtskraft
> ist <span class="m">m_e·g = 8,9 · 10⁻³⁰ N</span>. Das Verhältnis beträgt
> <span class="m">1,8 · 10¹⁴</span>; die Beschleunigung von <span class="m">1,76 · 10¹⁵ m/s²</span> ist
> das <span class="m">1,8 · 10¹⁴</span>-fache von <span class="m">g</span>. Das gilt **nicht** für ein
> Öltröpfchen von 3,7 · 10⁻¹⁵ kg: Dort sind Gewichtskraft und elektrische Kraft von gleicher
> Größenordnung, und genau das nutzt der Millikan-Versuch in Abschnitt 3.

### 2.2 Der Energiesatz: nur die Spannung zählt

**Fließtext:**

> Beschleunigt man ein Teilchen aus der Ruhe durch die Spannung <span class="m">U_B</span>, so verrichtet
> das Feld an ihm die Arbeit <span class="m">W = |q|·U_B</span> — das ist die Definition der Spannung
> als Energie pro Ladung (Vorwissensfrage aus dem Vorgängermodul). Diese Arbeit erscheint vollständig als Bewegungsenergie:
>
> - `data-tex` (Blockformel): `|q| \cdot U_B = \tfrac{1}{2}\,m\,v^2 \quad \Longrightarrow \quad v = \sqrt{\dfrac{2\,|q|\,U_B}{m}}`
> - `data-plain`: `|q| · U_B = ½ · m · v²   ⟹   v = √(2 · |q| · U_B / m)`
>
> Die Herleitung steht im Details-Block, denn sie zeigt, **warum weder der Plattenabstand noch die
> Feldstärke in der Formel stehen**.

**Details-Block 1** — Zusammenfassung *Herleitung: v = √(2·|q|·U/m) auf zwei Wegen*:

> **Weg 1 — Kinematik.** Im homogenen Feld ist die Beschleunigung konstant,
> <span class="m">a = |q|·E/m</span>. Aus der Ruhe gilt nach der Strecke <span class="m">d</span>
> (Plattenabstand) <span class="m">v² = 2·a·d</span>:
> - `data-tex`: `v^2 = 2\,a\,d = 2\cdot\dfrac{|q|\,E}{m}\cdot d = \dfrac{2\,|q|\,(E\,d)}{m} = \dfrac{2\,|q|\,U_B}{m}`
> - `data-plain`: `v² = 2 · a · d = 2 · (|q| · E / m) · d = 2 · |q| · (E · d) / m = 2 · |q| · U_B / m`
>
> Im letzten Schritt steckt <span class="m">E·d = U_B</span> aus dem Vorgängermodul: Feldstärke mal Strecke
> ist die Spannung.
>
> **Weg 2 — Energie.** Die Arbeit des Feldes ist Kraft mal Weg,
> <span class="m">W = |q|·E·d = |q|·U_B</span>, und sie geht ganz in Bewegungsenergie über:
> - `data-tex`: `|q|\,E\,d = \tfrac{1}{2}\,m\,v^2 \quad\Longrightarrow\quad v = \sqrt{\dfrac{2\,|q|\,U_B}{m}}`
> - `data-plain`: `|q| · E · d = ½ · m · v²   ⟹   v = √(2 · |q| · U_B / m)`
>
> **Einheitenprobe.** <span class="m">C·V/kg = J/kg = (kg·m²/s²)/kg = m²/s²</span>, die Wurzel gibt
> <span class="m">m/s</span>. ✓
>
> **Was daran wichtig ist.** In beiden Wegen fallen Feldstärke und Plattenabstand einzeln heraus und
> nur ihr Produkt, die Spannung, bleibt. Deshalb gilt der Energiesatz auch in Feldern, die gar nicht
> homogen sind, solange die Spannung zwischen Start- und Zielpunkt dieselbe ist: Die Arbeit hängt nur
> von Anfangs- und Endpunkt ab, nicht vom Weg (Wegunabhängigkeit aus dem Vorgängermodul).

**Das Elektronvolt.** Die Energie, die ein Teilchen der Ladung <span class="m">e</span> beim Durchlaufen
von einem Volt gewinnt, ist die Einheit **Elektronvolt**:

- `data-tex`: `1\,\mathrm{eV} = e \cdot 1\,\mathrm V = 1{,}602\cdot10^{-19}\,\mathrm J`
- `data-plain`: `1 eV = e · 1 V = 1,602 · 10⁻¹⁹ J`

Ein Elektron, das 65 kV durchläuft, hat 65 keV. Ein zweifach geladenes α-Teilchen hat bei derselben
Spannung 130 keV. Man liest den Energiegewinn also unmittelbar an Ladungszahl und Spannung ab, ohne zu
rechnen.

**Tabelle** (in `<div class="tabelle">` kapseln, Kontrollrechnung K-2), alle Teilchen mit
<span class="m">U_B = 1,0 kV</span> beschleunigt:

| Teilchen | <span class="m">q</span> | <span class="m">m</span> | <span class="m">|q|/m</span> | Endgeschwindigkeit <span class="m">v</span> | Energie |
|---|---|---|---|---|---|
| Elektron | −e | 9,109 · 10⁻³¹ kg | 1,759 · 10¹¹ C/kg | 1,875 · 10⁷ m/s (18 755 km/s) | 1,0 keV |
| Proton | +e | 1,673 · 10⁻²⁷ kg | 9,576 · 10⁷ C/kg | 4,376 · 10⁵ m/s (437,6 km/s) | 1,0 keV |
| α-Teilchen | +2e | 6,645 · 10⁻²⁷ kg | 4,822 · 10⁷ C/kg | 3,105 · 10⁵ m/s (310,5 km/s) | 2,0 keV |

Der Unterschied zwischen Elektron und Proton ist der Faktor
<span class="m">√(m_p/m_e) = √1836,6 = 42,86</span>: Bei **gleicher Energie** ist das Elektron fast
43-mal schneller.

**Merksatz 1** (`<div class="merksatz">`, Titel *Nur die Spannung zählt*):

> Die Energie, die ein Teilchen im Feld gewinnt, ist <span class="m">|q|·U_B</span> — unabhängig von
> Masse, Plattenabstand und Feldstärke. Die **Geschwindigkeit** hängt zusätzlich von der Masse ab und
> wächst nur mit der **Wurzel** der Spannung: Vierfache Spannung, doppelte Geschwindigkeit.

**Fehlvorstellung 1** (`<div class="hinweis">`):

> **Häufiger Fehler.** „Doppelte Spannung, doppelte Geschwindigkeit" oder „gleiche Energie, gleiche
> Geschwindigkeit". Beides ist falsch, und beide Fehler stecken in derselben Zeile. Die Energie ist
> proportional zu <span class="m">U_B</span>, die Geschwindigkeit nur zu <span class="m">√U_B</span>: Ein
> Elektron hat bei 1 kV die Geschwindigkeit <span class="m">1,875 · 10⁷ m/s</span> und bei 4 kV
> <span class="m">3,751 · 10⁷ m/s</span>, also das Doppelte, nicht das Vierfache. Und weil in der Formel die
> Masse steht, sind gleiche Energien nicht gleiche Geschwindigkeiten: Elektron und Proton haben bei 1 keV
> einen Geschwindigkeitsunterschied vom Faktor 43. Wer im Kopf die Bewegungsenergie
> <span class="m">½·m·v²</span> vor sich sieht, macht diesen Fehler nicht.

### 2.3 Wo die klassische Rechnung endet

**Fließtext:**

> Bei der Röntgenröhre aus dem Einstieg kam 0,504 c heraus. Bei rund 255 kV käme
> <span class="m">v = c</span> heraus, und bei 511 kV sogar 1,41 c. Das kann nicht stimmen: Nichts
> überschreitet die Lichtgeschwindigkeit. Die klassische Formel
> <span class="m">E_kin = ½·m·v²</span> gilt nur, solange <span class="m">v</span> klein gegen
> <span class="m">c</span> ist. Für größere Geschwindigkeiten gilt stattdessen (Ausblick, hier **ohne
> Herleitung**, sie gehört in die Relativitätstheorie):
>
> - `data-tex` (Blockformel): `E_{\mathrm{kin}} = (\gamma - 1)\,m\,c^2, \qquad \gamma = 1 + \dfrac{E_{\mathrm{kin}}}{m\,c^2}, \qquad \dfrac{v}{c} = \sqrt{1 - \dfrac{1}{\gamma^{2}}}`
> - `data-plain`: `E_kin = (γ − 1) · m · c²,   γ = 1 + E_kin/(m·c²),   v/c = √(1 − 1/γ²)`
>
> Die Ruheenergie des Elektrons ist <span class="m">m_e·c² = 511 keV</span>. Für kleine
> Energien liefert diese Formel wieder das klassische Ergebnis; wie schnell sie davon abweicht, zeigt die
> Tabelle.

**Tabelle** (in `<div class="tabelle">`, Elektron, Kontrollrechnung K-3):

| <span class="m">U_B</span> | klassisch <span class="m">v/c</span> | relativistisch <span class="m">v/c</span> | klassisches Ergebnis zu hoch um |
|---|---|---|---|
| 1 kV | 0,0626 | 0,0625 | 0,15 % |
| 10 kV | 0,198 | 0,195 | 1,5 % |
| 65 kV (Zahnarzt) | 0,504 | 0,461 | 9,3 % |
| 100 kV | 0,626 | 0,548 | 14,1 % |
| 255 kV | 0,999 | 0,745 | 34,1 % |
| 511 kV | 1,414 | 0,866 | 63,3 % |

**Bewertung im Fließtext:**

> Ein Proton erreicht dasselbe <span class="m">v/c = 0,1</span> erst bei rund 4,7 MV, weil seine Masse
> 1836-mal so groß ist. Deshalb rechnet man Protonen in Schulaufgaben fast immer klassisch, Elektronen ab
> einigen zehn Kilovolt nicht mehr. Als Faustregel gilt **v/c < 0,1: klassisch rechnen**; die Simulation in Abschnitt 4
> färbt ihre Anzeige orange, sobald diese Grenze überschritten wird. *Offen, mit der Fachschaft zu klären:*
> Ob im Kurs die relativistische Formel verlangt wird, ist eine Setzung des schulinternen Lehrplans und
> steht nicht in diesem Modul.

### 2.4 Ablenkung im Querfeld: der waagerechte Wurf des Elektrons

**Fließtext:**

> Nun fliegt das Teilchen nicht mehr **längs**, sondern **quer** zu den Feldlinien ins Feld. Es kommt aus
> der Beschleunigungsstrecke mit der Geschwindigkeit <span class="m">v₀</span> (aus 2.2) und tritt mittig
> in ein Plattenpaar der Länge <span class="m">L</span> im Abstand <span class="m">d</span> ein, an dem die
> Ablenkspannung <span class="m">U_A</span> liegt. Die Situation kennst du: Es ist der waagerechte Wurf
> aus der Einführungsphase (Vorwissen 2, waagerechter Wurf), nur mit der Beschleunigung
> <span class="m">a = |q|·E/m</span> statt <span class="m">g</span> und mit der Richtung durch das
> Vorzeichen von <span class="m">q</span>. In Flugrichtung wirkt keine Kraft, quer dazu eine konstante.
> Das Ergebnis der Herleitung sind vier Formeln:
>
> - `data-tex` (Blockformel): `y(x) = -\,\mathrm{sgn}(q)\,\dfrac{U_A}{4\,d\,U_B}\,x^2, \qquad y_a = -\,\mathrm{sgn}(q)\,\dfrac{U_A\,L^2}{4\,d\,U_B}`
> - `data-plain`: `y(x) = −sgn(q) · U_A / (4·d·U_B) · x²,   y_a = −sgn(q) · U_A · L² / (4·d·U_B)`
> - `data-tex` (Blockformel): `\tan\vartheta = -\,\mathrm{sgn}(q)\,\dfrac{U_A\,L}{2\,d\,U_B} = \dfrac{2\,y_a}{L}, \qquad Y = \tan\vartheta\cdot\left(\dfrac{L}{2} + D\right)`
> - `data-plain`: `tan θ = −sgn(q) · U_A · L / (2·d·U_B) = 2·y_a/L,   Y = tan θ · (L/2 + D)`

**Details-Block 2** — Zusammenfassung *Herleitung: Parabelbahn, Ablenkwinkel und Schirmauslenkung*:

> Das ist die **zweite vollständige Herleitung** des Moduls.
>
> **Schritt 1 — Zwei unabhängige Bewegungen.** Die Kraft <span class="m">F = q·E</span> zeigt quer zur
> Flugrichtung. In x-Richtung wirkt keine Kraft: gleichförmig mit <span class="m">v₀</span>. In
> y-Richtung ist die Beschleunigung konstant: <span class="m">a_y = q·E_y/m = −q·U_A/(m·d)</span>. Das
> Vorzeichen folgt aus 0.3: bei <span class="m">U_A > 0</span> zeigt das Feld nach unten,
> <span class="m">E_y = −U_A/d</span>.
>
> **Schritt 2 — Ortsfunktionen.** Zeit ab Eintritt bei <span class="m">x = 0</span>, <span class="m">y = 0</span>:
> - `data-tex`: `x(t) = v_0\,t, \qquad y(t) = \tfrac{1}{2}\,a_y\,t^2`
> - `data-plain`: `x(t) = v₀ · t,   y(t) = ½ · a_y · t²`
>
> **Schritt 3 — Zeit eliminieren.** Aus der ersten Gleichung <span class="m">t = x/v₀</span>, eingesetzt:
> - `data-tex`: `y(x) = \dfrac{a_y}{2\,v_0^2}\,x^2`
> - `data-plain`: `y(x) = a_y / (2·v₀²) · x²`
>
> Das ist eine **Parabel** mit dem Scheitel im Eintrittspunkt.
>
> **Schritt 4 — Beschleunigungsspannung einsetzen.** Mit <span class="m">v₀² = 2·|q|·U_B/m</span> (2.2) und
> <span class="m">a_y = −q·U_A/(m·d)</span>:
> - `data-tex`: `y(x) = \dfrac{-\,q\,U_A/(m\,d)}{2\cdot 2\,|q|\,U_B/m}\,x^2 = -\,\dfrac{q}{|q|}\cdot\dfrac{U_A}{4\,d\,U_B}\,x^2`
> - `data-plain`: `y(x) = [−q·U_A/(m·d)] / [2 · 2·|q|·U_B/m] · x² = −(q/|q|) · U_A/(4·d·U_B) · x²`
>
> Die Masse <span class="m">m</span> kürzt sich heraus, und von der Ladung bleibt nur das Vorzeichen
> <span class="m">q/|q| = sgn(q)</span>.
>
> **Schritt 5 — Am Plattenende.** Bei <span class="m">x = L</span> ist
> <span class="m">y_a = −sgn(q)·U_A·L²/(4·d·U_B)</span>.
>
> **Schritt 6 — Austrittswinkel.** Die Steigung der Parabel bei <span class="m">x = L</span> ist
> <span class="m">y'(L) = 2·y_a/L</span>, also
> <span class="m">tan ϑ = 2·y_a/L = −sgn(q)·U_A·L/(2·d·U_B)</span> (mit Vorzeichen). Dasselbe erhält man aus
> <span class="m">tan ϑ = v_y/v₀</span> mit <span class="m">v_y = a_y·L/v₀</span>.
>
> **Schritt 7 — Geradlinig zum Schirm.** Hinter dem Plattenende wirkt keine Kraft mehr, das Teilchen fliegt
> geradeaus unter dem Winkel <span class="m">ϑ</span>. Auf der Strecke <span class="m">D</span> kommt
> <span class="m">D·tan ϑ</span> hinzu:
> - `data-tex`: `Y = y_a + D\tan\vartheta = \tan\vartheta\cdot\left(\dfrac{L}{2} + D\right)`
> - `data-plain`: `Y = y_a + D · tan θ = tan θ · (L/2 + D)`
>
> Der Umformschritt nutzt <span class="m">y_a = tan ϑ · L/2</span> aus Schritt 6. **Anschaulich:** Verlängert
> man die Austrittsgerade rückwärts, trifft sie die Mittellinie genau in der Mitte des Plattenpaares,
> bei <span class="m">x = L/2</span>. Es sieht so aus, als käme das Teilchen von dort geradlinig.
>
> **Schritt 8 — Bedingung, dass es hinauskommt.** Das Teilchen darf die Platte nicht treffen:
> <span class="m">|y_a| ≤ d/2</span>, also <span class="m">|U_A| ≤ 2·d²·U_B/L²</span>.

**Zahlenbeispiel** (Startwerte der Simulation, Kontrollrechnung K-4): Ablenkeinheit
<span class="m">L = 6,0 cm</span>, <span class="m">d = 2,0 cm</span>, <span class="m">D = 20 cm</span>,
Elektron, <span class="m">U_B = 2,0 kV</span>, <span class="m">U_A = +100 V</span>:

> - Feldstärke <span class="m">E = U_A/d = 5,0 kV/m</span>.
> - <span class="m">y_a = 100 V · (0,060 m)² / (4 · 0,020 m · 2000 V) = 2,25 mm</span>, nach oben, weil das
>   Elektron zur positiven oberen Platte gezogen wird.
> - <span class="m">tan ϑ = 2·2,25 mm/60 mm = 0,075</span>, also <span class="m">ϑ = 4,29°</span>.
> - <span class="m">Y = 0,075 · (30 mm + 200 mm) = 17,25 mm</span>.
> - Grenzspannung: <span class="m">|U_A| ≤ 2 · (0,020)²/(0,060)² · 2000 V = 444 V</span>; darüber trifft das Elektron die Platte.
> - Kontrolle über die Zeit: <span class="m">v₀ = 2,652 · 10⁷ m/s</span>, <span class="m">t = L/v₀ = 2,26 ns</span>,
>   <span class="m">a = 8,79 · 10¹⁴ m/s²</span>, <span class="m">y_a = ½·a·t² = 2,25 mm</span> ✓.

**Merksatz 2** (Titel *Die Bahn kennt weder Ladung noch Masse*):

> Beschleunigt man verschiedene Teilchen mit **derselben** Spannung <span class="m">U_B</span> und lenkt sie mit
> **derselben** Ablenkspannung ab, so laufen sie auf **derselben Parabel** — Elektron und Proton,
> einfach und zweifach geladenes Teilchen. Ladung und Masse kürzen sich heraus. Unterschiedlich sind nur
> die **Richtung** (Vorzeichen von <span class="m">q</span>) und die **Flugzeit** (Masse).

**Fehlvorstellung 2** (`<div class="hinweis">`, die Auflösung der offenen Frage aus dem Vorgängermodul):

> **Häufiger Fehler.** „Die Ladung folgt der Feldlinie." Im Plattenpaar sind die Feldlinien senkrechte
> Geraden, die Bahn ist eine Parabel. Die Feldlinie gibt die Richtung der **Kraft** an, nicht die der
> **Geschwindigkeit**. Ohne Anfangsgeschwindigkeit quer zum Feld kommt man mit der Vorstellung durch
> (Beschleunigungsstrecke, Start aus der Ruhe), mit Anfangsgeschwindigkeit nicht mehr. Genau wie beim
> waagerechten Wurf: Die Gewichtskraft zeigt nach unten, die Kugel fliegt nicht senkrecht.

**Fehlvorstellung 3** (`<div class="hinweis">`):

> **Häufiger Fehler.** „Ein Proton ist fast 2000-mal schwerer als ein Elektron, also wird es viel schwächer
> abgelenkt." Das stimmt nur, wenn beide **dieselbe Geschwindigkeit** <span class="m">v₀</span> haben —
> dann ist <span class="m">y_a ∼ q/m</span> und das Proton wird 1836-mal schwächer abgelenkt. Kommen sie aber aus
> **derselben Beschleunigungsspannung**, hat das schwere Teilchen die kleinere Geschwindigkeit, bleibt
> länger im Feld und wird gerade so stark abgelenkt wie das leichte. Erst die Angabe, **wie** die Teilchen
> auf Geschwindigkeit kamen, entscheidet.

**Anwendung im Nebensatz (keine Rechnung erwartet):** Die Ablenkung ist proportional zu
<span class="m">U_A</span>: <span class="m">|Y| = S·|U_A|</span> mit der Ablenkempfindlichkeit
<span class="m">S = L·(L/2 + D)/(2·d·U_B)</span>; mit den Zahlen oben
<span class="m">S = 0,1725 mm/V</span>. Genau das nutzt ein Röhrenoszilloskop: Der Leuchtfleck zeigt die
Spannung, und zwar linear.

---

## 3 · Vertiefung — der Millikan-Versuch

`<section id="vertiefung">`, `.stufe`-Nummer **3**,
Überschrift **Der Millikan-Versuch: die Elementarladung wiegen**.

### 3.1 Idee und Aufbau

**Fließtext:**

> Ladung lässt sich nicht wiegen und nicht mit dem Maßband messen. Millikan hat sie deshalb auf eine
> Kraft zurückgeführt, die er messen konnte. Ein Öl wird in einen waagerechten Plattenkondensator
> zerstäubt (**Öl**, weil es kaum verdunstet), und dabei laden sich die Tröpfchen durch Reibung auf. Mit
> einem Mikroskop mit Strichskala beobachtet man **ein** Tröpfchen; es erscheint als heller Punkt.
> Vier Kräfte kommen ins Spiel, drei davon zählen:

**Tabelle** (in `<div class="tabelle">` kapseln, Kontrollrechnung K-5, Tröpfchen mit
<span class="m">r = 1,00 µm</span>, dreifach geladen, am Schwebepunkt):

| Kraft | Formel | Richtung | Wert im Beispiel |
|---|---|---|---|
| Gewichtskraft | <span class="m">F_G = m·g = (4/3)·π·r³·ρ·g</span> | nach unten | 3,60 · 10⁻¹⁴ N |
| elektrische Kraft | <span class="m">F_el = |q|·U/d</span> | nach oben (Tröpfchen negativ, obere Platte positiv) | 3,60 · 10⁻¹⁴ N bei 374,1 V |
| Stokes-Reibung | <span class="m">F_R = 6·π·η·r·v</span> | der Bewegung entgegen | 3,60 · 10⁻¹⁴ N bei 0,105 mm/s |
| Auftrieb | <span class="m">F_A = ρ_L·V·g</span> | nach oben | 0,14 % von <span class="m">F_G</span>, **vernachlässigt** |

**Fließtext danach:**

> Zur Reibung: Für eine kleine Kugel in zäher Luft wächst die Reibung **linear** mit der Geschwindigkeit
> (Stokes, gültig für <span class="m">Re ≪ 1</span>; hier <span class="m">Re = 1,4 · 10⁻⁵</span>). Deshalb stellt
> sich zu jeder Antriebskraft eine feste Endgeschwindigkeit ein, und zwar **fast sofort**: Die
> Einstellzeit ist <span class="m">τ = m/(6·π·η·r) = 1,07 · 10⁻⁵ s</span>. Ein Tröpfchen, das du im Mikroskop
> sinken siehst, hat schon lange die Endgeschwindigkeit.

### 3.2 Zwei Messungen, eine Ladung

Das ist die **dritte vollständige Herleitung** des Moduls, in einem `<details>`-Block mit der
Zusammenfassung *Herleitung: Wie aus Sinkgeschwindigkeit und Schwebespannung die Ladung wird*.

**Blockformel im Fließtext** (Ergebnis):

- `data-tex`: `|q| = \dfrac{m\,g\,d}{U_s} \quad\text{mit}\quad m = \tfrac{4}{3}\pi r^3 \rho, \quad r = \sqrt{\dfrac{9\,\eta\,v_s}{2\,\rho\,g}}`
- `data-plain`: `|q| = m · g · d / U_s   mit   m = (4/3)·π·r³·ρ,   r = √(9·η·v_s / (2·ρ·g))`

**Inhalt des Details-Blocks:**

> **Schritt 1 — Sinken ohne Feld (U = 0).** Nach der kurzen Einstellzeit ist die Kraftsumme null:
> Gewichtskraft und Reibung sind gleich groß.
> - `data-tex`: `m\,g = 6\pi\,\eta\,r\,v_s`
> - `data-plain`: `m · g = 6π · η · r · v_s`
>
> **Schritt 2 — Radius aus der Sinkgeschwindigkeit.** Mit <span class="m">m = (4/3)·π·r³·ρ</span>:
> - `data-tex`: `\tfrac{4}{3}\pi r^3 \rho\,g = 6\pi\,\eta\,r\,v_s \;\Longrightarrow\; v_s = \dfrac{2\,\rho\,g\,r^2}{9\,\eta} \;\Longrightarrow\; r = \sqrt{\dfrac{9\,\eta\,v_s}{2\,\rho\,g}}`
> - `data-plain`: `(4/3)·π·r³·ρ·g = 6π·η·r·v_s   ⟹   v_s = 2·ρ·g·r² / (9·η)   ⟹   r = √(9·η·v_s / (2·ρ·g))`
>
> Den Radius kann man nicht sehen, aber man kann ihn aus einer Zeitmessung berechnen.
>
> **Schritt 3 — Schweben.** Jetzt wird eine Spannung angelegt, gerade so, dass das Tröpfchen ruht. Ruhe
> heißt <span class="m">v = 0</span>, also keine Reibung, und nur zwei Kräfte halten sich das Gleichgewicht:
> - `data-tex`: `|q|\,E = m\,g \quad\Longrightarrow\quad |q|\,\dfrac{U_s}{d} = m\,g \quad\Longrightarrow\quad |q| = \dfrac{m\,g\,d}{U_s}`
> - `data-plain`: `|q| · E = m · g   ⟹   |q| · U_s / d = m · g   ⟹   |q| = m · g · d / U_s`
>
> **Schritt 4 — Zusammensetzen.**
> - `data-tex`: `|q| = \dfrac{4\pi\,\rho\,g\,d}{3\,U_s}\cdot r^3, \qquad r = \sqrt{\dfrac{9\,\eta\,v_s}{2\,\rho\,g}}`
> - `data-plain`: `|q| = 4π · ρ · g · d / (3 · U_s) · r³,   r = √(9·η·v_s / (2·ρ·g))`
>
> **Schritt 5 — Einheitenprobe.** <span class="m">kg/m³ · m/s² · m · m³ / V = kg·m²/(s²·V) = J/V = C</span>. ✓
>
> **Was in der Formel steckt.** Die Ladung geht über <span class="m">r³</span> und damit über
> <span class="m">v_s^{3/2}</span> ein: Ein Fehler von 1 % bei der Sinkgeschwindigkeit macht 1,5 % bei der Ladung.
> Die Schwebespannung <span class="m">U_s</span> geht nur linear ein. Man muss deshalb die
> **Zeitmessung** sorgfältig machen, nicht die Spannungsanzeige.

**Zahlenbeispiel** (Kontrollrechnung K-5): Ein Tröpfchen sinkt ohne Feld mit
<span class="m">v_s = 0,1054 mm/s</span> — für die Strecke 0,50 mm braucht es 4,74 s. Schwebespannung
<span class="m">U_s = 374,1 V</span> bei <span class="m">d = 5,00 mm</span>.

> - `data-tex`: `r = \sqrt{\dfrac{9 \cdot 1{,}81\cdot10^{-5}\,\mathrm{Pa\,s} \cdot 1{,}054\cdot10^{-4}\,\mathrm{m/s}}{2 \cdot 875\,\mathrm{kg/m^3} \cdot 9{,}81\,\mathrm{m/s^2}}} = 1{,}000\cdot10^{-6}\,\mathrm m`
> - `data-plain`: `r = √(9 · 1,81·10⁻⁵ Pa·s · 1,054·10⁻⁴ m/s / (2 · 875 kg/m³ · 9,81 m/s²)) = 1,000·10⁻⁶ m`
> - `data-tex`: `m = \tfrac{4}{3}\pi\,(1{,}000\cdot10^{-6}\,\mathrm m)^3 \cdot 875\,\dfrac{\mathrm{kg}}{\mathrm{m^3}} = 3{,}665\cdot10^{-15}\,\mathrm{kg}`
> - `data-plain`: `m = (4/3)·π·(1,000·10⁻⁶ m)³ · 875 kg/m³ = 3,665·10⁻¹⁵ kg`
> - `data-tex`: `|q| = \dfrac{3{,}665\cdot10^{-15}\,\mathrm{kg}\cdot 9{,}81\,\mathrm{m/s^2}\cdot 5{,}00\cdot10^{-3}\,\mathrm m}{374{,}1\,\mathrm V} = 4{,}806\cdot10^{-19}\,\mathrm C = 3{,}000\,e`
> - `data-plain`: `|q| = 3,665·10⁻¹⁵ kg · 9,81 m/s² · 5,00·10⁻³ m / 374,1 V = 4,805·10⁻¹⁹ C = 3,000 e`
>
> Das Tröpfchen trägt also genau **drei** Elementarladungen. Die Feldstärke dabei ist
> <span class="m">E = 374,1 V/5,00 mm = 74,8 kV/m</span>, gut 2 % der Durchschlagsfeldstärke von Luft
> (<span class="m">3 · 10⁶ V/m</span>). ✓

**Details-Block 3** — Zusammenfassung *Herleitung: Die Steig-Sink-Methode ohne Schweben*:

> Man muss nicht auf Schweben regeln. Legt man eine größere Spannung <span class="m">U</span> an, steigt das
> Tröpfchen mit konstanter Geschwindigkeit <span class="m">v_st</span>. Die Reibung zeigt jetzt nach unten:
> - `data-tex`: `|q|\,\dfrac{U}{d} = m\,g + 6\pi\,\eta\,r\,v_{st} = 6\pi\,\eta\,r\,(v_s + v_{st}) \quad\Longrightarrow\quad |q| = \dfrac{6\pi\,\eta\,r\,d\,(v_s + v_{st})}{U}`
> - `data-plain`: `|q| · U/d = m·g + 6π·η·r·v_st = 6π·η·r·(v_s + v_st)   ⟹   |q| = 6π·η·r·d·(v_s + v_st) / U`
>
> Im zweiten Schritt wurde <span class="m">m·g = 6π·η·r·v_s</span> aus dem Sinkversuch benutzt. Mit der Schwebespannung
> <span class="m">U_s</span> aus Schritt 3 folgt ein Zusammenhang, den die Simulation als Gerade zeigt:
> - `data-tex`: `v_{st} = v_s\left(\dfrac{U}{U_s} - 1\right)`
> - `data-plain`: `v_st = v_s · (U/U_s − 1)`
>
> Die Steiggeschwindigkeit ist **linear** in der Spannung, bei <span class="m">U = 0</span> ist sie
> <span class="m">−v_s</span> (Sinken), bei <span class="m">U = U_s</span> null (Schweben), bei
> <span class="m">U = 2·U_s</span> genau <span class="m">+v_s</span>. Zahlen: Für das Tröpfchen oben ist bei
> <span class="m">U = 748 V</span> die Steiggeschwindigkeit <span class="m">0,1053 mm/s</span> und
> <span class="m">|q| = 6π·η·r·d·(v_s + v_st)/U = 3,000 e</span> — dieselbe Ladung wie beim Schweben.

### 3.3 Was der Versuch zeigt — und was nicht

**Fließtext:**

> Millikan hat nicht ein Tröpfchen gemessen, sondern sehr viele. Trägt man die gemessenen Ladungen auf
> einer Zahlengeraden auf, häufen sie sich bei **ganzzahligen Vielfachen einer kleinsten Ladung**. Man
> liest sie so aus: Alle Werte durch den kleinsten teilen; kommen keine ganzen Zahlen heraus, durch die
> Hälfte, ein Drittel … teilen, bis alle Quotienten ganzzahlig werden. Oder man bildet die **Differenzen**
> zwischen den Werten, die ebenfalls Vielfache sind. Das Ergebnis ist die **Elementarladung**
> <span class="m">e = 1,602 · 10⁻¹⁹ C</span>. Millikans veröffentlichter Wert von 1913, rund <span class="m">1,592 · 10⁻¹⁹ C</span>, liegt etwa 0,6 % unter dem heutigen Wert; als übliche Ursache wird ein damals nicht genau bekannter Wert für die Viskosität der Luft genannt.
>
> **Was daraus folgt:** Ladung tritt nur in **Portionen** auf, sie ist *gequantelt*. Ein Tröpfchen kann
> <span class="m">3e</span> oder <span class="m">4e</span> tragen, aber nicht <span class="m">3,5e</span>. Und eine
> zweite Folge: Zusammen mit der spezifischen Ladung <span class="m">e/m_e = 1,759 · 10¹¹ C/kg</span> aus dem
> Fadenstrahlrohr (Magnetfeldmodul) ergibt sich die Masse des Elektrons,
> <span class="m">m_e = 1,602·10⁻¹⁹ C/(1,759·10¹¹ C/kg) = 9,11 · 10⁻³¹ kg</span>. Erst zwei
> unabhängige Messungen trennen Ladung und Masse.
>
> **Was daraus nicht folgt:** Die Daten zeigen, dass die kleinste *beobachtete* Portion <span class="m">e</span> ist.
> Ausschließen, dass es noch kleinere Portionen gibt, können sie nicht: Wäre die wahre Einheit
> <span class="m">e/2</span>, wären alle beobachteten Werte gerade Vielfache davon. Die Sicherheit kommt von
> den Tröpfchen mit **einer** Ladung und von den **Ladungsänderungen**, bei denen ein Tröpfchen durch
> Ionisation genau ein Elementarquant gewinnt oder verliert.

**Modellgrenze** (`<div class="hinweis">`):

> **Was dieses Modell weglässt.** Bei Tröpfchen im Bereich von 1 µm ist der Radius nicht mehr groß gegen die mittlere
> freie Weglänge der Luftmoleküle (rund 0,07 µm). Die Stokes-Reibung ist dann etwas kleiner als
> <span class="m">6·π·η·r·v</span>; die **Cunningham-Korrektur** beträgt bei <span class="m">r = 1 µm</span> rund 8,5 %.
> Ohne sie würde der Radius um rund 4 % und die Ladung um rund 13 % zu groß herauskommen (Kontrollrechnung K-5).
> Die Simulation in Abschnitt 4 rechnet konsequent ohne Korrektur; sie ist damit in sich stimmig. Ein reales
> Praktikum mit denselben Formeln würde dagegen Ladungen liefern, die nicht bei Vielfachen von
> 1,6·10⁻¹⁹ C, sondern bei etwa 1,8·10⁻¹⁹ C liegen.

**Merksatz 3** (Titel *Ladung kommt in Portionen*):

> Der Millikan-Versuch macht aus einer Zeit (Sinken), einer Spannung (Schweben) und einer Länge
> (Plattenabstand) die Ladung eines Tröpfchens. Trägt man viele Tröpfchen zusammen, liegen alle Ladungen bei
> ganzzahligen Vielfachen von <span class="m">e = 1,602 · 10⁻¹⁹ C</span>. Der **größte gemeinsame Teiler** der
> Messwerte ist die Elementarladung.

**Fehlvorstellung 4** (`<div class="hinweis">`):

> **Häufiger Fehler.** „Beim Schweben wirkt keine Kraft auf das Tröpfchen." Es wirken zwei, und sie sind
> gleich groß: Gewichtskraft nach unten, elektrische Kraft nach oben. Die **Summe** ist null. Ein
> schwebendes Tröpfchen ist kein kräftefreies Tröpfchen; nur die Reibung fehlt, weil es ruht
> (<span class="m">v = 0</span>). Ändert man die Spannung, setzt es sich in Bewegung, und die Reibung wächst,
> bis sie die **Differenz** der beiden anderen Kräfte ausgleicht. Die Steiggeschwindigkeit hängt deshalb von
> dieser Differenz ab und nicht von der elektrischen Kraft allein.

**Fehlvorstellung 5** (`<div class="hinweis">`):

> **Häufiger Fehler.** „Auf jedem Tröpfchen sitzt genau ein Elektron." Ein Tröpfchen trägt meist mehrere
> Elementarladungen, im Versuch etwa 1 bis 10. Und es trägt nicht „die Ladung der Elektronen", sondern den
> **Überschuss** oder das **Defizit** an Elektronen; deshalb sind auch positive Tröpfchen möglich, die
> im Feld nach unten gezogen werden.

---

## 4 · Interaktiver Kern — Teilchen im Feld: Strahl und Tröpfchen

`<section id="simulation">`, `.stufe`-Nummer **4**,
Überschrift **Teilchen im Feld: Strahl und Tröpfchen**.

Einleitender Absatz über der Simulation:

> Die Simulation hat zwei Betriebsarten. Im Modus **Strahl** beschleunigst du ein Elektron, Proton oder
> α-Teilchen mit der Spannung <span class="m">U_B</span> und lenkst es in einem Plattenpaar mit
> <span class="m">U_A</span> ab; darunter laufen zwei Diagramme mit: die Geschwindigkeit gegen die
> Beschleunigungsspannung, klassisch und relativistisch, und die Auslenkung auf dem Schirm gegen die
> Ablenkspannung. Im Modus **Millikan** beobachtest du vier Öltröpfchen im Kondensator, regelst die
> Spannung und liest Geschwindigkeiten ab; darunter laufen die Geschwindigkeit gegen die Spannung, als
> Messpunkte, die sich zur Geraden aufbauen, und die Kräfte auf das Tröpfchen als Balken.

### 4.1 Was die Simulation rechnet

Alle Rechnungen intern in **SI-Einheiten**, Umrechnung erst bei der Anzeige. Konstanten aus 0.1.

**Modus Strahl.** Feste Geometrie: <span class="m">L = 0,060 m</span>, <span class="m">d = 0,020 m</span>,
<span class="m">D = 0,200 m</span>. Teilchen: Elektron (<span class="m">q = −e</span>, <span class="m">m_e</span>),
Proton (<span class="m">+e</span>, <span class="m">m_p</span>), α-Teilchen (<span class="m">+2e</span>, <span class="m">m_α</span>).

| Schritt | Formel | Bemerkung |
|---|---|---|
| Beschleunigungsspannung | <span class="m">U_B = rund2(100 V · 10^(p/100))</span> | `p` vom Regler (0 … 300), auf **zwei signifikante Stellen** gerundet |
| Eintrittsgeschwindigkeit | <span class="m">v₀ = √(2·|q|·U_B/m)</span> | |
| Energie | <span class="m">E_kin = |q|·U_B</span> | Anzeige in keV: <span class="m">|q|/e · U_B/1000</span> |
| Flugzeit im Plattenpaar | <span class="m">t = L/v₀</span> | Anzeige in ns |
| Ablenkung am Plattenende | <span class="m">y_a = −sgn(q)·U_A·L²/(4·d·U_B)</span> | positiv nach oben |
| Winkel | <span class="m">tan θ = 2·y_a/L</span> (mit Vorzeichen) | Anzeige <span class="m">θ = arctan(...)</span> in ° |
| Auslenkung am Schirm | <span class="m">Y = tan θ · (L/2 + D)</span> | Anzeige in mm |
| Bahn im Plattenpaar | <span class="m">y(x) = −sgn(q)·U_A·x²/(4·d·U_B)</span> | <span class="m">0 ≤ x ≤ L</span> |
| Bahn dahinter | <span class="m">y(x) = y_a + tan θ·(x − L)</span> | bis <span class="m">x = L + D</span> |
| Plattentreffer | <span class="m">|y_a| > d/2</span> | dann <span class="m">x_hit = d·√(2·U_B/|U_A|)</span>; kein Schirmpunkt |
| Relativistische Kontrolle | <span class="m">γ = 1 + |q|·U_B/(m·c²)</span>, <span class="m">β_rel = √(1 − 1/γ²)</span> | nur für die Anzeige der Abweichung und Diagramm 1 |

Die Rundung `rund2` ist: `e = floor(log10(x))`, `f = 10^(e−1)`, `rund2 = round(x/f)·f`.
Damit liegen genau erreichbar: 100 · 200 · 320 · 1000 · 2000 · 5000 · 10 000 · 65 000 · 100 000 V
(Kontrolle in 4.2).

**Modus Millikan.** Feste Größen: <span class="m">d = 5,00 mm</span>, <span class="m">η = 1,81·10⁻⁵ Pa·s</span>,
<span class="m">ρ = 875 kg/m³</span>, <span class="m">g = 9,81 m/s²</span>, Auftrieb vernachlässigt.
Vier Tröpfchen (verdeckte Parameter, **nie** in der Oberfläche anzeigen):

| Tröpfchen | Radius <span class="m">r</span> | Elementarladungen <span class="m">n</span> (negativ) |
|---|---|---|
| 1 | 1,00 µm | 3 |
| 2 | 1,10 µm | 5 |
| 3 | 0,90 µm | 2 |
| 4 | 1,20 µm | 4 |

| Schritt | Formel | Bemerkung |
|---|---|---|
| Masse | <span class="m">m = (4/3)·π·r³·ρ</span> | |
| Gewichtskraft | <span class="m">F_G = m·g</span> | nach unten |
| Feldstärke | <span class="m">E = U/d</span> | |
| elektrische Kraft | <span class="m">F_el = n·e·U/d</span> | nach oben |
| Endgeschwindigkeit (positiv = aufwärts) | <span class="m">v = (F_el − F_G)/(6·π·η·r)</span> | sofort, ohne Einschwingen (<span class="m">τ ≈ 10⁻⁵ s</span>) |
| Stokes-Kraft | <span class="m">F_R = −6·π·η·r·v</span> | wirkt der Bewegung entgegen; Kraftsumme ist immer 0 |
| Position | <span class="m">z(t) = z₀ + ∫ v dt</span>, Sichtfeld 1,8 mm | wandert das Tröpfchen heraus, erscheint es am anderen Rand |
| Zeit für 0,50 mm | <span class="m">t = 0,50 mm/|v|</span> | Anzeige „—", wenn <span class="m">|v| < 0,2 µm/s</span> |

**Selbstkontrolle für den Bauagenten** (nach dem Bau stichprobenartig; K-6 bis K-8):

| Modus | Einstellung | Anzeigen |
|---|---|---|
| Strahl, Start | Elektron, 2,00 kV, +100 V | `v₀ = 26523,2 km/s` · `t = 2,26 ns` · `E_kin = 2,00 keV` · `y_a = +2,25 mm` · `Y = +17,25 mm` · `θ = +4,29°` · `v/c = 8,85 %` |
| Millikan, Start | Tröpfchen 1, U = 0 | `v = −105,39 µm/s` · `t(0,50 mm) = 4,74 s` |
| Millikan | Tröpfchen 1, U = 374 V | `v = −0,02 µm/s` · U = 375 V: `+0,26 µm/s` |

Weicht die Anzeige in der letzten Stelle ab, ist ein Umrechnungsfaktor falsch.

### 4.2 Regler und Bedienelemente — vollständige Liste

Alle Regler in `<div class="regler">`, alle Knöpfe in `<div class="knopfleiste">`. Der Modusschalter
besteht aus zwei Radios mit `name="modus"`; nur die Elemente des aktiven Modus sind sichtbar
(`hidden`), keines wird `disabled`.

| Element | `id` | Bereich | Schritt | Startwert | Beschriftung |
|---|---|---|---|---|---|
| Modus Strahl | `modStrahl` | Radio | – | aktiv | „Strahl im Querfeld" |
| Modus Millikan | `modMillikan` | Radio | – | – | „Millikan-Versuch" |
| Teilchen | Knöpfe `data-teil="e" \| "p" \| "a"` | – | – | `e` | „Elektron" · „Proton" · „α-Teilchen"; aktiver Knopf `primaer` |
| Beschleunigungsspannung <span class="m">U_B</span> | `rUB` | 0 … 300 | 1 | **130** | `Beschleunigungsspannung U_B <b><span id="lUB">2,00</span> kV</b>` (unter 1000 V in V) |
| Ablenkspannung <span class="m">U_A</span> | `rUA` | −200 … 200 | 5 | **100** | `Ablenkspannung U_A <b><span id="lUA">+100</span> V</b>` |
| Tröpfchen | Knöpfe `data-tropfen="1" \| "2" \| "3" \| "4"` | – | – | `1` | „Tröpfchen 1" … „Tröpfchen 4"; aktiver Knopf `primaer`; Wechsel löscht die Spur und setzt U auf 0 |
| Spannung <span class="m">U</span> | `rUM` | 0 … 1000 | 1 | **0** | `Spannung U <b><span id="lUM">0</span> V</b>` |
| Zeitraffer | Knöpfe `data-zeit="1" \| "5"` | – | – | `1` | „Echtzeit" · „5-fach"; wirkt nur auf die Animation, nicht auf angezeigte Werte |
| Spur löschen | `bSpur` | – | – | – | löscht die Messpunkte in Diagramm 1 (Modus Millikan) |
| Pause | `bPause` | – | – | – | „Pause“ / „Fortsetzen“: hält Strahlanimation und Tröpfchenbewegung an, Anzeigen und Regler bleiben bedienbar |
| Zurücksetzen | `bReset` | – | – | – | beide Modi auf Startwerte, Modus Strahl, Pause aus |

**Kontrolltabelle für den Regler `rUB`** (Formel aus 4.1, Zahlen aus K-6):

| Regler `p` | 0 | 30 | 50 | 100 | 130 | 170 | 200 | 281 | 300 |
|---|---|---|---|---|---|---|---|---|---|
| <span class="m">U_B</span> | 100 V | 200 V | 320 V | 1000 V | 2000 V | 5000 V | 10 kV | 65 kV | 100 kV |

**Sonderfälle:** Bei <span class="m">U_A = 0</span> läuft der Strahl geradeaus, alle Ablenkgrößen sind
null (Anzeige `0,00`). Bei Plattentreffer zeigen `aYA`, `aYS`, `aTH` den Text `—`.

### 4.3 Anzeigefelder

`<div class="anzeige">`, alle Zahlen über `fmt(zahl, stellen)` mit Komma.

**Modus Strahl:**

| Beschriftung | `id` | Einheit | Stellen | Startwert |
|---|---|---|---|---|
| Geschwindigkeit v₀ | `aV0` | km/s | 1 | 26523,2 km/s |
| Flugzeit im Plattenpaar | `aTF` | ns | 2 | 2,26 ns |
| Energie | `aEK` | keV | 2 | 2,00 keV |
| Ablenkung am Plattenende y_a | `aYA` | mm | 2, mit Vorzeichen | +2,25 mm |
| Auslenkung am Schirm Y | `aYS` | mm | 2, mit Vorzeichen | +17,25 mm |
| Ablenkwinkel θ | `aTH` | ° | 2, mit Vorzeichen | +4,29° |

Vorzeichen mit U+2212 (`−`), positive Werte mit `+`, null ohne Vorzeichen.
Fußzeile `aVc`: `v/c = 8,85 %` (2 Stellen). Ab <span class="m">v/c > 10 %</span> wird der Text orange
`#b45309` und ergänzt: *„über 10 % müsste relativistisch gerechnet werden: relativistisch
v/c = … %, der klassische Wert liegt … % zu hoch"*. Beispiel Elektron, 4,0 kV:
`v/c = 12,51 %`, relativistisch `12,44 %`, `0,6 % zu hoch`. Der Text endet mit: *„Auch Flugzeit, Ablenkung und Winkel sind dann klassisch gerechnet und entsprechend ungenau.“*

**Modus Millikan:**

| Beschriftung | `id` | Einheit | Stellen | Startwert |
|---|---|---|---|---|
| Spannung U | `aUm` | V | 0 | 0 V |
| Feldstärke E = U/d | `aEm` | kV/m | 2 | 0,00 kV/m |
| Geschwindigkeit v (**+ aufwärts**) | `aVm` | µm/s | 2, mit Vorzeichen | −105,39 µm/s |
| Richtung | `aRi` | Text | – | sinkt |
| Zeit für 0,50 mm | `aT05` | s | 2 | 4,74 s |

`aRi` lautet `sinkt` bei <span class="m">v < −0,2 µm/s</span>, `steigt` bei
<span class="m">v > 0,2 µm/s</span>, sonst `ruht` (auf dem 1-V-Raster ist die Schwebespannung damit für jedes Tröpfchen einstellbar). Darunter steht dauerhaft in Grau die Konstantenzeile:
*„Plattenabstand d = 5,00 mm · Viskosität η = 1,81·10⁻⁵ Pa·s · Öldichte ρ = 875 kg/m³ · g = 9,81 m/s² ·
Auftrieb vernachlässigt"*. Ohne diese Zeile fehlen den Lernenden die Größen für Teil B.

### 4.4 Canvas 1 im Modus Strahl

`<canvas id="cvSim" width="1000" height="400">`

**Maßstab:** `PX_PRO_MM = 2,4` px/mm, in **beiden** Richtungen gleich (Winkel bleiben unverzerrt; das
ist hier anders als beim Kondensator im Vorgängermodul und muss nicht angemerkt werden). Mittellinie bei
`y0 = 200` px, Plattenanfang bei `x = 200` px. Es folgt: Plattenlänge 144 px, Plattenabstand 48 px,
Schirm bei `x = 824` px, größte darstellbare Auslenkung 76,7 mm = 184 px (passt in die Höhe).

| Element | Geometrie | Farbe |
|---|---|---|
| Beschleunigungsstrecke (**nicht maßstäblich**) | Startplatte bei `x = 60`, Zielplatte mit Loch bei `x = 150`, je 60 px hoch; drei Feldlinien dazwischen von Plus nach Minus; Beschriftung „nicht maßstäblich" | Platten nach Teilchen (0.3), Feldlinien `#334155` |
| Ablenkplatten | Rechtecke `x = 200 … 344`, Dicke 6 px, obere Kante bei `y0 − 24 − 6`, untere bei `y0 + 24`; Polung nach Vorzeichen <span class="m">U_A</span> | rot `#dc2626` (+), blau `#1d4ed8` (−) |
| Feldlinien im Plattenpaar | 5 Linien senkrecht zwischen den Platten, Pfeil in der Mitte zeigt von + nach − | `#334155` |
| Schirm | senkrechte Linie bei `x = 824`, 400 px hoch; daneben Millimeterskala mit Marken alle 10 mm (24 px), beschriftet bei ±20, ±40, ±60 mm | `#94a3b8` |
| Bahn | Polygonzug aus 60 Punkten im Plattenpaar plus Gerade bis zum Schirm | violett `#7c3aed` |
| Verlängerung der Austrittsgeraden nach hinten | gestrichelt vom Plattenende bis zur Mittellinie bei `x = 200 + 72`, Beschriftung „scheinbarer Ursprung" | grau `#94a3b8` |
| Leuchtfleck | Kreis Radius 5 px am Schirm bei `y0 − Y·2,4` | Teilchenfarbe |
| Teilchen | Kreis Radius 5 px, läuft die Bahn ab | Elektron blau, Proton und α rot |
| Maßstab | unten links ein Balken von 24 px, Beschriftung „10 mm" | `#475569` |
| Beschriftungen | `U_B` an der Beschleunigungsstrecke, `U_A` an den Platten, `L` und `D` als Doppelpfeile, `Schirm` | `#475569` |

**Animation:** Das Teilchen legt die gesamte Bahn in 2,5 s zurück (Zeitlupe, unabhängig von der echten
Flugzeit, die als Zahl in `aTF` steht), dann 0,6 s Pause und Wiederholung. Beim Plattentreffer bleibt es
an der Platte stehen (kleiner Ring), die Bahn endet dort. Der Text unter dem Bild lautet *„Zeitlupe:
Die Flugzeit steht in der Anzeige."*

### 4.5 Canvas 1 im Modus Millikan

`<canvas id="cvSim" width="1000" height="400">` (dasselbe Element, anderer Inhalt)

**Maßstab:** `PX_PRO_MM = 200` px/mm in der Höhe. Sichtfeld 1,8 mm = 360 px, mittig zwischen
`y = 20` und `y = 380`. Das Sichtfeld ist ein Rechteck `x = 300 … 700`, hellgrau gefüllt.

| Element | Geometrie | Farbe |
|---|---|---|
| Platten | obere Platte als Balken oberhalb des Sichtfeldes (Beschriftung „obere Platte, +", rot), untere unterhalb („untere Platte, −", blau); zwischen ihnen Unterbrechungssymbol und die Beschriftung „Plattenabstand 5,00 mm (Ausschnitt 1,8 mm)" | `#dc2626`, `#1d4ed8` |
| Skala | senkrechte Strichskala am rechten Rand des Sichtfeldes, Marken alle 0,1 mm (20 px), beschriftet alle 0,5 mm mit „0,5 mm", „1,0 mm", „1,5 mm" | `#475569` |
| Tröpfchen | Kreis Radius 6 px (nicht maßstäblich, Text: *„Tröpfchen vergrößert dargestellt"*), `−`-Marke | `#ca8a04` |
| Kraftpfeile am Tröpfchen | `F_G` nach unten, `F_el` nach oben, `F_R` der Bewegung entgegen; Länge **8 px pro 10⁻¹⁴ N**, Pfeile unter 3 px werden weggelassen | `#334155`, `#dc2626`, `#0d7a52` |
| Datenblock | rechts vom Sichtfeld in Grau die Konstantenzeile aus 4.3 | `#475569` |

Position: Start bei 0,9 mm Höhe. Die Animation läuft in Echtzeit (Zeitraffer 5-fach optional): bei
<span class="m">v = −105 µm/s</span> sind das 21 px/s. Verlässt das Tröpfchen das Sichtfeld,
erscheint es am gegenüberliegenden Rand; im Hinweisfeld steht *„Das Mikroskop wurde nachgeführt."*

### 4.6 Die zwei Diagramme

Zwei Canvas: `<canvas id="cvD1" width="1000" height="220">` und
`<canvas id="cvD2" width="1000" height="220">`, Inhalt je nach Modus.

**Modus Strahl — Diagramm 1** (`cvD1`): Geschwindigkeit gegen Beschleunigungsspannung, mitlaufend.

| Achse | Bereich | Beschriftung |
|---|---|---|
| waagerecht | <span class="m">U_B</span> von 100 V bis 1 MV, **logarithmisch** (4 Dekaden), Marken bei 100 V, 1 kV, 10 kV, 100 kV, 1 MV | „Beschleunigungsspannung U_B" |
| senkrecht | <span class="m">v/c</span> von 0 bis 1,5 | „v/c" |

Inhalt: (1) die **klassische** Kurve <span class="m">v/c = √(2·|q|·U_B/(m·c²))</span> des gewählten Teilchens,
durchgezogen; (2) die **relativistische** Kurve <span class="m">β_rel(U_B)</span>, gestrichelt; (3) die Waagerechte
<span class="m">v/c = 1</span> mit Beschriftung *„Lichtgeschwindigkeit"*; (4) der Arbeitspunkt als gefüllter Kreis mit
gestrichelten Hilfslinien; (5) rechts von 100 kV (Ende des Reglerbereichs) eine hellgraue Fläche
*„außerhalb des Reglers"*. Beim **Elektron** schneidet die klassische Kurve bei rund 255 kV die Lichtlinie,
beim **Proton** bleibt sie den ganzen Reglerbereich am unteren Rand und liegt auf der relativistischen
Kurve. Ändert man das Teilchen, ändern sich **beide** Kurven; ändert man <span class="m">U_B</span>, wandert nur
der Arbeitspunkt. Kontrolle: Elektron, 100 kV: klassisch `0,626`, relativistisch `0,548`.

**Modus Strahl — Diagramm 2** (`cvD2`): Auslenkung am Schirm gegen Ablenkspannung.

| Achse | Bereich | Beschriftung |
|---|---|---|
| waagerecht | <span class="m">U_A</span> von −200 V bis +200 V | „Ablenkspannung U_A in V" |
| senkrecht | <span class="m">Y</span> von −80 mm bis +80 mm | „Auslenkung Y in mm" |

Inhalt: die **Gerade** <span class="m">Y(U_A) = −sgn(q)·U_A·L·(L/2 + D)/(2·d·U_B)</span> mit der
Ablenkempfindlichkeit als Steigung, **durchgezogen** im Bereich
<span class="m">|U_A| ≤ 2·d²·U_B/L²</span> (Plattentreffer sonst) und **gestrichelt grau** darüber
(Beschriftung *„Teilchen trifft die Platte"*); der Arbeitspunkt als gefüllter Kreis. Ändert man
<span class="m">U_B</span> oder das Vorzeichen der Ladung, **dreht** sich die Gerade um den Ursprung (Elektron
steigt, Proton fällt). Kontrolle: Elektron, 2,00 kV: Steigung <span class="m">0,1725 mm/V</span>, gültig bis
<span class="m">±444 V</span>, also im ganzen Reglerbereich von ±200 V; bei 500 V Beschleunigung nur bis
±111 V.

**Modus Millikan — Diagramm 1** (`cvD1`): Geschwindigkeit gegen Spannung als **Messspur**.

| Achse | Bereich | Beschriftung |
|---|---|---|
| waagerecht | <span class="m">U</span> von 0 bis 1000 V | „Spannung U in V" |
| senkrecht | <span class="m">v</span> von −200 bis +400 µm/s, Nulllinie kräftig | „Geschwindigkeit v in µm/s (aufwärts +)" |

Inhalt: Jede Reglerbewegung legt einen **Messpunkt** <span class="m">(U | v)</span> ab, der stehen bleibt.
Die Punkte liegen nach kurzer Zeit auf einer **Geraden**; ihr Schnittpunkt mit der Nulllinie ist die
Schwebespannung. Die Gerade selbst wird **nicht** eingezeichnet, damit die Schwebespannung nicht
vorgegeben ist. Der aktuelle Punkt ist ein größerer Kreis. Die Spur wird bei Tröpfchenwechsel, „Spur
löschen" und Zurücksetzen geleert. Kontrolle (Tröpfchen 1): Punkte `(0 | −105,39)`, `(500 | +35,48)`,
`(1000 | +176,34)` liegen auf einer Geraden mit der Steigung `0,2817 µm/(s·V)`.

**Modus Millikan — Diagramm 2** (`cvD2`): Kräfte auf das Tröpfchen als Balken.

Drei senkrechte Balken nebeneinander, Skala <span class="m">−2·10⁻¹³ N</span> bis
<span class="m">+2·10⁻¹³ N</span>, Nulllinie in der Mitte: **Gewichtskraft** (grau, nach unten, also negativ,
konstant), **elektrische Kraft** (rot, positiv, wächst mit <span class="m">U</span>) und **Stokes-Reibung**
(grün, positiv beim Sinken, negativ beim Steigen, null bei Ruhe). Über jedem Balken steht der Zahlenwert in
<span class="m">10⁻¹⁴ N</span> mit 2 Stellen. Darunter eine Zeile *„Summe = 0,00 · 10⁻¹⁴ N"*: Die drei Kräfte
gleichen sich stets aus, weil das Tröpfchen sofort seine Endgeschwindigkeit hat. Kontrolle: Tröpfchen 2,
U = 300 V: `F_G = −4,79`, `F_el = +4,81`, `F_R = −0,02` (×10⁻¹⁴ N; das Tröpfchen steigt mit +0,54 µm/s).

### 4.7 Hinweisfeld

`<p id="simHinweis">` unter der Knopfleiste, leer, solange nichts zu melden ist.

| Bedingung | Text |
|---|---|
| Plattentreffer (Modus Strahl) | „Das Teilchen trifft die Platte bei x = … cm und erreicht den Schirm nicht. Verkleinere U_A oder vergrößere U_B." |
| <span class="m">v/c > 10 %</span> | Ergänzung in `aVc`, siehe 4.3 (kein Hinweisfeld nötig) |
| Tröpfchen verlässt das Sichtfeld | „Das Mikroskop wurde nachgeführt." |
| Wechsel des Tröpfchens | „Neues Tröpfchen: Spannung auf 0 gesetzt, Spur gelöscht." |

### 4.8 Beobachtungsauftrag

`<div class="auftrag">`, Text:

> **Beobachtungsauftrag**
> **Teil A — Strahl.** Stelle im Modus *Strahl* ein: Elektron, <span class="m">U_B = 2,00 kV</span>,
> <span class="m">U_A = +100 V</span>. Notiere <span class="m">v₀</span>, Flugzeit,
> <span class="m">y_a</span>, <span class="m">Y</span> und <span class="m">θ</span>.
> **Schreibe vorher auf**, was du beim Wechsel auf *Proton* und dann auf *α-Teilchen* erwartest: Was
> ändert sich, was bleibt gleich? Wechsle dann und notiere jeweils dieselben fünf Größen. Stelle zuletzt
> wieder das Elektron ein, verdopple <span class="m">U_B</span> auf 4,0 kV und notiere <span class="m">v₀</span> und
> <span class="m">Y</span>.
>
> **Teil B — Tröpfchen.** Wechsle zum Modus *Millikan*. Lies bei jedem der vier Tröpfchen zuerst
> <span class="m">v_s</span> bei <span class="m">U = 0</span> ab. Regle danach die Spannung, bis die Anzeige „ruht“ erscheint (das
> Tröpfchen bewegt sich dann langsamer als 0,2 µm/s; die Messpunkte in Diagramm 1 helfen dir, den Nulldurchgang von
> „sinkt“ nach „steigt“ zu finden), und notiere
> <span class="m">U_s</span> auf 1 V genau. Mit *Pause* hältst du Strahl und Tröpfchen an, um in Ruhe abzulesen. Berechne mit den Formeln aus 3.2 für jedes Tröpfchen <span class="m">r</span>,
> <span class="m">m</span> und <span class="m">q</span>, und teile dann alle vier Ladungen durch die kleinste.
>
> **Schreibe zwei Sätze auf:** (a) Was hat sich beim Wechsel Elektron → Proton → α-Teilchen nicht
> geändert, was schon — und was sagt das über die Bahn? (b) Was fällt dir an den vier Ladungen auf, und
> welche Elementarladung liest du daraus ab?

**Erwartete Messwerte Teil A** (K-6, dient der Lehrkraft zur Kontrolle; U_A = +100 V):

| | v₀ | Flugzeit | y_a | Y | θ |
|---|---|---|---|---|---|
| Elektron, 2,00 kV | 26523,2 km/s | 2,26 ns | +2,25 mm | +17,25 mm | +4,29° |
| Proton, 2,00 kV | 618,9 km/s | 96,95 ns | −2,25 mm | −17,25 mm | −4,29° |
| α-Teilchen, 2,00 kV | 439,2 km/s | 136,62 ns | −2,25 mm | −17,25 mm | −4,29° |
| Elektron, 4,00 kV | 37509,5 km/s | 1,60 ns | +1,13 mm | +8,63 mm | +2,15° |

Beim letzten Wert kann die zweite Nachkommastelle wegen der Rundung von 8,625 und 1,125 um eins
abweichen (8,62 oder 8,63, 1,12 oder 1,13); das ist kein Fehler.

**Erwartete Messwerte Teil B** (K-7; Ablesegenauigkeit <span class="m">U_s ± 1 V</span> reicht für 0,3 % bei
<span class="m">q</span>, ein Fehler von 1 % bei <span class="m">v_s</span> bringt 1,5 %):

| Tröpfchen | <span class="m">v_s</span> | <span class="m">U_s</span> | <span class="m">r</span> | <span class="m">m</span> | <span class="m">q</span> | <span class="m">q/q_min</span> |
|---|---|---|---|---|---|---|
| 1 | 105,39 µm/s | ≈ 374,1 V | 1,00 µm | 3,665 · 10⁻¹⁵ kg | 4,806 · 10⁻¹⁹ C | 1,50 |
| 2 | 127,52 µm/s | ≈ 298,7 V | 1,10 µm | 4,878 · 10⁻¹⁵ kg | 8,010 · 10⁻¹⁹ C | 2,50 |
| 3 | 85,36 µm/s | ≈ 409,0 V | 0,90 µm | 2,672 · 10⁻¹⁵ kg | 3,204 · 10⁻¹⁹ C | 1,00 |
| 4 | 151,76 µm/s | ≈ 484,8 V | 1,20 µm | 6,333 · 10⁻¹⁵ kg | 6,408 · 10⁻¹⁹ C | 2,00 |

**Was die Lernenden finden sollen:** Die Quotienten 1,5 · 2,5 · 1,0 · 2,0 sind nicht alle ganz, also durch 2
teilen (alle Werte mal 2): 3 · 5 · 2 · 4. Die Elementarladung ist die Hälfte der kleinsten Ladung,
<span class="m">e = 3,204 · 10⁻¹⁹ C/2 = 1,602 · 10⁻¹⁹ C</span>. Wer den Radius statt aus
<span class="m">v_s</span> falsch bestimmt, sieht die Ganzzahligkeit nicht — das ist gewollt: Die
Ladungsquantelung steht erst da, wenn die Auswertung stimmt.

### 4.9 Die beiden Verständnisfragen zur Simulation

Beide direkt unter der Simulation, `<div class="aufgabe" data-mc="…">`, jeweils mit
`<span class="ab">Anforderungsbereich II</span>`. Sie sind **nur mit der Simulation** zu beantworten,
weil sie das Ablesen zweier Einstellungen verlangen.

---

#### sim1

**Frage:**

> Stelle im Modus *Strahl* das **Proton** und die Beschleunigungsspannung <span class="m">U_B = 500 V</span> ein
> (Regler `rUB` auf 70). Erhöhe dann die Ablenkspannung <span class="m">U_A</span> in 5-V-Schritten von +100 V an
> aufwärts und beobachte Bahn und Anzeigen. Welche Aussage passt zu dem, was du siehst?

| `data-i` | Option |
|---|---|
| 0 | Das Proton erreicht den Schirm bei jedem Wert von U_A bis 200 V, denn wegen seiner großen Masse ist es zu träge, um die Platte zu treffen. |
| 1 | Bis U_A = 110 V erreicht es den Schirm (dort Y = −75,90 mm); bei 115 V trifft es die Platte, und die Anzeigen für Ablenkung, Auslenkung und Winkel zeigen „—“. |
| 2 | Bis U_A = 110 V erreicht es den Schirm, und die Auslenkung bleibt dabei bei Y = −17,25 mm, weil sich Ladung und Masse aus der Bahn kürzen. |
| 3 | Die Grenze liegt bei U_A = 444 V wie im Zahlenbeispiel; im Regler wird das Proton daher nie an der Platte gefangen. |

`r: 1`

**Feedback:** Die vier Texte stehen in `daten.src`/`mcDaten` des Moduls; sie nennen für Option 0 den Denkfehler
„Masse statt Ablenkformel“, für Option 2 „Kürzen heißt nicht Unabhängigkeit von den Spannungen (17,25 mm gehört zu
2,00 kV und 100 V)“, für Option 3 „444 V gilt nur für 2,00 kV; die Grenze ist 2·d²·U_B/L² = 111 V“, und bestätigen
bei Option 1 die Anzeigen 110 V: `y_a = −9,90 mm`, `Y = −75,90 mm`, `θ = −18,26°`; 115 V: Plattentreffer bei `x = 5,9 cm`.

**Kontrollrechnung (Python):** `U_B = 500 V` (Regler 70, `rund2(501,19) = 500`), `U_A,max = 2·d²·U_B/L² = 111,1 V`.
Bei 110 V: `y_a = −110·0,0036/(4·0,02·500) = −9,90 mm`, `tan θ = 2·y_a/L = −0,33`, `Y = −0,33·0,23 = −75,90 mm`,
`θ = −18,26°`; bei 115 V: `|y_a| = 10,35 mm > 10 mm`, `x_hit = 0,02·√(2·500/115) = 5,9 cm`. Die Zahlen 110 V und
−75,90 mm stehen nirgends im Erklärtext.

---

#### sim2

**Frage:**

> Wechsle zum Modus *Millikan* und wähle Tröpfchen 3. Lies zuerst die Geschwindigkeit bei <span class="m">U = 0</span>
> ab und bestimme durch Probieren die Schwebespannung <span class="m">U_s</span> (Anzeige „ruht“). Stelle dann
> <span class="m">U = 300 V</span> ein und lies die Geschwindigkeit ab. Welche Aussage passt?

| `data-i` | Option |
|---|---|
| 0 | Das Tröpfchen sinkt mit etwa 62,6 µm/s, denn 300 V sind 73 % der Schwebespannung, also bleiben 73 % der Sinkgeschwindigkeit ohne Feld. |
| 1 | Das Tröpfchen sinkt mit etwa 22,8 µm/s, also nur noch gut ein Viertel der Geschwindigkeit ohne Feld. |
| 2 | Das Tröpfchen steigt mit etwa 22,8 µm/s, weil die elektrische Kraft nach oben zeigt. |
| 3 | Das Tröpfchen ruht, denn 300 V liegen in der Nähe der Schwebespannung. |

`r: 1`

**Feedback:** Option 0: Geschwindigkeit ist nicht proportional zu U, sondern zur Kraftdifferenz (Anzeige −22,76 µm/s
statt −62,6); Option 1: richtig, `v = v_s·(U/U_s − 1) = 85,36·(300/409,05 − 1) = −22,76 µm/s`; Option 2: Richtung
entscheidet der Vergleich mit U_s ≈ 409 V, Anzeige „sinkt“; Option 3: „ruht“ bei 409 V und 410 V (Doppelfenster wegen Steigung 0,2087 µm/(s·V) und Schwelle 0,2 µm/s), bei 300 V dagegen „sinkt“.

**Kontrollrechnung (Python):** Tröpfchen 3 (`r = 0,90 µm`, `n = 2`): `v_s = 85,36 µm/s`, `U_s = 409,05 V`, `v(300 V) = −22,76 µm/s`,
`v(409 V) = −0,01 µm/s` (ruht), `v(410 V) = +0,20 µm/s` (ruht, Schwelle 0,2 µm/s), `62,6 = 85,36·300/409,05`.
Ruheband 0,2 µm/s: Tröpfchen 3 ruht bei 409 V und 410 V, Tröpfchen 2 ruht ab 299 V (+0,11), Tröpfchen 4 ab 485 V (+0,06), Tröpfchen 1 bei 374 V (−0,02).

---

## 5 · Übungen

`<section id="uebungen">`, `.stufe`-Nummer **5**, Überschrift **Übungen — vom Einsetzen zum Beurteilen**.

Neun Aufgaben, verteilt auf die Anforderungsbereiche: **I** (ue1, ue2, ue3) · **II** (ue4, ue5, ue6) ·
**III** (ue7, ue8, ue9). Die drei Aufgaben im Anforderungsbereich III sind Begründungs- und
Bewertungsaufgaben mit Musterlösung **und** Bewertungskriterien; gerechnet wird dort nur so viel, wie das
Argument trägt.

**Hilfesystem.** **Tipp** räumt eine Hürde weg und nennt keine Formel · **Ansatz** gibt die Formel und den Weg,
rechnet aber nicht · **Lösungsweg** rechnet vollständig mit Zwischenschritten und Einheiten. Diese drei Stufen
(`data-hilfe="1|2|3"` mit `.hilfe-text[data-stufe="1|2|3"]`) haben die sechs auswertbaren Aufgaben ue1 bis ue6
(auch die Multiple-Choice-Aufgabe ue3 und die Zuordnung ue4), wie im Vorgängermodul. Die drei offenen
Bewertungsaufgaben ue7 bis ue9 folgen der Linie des Referenzmoduls (Entscheidung des Nutzers): **nur** ein Knopf
„Musterlösung anzeigen“ (`<button data-loesung="…">`, Text in `.hilfe-text[data-stufe="9"]`, mit den fetten
Bewertungskriterien), keine Tipp- und Ansatz-Knöpfe.

---

### 5.1 ue1 — Endgeschwindigkeit eines Elektrons

`<div class="aufgabe" data-num="ue1">`, `<span class="ab">Anforderungsbereich I</span>`

**Aufgabentext:**

> Ein Elektron wird aus der Ruhe zwischen zwei Elektroden durch die Spannung
> <span class="m">U_B = 2,5 kV</span> beschleunigt.
>
> Berechne seine Endgeschwindigkeit <span class="m">v</span>.

**Eingabe:** `type="number"`, Einheitenliste: `Einheit…` (leer) · `m/s` · `km/s` · **`m/s²`** · **`J`**
Die Distraktoren **m/s²** und **J** fangen zwei Verwechslungen ab: Geschwindigkeit mit Beschleunigung, und
die Energie <span class="m">e·U_B</span> mit dem gesuchten Tempo.

**`numDaten`-Eintrag:**

```js
ue1:{ wert:2.9654e7, einheit:"m/s", tol:1.5e5,
      alt:{wert:29654, einheit:"km/s"},
      ok:"Richtig. v = √(2·e·U_B/m_e) = √(2 · 1,602·10⁻¹⁹ C · 2500 V / 9,109·10⁻³¹ kg) = 2,965·10⁷ m/s = 29 654 km/s. Das sind 9,9 % der Lichtgeschwindigkeit, gerade noch unter der 10-%-Grenze: Die klassische Rechnung ist hier noch zulässig (relativistisch käme 2,955·10⁷ m/s, also 0,4 % weniger).",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. Gesucht ist eine Geschwindigkeit, also m/s oder km/s. m/s² wäre eine Beschleunigung, J eine Energie. Auch wenn 2,5 kV·e = 2,5 keV eine Energie ist: Zu berechnen ist das Tempo, das aus dieser Energie folgt.",
      sonder:[
        {wert:2.097e7, text:"Hier fehlt der Faktor 2 unter der Wurzel: √(e·U_B/m) = 2,097·10⁷ m/s. Aus |q|·U_B = ½·m·v² folgt v² = 2·|q|·U_B/m; die 2 kommt vom Bruch ½ auf der rechten Seite. Der Wert ist um den Faktor √2 zu klein."},
        {wert:6.92e5, text:"Das ist die Geschwindigkeit eines **Protons** bei 2,5 kV (m_p = 1,673·10⁻²⁷ kg). Gefragt ist aber ein Elektron mit m_e = 9,109·10⁻³¹ kg — es ist rund 43-mal schneller."}
      ],
      nah:"Die Größenordnung stimmt, der Wert nicht ganz. Zwei typische Stellen: Steht unter der Wurzel wirklich 2·e·U_B/m (mit der 2) und ist die Masse die des Elektrons, 9,109·10⁻³¹ kg? Und ist die Spannung in Volt eingesetzt (2,5 kV = 2500 V)?",
      weit:"Das liegt um mehr als den Faktor zwei daneben — da ist eine Zehnerpotenz verrutscht oder die Wurzel vergessen. Ohne Wurzel käme v² heraus (8,8·10¹⁴ m²/s²). Nutze die Hilfen und schreib jede Größe mit ihrer Einheit auf." }
```

*Hinweis an den Bauagenten:* Das Feld `sonder` ist eine Engine-Erweiterung, die im Vorgängermodul
`module/physik-q1-elektrisches-feld.html` bereits eingebaut ist (Auswertung in der Zahlen-Engine, Zeilen
um `d.sonder`); sie wird aus **diesem** Modul übernommen, nicht neu erfunden. Sonderfälle haben Vorrang vor
`nah` und `weit` und gelten nur in der Haupteinheit.

**Hilfe 1 (Tipp):**

> Die Spannung liefert dem Elektron Energie, und diese Energie muss irgendwo bleiben. Frag dich: In
> welcher Energieform steckt sie am Ende, und was hängt davon ab, wie schnell das Elektron ist?

**Hilfe 2 (Ansatz):**

> Die Arbeit des Feldes ist gleich der Bewegungsenergie:
> - `data-tex`: `|q| \cdot U_B = \tfrac{1}{2}\,m\,v^2`
> - `data-plain`: `|q| · U_B = ½ · m · v²`
>
> Löse nach <span class="m">v</span> auf und setze <span class="m">|q| = e = 1,602 · 10⁻¹⁹ C</span>,
> <span class="m">m = m_e = 9,109 · 10⁻³¹ kg</span> und <span class="m">U_B</span> in Volt ein.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** U_B = 2,5 kV = 2500 V · e = 1,602 · 10⁻¹⁹ C · m_e = 9,109 · 10⁻³¹ kg
>
> **Schritt 1 — Energie.** <span class="m">W = e·U_B = 1,602·10⁻¹⁹ C · 2500 V = 4,005·10⁻¹⁶ J = 2,5 keV</span>
>
> **Schritt 2 — Auflösen und einsetzen.**
> - `data-tex`: `v = \sqrt{\dfrac{2\,e\,U_B}{m_{\mathrm e}}} = \sqrt{\dfrac{2 \cdot 4{,}005\cdot10^{-16}\,\mathrm J}{9{,}109\cdot10^{-31}\,\mathrm{kg}}} = \sqrt{8{,}794\cdot10^{14}\,\dfrac{\mathrm{m^2}}{\mathrm{s^2}}} = 2{,}965\cdot10^{7}\,\dfrac{\mathrm m}{\mathrm s}`
> - `data-plain`: `v = √(2 · 4,005·10⁻¹⁶ J / 9,109·10⁻³¹ kg) = √(8,794·10¹⁴ m²/s²) = 2,965·10⁷ m/s`
>
> Einheitenprobe: J/kg = m²/s², Wurzel: m/s ✓
>
> **Schritt 3 — Einordnen.** <span class="m">v/c = 2,965·10⁷/2,998·10⁸ = 0,099</span>, knapp unter der Grenze
> 0,1 aus 2.3; die klassische Rechnung ist zulässig.
>
> **Ergebnis: v = 2,965 · 10⁷ m/s = 29 654 km/s ≈ 3,0 · 10⁷ m/s.**

---

### 5.2 ue2 — Ladung eines schwebenden Öltröpfchens

`<div class="aufgabe" data-num="ue2">`, `<span class="ab">Anforderungsbereich I</span>`

**Aufgabentext:**

> In einem Millikan-Kondensator mit dem Plattenabstand <span class="m">d = 6,0 mm</span> schwebt ein
> Öltröpfchen der Masse <span class="m">m = 3,43 · 10⁻¹⁵ kg</span> bei der Spannung
> <span class="m">U_s = 420 V</span>. Der Auftrieb in Luft ist zu vernachlässigen,
> <span class="m">g = 9,81 m/s²</span>.
>
> Berechne die Ladung <span class="m">q</span> des Tröpfchens in Vielfachen der Elementarladung
> <span class="m">e = 1,602 · 10⁻¹⁹ C</span>.

**Eingabe:** `Einheit…` (leer) · `e` · `C` · **`C/kg`** · **`V/m`**
Der Distraktor **C/kg** fängt die Verwechslung von Ladung und spezifischer Ladung ab; **V/m** die von
Ladung und Feldstärke, die auf dem Weg als Zwischenwert auftritt.

**`numDaten`-Eintrag:**

```js
ue2:{ wert:3.0, einheit:"e", tol:0.1,
      alt:{wert:4.806e-19, einheit:"C"},
      ok:"Richtig. Schweben heißt Kräftegleichgewicht: |q|·U_s/d = m·g, also |q| = m·g·d/U_s = 3,43·10⁻¹⁵ kg · 9,81 m/s² · 6,0·10⁻³ m / 420 V = 4,807·10⁻¹⁹ C = 3,0 e. Ein Vielfaches von e — das Tröpfchen trägt drei Elementarladungen.",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. Gesucht ist eine Ladung: entweder als Vielfaches von e oder in Coulomb. C/kg wäre eine spezifische Ladung, V/m eine Feldstärke (die ist hier 70 kV/m und nur ein Zwischenschritt).",
      nah:"Knapp daneben, aber nicht auf drei Elementarladungen. Prüfe: Steht im Zähler m·g·d, also Gewichtskraft mal Plattenabstand, und im Nenner nur die Spannung U_s? Und ist d in Metern eingesetzt (6,0 mm = 6,0·10⁻³ m)?",
      weit:"Das liegt weit daneben. Häufigste Ursachen: der Plattenabstand steht in mm statt in m (Faktor 1000), oder du hast E = U/d falsch herum genommen. Nutze die Hilfen." }
```

**Hilfe 1 (Tipp):**

> Das Tröpfchen ruht. Was folgt daraus für die Summe aller Kräfte, die auf es wirken? Und welche zwei
> Kräfte bleiben übrig, wenn es nicht mehr sinkt oder steigt?

**Hilfe 2 (Ansatz):**

> Beim Schweben halten sich Gewichtskraft und elektrische Kraft das Gleichgewicht, Reibung gibt es nicht:
> - `data-tex`: `|q|\,E = m\,g \quad\text{mit}\quad E = \dfrac{U_s}{d}`
> - `data-plain`: `|q| · E = m · g   mit   E = U_s / d`
>
> Löse nach <span class="m">|q|</span> auf, rechne in Coulomb und teile das Ergebnis durch
> <span class="m">e</span>.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** m = 3,43 · 10⁻¹⁵ kg · d = 6,0 mm = 6,0 · 10⁻³ m · U_s = 420 V · g = 9,81 m/s²
>
> **Schritt 1 — Gewichtskraft.** <span class="m">F_G = m·g = 3,43·10⁻¹⁵ kg · 9,81 m/s² = 3,365·10⁻¹⁴ N</span>
>
> **Schritt 2 — Feldstärke.** <span class="m">E = U_s/d = 420 V / 6,0·10⁻³ m = 7,00·10⁴ V/m</span>
>
> **Schritt 3 — Ladung.**
> - `data-tex`: `|q| = \dfrac{F_G}{E} = \dfrac{3{,}365\cdot10^{-14}\,\mathrm N}{7{,}00\cdot10^{4}\,\mathrm{V/m}} = 4{,}807\cdot10^{-19}\,\mathrm C`
> - `data-plain`: `|q| = F_G / E = 3,365·10⁻¹⁴ N / 7,00·10⁴ V/m = 4,807·10⁻¹⁹ C`
>
> **Schritt 4 — In Elementarladungen.** <span class="m">n = 4,807·10⁻¹⁹ C / 1,602·10⁻¹⁹ C = 3,001</span>
>
> Einheitenprobe: N/(V/m) = N·m/V = J/V = C ✓
>
> **Ergebnis: |q| = 4,807 · 10⁻¹⁹ C = 3,0 e.** Ein ganzzahliges Vielfaches — das ist die Beobachtung, auf der
> der Schluss auf die Quantelung der Ladung beruht.

---

### 5.3 ue3 — Welche Bahn beschreibt das Elektron im Querfeld? (Multiple Choice)

`<div class="aufgabe" data-mc="ue3">`, `<span class="ab">Anforderungsbereich I</span>`,
**vier** Optionen, mit Hilfen 1–3.

**Frage:**

> Ein Elektron fliegt mit der Geschwindigkeit <span class="m">v₀</span> senkrecht zu den Feldlinien in ein
> homogenes elektrisches Feld zwischen zwei Platten ein. Welche Aussage über seine Bahn **im Feld** ist richtig?

| `data-i` | Option |
|---|---|
| 0 | Eine Kreisbahn, weil die Kraft ständig senkrecht auf der Geschwindigkeit steht. |
| 1 | Eine Gerade entlang einer Feldlinie, weil das Elektron der Feldlinie folgt. |
| 2 | Eine Parabel: quer zum Feld gleichförmig, längs des Feldes (entgegengesetzt zu dessen Richtung) gleichmäßig beschleunigt. |
| 3 | Zuerst geradeaus, beim Eintritt ein Knick, danach wieder eine Gerade, weil die Kraft nur am Rand des Feldes wirkt. |

`r: 2`

**Feedback (`fb`):**

- `fb[0]`: „Eine Kreisbahn entsteht, wenn die Kraft **immer senkrecht auf der momentanen Geschwindigkeit**
  steht — das ist die Lorentzkraft im Magnetfeld. Die elektrische Kraft F = q·E hat dagegen eine feste
  Richtung, unabhängig davon, wohin sich das Elektron bewegt. Sie beschleunigt es längs der Feldlinien – beim Elektron
  entgegen der Feldrichtung – und ändert dabei Betrag und Richtung der Geschwindigkeit."
- `fb[1]`: „Das ist die Fehlvorstellung 'Feldlinie gleich Bahn'. Die Feldlinie zeigt die Richtung der **Kraft**,
  nicht der Geschwindigkeit. Das Elektron hat eine Anfangsgeschwindigkeit quer dazu, die erhalten bleibt, und
  bekommt längs der Feldlinien zusätzlich Geschwindigkeit: Die Bahn krümmt sich, verläuft aber nicht
  entlang der Feldlinie. Genau wie beim waagerechten Wurf: Die Gewichtskraft zeigt nach unten, die Kugel fliegt
  nicht senkrecht."
- `fb[2]`: „Richtig. In x-Richtung gibt es keine Kraft, also x = v₀·t; in y-Richtung wirkt die konstante Kraft
  F = |q|·E, also y = ½·a·t². Eliminiert man t, bleibt y ∼ x²: eine Parabel wie beim waagerechten Wurf, nur mit
  a = |q|·E/m statt g."
- `fb[3]`: „Die Kraft wirkt nicht nur am Rand, sondern **überall im homogenen Feld und die ganze Zeit**, solange
  das Elektron zwischen den Platten ist. Die Quergeschwindigkeit wächst deshalb stetig, v_y = a·t, und die
  Bahn krümmt sich gleichmäßig. Einen Knick gäbe es nur, wenn die Kraft plötzlich einsetzte; erst hinter dem
  Plattenende ist die Bahn wieder eine Gerade."

**Hilfe 1 (Tipp):**

> Vergleiche mit dem waagerechten Wurf aus der Einführungsphase: Dort gibt es eine Kraft in **einer**
> Richtung und eine Anfangsgeschwindigkeit in einer **anderen**. Was ist hier die Kraft, und wie ändert sie
> sich unterwegs?

**Hilfe 2 (Ansatz):**

> Zerlege die Bewegung in zwei unabhängige Richtungen. Längs der Flugrichtung <span class="m">x</span>: keine
> Kraft. Quer dazu <span class="m">y</span>: konstante Beschleunigung <span class="m">a = |q|·E/m</span>.
> Schreibe <span class="m">x(t)</span> und <span class="m">y(t)</span> hin und eliminiere die Zeit; die Form von
> <span class="m">y(x)</span> verrät dir die Bahn.

**Hilfe 3 (Lösungsweg):**

> **Schritt 1.** Kraft im Feld: <span class="m">F = q·E</span>, konstant nach Betrag und Richtung, quer zu
> <span class="m">v₀</span>.
>
> **Schritt 2.** <span class="m">x(t) = v₀·t</span> und <span class="m">y(t) = ½·a·t²</span> mit
> <span class="m">a = |q|·E/m</span> (das Vorzeichen von <span class="m">q</span> bestimmt nur die Richtung).
>
> **Schritt 3.** Aus der ersten Gleichung <span class="m">t = x/v₀</span>, eingesetzt:
> <span class="m">y = a/(2·v₀²) · x²</span>, also **y proportional zu x²: eine Parabel**.
>
> **Schritt 4 — Die anderen Optionen prüfen.** Kreis: Die Kraft wäre stets senkrecht zu <span class="m">v</span>
> (Magnetfeld). Gerade entlang der Feldlinie: Dann wäre <span class="m">v₀</span> null. Knick: Die Kraft ist nicht
> nur am Rand, sondern überall vorhanden.
>
> **Ergebnis: Option 2, Parabel.**

---

### 5.4 ue4 — Zuordnung: vier Abhängigkeiten, vier Diagramme

`<div class="aufgabe" data-num="ue4">`, `<span class="ab">Anforderungsbereich II</span>`
Das ist die **einzige** Zuordnungsaufgabe des Moduls (Engine läuft über einen festen Selektor).

**Aufgabentext:**

> Vier Messreihen zur Beschleunigung und Ablenkung geladener Teilchen, vier Diagramme. Ordne jeder Messreihe
> den passenden Kurvenverlauf zu. Die Achsen sind jeweils bei null skaliert; auf Zahlenwerte kommt es nicht an,
> nur auf die Form.

**Die vier Diagramme** als Inline-SVG in `<div class="diagramme">`, jeweils
`viewBox="0 0 170 110"`, Achsen in `#94a3b8`, Kurve in `#1d4ed8` mit `stroke-width="2.5"`,
`fill="none"`. Achsen einheitlich: x-Achse `16,88 158,88`, y-Achse `22,94 22,14`.

| Bild | `figcaption` | Verlauf | `points` |
|---|---|---|---|
| A | A | Wurzelkurve, steigt, wird flacher | `22,88 28,73 35,66 42,62 48,58 54,54 61,51 68,48 74,45 80,42 87,40 94,38 100,35 106,33 113,31 120,29 126,27 132,25 139,23 146,22 152,20` |
| B | B | Ursprungsgerade | `22,88 152,20` |
| C | C | Hyperbel, fällt | `36,20 40,32 45,41 49,47 54,52 58,56 63,59 67,61 72,64 76,65 81,67 85,68 90,70 94,71 98,72 103,72 107,73 112,74 116,74 121,75 125,76 130,76 134,76 139,77 143,77 148,78 152,78` |
| D | D | waagerechte Gerade | `22,48 152,48` |

**Die vier Zeilen** in `<div class="zuordnung">`, in **dieser** Markup-Reihenfolge
(sie entspricht bewusst **nicht** der Diagrammreihenfolge A–D):

| Nr. | Situationsbeschreibung | `data-loesung` |
|---|---|---|
| 1 | Ein Elektronenstrahl wird mit der Spannung <span class="m">U_B</span> beschleunigt und im Plattenpaar mit **fester** Ablenkspannung <span class="m">U_A</span> abgelenkt. Du veränderst <span class="m">U_B</span>. Aufgetragen ist der Betrag der Ablenkung <span class="m">y_a</span> am Plattenende gegen <span class="m">U_B</span>. | **C** |
| 2 | Ein Elektron wird aus der Ruhe mit der Spannung <span class="m">U_B</span> beschleunigt. Aufgetragen ist die Endgeschwindigkeit <span class="m">v</span> gegen <span class="m">U_B</span>. | **A** |
| 3 | Teilchen gleicher Ladung <span class="m">|q|</span>, aber sehr verschiedener Masse (etwa Elektron und Proton) werden mit derselben Spannung <span class="m">U_B</span> beschleunigt und mit derselben Spannung <span class="m">U_A</span> abgelenkt. Aufgetragen ist der Betrag der Ablenkung <span class="m">y_a</span> gegen die Masse <span class="m">m</span>. | **D** |
| 4 | Ein Elektronenstrahl mit **fester** Beschleunigungsspannung wird im Plattenpaar abgelenkt. Du veränderst die Ablenkspannung <span class="m">U_A</span>. Aufgetragen ist der Betrag der Ablenkung <span class="m">y_a</span> gegen <span class="m">U_A</span>. | **B** |

Lösungsfolge in Markup-Reihenfolge: **C – A – D – B**.
Jedes `<select>` enthält `…` (leer) · A · B · C · D.

**Begründung jeder Zuordnung** (gehört in die Rückmeldung bei vollständiger Lösung):

| Zeile | Rechnung | Form |
|---|---|---|
| 1 | <span class="m">y_a = U_A·L²/(4·d·U_B) = k/U_B</span>, <span class="m">U_B</span> im Nenner | umgekehrt proportional → Hyperbel **C** |
| 2 | <span class="m">v = √(2·e·U_B/m) = k·√U_B</span> | Wurzelfunktion → **A** |
| 3 | <span class="m">y_a</span> enthält weder <span class="m">m</span> noch <span class="m">q</span> | konstant → Waagerechte **D** |
| 4 | <span class="m">y_a = k·U_A</span>, <span class="m">U_A</span> im Zähler | proportional → Ursprungsgerade **B** |

**Rückmeldungstext bei Teilerfolg** (nennt die Strategie, nicht die Lösung):

> Noch nicht alles passt. Geh jede Zeile in zwei Schritten durch: **Erstens** — welche Größe wird verändert,
> und welche Formel verbindet sie mit der aufgetragenen? **Zweitens** — steht die veränderte Größe in dieser
> Formel im Zähler (Gerade), im Nenner (Hyperbel), unter einer Wurzel (Wurzelkurve) oder gar nicht
> (Waagerechte)?

**Rückmeldungstext bei vollständiger Lösung:** „Richtig, alle vier stimmen. Merk dir das Muster: Zeile 1 und 4
unterscheiden sich nur darin, welche der beiden Spannungen verändert wird — die eine steht im Nenner, die
andere im Zähler. Und Zeile 3 ist die zentrale Aussage des Kapitels: Masse und Ladung kürzen sich aus der
Bahn heraus."

**Hilfe 1 (Tipp):**

> Schreibe zuerst hin, **welche Größe du veränderst** und **welche du aufträgst**. Halte alles andere fest.
> Dann suchst du die eine Formel, in der beide vorkommen. Wer sofort auf die Achsenbeschriftung schaut, greift
> in der Hälfte der Fälle zur falschen Formel.

**Hilfe 2 (Ansatz):**

> **Schritt 1 — Formeln.**
> - `data-tex`: `v = \sqrt{\dfrac{2\,|q|\,U_B}{m}}, \qquad y_a = \dfrac{U_A\,L^2}{4\,d\,U_B}`
> - `data-plain`: `v = √(2·|q|·U_B/m),   y_a = U_A · L² / (4·d·U_B)`
>
> **Schritt 2 — Form ablesen.** Stelle so um, dass nur die veränderte Größe als Variable übrig bleibt, alles
> andere ist eine Konstante <span class="m">k</span>:
>
> | Die veränderte Größe steht … | Kurve |
> |---|---|
> | im Zähler, erste Potenz (<span class="m">y = k·x</span>) | Ursprungsgerade |
> | im Nenner (<span class="m">y = k/x</span>) | Hyperbel |
> | unter einer Wurzel (<span class="m">y = k·√x</span>) | Wurzelkurve |
> | gar nicht in der Formel (<span class="m">y = k</span>) | Waagerechte |

**Hilfe 3 (Lösungsweg):**

> **Zeile 1 — U_A fest, U_B verändert, y_a gegen U_B.** <span class="m">y_a = U_A·L²/(4·d·U_B) = k/U_B</span>,
> also umgekehrt proportional. Kontrollzahlen (<span class="m">U_A = 100 V</span>, <span class="m">L = 6,0 cm</span>,
> <span class="m">d = 2,0 cm</span>): <span class="m">1000 V → 4,50 mm</span>,
> <span class="m">2000 V → 2,25 mm</span>, <span class="m">4000 V → 1,125 mm</span> — doppelte Spannung, halbe
> Ablenkung. **→ Diagramm C (Hyperbel).**
>
> **Zeile 2 — v gegen U_B.** <span class="m">v = √(2·e·U_B/m) = k·√U_B</span>. Kontrollzahlen (Elektron):
> <span class="m">500 V → 1,326·10⁷ m/s</span>, <span class="m">2000 V → 2,652·10⁷ m/s</span> — vierfache Spannung,
> doppelte Geschwindigkeit. **→ Diagramm A (Wurzelkurve).**
>
> **Zeile 3 — y_a gegen die Masse.** In <span class="m">y_a = U_A·L²/(4·d·U_B)</span> kommt <span class="m">m</span> nicht
> vor. Kontrollzahlen (<span class="m">U_B = 2000 V</span>): Elektron
> <span class="m">|y_a| = 2,25 mm</span>, Proton <span class="m">|y_a| = 2,25 mm</span> — 1836-fache Masse, dieselbe
> Ablenkung. **→ Diagramm D (Waagerechte).**
>
> **Zeile 4 — y_a gegen U_A.** <span class="m">y_a = k·U_A</span> mit
> <span class="m">k = L²/(4·d·U_B)</span>. Kontrollzahlen (<span class="m">U_B = 2000 V</span>):
> <span class="m">50 V → 1,125 mm</span>, <span class="m">100 V → 2,25 mm</span>,
> <span class="m">200 V → 4,50 mm</span>. **→ Diagramm B (Ursprungsgerade).**
>
> **Lösungsfolge in Markup-Reihenfolge: C – A – D – B.**
>
> **Merk dir das Muster, nicht die vier Antworten.** Die Zeilen 1 und 4 unterscheiden sich nur darin, welche
> Spannung verändert wird, und ergeben Hyperbel und Gerade. Die Zeilen 2 und 3 zeigen zwei Gesichter derselben
> Physik: In der Geschwindigkeit stecken Masse und Ladung, in der Bahn nicht mehr.

---

### 5.5 ue5 — Auslenkung auf dem Schirm einer Oszilloskopröhre

`<div class="aufgabe" data-num="ue5">`, `<span class="ab">Anforderungsbereich II</span>`

**Aufgabentext:**

> In einer Elektronenstrahlröhre werden Elektronen aus der Ruhe mit <span class="m">U_B = 1,2 kV</span>
> beschleunigt. Sie treten mittig in ein Plattenpaar der Länge <span class="m">L = 3,0 cm</span> im Abstand
> <span class="m">d = 8,0 mm</span> ein. An den Platten liegt <span class="m">U_A = 24 V</span>, die obere Platte ist
> positiv. Der Leuchtschirm steht <span class="m">D = 15 cm</span> hinter dem Plattenende.
>
> Berechne den **Betrag** der Auslenkung <span class="m">Y</span> des Leuchtflecks auf dem Schirm.

**Eingabe:** `Einheit…` (leer) · `mm` · `cm` · `m` · **`°`**
Der Distraktor **°** fängt die Verwechslung mit dem Ablenkwinkel ab, der auf dem Weg als Zwischenwert
entsteht (2,15°).

**`numDaten`-Eintrag:**

```js
ue5:{ wert:6.19, einheit:"mm", tol:0.10,
      alt:{wert:0.619, einheit:"cm"},
      ok:"Richtig. y_a = U_A·L²/(4·d·U_B) = 0,5625 mm am Plattenende, tan θ = 2·y_a/L = 0,0375, und Y = tan θ · (L/2 + D) = 0,0375 · 16,5 cm = 6,19 mm. Der Hauptteil, 5,63 mm, entsteht auf der geraden Strecke hinter den Platten, nur 0,56 mm im Feld selbst.",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. Gesucht ist eine Länge auf dem Schirm, also mm oder cm. Ein Grad-Wert wäre der Ablenkwinkel (2,15°), der nur ein Zwischenergebnis ist.",
      sonder:[
        {wert:5.625, text:"Das ist nur der Beitrag der Strecke hinter den Platten, D·tan θ = 150 mm · 0,0375. Es fehlt die Ablenkung y_a = 0,56 mm, die das Elektron schon im Feld erfahren hat. Zusammen: Y = y_a + D·tan θ = tan θ·(L/2 + D)."},
        {wert:0.5625, text:"Das ist nur die Ablenkung y_a am Plattenende. Danach fliegt das Elektron noch 15 cm geradeaus und wird dabei weiter nach oben getragen: Y = y_a + D·tan θ."},
        {wert:12.375, text:"Das ist doppelt so viel wie richtig. Vermutlich fehlt im Nenner von y_a ein Faktor 2, etwa weil die ½ aus y = ½·a·t² und die 2 aus v₀² = 2·e·U_B/m nicht beide eingesetzt wurden. Es gilt y_a = U_A·L²/(4·d·U_B) mit der 4 im Nenner."},
        {wert:24.75, text:"Das ist genau das Vierfache. Im Nenner von y_a fehlt die 4 (sie besteht aus 2 aus y = ½·a·t² und 2 aus v₀² = 2·e·U_B/m). Es gilt y_a = U_A·L²/(4·d·U_B)."}
      ],
      nah:"Die Größenordnung stimmt, der Wert nicht. Prüfe: Hast du hinter dem Plattenende noch die gerade Strecke D mitgenommen — am besten über tan θ · (L/2 + D)? Und sind L, d, D in Metern eingesetzt?",
      weit:"Das liegt um mehr als den Faktor zwei daneben. Vermutlich stimmt eine Umrechnung nicht (cm und mm in Meter) oder eine Formel steht auf dem Kopf. Nutze die Hilfen." }
```

**Hilfe 1 (Tipp):**

> Die Strecke hat zwei Teile: die kurze **im** Feld, wo die Bahn gekrümmt ist, und die lange **hinter** dem
> Feld, wo sie geradlinig verläuft. Berechne erst, wie stark das Elektron am Plattenende abgelenkt ist und
> unter welchem Winkel es austritt.

**Hilfe 2 (Ansatz):**

> Im Feld gilt die Parabelbahn, hinter dem Plattenende die Tangente daran:
> - `data-tex`: `y_a = \dfrac{U_A\,L^2}{4\,d\,U_B}, \qquad \tan\vartheta = \dfrac{2\,y_a}{L}, \qquad Y = \tan\vartheta\cdot\left(\dfrac{L}{2} + D\right)`
> - `data-plain`: `y_a = U_A · L² / (4·d·U_B),   tan θ = 2·y_a/L,   Y = tan θ · (L/2 + D)`
>
> Rechne alle Längen vorher in Meter um.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** U_B = 1200 V · L = 3,0 cm = 0,030 m · d = 8,0 mm = 8,0·10⁻³ m · D = 15 cm = 0,150 m · U_A = 24 V
>
> **Schritt 1 — Ablenkung am Plattenende.**
> - `data-tex`: `y_a = \dfrac{24\,\mathrm V \cdot (0{,}030\,\mathrm m)^2}{4 \cdot 8{,}0\cdot10^{-3}\,\mathrm m \cdot 1200\,\mathrm V} = \dfrac{2{,}16\cdot10^{-2}}{38{,}4}\,\mathrm m = 5{,}625\cdot10^{-4}\,\mathrm m = 0{,}5625\,\mathrm{mm}`
> - `data-plain`: `y_a = 24 V · (0,030 m)² / (4 · 8,0·10⁻³ m · 1200 V) = 2,16·10⁻² / 38,4 m = 5,625·10⁻⁴ m = 0,5625 mm`
>
> **Schritt 2 — Winkel.** <span class="m">tan ϑ = 2·y_a/L = 2 · 5,625·10⁻⁴ m/0,030 m = 0,0375</span>, also
> <span class="m">ϑ = 2,15°</span>.
>
> **Schritt 3 — Schirm.**
> - `data-tex`: `Y = \tan\vartheta\cdot\left(\dfrac{L}{2} + D\right) = 0{,}0375 \cdot (0{,}015\,\mathrm m + 0{,}150\,\mathrm m) = 6{,}19\cdot10^{-3}\,\mathrm m`
> - `data-plain`: `Y = tan θ · (L/2 + D) = 0,0375 · (0,015 m + 0,150 m) = 6,19·10⁻³ m`
>
> **Kontrolle.** <span class="m">Y = y_a + D·tan ϑ = 0,5625 mm + 150 mm · 0,0375 = 0,5625 mm + 5,625 mm = 6,19 mm</span>
> ✓. Zweiter Weg über die Zeit: <span class="m">v₀ = 2,054·10⁷ m/s</span>, <span class="m">t = L/v₀ = 1,46 ns</span>,
> <span class="m">a = e·U_A/(m·d) = 5,28·10¹⁴ m/s²</span>, <span class="m">y_a = ½·a·t² = 0,5625 mm</span>.
> Das Elektron trifft die Platte nicht: <span class="m">y_a < d/2 = 4,0 mm</span>.
>
> **Ergebnis: |Y| = 6,19 mm nach oben** (zur positiven Platte hin).

---

### 5.6 ue6 — Ladung aus Sinkgeschwindigkeit und Schwebespannung

`<div class="aufgabe" data-num="ue6">`, `<span class="ab">Anforderungsbereich II</span>`

**Aufgabentext:**

> Ein Öltröpfchen (Dichte <span class="m">ρ = 875 kg/m³</span>) sinkt ohne Feld gleichförmig mit
> <span class="m">v_s = 0,140 mm/s</span>. Danach schwebt es bei der Spannung <span class="m">U_s = 430 V</span> im
> Kondensator mit <span class="m">d = 5,00 mm</span>. Luft: <span class="m">η = 1,81 · 10⁻⁵ Pa·s</span>,
> <span class="m">g = 9,81 m/s²</span>; Auftrieb vernachlässigen. Der Radius des Tröpfchens ist **nicht** gegeben.
>
> Berechne die Ladung des Tröpfchens in Vielfachen der Elementarladung
> <span class="m">e = 1,602 · 10⁻¹⁹ C</span>.

**Eingabe:** `Einheit…` (leer) · `e` · `C` · **`kg`** · **`µm`**
Die Distraktoren **kg** und **µm** fangen die Zwischenergebnisse Masse und Radius ab.

**`numDaten`-Eintrag:**

```js
ue6:{ wert:4.0, einheit:"e", tol:0.1,
      alt:{wert:6.408e-19, einheit:"C"},
      ok:"Richtig. r = √(9·η·v_s/(2·ρ·g)) = 1,153 µm, m = (4/3)·π·r³·ρ = 5,612·10⁻¹⁵ kg, |q| = m·g·d/U_s = 6,401·10⁻¹⁹ C = 3,996 e ≈ 4 e. Das Ergebnis liegt bis auf 0,1 % bei einem Vielfachen von e — so sieht die Quantelung in einer einzelnen Messung aus.",
      falschEinheit:"Der Zahlenwert passt, die Einheit nicht. Gesucht ist eine Ladung, in e oder in C. kg wäre die Masse des Tröpfchens (5,6·10⁻¹⁵ kg) und µm sein Radius (1,15 µm), beides nur Zwischenergebnisse.",
      sonder:[
        {wert:32.0, text:"Das ist genau das Achtfache von 4 e. Vermutlich wurde der **Durchmesser** oder der doppelte Radius als r in m = (4/3)·π·r³·ρ eingesetzt: 2³ = 8. Aus v_s folgt der Radius r = 1,153 µm, nicht der Durchmesser."},
        {wert:0.42, text:"Hier fehlt der Faktor 9/2 in der Radiusformel: Mit r = √(η·v_s/(ρ·g)) statt r = √(9·η·v_s/(2·ρ·g)) wird der Radius zu klein und wegen r³ die Ladung viel zu klein. Leite die Formel aus m·g = 6·π·η·r·v_s mit m = (4/3)·π·r³·ρ noch einmal her."}
      ],
      nah:"Nicht ganz. Zwei typische Stellen: Ist der Radius aus v_s berechnet mit r = √(9·η·v_s/(2·ρ·g)) — und dann als r³ in die Masse eingegangen? Und ist v_s in m/s eingesetzt (0,140 mm/s = 1,40·10⁻⁴ m/s), d in m?",
      weit:"Das liegt weit daneben. Meist steckt eine falsche Zehnerpotenz bei v_s (mm/s → m/s) oder ein fehlender Zwischenschritt dahinter: Erst der Radius, dann die Masse, dann die Ladung. Nutze die Hilfen." }
```

**Hilfe 1 (Tipp):**

> Aus dem Schweben allein bekommst du nur dann die Ladung, wenn du die Masse kennst. Die ist nicht gegeben — aber
> das **Sinken ohne Feld** verrät sie dir indirekt. Frag dich: Welche zwei Kräfte sind beim gleichförmigen
> Sinken gleich groß, und was steckt in der einen von ihnen an Geometrie?

**Hilfe 2 (Ansatz):**

> Drei Schritte: Aus dem Sinken (Gewichtskraft gleich Stokes-Reibung) folgt der Radius, aus dem Radius die Masse,
> aus dem Schweben die Ladung:
> - `data-tex`: `r = \sqrt{\dfrac{9\,\eta\,v_s}{2\,\rho\,g}}, \qquad m = \tfrac{4}{3}\pi r^3\rho, \qquad |q| = \dfrac{m\,g\,d}{U_s}`
> - `data-plain`: `r = √(9·η·v_s/(2·ρ·g)),   m = (4/3)·π·r³·ρ,   |q| = m·g·d/U_s`
>
> Alles in SI-Einheiten einsetzen; am Ende durch <span class="m">e</span> teilen.

**Hilfe 3 (Lösungsweg):**

> **Gegeben:** v_s = 0,140 mm/s = 1,40·10⁻⁴ m/s · U_s = 430 V · d = 5,00·10⁻³ m · ρ = 875 kg/m³ ·
> η = 1,81·10⁻⁵ Pa·s · g = 9,81 m/s²
>
> **Schritt 1 — Radius.**
> - `data-tex`: `r = \sqrt{\dfrac{9 \cdot 1{,}81\cdot10^{-5}\,\mathrm{Pa\,s}\cdot 1{,}40\cdot10^{-4}\,\mathrm{m/s}}{2\cdot 875\,\mathrm{kg/m^3}\cdot 9{,}81\,\mathrm{m/s^2}}} = \sqrt{1{,}328\cdot10^{-12}\,\mathrm{m^2}} = 1{,}153\cdot10^{-6}\,\mathrm m`
> - `data-plain`: `r = √(9 · 1,81·10⁻⁵ · 1,40·10⁻⁴ / (2 · 875 · 9,81)) m = √(1,328·10⁻¹² m²) = 1,153·10⁻⁶ m`
>
> **Schritt 2 — Masse und Gewichtskraft.**
> <span class="m">m = (4/3)·π·(1,153·10⁻⁶ m)³ · 875 kg/m³ = 5,612·10⁻¹⁵ kg</span>,
> <span class="m">F_G = m·g = 5,505·10⁻¹⁴ N</span>.
>
> **Schritt 3 — Ladung.**
> - `data-tex`: `|q| = \dfrac{F_G\,d}{U_s} = \dfrac{5{,}505\cdot10^{-14}\,\mathrm N \cdot 5{,}00\cdot10^{-3}\,\mathrm m}{430\,\mathrm V} = 6{,}401\cdot10^{-19}\,\mathrm C`
> - `data-plain`: `|q| = F_G · d / U_s = 5,505·10⁻¹⁴ N · 5,00·10⁻³ m / 430 V = 6,401·10⁻¹⁹ C`
>
> **Schritt 4 — In Elementarladungen.** <span class="m">n = 6,401·10⁻¹⁹ C/1,602·10⁻¹⁹ C = 3,996 ≈ 4</span>
>
> **Kontrolle.** Stokes-Reibung bei <span class="m">v_s</span>:
> <span class="m">6·π·η·r·v_s = 5,505·10⁻¹⁴ N = m·g</span> ✓; Reynoldszahl
> <span class="m">Re = 2,1·10⁻⁵ ≪ 1</span>, Stokes gilt. Feldstärke
> <span class="m">E = 430 V/5,00 mm = 86 kV/m</span>, weit unter dem Durchschlag.
>
> **Ergebnis: |q| = 6,40 · 10⁻¹⁹ C = 4,0 e.** Die Ladung geht über <span class="m">r³ ∼ v_s^{3/2}</span>
> ein: Ein Ablesefehler von 1 % bei <span class="m">v_s</span> verschiebt das Ergebnis um 1,5 %.

---

### 5.7 ue7 — Bewertung: „Das schwere Proton wird schwächer abgelenkt"

`<div class="aufgabe" data-num="ue7">`, `<span class="ab">Anforderungsbereich III</span>`,
`<textarea>` und ein Knopf „Musterlösung anzeigen“ (`<button data-loesung=\"ue7\">`), Musterlösung in
`.hilfe-text[data-stufe=\"9\"]`.

**Aufgabentext:**

> Im Kurs streiten zwei: **Anna** sagt: „Ein Proton ist 1836-mal schwerer als ein Elektron, also wird es im
> Plattenpaar viel schwächer abgelenkt." **Ben** sagt: „Die Ablenkung hängt gar nicht von der Teilchenart ab."
>
> Nimm zu beiden Aussagen physikalisch begründet Stellung. Rechne dazu für die Ablenkeinheit aus 2.4
> (<span class="m">L = 6,0 cm</span>, <span class="m">d = 2,0 cm</span>, <span class="m">U_A = 100 V</span>) die Ablenkung
> <span class="m">y_a</span> von Elektron und Proton in zwei Fällen:
> **(I)** beide wurden mit derselben Spannung <span class="m">U_B = 2,0 kV</span> beschleunigt,
> **(II)** beide treten mit derselben Geschwindigkeit <span class="m">v₀ = 2,65 · 10⁷ m/s</span> ein.
> Gib am Ende an, welche Angabe fehlt, damit sich der Streit überhaupt entscheiden lässt.

**Musterlösung — erwartete Argumentation** (Knopf „Musterlösung anzeigen“):

> **Gemeinsame Rechnung.** Feldstärke <span class="m">E = U_A/d = 100 V/0,020 m = 5,0 kV/m</span>, Beschleunigung
> <span class="m">a = e·E/m</span>: Elektron <span class="m">a_e = 8,794·10¹⁴ m/s²</span>, Proton
> <span class="m">a_p = 4,788·10¹¹ m/s²</span> (das Verhältnis ist <span class="m">m_e/m_p = 1/1836,6</span>).
>
> **Fall II — gleiche Geschwindigkeit <span class="m">v₀ = 2,65·10⁷ m/s</span>.** Beide brauchen dieselbe Zeit
> <span class="m">t = L/v₀ = 2,26 ns</span> für die Platten. Dann ist
> <span class="m">y_e = ½·a_e·t² = 2,25 mm</span> und
> <span class="m">y_p = ½·a_p·t² = 1,23·10⁻³ mm = 1,2 µm</span>. Das Verhältnis ist genau
> <span class="m">y_p/y_e = m_e/m_p = 1/1836</span>. **Anna hat recht** — aber nur unter der Voraussetzung, die sie
> nicht nennt: gleiche Geschwindigkeit. (Ein Proton mit diesem Tempo hätte eine Energie von 3,67 MeV.)
>
> **Fall I — gleiche Beschleunigungsspannung <span class="m">U_B = 2,0 kV</span>.** Jetzt haben sie **nicht**
> dasselbe Tempo: <span class="m">v_e = 2,652·10⁷ m/s</span>, <span class="m">v_p = 6,189·10⁵ m/s</span>. Das Proton
> braucht deshalb die längere Zeit, <span class="m">t_p = 96,95 ns</span> statt <span class="m">t_e = 2,26 ns</span>: den Faktor
> <span class="m">√(m_p/m_e) = 42,86</span>. Seine Beschleunigung ist um den Faktor 1836,6 kleiner, die Zeit im Quadrat
> aber um <span class="m">42,86² = 1836,6</span> größer; beides hebt sich auf:
> <span class="m">y_e = y_p = 2,25 mm</span>, allgemein (im Betrag) <span class="m">|y_a| = U_A·L²/(4·d·U_B)</span> ohne
> <span class="m">q</span> und <span class="m">m</span>. **Ben hat recht** — wieder mit einer Voraussetzung: gleiche
> Beschleunigungsspannung. Die Richtung ist dabei entgegengesetzt: Das Elektron wird zur positiven, das Proton zur
> negativen Platte gezogen. Insofern hängt die Ablenkung doch von der Teilchenart ab, nämlich vom
> **Vorzeichen** der Ladung.
>
> **Fazit.** Beide Aussagen sind für sich unvollständig. Entscheidbar wird der Streit durch die Angabe, **wie die
> Teilchen auf Geschwindigkeit gekommen sind**: über die Beschleunigungsspannung (dann ist die Bahn für alle
> Teilchen gleich, nur das Vorzeichen zählt) oder mit vorgegebenem Tempo (dann gilt <span class="m">y_a ∼ q/m</span>).

**Bewertungskriterien:**

> **Bewertungskriterien**
> · beide Aussagen einzeln geprüft und keine pauschal als richtig oder falsch abgetan ·
> Fall II gerechnet oder begründet mit <span class="m">y_a ∼ q/m</span>, Verhältnis 1/1836 belegt ·
> Fall I mit dem Energiesatz gerechnet, Kürzen von <span class="m">q</span> und <span class="m">m</span> gezeigt, Ergebnis 2,25 mm bei beiden ·
> Ursache der Kompensation benannt (kleinere Beschleunigung, aber längere Verweildauer) ·
> entgegengesetzte Ablenkrichtung als Folge des Ladungsvorzeichens erwähnt ·
> abschließendes Urteil, dass die fehlende Angabe „gleiche Geschwindigkeit oder gleiche Spannung" den Streit entscheidet.

---

### 5.8 ue8 — Bewertung: „Die Elementarladung ist die kleinste gemessene Ladung"

`<div class="aufgabe" data-num="ue8">`, `<span class="ab">Anforderungsbereich III</span>`,
`<textarea>` und ein Knopf „Musterlösung anzeigen“ (`<button data-loesung=\"ue8\">`), Musterlösung in
`.hilfe-text[data-stufe=\"9\"]`.

**Aufgabentext:**

> Bei einem Millikan-Versuch wurden fünf Tröpfchen ausgewertet. Die Ladungen (jeweils mit einer Unsicherheit von
> etwa 1,5 %) lauten, in Einheiten von <span class="m">10⁻¹⁹ C</span>:
> **3,22 · 4,79 · 6,41 · 8,05 · 9,58.**
>
> Ein Schüler schreibt in sein Protokoll: *„Die kleinste gemessene Ladung ist 3,22·10⁻¹⁹ C. Das ist die
> Elementarladung."*
>
> Beurteile diese Schlussfolgerung anhand der Daten, gib die beste Schätzung für die Elementarladung an und
> begründe, wie sicher man aus solchen Daten auf eine **Quantelung** der Ladung schließen kann und was die Daten
> **nicht** ausschließen.

**Musterlösung — erwartete Argumentation** (Knopf „Musterlösung anzeigen“):

> **1. Die Schlussfolgerung ist falsch.** Wäre <span class="m">3,22·10⁻¹⁹ C</span> die Elementarladung, müssten alle
> Werte ganze Vielfache davon sein. Es ergibt sich aber
> <span class="m">4,79/3,22 = 1,49</span>, <span class="m">6,41/3,22 = 1,99</span>,
> <span class="m">8,05/3,22 = 2,50</span>, <span class="m">9,58/3,22 = 2,98</span>: zwei davon liegen bei
> halbzahligen Werten. 4,79 ist kein ganzes Vielfaches von 3,22 und liegt weit außerhalb der 1,5 %.
>
> **2. Der größte gemeinsame Teiler.** Die Differenzen benachbarter Werte sind
> <span class="m">1,57 · 1,62 · 1,64 · 1,53</span> (Mittelwert <span class="m">1,59</span>). Teilt man alle Werte durch
> <span class="m">1,60</span>, erhält man
> <span class="m">2,01 · 2,99 · 4,01 · 5,03 · 5,99</span>, also **ganzzahlig innerhalb von etwa 1 %**, passend zu
> <span class="m">n = 2 · 3 · 4 · 5 · 6</span>.
>
> **3. Beste Schätzung.**
> - `data-tex`: `e = \dfrac{\sum q}{\sum n} = \dfrac{(3{,}22 + 4{,}79 + 6{,}41 + 8{,}05 + 9{,}58)\cdot10^{-19}\,\mathrm C}{2+3+4+5+6} = \dfrac{32{,}05\cdot10^{-19}\,\mathrm C}{20} = 1{,}6025\cdot10^{-19}\,\mathrm C`
> - `data-plain`: `e = Σq / Σn = (3,22 + 4,79 + 6,41 + 8,05 + 9,58)·10⁻¹⁹ C / (2+3+4+5+6) = 32,05·10⁻¹⁹ C / 20 = 1,6025·10⁻¹⁹ C`
>
> Das weicht um 0,03 % vom heutigen Wert <span class="m">1,602·10⁻¹⁹ C</span> ab, weit innerhalb der
> angegebenen Unsicherheit (die Summenbildung mittelt Zufallsfehler heraus).
>
> **4. Wie sicher ist der Schluss auf Quantelung?** Er ist **gut gestützt, aber nicht bewiesen.** Dafür spricht:
> Alle fünf Werte liegen innerhalb ihrer Unsicherheit auf ganzzahligen Vielfachen, und fünf zufällige Werte
> zeigten das nur mit sehr kleiner Wahrscheinlichkeit. Voraussetzung für die Zuordnung ist die Auflösung: Bei
> <span class="m">1,5 %</span> Unsicherheit unterscheidet man <span class="m">n</span> und <span class="m">n+1</span> nur bis
> etwa <span class="m">n ≈ 33</span> (dann ist 1,5 % von <span class="m">q</span> gleich einem halben <span class="m">e</span>).
> Größere Ladungen wären nicht mehr eindeutig zuzuordnen.
>
> **5. Was die Daten nicht ausschließen.** Wäre die wahre Einheit <span class="m">e/2 = 0,80·10⁻¹⁹ C</span>, wären
> dieselben Werte die Vielfachen <span class="m">4 · 6 · 8 · 10 · 12</span> — kein Widerspruch. Daten mit größten
> Ladungen zeigen nur, dass die Portion **höchstens** <span class="m">1,6·10⁻¹⁹ C</span> ist. Zweifel räumt man aus mit
> Tröpfchen, die **wenige** Ladungen tragen (die kleinste beobachtete Ladung ist 1,6 und nicht 0,8),
> und mit **Ladungsänderungen**: Ein Tröpfchen wird durch Ionisation geladen oder entladen, und die Sprünge
> sind Vielfache von genau **einem** Quant.
>
> **Fazit.** Der Schüler hat Recht darin, dass man den kleinsten Wert betrachten muss, aber er hätte prüfen
> müssen, ob die anderen Werte ganze Vielfache sind. Die Elementarladung ist
> <span class="m">e = 1,60·10⁻¹⁹ C</span>; die Quantelung der Ladung ist die gestützte Deutung, nicht die reine Messung.

**Bewertungskriterien:**

> **Bewertungskriterien**
> · Schlussfolgerung mit den Quotienten <span class="m">q/3,22</span> als falsch erkannt (nicht ganzzahlig) ·
> gemeinsamen Teiler <span class="m">≈ 1,6·10⁻¹⁹ C</span> über Quotienten oder Differenzen gefunden ·
> Ganzzahligkeit der Faktoren 2 · 3 · 4 · 5 · 6 im Rahmen der Unsicherheit belegt ·
> beste Schätzung 1,60·10⁻¹⁹ C (Rechnung oder Mittelung) angegeben ·
> Grenze der Aussage benannt: Daten allein schließen kleinere Einheiten (<span class="m">e/2</span>) nicht aus ·
> Maßnahme genannt (kleine Ladungen, Ladungsänderungen) oder Auflösungsgrenze der Messung diskutiert.

---

### 5.9 ue9 — Bewertung: Ist die klassische Rechnung für die Röntgenröhre zulässig?

`<div class="aufgabe" data-num="ue9">`, `<span class="ab">Anforderungsbereich III</span>`,
`<textarea>` und ein Knopf „Musterlösung anzeigen“ (`<button data-loesung=\"ue9\">`), Musterlösung in
`.hilfe-text[data-stufe=\"9\"]`.

**Aufgabentext:**

> Ein Lernender rechnet für die Röntgenröhre aus dem Einstieg mit <span class="m">U_B = 65 kV</span>:
> <span class="m">v = √(2·e·U_B/m_e) = 1,51·10⁸ m/s</span>. Dazu schreibt er: *„Die Formel ist aus der Mechanik und
> gilt überall, wo ein Teilchen im Feld beschleunigt wird. Das Ergebnis ist also richtig."*
>
> Beurteile die Aussage. Belege dein Urteil mit einer Größenordnung und gib an, wie sich das Ergebnis ändert, wenn
> man die Ruheenergie <span class="m">m_e·c² = 511 keV</span> berücksichtigt. Die relativistischen Formeln aus 2.3
> darfst du benutzen.

**Musterlösung — erwartete Argumentation** (Knopf „Musterlösung anzeigen“):

> **1. Größenordnung.** <span class="m">v/c = 1,512·10⁸/2,998·10⁸ = 0,504</span> — die halbe Lichtgeschwindigkeit.
> Die Faustregel <span class="m">v/c < 0,1</span> für die klassische Rechnung ist damit weit überschritten (Faktor 5).
>
> **2. Relativistisch gerechnet.** <span class="m">E_kin = 65 keV</span>, <span class="m">γ = 1 + 65/511,06 = 1,1272</span>,
> <span class="m">v/c = √(1 − 1/1,1272²) = 0,4615</span>, also <span class="m">v = 1,383·10⁸ m/s</span>.
>
> **3. Abweichung.** Das klassische Ergebnis liegt um <span class="m">1,512/1,383 − 1 = 9,3 %</span> **zu hoch**.
> Die Gegenprobe über die Energie: Setzt man den richtigen Wert <span class="m">1,383·10⁸ m/s</span> in
> <span class="m">½·m_e·v²</span> ein, erhält man nur <span class="m">54,4 keV</span> statt der zugeführten
> <span class="m">65 keV</span> (16 % zu wenig). Die Bewegungsenergie steckt nicht mehr vollständig im
> Term <span class="m">½·m·v²</span>.
>
> **4. Urteil.** Die Aussage ist **falsch**. Die Formel folgt aus der klassischen Bewegungsenergie
> <span class="m">½·m·v²</span>, und die ist nur für <span class="m">v ≪ c</span> gültig; sie gilt eben nicht „überall".
> Die **Spannungsformel** <span class="m">E_kin = |q|·U_B</span> gilt dagegen immer, nur die Umrechnung in eine
> Geschwindigkeit nicht. Bei 255 kV käme klassisch <span class="m">v = c</span> heraus, bei 511 kV sogar 1,41 c —
> spätestens dort wäre der Fehler offensichtlich. Ein Proton bräuchte für <span class="m">v/c = 0,1</span>
> dagegen rund 4,7 MV; für schwere Teilchen bleibt die Rechnung klassisch.
>
> **5. Einordnung für Prüfungen.** Ob im Zentralabitur relativistisch gerechnet werden muss, hängt vom
> Aufgabentext ab (Hinweis siehe Lehrerteil); wichtig ist die begründete Bewertung des Ergebnisses.

**Bewertungskriterien:**

> **Bewertungskriterien**
> · <span class="m">v/c = 0,50</span> berechnet und mit der Faustregel 0,1 verglichen ·
> Gültigkeitsbereich der klassischen Bewegungsenergie als Ursache benannt (nicht das Ergebnis pauschal als „falsch" abgetan) ·
> relativistischer Wert <span class="m">0,46 c</span> bzw. <span class="m">1,38·10⁸ m/s</span> mit Rechenweg angegeben ·
> Abweichung von rund 9 % quantifiziert ·
> zwischen <span class="m">E_kin = |q|·U_B</span> (immer gültig) und der Umrechnung in <span class="m">v</span> (nur klassisch) unterschieden ·
> Zusatzpunkt für die Extremfälle (<span class="m">v ≥ c</span> bei 255 kV) oder den Protonenvergleich.

---

## 6 · Abschluss

`<section id="abschluss">`, `.stufe`-Nummer **6**,
Überschrift **Zusammenfassung und Selbstcheck**.

### 6.1 Vier Kernaussagen (je ein `<div class="merksatz">`)

**Kernaussage 1 — Nur die Spannung zählt.**
Titel: *Vom Feld zur Bewegungsenergie.* Ein Teilchen, das im Feld die Spannung <span class="m">U_B</span>
durchläuft, gewinnt die Energie <span class="m">|q|·U_B</span>, unabhängig von Plattenabstand, Feldstärke und
Masse. Die Geschwindigkeit folgt aus der Bewegungsenergie und wächst nur mit der **Wurzel** der Spannung; in
ihr steckt die Masse. Bei gleicher Energie ist ein Elektron 43-mal schneller als ein Proton. Die Formel
gilt nur, solange <span class="m">v ≪ c</span> ist, die Faustregel ist <span class="m">v/c < 0,1</span>.

- `data-tex`: `|q|\,U_B = \tfrac{1}{2}\,m\,v^2 \quad\Longrightarrow\quad v = \sqrt{\dfrac{2\,|q|\,U_B}{m}}`
- `data-plain`: `|q| · U_B = ½ · m · v²   ⟹   v = √(2 · |q| · U_B / m)`

**Kernaussage 2 — Quer zum Feld entsteht eine Parabel.**
Titel: *Waagerechter Wurf mit anderer Beschleunigung.* Quer zu den Feldlinien ist die Bewegung die Überlagerung
einer gleichförmigen und einer gleichmäßig beschleunigten Bewegung, also eine Parabel. Die Feldlinie zeigt die
Richtung der Kraft, nicht der Bahn. Bei gleicher Beschleunigungsspannung kürzen sich Ladung und Masse aus der Bahn
heraus; das Vorzeichen der Ladung legt nur die Richtung fest.

- `data-tex`: `y_a = -\,\mathrm{sgn}(q)\,\dfrac{U_A\,L^2}{4\,d\,U_B}, \qquad \tan\vartheta = -\,\mathrm{sgn}(q)\,\dfrac{U_A\,L}{2\,d\,U_B}, \qquad Y = \tan\vartheta\cdot\left(\dfrac{L}{2} + D\right)`
- `data-plain`: `y_a = −sgn(q) · U_A · L² / (4·d·U_B),   tan θ = −sgn(q) · U_A · L / (2·d·U_B),   Y = tan θ · (L/2 + D)`

**Kernaussage 3 — Millikan macht aus Zeit, Spannung und Länge eine Ladung.**
Titel: *Zwei Messungen, eine Ladung.* Ohne Feld sinkt das Öltröpfchen mit der Geschwindigkeit, bei der die
Stokes-Reibung die Gewichtskraft ausgleicht; daraus folgen Radius und Masse. Mit Feld lässt es sich in die
Schwebe bringen, wo elektrische Kraft und Gewichtskraft gleich groß sind; daraus folgt die Ladung. Der Radius geht
mit der dritten Potenz ein, deshalb kommt es auf die Zeitmessung an.

- `data-tex`: `r = \sqrt{\dfrac{9\,\eta\,v_s}{2\,\rho\,g}}, \qquad |q| = \dfrac{m\,g\,d}{U_s} = \dfrac{4\pi\,\rho\,g\,d}{3\,U_s}\,r^3`
- `data-plain`: `r = √(9·η·v_s/(2·ρ·g)),   |q| = m·g·d/U_s = 4π·ρ·g·d/(3·U_s) · r³`

**Kernaussage 4 — Ladung kommt in Portionen, und jede Formel hat eine Grenze.**
Titel: *Was die Messreihe zeigt und was nicht.* Trägt man die Ladungen vieler Tröpfchen zusammen, sind sie
ganzzahlige Vielfache von <span class="m">e = 1,602 · 10⁻¹⁹ C</span>; der größte gemeinsame Teiler der Messwerte
ist die Elementarladung. Die Daten stützen die Quantelung, schließen aber nicht aus, dass es noch kleinere
Portionen gibt, und die Auswertung hat Modellgrenzen: Stokes-Reibung ohne Cunningham-Korrektur, klassische
Bewegungsenergie nur bei kleinem <span class="m">v/c</span>. Gute Physik nennt die Grenze mit.

- `data-tex`: `q = n\cdot e \quad (n = 1, 2, 3, \dots), \qquad e = 1{,}602\cdot10^{-19}\,\mathrm C`
- `data-plain`: `q = n · e   (n = 1, 2, 3, …),   e = 1,602 · 10⁻¹⁹ C`

### 6.2 Blick aufs Zentralabitur (`<div class="hinweis">`)

**Im Zentralabitur.** Beschleunigung und Ablenkung geladener Teilchen sowie der Millikan-Versuch stehen im
Inhaltsfeld *Ladungen, Felder und Induktion* und kommen meist als Bausteine größerer Aufgaben vor. Die folgenden
Gestalten sind *Erfahrungswerte aus der Aufgabenkultur*, keine Zitate; welche davon in deinem Jahrgang
vorkommen, sagt dir das aktuelle Übungsmaterial der Fachschaft (**offen:** Abgleich mit den veröffentlichten
Aufgaben der Standardsicherung NRW):

- **Endgeschwindigkeit oder Energie nach der Beschleunigung**, oft mit Angabe in eV. Die Punkte gehen selten an
  der Formel verloren, sondern an Vorsätzen: kV in V, eV in J.
- **Ablenkung im Kondensator**: Bahnform begründen (waagerechter Wurf), Ablenkung, Austrittswinkel oder
  Schirmauslenkung berechnen, prüfen, ob das Teilchen die Platte trifft (<span class="m">|y_a| ≤ d/2</span>).
  Erkennbar an *„Zeige, dass die Bahn eine Parabel ist"* oder *„Bestimme die Auslenkung auf dem Schirm"*.
- **Begründen statt Rechnen**: Warum hängt die Bahn bei gleicher Beschleunigungsspannung nicht von der Masse ab?
  Was ändert sich bei doppelter Ladung? Wer nur „schwerer, also träger" antwortet, verliert den Punkt.
- **Millikan-Versuch**: Kräftegleichgewicht aufstellen, Schwebemethode oder Steig-Sink-Methode auswerten, aus einer
  Messreihe die Elementarladung als größten gemeinsamen Teiler bestimmen. Meist ist die Stokes-Reibung
  <span class="m">6·π·η·r·v</span> im Aufgabentext gegeben; den Radius aus der Sinkgeschwindigkeit musst du selbst
  berechnen.
- **Bewertung**: Modellannahmen (Auftrieb vernachlässigt, Stokes-Reibung), Unsicherheit einer Messreihe, Grenzen der
  klassischen Rechnung.
- **Anschluss**: Im Magnetfeldmodul wird das beschleunigte Teilchen in ein Magnetfeld geschossen
  (<span class="m">v = √(2·|q|·U/m)</span> ist dort schon Rechengrundlage) und im Wien-Filter mit gekreuzten Feldern
  kombiniert. Die Spannungsformel ist die **Nahtstelle** zwischen beiden Modulen.

### 6.3 Selbstcheck (`.karte` mit `<h3>Selbstcheck</h3>`, sechs `.check`-Zeilen)

Vorspann: *Hak ehrlich ab. Was du hier nicht ankreuzen kannst, holst du besser jetzt nach als in der Klausur.*

1. Ich kann die Bewegung eines geladenen Teilchens im homogenen Längsfeld mit Kraft und Energiesatz beschreiben,
   <span class="m">v = √(2·|q|·U/m)</span> herleiten und erklären, warum nur die Spannung, nicht Plattenabstand oder
   Feldstärke, eingeht.
2. Ich kann Energien in Elektronvolt angeben und umrechnen, Geschwindigkeiten berechnen und begründet beurteilen,
   ob die klassische Rechnung noch zulässig ist.
3. Ich kann die Bahn eines Teilchens im homogenen Querfeld als Parabel herleiten und Ablenkung, Austrittswinkel und
   Schirmauslenkung berechnen.
4. Ich kann begründen, warum eine Feldlinie im Allgemeinen keine Bahnkurve ist und warum Elektron, Proton und
   α-Teilchen bei gleicher Beschleunigungsspannung dieselbe Bahn beschreiben, aber in unterschiedliche Richtungen und
   mit unterschiedlicher Flugzeit.
5. Ich kann den Millikan-Versuch erläutern: die auftretenden Kräfte benennen, aus der Sinkgeschwindigkeit den Radius
   und aus der Schwebespannung die Ladung berechnen, und die Steig-Sink-Methode auswerten.
6. Ich kann eine Messreihe zur Ladung auswerten, die Elementarladung als größten gemeinsamen Teiler bestimmen und
   beurteilen, was die Daten zeigen, was nicht und welche Modellgrenzen (Stokes-Reibung, Auftrieb) in die
   Auswertung eingehen.

### 6.4 Export und Druck

Knopfleiste wie im Referenzmodul: `Ergebnisse kopieren` (`id="bExport"`) und `Als Arbeitsblatt drucken`. Darunter
der graue Hinweis, dass nichts gespeichert wird und die Ergebnisse die Seite nur über den Kopieren-Knopf verlassen.

`var namen = {…}` am Skriptende — **jeder** automatisch ausgewertete Schlüssel muss hier stehen, sonst fehlt die
Aufgabe im Export:

```
vw1: "Vorwissen 1 – Arbeit und Bewegungsenergie"
vw2: "Vorwissen 2 – Waagerechter Wurf"
vw3: "Vorwissen 3 – Gleichförmige Bewegung heißt Kräftegleichgewicht"
sim1:"Simulation 1 – Grenzspannung am Plattenpaar"
sim2:"Simulation 2 – Sinken bei Teilspannung"
ue1: "Aufgabe 1 – Endgeschwindigkeit eines Elektrons"
ue2: "Aufgabe 2 – Ladung eines schwebenden Öltröpfchens"
ue3: "Aufgabe 3 – Bahnform im Querfeld"
ue4: "Aufgabe 4 – Zuordnung Abhängigkeit zu Diagramm"
ue5: "Aufgabe 5 – Auslenkung auf dem Schirm"
ue6: "Aufgabe 6 – Ladung aus Sinkgeschwindigkeit und Schwebespannung"
```

Die offenen Aufgaben `ue7`, `ue8` und `ue9` werden nicht automatisch ausgewertet und erscheinen — wie im
Referenzmodul — nicht im Export. Der Exporttext nennt sie am Ende trotzdem in einer Zeile:
*„Drei Bewertungsaufgaben (ue7–ue9) wurden nicht automatisch ausgewertet."*

### 6.5 Anschlusshinweis (`<div class="hinweis">`)

**Wie es weitergeht.** Bis hierher hat sich alles nach dem elektrischen Feld gerichtet: Die Kraft zeigte in
Feldrichtung, und der Energiesatz lieferte das Tempo. Im Magnetfeldmodul steht die Kraft **senkrecht** auf der
Geschwindigkeit: Sie ändert die Richtung, nicht den Betrag, und aus der Parabel wird eine Kreisbahn. Der Wert, den
du hier für die Geschwindigkeit ausgerechnet hast, ist dort der Eintrittswert; und die Elementarladung, die du eben
aus Tröpfchen gewonnen hast, ist die zweite Hälfte der Rechnung, mit der sich die Masse des Elektrons ergibt: Das
Fadenstrahlrohr liefert nur <span class="m">e/m</span>, erst der Millikan-Versuch trennt beide.

---

## Lehrerteil

`<details class="lehrer">` mit `<summary>Für die Lehrkraft</summary>`, am Ende von Abschnitt 6, verschwindet beim
Drucken (`@media print` aus dem Referenzmodul, unverändert übernommen).

### Einordnung

Inhaltsfeld **„Ladungen, Felder und Induktion"** (Kernlehrplan Physik, gymnasiale Oberstufe NRW, Leistungskurs).
Das Modul behandelt die Bewegung geladener Teilchen im homogenen elektrischen Feld (Längs- und Querfeld) und den
Millikan-Versuch als Messung der Elementarladung.

Kompetenzbereiche mit Schwerpunkt: **Umgang mit Fachwissen** (Energiesatz, Bahn im Querfeld, Kräftebilanz am
Öltröpfchen), **Erkenntnisgewinnung** (die drei Herleitungen in 2.2, 2.4 und 3.2, Auswertung der Messreihe in der
Simulation), **Kommunikation** (Diagramme lesen, ue4; Beobachtung protokollieren) und **Bewertung** (ue7, ue8, ue9:
Aussagen prüfen, Modellgrenzen und Unsicherheit beurteilen). Die drei Aufgaben im Anforderungsbereich III sind kein
Zusatz, sondern der Ort, an dem der Leistungskurs sich vom Grundkurs unterscheidet.

Vorausgesetzt werden: Bewegungsenergie und Arbeit sowie waagerechter Wurf aus der Einführungsphase und das
Kräftegleichgewicht bei gleichförmiger Bewegung (Vorwissensfragen vw1 bis vw3) sowie aus dem Vorgängermodul
<span class="m">E = U/d</span>, <span class="m">F = |q|·E</span> und Spannung als Energie pro Ladung.

**Stellung in der Reihe:** Das Modul folgt auf `physik-q1-elektrisches-feld.html` und sollte vor
`physik-q1-magnetisches-feld.html` behandelt werden; dieses setzt <span class="m">v = √(2·|q|·U/m)</span> als Rechengrundlage
voraus und verweist ausdrücklich auf den Millikan-Versuch. Wird die Reihenfolge vertauscht, reicht der Abschnitt 2.2
allein als Brücke.

*Offen markiert und als didaktische Setzung zu lesen, nicht als Vorgabe des Kernlehrplans:*

- die Einordnung des Millikan-Versuchs und der Elektronenstrahlablenkung im Inhaltsfeld 1 und ihre Lage zwischen
  elektrischem und magnetischem Feld; Kompetenzerwartungen werden hier nicht einzeln zitiert, der Abgleich mit dem
  schulinternen Lehrplan steht aus;
- die Frage, ob im Kurs relativistisch gerechnet werden soll (2.3 ist ein Ausblick ohne Herleitung; das Magnetfeldmodul
  bleibt ebenfalls bei der klassischen Form);
- die Wahl von Stokes-Reibung ohne Cunningham-Korrektur und ohne Auftrieb; für den LK vertretbar, aber eine Auswahl —
  wo die Fachschaft die Korrektur behandeln will, gehört sie an das Ende von 3.3;
- die Reihenfolge „Energiesatz → Querfeld → Millikan" (der Kernlehrplan nennt Inhalte, nicht ihre Abfolge).

### Zeitbedarf

Ausgelegt auf **135 Minuten** (Doppelstunde plus Einzelstunde oder drei Einzelstunden; Tabelle im Modul in
`<div class="tabelle">` kapseln):

| Abschnitt | Zeit | Sozialform |
|---|---|---|
| 1 Einstieg (Aufhänger, drei Vorwissensfragen) | 10 min | Plenum, Fragen in Einzelarbeit |
| 2 Erklärteil: Längsfeld, Energiesatz, Grenze v/c, Querfeld | 35 min | lehrergelenkt, Herleitung 2.4 gemeinsam an der Tafel |
| 3 Millikan-Versuch (Kräfte, Herleitung, Quantelung) | 20 min | Plenum, Herleitung im Details-Block je nach Kurs |
| 4 Simulation mit Beobachtungsauftrag und zwei MC-Fragen | 30 min | Partnerarbeit am Gerät, Teil A und B getrennt |
| 5 Übungen (Auswahl, siehe Differenzierung) | 30 min | Einzel- oder Partnerarbeit |
| 6 Abschluss, Selbstcheck, Export | 10 min | Plenum |

**Schnitte.** Bei einer Doppelstunde plus Einzelstunde liegt der natürliche Schnitt **nach 2.4** (Parabelbahn): Die
erste Einheit endet mit dem Modus *Strahl* der Simulation (Teil A), die zweite beginnt mit Millikan und Teil B.
Bei drei Einzelstunden: nach 2.2, nach 2.4.

**Realistisch in einer Doppelstunde:** Abschnitte 1 bis 2 vollständig, Simulation Teil A, ue1, ue3. Die drei
Bewertungsaufgaben ue7 bis ue9 sind als Hausaufgabe, Vertretungsmaterial oder Klausurvorbereitung angelegt; für die
Stunde reicht **eine** davon (ue7 passt zu 2.4, ue8 zu Teil B der Simulation).

### Typische Schülerfehler — und wo im Unterrichtsgespräch anzuhalten ist

**(1) „Doppelte Spannung, doppelte Geschwindigkeit."** Wird in vw1 und ue4 (Zeile 2) geprüft.
→ **Anhalten** nach Merksatz 1 in 2.2. Tafel: 1 kV → 4 kV, Elektron: 1,875·10⁷ m/s → 3,751·10⁷ m/s. Die Frage
*„Wie oft passt die Energie in die Geschwindigkeit hinein?"* führt auf die Wurzel.

**(2) „Gleiche Energie, gleiche Geschwindigkeit."** Elektron und Proton bei 1 keV, Faktor 43.
→ **Anhalten** an der Tabelle in 2.2 und die Frage stellen, welches Teilchen später ankommt.

**(3) „Die Feldlinie ist die Flugbahn."** Wird in ue3 direkt geprüft und ist die Auflösung der offenen Frage aus
dem Vorgängermodul.
→ **Anhalten** in 2.4 vor der Herleitung: Wurf-Analogie an die Tafel, dann den Modus *Strahl* mit *U_A = 0* und *U_A = 100 V*
zeigen. Wichtig ist der harmlose Sonderfall (Start aus der Ruhe, Beschleunigungsstrecke), damit die Aussage nicht wie
eine Spitzfindigkeit wirkt.

**(4) „Schwere Teilchen werden schwächer abgelenkt."** Stimmt nur bei gleicher Geschwindigkeit; wird in ue7 und im Beobachtungsauftrag Teil A
geprüft (sim1 prüft dazu die Grenzspannung am Plattenpaar).
→ **Anhalten** direkt nach Merksatz 2. Frage an den Kurs, bevor die Simulation läuft: *„Was ist bei beiden Teilchen
gleich, wenn sie aus derselben Spannung kommen?"* Erst dann Modus *Strahl* mit Elektron und Proton vergleichen.

**(5) Schirmauslenkung nur mit D·tan θ.** Der Beitrag der Strecke im Feld wird vergessen (ue5, Sonderwert 5,63 mm).
→ **Anhalten** an Schritt 7 der Herleitung: die gestrichelte Verlängerung in der Simulation zeigen. Sie trifft die
Mittellinie in der Plattenmitte; deshalb steht **L/2 + D** in der Formel.

**(6) Vorzeichen und Richtung.** Das Elektron wird zur **positiven** Platte gezogen; viele zeichnen den Pfeil in
Feldrichtung.
→ **Anhalten** an der Konvention in 0.3, dann die Teilchenknöpfe wechseln: Elektron oben, Proton unten.

**(7) „Beim Schweben wirkt keine Kraft."** Fehlvorstellung 4 in 3.3; sim2.
→ **Anhalten** in 3.2 bei Schritt 3. Zeichnung der beiden Pfeile an der Tafel, dann *U = 2·U_s* in der Simulation
einstellen: Das Tröpfchen steigt mit +v_s, nicht mit 2·v_s.

**(8) Durchmesser statt Radius, Fehlerfortpflanzung.** In ue6 als Sonderwert 32 e abgefangen.
→ **Anhalten** bei der Formel für *r*. Der Radius geht über *r³* ein; ein kleiner Ablesefehler bei der Sinkzeit
wird dadurch vergrößert. Ein Beispiel rechnen: 1 % bei *v_s* sind 1,5 % bei *q*.

**(9) „Die Elementarladung ist der kleinste gemessene Wert."** Wird in ue8 geprüft.
→ **Anhalten** in der Auswertung von Teil B: Die Quotienten 1,5 · 2,5 · 1,0 · 2,0 zeigen, dass der kleinste Wert
*nicht* die Portion ist. Fragen: *„Welche Zahl teilt alle vier?"*

**(10) Einheiten und Zehnerpotenzen.** mm/s → m/s, µm, kV, eV ↔ J.
→ **Anhalten** beim ersten gemeinsamen Einsetzen. Regel für den Kurs: **Erst alles in SI, dann einsetzen, und jede
Zahl mit ihrer Einheit hinschreiben.**

**(11) „Die Formel gilt überall."** Wird in ue9 geprüft.
→ **Anhalten** an der Tabelle in 2.3 und an der 65-kV-Zeile: 9,3 % Abweichung sind bei einer Schulaufgabe keine
Kleinigkeit.

### Pause und Ruheband

Der Knopf *Pause* hält Strahlanimation und Tröpfchenbewegung an (Anzeigen und Regler bleiben bedienbar). Die Anzeige „ruht“
erscheint bei |v| < 0,2 µm/s. Tröpfchen 3 ruht in einem Doppelfenster bei 409 V und 410 V. Lösungen der Simulationsfragen: `sim1` Proton, 500 V: bis 110 V (y_a = −9,90 mm,
Y = −75,90 mm, θ = −18,26°), bei 115 V Plattentreffer bei x = 5,9 cm; `sim2` Tröpfchen 3: v_s = 85,36 µm/s, U_s ≈ 409 V,
bei 300 V v = −22,76 µm/s.

### Differenzierung

**Für schnellere Lernende:**

- **Energie im Querfeld.** Das Elektron gewinnt beim Durchqueren des Plattenpaars zusätzliche Bewegungsenergie
  <span class="m">|q|·E·y_a</span>: Mit den Zahlen der Simulation <span class="m">e · 5,0 kV/m · 2,25 mm = 11,25 eV</span>,
  nachgerechnet über die Quergeschwindigkeit <span class="m">½·m·v_y² = 11,25 eV</span> (Kontrolle K-10). Damit ist die
  Endenergie am Schirm <span class="m">2000 eV + 11,25 eV</span>, ein schöner Beleg für die Wegunabhängigkeit.
- **Die Ladung aus der Steigung.** Aus der Steigung der Messspur (Diagramm 1, Modus *Millikan*) folgt
  <span class="m">q = 6·π·η·r·d·(Δv/ΔU)</span>; mit Tröpfchen 1 ergibt sich aus
  <span class="m">0,2817 µm/(s·V)</span> wieder <span class="m">3,0 e</span> (K-7). Das ist die Steig-Sink-Methode ohne
  Abwarten auf Schweben.
- **Gekreuzte Felder.** Wann läuft ein Elektron im Plattenpaar geradeaus, wenn zusätzlich ein Magnetfeld senkrecht
  wirkt? Bedingung <span class="m">|q|·E = |q|·v·B</span>, also <span class="m">v = E/B</span> — der Vorgriff auf den Wien-Filter
  im Magnetfeldmodul.
- **Cunningham-Korrektur.** Mit dem Faktor 1,085 bei <span class="m">r = 1 µm</span> nachrechnen, warum ein reales
  Praktikum ohne Korrektur zu große Ladungen liefert (K-5: Radius 4 %, Ladung 13 %).
- **Zusatz zu ue8:** Bei welcher relativen Unsicherheit lässt sich ein Tröpfchen mit 20 Elementarladungen noch eindeutig
  zuordnen? (Antwort: unter 2,5 %, denn 2,5 % von 20 e ist gleich 0,5 e.)

**Für Lernende, die mehr Zeit brauchen:**

- Pflichtteil sind **ue1, ue2, ue3 und ue4**. ue1 und ue2 sind reines Handwerk mit Einheiten, ue3 und ue4 verlangen
  keine Rechnung und tragen trotzdem die zentrale Einsicht des Moduls.
- Die Herleitungen in Details-Block 1 (Energiesatz) und Details-Block 2 (Parabel) können übersprungen werden; die
  Merksätze 1 und 2 tragen das Ergebnis auch allein. Was **nicht** entfallen darf, ist die Tabelle in 2.2 und die
  Aussage „Ladung und Masse kürzen sich aus der Bahn heraus".
- Von den drei Bewertungsaufgaben genügt **ue8**; sie hängt an einem einzigen Zahlenvergleich. ue7 verlangt zwei
  Fälle sauber zu trennen, ue9 eine relativistische Nebenrechnung.
- Der Beobachtungsauftrag lässt sich halbieren: nur Teil A, Elektron gegen Proton, ohne α-Teilchen und ohne Verdopplung
  von U_B; Teil B dann als Demonstration mit einem Tröpfchen im Plenum.

### Bezug zu Realexperimenten

- **Elektronenstrahlablenkröhre mit Plattenpaar — das Kernexperiment für Abschnitt 2.** Eine evakuierte Röhre mit
  Leuchtschirm zeigt die Bahn als Spur. Ändere <span class="m">U_A</span> und beobachte die lineare Auslenkung; vertausche die
  Polung und die Spur springt auf die andere Seite. Verdopple <span class="m">U_B</span> und die Auslenkung halbiert sich.
  Das ist Teil A des Beobachtungsauftrags in echt. **Aufwand:** 10 Minuten. **Stolperstelle:** Die Schulröhre hat kein
  gerades homogenes Feld; das Ergebnis weicht um einige Prozent ab (Randfeld), was ein guter Anlass für den Vergleich
  mit der Idealisierung ist.
- **Röhrenoszilloskop oder Braunsche Röhre.** Ein Sinussignal am Y-Eingang und die Zeitablenkung machen die
  lineare Ablenkempfindlichkeit anschaulich (<span class="m">|Y| = S·|U_A|</span>); die Anodenspannung im Innern ist der
  Wert <span class="m">U_B</span> aus dem Modul. Alte Geräte mit Röhre werden selten, ein Video genügt.
- **Millikan-Apparatur.** Die Schulversion mit einem Mikroskop und einer Skala erlaubt, Tröpfchen zu sinken und zu
  steigen zu sehen und die Zeiten für eine Skalenstrecke zu stoppen. **Aufwand:** 45 Minuten mit Einweisung, gut
  als Lehrerdemonstration mit Beamer-Kamera. **Stolperstellen:** Tröpfchen driften und verdunsten, die Ladung ändert
  sich unbemerkt, Konvektionsströme verfälschen die Zeit. Die Auswertung der Videos mit den Formeln aus 3.2 liefert
  Werte im Bereich von einigen 10⁻¹⁹ C; die Häufung bei Vielfachen ist bei wenigen Tröpfchen oft unscharf, was
  ue8 vorbereitet.
- **Simulation als Ersatz.** Der Modus *Millikan* der Seite ist bewusst so gebaut, dass die Auswertung wie beim Realversuch
  läuft (Zeit, Spannung, Länge); wer keine Apparatur hat, lässt Teil B als Messpraktikum durchführen. **Wichtig:** Die
  Simulation rechnet ohne Cunningham-Korrektur und bekommt deshalb saubere ganze Zahlen, ein Realversuch nicht.
- **Fadenstrahlrohr** (Vorgriff auf das Magnetfeldmodul): Dieselbe Elektronenkanone, nur mit Magnetfeld; die Kanone
  bestimmt die Beschleunigungsspannung. Der Aufbau eignet sich, den Übergang von *v = √(2·e·U/m)* zur Kreisbahn zu
  zeigen.

---

## Checkliste für den Bauagenten

### Benötigte Bausteine und ihre Schlüssel

| Schlüssel | Baustein | `data`-Attribut | Optionen / Besonderheit | AB | Fundstelle |
|---|---|---|---|---|---|
| `vw1` | Multiple Choice | `data-mc="vw1"` | 3 Optionen, `r: 1` | — | 1.2 |
| `vw2` | Multiple Choice | `data-mc="vw2"` | 3 Optionen, `r: 1` | — | 1.2 |
| `vw3` | Multiple Choice | `data-mc="vw3"` | 3 Optionen, `r: 1` | — | 1.2 |
| `sim1` | Multiple Choice | `data-mc="sim1"` | **4** Optionen, `r: 1` | II | 4.9 |
| `sim2` | Multiple Choice | `data-mc="sim2"` | **4** Optionen, `r: 1` | II | 4.9 |
| `ue1` | Zahleneingabe | `data-num="ue1"` | `wert: 2.9654e7`, `"m/s"`, `tol: 1.5e5`, `alt: 29654 "km/s"`, Distraktoreinheiten `m/s²`, `J`, **`sonder`-Liste** (2,097e7 · 6,92e5) | I | 5.1 |
| `ue2` | Zahleneingabe | `data-num="ue2"` | `wert: 3.0`, `"e"`, `tol: 0.1`, `alt: 4.806e-19 "C"`, Distraktoreinheiten `C/kg`, `V/m` | I | 5.2 |
| `ue3` | Multiple Choice | `data-mc="ue3"` | **4** Optionen, `r: 2`, **mit** Hilfen 1–3 | I | 5.3 |
| `ue4` | Zuordnung | `data-check="zuordnung"` | 4 SVG-Diagramme, Lösung **C · A · D · B**, **mit** Hilfen 1–3 | II | 5.4 |
| `ue5` | Zahleneingabe | `data-num="ue5"` | `wert: 6.19`, `"mm"`, `tol: 0.10`, `alt: 0.619 "cm"`, Distraktoreinheit `°`, **`sonder`-Liste** (5,625 · 0,5625 · 12,375 · 24,75) | II | 5.5 |
| `ue6` | Zahleneingabe | `data-num="ue6"` | `wert: 4.0`, `"e"`, `tol: 0.1`, `alt: 6.408e-19 "C"`, Distraktoreinheiten `kg`, `µm`, **`sonder`-Liste** (32,0 · 0,42) | II | 5.6 |
| `ue7` | offene Aufgabe | `data-loesung="ue7"` | `<textarea>`, nur Knopf „Musterlösung anzeigen“ (Text in `.hilfe-text[data-stufe="9"]`) | III | 5.7 |
| `ue8` | offene Aufgabe | `data-loesung="ue8"` | `<textarea>`, nur Knopf „Musterlösung anzeigen“ (Text in `.hilfe-text[data-stufe="9"]`) | III | 5.8 |
| `ue9` | offene Aufgabe | `data-loesung="ue9"` | `<textarea>`, nur Knopf „Musterlösung anzeigen“ (Text in `.hilfe-text[data-stufe="9"]`) | III | 5.9 |

**Hilfestufen** (`<button data-hilfe="1|2|3">` plus `.hilfe-text[data-stufe="1|2|3"]`) bekommen `ue1` bis `ue6`, also **alle
sechs** auswertbaren Übungsaufgaben. Die offenen Aufgaben `ue7` bis `ue9` bekommen **keine** Hilfestufen, sondern
nur den Knopf `data-loesung` mit der Musterlösung **und** den fetten Bewertungskriterien in
`.hilfe-text[data-stufe="9"]` (Linie des Referenzmoduls, Entscheidung des Nutzers).

> **Abweichung von `CLAUDE.md`, bewusst so entschieden.** `CLAUDE.md` verlangt für Abschnitt 5 „jede mit
> dreistufigem Hilfesystem"; das Referenzmodul hat Hilfen nur bei den Zahleneingaben, das Vorgängermodul zusätzlich
> bei ue3 und ue4. Für die Bewertungsaufgaben ue7 bis ue9 gilt die Referenzlinie: nur die Musterlösung.

### Vier Stellen, an denen generischer Code angefasst werden muss

1. **Zuordnungs-Engine.** Im Referenzmodul steht hart `ergebnisse.a3 = …`. Für dieses Modul muss daraus
   `ergebnisse.ue4 = …` werden. Ebenso sind die beiden Rückmeldungstexte modulspezifisch: der Erfolgstext und der
   Teilerfolgstext wörtlich aus 5.4 („Noch nicht alles passt. Geh jede Zeile in zwei Schritten durch …").
2. **`var namen = {…}`** am Skriptende: die elf Einträge aus 6.4. Fehlt ein Schlüssel, fällt die Aufgabe still aus dem
   Export.
3. **`sonder`-Auswertung in der Zahlen-Engine.** Das Vorgängermodul `module/physik-q1-elektrisches-feld.html` hat sie
   bereits (Auswertung mit `d.sonder`, nur in der Haupteinheit, Vorrang vor `nah`/`weit`). Diese Fassung der Engine
   wird übernommen. Drei Aufgaben (ue1, ue5, ue6) benutzen `sonder`.
4. **Zahlen-Engine mit sehr kleinen Sollwerten.** ue2 und ue6 haben `alt` in Coulomb mit Werten um
   <span class="m">5 · 10⁻¹⁹</span>. Die Engine rechnet `tol` mit demselben Faktor um (`0,1 · 4,806e-19/3,0 = 1,602e-20`)
   und vergleicht mit `(1 + eps)` multiplikativ; das trägt auch bei so kleinen Zahlen. Im Modulcheck trotzdem
   testen, ob `4.806e-19` in einem `<input type="number" step="any">` akzeptiert und richtig gelesen wird.

Alles Übrige — `<style>`-Block, `formelnRendern()`, MC-Engine, Zahlen-Engine (abgesehen von 3.), Hilfesystem, Export,
Druck-CSS — wird unverändert übernommen. Einzige erlaubte CSS-Änderung sind die drei Akzent-Tokens; für Physik bleiben
sie ohnehin, wie sie im Referenzmodul stehen (`#1d4ed8` · `#eff6ff` · `#bfdbfe`).

### Simulationsbausteine

| Element | `id` bzw. `data`-Attribut | Bereich / Werte |
|---|---|---|
| Canvas Bild | `cvSim` | `width="1000" height="400"`, zwei Inhalte je nach Modus |
| Canvas Diagramm 1 | `cvD1` | `width="1000" height="220"` |
| Canvas Diagramm 2 | `cvD2` | `width="1000" height="220"` |
| Modus | `modStrahl`, `modMillikan` | Radios `name="modus"`, Start `modStrahl` |
| Teilchen | `data-teil="e" \| "p" \| "a"` | Start `e`, aktiver Knopf `primaer` |
| Regler `U_B` | `rUB`, Anzeige `lUB` | 0 … 300, Schritt 1, Start **130** (= 2,00 kV) |
| Regler `U_A` | `rUA`, Anzeige `lUA` | −200 … 200, Schritt 5, Start **100** (V) |
| Tröpfchen | `data-tropfen="1" \| "2" \| "3" \| "4"` | Start 1, aktiver Knopf `primaer` |
| Regler `U` (Millikan) | `rUM`, Anzeige `lUM` | 0 … 1000, Schritt 1, Start **0** (V) |
| Zeitraffer | `data-zeit="1" \| "5"` | Start `1` |
| Spur löschen | `bSpur` | leert die Messpunkte in Diagramm 1 (Modus Millikan) |
| Pause | `bPause` | hält die Animation an |
| Zurücksetzen | `bReset` | beide Modi auf Startwerte |
| Anzeigen Strahl | `aV0`, `aTF`, `aEK`, `aYA`, `aYS`, `aTH`, `aVc` | Startwerte: `26523,2 km/s`, `2,26 ns`, `2,00 keV`, `+2,25 mm`, `+17,25 mm`, `+4,29°`, `v/c = 8,85 %` |
| Anzeigen Millikan | `aUm`, `aEm`, `aVm`, `aRi`, `aT05` | Startwerte: `0 V`, `0,00 kV/m`, `−105,39 µm/s`, `sinkt`, `4,74 s` |
| Hinweisfeld | `simHinweis` | leer, solange keine der Meldungen aus 4.7 greift |

Kein Regler wird jemals `disabled`; der Modusschalter blendet die Elemente des jeweils anderen Modus mit `hidden` aus.

### Prüfpunkte vor der Abnahme

1. **Startwerte der Simulation** (Modus Strahl, Elektron): `v₀ = 26523,2 km/s` · `t = 2,26 ns` · `E_kin = 2,00 keV` ·
   `y_a = +2,25 mm` · `Y = +17,25 mm` · `θ = +4,29°` · `v/c = 8,85 %`. Weicht eine Anzeige in der letzten Stelle ab, ist
   ein Umrechnungsfaktor falsch.
2. **Beobachtungsauftrag Teil A nachfahren** (Tabelle in 4.8): Proton `618,9 km/s` · `96,95 ns` · `−17,25 mm`;
   α-Teilchen `439,2 km/s` · `136,62 ns` · `−17,25 mm`; Elektron 4,0 kV: `37509,5 km/s` und `Y = 8,62/8,63 mm`.
   Der Betrag von `Y` muss bei allen drei Teilchen **exakt** 17,25 mm sein, daran hängt der Beobachtungsauftrag Teil A.
3. **Beobachtungsauftrag Teil B nachfahren** (Tabelle in 4.8): `v_s` bei `U = 0` für die vier Tröpfchen
   `105,39 · 127,52 · 85,36 · 151,76 µm/s`; Vorzeichenwechsel von `v` zwischen `374/375 V`, `298/299 V`, `409/410 V`,
   `484/485 V`. Radien und Elementarladungszahlen dürfen **nirgends** in der Oberfläche stehen.
4. **Regler `rUB`**: `p = 0 · 30 · 50 · 100 · 130 · 170 · 200 · 281 · 300` ergibt `100 · 200 · 320 · 1000 · 2000 · 5000 ·
   10 000 · 65 000 · 100 000 V` (Rundung auf zwei Stellen, Tabelle in 4.2).
5. **Meldungen**: Plattentreffer (Test: Elektron, `p = 0`, `U_A = +200 V`, Treffer bei `x = 2,0 cm`) · orange
   Warnung bei `v/c > 10 %` (Test: Elektron, 4,0 kV: `12,51 %`, relativistisch `12,44 %`) · Nachführen des
   Tröpfchens (Test: Zeitraffer 5-fach, `U = 0` laufen lassen) · Tröpfchenwechsel löscht die Spur.
6. **Diagramme**: Strahl 1 — klassische Kurve schneidet bei rund 255 kV die Lichtlinie (Elektron), Proton bleibt unten;
   Strahl 2 — Gerade dreht sich mit `U_B`, Vorzeichenwechsel beim Teilchenwechsel Elektron ↔ Proton; Millikan 1 —
   Messpunkte für Tröpfchen 1 bei `(0 | −105,39)`, `(500 | +35,48)`, `(1000 | +176,34)` liegen auf einer Geraden;
   Millikan 2 — Kräftesumme immer `0,00`.
7. **Maßstab**: Bild im Modus Strahl hat den Maßstabsbalken „10 mm"; Modus Millikan hat die Beschriftung
   „Tröpfchen vergrößert dargestellt" und die Konstantenzeile aus 4.3.
8. **Alle Zahleneingaben in allen Fällen** testen (richtig · richtige Zahl mit falscher Einheit · nah daneben · weit
   daneben · jeder `sonder`-Wert) und zusätzlich die Alternativeinheit: `2,965·10⁷ m/s` ↔ `29654 km/s` ·
   `3,0 e` ↔ `4,806e-19 C` · `6,19 mm` ↔ `0,619 cm` · `4,0 e` ↔ `6,408e-19 C`.
9. **Hilfestufen**: jede der drei Stufen aller Aufgaben `ue1`–`ue6` öffnet und schließt; bei `ue7`–`ue9` gibt es nur den
   Musterlösungsknopf (`data-loesung`), der sich öffnet und schließt.
10. **Feedbackzahl gegen Optionszahl**: `sim1`, `sim2` und `ue3` haben **vier** Optionen und brauchen **vier** `fb`-Einträge;
    `vw1`–`vw3` haben drei. `data-i` lückenlos von 0 an, `name` jedes Radios gleich dem Wert von `data-mc`.
    `ue3` hat `r: 2`, alle anderen `r: 1`.
11. **Zuordnung in beiden Richtungen** testen: vollständig richtig (**C · A · D · B**) und teilweise falsch. Die
    Reihenfolge der Situationen darf nicht der Diagrammreihenfolge entsprechen; sie tut es hier auch nicht.
12. **Offline-Fallback**: Jede Formel hat ein gefülltes `data-plain` mit Unicode (`ε`, `θ`, `η`, `ρ`, `π`, `·`, `−`, `⁻¹⁹`, `⟹`, `½`,
    `√`, `Σ`, `∼`). Stichprobe ohne Netz.
13. **Tabellenkapselung**: Jede `<table>` steht in `<div class="tabelle">`. Dieses Modul hat viele, unter anderem in 0.1,
    0.2, 0.3, 2.2, 2.3, 3.1, 4.1, 4.2, 4.3, 4.8, im Lehrerteil und in den Hilfetexten von ue4.
14. **Kein waagerechtes Scrollen** bei 1280, 900 und 390 px; Druckansicht enthält die Aufgaben, aber keine
    Bedienelemente und keinen Lehrerteil.
15. **Modulcheck** laufen lassen:
    `PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/physik-q1-geladene-teilchen-e-feld.html"` — `blocker` und
    `maengel` müssen leer sein.
16. **Modulliste**: Der Eintrag in `fachliches/modulliste.md` steht auf `in Arbeit` und wird erst **danach** auf `fertig` gesetzt.

### Quelle der Kontrollrechnungen

Alle Zahlenwerte dieses Dokuments wurden mit Python nachgerechnet, durchgehend mit den Konstanten aus 0.1. Das Skript
prüft **jede im Text genannte Zahl** gegen die Rechnung (Toleranz 0,5 % bzw. die letzte angegebene Stelle) und bricht
bei einer Abweichung ab. Ergebnis des letzten Laufs: **196 Prüfungen bestanden, 0 Abweichungen.**

Was geprüft wird:

| Nr. | Gegenstand | Fundstelle |
|---|---|---|
| K-1 | 65-kV-Aufhänger: Energie, klassisches und relativistisches Tempo, Abweichung 9,3 % | 1.1 |
| K-2 | Beschleunigung: Tabelle 1 kV, Faktor 43, Verhältnis Feldkraft zu Gewichtskraft, v(4 kV)/v(1 kV) | 2.1, 2.2 |
| K-3 | Grenze der klassischen Rechnung, sechs Zeilen, Protonengrenze 4,7 MV | 2.3 |
| K-4 | Ablenkbeispiel und Startwerte: y_a, θ, Y, Grenzspannung, Kontrolle über t und a, Empfindlichkeit | 2.4 |
| K-5 | Millikan-Beispiel: r, m, q, Re, τ, Steig-Sink, Cunningham-Folgen (Radius 4 %, Ladung 13 %), m_e | 3.1–3.3 |
| K-6 | Simulation Strahl: Rundung der Regler, Tabelle 4.8, `sim1`, 4-kV-Warnung, Plattentreffer | 4.1–4.9 |
| K-7 | Simulation Millikan: vier Tröpfchen, Diagramm-Kontrollwerte, Quotienten, Kräftebalken | 4.6, 4.8 |
| K-8 | `sim2`: Tröpfchen 3 bei 300 V (−22,76 µm/s) und `sim1`: Proton bei 500 V (Grenze 110 V, Y = −75,90 mm), beides mit Python nachgerechnet | 4.9 |
| K-9 | Übungen ue1, ue2, ue4, ue5, ue6, ue7, ue8, ue9 samt der Fehlwerte in den `sonder`-Listen | 5 |
| K-10 | Vorwissen vw2, Zusatz Energiegewinn im Querfeld (11,25 eV auf zwei Wegen) | 1.2, Lehrerteil |

Abweichungen zwischen den im Text genannten gerundeten Werten und der Rechnung liegen ausnahmslos in der letzten
angegebenen Stelle. Größte gefundene Abweichung: Die Cunningham-Korrektur beträgt 8,55 %, im Text steht „rund 8,5 %";
die Abweichung bei „1,5 %" (1,46 %) und „0,15 %" (0,147 %) in Tabelle 2.3 ist Rundung.

**Das Skript** (`kontrolle.py`, lauffähig mit `python`; die Ausgabe der 196 Zeilen `OK` ist hier nicht abgedruckt):

```python
# Kontrollrechnung, Modul physik-q1-geladene-teilchen-e-feld
# Konstanten wie in Abschnitt 0.1. Jede im Text genannte Zahl wird gegen die Rechnung geprüft.
from math import sqrt, pi, log10, floor, atan, degrees, exp

e = 1.602e-19; me = 9.109e-31; mp = 1.673e-27; ma = 6.645e-27; c = 2.998e8; g = 9.81
eta = 1.81e-5; rho = 875.0; rhoL = 1.20
L = 0.060; d = 0.020; D = 0.200          # Ablenkeinheit
dM = 5.00e-3                             # Plattenabstand Millikan
n_ok = 0
fehler = []


def chk(name, ist, soll, tol=0.005):
    """Vergleich mit relativer Toleranz (Standard 0,5 %, entspricht der letzten angegebenen Stelle)."""
    global n_ok
    ok = abs(ist - soll) <= tol * abs(soll)
    n_ok += ok
    print(("OK   " if ok else "FEHL ") + "%-46s %.6g  (Text: %.6g)" % (name, ist, soll))
    if not ok:
        fehler.append(name)


def v_kl(q, m, U):
    return sqrt(2 * abs(q) * U / m)


def beta_rel(q, m, U):
    gam = 1 + abs(q) * U / (m * c * c)
    return sqrt(1 - 1 / gam ** 2), gam


print("K-1 Aufhänger 65 kV")
vk = v_kl(e, me, 65e3); br, gam = beta_rel(e, me, 65e3)
chk("E_kin in J", e * 65e3, 1.041e-14); chk("v klassisch m/s", vk, 1.512e8); chk("v/c klassisch", vk / c, 0.504)
chk("gamma", gam, 1.1272); chk("beta rel", br, 0.4615); chk("klassisch zu hoch %", (vk / c / br - 1) * 100, 9.3)
chk("Ruheenergie keV", me * c * c / e / 1e3, 511.06)

print("K-2 Energiesatz, Tabelle 1 kV")
chk("a Elektron bei 10 kV/m", e * 1e4 / me, 1.759e15); chk("F_el/F_G", e * 1e4 / (me * g), 1.8e14, 0.02)
chk("F_el N", e * 1e4, 1.602e-15); chk("F_G Elektron N", me * g, 8.94e-30, 0.01)
for n, q, m, vt, qm in [("Elektron", e, me, 1.875e7, 1.759e11), ("Proton", e, mp, 4.376e5, 9.576e7),
                        ("alpha", 2 * e, ma, 3.105e5, 4.822e7)]:
    chk("v(1 kV) " + n, v_kl(q, m, 1e3), vt); chk("|q|/m " + n, abs(q) / m, qm)
chk("sqrt(mp/me)", sqrt(mp / me), 42.86); chk("v(4 kV) Elektron", v_kl(e, me, 4e3), 3.751e7)
chk("v(4kV)/v(1kV)", v_kl(e, me, 4e3) / v_kl(e, me, 1e3), 2.0)

print("K-3 Grenze der klassischen Rechnung (Elektron)")
for U, bk, brs, ab in [(1e3, 0.0626, 0.0625, 0.15), (1e4, 0.198, 0.195, 1.5), (65e3, 0.504, 0.461, 9.3),
                       (1e5, 0.626, 0.548, 14.1), (255e3, 0.999, 0.745, 34.1), (511e3, 1.414, 0.866, 63.3)]:
    b1 = v_kl(e, me, U) / c; b2, _ = beta_rel(e, me, U)
    chk("U=%d V klass." % U, b1, bk, 0.005); chk("U=%d V rel." % U, b2, brs, 0.003)
    chk("U=%d V Abw. %%" % U, (b1 / b2 - 1) * 100, ab, 0.03)
chk("Proton v/c=0,1 bei MV", 0.5 * mp * c * c * 0.01 / e / 1e6, 4.7, 0.01)

print("K-4 Ablenkung, Beispiel 2.4 und Startwerte der Simulation")
UB, UA = 2000, 100
ya = UA * L ** 2 / (4 * d * UB); tan = 2 * ya / L; Y = tan * (L / 2 + D)
chk("E kV/m", UA / d / 1e3, 5.0); chk("y_a mm", ya * 1e3, 2.25); chk("tan theta", tan, 0.075)
chk("theta Grad", degrees(atan(tan)), 4.29); chk("Y mm", Y * 1e3, 17.25)
chk("U_A max V", 2 * d ** 2 / L ** 2 * UB, 444, 0.002)
v0 = v_kl(e, me, UB); t = L / v0; a = e * (UA / d) / me
chk("v0 m/s", v0, 2.652e7); chk("t ns", t * 1e9, 2.26); chk("a m/s2", a, 8.79e14)
chk("y_a über t mm", 0.5 * a * t * t * 1e3, 2.25)
chk("Empfindlichkeit mm/V", L * (L / 2 + D) / (2 * d * UB) * 1e3, 0.1725)

print("K-5 Millikan: Beispiel Abschnitt 3")
r = 1.0e-6; m = 4 / 3 * pi * r ** 3 * rho; FG = m * g; vs = FG / (6 * pi * eta * r); Us = FG * dM / (3 * e)
chk("m kg", m, 3.665e-15); chk("F_G N", FG, 3.60e-14, 0.01); chk("v_s mm/s", vs * 1e3, 0.1054, 0.002)
chk("Re", rhoL * vs * 2 * r / eta, 1.4e-5, 0.05); chk("tau s", m / (6 * pi * eta * r), 1.07e-5, 0.01)
chk("U_s V", Us, 374.1, 0.001); chk("E kV/m", Us / dM / 1e3, 74.8, 0.001)
chk("E/E_max %", Us / dM / 3e6 * 100, 2.5, 0.05)
chk("Auftrieb/Gewicht %", rhoL / rho * 100, 0.14, 0.03); chk("Zeit für 0,50 mm s", 0.5e-3 / vs, 4.74, 0.002)
rr = sqrt(9 * eta * 1.054e-4 / (2 * rho * g)); chk("r aus v_s=1,054e-4 in µm", rr * 1e6, 1.000, 0.001)
q = (4 / 3 * pi * rr ** 3 * rho) * g * dM / 374.1; chk("q C", q, 4.806e-19, 0.001); chk("q/e", q / e, 3.000, 0.001)
vst = vs * (748 / Us - 1); chk("v_st bei 748 V mm/s", vst * 1e3, 0.1053, 0.002)
chk("q über Steig-Sink /e", 6 * pi * eta * r * dM * (vs + vst) / 748 / e, 3.000, 0.001)
lam = 68e-9; Kn = lam / r; Cc = 1 + Kn * (1.257 + 0.4 * exp(-1.1 / Kn))
chk("Cunningham %", (Cc - 1) * 100, 8.5, 0.02); chk("r zu groß %", (sqrt(Cc) - 1) * 100, 4, 0.1)
chk("q zu groß %", (Cc ** 1.5 - 1) * 100, 13, 0.05); chk("1,131 * 1,602", Cc ** 1.5 * 1.602, 1.8, 0.02)
chk("Millikan 1913 vs heute %", (1 - 1.592 / 1.602) * 100, 0.6, 0.05)
chk("m_e aus e und e/m", 1.602e-19 / 1.759e11, 9.11e-31, 0.002)

print("K-6 Simulation Modus Strahl (Tabelle 4.8, sim1)")


def rund2(x):
    ee = floor(log10(x)); f = 10 ** (ee - 1); return round(x / f) * f


for p, Ut in [(0, 100), (30, 200), (50, 320), (100, 1000), (130, 2000), (170, 5000), (200, 1e4), (281, 65e3), (300, 1e5)]:
    chk("rund2 p=%d" % p, rund2(100 * 10 ** (p / 100)), Ut, 1e-9)
for nm, q, m, sg, v0t, tt, Ek in [("e", e, me, -1, 26523.2, 2.26, 2.0), ("p", e, mp, 1, 618.9, 96.95, 2.0),
                                  ("a", 2 * e, ma, 1, 439.2, 136.62, 4.0)]:
    v0 = v_kl(q, m, 2000); ya_ = -sg * 100 * L ** 2 / (4 * d * 2000)
    chk("v0 km/s " + nm, v0 / 1e3, v0t, 1e-4); chk("t ns " + nm, L / v0 * 1e9, tt, 0.002)
    chk("E_kin keV " + nm, abs(q) * 2000 / e / 1e3, Ek, 1e-9); chk("Y mm " + nm, ya_ * 2 / L * (L / 2 + D) * 1e3, -sg * 17.25, 1e-9)
chk("v_p/v_e", v_kl(e, mp, 1) / v_kl(e, me, 1), 0.0233, 0.005)
chk("v/c Start (8,85 %)", v_kl(e, me, 2000) / c * 100, 8.85, 0.002)
chk("4 kV: v0 km/s", v_kl(e, me, 4000) / 1e3, 37509.5, 1e-4)
chk("4 kV: Y mm", 100 * L ** 2 / (4 * d * 4000) * 2 / L * (L / 2 + D) * 1e3, 8.625, 1e-9)
b1 = v_kl(e, me, 4000) / c; b2, _ = beta_rel(e, me, 4000)
chk("4 kV: v/c klass. %", b1 * 100, 12.51, 0.002); chk("4 kV: v/c rel. %", b2 * 100, 12.44, 0.002)
chk("4 kV: Abw. %", (b1 / b2 - 1) * 100, 0.6, 0.06)
chk("Plattentreffer x_hit cm (100 V, 200 V)", d * sqrt(2 * 100 / 200) * 100, 2.0, 1e-9)
chk("Grenze U_A bei 500 V", 2 * d ** 2 / L ** 2 * 500, 111, 0.002)
chk("Elektron 100 kV klass. v/c", v_kl(e, me, 1e5) / c, 0.626, 0.002)

print("K-7 Simulation Modus Millikan (vier Tröpfchen)")
T = [(1.00e-6, 3, 105.39, 374.1, 3.665e-15, 4.806e-19), (1.10e-6, 5, 127.52, 298.7, 4.878e-15, 8.010e-19),
     (0.90e-6, 2, 85.36, 409.0, 2.672e-15, 3.204e-19), (1.20e-6, 4, 151.76, 484.8, 6.333e-15, 6.408e-19)]
qs = []
for i, (r, n, vs_t, Us_t, m_t, q_t) in enumerate(T, 1):
    m = 4 / 3 * pi * r ** 3 * rho; vs = m * g / (6 * pi * eta * r); Us = m * g * dM / (n * e); qs.append(n * e)
    chk("T%d v_s µm/s" % i, vs * 1e6, vs_t, 0.0005); chk("T%d U_s V" % i, Us, Us_t, 0.0005)
    chk("T%d m kg" % i, m, m_t, 0.0005); chk("T%d q C" % i, n * e, q_t, 0.0005)
    r_est = sqrt(9 * eta * vs / (2 * rho * g)); q_est = 4 / 3 * pi * r_est ** 3 * rho * g * dM / round(Us)
    chk("T%d q/e aus Messung (U_s gerundet)" % i, q_est / e, n, 0.004)
vs1 = 4 / 3 * pi * 1e-18 * rho * g / (6 * pi * eta * 1e-6); Us1 = 4 / 3 * pi * 1e-18 * rho * g * dM / (3 * e)
v1 = lambda U: vs1 * 1e6 * (U / Us1 - 1)
chk("T1 v(0) µm/s", v1(0), -105.39, 0.001); chk("T1 v(375 V)", v1(375), 0.26, 0.02)
chk("T1 v(500 V)", v1(500), 35.48, 0.002); chk("T1 v(1000 V)", v1(1000), 176.34, 0.001)
chk("T1 v(374 V) (Vorzeichen -)", -v1(374), 0.02, 0.06)
chk("T1 Steigung µm/(s V)", (v1(1000) - v1(0)) / 1000, 0.2817, 0.001)
qmin = min(qs); chk("Verhältnisse 1,5|2,5|1|2 (Summe)", sum(x / qmin for x in qs), 7.0, 1e-9)
chk("e aus q_min/2", qmin / 2, 1.602e-19, 1e-9)
r, n = T[1][0], T[1][1]; m = 4 / 3 * pi * r ** 3 * rho; Fel = n * e * 300 / dM
chk("T2 300 V: F_G in 1e-14 N", m * g * 1e14, 4.79, 0.002); chk("T2 300 V: F_el", Fel * 1e14, 4.81, 0.002)
v300 = (Fel - m * g) / (6 * pi * eta * r); chk("T2 300 V: v µm/s", v300 * 1e6, 0.54, 0.02)
chk("T2 300 V: F_R (Betrag)", 6 * pi * eta * r * v300 * 1e14, 0.02, 0.1)
chk("Steigung -> q/e (T1)", 6 * pi * eta * 1e-6 * dM * (0.2817e-6) / e, 3.0, 0.002)

print("K-8 sim2: Tröpfchen 1 bei 748 V")
r, n = T[0][0], T[0][1]; m = 4 / 3 * pi * r ** 3 * rho; vs = m * g / (6 * pi * eta * r); Us = m * g * dM / (n * e)
vdir = (n * e * 748 / dM - m * g) / (6 * pi * eta * r)
chk("v(748 V) µm/s (Formel)", vs * (748 / Us - 1) * 1e6, 105.35, 0.001); chk("v(748 V) µm/s (direkt)", vdir * 1e6, 105.35, 0.001)
chk("2*v_s mm/s (Option 0)", 2 * vs * 1e3, 0.211, 0.002)

print("K-9 Übungen")
chk("ue1 v m/s", v_kl(e, me, 2500), 2.9654e7, 1e-4); chk("ue1 v/c", v_kl(e, me, 2500) / c, 0.099, 0.005)
chk("ue1 ohne Faktor 2", sqrt(e * 2500 / me), 2.097e7, 0.001); chk("ue1 Proton", v_kl(e, mp, 2500), 6.92e5, 0.002)
chk("ue1 rel. v m/s", beta_rel(e, me, 2500)[0] * c, 2.955e7, 0.001)
qq = 3.43e-15 * g * 6.0e-3 / 420
chk("ue2 q C", qq, 4.807e-19, 0.001); chk("ue2 q/e", qq / e, 3.0, 0.001); chk("ue2 E kV/m", 420 / 6e-3 / 1e3, 70.0)
UB, UA, LL, dd, DD = 1200, 24, 0.030, 8.0e-3, 0.150
ya5 = UA * LL ** 2 / (4 * dd * UB); t5 = 2 * ya5 / LL
chk("ue5 y_a mm", ya5 * 1e3, 0.5625, 1e-6); chk("ue5 tan", t5, 0.0375, 1e-6); chk("ue5 theta", degrees(atan(t5)), 2.15, 0.005)
chk("ue5 Y mm", t5 * (LL / 2 + DD) * 1e3, 6.19, 0.001); chk("ue5 nur D*tan mm", DD * t5 * 1e3, 5.625, 1e-6)
chk("ue5 Faktor 2 zu groß", 2 * t5 * (LL / 2 + DD) * 1e3, 12.375, 1e-6)
chk("ue5 Faktor 4 zu groß", 4 * t5 * (LL / 2 + DD) * 1e3, 24.75, 1e-6)
v5 = v_kl(e, me, UB); t_ = LL / v5; a5 = e * UA / dd / me
chk("ue5 v0", v5, 2.054e7, 0.001); chk("ue5 t ns", t_ * 1e9, 1.46, 0.003); chk("ue5 a", a5, 5.28e14, 0.003)
chk("ue5 y_a über t", 0.5 * a5 * t_ ** 2 * 1e3, 0.5625, 1e-6)
vs6 = 0.140e-3; r6 = sqrt(9 * eta * vs6 / (2 * rho * g)); m6 = 4 / 3 * pi * r6 ** 3 * rho; q6 = m6 * g * dM / 430
chk("ue6 r µm", r6 * 1e6, 1.153, 0.001); chk("ue6 m kg", m6, 5.612e-15, 0.001); chk("ue6 F_G N", m6 * g, 5.505e-14, 0.001)
chk("ue6 q C", q6, 6.401e-19, 0.001); chk("ue6 q/e", q6 / e, 3.996, 0.001)
chk("ue6 Stokes-Kontrolle", 6 * pi * eta * r6 * vs6, m6 * g, 1e-9)
chk("ue6 Re", rhoL * vs6 * 2 * r6 / eta, 2.1e-5, 0.03); chk("ue6 E kV/m", 430 / dM / 1e3, 86.0, 1e-6)
rw = sqrt(eta * vs6 / (rho * g)); chk("ue6 Fehler ohne 9/2", (rw / r6) ** 3 * q6 / e, 0.42, 0.01)
chk("ue6 Durchmesser statt r", 8 * q6 / e, 32.0, 0.005)
UB, UA = 2000, 100; Eq = UA / d
for nm, m in [("e", me), ("p", mp)]:
    chk("ue7 a " + nm, e * Eq / m, {"e": 8.794e14, "p": 4.788e11}[nm], 0.001)
v0 = v_kl(e, me, 2000)
chk("ue7 Fall II y_p µm", 0.5 * (e * Eq / mp) * (L / v0) ** 2 * 1e6, 1.225, 0.002)
chk("ue7 y_p/y_e", me / mp, 1 / 1836.6, 0.001); chk("ue7 t_p ns", L / v_kl(e, mp, 2000) * 1e9, 96.95, 0.001)
chk("ue7 t_p/t_e", sqrt(mp / me), 42.86, 0.001); chk("ue7 42,86^2", sqrt(mp / me) ** 2, 1836.6, 0.001)
chk("ue7 Proton-Energie bei v0 MeV", 0.5 * mp * v0 ** 2 / e / 1e6, 3.67, 0.002)
qm = [3.22, 4.79, 6.41, 8.05, 9.58]
chk("ue8 Summe", sum(qm), 32.05, 1e-9); chk("ue8 e-Schätzung", sum(qm) / 20, 1.6025, 1e-6)
chk("ue8 Abw. %", (sum(qm) / 20 / 1.602 - 1) * 100, 0.03, 0.1)
chk("ue8 mittlere Differenz", sum(qm[i + 1] - qm[i] for i in range(4)) / 4, 1.59, 0.003)
chk("ue8 q2/q1", qm[1] / qm[0], 1.49, 0.005); chk("ue8 q5/1,60", qm[4] / 1.6, 5.99, 0.002)
chk("ue8 n_max bei 1,5 %", 0.5 / 0.015, 33, 0.02)
vk = v_kl(e, me, 65e3); br, gam = beta_rel(e, me, 65e3)
chk("ue9 v_rel m/s", br * c, 1.383e8, 0.001); chk("ue9 Abw. %", (vk / (br * c) - 1) * 100, 9.3, 0.01)
chk("ue9 E_kin klass. mit v_rel keV", 0.5 * me * (br * c) ** 2 / e / 1e3, 54.4, 0.002)
chk("ue9 Fehlbetrag %", (1 - 0.5 * me * (br * c) ** 2 / (e * 65e3)) * 100, 16, 0.03)
chk("ue4 v(500 V)", v_kl(e, me, 500), 1.326e7, 0.001); chk("ue4 y_a(1000 V) mm", 100 * L ** 2 / (4 * d * 1000) * 1e3, 4.5, 1e-6)
chk("ue4 y_a(4000 V) mm", 100 * L ** 2 / (4 * d * 4000) * 1e3, 1.125, 1e-6)
chk("ue4 y_a(50 V) mm", 50 * L ** 2 / (4 * d * 2000) * 1e3, 1.125, 1e-6)

print("K-10 Vorwissen und Zusatz")
chk("vw2 t s", sqrt(2 * 0.8 / g), 0.404, 0.002); chk("vw2 x m", 3.0 * sqrt(2 * 0.8 / g), 1.21, 0.002)
chk("vw2 x ohne 2", 3.0 * sqrt(0.8 / g), 0.86, 0.01); chk("vw2 x lineare t", 3.0 * (2 * 0.8 / g), 0.49, 0.01)
ya = UA * L ** 2 / (4 * d * UB); vy = (e * Eq / me) * (L / v_kl(e, me, 2000))
chk("Zusatz Energiegewinn im Querfeld eV", 0.5 * me * vy ** 2 / e, 11.25, 0.002)
chk("Zusatz e*E*y_a in eV", Eq * ya, 11.25, 0.002)
print("\n%d Prüfungen bestanden, %d Abweichungen: %s" % (n_ok, len(fehler), fehler))
assert not fehler
```

---

<!-- FORTSCHRITT: Inhaltsdatei vollstaendig: Abschnitte 0-6, Lehrerteil, Checkliste, Kontrollrechnung (196 Pruefungen). Naechster Schritt liegt beim Bauagenten: module/physik-q1-geladene-teilchen-e-feld.html als Kopie von module/physik-q1-induktion.html. -->
