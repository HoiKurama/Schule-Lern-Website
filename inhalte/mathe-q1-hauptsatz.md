# Modulinhalt: mathe-q1-hauptsatz

**Datei für den Bauagenten:** `module/mathe-q1-hauptsatz.html`
**Fach/Stufe:** Mathematik · Qualifikationsphase 1 · Leistungskurs
**Kopf-Chips:** `Inhaltsfeld: Funktionen und Analysis` · `Kernlehrplan NRW, GOSt` · `ca. 90 Minuten`
**Titel im Kopf (`<h1>`):** Der Hauptsatz der Differential- und Integralrechnung
**Farbtokens:** Mathematik — `--akzent: #0d7a52`, `--akzent-hell: #e7f6ef`, `--akzent-rand: #b5e0cd`
**Footer-Zeile:** Mathematik LK Q1 · Stammfunktion, Hauptsatz und Integralfunktion · erstellt für den Unterricht nach dem Kernlehrplan NRW für die gymnasiale Oberstufe.

**Anschluss.** Baut unmittelbar auf `mathe-q1-integral-rekonstruktion.html` auf. Dort wurde das
bestimmte Integral als gemeinsamer Grenzwert von Unter- und Obersumme definiert, der Hauptsatz
ausdrücklich **nicht** eingeführt. Ober-/Untersummen, Intervalladditivität, orientierter
Flächeninhalt und die Unterscheidung Rate / Zuwachs / Bestand dürfen als bekannt vorausgesetzt
und **nicht erneut hergeleitet** werden. Die Zuflussrate `f(t) = −0,2t² + 1,6t + 1,8` aus der
Simulation des Vorgängermoduls wird hier bewusst wieder aufgegriffen — dieselben Zahlen, neuer
Rechenweg.

**Seitengliederung (sechs `<section>` gemäß CLAUDE.md):**

| `<section id>` | `.stufe`-Nr. | Überschrift | kommt aus Abschnitt |
|---|---|---|---|
| `einstieg` | 1 | Einstieg | Abschnitt 1 |
| `integralfunktion` | 2 | Die Integralfunktion und ihre Ableitung | Abschnitt 2 |
| `stammfunktion` | 3 | Stammfunktion, Hauptsatz und Rechenpraxis | Abschnitt 3 |
| `simulation` | 4 | Zwei Diagramme, ein Zusammenhang | Abschnitt 4 |
| `uebungen` | 5 | Übungen | Abschnitt 5 |
| `abschluss` | 6 | Zusammenfassung und Selbstcheck | Abschnitt 6 + Lehrerteil |

**Schreibweise in diesem Dokument.** Formeln stehen hier in Klartext. Der Bauagent setzt jede
davon als `<span class="m" data-tex="…" data-plain="…">` bzw. `<div class="m block">`. Wo die
LaTeX-Fassung nicht offensichtlich ist, steht sie als `TEX:` daneben. Alle Dezimalzahlen im
fertigen Modul mit **Komma**.

**Alle Zahlen in diesem Dokument sind gerechnet**, nicht geschätzt. Die Kontrollrechnungen
stehen jeweils unmittelbar bei der Stelle, an der die Zahl auftaucht. Numerische Gegenproben
wurden mit der Mittelpunktsregel bei 200 000 bzw. 400 000 Streifen durchgeführt.

---

## Abschnitt 1 — Einstieg

`<section id="einstieg">`, `.stufe`-Nummer **1**, Überschrift **Einstieg**.

### 1.1 Aufhänger (zwei Absätze Fließtext)

**Absatz 1.**
Du drehst die Dusche auf. An modernen Armaturen sitzt ein kleiner Durchflussmesser, der dir
sekündlich anzeigt, wie viel Wasser gerade läuft — mal 9 Liter pro Minute, mal 4, je nachdem,
wie weit du den Hebel aufmachst. Willst du am Ende wissen, wie viel du insgesamt verbraucht
hast, müsstest du nach dem Verfahren der letzten Einheit die ganze Kurve in Streifen zerlegen
und aufsummieren. Für eine Genauigkeit von einem Zehntelliter waren es dort dreihundertzwanzig
Streifen — für fünf Minuten Duschen ein absurder Aufwand.

**Absatz 2.**
Im Keller hängt derweil ein Wasserzähler. Der zeigt keine Rate, sondern einen Stand: 1834,62 m³.
Du liest ihn vor dem Duschen ab und danach noch einmal, ziehst ab, fertig. Zwei Zahlen statt
dreihundertzwanzig Streifen — und beide Wege liefern denselben Liter. Dass das kein Zufall ist,
sondern ein Satz, der Ableiten und Integrieren zu zwei Richtungen derselben Straße macht, ist
das Thema dieser Einheit. Die eigentliche Frage ist dabei nicht, wie man die Subtraktion
ausführt, sondern warum der Zählerstand überhaupt etwas über die Fläche unter dem Ratengraphen
weiß.

### 1.2 Vorwissensfragen (Multiple Choice, `.karte` mit `<h3>Vorwissen prüfen</h3>`)

Einleitungssatz unter der Überschrift (grau, 15 px):
*Zwei Fragen aus der Einführungsphase, eine aus der letzten Einheit. Wenn du hier hängst, lohnt
sich ein Blick zurück, bevor du weitermachst.*

**vw1** — Schlüssel `vw1`, Radio-Name `vw1`, richtige Option: **Index 1**

> Frage: Welche der drei Funktionen hat die Ableitung `f(x) = x²`?
>
> - `data-i="0"`: `F(x) = 2x`
> - `data-i="1"`: `F(x) = (1/3)·x³ − 5`
> - `data-i="2"`: `F(x) = x³`

Feedback (`fb`-Array, drei Einträge):

- **Index 0:** Du hast abgeleitet statt rückwärts gedacht: Aus `x²` wird beim Ableiten `2x`.
  Gesucht ist aber die Funktion, die man ableiten **muss**, um `x²` zu bekommen — dabei wächst
  der Exponent um 1, er schrumpft nicht.
- **Index 1 (richtig):** Richtig. `F′(x) = (1/3)·3x² = x²`, und die Konstante `−5` fällt beim
  Ableiten weg. Genau diese drei Beobachtungen — Exponent plus eins, Vorfaktor ausgleichen,
  Konstante beliebig — tragen die ganze Einheit.
- **Index 2:** Fast. Der Exponent stimmt, aber `(x³)′ = 3x²` — das ist dreimal zu viel. Der
  Faktor `1/3` muss vorgezogen werden, damit beim Ableiten wieder genau `x²` herauskommt.

**vw2** — Schlüssel `vw2`, Radio-Name `vw2`, richtige Option: **Index 2**

> Frage: Für eine auf `[2; 5]` differenzierbare Funktion `F` gilt `F′(x) < 0` für alle `x` aus
> diesem Intervall. Was folgt daraus sicher?
>
> - `data-i="0"`: `F(x) < 0` für alle `x` aus `[2; 5]`.
> - `data-i="1"`: `F` hat in `[2; 5]` mindestens eine Nullstelle.
> - `data-i="2"`: `F` ist auf `[2; 5]` streng monoton fallend.

Feedback:

- **Index 0:** Das ist die häufigste Verwechslung im ganzen Kapitel — sie wird dich hier noch
  verfolgen. Die Ableitung sagt etwas über die **Steigung**, nicht über die Höhe.
  `F(x) = 100 − x` hat überall die Ableitung `−1 < 0` und ist auf `[2; 5]` trotzdem durchgehend
  positiv (von 98 bis 95).
- **Index 1:** Eine Nullstelle ist nicht erzwungen. `F(x) = 100 − x` fällt auf `[2; 5]` streng
  monoton und kommt der Null nicht einmal nahe. Fallen heißt nicht, dass man unterwegs die
  Achse trifft.
- **Index 2 (richtig):** Richtig, das ist das Monotoniekriterium aus der Einführungsphase:
  negative Ableitung auf einem Intervall heißt streng monoton fallend. Mehr folgt daraus nicht —
  insbesondere nichts über das Vorzeichen von `F` selbst.

**vw3** — Schlüssel `vw3`, Radio-Name `vw3`, richtige Option: **Index 1**

> Frage: Eine Zuflussrate `f` ist auf `[0; 4]` positiv und auf `[4; 6]` negativ. Bekannt sind
> `∫₀⁴ f(t) dt = 18` und `∫₄⁶ f(t) dt = −6` (jeweils in m³). Wie groß ist `∫₀⁶ f(t) dt`?
>
> - `data-i="0"`: `24 m³`
> - `data-i="1"`: `12 m³`
> - `data-i="2"`: `18 m³`

Feedback:

- **Index 0:** Du hast die Beträge addiert. `24 m³` ist die insgesamt **bewegte** Wassermenge —
  zugeflossen plus abgeflossen. Das Integral zählt aber orientiert: Was unterhalb der Achse
  liegt, wird abgezogen.
- **Index 1 (richtig):** Richtig. Intervalladditivität: `∫₀⁶ = ∫₀⁴ + ∫₄⁶ = 18 + (−6) = 12`.
  Der Bestand ist am Ende um `12 m³` gewachsen, obwohl zwischendurch `6 m³` wieder abgeflossen
  sind.
- **Index 2:** Du hast den negativen Anteil weggelassen. `18 m³` ist der Zuwachs bis `t = 4` —
  danach passiert aber noch etwas, und zwar in die andere Richtung. Ein Integral über ein
  größeres Intervall kann durchaus kleiner sein als über ein kleineres.

**Kontrollrechnung vw3.** `18 + (−6) = 12`. Gegenprobe an der Modellrate dieses Moduls
(`f(t) = −0,2t² + 1,6t + 1,8`): `∫₀⁹ f dt = 32,40`, `∫₉¹² f dt = 21,60 − 32,40 = −10,80`,
Summe `21,60`. Numerisch mit 400 000 Streifen: `21,600000000`; analytisch `21,6`; Abweichung
`1,8·10⁻¹⁰`.

---

## Abschnitt 2 — Erklärteil, erster Block

`<section id="integralfunktion">`, `.stufe`-Nummer **2**,
Überschrift **Die Integralfunktion und ihre Ableitung**.

### 2.1 Die obere Grenze wird zur Variablen (`<h3>`)

Bisher war ein Integral eine **Zahl**: `∫₀⁶ f(t) dt = 25,2 m³`. Zwei feste Grenzen hinein, eine
Zahl heraus. Der Wasserzähler im Keller macht etwas anderes: Er zeigt zu **jedem** Zeitpunkt
einen Wert an. Sein Stand ist keine Zahl, sondern eine Funktion der Zeit.

Genau das ist der Schritt. Wir halten die untere Grenze fest und lassen die obere wandern:

> **Definition (Integralfunktion).** `f` sei auf einem Intervall `I` stetig und `a ∈ I` fest.
> Dann heißt
>
> `I_a(x) = ∫ₐˣ f(t) dt` für `x ∈ I`
>
> die **Integralfunktion von `f` zur unteren Grenze `a`**.
>
> TEX: `I_a(x) = \int_a^x f(t)\,\mathrm{d}t`
> data-plain: `I_a(x) = ∫ von a bis x f(t) dt`

Zwei Dinge an der Schreibweise sind keine Schönheitsfrage, sondern Pflicht:

1. **Die Integrationsvariable heißt `t`, nicht `x`.** `x` ist jetzt die obere Grenze und damit
   die Variable der neuen Funktion. `∫ₐˣ f(x) dx` wäre so sinnvoll wie eine Laufvariable, die
   gleichzeitig das Schleifenende ist. Welchen Buchstaben du für die Integrationsvariable
   nimmst, ist dagegen völlig egal: `∫ₐˣ f(t) dt` und `∫ₐˣ f(u) du` sind dieselbe Funktion.
2. **`I_a(a) = 0`**, denn `∫ₐᵃ f(t) dt = 0`. Jede Integralfunktion hat an ihrer unteren Grenze
   eine Nullstelle. Merk dir das, es wird in Abschnitt 3 zum Erkennungszeichen.

**Beispiel mit den Zahlen aus der letzten Einheit.** Der Zufluss in ein Rückhaltebecken war
`f(t) = −0,2t² + 1,6t + 1,8` (in m³/h, `t` in h). Die Werte der Integralfunktion `I₀` hattest du
in der Simulation abgelesen (Tabelle in `<div class="tabelle">` kapseln):

| `x` in h | 0 | 3 | 6 | 9 | 12 |
|---|---|---|---|---|---|
| `f(x)` in m³/h | 1,80 | 4,80 | 4,20 | 0,00 | −7,80 |
| `I₀(x)` in m³ | 0,00 | 10,80 | 25,20 | 32,40 | 21,60 |

*Kontrollrechnung (numerisch, Mittelpunktsregel, 400 000 Streifen):*
`∫₀³ f = 10,800000`, `∫₀⁶ f = 25,200000`, `∫₀⁹ f = 32,400000`, `∫₀¹² f = 21,600000`.
Größte Abweichung zur geschlossenen Form `1,8·10⁻¹⁰`.
Funktionswerte: `f(0) = 1,80`, `f(3) = −1,8 + 4,8 + 1,8 = 4,80`, `f(6) = −7,2 + 9,6 + 1,8 = 4,20`,
`f(9) = −16,2 + 14,4 + 1,8 = 0,00`, `f(12) = −28,8 + 19,2 + 1,8 = −7,80`.

Schau dir die letzte Spalte an: `I₀` **wächst nicht mehr**, sondern fällt zwischen 9 h und 12 h
von 32,40 auf 21,60. Und genau dort ist `f` negativ geworden. Das ist kein Zufall.

### 2.2 Die Beobachtung: `I` weiß von `f` mehr, als es müsste (`<h3>`)

Wir messen die Steigung von `I₀` an der Stelle `x = 3` — ganz normal über Differenzenquotienten
(Tabelle in `<div class="tabelle">` kapseln):

| `h` | `(I₀(3 + h) − I₀(3)) / h` |
|---|---|
| 1 | 4,93333 |
| 0,5 | 4,88333 |
| 0,1 | 4,81933 |
| 0,01 | 4,80199 |
| 0,001 | 4,80020 |

Die Zahlen laufen auf **4,80** zu. Und `f(3) = −0,2·9 + 1,6·3 + 1,8 = −1,8 + 4,8 + 1,8 = 4,80`.

*Kontrollrechnung:* mit `I₀(x) = −x³/15 + 0,8x² + 1,8x` ergibt sich `I₀(3) = 10,80000`,
`I₀(4) = 15,73333`, `I₀(3,5) = 13,24167`, `I₀(3,1) = 11,28193`, `I₀(3,01) = 10,84802`,
`I₀(3,001) = 10,80480`. Die Differenzenquotienten daraus sind die Tabellenwerte; die Abweichung
zu 4,80 schrumpft von `1,33·10⁻¹` auf `2,00·10⁻⁴`, also linear mit `h`.

Dasselbe an jeder anderen Stelle. Die Vermutung liegt auf dem Tisch:

> **Merksatz (Kernaussage 1).** Die Integralfunktion ist die Umkehrung des Ableitens.
> Wer eine Rate aufsummiert und dann wieder die Änderungsrate des Aufsummierten bildet, landet
> bei der Rate, mit der er angefangen hat. Das Integral verliert unterwegs keine Information —
> es hält sie nur in anderer Form fest.

Anschaulich ist das auch ohne Rechnung plausibel: Wenn zur Zeit `x` gerade 4,80 m³ pro Stunde
zulaufen, dann steigt der Zählerstand in diesem Moment eben mit 4,80 m³ pro Stunde. Der Wert
der Rate **ist** die Wachstumsgeschwindigkeit des Bestands. Was fehlt, ist der Beweis, dass das
für jede stetige Funktion gilt und nicht nur für unser Beispiel.

### 2.3 Herleitung (ausgelagert in `<details>`)

`<summary>` **Warum `I_a′(x) = f(x)` gilt — die Begründung mit einem einzigen Streifen** `</summary>`

**Schritt 1 — den Differenzenquotienten als Integral schreiben.** Für `h > 0` liefert die
Intervalladditivität, die du schon kennst:

`I_a(x + h) − I_a(x) = ∫ₐ^(x+h) f − ∫ₐˣ f = ∫ₓ^(x+h) f(t) dt`

TEX: `I_a(x+h) - I_a(x) = \int_a^{x+h} f - \int_a^{x} f = \int_x^{x+h} f(t)\,\mathrm{d}t`

Der Zähler des Differenzenquotienten ist also das Integral über **ein einziges schmales
Intervall** der Breite `h`. Genau das Objekt, mit dem du in der letzten Einheit hantiert hast:
ein Streifen.

**Schritt 2 — den Streifen einschachteln.** `f` ist stetig, und `[x; x + h]` ist abgeschlossen
und beschränkt; also nimmt `f` dort ein Minimum `m(h)` und ein Maximum `M(h)` an (Satz vom
Minimum und Maximum). Für diesen einen Streifen sind `m(h)·h` die Untersumme und `M(h)·h` die
Obersumme, und aus der Definition des Integrals folgt unmittelbar

`m(h)·h ≤ ∫ₓ^(x+h) f(t) dt ≤ M(h)·h`

TEX: `m(h)\cdot h \le \int_x^{x+h} f(t)\,\mathrm{d}t \le M(h)\cdot h`

**Schritt 3 — durch `h` teilen.** Weil `h > 0` ist, bleiben die Ungleichheitszeichen stehen:

`m(h) ≤ (I_a(x + h) − I_a(x)) / h ≤ M(h)`

**Schritt 4 — Grenzübergang.** Für `h → 0` schrumpft das Intervall `[x; x + h]` auf den Punkt
`x` zusammen. Weil `f` **stetig** ist, streben sowohl das Minimum als auch das Maximum auf
diesem Intervall gegen `f(x)`:

`lim (h→0⁺) m(h) = f(x)` und `lim (h→0⁺) M(h) = f(x)`

Der Differenzenquotient ist zwischen zwei Größen eingeklemmt, die denselben Grenzwert haben.
Nach dem Einschließungskriterium hat er selbst diesen Grenzwert:

`lim (h→0⁺) (I_a(x + h) − I_a(x)) / h = f(x)`

**Schritt 5 — negative `h`.** Für `h < 0` läuft die Rechnung gleich, nur heißt das Intervall
jetzt `[x + h; x]`, und die Division durch das negative `h` dreht die Ungleichungen um — die
Einschachtelung bleibt, nur mit vertauschten Rollen von `m` und `M`. Rechts- und linksseitiger
Grenzwert stimmen überein, also existiert die Ableitung, und es gilt `I_a′(x) = f(x)`. ∎

**Wo genau die Stetigkeit gebraucht wird.** Nur in Schritt 4. Ohne sie könnten `m(h)` und `M(h)`
auch bei beliebig kleinem `h` weit auseinanderliegen, und die Zange schließt sich nicht. Das ist
derselbe Punkt, an dem in der letzten Einheit die Schere `O_n − U_n` gegen null ging: dasselbe
Argument, nur auf einen einzigen Streifen angewandt statt auf alle gleichzeitig.

*(Ende `<details>`.)*

### 2.4 Hauptsatz, Teil 1 (`<h3>`)

> **Hauptsatz der Differential- und Integralrechnung, Teil 1.**
> Ist `f` auf einem Intervall `I` stetig und `a ∈ I`, so ist die Integralfunktion
> `I_a(x) = ∫ₐˣ f(t) dt` auf `I` differenzierbar, und es gilt
>
> `I_a′(x) = f(x)` für alle `x ∈ I`.
>
> TEX (abgesetzt): `\frac{\mathrm{d}}{\mathrm{d}x}\int_a^x f(t)\,\mathrm{d}t = f(x)`
> data-plain: `d/dx ∫ von a bis x f(t) dt = f(x)`

Der Satz sagt zwei Dinge, und das zweite wird gern überlesen:

- Ableiten macht das Integrieren rückgängig.
- **Jede stetige Funktion besitzt überhaupt eine Funktion, deren Ableitung sie ist** — nämlich
  ihre Integralfunktion. Das ist eine Existenzaussage, und sie ist alles andere als
  selbstverständlich. Zu `f(x) = e^(−x²)` etwa findest du durch noch so geschicktes
  Rückwärtsableiten keine Stammfunktion, weil es keine gibt, die sich mit den Funktionen der
  Schule hinschreiben lässt. Existieren tut sie trotzdem — der Hauptsatz liefert sie als
  Integral.

### 2.5 Die typische Fehlvorstellung — und was dagegen hilft (`<div class="hinweis">`)

**Häufiger Fehler.** „Wenn `f` negativ ist, ist auch `I` negativ." Das klingt zwingend und ist
falsch. Richtig ist: Wenn `f` negativ ist, **fällt** `I`. Über die Höhe von `I` sagt das
Vorzeichen von `f` gar nichts.

Rechne es an der Modellrate nach. Bei `x = 10,5` ist

`f(10,5) = −0,2·110,25 + 1,6·10,5 + 1,8 = −22,05 + 16,80 + 1,80 = −3,45` (m³/h)

und trotzdem

`I₀(10,5) = −10,5³/15 + 0,8·10,5² + 1,8·10,5 = −77,175 + 88,20 + 18,90 = 29,925` (m³).

*Kontrollrechnung:* `10,5³ = 1157,625`, `1157,625/15 = 77,175`; `10,5² = 110,25`,
`0,8·110,25 = 88,20`; `1,8·10,5 = 18,90`. Numerische Gegenprobe `∫₀^10,5 f dt = 29,925000`.

Die Rate ist negativ, der Bestand ist mit knapp 30 m³ immer noch deutlich positiv — er ist eben
nur auf dem Rückweg. Wer das verwechselt, hat `I` als „Fläche" gelesen statt als Bestand.

> **Merksatz (Kernaussage 2).** Das Vorzeichen von `f` steuert die **Monotonie** von `I`, nicht
> das Vorzeichen von `I`. `f > 0` heißt: `I` steigt. `f < 0` heißt: `I` fällt. Hat `f` eine
> Nullstelle mit Vorzeichenwechsel, so hat `I` dort einen Extrempunkt. Alles, was du über
> Monotonie, Extrem- und Wendepunkte aus der Kurvendiskussion weißt, gilt unverändert weiter —
> `f` ist hier einfach die erste Ableitung von `I`.

---

## Abschnitt 3 — Erklärteil, zweiter Block (Vertiefung)

`<section id="stammfunktion">`, `.stufe`-Nummer **3**,
Überschrift **Stammfunktion, Hauptsatz und Rechenpraxis**.

### 3.1 Der Begriff Stammfunktion (`<h3>`)

Die Integralfunktion ist ein Beispiel für etwas Allgemeineres. Wir geben dem Ding einen Namen
und lösen es vom Integral ab:

> **Definition (Stammfunktion).** `F` heißt **Stammfunktion** von `f` auf einem Intervall `I`,
> wenn `F` dort differenzierbar ist und `F′(x) = f(x)` für alle `x ∈ I` gilt.

Nach Teil 1 des Hauptsatzes ist `I_a` eine Stammfunktion von `f`. Sie ist aber nicht die
einzige: Ist `F` eine Stammfunktion, so auch `F + 7`, `F − 1000` und `F + C` für jedes reelle
`C`, weil Konstanten beim Ableiten wegfallen. Die entscheidende Frage ist, ob es darüber hinaus
noch andere gibt.

> **Satz.** Sind `F` und `G` beide Stammfunktionen von `f` auf **einem Intervall** `I`, so gibt
> es eine Konstante `C` mit `G(x) = F(x) + C` für alle `x ∈ I`.

**`<details>`** — `<summary>` **Beweis: warum sich zwei Stammfunktionen nur um eine Konstante unterscheiden** `</summary>`

Setze `D = G − F`. Dann ist `D′(x) = G′(x) − F′(x) = f(x) − f(x) = 0` für alle `x ∈ I`. Eine
Funktion, deren Ableitung auf einem Intervall überall null ist, ist dort konstant: Zu je zwei
Stellen `x₁ < x₂` aus `I` liefert der Mittelwertsatz ein `ξ` dazwischen mit

`D(x₂) − D(x₁) = D′(ξ)·(x₂ − x₁) = 0·(x₂ − x₁) = 0`,

also `D(x₂) = D(x₁)`. Da `x₁` und `x₂` beliebig waren, nimmt `D` auf `I` überall denselben Wert
`C` an, und es folgt `G = F + C`. ∎

**Warum „auf einem Intervall" nicht weggelassen werden darf.** Auf `ℝ \ {0}` ist sowohl
`F(x) = −1/x` eine Stammfunktion von `f(x) = 1/x²` als auch die Funktion `G`, die für `x < 0`
gleich `−1/x` und für `x > 0` gleich `−1/x + 1` ist (Probe: `F′(x) = 1/x² = f(x)`, und `G` hat
stückweise dieselbe Ableitung). Die Differenz `G − F` ist links von null gleich 0 und rechts
davon gleich 1 — nicht konstant. Der Definitionsbereich zerfällt eben in zwei Intervalle, und
auf jedem darf die Konstante anders sein.

*(Ende `<details>`.)*

> **Merksatz (Kernaussage 3).** Die Menge aller Stammfunktionen einer Funktion auf einem
> Intervall ist eine **Schar paralleler Graphen**: `F(x) + C`. Sie unterscheiden sich in der
> Höhe, nirgends in der Steigung. Deshalb ist das `+ C` kein Schönheitsfehler, sondern die
> Aussage, dass die Ableitung die Höhenlage nicht kennt — und nicht kennen kann.

### 3.2 Hauptsatz, Teil 2 — die Berechnungsformel (`<h3>`)

> **Hauptsatz der Differential- und Integralrechnung, Teil 2.**
> Ist `f` auf `[a; b]` stetig und `F` **irgendeine** Stammfunktion von `f` auf `[a; b]`, so gilt
>
> `∫ₐᵇ f(x) dx = F(b) − F(a) = [F(x)]ₐᵇ`
>
> TEX (abgesetzt): `\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a) = \big[F(x)\big]_a^b`
> data-plain: `∫ von a bis b f(x) dx = F(b) − F(a) = [F(x)] von a bis b`

**`<details>`** — `<summary>` **Wie aus Teil 1 die Berechnungsformel wird — und warum das `+ C` egal ist** `</summary>`

Nach Teil 1 ist `I_a(x) = ∫ₐˣ f(t) dt` eine Stammfunktion von `f`. Sei `F` eine beliebige
weitere. Nach dem Satz aus 3.1 unterscheiden sich beide nur um eine Konstante:

`F(x) = I_a(x) + C`

Damit rechnen wir die Differenz aus:

`F(b) − F(a) = (I_a(b) + C) − (I_a(a) + C) = I_a(b) − I_a(a)`

Das `C` kürzt sich weg — **deshalb** darf man irgendeine Stammfunktion nehmen. Und weil
`I_a(a) = ∫ₐᵃ f(t) dt = 0` ist, bleibt

`F(b) − F(a) = I_a(b) = ∫ₐᵇ f(t) dt` ∎

Halte fest, was hier eigentlich passiert ist: Ein Grenzwert von Summen mit beliebig vielen
Summanden wird durch **zwei Funktionswerte** ersetzt. Der gesamte Aufwand der letzten Einheit —
Streifen, Einschachtelung, 320 Rechtecke für ein Zehntel Kubikmeter — schrumpft auf eine
Subtraktion. Das ist der Grund, warum dieser Satz „Hauptsatz" heißt und nicht „Satz 7.3".

*(Ende `<details>`.)*

Kontrolle am Einstiegsbeispiel: Der Wasserzähler zeigt einen Bestand, also eine Stammfunktion
der Durchflussrate. Vorher ablesen, nachher ablesen, subtrahieren — das ist buchstäblich
`F(b) − F(a)`. Der Hauptsatz sagt zusätzlich: Wie der Zähler irgendwann geeicht wurde, ist für
den Verbrauch bedeutungslos. Genau das ist das `+ C`.

### 3.3 Grundintegrale und Regeln (`<h3>`)

Damit ist Integrieren zum Rückwärtsableiten geworden. Die Tabelle liest man von rechts nach
links, wenn man ableitet, und von links nach rechts, wenn man integriert
(in `<div class="tabelle">` kapseln):

| `f(x)` | Stammfunktion `F(x)` | Bedingung |
|---|---|---|
| `c` (konstant) | `c·x` | — |
| `xⁿ` | `x^(n+1)/(n + 1)` | `n ≠ −1` |
| `1/x` | `ln(\|x\|)` | `x ≠ 0` |
| `eˣ` | `eˣ` | — |
| `e^(kx)` | `(1/k)·e^(kx)` | `k ≠ 0` |
| `sin x` | `−cos x` | — |
| `cos x` | `sin x` | — |

Dazu drei Regeln, die direkt aus den Ableitungsregeln folgen:

- **Faktorregel:** `∫ c·f(x) dx = c·∫ f(x) dx`
- **Summenregel:** `∫ (f(x) + g(x)) dx = ∫ f(x) dx + ∫ g(x) dx`
- **Lineare Substitution:** Ist `F` Stammfunktion von `f`, so ist `(1/k)·F(kx + b)` Stammfunktion
  von `f(kx + b)`. Der Faktor `1/k` gleicht die innere Ableitung aus.
  TEX: `\int f(kx+b)\,\mathrm{d}x = \tfrac{1}{k}\,F(kx+b) + C`

**Warnung, die im LK jedes Jahr Punkte kostet.** Es gibt **keine** Produktregel und **keine**
Quotientenregel für Integrale. `∫ f·g` ist nicht `(∫f)·(∫g)`. Probe in einer Zeile:

`∫₀¹ x·x dx = ∫₀¹ x² dx = 1/3 ≈ 0,3333`, aber `(∫₀¹ x dx)·(∫₀¹ x dx) = (1/2)·(1/2) = 1/4 = 0,25`.

*Kontrollrechnung (numerisch, 200 000 Streifen):* `∫₀¹ x² dx = 0,33333333` und
`(∫₀¹ x dx)² = 0,25000000` — die beiden Zahlen sind verschieden, damit ist die Produktregel
widerlegt. Die einzige Rückwärtsversion der Kettenregel, die du in Q1 brauchst, ist die lineare
Substitution oben.

### 3.4 Was die Integralfunktion von `f` erbt (`<h3>`)

Weil `I_a′ = f` gilt, verschiebt sich alles um **eine Ableitungsstufe nach oben**. Das ist die
Tabelle, die im Abitur bei jeder Graphenzuordnung gebraucht wird
(in `<div class="tabelle">` kapseln):

| am Graphen von `f` | folgt für `I_a` | Beleg an der Modellrate |
|---|---|---|
| `f(x) > 0` | `I_a` streng monoton steigend | auf `[0; 9]` steigt `I₀` von 0,00 auf 32,40 |
| `f(x) < 0` | `I_a` streng monoton fallend | auf `[9; 12]` fällt `I₀` von 32,40 auf 21,60 |
| Nullstelle von `f`, VZW `+ → −` | Hochpunkt von `I_a` | `x = 9`, Hochpunkt `(9 \| 32,40)` |
| Nullstelle von `f`, VZW `− → +` | Tiefpunkt von `I_a` | Rate B in der Simulation: `x = 4` |
| Hochpunkt von `f` | Wendestelle von `I_a`, größte Steigung | `x = 4`, `I₀(4) = 15,73`, Steigung `5,00` |
| `f` streng monoton steigend | `I_a` linksgekrümmt | auf `[0; 4]` |
| `f` streng monoton fallend | `I_a` rechtsgekrümmt | auf `[4; 12]` |

*Kontrollrechnung zur Zeile „Hochpunkt von `f`":* `f′(t) = −0,4t + 1,6 = 0` ⟺ `t = 4`;
`f(4) = −0,2·16 + 1,6·4 + 1,8 = −3,20 + 6,40 + 1,80 = 5,00`;
`I₀(4) = −64/15 + 0,8·16 + 1,8·4 = −4,26667 + 12,80 + 7,20 = 15,73333`.
`I₀″(t) = f′(t) = −0,4t + 1,6` wechselt bei `t = 4` das Vorzeichen von `+` nach `−`: eine
Links-Rechts-Wendestelle.
*Kontrollrechnung zur Zeile „VZW `+ → −`":* `f(8) = −12,8 + 12,8 + 1,8 = +1,80`,
`f(10) = −20 + 16 + 1,8 = −2,20`. Vorzeichenwechsel bestätigt; `I₀(9) = 32,40` ist größer als
`I₀(8) = 31,46667` und `I₀(10) = 31,33333`.

### 3.5 Die untere Grenze verschieben (`<h3>`)

Was passiert, wenn man `a` ändert? Wieder Intervalladditivität:

`I_b(x) = ∫_b^x f(t) dt = ∫ₐˣ f(t) dt − ∫ₐᵇ f(t) dt = I_a(x) − I_a(b)`

TEX: `I_b(x) = I_a(x) - I_a(b)`

Es kommt also nur eine **Konstante** dazu — der Graph verschiebt sich senkrecht, die Form bleibt
gleich. Das passt zusammen: Alle Integralfunktionen derselben Funktion sind Stammfunktionen und
unterscheiden sich daher höchstens um eine Konstante.

Zahlenprobe an der Modellrate mit `I₀(3) = 10,80` (in `<div class="tabelle">` kapseln):

| `x` in h | 0 | 3 | 6 | 9 | 12 |
|---|---|---|---|---|---|
| `I₀(x)` in m³ | 0,00 | 10,80 | 25,20 | 32,40 | 21,60 |
| `I₃(x)` in m³ | −10,80 | 0,00 | 14,40 | 21,60 | 10,80 |
| Differenz | 10,80 | 10,80 | 10,80 | 10,80 | 10,80 |

Die Differenz ist in jeder Spalte 10,80 — konstant, wie behauptet. Und `I₃(3) = 0`, wie es sein
muss.

### 3.6 Nicht jede Stammfunktion ist eine Integralfunktion (`<div class="hinweis">`)

Umgekehrt gilt der Zusammenhang **nicht**. Nimm `f(x) = eˣ`. Die Integralfunktionen sind

`I_a(x) = ∫ₐˣ e^t dt = [e^t]ₐˣ = eˣ − e^a`

Weil `e^a > 0` für jedes reelle `a` ist, kann die additive Konstante `−e^a` nur **negativ**
sein. `F(x) = eˣ − 1` ist also eine Integralfunktion (zu `a = 0`), `F(x) = eˣ + 1` dagegen
nicht: Man müsste `e^a = −1` lösen, und das geht nicht.

> **Kriterium.** Eine Stammfunktion `F` von `f` auf einem Intervall `I` ist **genau dann** eine
> Integralfunktion von `f`, wenn sie in `I` mindestens eine **Nullstelle** hat. Denn ist
> `F(a) = 0`, so haben `F` und `I_a` dieselbe Ableitung und denselben Wert an der Stelle `a` —
> die Konstante zwischen ihnen ist damit null, also `F = I_a`.
>
> Probe: `eˣ + 1 = 0` hat keine Lösung (`eˣ > 0`), `eˣ − 1 = 0` hat die Lösung `x = 0` — und das
> ist genau die untere Grenze.
>
> *Kontrollrechnung:* `eˣ + c` ist genau für `c < 0` eine Integralfunktion, dann mit
> `a = ln(−c)`. Für `c = −0,5` etwa `a = ln 0,5 = −0,6931`, Probe: `e^(−0,6931) = 0,5000 = −c` ✓.
> Für `c = 0` und `c = 1` ist `e^a = −c` unlösbar.

Damit gilt: **Jede Integralfunktion ist eine Stammfunktion, aber nicht jede Stammfunktion ist
eine Integralfunktion.** Die Unterscheidung wirkt kleinlich, ist aber ein beliebter
Prüfungsgegenstand, weil sie zeigt, ob man den Unterschied zwischen einer Definition und einer
Eigenschaft verstanden hat.

---

## Abschnitt 4 — Interaktiver Kern

`<section id="simulation">`, `.stufe`-Nummer **4**,
Überschrift **Zwei Diagramme, ein Zusammenhang**.

### 4.1 Was die Simulation zeigen soll

Ein Canvas (`id="cvSim"`, `width="1000" height="560"`, per CSS `width:100%`), darin zwei
**übereinanderliegende** Koordinatensysteme mit gemeinsamer `t`-Achse:

- **oben (die Rate `f`):** der Graph von `f` auf `[0; 12]`. Der Bereich zwischen den Grenzen
  `a` und `x` ist eingefärbt: Flächenstücke oberhalb der Achse in `--akzent-hell` mit Rand
  `--akzent`, Flächenstücke unterhalb in `#fee2e2` mit Rand `#dc2626`. Senkrechte Linie bei
  `t = a` (gestrichelt, beschriftet mit `a`) und bei `t = x` (durchgezogen, beschriftet mit `x`).
- **unten (die Integralfunktion `I_a`):** der Graph von `I_a` über `[0; 12]`, **durchgezogen bis
  zur aktuellen Stelle `x`, danach hellgrau gestrichelt**. So baut sich die Kurve beim Ziehen
  sichtbar auf. Am Punkt `(x | I_a(x))` ein ausgefüllter Kreis und — wenn die Checkbox gesetzt
  ist — die Tangente mit der Steigung `f(x)`, gezeichnet über `x ± 1,5` Stunden.

Der didaktische Kern ist das Nebeneinander zweier **unabhängig gewonnener Zahlen**: `f(x)` wird
aus der Funktionsgleichung berechnet und gehört zum oberen Diagramm; die Steigung von `I_a`
wird numerisch aus der aufsummierten Fläche bestimmt und gehört zum unteren. Der Hauptsatz
behauptet, dass sie gleich sind — und die Anzeige zeigt es Ziffer für Ziffer.

### 4.2 Auswählbare Raten (drei Knöpfe in `.knopfleiste`, `data-rate="A|B|C"`)

Alle drei sind Zuflussraten in m³/h, `t` in h, dargestellt auf `[0; 12]`.

| Knopf | `f(t)` | geschlossene Stammfunktion `F(t)` mit `F(0) = 0` | Besonderheit |
|---|---|---|---|
| **Rate A** – „Regenrückhaltebecken" | `−0,2t² + 1,6t + 1,8` | `−t³/15 + 0,8t² + 1,8t` | Nullstelle bei `t = 9` mit VZW `+ → −`, Hochpunkt der Rate bei `t = 4` |
| **Rate B** – „Zulauf setzt spät ein" | `0,8t − 3,2` | `0,4t² − 3,2t` | Nullstelle bei `t = 4` mit VZW `− → +` |
| **Rate C** – „auslaufender Tank" | `4·e^(−0,3t)` | `−(40/3)·e^(−0,3t) + 40/3` | überall positiv, keine Extremstelle von `I` |

*Kontrollrechnungen zu den Stammfunktionen:*
Rate A: `F′(t) = −3t²/15 + 1,6t + 1,8 = −0,2t² + 1,6t + 1,8` ✓.
Rate B: `F′(t) = 0,8t − 3,2` ✓. Nullstelle `0,8t = 3,2` ⟹ `t = 4`.
Rate C: `F′(t) = −(40/3)·(−0,3)·e^(−0,3t) = 4·e^(−0,3t)` ✓.

*Wertetabellen (für die Abnahme durch den Bauagenten):*

Rate A: `f(0) = 1,80`, `f(4) = 5,00`, `f(9) = 0,00`, `f(10,5) = −3,45`, `f(12) = −7,80`;
`F(3) = 10,80`, `F(4) = 15,73333`, `F(6) = 25,20`, `F(9) = 32,40`, `F(10,5) = 29,925`,
`F(12) = 21,60`.

Rate B: `f(0) = −3,20`, `f(4) = 0,00`, `f(12) = 6,40`;
`F(2) = −4,80`, `F(4) = −6,40`, `F(6) = −4,80`, `F(8) = 0,00`, `F(12) = 19,20`.

Rate C: `f(0) = 4,00`, `f(5) = 0,89252`, `f(12) = 0,10929`;
`F(5) = 10,35826`, `F(12) = 12,96902`; Grenzwert für `t → ∞`: `40/3 = 13,33333`.

### 4.3 Wie der Bauagent rechnen soll

**Integralwert (die untere Kurve).** Nicht die geschlossene Form verwenden, sondern **numerisch
aufsummieren** — das ist der ehrliche Anschluss an die letzte Einheit und macht die Anzeige
unabhängig von der Stammfunktion:

```
function Isum(f, a, x){            // Simpson-Regel, n = 200 Teilintervalle
  if (Math.abs(x - a) < 1e-12) return 0;
  var n = 200, h = (x - a)/n, s = f(a) + f(x);
  for (var k = 1; k < n; k++) s += (k % 2 ? 4 : 2) * f(a + k*h);
  return s * h / 3;
}
```

Vorzeichen: Bei `x < a` liefert die Formel automatisch den negativen Wert — genau richtig, denn
`∫ₐˣ = −∫ₓᵃ`. Diesen Fall im Text ausdrücklich erwähnen.

*Genauigkeitsprüfung (gerechnet):* Über alle Kombinationen `a ∈ {0; 1,5; 3; 7,5; 12}` und
`x ∈ {0; 2,5; 6; 9; 12}` und alle drei Raten beträgt der größte Unterschied zur geschlossenen
Form `7,6·10⁻⁹`. Für die Raten A und B ist Simpson sogar exakt (Fehler `< 3·10⁻¹⁴`), weil die
Regel Polynome bis zum Grad 3 exakt integriert.

**Tangentensteigung (Anzeige zur unteren Kurve).** Zentrale Differenz auf derselben Summe:

```
var mS = (Isum(f, a, x + 0.02) - Isum(f, a, x - 0.02)) / 0.04;
```

Die Funktionen sind über `[0; 12]` hinaus definiert, das Überschreiten des Randes um 0,02 ist
unproblematisch.

*Genauigkeitsprüfung (gerechnet):*

| Rate | `x` | zentrale Differenz | `f(x)` | Abweichung |
|---|---|---|---|---|
| A | 4,0 | 4,999973 | 5,000000 | `2,7·10⁻⁵` |
| A | 10,5 | −3,450027 | −3,450000 | `2,7·10⁻⁵` |
| B | 4,0 | 0,000000 | 0,000000 | `6,7·10⁻¹⁴` |
| C | 7,0 | 0,489829 | 0,489826 | `2,9·10⁻⁶` |

Auf zwei Nachkommastellen — so wird angezeigt — sind beide Zahlen immer identisch. Genau das ist
die Aussage, die die Simulation transportieren soll.

### 4.4 Regler, Knöpfe, Anzeigen

**Regler (`<div class="regler">`):**

| `id` | Größe | von | bis | Schritt | Startwert | Anzeige |
|---|---|---|---|---|---|---|
| `rA` | untere Grenze `a` | 0 | 12 | 0,1 | 0,0 | eine Nachkommastelle, Einheit h |
| `rX` | obere Grenze `x` | 0 | 12 | 0,05 | 6,00 | zwei Nachkommastellen, Einheit h |

Umsetzung wie im Referenzmodul über ganzzahlige `range`-Werte (`rA`: 0…120, geteilt durch 10;
`rX`: 0…240, geteilt durch 20), damit `step` und Rundung sauber bleiben.

**Knopfleiste:** `Rate A` · `Rate B` · `Rate C` (aktive Rate hervorheben) ·
`▶ Abspielen / ❚❚ Pause` (lässt `x` mit `2,0 h` pro Sekunde von der aktuellen Stelle bis 12
laufen und stoppt dort) · `Zurücksetzen` (`a = 0`, `x = 6,00`, Rate A).
Checkbox `Tangente an I einblenden` (Vorgabe: an).

**Ziehen:** `pointerdown` / `pointermove` / `pointerup` auf dem Canvas mit `setPointerCapture`.
Ein Zeigen in die **obere** Hälfte setzt `x`, ein Zeigen mit gedrückter Umschalttaste oder in
die untere Hälfte setzt `a`. Umrechnung Pixel → Stunde siehe 4.5.

**Anzeigen (`<div class="anzeige">`), alle Zahlen mit `fmt()` und Komma:**

| Feld | Inhalt | Stellen |
|---|---|---|
| `a` | untere Grenze in h | 1 |
| `x` | obere Grenze in h | 2 |
| `f(x)` | Wert der Rate, **aus dem oberen Diagramm**, in m³/h | 2 |
| `I_a(x)` | Wert des Integrals, **aus der Streifensumme**, in m³ | 2 |
| Steigung von `I_a` bei `x` | zentrale Differenz, **aus dem unteren Diagramm**, in m³/h | 2 |
| Unterschied | Betrag der Differenz der beiden vorigen Felder | 3 |

Das letzte Feld steht immer auf `0,000`. Es ist Absicht, dass es da steht: Es ist der Hauptsatz
als laufende Messung.

### 4.5 Maßstäbe (als Konstanten oben in der IIFE dokumentieren)

- `t`-Achse: `t ∈ [0; 12]` auf die Pixel `70 … 970` ⟹ **75,0 px pro Stunde**,
  `tPx(t) = 70 + 75·t`, Umkehrung `pxT(p) = (p − 70)/75`.
- Oberes Diagramm: Zeichenfläche `y = 30 … 260` (230 px hoch).
- Unteres Diagramm: Zeichenfläche `y = 320 … 540` (220 px hoch).
- Wertebereiche und daraus folgende Maßstäbe (gerechnet):

| Rate | `f`-Achse | px je `m³/h` | `I`-Achse | px je `m³` |
|---|---|---|---|---|
| A | `−9,0 … 6,0` | 15,3333 | `−36,0 … 36,0` | 3,0556 |
| B | `−4,0 … 7,0` | 20,9091 | `−28,0 … 28,0` | 3,9286 |
| C | `−0,5 … 4,5` | 46,0000 | `−14,5 … 14,5` | 7,5862 |

*Begründung der Bereiche (gerechnet):* Auf `[0; 12]` gilt
Rate A: `f ∈ [−7,80; 5,00]`, `I_a(x) = F(x) − F(a) ∈ [−32,40; 32,40]`;
Rate B: `f ∈ [−3,20; 6,40]`, `I_a ∈ [−25,60; 25,60]`;
Rate C: `f ∈ [0,109; 4,00]`, `I_a ∈ [−12,97; 12,97]`.
Jeder gewählte Achsenbereich umschließt den zugehörigen Wertebereich mit Rand.

### 4.6 Beobachtungsauftrag (`<div class="auftrag">`)

> **Beobachtungsauftrag**
> Stelle **Rate B** ein und setze `a = 0,0`. Drück auf „Abspielen" und schau **nur auf das untere
> Diagramm**: Bei welchem `x` ist die Kurve am tiefsten? Halte dort an und lies im **oberen**
> Diagramm ab, welchen Wert `f` an dieser Stelle hat.
> Wiederhole das mit **Rate A**, diesmal auf der Suche nach dem **höchsten** Punkt der unteren
> Kurve, und notiere wieder die Stelle samt zugehörigem `f`-Wert.
> Formuliere aus beiden Beobachtungen einen Satz, der beschreibt, woran man **allein im oberen
> Diagramm** erkennt, wo die untere Kurve einen Extrempunkt hat.
> Prüfe deinen Satz zum Schluss an **Rate C**: Was sagt er dort voraus — und stimmt es?

Erwartetes Ergebnis (für die Lehrkraft, nicht auf der Seite): Rate B hat den Tiefpunkt bei
`x = 4,00` mit `I₀(4) = −6,40 m³` und `f(4) = 0,00`; Rate A hat den Hochpunkt bei `x = 9,00` mit
`I₀(9) = 32,40 m³` und `f(9) = 0,00`. Der Satz lautet sinngemäß: *Die untere Kurve hat dort einen
Extrempunkt, wo die obere eine Nullstelle mit Vorzeichenwechsel hat; bei `− → +` einen Tiefpunkt,
bei `+ → −` einen Hochpunkt.* Rate C hat keine Nullstelle (`f(t) = 4e^(−0,3t) > 0` für alle `t`),
also sagt der Satz vorher: kein Extrempunkt im Inneren, `I` steigt durchgehend. Genau das zeigt
die Simulation — die Kurve steigt von 0,00 auf 12,97 m³ und wird dabei immer flacher.

### 4.7 Verständnisfragen zur Simulation (zwei Multiple-Choice-Aufgaben)

**sim1** — Schlüssel `sim1`, Radio-Name `sim1`, richtige Option: **Index 1**,
`<span class="ab">Anforderungsbereich II</span>`

> Frage: Stell **Rate B** und `a = 2,0` ein und fahre `x` von 0 bis 12. Bei welchen Werten von `x`
> zeigt das Feld „Integral“ genau `0,00 m³`?
>
> - `data-i="0"`: Nur bei `x = 2,00`, denn dort beginnt die Integration.
> - `data-i="1"`: Bei `x = 2,00` und noch einmal bei `x = 6,00`.
> - `data-i="2"`: Bei `x = 2,00` und bei `x = 4,00`, denn dort hat die Rate ihre Nullstelle.

Feedback:

- **Index 0:** Bei x = 2,00 steht die Anzeige auf 0,00 m³ – das ist die Definition Iₐ(a) = 0. Aber die Kurve läuft danach nicht ewig in eine Richtung: Bei x = 4,00 zeigt sie I₂(4,00) = −1,60 m³, also nicht null. Nach der Nullstelle der Rate steigt sie wieder und kreuzt die Achse ein zweites Mal.
- **Index 1 (richtig):** Richtig. Von x = 2 bis 4 fließt netto Wasser ab (f < 0), die Kurve fällt bis I₂(4,00) = −1,60 m³. Danach ist f > 0, die Kurve steigt und erreicht bei x = 6,00 wieder I₂(6,00) = 0,00 m³: Die Fläche von 4 bis 6 gleicht die Fläche von 2 bis 4 exakt aus. Bei x = 0 steht übrigens +4,80 m³, weil dort x < a gilt.
- **Index 2:** Die Rate hat bei x = 4,00 ihre Nullstelle, aber das heißt nur, dass die Steigung der unteren Kurve dort null ist – ihr Tiefpunkt. Die Anzeige liefert I₂(4,00) = −1,60 m³. Der Wert des Integrals ist null, wenn sich Flächenanteile aufheben, nicht dort, wo f null ist.

**sim2** — Schlüssel `sim2`, Radio-Name `sim2`, richtige Option: **Index 1**,
`<span class="ab">Anforderungsbereich II</span>`

> Frage: Stell **Rate C** und `a = 0,0` ein und fahre `x` bis `x = 12,00`. Lies dort das Integral
> (`12,97 m³`) und die Steigung (`0,11 m³/h`) ab. Wie deutest du diese beiden Zahlen?
>
> - `data-i="0"`: Die Steigung ist fast null, also ist `12,97 m³` der Endwert und die Kurve
>   verläuft ab hier waagerecht.
> - `data-i="1"`: Die Steigung ist noch positiv, also wächst der Bestand weiter und nähert sich
>   `40/3 ≈ 13,33 m³`, ohne ihn je zu erreichen.
> - `data-i="2"`: Die Steigung ist klein geworden, also hat die Kurve ihren Hochpunkt
>   überschritten und der Bestand nimmt danach wieder ab.

Feedback:

- **Index 0:** Fast null ist nicht null: Die Anzeige zeigt bei x = 12,00 noch 0,11 m³/h, und die Exponentialfunktion 4·e^(−0,3·x) wird nie null. Die Kurve flacht ab, steigt aber weiter. 12,97 m³ ist deshalb noch nicht der Endwert, sondern eine Zwischenstation auf dem Weg zu 40/3 ≈ 13,33 m³.
- **Index 1 (richtig):** Richtig. Die Steigung der unteren Kurve ist f(x), und die bleibt positiv, wird aber klein: bei x = 12,00 nur noch 0,11 m³/h. Der Bestand ist dort auf 12,97 m³ gewachsen und nähert sich dem Wert 40/3 ≈ 13,33 m³, den er nie ganz erreicht.
- **Index 2:** Eine kleine Steigung ist keine negative. Die Kurve fällt nur, wo f negativ ist, und Rate C ist überall positiv (kleinster Wert 0,11 m³/h). Eine sinkende Rate heißt: Der Zuwachs wird kleiner, der Bestand wächst trotzdem weiter. Einen Hochpunkt gibt es nicht.

---

## Abschnitt 5 — Übungen

`<section id="uebungen">`, `.stufe`-Nummer **5**, Überschrift **Übungen**.
Sieben Aufgaben, verteilt über die Anforderungsbereiche I bis III.

### a1 — Anforderungsbereich I · Zahleneingabe · Schlüssel `a1`

**Aufgabentext.** Berechne `∫₁³ (3x² − 4x + 5) dx`. Gib das Ergebnis in Flächeneinheiten (FE)
an.

**Einheitenauswahl:** `FE` · `LE` · `FE²` · `m³` (die letzten drei sind Distraktoren).

**Daten:** `wert: 20`, `einheit: "FE"`, `tol: 0.05`, keine Alternativeinheit.

**Hilfe 1 (Tipp).** Du brauchst hier keine Streifen mehr. Gesucht ist eine Funktion, deren
Ableitung der Integrand ist — und die findest du summandenweise.

**Hilfe 2 (Ansatz).** Eine Stammfunktion ist `F(x) = x³ − 2x² + 5x`. Kontrolliere sie durch
Ableiten, bevor du weiterrechnest. Danach liefert Teil 2 des Hauptsatzes
`∫₁³ f(x) dx = F(3) − F(1)`.

**Hilfe 3 (Lösungsweg).** Probe: `F′(x) = 3x² − 4x + 5` ✓.
`F(3) = 27 − 2·9 + 15 = 27 − 18 + 15 = 24`.
`F(1) = 1 − 2 + 5 = 4`.
`∫₁³ (3x² − 4x + 5) dx = 24 − 4 = 20 FE`.
*Numerische Gegenprobe (200 000 Streifen): `19,99999999995`.*

**Rückmeldungen:**

- `ok`: Richtig. `F(x) = x³ − 2x² + 5x` mit `F(3) = 24` und `F(1) = 4`, Differenz 20 FE.
- `falschEinheit`: Der Zahlenwert stimmt. Ein bestimmtes Integral über eine einheitenlose
  Funktion ist ein orientierter Flächeninhalt und wird in Flächeneinheiten (FE) angegeben.
  Längeneinheiten trügen die Achsen, nicht das Produkt aus beiden.
- `nah`: Dicht dran, aber ein Schritt fehlt. 24 bekommt, wer nur `F(3)` einsetzt und `F(1) = 4`
  vergisst — die untere Grenze wird immer abgezogen. 28 entsteht beim Addieren statt Subtrahieren.
  16 ist `f(3) − f(1)`, also die Differenz der Integrandwerte: Damit hättest du abgeleitet
  gedacht statt integriert.
- `weit`: 10 bekommt man mit `F(x) = x³ − 2x² + 5`. Aus der Konstanten 5 wird beim
  Rückwärtsableiten `5x`, nicht wieder 5 — leite deine Stammfunktion zur Probe ab, es muss genau
  `3x² − 4x + 5` herauskommen. Die Hilfen führen dich Schritt für Schritt.

### a2 — Anforderungsbereich II · Zahleneingabe · Schlüssel `a2`

**Aufgabentext.** Der Zufluss in ein Regenrückhaltebecken wird durch
`f(t) = −0,2t² + 1,6t + 1,8` beschrieben (`f` in m³/h, `t` in h) — dieselbe Rate wie in der
letzten Einheit. Berechne mit dem Hauptsatz, wie viel Wasser zwischen `t = 2 h` und `t = 7 h`
zufließt. Runde auf zwei Nachkommastellen.

**Einheitenauswahl:** `m³` · `L` · `m³/h` · `kWh`.

**Daten:** `wert: 22.67`, `einheit: "m³"`, `tol: 0.05`, `alt: {wert: 22670, einheit: "L"}`
(daraus abgeleitete Toleranz 50 L; der exakte Wert 22 666,7 L liegt darin).

**Hilfe 1 (Tipp).** Streifen brauchst du nicht mehr. Suche eine Funktion, deren Ableitung die
Rate ist, und setze zwei Werte ein. Achte auf die Grenzen — gefragt ist nicht der Zufluss ab
Beginn.

**Hilfe 2 (Ansatz).** `F(t) = −t³/15 + 0,8t² + 1,8t`. Probe durch Ableiten:
`F′(t) = −3t²/15 + 1,6t + 1,8 = −0,2t² + 1,6t + 1,8` ✓. Der gesuchte Zufluss ist
`∫₂⁷ f(t) dt = F(7) − F(2)`.

**Hilfe 3 (Lösungsweg).**
`F(7) = −343/15 + 0,8·49 + 1,8·7 = −22,8667 + 39,20 + 12,60 = 28,9333 m³` (exakt `434/15`).
`F(2) = −8/15 + 0,8·4 + 1,8·2 = −0,5333 + 3,20 + 3,60 = 6,2667 m³` (exakt `94/15`).
`∫₂⁷ f dt = 434/15 − 94/15 = 340/15 = 68/3 = 22,6667 m³ ≈ 22,67 m³`.
*Plausibilitätsprobe:* Die mittlere Rate wäre `22,6667 / 5 = 4,53 m³/h` und liegt damit zwischen
`f(7) = 3,20 m³/h` und dem Maximum `f(4) = 5,00 m³/h` — passt.
*Numerische Gegenprobe (400 000 Streifen): `22,66666667`.*

**Rückmeldungen:**

- `ok`: Richtig. `F(t) = −t³/15 + 0,8t² + 1,8t`, `F(7) = 434/15 = 28,93 m³`,
  `F(2) = 94/15 = 6,27 m³`, Differenz `68/3 ≈ 22,67 m³` (rund 22 670 L).
- `falschEinheit`: Der Zahlenwert stimmt. m³/h mal h ergibt m³ — das Integral über eine Rate ist
  eine Menge, keine Rate. In Litern wären es rund 22 670 L.
- `nah`: 18,50 m³ bekommt, wer den Mittelwert der Randraten `(4,20 + 3,20)/2 = 3,70 m³/h` mit den
  5 Stunden multipliziert. Das ist die Trapezformel mit einem einzigen Streifen; sie unterschätzt
  hier, weil der Graph zwischen `t = 2` und `t = 7` rechtsgekrümmt ist. 28,93 m³ ist `F(7)`
  allein — dann hast du ab `t = 0` gerechnet statt ab `t = 2`.
- `weit`: Steht bei dir etwa `−1,0`, hast du `f(7) − f(2) = 3,20 − 4,20` gerechnet, also die
  Änderung der **Rate** statt des Zuflusses. Der Hauptsatz verlangt die Differenz der Werte
  einer **Stammfunktion**, nicht der Funktionswerte selbst. Die Hilfen zeigen dir die
  Stammfunktion.

### a3 — Anforderungsbereich II · Zuordnung · Schlüssel `a3`

> **Wichtig für den Bauagenten:** Die Zuordnungs-Engine des Referenzmoduls schreibt fest in
> `ergebnisse.a3`. Der Schlüssel dieser Aufgabe muss deshalb `a3` heißen, sonst taucht sie im
> Export nicht auf.

**Aufgabentext.** Die vier Diagramme A bis D zeigen jeweils den Graphen einer Rate `f` auf dem
Intervall `[0; 6]`. Ordne jeder Aussage über die zugehörige Integralfunktion
`I₀(x) = ∫₀ˣ f(t) dt` das passende Diagramm zu.

**Die vier Diagramme (Inline-SVG, `viewBox="0 0 160 90"`, Graph `stroke="#0d7a52"
stroke-width="2.5" fill="none"`).**
Achsen: `x`-Achse `line x1="12" y1="52.5" x2="156" y2="52.5"`, `y`-Achse
`line x1="18" y1="6" x2="18" y2="84"`, beide `stroke="#94a3b8"`.
Abbildung: `x ∈ [0; 6] → px = 18 + 22·x`, `f ∈ [−4; 7] → py = 78 − (70/11)·(f + 4)`.

| Diagramm | Rate | `polyline points` | `f`-Werte bei `x = 0 … 6` |
|---|---|---|---|
| **A** | `f(x) = 6 − 0,8x` | `18.0,14.4 150.0,44.9` | 6,00 · 5,20 · 4,40 · 3,60 · 2,80 · 2,00 · 1,20 |
| **B** | `f(x) = 0,8x − 3,2` | `18.0,72.9 150.0,42.4` | −3,20 · −2,40 · −1,60 · −0,80 · 0,00 · 0,80 · 1,60 |
| **C** | `f(x) = −2` | `18.0,65.3 150.0,65.3` | durchgehend −2,00 |
| **D** | `f(x) = −x²/3 + 2x` | `18.0,52.5 29.0,46.7 40.0,41.9 51.0,38.2 62.0,35.6 73.0,34.0 84.0,33.5 95.0,34.0 106.0,35.6 117.0,38.2 128.0,41.9 139.0,46.7 150.0,52.5` | 0,00 · 1,67 · 2,67 · 3,00 · 2,67 · 1,67 · 0,00 |

**Die vier Zeilen (`data-loesung` in dieser Reihenfolge: C, D, B, A — bewusst nicht A, B, C, D):**

| Reihenfolge | Aussage über `I₀` | `data-loesung` |
|---|---|---|
| 1 | `I₀` ist eine fallende Gerade durch den Ursprung. | `C` |
| 2 | `I₀` steigt auf dem ganzen Intervall; ihre Steigung ist bei `x = 3` am größten. | `D` |
| 3 | `I₀` fällt zuerst, hat bei `x = 4` einen Tiefpunkt und steigt danach wieder. | `B` |
| 4 | `I₀` steigt auf dem ganzen Intervall, wird dabei aber immer flacher. | `A` |

**Kontrollrechnungen zu den vier Integralfunktionen** (jeweils analytisch und numerisch mit
200 000 Streifen geprüft, Abweichung `< 10⁻⁶`):

- **A:** `I₀(x) = 6x − 0,4x²`. Werte bei `x = 0 … 6`: 0,00 · 5,60 · 10,40 · 14,40 · 17,60 ·
  20,00 · 21,60. Steigung `f` fällt von 6,00 auf 1,20 ⟹ steigend und rechtsgekrümmt.
- **B:** `I₀(x) = 0,4x² − 3,2x`. Werte: 0,00 · −2,80 · −4,80 · −6,00 · −6,40 · −6,00 · −4,80.
  Tiefpunkt bei `x = 4` mit `I₀(4) = −6,40`, denn `f(4) = 0` mit VZW `− → +`.
- **C:** `I₀(x) = −2x`. Werte: 0,00 · −2,00 · −4,00 · −6,00 · −8,00 · −10,00 · −12,00. Konstante
  Rate ⟹ Gerade; `I₀(0) = 0` wie bei jeder Integralfunktion.
- **D:** `I₀(x) = −x³/9 + x²`. Werte: 0,00 · 0,89 · 3,11 · 6,00 · 8,89 · 11,11 · 12,00.
  `I₀″(x) = f′(x) = −2x/3 + 2 = 0` ⟺ `x = 3` mit VZW `+ → −` ⟹ Wendestelle, größte Steigung
  `f(3) = 3,00`.

**Rückmeldung bei voller Punktzahl.** Alle vier richtig. Entscheidend war jedes Mal, dass `f`
die **Ableitung** von `I₀` ist: Das Vorzeichen von `f` gibt die Monotonie, die Nullstelle mit
Vorzeichenwechsel den Extrempunkt, und der Hochpunkt von `f` die Stelle größter Steigung, also
die Wendestelle.

**Rückmeldung bei Teilerfolg** (nennt die Strategie, nicht die Lösung). Geh jede Aussage in
derselben Reihenfolge durch: erstens Vorzeichen von `f` — steigt oder fällt `I₀`? Zweitens
Nullstellen von `f` mit Vorzeichenwechsel — wo hat `I₀` einen Extrempunkt? Drittens Extremstellen
von `f` — wo ist `I₀` am steilsten? Wer über die Fläche nachdenkt, kommt langsamer ans Ziel als
wer `f` als erste Ableitung liest.

### a4 — Anforderungsbereich II · Zahleneingabe · Schlüssel `a4`

**Aufgabentext.** Aus einem Behälter läuft Wasser mit der Rate `f(t) = 4·e^(−0,3t)` (`f` in
L/min, `t` in min). Berechne, wie viel Wasser in den ersten 5 Minuten ausläuft. Runde auf zwei
Nachkommastellen.

**Einheitenauswahl:** `L` · `m³` · `L/min` · `min`.

**Daten:** `wert: 10.36`, `einheit: "L"`, `tol: 0.05`, `alt: {wert: 0.01036, einheit: "m³"}`
(abgeleitete Toleranz `0,00005 m³`; der exakte Wert `0,01035826 m³` liegt darin).

**Hilfe 1 (Tipp).** Beim Ableiten einer `e`-Funktion mit linearem Exponenten kommt die innere
Ableitung als Faktor dazu. Beim Rückwärtsgehen musst du diesen Faktor also wieder loswerden.

**Hilfe 2 (Ansatz).** Lineare Substitution: Zu `f(t) = 4·e^(−0,3t)` gehört
`F(t) = 4·e^(−0,3t)/(−0,3) = −(40/3)·e^(−0,3t)`. Kontrolliere durch Ableiten. Danach
`∫₀⁵ f(t) dt = F(5) − F(0)`.

**Hilfe 3 (Lösungsweg).**
Probe: `F′(t) = −(40/3)·(−0,3)·e^(−0,3t) = 4·e^(−0,3t)` ✓.
`F(5) = −(40/3)·e^(−1,5) = −13,33333 · 0,2231302 = −2,97507`.
`F(0) = −(40/3)·e^0 = −13,33333`.
`∫₀⁵ f dt = −2,97507 − (−13,33333) = 10,35826 ≈ 10,36 L`.
Kurzform: `I₀(x) = (40/3)·(1 − e^(−0,3x))`, also `I₀(5) = 13,33333 · 0,7768698 = 10,35826`.
*Numerische Gegenprobe (200 000 Streifen): `10,358264531`.*
*Nebenbei:* Für `x → ∞` strebt `I₀(x)` gegen `40/3 = 13,33 L` — mehr als 13,33 L können aus dem
Behälter nie auslaufen, egal wie lange man wartet.

**Rückmeldungen:**

- `ok`: Richtig. `F(t) = −(40/3)·e^(−0,3t)`, also
  `∫₀⁵ f dt = (40/3)·(1 − e^(−1,5)) = 13,3333 · 0,77687 = 10,36 L`.
- `falschEinheit`: Der Zahlenwert stimmt. L/min mal min ergibt Liter — herausgekommen ist eine
  Menge, keine Rate und keine Zeit. In Kubikmetern wären es 0,01036 m³.
- `nah`: 13,33 L ist der Grenzwert für unendlich lange Zeit, nicht der Wert nach 5 Minuten; dann
  hast du `e^(−1,5)` wie null behandelt, es ist aber 0,2231. 20,00 L bekommt, wer die
  Anfangsrate `f(0) = 4 L/min` mit 5 min multipliziert — die Rate fällt jedoch, also muss weniger
  herauskommen.
- `weit`: Steht bei dir etwa `−3,11`, fehlt der Faktor `1/(−0,3)`; du hast mit
  `F(t) = 4·e^(−0,3t)` gerechnet. Leite das zur Probe ab: Wegen der Kettenregel kommt
  `−1,2·e^(−0,3t)` heraus, nicht die Rate. 4,46 L wäre `f(5)·5`, also die Rate **am Ende** mal
  die Zeit — das unterschätzt, weil die Rate vorher größer war.

### a5 — Anforderungsbereich II · Zahleneingabe · Schlüssel `a5`

**Aufgabentext.** Dasselbe Rückhaltebecken wie in Aufgabe 2 mit der Zuflussrate
`f(t) = −0,2t² + 1,6t + 1,8` (m³/h). Zum Zeitpunkt `t = 0` enthält es bereits `8,5 m³`. Bestimme
den größten Wasserbestand, den das Becken im Zeitraum `0 ≤ t ≤ 12` erreicht.

**Einheitenauswahl:** `m³` · `L` · `m³/h` · `h`.

**Daten:** `wert: 40.9`, `einheit: "m³"`, `tol: 0.05`, `alt: {wert: 40900, einheit: "L"}`.

**Hilfe 1 (Tipp).** Der Bestand ist dann am größten, wenn er aufhört zu wachsen und anfängt zu
fallen. Was macht die Zuflussrate genau in diesem Moment? Und: Wie viel war zu Beginn schon da?

**Hilfe 2 (Ansatz).** Die Bestandsfunktion ist `V(t) = 8,5 + ∫₀ᵗ f(u) du`, ausgerechnet
`V(t) = 8,5 − t³/15 + 0,8t² + 1,8t`. Nach dem Hauptsatz gilt `V′(t) = f(t)`. Setze also
`f(t) = 0`, prüfe den Vorzeichenwechsel und vergleiche den gefundenen Wert am Ende mit den
Randwerten `V(0)` und `V(12)`.

**Hilfe 3 (Lösungsweg).**
`−0,2t² + 1,6t + 1,8 = 0 | : (−0,2)` ⟹ `t² − 8t − 9 = 0` ⟹
`t = (8 ± √(64 + 36))/2 = (8 ± 10)/2`, also `t₁ = 9` und `t₂ = −1` (entfällt).
Vorzeichenwechsel: `f(8) = −12,8 + 12,8 + 1,8 = +1,80`, `f(10) = −20 + 16 + 1,8 = −2,20`, also
`+ → −` und damit ein Hochpunkt von `V`.
`V(9) = 8,5 + (−729/15 + 0,8·81 + 1,8·9) = 8,5 + (−48,60 + 64,80 + 16,20) = 8,5 + 32,40 = 40,90 m³`.
Randvergleich: `V(0) = 8,50 m³` und `V(12) = 8,5 + 21,60 = 30,10 m³` — beide kleiner.
Der größte Bestand ist also **40,90 m³**.

**Rückmeldungen:**

- `ok`: Richtig. `V′(t) = f(t) = 0` liefert `t = 9 h` mit Vorzeichenwechsel `+ → −`;
  `V(9) = 8,50 m³ + 32,40 m³ = 40,90 m³`, und die Randwerte 8,50 m³ und 30,10 m³ sind kleiner.
- `falschEinheit`: Der Zahlenwert stimmt. Gefragt ist ein Bestand, also ein Volumen in m³ (oder
  40 900 L) — nicht der Zeitpunkt in Stunden und auch keine Rate in m³/h.
- `nah`: 32,40 m³ ist der **Zuwachs** von 0 h bis 9 h; der Anfangsbestand von 8,50 m³ fehlt.
  30,10 m³ wäre der Bestand am rechten Rand bei `t = 12 h` — zwischendurch war mehr Wasser im
  Becken. 24,23 m³ ergibt sich für `t = 4 h`, also am Hochpunkt der **Rate**: Dort fließt am
  schnellsten zu, das Becken ist aber noch nicht am vollsten.
- `weit`: Prüf zuerst, welche Größe du überhaupt bestimmst. Gesucht ist der maximale **Wert** von
  `V`, nicht der Zeitpunkt (9 h) und nicht der maximale Zufluss (5,00 m³/h). Und `V` ist nicht
  das Integral allein: `V(t) = 8,5 + ∫₀ᵗ f` — der Anfangsbestand steht im Text, nicht im Graphen.

### a6 — Anforderungsbereich III · offene Begründungsaufgabe · Schlüssel `a6`

**Aufgabentext.** Lena schreibt in ihr Heft: *„Wenn eine Funktion `f` auf einem Intervall
durchgehend negativ ist, dann ist dort auch jede Stammfunktion `F` von `f` negativ."* Nimm zu
dieser Aussage begründet Stellung. Geh dabei auch darauf ein, warum Lenas Behauptung für die
**Integralfunktion** `I_a` rechts von `a` trotzdem zutrifft.

Baustein: `<textarea>` + `<button data-loesung="a6">Musterlösung anzeigen</button>` +
`<div class="hilfe-text" data-stufe="9">`.

**Erwartete Argumentation (Musterlösung).**

Die Aussage ist **falsch**; ein Gegenbeispiel genügt. Betrachte `f(t) = −1` auf `[0; 10]` — ein
Becken, aus dem gleichmäßig mit 1 m³/h abläuft. Die Funktion `F(t) = 100 − t` ist eine
Stammfunktion, denn `F′(t) = −1 = f(t)`. Sie ist auf `[0; 10]` durchgehend **positiv**:
`F(0) = 100`, `F(2) = 98`, `F(5) = 95`, `F(10) = 90`. Damit ist Lenas Behauptung widerlegt.

Warum sie im Allgemeinen scheitert: `f = F′` steuert die **Steigung** von `F`, nicht die Höhe.
Aus `f < 0` folgt über das Monotoniekriterium nur, dass `F` streng monoton **fällt**. Wo `F`
dabei verläuft, hängt vom Anfangswert ab — und den legt erst die Integrationskonstante fest. Zu
jeder Stammfunktion `F` ist auch `F + C` eine, man kann den Graphen also beliebig weit nach oben
schieben, ohne dass sich an `f` das Geringste ändert.

Warum die Behauptung für die Integralfunktion doch gilt: `I_a` ist unter allen Stammfunktionen
diejenige mit `I_a(a) = 0`. Für `x > a` ist `I_a(x) = ∫ₐˣ f(t) dt`, und weil `f` auf `[a; x]`
negativ ist, sind alle Produktsummen negativ, also auch ihr Grenzwert. Die Integralfunktion
startet zwingend bei null und kann von dort nur nach unten. Für `x < a` dreht sich das Vorzeichen
um: Dann ist `I_a(x) = −∫ₓᵃ f(t) dt > 0`. Im Gegenbeispiel:
`I₀(x) = F(x) − F(0) = (100 − x) − 100 = −x`, also `I₀(10) = −10 < 0` ✓ und `I₀(−3) = 3 > 0`.

**Bewertungskriterien.** Aussage klar als falsch gekennzeichnet · konkretes Gegenbeispiel mit
Nachweis `F′ = f` · Unterscheidung zwischen Steigung und Höhe bzw. ausdrücklicher Bezug auf das
Monotoniekriterium · Rolle der Integrationskonstanten benannt · Sonderstellung der
Integralfunktion über `I_a(a) = 0` begründet · Hinweis auf die Umkehrung des Vorzeichens für
`x < a`.

### a7 — Anforderungsbereich III · offene Begründungsaufgabe · Schlüssel `a7`

**Aufgabentext.** Gegeben ist `f(x) = eˣ`.
**a)** Zeige, dass `F₁(x) = eˣ − 1` eine Integralfunktion von `f` ist, und gib die zugehörige
untere Grenze an.
**b)** Begründe, dass `F₂(x) = eˣ + 1` zwar eine Stammfunktion, aber **keine** Integralfunktion
von `f` ist.
**c)** Formuliere ein allgemeines Kriterium dafür, wann eine Stammfunktion einer stetigen
Funktion eine Integralfunktion ist, und begründe es in beiden Richtungen.

Baustein: `<textarea>` + `<button data-loesung="a7">Musterlösung anzeigen</button>` +
`<div class="hilfe-text" data-stufe="9">`.

**Erwartete Argumentation (Musterlösung).**

**a)** Eine Stammfunktion von `eˣ` ist `eˣ` selbst. Nach Teil 2 des Hauptsatzes gilt
`∫₀ˣ e^t dt = [e^t]₀ˣ = eˣ − e⁰ = eˣ − 1 = F₁(x)`. Also ist `F₁` die Integralfunktion von `f`
zur unteren Grenze **`a = 0`**. Kontrolle: `F₁(0) = e⁰ − 1 = 0` ✓, wie es für jede
Integralfunktion an ihrer unteren Grenze sein muss. *(Numerische Gegenprobe: `∫₀² e^t dt =
6,389056099`, und `F₁(2) = e² − 1 = 6,389056099`.)*

**b)** `F₂′(x) = eˣ = f(x)`, also ist `F₂` eine Stammfunktion. Wäre `F₂` zusätzlich eine
Integralfunktion, gäbe es ein `a` mit `eˣ + 1 = ∫ₐˣ e^t dt = eˣ − e^a` für alle `x`. Subtraktion
von `eˣ` liefert `1 = −e^a`, also `e^a = −1`. Die Exponentialfunktion nimmt aber nur positive
Werte an; die Gleichung ist unlösbar. Folglich ist `F₂` keine Integralfunktion von `f`.
Anschaulich: `F₂(x) = eˣ + 1 > 1 > 0` für alle `x` — der Graph hat keine Nullstelle, eine
Integralfunktion muss aber an ihrer unteren Grenze eine haben.

**c)** **Kriterium:** Eine Stammfunktion `F` von `f` auf einem Intervall `I` ist genau dann eine
Integralfunktion von `f`, wenn `F` in `I` mindestens eine Nullstelle besitzt.

*„⟸":* Sei `F(a) = 0` für ein `a ∈ I`. Nach Teil 1 des Hauptsatzes ist `I_a` ebenfalls eine
Stammfunktion von `f` auf `I`. Nach dem Satz über die Eindeutigkeit bis auf eine Konstante gibt
es ein `C` mit `F = I_a + C`. Einsetzen von `a`: `0 = F(a) = I_a(a) + C = 0 + C`, also `C = 0`
und damit `F = I_a`.
*„⟹":* Ist `F = I_a` für ein `a ∈ I`, so ist `F(a) = ∫ₐᵃ f(t) dt = 0`, also hat `F` eine
Nullstelle.

*Ergänzung zum Beispiel:* Für `f(x) = eˣ` sind die Stammfunktionen genau die Funktionen
`eˣ + c`. Sie sind genau dann Integralfunktionen, wenn `c < 0` ist, denn dann hat `eˣ + c = 0`
die Lösung `a = ln(−c)`. Für `c = −0,5` etwa ist `a = ln 0,5 = −0,6931`; Probe:
`e^(−0,6931) = 0,5000 = −c` ✓. Für `c ≥ 0` gibt es kein solches `a`.

**Bewertungskriterien.** a) korrekte Anwendung von Teil 2 des Hauptsatzes und Angabe `a = 0` ·
b) Nachweis `F₂′ = f` **und** Widerspruchsargument über `e^a = −1` (alternativ über die fehlende
Nullstelle) · c) Kriterium korrekt als „genau dann, wenn" formuliert · beide Beweisrichtungen
ausgeführt · Verwendung des Satzes über die Eindeutigkeit bis auf eine Konstante ·
saubere Trennung zwischen dem Begriff Stammfunktion (Eigenschaft `F′ = f`) und dem Begriff
Integralfunktion (Darstellung als Integral mit fester unterer Grenze).

---

## Abschnitt 6 — Abschluss

`<section id="abschluss">`, `.stufe`-Nummer **6**,
Überschrift **Zusammenfassung und Selbstcheck**.

### 6.1 Vier Kernaussagen (je ein `<div class="merksatz">`)

**Kernaussage 1 — Integrieren und Ableiten sind Hin- und Rückweg.**
Für stetiges `f` ist die Integralfunktion `I_a(x) = ∫ₐˣ f(t) dt` differenzierbar mit
`I_a′(x) = f(x)`. Wer eine Rate aufsummiert und vom Ergebnis wieder die Änderungsrate bildet,
landet bei der Rate, mit der er begonnen hat. Der Beweis steckt in einem einzigen Streifen:
`m(h)·h ≤ ∫ₓ^(x+h) f ≤ M(h)·h`, geteilt durch `h`, und die Stetigkeit schließt die Zange.

**Kernaussage 2 — `f` ist die Ableitung von `I`, also gelten alle Regeln der Kurvendiskussion.**
`f > 0` heißt: `I` steigt. `f < 0` heißt: `I` fällt — **nicht**, dass `I` negativ wird.
Eine Nullstelle von `f` mit Vorzeichenwechsel ergibt einen Extrempunkt von `I`, ein Extrempunkt
von `f` eine Wendestelle von `I`. Alles rutscht um eine Ableitungsstufe nach oben.

**Kernaussage 3 — Die Stammfunktion ist nur bis auf eine Konstante bestimmt.**
Auf einem Intervall unterscheiden sich je zwei Stammfunktionen derselben Funktion nur um ein
`+ C`; der Beweis läuft über `D′ = 0` und den Mittelwertsatz. Auf einem Definitionsbereich, der
in mehrere Intervalle zerfällt, gilt das nicht mehr — dort darf auf jedem Stück eine andere
Konstante stehen.

**Kernaussage 4 — Der Hauptsatz ersetzt einen Grenzwert durch zwei Funktionswerte.**
`∫ₐᵇ f(x) dx = F(b) − F(a)` für **irgendeine** Stammfunktion `F`, denn die Konstante kürzt sich
in der Differenz heraus. Statt 320 Streifen genügen zwei Einsetzungen. Vorausgesetzt wird dabei
die Stetigkeit von `f` auf dem ganzen Intervall — nicht jedes Integral löst sich so, aber jedes,
dessen Integrand eine hinschreibbare Stammfunktion hat.

### 6.2 Blick aufs Zentralabitur (`<div class="hinweis">`)

**Im Zentralabitur.** Der Hauptsatz ist kein eigenes Aufgabenthema, sondern das Werkzeug, mit
dem fast jede Analysis-Aufgabe der Q1 gerechnet wird. Diese Gestalten begegnen dir regelmäßig:

- **Bestimmtes Integral berechnen**, meist als Teilaufgabe im Anforderungsbereich I. Die
  Stammfunktion wird verlangt, und es lohnt sich, sie vor dem Einsetzen einmal abzuleiten — der
  Vorzeichenfehler bei `e^(kx)` und der vergessene Faktor `1/k` sind die zwei häufigsten
  Fehlerquellen.
- **Graphenzuordnung `f` ↔ `F`.** Gegeben sind mehrere Graphen, zugeordnet werden soll, welcher
  die Stammfunktion welches anderen ist. Argumentiert wird über Nullstellen mit
  Vorzeichenwechsel (Extremstellen der Stammfunktion) und über Extremstellen (Wendestellen der
  Stammfunktion) — nie über „sieht ähnlich aus".
- **Sachkontext mit Anfangsbestand.** Eine Rate ist gegeben, gefragt ist ein Bestand. Der
  Anfangswert steht im Text, nicht im Graphen; das Integral liefert nur die Änderung.
- **Steckbriefaufgaben zur Stammfunktion**: „Bestimme die Stammfunktion `F` von `f` mit
  `F(2) = 5`." Gemeint ist: allgemeine Stammfunktion aufstellen, Bedingung einsetzen, `C`
  bestimmen.
- **Begründungsaufgaben im LK**: Warum darf man irgendeine Stammfunktion nehmen? Warum ist eine
  Integralfunktion immer eine Stammfunktion, aber nicht umgekehrt? Warum braucht der Satz die
  Stetigkeit? Genau solche Fragen hast du in den Aufgaben a6 und a7 geübt.
- **Anschlussthema** ist die Fläche zwischen zwei Graphen. Dort wird zusätzlich an den
  Schnittstellen zerlegt und mit Beträgen gearbeitet — der Hauptsatz selbst bleibt derselbe.

### 6.3 Selbstcheck (`.karte` mit `<h3>Selbstcheck</h3>`, sechs `.check`-Zeilen)

Vorspann: *Hak ehrlich ab. Was du hier nicht ankreuzen kannst, holst du besser jetzt nach als in
der Klausur.*

1. Ich kann die Integralfunktion `I_a(x) = ∫ₐˣ f(t) dt` definieren, erklären, warum die
   Integrationsvariable anders heißen muss als die obere Grenze, und begründen, warum stets
   `I_a(a) = 0` gilt.
2. Ich kann den Hauptsatz in beiden Teilen formulieren und die Aussage `I_a′ = f` über die
   Einschachtelung eines einzelnen Streifens begründen, einschließlich der Stelle, an der die
   Stetigkeit von `f` gebraucht wird.
3. Ich kann zu einer gegebenen Funktion eine Stammfunktion angeben — auch bei `e^(kx)` und
   linearer Substitution — und meine Stammfunktion durch Ableiten selbst überprüfen.
4. Ich kann bestimmte Integrale mit `∫ₐᵇ f = F(b) − F(a)` berechnen und begründen, warum dabei
   jede beliebige Stammfunktion zum selben Ergebnis führt.
5. Ich kann aus dem Graphen einer Funktion `f` auf Monotonie, Extrem- und Wendestellen ihrer
   Integralfunktion schließen und dabei sicher zwischen dem Vorzeichen von `f` und dem Vorzeichen
   von `I` unterscheiden.
6. Ich kann in einem Sachzusammenhang aus einer Änderungsrate und einem Anfangswert die
   Bestandsfunktion aufstellen, ihren größten Wert bestimmen und meine Wahl der Randbetrachtung
   begründen.

### 6.4 Export und Druck

Knopfleiste wie im Referenzmodul: `Ergebnisse kopieren` (`id="bExport"`) und
`Als Arbeitsblatt drucken`. Darunter der Hinweis, dass nichts gespeichert wird.

`var namen = {…}` am Skriptende:

```
vw1: "Vorwissen 1 – Stammfunktion erkennen"
vw2: "Vorwissen 2 – Monotoniekriterium"
vw3: "Vorwissen 3 – Intervalladditivität"
sim1:"Simulation 1 – Nullstellen der Integralfunktion"
sim2:"Simulation 2 – sinkende Rate, steigender Bestand"
a1:  "Aufgabe 1 – bestimmtes Integral eines Polynoms"
a2:  "Aufgabe 2 – Zufluss mit dem Hauptsatz"
a3:  "Aufgabe 3 – Zuordnung Rate zu Integralfunktion"
a4:  "Aufgabe 4 – Integral einer e-Funktion"
a5:  "Aufgabe 5 – maximaler Bestand"
```

Die offenen Aufgaben a6 und a7 werden nicht automatisch ausgewertet und erscheinen daher — wie
im Referenzmodul — nicht im Export.

### 6.5 Anschlusshinweis (`<div class="hinweis">`)

**Wie es weitergeht.** Du kannst jetzt ein bestimmtes Integral in zwei Zeilen ausrechnen. Was du
damit noch nicht kannst, ist der ehrliche Flächeninhalt: Wenn der Graph die Achse schneidet,
zählt das Integral die Stücke darunter negativ, und ein Ergebnis von null heißt dann nicht, dass
nichts da wäre. Im nächsten Schritt kommen deshalb die Zerlegung an Nullstellen, der Betrag und
die Fläche **zwischen zwei Graphen** dazu. Das Werkzeug bleibt dasselbe — nur die Frage, was man
überhaupt integriert, wird genauer gestellt.

---

## Lehrerteil

`<details class="lehrer">` mit `<summary>Für die Lehrkraft</summary>`, am Ende von Abschnitt 6,
verschwindet beim Drucken.

### Einordnung

Inhaltsfeld **„Funktionen und Analysis"** (Kernlehrplan Mathematik, gymnasiale Oberstufe NRW).
Q1 umfasst die Fortführung der Analysis bis zur Integralrechnung einschließlich Hauptsatz und
Flächen zwischen Graphen; dieses Modul deckt das Kernstück ab: Integralfunktion, Hauptsatz in
beiden Teilen, Stammfunktion, Grundintegrale, lineare Substitution.

Prozessbezogene Schwerpunkte sind **Argumentieren** (der Beweis in 2.3, die Aufgaben a6 und a7),
**Werkzeuge nutzen** (die Simulation als Messinstrument, nicht als Illustration) und
**Modellieren** (a2, a4, a5). Vorausgesetzt werden: Ableitungsregeln für Potenz-, Exponential-
und trigonometrische Funktionen, Monotonie- und Krümmungsverhalten, notwendiges und hinreichendes
Kriterium für Extremstellen sowie — aus dem unmittelbar vorangehenden Modul — das bestimmte
Integral als gemeinsamer Grenzwert von Unter- und Obersumme, Intervalladditivität und der
orientierte Flächeninhalt.

**Stellung in der Reihe:** unmittelbar nach `mathe-q1-integral-rekonstruktion.html` und vor
`mathe-q1-flaechen-zwischen-graphen.html`. Wird dieses Modul **vor** dem Rekonstruktionsmodul
eingesetzt, verliert der Hauptsatz seine Pointe: Ohne die Erfahrung, dass 320 Streifen für ein
Zehntel Kubikmeter nötig sind, ist `F(b) − F(a)` bloß eine weitere Formel.

*Offen markiert:* Die Reihenfolge „Integralfunktion vor Stammfunktion" (statt umgekehrt) ist eine
fachdidaktische Entscheidung dieses Moduls, keine Vorgabe des Kernlehrplans. Sie wurde gewählt,
weil sie die Existenzaussage des Hauptsatzes sichtbar macht und den Anschluss an die
Ober-/Untersummen des Vorgängermoduls trägt. Ebenfalls nicht im Kernlehrplan festgelegt und
deshalb als Setzung zu lesen: dass der Mittelwertsatz hier benutzt (aber nicht bewiesen) wird.

### Zeitbedarf

Ausgelegt auf eine Doppelstunde von 90 Minuten (Tabelle im Modul in `<div class="tabelle">`
kapseln):

| Abschnitt | Zeit | Sozialform |
|---|---|---|
| 1 Einstieg (Wasserzähler, drei Vorwissensfragen) | 8 min | Plenum, Fragen in Einzelarbeit |
| 2 Integralfunktion, Differenzenquotienten-Tabelle, Hauptsatz Teil 1 | 20 min | lehrergelenkt, Details-Block je nach Kurs |
| 3 Stammfunktion, Hauptsatz Teil 2, Grundintegrale, Vererbungstabelle | 22 min | Plenum mit Sicherungsphasen |
| 4 Simulation mit Beobachtungsauftrag und zwei MC-Fragen | 20 min | Partnerarbeit am Gerät |
| 5 Übungen (Auswahl, siehe Differenzierung) | 15 min | Einzel- oder Partnerarbeit |
| 6 Abschluss, Selbstcheck, Export | 5 min | Plenum |

Realistisch in 90 Minuten schaffbar sind die Abschnitte 1 bis 4 vollständig sowie die Aufgaben
a1 und a2. Der Rest ist Hausaufgabe oder Material für die Folgestunde. Wer den Beweis in 2.3 im
Plenum entwickelt statt ihn lesen zu lassen, braucht dafür allein 12 bis 15 Minuten — dann fällt
der Übungsteil in der Stunde aus. Bei zwei Einzelstunden bietet sich der Schnitt nach Abschnitt 3
an; die Simulation eröffnet dann die zweite Stunde und wiederholt dabei den Satz.

### Typische Schülerfehler — und wo anzuhalten ist

**(1) „`f` negativ, also `I` negativ."** Der Leitfehler dieses Moduls. Ursache ist das
Flächenbild: Wer `I` als Fläche denkt, denkt auch, negative Fläche heiße negativer Wert.
→ **Anhalten** am Ende von 2.5, bevor Abschnitt 3 beginnt. Frage an den Kurs: „Bei `x = 10,5`
fließt Wasser ab. Ist das Becken deshalb leer?" Danach die beiden Zahlen an die Tafel:
`f(10,5) = −3,45`, `I₀(10,5) = 29,925`. Der Fehlerkasten in 2.5 und Aufgabe a6 prüfen es; `sim2` sichert die verwandte Verwechslung „sinkende Rate ⇒ sinkender Bestand“ ab.

**(2) `∫ₐˣ f(x) dx` — Integrationsvariable und Grenze gleich benannt.** Wird oft als Pedanterie
abgetan, führt aber beim Ableiten der Integralfunktion direkt in die Irre.
→ **Anhalten** direkt nach der Definition in 2.1. Analogie zur Programmierung oder zur
Summenschreibweise: Der Laufindex darf nicht die obere Grenze sein.

**(3) Vergessene Subtraktion der unteren Grenze.** `F(b)` wird hingeschrieben, `F(a)` nicht.
Besonders häufig, wenn `F(a) = 0` in Übungsaufgaben zufällig oft vorkommt — deshalb ist in a1
bewusst `F(1) = 4 ≠ 0` gewählt.
→ **Anhalten** nach dem ersten gemeinsamen Beispiel. Die eckige Klammer `[F(x)]ₐᵇ` als
Schreibdisziplin einführen: erst Klammer, dann Grenzen, dann einsetzen.

**(4) Fehlender Faktor `1/k` bei `e^(kx)`.** Der Klassiker in a4. Die Ursache ist, dass beim
Ableiten die innere Ableitung dazukommt, beim Integrieren also herausgeteilt werden muss.
→ **Anhalten** in 3.3 bei der Zeile `e^(kx)`. Regel für den Kurs: **Jede Stammfunktion wird
abgeleitet, bevor sie benutzt wird.** Das kostet zehn Sekunden und rettet in der Klausur mehrere
Punkte.

**(5) Erfundene Produktregel für Integrale.** `∫ x·eˣ dx = (x²/2)·eˣ` erscheint jedes Jahr.
→ **Anhalten** bei der Warnung in 3.3 und das Gegenbeispiel `∫₀¹ x·x dx = 1/3` gegen
`(1/2)·(1/2) = 1/4` gemeinsam rechnen lassen. Eine Zeile, die sitzt.

**(6) Extremstelle der Rate wird mit Extremstelle des Bestands verwechselt.** Im Beobachtungsauftrag und in a5
direkt geprüft: `t = 4` gegen `t = 9`; `sim1` prüft zusätzlich „Nullstelle der Rate = Nullstelle des Integrals“.
→ **Anhalten** in der Simulation bei Rate A. „Wann ist am meisten Wasser drin — wenn es am
schnellsten zuläuft oder wenn es aufhört zuzulaufen?" Erst danach die Vererbungstabelle in 3.4
gemeinsam ausfüllen lassen, statt sie vorzulesen.

**(7) Stammfunktion und Integralfunktion werden gleichgesetzt.** Kommt spätestens bei a7.
→ **Anhalten** bei 3.6. Der Merksatz „Integralfunktion = Stammfunktion mit Nullstelle" ist knapp
genug für die Tafel, und das Gegenbeispiel `eˣ + 1` ist in einer Minute erklärt.

**(8) „Der Hauptsatz gilt immer."** Die Stetigkeitsvoraussetzung wird überlesen.
→ **Anhalten** nach Schritt 4 im Beweis. Der einzige Ort, an dem die Stetigkeit gebraucht wird,
lässt sich im Beweistext markieren — das ist ein gutes Beispiel dafür, wie man einen Beweis auf
seine Voraussetzungen hin liest.

### Differenzierung

**Für schnellere Lernende:**

- Die Frage aus 3.1 vertiefen: Warum darf man `ℝ \ {0}` nicht als „ein Intervall" behandeln?
  Aufgabe: Zeige, dass `F(x) = −1/x` und die stückweise definierte Funktion `G` (links `−1/x`,
  rechts `−1/x + 1`) beide Stammfunktionen von `1/x²` auf `ℝ \ {0}` sind, ihre Differenz aber
  nicht konstant ist. Das ist der Übergang zur Frage, warum die Voraussetzung im Satz steht.
- Die Integralfunktion von `f(x) = |x|` untersuchen: `I₀` ist differenzierbar, obwohl `f` an der
  Stelle 0 einen Knick hat — das Integrieren glättet. Anschlussfrage: Gilt der Satz auch für eine
  Funktion mit Sprungstelle?
- In der Simulation `a` systematisch verändern und die Kurvenschar protokollieren; daraus die
  Aussage `I_b = I_a − I_a(b)` selbst formulieren und beweisen.
- Zusatzaufgabe zu a7: Für welche `c` ist `x³/3 + c` eine Integralfunktion von `x²`? (Antwort:
  für **jedes** `c`, denn `x³/3 + c` hat wegen der Surjektivität von `x³` stets eine Nullstelle,
  nämlich `a = −(3c)^(1/3)`. Der Unterschied zu `eˣ` ist genau die Wertemenge der Stammfunktion —
  das ist die eigentliche Pointe.)

**Für Lernende, die mehr Zeit brauchen:**

- Pflichtteil sind a1, a2 und a3. a1 ist reines Handwerk, a2 dasselbe Handwerk im Sachkontext,
  a3 verlangt keine Rechnung und trägt trotzdem die zentrale Einsicht.
- Die Tabelle in 3.4 vorab gemeinsam an der Tafel ausfüllen und als Merkblatt mitgeben; damit
  ist a3 ohne weitere Hilfe lösbar.
- Von den beiden AB-III-Aufgaben genügt a6. Sie hängt an einer einzigen falschen Aussage und
  braucht nur ein Gegenbeispiel, während a7 drei Teilschritte und eine Äquivalenzbegründung
  verlangt.
- Der Beweis in 2.3 kann übersprungen werden; die Differenzenquotienten-Tabelle in 2.2 trägt die
  Einsicht auch allein. Sie ist bewusst so gebaut, dass man das Ergebnis 4,80 ohne jede
  Vorkenntnis ablesen kann.

### Bezug zu Realexperimenten und Daten

- **Wasserzähler und Durchflussmesser.** Der Einstieg ist mit zwei Handyfotos ein echtes
  Experiment: Zählerstand vor und nach einem Vorgang, parallel die angezeigte Momentanrate
  mitfilmen. Der Vergleich „Differenz der Zählerstände" gegen „aufsummierte Rate" ist der
  Hauptsatz in Reinform, samt Messabweichung. Aufwand: 10 Minuten Vorbereitung.
- **Fahrzeug mit Tacho und Kilometerzähler.** Dieselbe Struktur, nur mit `v` und `s`. Ein kurzes
  Video einer Autofahrt (Beifahrersitz, Blick aufs Kombiinstrument) liefert beide Größen
  gleichzeitig. Die Lernenden schätzen aus dem Tachoverlauf die Strecke ab und vergleichen mit
  der Differenz der Kilometerstände.
- **Kondensator-Entladung (Anschluss Physik).** `I(t) = I₀·e^(−t/RC)` und die geflossene Ladung
  `Q = ∫ I dt`. Die Rate C der Simulation ist exakt dieses Modell mit `1/RC = 0,3`. Eine
  Absprache mit der Physik-Fachschaft lohnt sich, weil dort dieselbe Rechnung unter anderem Namen
  vorkommt — und weil der Grenzwert `40/3` dem „endlichen Gesamtladungsbetrag" entspricht.
- **Abflussdaten eines Flusses.** Die Landesbehörden veröffentlichen Pegel- und Abflusswerte in
  m³/s. Mit einem Tabellenkalkulationsprogramm lässt sich die Summenkurve bilden; sie ist die
  numerische Integralfunktion. Der Vergleich ihrer Steigung mit den Rohdaten ist Teil 1 des
  Hauptsatzes an echten Zahlen.
- **CAS/GTR.** Sinnvoll erst **nach** dieser Stunde. Wer `fnInt` kennt, bevor er den Hauptsatz
  kennt, hält das Integral für eine Taste. Ein guter Einsatz ist dagegen die Kontrolle der
  eigenen Stammfunktionen durch Ableiten im Rechner — das entspricht genau der Disziplin, die
  unter Fehler (4) empfohlen wird.

---

## Checkliste für den Bauagenten

### Benötigte Bausteine und ihre Schlüssel

| Schlüssel | Baustein | `data`-Attribut | Optionen / Besonderheit | AB |
|---|---|---|---|---|
| `vw1` | Multiple Choice | `data-mc="vw1"` | 3 Optionen, `r: 1` | — |
| `vw2` | Multiple Choice | `data-mc="vw2"` | 3 Optionen, `r: 2` | — |
| `vw3` | Multiple Choice | `data-mc="vw3"` | 3 Optionen, `r: 1` | — |
| `sim1` | Multiple Choice | `data-mc="sim1"` | 3 Optionen, `r: 1` | II |
| `sim2` | Multiple Choice | `data-mc="sim2"` | 3 Optionen, `r: 1` | II |
| `a1` | Zahleneingabe | `data-num="a1"` | `wert: 20`, `"FE"`, `tol: 0.05`, kein `alt` | I |
| `a2` | Zahleneingabe | `data-num="a2"` | `wert: 22.67`, `"m³"`, `tol: 0.05`, `alt: 22670 "L"` | II |
| `a3` | Zuordnung | `data-check="zuordnung"` | 4 SVG-Diagramme, Lösung C·D·B·A | II |
| `a4` | Zahleneingabe | `data-num="a4"` | `wert: 10.36`, `"L"`, `tol: 0.05`, `alt: 0.01036 "m³"` | II |
| `a5` | Zahleneingabe | `data-num="a5"` | `wert: 40.9`, `"m³"`, `tol: 0.05`, `alt: 40900 "L"` | II |
| `a6` | offene Aufgabe | `data-loesung="a6"` | `<textarea>`, Lösung in `data-stufe="9"` | III |
| `a7` | offene Aufgabe | `data-loesung="a7"` | `<textarea>`, Lösung in `data-stufe="9"` | III |

Dreistufige Hilfen (`data-hilfe="1|2|3"` plus `.hilfe-text[data-stufe="1|2|3"]`) bekommen:
`a1`, `a2`, `a4`, `a5`. Die Zuordnung `a3` und die offenen Aufgaben `a6`, `a7` bekommen keine
Hilfestufen 1–3 (wie im Referenzmodul); `a6` und `a7` bekommen stattdessen `data-stufe="9"`.

### Simulationsbausteine

| Element | `id` | Bereich / Werte |
|---|---|---|
| Canvas | `cvSim` | `width="1000" height="560"` |
| Regler untere Grenze `a` | `rA` | 0 … 120 → `a = rA/10`, Start 0 |
| Regler obere Grenze `x` | `rX` | 0 … 240 → `x = rX/20`, Start 120 (`x = 6,00`) |
| Anzeige `a` | `lA` | 1 Nachkommastelle |
| Anzeige `x` | `lX` | 2 Nachkommastellen |
| Anzeige `f(x)` | `lF` | 2 Nachkommastellen |
| Anzeige `I_a(x)` | `lI` | 2 Nachkommastellen |
| Anzeige Steigung von `I_a` | `lM` | 2 Nachkommastellen |
| Anzeige Unterschied | `lD` | 3 Nachkommastellen, steht immer auf `0,000` |
| Knöpfe Rate | `data-rate="A"`, `"B"`, `"C"` | Rate A ist Startzustand |
| Knopf Abspielen | `bPlay` | `x` läuft mit 2,0 h/s bis 12, dann Stopp |
| Knopf Zurücksetzen | `bReset` | Rate A, `a = 0`, `x = 6,00` |
| Checkbox Tangente | `cTan` | Vorgabe: gesetzt |

### Prüfpunkte vor der Abnahme

1. Jede der 11 Formeln in Abschnitt 3.3 und jede abgesetzte Formel hat ein gefülltes
   `data-plain` mit Unicode (`∫`, `≤`, `⟹`, `⁻`, `·`, `−`).
2. Alle sechs Tabellen dieses Moduls stehen in `<div class="tabelle">`.
3. Die Simulation liefert bei Rate A, `a = 0`, `x = 9,00` den Wert `I = 32,40` und die Steigung
   `0,00`; bei `x = 10,50` die Werte `I = 29,93` und Steigung `−3,45`; bei `x = 4,00` die Werte
   `I = 15,73` und Steigung `5,00`. Bei Rate B, `a = 0`, `x = 4,00`: `I = −6,40`, Steigung
   `0,00`. Bei Rate C, `a = 0`, `x = 5,00`: `I = 10,36`, Steigung `0,89`.
4. Bei `x < a` zeigt die Simulation einen negativen Integralwert an (Test: Rate A, `a = 9,0`,
   `x = 3,00` ⟹ `I = 10,80 − 32,40 = −21,60`).
5. Der Eintrag in `fachliches/modulliste.md` wird nach bestandener Prüfung von `in Arbeit` auf
   `fertig` gesetzt.

### Quelle der Kontrollrechnungen

Alle Zahlenwerte dieses Dokuments wurden mit Python nachgerechnet (Brüche über
`fractions.Fraction`, numerische Gegenproben über die Mittelpunktsregel mit 200 000 bzw.
400 000 Streifen sowie über die Simpson-Regel mit `n = 200`, also demselben Verfahren, das die
Simulation verwenden soll). Die größte gefundene Abweichung zwischen geschlossener Form und
numerischer Gegenprobe beträgt `1,8·10⁻¹⁰`, die größte Abweichung der zentralen Differenz von
`f(x)` beträgt `2,7·10⁻⁵` und liegt damit drei Größenordnungen unter der angezeigten
Rundungsstelle.
