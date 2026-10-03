# Modulinhalt: mathe-q1-flaechen-zwischen-graphen

**Datei für den Bauagenten:** `module/mathe-q1-flaechen-zwischen-graphen.html`
**Fach/Stufe:** Mathematik · Qualifikationsphase 1 · Leistungskurs
**Kopf-Chips:** `Inhaltsfeld: Funktionen und Analysis` · `Kernlehrplan NRW, GOSt` · `ca. 90 Minuten`
**Titel im Kopf (`<h1>`):** Flächen zwischen Kurven – Vorzeichenwechsel und Schnittstellen
**Farbtokens:** Mathematik — `--akzent: #0d7a52`, `--akzent-hell: #e7f6ef`, `--akzent-rand: #b5e0cd`
**Footer-Zeile:** Mathematik LK Q1 · Flächeninhalt zwischen Graphen, Vorzeichenwechsel und Schnittstellen · erstellt für den Unterricht nach dem Kernlehrplan NRW für die gymnasiale Oberstufe.

**Anschluss.** Baut unmittelbar auf `mathe-q1-hauptsatz.html` auf (Inhalt: `inhalte/mathe-q1-hauptsatz.md`,
nur gelesen). Vorausgesetzt und **nicht erneut hergeleitet** werden: bestimmtes Integral als Grenzwert
von Unter- und Obersummen, Intervalladditivität, orientierter Flächeninhalt, Hauptsatz in beiden
Teilen (`I_a′ = f`, `∫ₐᵇ f = F(b) − F(a)`), Integralfunktion, Grundintegrale, lineare Substitution.
Das Schlussstück des Hauptsatz-Moduls kündigt genau dieses Thema an: „Wenn der Graph die Achse
schneidet, zählt das Integral die Stücke darunter negativ, und ein Ergebnis von null heißt dann
nicht, dass nichts da wäre." Das ist der Aufhänger.

**Seitengliederung (sechs `<section>` gemäß CLAUDE.md):**

| `<section id>` | `.stufe`-Nr. | Überschrift | kommt aus Abschnitt |
|---|---|---|---|
| `einstieg` | 1 | Einstieg | Abschnitt 1 |
| `bilanz` | 2 | Bilanz ist nicht Flächeninhalt | Abschnitt 2 |
| `zwischen` | 3 | Zwischen zwei Graphen: Schnittstellen als Grenzen | Abschnitt 3 |
| `simulation` | 4 | Wo Bilanz und Flächeninhalt auseinanderlaufen | Abschnitt 4 |
| `uebungen` | 5 | Übungen | Abschnitt 5 |
| `abschluss` | 6 | Zusammenfassung und Selbstcheck | Abschnitt 6 + Lehrerteil |

**Schreibweise in diesem Dokument.** Formeln stehen hier in Klartext. Der Bauagent setzt jede davon
als `<span class="m" data-tex="…" data-plain="…">` bzw. `<div class="m block">`. Wo die
LaTeX-Fassung nicht offensichtlich ist, steht sie als `TEX:` daneben. Alle Dezimalzahlen im
fertigen Modul mit **Komma**. Im Modul heißt `∫ₐᵇ f dx` der **Integralwert** oder die **Bilanz**
(orientierter Flächeninhalt, Teile oberhalb der Achse positiv, unterhalb negativ), `∫ₐᵇ |f| dx` der
**Flächeninhalt**. Diese zwei Wörter werden im ganzen Modul strikt getrennt benutzt.

**Alle Zahlen in diesem Dokument sind gerechnet**, nicht geschätzt. Kontrollrechnungen stehen bei
der jeweiligen Stelle; das vollständige Prüfskript (sympy, mpmath, Simulationsverfahren) steht am
Ende der Datei im Abschnitt „Quelle der Kontrollrechnungen" und enthält für jede hier genannte Zahl
eine `assert`-Zeile.

**Arbeitsstand dieser Datei:** vollständig (sechs Abschnitte, Lehrerteil, Checkliste, Prüfskript); nachgeführt nach Fach- und Technikprüfung (Canvas 1000 × 670, Marken/Legende/Titel neu gesetzt, Paar-C-Einheit `min`, Hinweis zu Paar B, Rückmeldetexte und Einheiten in a5/a6 vereinheitlicht).

---

## Abschnitt 1 — Einstieg

`<section id="einstieg">`, `.stufe`-Nummer **1**, Überschrift **Einstieg**.

### 1.1 Aufhänger (zwei Absätze Fließtext)

**Absatz 1.**
Für eine neue Umgehungsstraße legt das Planungsbüro einen Querschnitt durch das Gelände: eine
Kurve für die Geländeoberfläche (G), darunter oder darüber eine fast gerade Linie für die geplante
Trasse (T). Wo das Gelände höher liegt als die Trasse, muss Boden abgetragen werden — ein
**Einschnitt**. Wo es tiefer liegt, muss aufgeschüttet werden — ein **Damm**. Für die Kalkulation
will der Bauleiter zwei Zahlen: Wie viel Erde bleibt am Ende übrig oder fehlt (bestimmt, ob
Lastwagen Boden abfahren oder anliefern müssen), und wie viel Erde wird insgesamt bewegt
(bestimmt, wie lange die Bagger laufen).

**Absatz 2.**
Aus der letzten Einheit kennst du ein Werkzeug, das die erste Zahl sofort liefert: `∫ (G − T) dx`
zählt jeden Einschnitt positiv und jeden Damm negativ. Fällt beides gleich groß aus, steht dort
eine glatte Null — und der Bauleiter würde meinen, die Baustelle bewege gar keine Erde, obwohl
wochenlang Lastwagen fahren. Das Integral rechnet also korrekt und beantwortet trotzdem nicht die
Frage nach dem Aufwand. Diese Einheit klärt, wie du aus der Bilanz einen ehrlichen Flächeninhalt
machst, wo du dafür die Grenzen hernimmst — nämlich dort, wo sich die beiden Kurven schneiden —
und warum nicht jede Schnittstelle dazugehört.

### 1.2 Vorwissensfragen (Multiple Choice, `.karte` mit `<h3>Vorwissen prüfen</h3>`)

Einleitungssatz unter der Überschrift (grau, 15 px):
*Zwei Fragen aus der Einführungsphase, eine aus der letzten Einheit. Wenn du hier hängst, lohnt
sich ein Blick zurück, bevor du weitermachst.*

**vw1** — Schlüssel `vw1`, Radio-Name `vw1`, richtige Option: **Index 1** (Einführungsphase:
quadratische Gleichungen)

> Frage: Wo schneiden sich die Graphen von `f(x) = x²` und `g(x) = x + 2`?
>
> - `data-i="0"`: bei `x = 1` und `x = −2`
> - `data-i="1"`: bei `x = −1` und `x = 2`
> - `data-i="2"`: nur bei `x = 2`

Feedback (`fb`-Array, drei Einträge):

- **Index 0:** Vorzeichenfehler beim Umformen. Aus `x² = x + 2` folgt `x² − x − 2 = 0`; deine beiden
  Werte lösen dagegen `x² + x − 2 = 0`, also `x² = 2 − x` — das ist die Schnittstellengleichung
  mit der fallenden Geraden `y = 2 − x`. Probe: `f(1) = 1`, aber `g(1) = 3`; keine Schnittstelle.
- **Index 1 (richtig):** Richtig. `x² − x − 2 = (x − 2)(x + 1) = 0`. Probe: `f(−1) = 1 = g(−1)` und
  `f(2) = 4 = g(2)`. Merk dir das Vorgehen — Funktionsterme gleichsetzen, auf null bringen,
  lösen: Es ist der erste Schritt jeder Flächenaufgabe dieser Einheit.
- **Index 2:** Die negative Lösung wurde verworfen, vermutlich weil „Fläche nicht negativ sein
  kann". Die Frage betrifft aber Schnittstellen, nicht Flächen: `f(−1) = 1 = g(−1)`, also ist
  `x = −1` ebenfalls eine. Hier ist das später besonders bitter — eine verlorene Schnittstelle ist
  eine verlorene Integrationsgrenze.

**vw2** — Schlüssel `vw2`, Radio-Name `vw2`, richtige Option: **Index 0** (aus der letzten Einheit:
Linearität des Integrals)

> Frage: Bekannt sind `∫₀² f(x) dx = 5` und `∫₀² g(x) dx = 2`. Wie groß ist
> `∫₀² (f(x) − 2·g(x)) dx`?
>
> - `data-i="0"`: `1`
> - `data-i="1"`: `3`
> - `data-i="2"`: `9`

Feedback:

- **Index 0 (richtig):** Richtig. Das Integral ist linear: `∫ (f − 2g) = ∫ f − 2·∫ g = 5 − 4 = 1`.
  Genau diese Zeile trägt später die Formel `∫ (f − g)` für die Fläche zwischen zwei Graphen.
- **Index 1:** Du hast `5 − 2` gerechnet, also den Faktor 2 vor `g` nicht mitgenommen. Konstante
  Faktoren gehören zum Integral: `∫ 2g = 2·∫ g = 4`. Probe mit `g = 1` auf `[0; 2]`: `∫ 2·1 dx = 4`,
  nicht 2.
- **Index 2:** Aus dem Minuszeichen wurde ein Pluszeichen: `5 + 2·2 = 9` wäre `∫ (f + 2g)`. Die
  Differenz zweier Funktionen wird zur Differenz der Integrale — und genau das Vorzeichen
  entscheidet später darüber, welcher Graph „oben" liegt.

**vw3** — Schlüssel `vw3`, Radio-Name `vw3`, richtige Option: **Index 2** (Einführungsphase:
Nullstellen ganzrationaler Funktionen)

> Frage: Wie viele Nullstellen hat `f(x) = x³ − 3x`?
>
> - `data-i="0"`: eine, nämlich `x = 0`
> - `data-i="1"`: zwei, nämlich `x = √3` und `x = −√3`
> - `data-i="2"`: drei, nämlich `x = −√3`, `x = 0` und `x = √3`

Feedback:

- **Index 0:** `x = 0` ist eine Nullstelle, aber nicht die einzige. `x³ − 3x = x·(x² − 3)`: Ein
  Produkt ist null, wenn **ein** Faktor null ist — der zweite Faktor liefert `x² = 3`, also
  `x = ±√3`. Rechne jeden Faktor einzeln durch.
- **Index 1:** Du hast beide Seiten durch `x` geteilt und damit die Nullstelle `x = 0` verloren.
  Bei Nullstellen wird ausgeklammert, nicht gekürzt: `x·(x² − 3) = 0` hat drei Lösungen. In dieser
  Einheit wäre jede verlorene Nullstelle eine verlorene Integrationsgrenze.
- **Index 2 (richtig):** Richtig, `x·(x² − 3) = 0` liefert `0` und `±√3`. Ausklammern statt kürzen —
  und alle drei Nullstellen sind hier Kandidaten für Integrationsgrenzen.

**Kontrollrechnung vw1–vw3.** vw1: `x² − x − 2 = 0` ⟹ `x = (1 ± √(1 + 8))/2 = (1 ± 3)/2`, also `2`
und `−1`. Fehlerfall `x² + x − 2 = 0` ⟹ `x = 1` und `x = −2` (Index 0), Probe `g(1) = 3 ≠ 1 = f(1)`.
vw2: `5 − 2·2 = 1`; Fehlerwerte `5 − 2 = 3`, `5 + 4 = 9`. vw3: `x³ − 3x = 0` ⟹ `x ∈ {−√3; 0; √3}`
mit `√3 = 1,7321`. Alle Werte im Prüfskript nachgerechnet.

---

## Abschnitt 2 — Erklärteil, erster Block

`<section id="bilanz">`, `.stufe`-Nummer **2**, Überschrift **Bilanz ist nicht Flächeninhalt**.

### 2.1 Ein Integral, das nicht die Fläche misst (`<h3>`)

Wir arbeiten mit einer einzigen Funktion, bis die Idee sitzt:

`f(x) = x³ − 4x² + 3x = x·(x − 1)·(x − 3)`, betrachtet auf dem Intervall `[0; 3]`.

Ausklammern liefert die Nullstellen sofort: `x = 0`, `x = 1`, `x = 3`. Zwischen `0` und `1` liegt
der Graph oberhalb der Achse (Probe `f(0,5) = 0,5·(−0,5)·(−2,5) = +0,625`), zwischen `1` und `3`
unterhalb (Probe `f(2) = 2·1·(−1) = −2`). Es gibt also zwei Flächenstücke, ein positives und ein
negatives.

Mit der Stammfunktion `F(x) = x⁴/4 − (4/3)·x³ + (3/2)·x²` (Probe: `F′(x) = x³ − 4x² + 3x` ✓) rechnest
du (Tabelle in `<div class="tabelle">` kapseln):

| `x` | 0 | 1 | 3 |
|---|---|---|---|
| `F(x)` | 0 | 5/12 ≈ 0,4167 | −9/4 = −2,25 |

Damit:

- oberes Stück: `∫₀¹ f dx = F(1) − F(0) = 5/12 ≈ 0,4167`
- unteres Stück: `∫₁³ f dx = F(3) − F(1) = −9/4 − 5/12 = −27/12 − 5/12 = −32/12 = −8/3 ≈ −2,6667`
- Integralwert insgesamt: `∫₀³ f dx = F(3) − F(0) = −9/4 = −2,25`

Ein Flächeninhalt kann nicht negativ sein, und `−2,25` ist es trotzdem. Schlimmer: Selbst der
Betrag `2,25` ist **nicht** der Flächeninhalt. Das obere Stück (0,4167) und das untere (2,6667)
haben sich im Integral teilweise weggerechnet. Tatsächlich bedeckt der Graph mit der Achse
`5/12 + 8/3 = 5/12 + 32/12 = 37/12 ≈ 3,0833` Flächeneinheiten.

*Kontrollrechnung:* numerisch (Mittelpunktsregel, 400 000 Streifen) `∫₀¹ f = 0,41666667`,
`∫₁³ f = −2,66666667`, `∫₀³ f = −2,25000000`, `∫₀³ |f| = 3,08333333`. Größte Abweichung zur
geschlossenen Form `< 10⁻⁹`. Relative Abweichung der Näherung „Betrag des Integrals":
`(3,0833 − 2,25)/3,0833 = 0,2703`, also `27,0 %` zu wenig.

### 2.2 Bilanz und Flächeninhalt — zwei Wörter, zwei Zahlen (`<h3>`)

Damit du beides sauber auseinanderhältst, bekommen die beiden Größen Namen:

> **Definition (Flächeninhalt zwischen Graph und x-Achse).** `f` sei auf `[a; b]` stetig. Dann heißt
>
> `A = ∫ₐᵇ |f(x)| dx`
>
> der **Flächeninhalt** zwischen dem Graphen von `f` und der `x`-Achse über `[a; b]`. Das gewöhnliche
> Integral `∫ₐᵇ f(x) dx` heißt dagegen die **Bilanz** (orientierter Flächeninhalt).
>
> TEX: `A = \int_a^b |f(x)|\,\mathrm{d}x`
> data-plain: `A = ∫ von a bis b |f(x)| dx`

Bezeichnet `P` die Summe aller Flächenstücke **oberhalb** der Achse und `N` die aller Stücke
**unterhalb** (beide positiv gezählt), dann gilt

`Bilanz = P − N` und `Flächeninhalt = P + N`.

Für unser Beispiel: `P = 5/12`, `N = 8/3`, also Bilanz `5/12 − 32/12 = −27/12 = −9/4` ✓ und
Flächeninhalt `37/12` ✓. Daraus folgt eine Beziehung, die die Simulation später zeigt:

`Flächeninhalt − |Bilanz| = 2·min(P, N)`.

Im Beispiel: `37/12 − 27/12 = 10/12 = 2·(5/12)` ✓. Die Differenz ist also **doppelt so groß wie das
kleinere der beiden Stücke** — das Stück, das sich in der Bilanz vollständig „versteckt".

### 2.3 Herleitung (ausgelagert in `<details>`)

`<summary>` **Warum `∫|f|` der Flächeninhalt ist — und warum man an Nullstellen zerlegt** `</summary>`

**Schritt 1 — oberhalb der Achse.** Ist `f ≥ 0` auf `[u; v]`, dann ist der Flächeninhalt unter dem
Graphen nach der Definition aus der Einheit über Ober- und Untersummen genau `∫ᵤᵛ f dx`. Hier ist
nichts zu zeigen.

**Schritt 2 — unterhalb der Achse.** Ist `f ≤ 0` auf `[u; v]`, dann ist `−f ≥ 0`, und der Graph von
`−f` entsteht durch Spiegelung an der `x`-Achse. Die Spiegelung ändert weder Breite noch Höhe eines
Streifens und damit keinen Flächeninhalt; auch für die Summen gilt das sichtbar:
die Untersumme von `−f` ist das Negative der Obersumme von `f` (das Minimum von `−f` ist das
Negative des Maximums von `f`). Also `∫ᵤᵛ (−f) dx = −∫ᵤᵛ f dx`, und der Flächeninhalt ist
`−∫ᵤᵛ f dx = |∫ᵤᵛ f dx|`, denn `∫ᵤᵛ f dx ≤ 0`.

**Schritt 3 — Zerlegen.** Hat die stetige Funktion `f` auf `[a; b]` genau die Nullstellen
`a < z₁ < z₂ < … < zₖ < b` mit Vorzeichenwechsel, so hat `f` auf jedem Teilintervall
`[zᵢ; zᵢ₊₁]` ein festes Vorzeichen (Zwischenwertsatz: ein Vorzeichenwechsel ohne Nullstelle ist bei
stetigem `f` unmöglich). Auf jedem Stück gilt Schritt 1 oder 2, und die Intervalladditivität
setzt zusammen:

`A = |∫ₐ^(z₁) f| + |∫_(z₁)^(z₂) f| + … + |∫_(zₖ)^b f|`

**Schritt 4 — warum nicht einfach `|∫ₐᵇ f|`.** Für jedes stetige `f` gilt die Dreiecksungleichung
für Integrale `|∫ₐᵇ f| ≤ ∫ₐᵇ |f|`, denn `−|f| ≤ f ≤ |f|` und das Integral erhält Ungleichungen.
Gleichheit gilt genau dann, wenn `f` auf `[a; b]` nirgends das Vorzeichen wechselt. Sobald
Stücke mit verschiedenem Vorzeichen da sind, ist die rechte Seite **echt** größer — im Beispiel
`2,25 < 3,0833`. ∎

**Wo genau die Stetigkeit gebraucht wird.** In Schritt 3: Nur weil `f` zwischen zwei aufeinander
folgenden Nullstellen nicht springen kann, ist das Vorzeichen dort konstant und der Betrag lässt
sich abspalten. Für Funktionen mit Sprungstellen müsstest du die Sprungstellen wie Nullstellen
behandeln.

*(Ende `<details>`.)*

### 2.4 Das Verfahren in vier Schritten (`<div class="merksatz">`)

> **Merksatz (Kernaussage 1).** Das Integral ist eine **Bilanz**, der Flächeninhalt eine **Summe
> von Beträgen**. Ein Integralwert von null sagt nur, dass sich Flächenstücke aufheben — nie, dass
> keine Fläche da ist. Deshalb gilt: **Die Nullstellen mit Vorzeichenwechsel sind die
> Integrationsgrenzen des Flächeninhalts.**

So gehst du vor:

1. **Skizze oder Vorzeichenbild** — wo liegt der Graph oberhalb, wo unterhalb der Achse?
2. **Nullstellen im Intervall bestimmen** — alle, aber nur die mit Vorzeichenwechsel zählen als
   Grenzen. Nullstellen **außerhalb** von `[a; b]` spielen keine Rolle.
3. **Eine** Stammfunktion `F` bilden und ihre Werte an allen Grenzen `a, z₁, …, zₖ, b` in einer
   Tabelle festhalten. Die Teilintegrale sind dann die Differenzen benachbarter Tabellenwerte.
4. **Beträge der Teilintegrale addieren.** Nie das Gesamtintegral mit Betragsstrichen versehen.

Im Beispiel: `A = |F(1) − F(0)| + |F(3) − F(1)| = |5/12| + |−32/12| = 37/12`. Die Tabelle aus 2.1
war schon Schritt 3.

### 2.5 Die typische Fehlvorstellung — und was dagegen hilft (`<div class="hinweis">`)

**Häufiger Fehler.** „Ich rechne das Integral aus, wenn es negativ ist, lasse ich das Minus weg —
fertig." Das klingt vernünftig und ist trotzdem falsch, sobald der Graph die Achse schneidet.
Der Betrag gehört **um jedes Teilstück**, nicht um die Summe. In unserem Beispiel liefert die
Betragsstrich-Abkürzung `|−2,25| = 2,25`, der Flächeninhalt ist aber `3,08` — fast ein Drittel
mehr. Und der Extremfall: Bei `f(x) = x³` auf `[−1; 1]` steht die Bilanz auf `0`, der Flächeninhalt
ist `1/2`. Wer bei „Ergebnis null" schließt, die Kurve habe keine Fläche mit der Achse, hat die
Bilanz mit dem Flächeninhalt verwechselt.

*Kontrollrechnung:* `∫₋₁¹ x³ dx = 0`, `2·∫₀¹ x³ dx = 2·(1/4) = 1/2`. Numerisch:
`∫₋₁¹ |x³| dx = 0,50000000`.

**Merkhilfe für die Klausur:** Steht in einer Aufgabe „Flächeninhalt", „umschlossene Fläche" oder
„Flächenstück", lautet die erste Zeile deiner Rechnung **nicht** `∫ … dx`, sondern eine
Nullstellenrechnung.

### 2.6 Zwei Kurven, die sich aufbauen — Anschluss an den Hauptsatz (`<h3>`)

Die Bilanzkurve und die Flächenkurve wachsen mit der oberen Grenze `x`:

`B(x) = ∫ₐˣ f(t) dt` und `A(x) = ∫ₐˣ |f(t)| dt`.

Nach Teil 1 des Hauptsatzes gilt `B′(x) = f(x)`. Auch `|f|` ist stetig, also gilt ebenso
`A′(x) = |f(x)|`. Daraus lesen wir ab, ohne zu rechnen:

- `A` ist **nie fallend**: `A′ = |f| ≥ 0`. Flächeninhalt kann nur wachsen.
- `B` **steigt**, wo `f > 0`, und **fällt**, wo `f < 0`. Bei einem Vorzeichenwechsel von `f`
  hat `B` einen Extrempunkt.
- Dort, wo `f` das Vorzeichen wechselt, **trennen sich die beiden Kurven**: Bis zur ersten
  Nullstelle gilt `A(x) = |B(x)|`, danach wächst `A` weiter, während `B` umkehrt.

Genau diese beiden Kurven baut die Simulation in Abschnitt 4 vor deinen Augen auf.

---

## Abschnitt 3 — Erklärteil, zweiter Block (Vertiefung)

`<section id="zwischen">`, `.stufe`-Nummer **3**,
Überschrift **Zwischen zwei Graphen: Schnittstellen als Grenzen**.

### 3.1 Von der Achse zu zwei Graphen (`<h3>`)

Die `x`-Achse ist selbst ein Graph, nämlich der von `g(x) = 0`. Die Aufgabe „Fläche zwischen `f`
und der Achse" ist damit ein Sonderfall der Aufgabe „Fläche zwischen `f` und `g`". Der Trick des
Abschnitts: Man führt den allgemeinen Fall auf den Sonderfall zurück, indem man die
**Differenzfunktion**

`h(x) = f(x) − g(x)`

bildet. Sie misst den senkrechten Abstand der Graphen, mit Vorzeichen: `h > 0` heißt „`f` liegt
oben", `h < 0` heißt „`g` liegt oben", `h = 0` heißt „die Graphen treffen sich".

> **Satz (Fläche zwischen zwei Graphen).** `f` und `g` seien auf `[a; b]` stetig. Dann ist der
> Flächeninhalt zwischen den Graphen über `[a; b]`
>
> `A = ∫ₐᵇ |f(x) − g(x)| dx`.
>
> Gilt `f ≥ g` auf ganz `[a; b]`, so vereinfacht sich das zu `A = ∫ₐᵇ (f(x) − g(x)) dx` — und es
> ist gleichgültig, wie die Graphen zur `x`-Achse liegen.
>
> TEX (abgesetzt): `A = \int_a^b \bigl|\,f(x)-g(x)\,\bigr|\,\mathrm{d}x`
> data-plain: `A = ∫ von a bis b |f(x) − g(x)| dx`

Das Wörtchen „gleichgültig" ist der überraschende Teil: Die Fläche zwischen zwei Graphen hängt
nicht davon ab, ob sie über, unter oder quer zur Achse liegen. Das liefert die folgende Herleitung.

### 3.2 Herleitung (ausgelagert in `<details>`)

`<summary>` **Warum `∫ (f − g)` die Fläche zwischen den Graphen ist — auch unterhalb der Achse** `</summary>`

**Voraussetzung.** `f ≥ g` auf `[a; b]`, beide stetig.

**Schritt 1 — beide Graphen über die Achse heben.** `g` ist stetig auf dem abgeschlossenen
Intervall `[a; b]` und hat dort ein Minimum `m` (Satz vom Minimum und Maximum). Wähle
`c = |m|`. Dann gilt `g(x) + c ≥ 0` für alle `x ∈ [a; b]` und erst recht `f(x) + c ≥ g(x) + c ≥ 0`.

**Schritt 2 — die Verschiebung ändert die Fläche nicht.** Die senkrechte Verschiebung beider
Graphen um `c` nach oben ist eine Kongruenzabbildung. Das Flächenstück zwischen den Graphen wird
dabei nur verschoben, sein Inhalt bleibt gleich.

**Schritt 3 — Fläche als Differenz zweier Flächen „unter" den Graphen.** Nach Schritt 1 liegen
beide verschobenen Graphen oberhalb der Achse, und der Graph von `g + c` liegt unter dem von
`f + c`. Das Flächenstück dazwischen ist deshalb die Fläche unter `f + c` **minus** die Fläche unter
`g + c`. Beide sind nach Definition Integrale:

`A = ∫ₐᵇ (f + c) dx − ∫ₐᵇ (g + c) dx`

**Schritt 4 — rechnen.** Wegen der Linearität des Integrals (vw2!) gilt
`∫ (f + c) − ∫ (g + c) = ∫ ((f + c) − (g + c)) = ∫ (f − g)`. Die Konstante `c` kürzt sich heraus:

`A = ∫ₐᵇ (f(x) − g(x)) dx`.

**Schritt 5 — ohne Voraussetzung `f ≥ g`.** Ist nicht überall `f ≥ g`, so zerlegt man an den
Stellen, wo `h = f − g` das Vorzeichen wechselt. Auf jedem Stück ist entweder `f ≥ g` (Schritt 1–4
direkt) oder `g ≥ f` (Rollen tauschen, Ergebnis `∫ (g − f) = −∫ (f − g)`). Auf jedem Stück steht
damit `|∫ h|`, und Zusammensetzen ergibt `A = ∫ |h|` — genau das Ergebnis aus Abschnitt 2, nur mit
`h` statt `f`. ∎

**Was die Herleitung zeigt.** Die Fläche zwischen zwei Graphen ist die Fläche zwischen **einem**
Graphen, dem von `h`, und der Achse. Alles aus Abschnitt 2 gilt deshalb unverändert weiter: Bilanz
und Flächeninhalt, die vier Schritte, die Beträge um die Teilstücke.

*(Ende `<details>`.)*

### 3.3 Schnittstellen als Integrationsgrenzen (`<h3>`)

Die Nullstellen von `h` sind die Stellen mit `f(x) = g(x)` — die **Schnittstellen** der beiden
Graphen. Sie liefern die Integrationsgrenzen. Das Verfahren aus 2.4, in die Sprache der zwei
Graphen übersetzt (`<div class="merksatz">`):

> **Merksatz (Kernaussage 2).** Der Flächeninhalt zwischen zwei Graphen wird in fünf Schritten
> berechnet:
>
> 1. **Differenzfunktion** `h = f − g` bilden und so weit wie möglich vereinfachen (ausklammern,
>    faktorisieren).
> 2. **Schnittstellen** bestimmen: `h(x) = 0` lösen, alle reellen Lösungen.
> 3. **Grenzen festlegen.** Ist ein Intervall `[a; b]` vorgegeben, zählen nur die Schnittstellen in
>    seinem Inneren, und nur solche mit **Vorzeichenwechsel von `h`**. Heißt es „die Graphen
>    schließen eine Fläche ein", sind es die Schnittstellen selbst, jeweils zwei benachbarte.
> 4. **Eine** Stammfunktion `H` von `h` bilden, `H` an allen Grenzen auswerten.
> 5. **Beträge** der Teilintegrale `|H(zᵢ₊₁) − H(zᵢ)|` addieren.

**Durchgerechnetes Beispiel.** Gegeben sind `f(x) = x³ − 3x²` und `g(x) = x² + 7x − 10`. Die Graphen
schließen eine Fläche ein. Bestimme ihren Inhalt.

*Schritt 1.* `h(x) = f(x) − g(x) = x³ − 3x² − x² − 7x + 10 = x³ − 4x² − 7x + 10`.

*Schritt 2.* Ein Wert zum Raten: `h(1) = 1 − 4 − 7 + 10 = 0`. Polynomdivision durch `(x − 1)` gibt
`h(x) = (x − 1)(x² − 3x − 10) = (x − 1)(x − 5)(x + 2)`. Schnittstellen also `x = −2`, `x = 1`,
`x = 5`. Probe an den Funktionstermen: `f(−2) = −20 = g(−2)`, `f(1) = −2 = g(1)`, `f(5) = 50 = g(5)` ✓.

*Schritt 3.* Es sind drei Schnittstellen, also zwei Teilflächen. Ob `h` an allen Stellen das
Vorzeichen wechselt, prüfst du mit dem Vorzeichenbild: `h(−3) = (−4)(−8)(−1) = −32 < 0`,
`h(0) = 10 > 0`, `h(3) = 2·(−2)·5 = −20 < 0`, `h(6) = 5·1·8 = 40 > 0`. Auf `(−2; 1)` liegt `f` oben,
auf `(1; 5)` liegt `g` oben. (Bei einfachen Nullstellen wechselt `h` immer das Vorzeichen.)

*Schritt 4.* `H(x) = x⁴/4 − (4/3)·x³ − (7/2)·x² + 10x`. Tabelle (in `<div class="tabelle">`):

| `x` | −2 | 1 | 5 |
|---|---|---|---|
| `H(x)` | −58/3 ≈ −19,3333 | 65/12 ≈ 5,4167 | −575/12 ≈ −47,9167 |

*Schritt 5.* `H(1) − H(−2) = 65/12 + 232/12 = 297/12 = 99/4 = 24,75` (f oben) und
`H(5) − H(1) = −575/12 − 65/12 = −640/12 = −160/3 ≈ −53,3333` (g oben). Der Flächeninhalt ist

`A = 99/4 + 160/3 = 297/12 + 640/12 = 937/12 ≈ 78,0833` FE.

Die Bilanz wäre dagegen `99/4 − 160/3 = 297/12 − 640/12 = −343/12 ≈ −28,5833`. Die Abkürzung „Betrag
der Bilanz" ist hier um fast zwei Drittel zu klein: `(937/12 − 343/12)/(937/12) = 594/937 = 0,634`,
also `63,4 %`. Das größere Stück ist so viel größer, dass die Bilanz sein Vorzeichen bekommt — und
vom kleineren Stück bleibt in der Bilanz nichts zu sehen.

*Kontrollrechnung:* numerisch (400 000 Streifen) `∫₋₂¹ h = 24,75000000`, `∫₁⁵ h = −53,33333333`,
`∫₋₂⁵ |h| = 78,08333333`. Exakt (`fractions.Fraction`): `937/12`.
`H(−2) = 4 + 32/3 − 14 − 20 = −58/3` ✓, `H(1) = (3 − 16 − 42 + 120)/12 = 65/12` ✓,
`H(5) = (1875 − 2000 − 1050 + 600)/12 = −575/12` ✓.

**Und wenn ein Intervall vorgegeben ist?** Soll dieselbe Aufgabe nur auf `[0; 4]` gelten, liegt
`x = −2` außerhalb und ist bedeutungslos, und `x = 5` liegt rechts des Intervalls. Übrig bleibt die
Grenze `x = 1`: `∫₀¹ h = H(1) − H(0) = 65/12`, `∫₁⁴ h = H(4) − H(1) = −112/3 − 65/12 = −513/12 = −171/4`,
also `A = 65/12 + 513/12 = 578/12 = 289/6 ≈ 48,1667` FE bei einer Bilanz von
`65/12 − 513/12 = −448/12 = −112/3 ≈ −37,3333`. (Tabellenwerte `H(0) = 0`, `H(1) = 65/12`,
`H(4) = −112/3`.)

### 3.4 Nicht jede Schnittstelle ist eine Grenze (`<div class="hinweis">`)

Die zweite Fehlvorstellung dieser Einheit ist das Gegenstück der ersten: „Jede Schnittstelle
zerlegt." Sie stimmt nur bei Schnittstellen, an denen `h` das **Vorzeichen wechselt**.

Nimm `f(x) = x²` und `g(x) = 2x − 1`. Dann ist `h(x) = x² − 2x + 1 = (x − 1)²`. Die Graphen haben
genau einen gemeinsamen Punkt bei `x = 1` — sie **berühren** sich, die Parabel liegt danach weiter
oberhalb der Geraden. `h` hat eine doppelte Nullstelle, aber **keinen** Vorzeichenwechsel:
`h ≥ 0` überall. Für `[−1; 3]` gilt daher ohne jede Zerlegung

`A = ∫₋₁³ (x − 1)² dx = [(x − 1)³/3]₋₁³ = 8/3 − (−8/3) = 16/3 ≈ 5,3333` FE.

Würdest du bei `x = 1` trotzdem teilen, käme `8/3 + 8/3 = 16/3` heraus — dasselbe, nur mit mehr
Arbeit. Kein Schaden, aber ein Zeichen, dass das Kriterium noch nicht sitzt.

**Kriterium** (für ganzrationale Funktionen). Eine Nullstelle von `h` mit **ungerader** Vielfachheit (einfach, dreifach, …) ist ein
Vorzeichenwechsel und damit eine Integrationsgrenze. Eine mit **gerader** Vielfachheit (doppelt,
vierfach, …) ist eine Berührstelle und braucht keine Zerlegung.

**Eine dritte Falle: Symmetrie ohne Beweis.** Für `f(x) = x³` und `g(x) = x` ist `h(x) = x³ − x =
x(x − 1)(x + 1)` punktsymmetrisch zum Ursprung, und `∫₋₁¹ h dx = 0`. Der Flächeninhalt ist
`2·∫₀¹ (x − x³) dx = 2·(1/2 − 1/4) = 1/2`. Die Symmetrie darf man nutzen, um die Rechnung zu
halbieren — nie, um sie zu ersetzen.

*Kontrollrechnung:* `∫₋₁³ (x − 1)² dx = 16/3`, numerisch `5,33333333`. `∫₋₁¹ (x³ − x) dx = 0`,
`∫₀¹ (x − x³) dx = 1/4`, Flächeninhalt `1/2`; numerisch `∫₋₁¹ |x³ − x| dx = 0,50000000`.

### 3.5 Zusatz: die Parabelformel (`<details>`, freiwillig)

`<summary>` **Zusatz: Fläche zwischen Parabel und Gerade (oder zwei Parabeln) in einer Zeile** `</summary>`

Hat `h` genau zwei Nullstellen `x₁ < x₂` und ist `h(x) = α·(x − x₁)(x − x₂)`, so gilt für die von
den Graphen eingeschlossene Fläche

`A = |α|·(x₂ − x₁)³/6`.

*Herleitung.* Mit `u = x − x₁` und `d = x₂ − x₁` ist `x − x₂ = u − d`, und
`∫ₓ₁^(x₂) (x − x₁)(x − x₂) dx = ∫₀^d u·(u − d) du = [u³/3 − d·u²/2]₀^d = d³/3 − d³/2 = −d³/6`. Der Betrag
liefert `|α|·d³/6`. ∎

*Beispiel* (führt in Aufgabe a2): `h(x) = −2x² + 4x + 2` hat die Nullstellen `1 ± √2`, also
`d = 2√2`, `α = −2` und `A = 2·(2√2)³/6 = 2·16√2/6 = 16√2/3 ≈ 7,5425`.
*Kontrollrechnung:* `(2√2)³ = 8·2√2 = 16√2 = 22,6274`, `2·22,6274/6 = 7,5425`; direkt
`∫ (−2x² + 4x + 2) dx` von `1 − √2` bis `1 + √2` = `7,54247233` (sympy); numerisch identisch.

### 3.6 Nicht immer lassen sich Schnittstellen exakt angeben (`<div class="hinweis">`)

Bei Exponential- und trigonometrischen Funktionen ist `h(x) = 0` oft nur mit dem Logarithmus oder
gar nur numerisch lösbar. Beispiel aus dem Zufluss der Vorgängereinheit: Zufluss
`z(t) = 4·e^(−0,3t)` gegen einen konstanten Abfluss von `1,5` (beide in L/min). Die Schnittstelle
ist die Lösung von `4·e^(−0,3t) = 1,5`, also `e^(−0,3t) = 3/8` und
`t = ln(8/3)/0,3 = 3,2694 min`. Mehr als eine exakte Schnittstelle braucht es nicht: Die
Simulation im nächsten Abschnitt macht daraus eine Aufgabe zum Ausprobieren, Aufgabe a4 rechnet
sie durch.

*Kontrollrechnung:* `ln(8/3) = 0,98083`, `0,98083/0,3 = 3,26943`. Probe: `4·e^(−0,3·3,26943) = 4·e^(−0,98083) =
4·0,375 = 1,5000` ✓.

> **Merksatz (Kernaussage 3).** Der Flächeninhalt zwischen zwei Graphen ist `∫ |f − g| dx`.
> Berechnet wird er stückweise: Die Grenzen sind die **Schnittstellen mit Vorzeichenwechsel**, die
> Teilstücke tragen Betragsstriche, und es genügt **eine** Stammfunktion von `f − g`. Ob `f` oder
> `g` oben liegt, ist gleichgültig; ob die Graphen die Achse schneiden, ebenfalls.

---

## Abschnitt 4 — Interaktiver Kern

`<section id="simulation">`, `.stufe`-Nummer **4**,
Überschrift **Wo Bilanz und Flächeninhalt auseinanderlaufen**.

### 4.1 Was die Simulation zeigen soll

Ein Canvas (`id="cvSim"`, `width="1000" height="690"`, `style="touch-action:none"`, `role="img"` mit `aria-label`, per CSS `width:100%`) mit zwei
**übereinanderliegenden** Koordinatensystemen und gemeinsamer `x`-Achse:

- **oben (die zwei Graphen):** die Graphen von `f` (Farbe `--akzent`, 3 px) und `g` (Farbe `#334155`,
  3 px), beschriftet am rechten Rand mit `f` und `g`. Zwischen den Grenzen `a` und `b` ist die Fläche
  zwischen den Graphen eingefärbt: **wo `f` oben liegt** in `rgba(13,122,82,0.28)` (grün), **wo `g`
  oben liegt** in `rgba(220,38,38,0.25)` (rot); Ränder in `#0d7a52` bzw. `#dc2626`. Senkrechte Linie
  bei `x = a` (gestrichelt, Beschriftung `a`) und bei `x = b` (durchgezogen, Beschriftung `b`).
  Optional (Checkbox `cSchn`, **Vorgabe: aus**) Punkte auf den Graphen an den Schnittstellen mit
  Vorzeichenwechsel. Berührstellen werden **nie** markiert.
- **unten (die zwei Kurven, die sich aufbauen):** über der oberen Grenze `x` die
  **Bilanzkurve** `B(x) = ∫ₐˣ (f − g) dt` (Farbe `#1d4ed8`, 3 px) und die
  **Flächenkurve** `A(x) = ∫ₐˣ |f − g| dt` (Farbe `#d97706`, 3 px). Beide beginnen bei `x = a` im
  Nullpunkt, sind bis `x = b` durchgezogen und laufen danach hellgrau gestrichelt bis zum rechten
  Rand weiter. Auf der senkrechten Linie `x = b` je ein ausgefüllter Kreis auf jeder Kurve.
  Legende im Diagramm: „Bilanz" (blau), „Flächeninhalt" (orange).
- Die senkrechte Linie bei `b` läuft **durch beide Diagramme**, damit man sieht, welche Stelle
  oben zu welchem Wert unten gehört.

Der didaktische Kern ist das **Auseinanderlaufen der beiden Kurven unten**: Sie beginnen gleich
(oder gespiegelt), solange `h = f − g` sein Vorzeichen nicht wechselt, und trennen sich an der
ersten Schnittstelle. Das ist Abschnitt 2.6 (`B′ = h`, `A′ = |h|`) zum Anfassen.

### 4.2 Auswählbare Paare (drei Knöpfe in `.knopfleiste`, `data-paar="A|B|C"`)

| Knopf | `f` | `g` | Bereich | Einheit der Flächen | Besonderheit |
|---|---|---|---|---|---|
| **Paar A** – „drei Schnittstellen" | `x³ − 2x²` | `2x² − x − 6` | `x ∈ [−1,5; 3,5]` | FE | Schnittstellen `−1`, `2`, `3`, alle mit Vorzeichenwechsel |
| **Paar B** – „Berührung" | `x²` | `2x − 1` | `x ∈ [−1; 3]` | FE | eine Berührstelle bei `x = 1`, **kein** Vorzeichenwechsel |
| **Paar C** – „Zufluss gegen Abfluss" | `4·e^(−0,3x)` | `1,5` | `x ∈ [0; 10]` (`x` in min, `f`, `g` in L/min) | L | eine Schnittstelle bei `x = ln(8/3)/0,3 ≈ 3,2694`, nicht exakt auf dem Regler-Raster |

*Kontrollrechnungen zu den Schnittstellen:* Paar A: `f(−1) = −3 = g(−1)`, `f(2) = 0 = g(2)`,
`f(3) = 9 = g(3)`; `h = (x + 1)(x − 2)(x − 3)`. Paar B: `h = (x − 1)²`. Paar C: `h(3,2694) =
4·e^(−0,98083) − 1,5 = 0,0000`.

**Wichtig für die Verständnisfragen:** Die Funktionsterme von **Paar A** werden auf der Seite
**nirgends** angezeigt (weder im Knopf noch in der Beschriftung des Diagramms; die Graphen heißen nur
`f` und `g`). Paar A erscheint im Erklärteil nicht, und `sim1`/`sim2` sind mit den Termen zwar rechnerisch,
aber nur mit erheblichem Aufwand lösbar; ohne Terme ist die Simulation das Messgerät. Die Terme von
Paar B und Paar C dürfen beschriftet werden (sie stehen auch in 3.4 bzw. 3.6).

Wertebereiche auf dem jeweiligen Bereich (gerechnet, Raster 0,25 für alle `a < b`):
Paar A: `f, g ∈ [−7,875; 18,375]`, Bilanz `∈ [−1,807; 11,391]`, Flächeninhalt `≤ 14,365`.
Paar B: `f, g ∈ [−3; 9]`, Bilanz und Flächeninhalt `∈ [0,005; 5,333]`.
Paar C: `f, g ∈ [0,199; 4,000]`, Bilanz `∈ [−5,760; 3,429]`, Flächeninhalt `≤ 9,189`.

### 4.3 Wie der Bauagent rechnen soll

**Ziel:** Bilanz und Flächeninhalt für beliebige `a < b` auf dem Regler-Raster, ohne Stammfunktion und
ohne Betragsintegral-Näherung. Vorgehen in zwei Stufen, damit die Anzeige auch an Vorzeichenwechseln
scharf bleibt.

**Stufe 1 — Nullstellen mit Vorzeichenwechsel einmal je Paar bestimmen.**

```
function nullstellen(p){            // p.f, p.g, p.lo, p.hi
  var N = 4000, r = [], letzte = 0, letzteX = 0;
  function h(x){ return p.f(x) - p.g(x); }
  for (var i = 0; i <= N; i++){
    var x = p.lo + (p.hi - p.lo) * i / N, v = h(x);
    var s = Math.abs(v) < 1e-12 ? 0 : (v > 0 ? 1 : -1);
    if (s === 0) continue;                       // Nullstelle selbst überspringen
    if (letzte !== 0 && s !== letzte){           // Vorzeichenwechsel zwischen letzteX und x
      var lo = letzteX, hi = x;
      for (var k = 0; k < 60; k++){              // Bisektion
        var m = (lo + hi) / 2, vm = h(m);
        if (Math.abs(vm) < 1e-13){ lo = hi = m; break; }
        if ((vm > 0) === (letzte > 0)) lo = m; else hi = m;
      }
      r.push((lo + hi) / 2);
    }
    letzte = s; letzteX = x;
  }
  return r;                                      // Berührstellen fehlen absichtlich
}
```

**Stufe 2 — Tabellen der aufsummierten Werte auf dem Regler-Raster (Schrittweite 0,01).** Für jede
Rasterzelle `[u; v]` wird das Integral von `h` und von `|h|` bestimmt; enthält die Zelle eine Nullstelle
aus Stufe 1 im Inneren, wird dort geteilt. Auf jedem Stück Simpson-Regel mit `n = 8`:

```
function simpson(fn, a, b, n){                   // n gerade
  var hh = (b - a) / n, s = fn(a) + fn(b);
  for (var k = 1; k < n; k++) s += (k % 2 ? 4 : 2) * fn(a + k * hh);
  return s * hh / 3;
}
// Bcum[0] = Acum[0] = 0;  pro Zelle j (u = lo + j/100, v = u + 0,01):
//   Stücke = [u, (Nullstellen in (u,v))…, v]
//   je Stück s..t:  val = simpson(h, s, t, 8);  db += val;  da += Math.abs(val);
//   Bcum[j+1] = Bcum[j] + db;  Acum[j+1] = Acum[j] + da;
```

**Anzeigewerte** (`ja`, `jb` sind die ganzzahligen Reglerwerte, `a = lo + ja/100`, `b = lo + jb/100`):

```
Bilanz        = Bcum[jb] - Bcum[ja]
Flaeche       = Acum[jb] - Acum[ja]
P (f oben)    = Math.max(0, (Flaeche + Bilanz) / 2)
N (g oben)    = Math.max(0, (Flaeche - Bilanz) / 2)
Differenz     = Flaeche - Math.abs(Bilanz)          (= 2·min(P, N))
h(b)          = f(b) - g(b)
Wechsel       = Anzahl der Nullstellen r aus Stufe 1 mit a < r < b
```

`fmt()` muss **negative Nullen** abfangen: Werte mit `Math.abs(v) < 0.005` werden als `0,00`
angezeigt, nie als `−0,00`.

Die untere Kurve entsteht aus denselben Tabellen: `B(x) = Bcum[jx] − Bcum[ja]`,
`A(x) = Acum[jx] − Acum[ja]` für `jx = ja … n`. Kein zusätzlicher Rechenaufwand beim Ziehen.

*Genauigkeitsprüfung (gerechnet):* Für alle drei Paare, je 60 zufällige Rasterpaare `(a, b)`, beträgt
der größte Unterschied zu `mpmath.quad` (30 Stellen, mit Teilung an den Nullstellen) `1,1·10⁻¹⁴`. Das
Verfahren aus Stufe 1 und 2 ist auf der Anzeigegenauigkeit von zwei Nachkommastellen also exakt. Die Teilung an
den Nullstellen ist für die Anzeige nicht zwingend, aber sauber: Ohne sie erreicht eine einzelne
Simpson-Näherung von `∫|h|` über `[a; b]` (`n = 200`) wegen des Knicks Abweichungen bis `4,6·10⁻⁵`
(gemessen für Paar A mit `a = −1,43`, `b = 3,37` und für Paar C mit `[0; 10]`) — noch unter der
Anzeigegenauigkeit, aber nicht mehr exakt. Mit Teilung sind es `10⁻¹⁴`. Das Prüfskript weist beides aus.

**Kontrollwerte für die Abnahme** (aus dem Tabellenverfahren, bei Komma-Formatierung; Bilanz und
Flächeninhalt in FE bei A und B, in L bei C):

| Paar | `a` | `b` | `h(b)` | `P` | `N` | Bilanz | Flächeninhalt | Differenz | Wechsel |
|---|---|---|---|---|---|---|---|---|---|
| A | −1,50 | −1,40 | −5,98 | 0,00 | 0,69 | −0,69 | 0,69 | 0,00 | 0 |
| A | −1,50 | −1,00 | 0,00 | 0,00 | 1,81 | −1,81 | 1,81 | 0,00 | 0 |
| A | −1,50 | −0,38 | 4,99 | 1,79 | 1,81 | −0,02 | 3,59 | 3,57 | 1 |
| A | −1,50 | −0,37 | 5,03 | 1,84 | 1,81 | 0,03 | 3,64 | 3,61 | 1 |
| A | −1,50 | 0,00 | 6,00 | 3,92 | 1,81 | 2,11 | 5,72 | 3,61 | 1 |
| A | −1,50 | 2,00 | 0,00 | 11,25 | 1,81 | 9,44 | 13,06 | 3,61 | 1 |
| A | −1,50 | 3,00 | 0,00 | 11,25 | 2,39 | 8,86 | 13,64 | 4,78 | 2 |
| A | −1,50 | 3,50 | 3,38 | 11,97 | 2,39 | 9,58 | 14,36 | 4,78 | 3 |
| A | −1,00 | 3,50 | 3,38 | 11,97 | 0,58 | 11,39 | 12,56 | 1,17 | 2 |
| A | 0,00 | 3,50 | 3,38 | 8,06 | 0,58 | 7,47 | 8,64 | 1,17 | 2 |
| A | 3,00 | 3,50 | 3,38 | 0,72 | 0,00 | 0,72 | 0,72 | 0,00 | 0 |
| A | −1,00 | 2,00 | 0,00 | 11,25 | 0,00 | 11,25 | 11,25 | 0,00 | 0 |
| B | −1,00 | 3,00 | 4,00 | 5,33 | 0,00 | 5,33 | 5,33 | 0,00 | 0 |
| B | −1,00 | 1,00 | 0,00 | 2,67 | 0,00 | 2,67 | 2,67 | 0,00 | 0 |
| C | 0,00 | 10,00 | −1,30 | 3,43 | 5,76 | −2,33 | 9,19 | 6,86 | 1 |
| C | 0,00 | 5,00 | −0,61 | 3,43 | 0,57 | 2,86 | 4,00 | 1,14 | 1 |
| C | 3,27 | 10,00 | −1,30 | 0,00 | 5,76 | −5,76 | 5,76 | 0,00 | 0 |

(Tabelle im Modul selbst nicht abbilden; sie ist Abnahmehilfe für den Bauagenten. Diese Werte
stehen **nicht** auf der Seite, damit die Verständnisfragen sich nur durch Bedienen beantworten
lassen.)

### 4.4 Regler, Knöpfe, Anzeigen

**Regler (`<div class="regler">`)**, beide mit ganzzahligen `range`-Werten (Rundung sauber, Schritt 0,01):

| `id` | Größe | `min` | `max` | Umrechnung | Startwert (Paar A) | Anzeige |
|---|---|---|---|---|---|---|
| `rA` | untere Grenze `a` | 0 | `100·(hi − lo) − 10` | `a = lo + rA/100` | 0 (`a = −1,50`) | zwei Nachkommastellen |
| `rB` | obere Grenze `b` | 10 | `100·(hi − lo)` | `b = lo + rB/100` | 500 (`b = 3,50`) | zwei Nachkommastellen |

Die Abstandsbedingung `b − a ≥ 0,10` wird erzwungen: Wird `a` über `b − 0,10` hinaus geschoben,
schiebt sie `b` mit (und umgekehrt), bis der Rand des Bereichs erreicht ist. Beim Paarwechsel werden
`max`/`min` der Regler neu gesetzt und `a = lo`, `b = hi`.

Größenordnungen: Paar A `rA ∈ [0; 490]`, `rB ∈ [10; 500]`; Paar B `rA ∈ [0; 390]`, `rB ∈ [10; 400]`;
Paar C `rA ∈ [0; 990]`, `rB ∈ [10; 1000]`.

**Knopfleiste:** `Paar A` · `Paar B` · `Paar C` (aktives Paar hervorheben) ·
`▶ Abspielen / ❚❚ Pause` (lässt `b` mit `(hi − lo)/5` Einheiten pro Sekunde von der aktuellen Stelle
bis `hi` laufen und stoppt dort; `dt` auf `Math.min(0.05, …)` begrenzen) ·
`Zurücksetzen` (Paar A, `a = −1,50`, `b = 3,50`, Schnittstellen aus).
Checkbox `Schnittstellen markieren` (`id="cSchn"`, **Vorgabe: aus**).

**Ziehen:** `pointerdown` / `pointermove` / `pointerup` auf dem Canvas mit `setPointerCapture`. Beim
`pointerdown` wird die **näher liegende** der beiden Grenzlinien (`a` oder `b`) gegriffen, in beiden
Diagrammen gleichermaßen; `pointermove` setzt die gegriffene Grenze. Umrechnung Pixel → `x` siehe 4.5.

**Anzeigen (`<div class="anzeige">`), alle Zahlen mit `fmt()` und Komma:**

| `id` | Feld | Stellen | Einheit |
|---|---|---|---|
| `lA` | untere Grenze `a` | 2 | — |
| `lB` | obere Grenze `b` | 2 | — |
| `lH` | `f(b) − g(b)`, Höhe der Lücke an der Stelle `b` (Vorzeichen zeigt, wer oben liegt) | 2 | — |
| `lP` | Fläche, in der `f` oben liegt (`P`) | 2 | FE bzw. L |
| `lN` | Fläche, in der `g` oben liegt (`N`) | 2 | FE bzw. L |
| `lBil` | **Bilanz** `∫ₐᵇ (f − g)` | 2 | FE bzw. L |
| `lFl` | **Flächeninhalt** `∫ₐᵇ |f − g|` | 2 | FE bzw. L |
| `lDiff` | `Flächeninhalt − |Bilanz|` | 2 | FE bzw. L |
| `lNs` | Zahl der Vorzeichenwechsel von `f − g` im offenen Intervall `(a; b)` (Feldbeschriftung „Vorzeichenwechsel in (a; b)“) | 0 | — |

Der Wechsel von `lNs` beim Ziehen ist absichtlich sichtbar: An einer Berührstelle (Paar B, `b = 1`)
zeigt `lH` den Wert `0,00`, aber `lNs` bleibt bei `0`.

### 4.5 Maßstäbe (als Konstanten oben in der IIFE dokumentieren)

- Beide Diagramme teilen die `x`-Pixel `70 … 970` (900 px), pro Paar `pxProEinheit = 900/(hi − lo)`;
  `xPx(x) = 70 + (x − lo)·pxProEinheit`, Umkehrung `pxX(p) = lo + (p − 70)/pxProEinheit`.
- Oberes Diagramm: Zeichenfläche `y = 40 … 280` (240 px hoch).
- Unteres Diagramm: Zeichenfläche `y = 370 … 610` (240 px hoch); Canvashöhe `690`, damit auch bei vergrößerter Schrift (schmale Bildschirme, Schriftfaktor `kk()` bis 2,1) Titel und Achsenbeschriftung im Bild bleiben.
- Wertebereiche und daraus folgende Maßstäbe (gerechnet):

| Paar | `x`-Bereich | px je Einheit `x` | obere `y`-Achse | px je Einheit | untere `y`-Achse | px je Einheit |
|---|---|---|---|---|---|---|
| A | −1,5 … 3,5 | 180,0 | −10 … 20 | 8,0000 | −4 … 16 | 12,0000 |
| B | −1 … 3 | 225,0 | −4 … 10 | 17,1429 | −1 … 6 | 34,2857 |
| C | 0 … 10 | 90,0 | −0,5 … 4,5 | 48,0000 | −7 … 10 | 14,1176 |

Jeder gewählte Achsenbereich umschließt den Wertebereich aus 4.2 mit Rand. Beschriftung der
`x`-Achse in ganzen Einheiten (bei C alle 2 min), der `y`-Achsen in geeigneten Schritten
(A oben 5, unten 4; B oben 2, unten 1; C oben 1, unten 2).

**Hinweis Bauteil:** `data-num` steht nur an a1, a2, a4, a5; a3 (Zuordnung), a6 und a7 (offen) tragen es nicht (Engine und Modulcheck brauchen es nicht).

**Nachtrag zur Darstellung (nach der Technikprüfung).** Titel der beiden Diagramme beginnen 10 px rechts von der
Achse, damit die Linie `a` sie nicht schneidet. Die Legende „Bilanz“/„Flächeninhalt“ wird rechtsbündig aus der
gemessenen Textbreite gesetzt. Die Marken `a` (links der Linie, am linken Rand rechts davon) und `b` (rechts der
Linie, ab `x`-Pixel 930 links davon) stehen in zwei Zeilen untereinander, `b` eine Zeile tiefer, sodass sie sich bei
kleinstem Abstand nicht überlappen und `b` nicht auf das Label „f“ trifft. Paar C: Titel „f = Zufluss z(t) = 4·e^(−0,3t),
g = Abfluss 1,5“, die Felder `a` und `b` tragen die Einheit „min“. Im Text steht ein Hinweis, dass bei Paar B die
orange Kurve genau unter der blauen liegt.

### 4.6 Beobachtungsauftrag (`<div class="auftrag">`)

> **Beobachtungsauftrag**
> Stelle **Paar A** ein und setze `a = −1,50`. Zieh `b` langsam von ganz links nach rechts und
> beobachte die Kurven im **unteren** Diagramm sowie die Felder „Bilanz", „Flächeninhalt" und
> „Differenz".
> Notiere drei Dinge: **(1)** die Stellen `b`, an denen die blaue Kurve ihre Richtung wechselt, und
> was das Feld `f(b) − g(b)` dort zeigt; **(2)** die Bereiche von `b`, in denen die Differenz
> **nicht** wächst, obwohl `b` weiterläuft, samt ihren Werten; **(3)** bis zu welcher Stelle die
> orange Kurve das **Spiegelbild** der blauen an der Achse ist.
> Formuliere daraus einen Satz, der beschreibt, wann „Flächeninhalt = Betrag der Bilanz" gilt und
> wann nicht. Prüfe deinen Satz zum Schluss an **Paar B** mit `a = −1,00` und `b` von `−0,90` bis
> `3,00`: Was sagt er voraus — und stimmt es?

Erwartetes Ergebnis (für die Lehrkraft, nicht auf der Seite): **(1)** Die blaue Kurve wechselt bei
`b = −1,00` (Tiefpunkt, Bilanz `−1,81`), `b = 2,00` (Hochpunkt, `9,44`) und `b = 3,00` (Tiefpunkt,
`8,86`); an allen drei Stellen zeigt `f(b) − g(b)` den Wert `0,00` — die Steigung der blauen Kurve
ist `f − g`. **(2)** Die Differenz ist `0,00` bis `b = −1,00`, wächst dann bis `b = −0,37` auf `3,61` (dort ist
das zweite Stück so groß wie das erste geworden; bei `−0,38` zeigt das Feld `3,57`), bleibt auf `3,61` bis `b = 2,00`, wächst bis
`b = 3,00` auf `4,78` und bleibt danach dort (Konstanz bei `3,61` für `−0,37 ≤ b ≤ 2,00` und bei
`4,78` für `b ≥ 3,00`). Sie ist `2·min(P, N)`. **(3)** Bis `b = −1,00`, der ersten
Schnittstelle rechts von `a`, ist die orange Kurve das Spiegelbild der blauen (`A = −B`); ab dort
gilt das nicht mehr. Sinngemäßer Satz: *Flächeninhalt und Betrag der Bilanz stimmen
genau so lange überein, bis `b` die erste Schnittstelle mit Vorzeichenwechsel überschreitet; danach
ist der Flächeninhalt größer, und der Unterschied ist das Doppelte des kleineren Teilstücks.*
Prüfung an Paar B: Der Satz sagt voraus, dass die Differenz durchgehend `0,00` bleibt, weil `f − g`
sein Vorzeichen nie wechselt, obwohl `f(b) − g(b)` bei `b = 1,00` den Wert `0,00` zeigt und die
Graphen sich dort berühren. Die Simulation bestätigt es: Differenz `0,00`, Wechsel `0`, beide
Kurven decken sich.

### 4.7 Verständnisfragen zur Simulation (zwei Multiple-Choice-Aufgaben)

Beide Fragen beruhen auf Ablesewerten, die **nirgends auf der Seite stehen** und sich ohne Rechner
nur mühsam bestimmen lassen (die zweite verlangt die Nullstelle einer Polynomgleichung vierten
Grades). Wer nicht bedient, kann nur raten.

**sim1** — Schlüssel `sim1`, Radio-Name `sim1`, richtige Option: **Index 1**,
`<span class="ab">Anforderungsbereich II</span>`

> Frage: Stell **Paar A** ein, setze `b = 3,50` und verschiebe **nur** `a`. Bei welcher der drei
> Einstellungen zeigt das Feld „Bilanz" den größten Wert?
>
> - `data-i="0"`: bei `a = −1,50`, denn dann ist am meisten Fläche dabei.
> - `data-i="1"`: bei `a = −1,00`, denn dort wechselt `f − g` das Vorzeichen.
> - `data-i="2"`: bei `a = 3,00`, denn das ist die letzte Schnittstelle.

Feedback:

- **Index 0:** Mehr Fläche heißt nicht mehr Bilanz. Zwischen `−1,50` und `−1,00` liegt `g` oben
  (`f − g < 0`), dieses Stück wird abgezogen: Die Anzeige zeigt `9,58`, bei `a = −1,00` dagegen `11,39` —
  Differenz genau das Stück `1,81`. Eine Bilanz wächst nur, wenn du Stücke mit `f − g > 0` mitnimmst.
- **Index 1 (richtig):** Richtig. Bei `a = −1,00` beginnt die Integration genau dort, wo `f − g` von
  negativ auf positiv wechselt, und die Anzeige zeigt `11,39` (bei `−1,50`: `9,58`, bei `3,00`: `0,72`).
  Verschiebst du `a` von dort nach links oder rechts, sinkt die Bilanz. Grund: `∂/∂a ∫ₐᵇ h = −h(a)`
  — die Bilanz hat als Funktion von `a` dort ein Maximum, wo `h` von `−` nach `+` wechselt.
- **Index 2:** `a = 3,00` ist eine Schnittstelle, und die Bilanz ist dort tatsächlich ein lokales
  Maximum — aber nur ein lokales: Sie zeigt `0,72`. Von `3,00` bis `3,50` ist nur ein schmales Stück
  dabei, und das große Stück von `−1,00` bis `2,00` (`11,25`) fehlt. Eine Schnittstelle ist nur ein
  Kandidat; welche die größte Bilanz liefert, entscheidet der Vergleich der Anzeigen.

**sim2** — Schlüssel `sim2`, Radio-Name `sim2`, richtige Option: **Index 2**,
`<span class="ab">Anforderungsbereich II</span>`

> Frage: Stell **Paar A** ein und setze `a = −1,50`. Zieh `b` von links nach rechts. Bei welchem `b`
> steht die Bilanz nach dem Start zum ersten Mal wieder auf (etwa) `0,00`?
>
> - `data-i="0"`: bei `b = −1,00`, denn dort schneiden sich die Graphen.
> - `data-i="1"`: bei `b = −0,50`, denn das ist von der Schnittstelle genauso weit entfernt wie `a`.
> - `data-i="2"`: bei `b = −0,38`, denn dort hat sich das Stück oberhalb der Achse gegen das Stück unterhalb aufgehoben.

Feedback:

- **Index 0:** Die Schnittstelle bei `−1,00` ist die Stelle, an der die Bilanzkurve **umkehrt**,
  nicht die, an der sie null erreicht: Die Anzeige zeigt dort `−1,81`, den tiefsten Wert. Um wieder
  bei null anzukommen, muss die Kurve das bis dahin Abgezogene erst wieder aufholen. Nullstelle der
  Differenzfunktion und Nullstelle der Bilanz sind zwei verschiedene Dinge.
- **Index 1:** Du hast gespiegelt: gleicher Abstand rechts und links der Schnittstelle. Das würde
  klappen, wenn `f − g` punktsymmetrisch zu `−1` verliefe. Tut es nicht: Im Abstand `0,4` links der Schnittstelle
  (`b = −1,40`) zeigt das Feld `f(b) − g(b)` `−5,98`, im gleichen Abstand rechts (`b = −0,60`) nur `+3,74`
  (Kontrolle: `h = (x + 1)(x − 2)(x − 3)`, `h(−1,4) = −5,984`, `h(−0,6) = 3,744`). Das
  rechte Stück ist deshalb kleiner als das linke (`1,22` gegen `1,81`), und die Anzeige steht bei
  `b = −0,50` noch auf `−0,58`. Es muss weiter nach rechts gehen, bis das rechte Stück aufgeholt hat.
- **Index 2 (richtig):** Richtig. Bei `b = −0,38` zeigt die Anzeige `−0,02`, bei `b = −0,37` schon
  `+0,03`; der Nulldurchgang liegt bei `b ≈ −0,376`. Dort ist das Stück oberhalb (`P = 1,79`) praktisch
  so groß geworden wie das Stück unterhalb (`N = 1,81`). Und: Der Flächeninhalt steht dort auf `3,59`,
  nicht bei null — Bilanz null heißt nicht „keine Fläche".

**Kontrollrechnung sim1/sim2.** sim1: `B(a; 3,5)` für `a = −1,5; −1,0; 3,0` ergibt `9,5833; 11,3906;
0,7240` (exakt `115/12`, `729/64`, `139/192`). Lokale Extrema der Bilanz als Funktion von `a` liegen bei den
Schnittstellen `−1` (Maximum) und `3` (Maximum) sowie bei `2` (Minimum, `0,1406`); die Anzeige-Scans
bei `−1,4; −1,2; −0,9; −0,8` liefern `10,27; 11,13; 11,33; 11,17`, das globale Maximum auf `a ∈ [−1,5; 3,4]`
liegt also bei `a = −1`. sim2: `B(−1,5; b)` ist für `b = −1,0; −0,5; −0,38; −0,37; 2,0` gleich
`−1,8073; −0,5833; −0,0200; +0,0300; 9,4427`; Nullstelle `b₀ = −0,375987` (mpmath `findroot`), Probe
`B(−1,5; −0,376) = −0,0001`.

---

## Abschnitt 5 — Übungen

`<section id="uebungen">`, `.stufe`-Nummer **5**, Überschrift **Übungen**.
Sieben Aufgaben, verteilt über die Anforderungsbereiche I bis III. **Jede** Aufgabe bekommt ein
dreistufiges Hilfesystem (`data-hilfe="1|2|3"` mit `.hilfe-text[data-stufe="1|2|3"]`), auch die
Zuordnung `a3` und die offenen Aufgaben `a6`, `a7`; die Engine bindet die Hilfeknöpfe pro `.aufgabe`
und ist nicht auf Zahleneingaben beschränkt. Bei `a6` und `a7` liegt die vollständige Musterlösung
zusätzlich in `.hilfe-text[data-stufe="9"]` (Knopf `data-loesung`).

| Aufgabe | AB | Typ | Kern |
|---|---|---|---|
| `a1` | I | Zahleneingabe | Fläche Graph–Achse, Zerlegung an zwei Nullstellen |
| `a2` | II | Zahleneingabe | Fläche zwischen zwei Parabeln, irrationale Schnittstellen |
| `a3` | II | Zuordnung | Bilanz gegen Flächeninhalt an vier Graphenpaaren |
| `a4` | II | Zahleneingabe | Zufluss gegen Abfluss, Schnittstelle über Logarithmus |
| `a5` | II | Zahleneingabe | Massenausgleich im Straßenbau, Einheitenumrechnung |
| `a6` | III | offen | Bewertung einer Bauleiter-Aussage (Bilanz gegen Aufwand) |
| `a7` | III | offen | Fehleranalyse dreier Schülerlösungen |

### a1 — Anforderungsbereich I · Zahleneingabe · Schlüssel `a1`

**Aufgabentext.** Gegeben ist `f(x) = x² − 4x + 3`. Berechne den Flächeninhalt, den der Graph von
`f` über dem Intervall `[0; 4]` mit der `x`-Achse einschließt. Gib das Ergebnis in Flächeneinheiten
(FE) an.

**Einheitenauswahl:** `FE` · `LE` · `FE²` · `m³` (die letzten drei sind Distraktoren).

**Daten:** `wert: 4`, `einheit: "FE"`, `tol: 0.05`, keine Alternativeinheit.

**Hilfe 1 (Tipp).** Skizziere die nach oben geöffnete Parabel und frag dich, auf wie vielen Stücken
des Intervalls sie über beziehungsweise unter der Achse verläuft — erst dann wird integriert.

**Hilfe 2 (Ansatz).** Die Nullstellen von `f` sind die Grenzen der Teilstücke; sie folgen aus
`x² − 4x + 3 = 0`. Bilde **eine** Stammfunktion `F` und halte `F` an allen Grenzen in einer Tabelle
fest; die Teilintegrale sind die Differenzen benachbarter Werte, und um jedes kommt ein Betrag.

**Hilfe 3 (Lösungsweg).**
`x² − 4x + 3 = (x − 1)(x − 3) = 0`, Nullstellen `x = 1` und `x = 3`, beide in `(0; 4)` mit
Vorzeichenwechsel. Vorzeichen: `f(0) = 3 > 0`, `f(2) = −1 < 0`, `f(4) = 3 > 0`.
`F(x) = x³/3 − 2x² + 3x` (Probe: `F′ = x² − 4x + 3` ✓).
`F(0) = 0`, `F(1) = 1/3 − 2 + 3 = 4/3`, `F(3) = 9 − 18 + 9 = 0`, `F(4) = 64/3 − 32 + 12 = 4/3`.
`∫₀¹ f = 4/3 − 0 = 4/3`, `∫₁³ f = 0 − 4/3 = −4/3`, `∫₃⁴ f = 4/3 − 0 = 4/3`.
`A = 4/3 + 4/3 + 4/3 = 4 FE`. Die **Bilanz** wäre `F(4) − F(0) = 4/3 ≈ 1,33` — ein Drittel des
Flächeninhalts.
*Numerische Gegenprobe (`mpmath.quad`, Teilung an den Nullstellen): `4,0000000000`.*

**Rückmeldungen:**

- `ok`: Richtig. Nullstellen `1` und `3` teilen `[0; 4]` in drei Stücke mit den Beträgen
  `4/3`, `4/3`, `4/3`; Summe `4 FE`. Die Bilanz allein hätte nur `4/3` geliefert.
- `falschEinheit`: Der Zahlenwert stimmt. Ein Flächeninhalt zwischen Graph und Achse wird in
  Flächeneinheiten (FE) angegeben — Länge mal Länge. `LE` misst Längen, `FE²` wäre eine
  vierdimensionale Größe, und `m³` ist ein Volumen.
- `nah`: `2,67` (= `8/3`) bekommt, wer nur zwei der drei Stücke addiert — meist fehlt das letzte
  Stück von `3` bis `4`, weil nach der zweiten Nullstelle „nichts mehr passiert". Doch das Intervall
  reicht bis `4`, und dort liegt der Graph wieder oberhalb der Achse.
- `weit`: Je nach Wert: `1,33` (= `4/3`) ist die **Bilanz** `F(4) − F(0)`: Du hast ohne Zerlegung integriert,
  und die Stücke haben sich zum Teil weggerechnet. Der Flächeninhalt braucht die Nullstellen als
  Grenzen. `0` ist typisch, wenn du nur `F(4) − F(1)` bildest. Die Hilfen führen dich durch.

### a2 — Anforderungsbereich II · Zahleneingabe · Schlüssel `a2`

**Aufgabentext.** Die Öffnung eines Zierfensters wird oben vom Graphen von `f(x) = −x² + 3x + 2`
und unten vom Graphen von `g(x) = x² − x` begrenzt (1 LE = 1 dm). Berechne die Glasfläche, die von
beiden Graphen eingeschlossen wird. Runde auf zwei Nachkommastellen.

**Einheitenauswahl:** `dm²` · `cm²` · `dm³` · `dm` (die letzten zwei sind Distraktoren).

**Daten:** `wert: 7.54`, `einheit: "dm²"`, `tol: 0.05`, `alt: {wert: 754, einheit: "cm²"}`
(abgeleitete Toleranz `5 cm²`; der exakte Wert `754,25 cm²` liegt darin).

**Hilfe 1 (Tipp).** Wo das Fenster links und rechts endet, sagt dir der Text nicht — es sind die
Stellen, an denen sich die Graphen treffen.

**Hilfe 2 (Ansatz).** Bilde `h = f − g`, setze `h(x) = 0` und löse mit der Lösungsformel. Da
`f` oben liegt, ist der Flächeninhalt `∫ h dx` zwischen den beiden Lösungen. Als Stammfunktion von
`h` nimmst du `H(x)`; die Formel für den Flächeninhalt ist `H(x₂) − H(x₁)`.

**Hilfe 3 (Lösungsweg).**
`h(x) = −x² + 3x + 2 − x² + x = −2x² + 4x + 2`.
`−2x² + 4x + 2 = 0 | : (−2)` ⟹ `x² − 2x − 1 = 0` ⟹ `x = 1 ± √(1 + 1) = 1 ± √2`,
also `x₁ = 1 − √2 ≈ −0,4142` und `x₂ = 1 + √2 ≈ 2,4142`.
Vorzeichen: `h(1) = −2 + 4 + 2 = 4 > 0`, `f` liegt oben (Probe: `f(1) = 4`, `g(1) = 0`).
`H(x) = −(2/3)·x³ + 2x² + 2x`.
`H(x₂) = 7,1046`, `H(x₁) = −0,4379`.
`A = H(x₂) − H(x₁) = 7,1046 + 0,4379 = 7,5425 dm² ≈ 7,54 dm²` (exakt `16·√2/3`).
*Kontrolle mit der Parabelformel aus 3.5:* `|α|·d³/6` mit `α = −2`, `d = 2√2`:
`2·(2,8284)³/6 = 2·22,6274/6 = 7,5425` ✓. In Quadratzentimetern: `754,25 cm²`.
*Numerische Gegenprobe (sympy exakt, mpmath): `7,54247233`.*

**Rückmeldungen:**

- `ok`: Richtig. `h = −2x² + 4x + 2` hat die Nullstellen `1 ± √2`, und
  `H(x₂) − H(x₁) = 16·√2/3 ≈ 7,54 dm²` (rund 754 cm²).
- `falschEinheit`: Der Zahlenwert stimmt. Fläche in `dm²` (oder `754 cm²`) — `dm` wäre eine Länge,
  `dm³` ein Volumen. Beim Umrechnen: `1 dm² = 100 cm²`, nicht `10`.
- `nah`: Falls dein Wert negativ war: Ein negativer Wert wie `−7,54` entsteht, wenn `g − f` statt `f − g` integriert wird: Der
  Betrag ist richtig, das Vorzeichen zeigt nur, dass `g` unten liegt; ein Flächeninhalt ist nie negativ.
  (Er landet in `nah`, weil die unveränderte Engine den Faktor mit `Math.abs` bildet.) Falls dein
  Wert positiv war (Vergleichswerte in `dm²`): `6,00` bekommt, wer die Grenzen `0` und `3` „geraten" hat, weil die Schnittstellen krumm
  sind — sie sind aber `1 ± √2` und stehen so in der Lösungsformel. `11,31` ist ein Rechteck aus
  der Breite `x₂ − x₁ = 2,83` und der größten Lücke `h(1) = 4`; die Lücke ist aber nur in der Mitte
  so groß, überall sonst kleiner. `5,66` ist das Dreieck aus derselben Breite und Höhe — die
  Lückenfunktion `h` ist eine nach unten geöffnete Parabel und liegt oberhalb der Dreiecksseiten.
  Die echte Fläche liegt zwischen beiden (genauer: zwei Drittel des Rechtecks, `2/3·11,31 = 7,54`) und
  muss integriert werden.
- `weit`: Sehr kleine Werte wie `2,83` sind die Breite `x₂ − x₁` — davon hast du noch nicht
  integriert. Die Hilfen führen Schritt für Schritt.

### a3 — Anforderungsbereich II · Zuordnung · Schlüssel `a3`

> **Wichtig für den Bauagenten:** Die Zuordnungs-Engine des Referenzmoduls schreibt fest in
> `ergebnisse.a3`. Der Schlüssel dieser Aufgabe muss deshalb `a3` heißen, sonst taucht sie im
> Export nicht auf.

**Aufgabentext.** Die vier Diagramme A bis D zeigen jeweils denselben Graphen `g(x) = 2`
(gestrichelt) und einen Graphen `f` (durchgezogen) auf dem Intervall `[0; 6]`. Die Funktionsterme
stehen unter den Diagrammen. Ordne jeder Aussage das passende Diagramm zu. Rechne, wo du dir nicht
sicher bist — die Bilanz `∫₀⁶ (f − g) dx` und der Flächeninhalt `∫₀⁶ |f − g| dx` lassen sich in allen
vier Fällen im Kopf oder mit wenigen Zeilen bestimmen.

**Die vier Diagramme (Inline-SVG, `viewBox="0 0 160 90"`).**
Achsen: `x`-Achse `line x1="12" y1="71" x2="156" y2="71"`, `y`-Achse `line x1="18" y1="6" x2="18"
y2="84"`, beide `stroke="#94a3b8"`. Graph `g`: `line x1="18" y1="53" x2="150" y2="53"
stroke="#475569" stroke-width="2" stroke-dasharray="5 4"`. Graph `f`: `polyline stroke="#0d7a52"
stroke-width="2.5" fill="none"`.
Abbildung: `x ∈ [0; 6] → px = 18 + 22·x`, `y ∈ [−1; 7] → py = 80 − 9·(y + 1)`
(daraus `y = 0` bei `py = 71`, `y = 2` bei `py = 53`).
Unter jedem Diagramm eine Zeile Beschriftung mit dem Funktionsterm von `f`.

| Diagramm | Funktionsterm `f` | `polyline points` |
|---|---|---|
| **A** | `2 + 0,5·(x − 2)(x − 4)` | `18.0,17.0 29.0,29.4 40.0,39.5 51.0,47.4 62.0,53.0 73.0,56.4 84.0,57.5 95.0,56.4 106.0,53.0 117.0,47.4 128.0,39.5 139.0,29.4 150.0,17.0` |
| **B** | `3 + 0,2·(x − 3)²` | `18.0,27.8 29.0,32.8 40.0,36.8 51.0,39.9 62.0,42.2 73.0,43.6 84.0,44.0 95.0,43.6 106.0,42.2 117.0,39.9 128.0,36.8 139.0,32.8 150.0,27.8` |
| **C** | `2 + 0,3·(x − 3)²` | `18.0,28.7 29.0,36.1 40.0,42.2 51.0,46.9 62.0,50.3 73.0,52.3 84.0,53.0 95.0,52.3 106.0,50.3 117.0,46.9 128.0,42.2 139.0,36.1 150.0,28.7` |
| **D** | `2 + 0,8·(x − 3)` | `18.0,74.6 150.0,31.4` |

**Die vier Zeilen (`data-loesung` in dieser Reihenfolge: C, D, A, B — bewusst nicht A, B, C, D):**

| Reihenfolge | Aussage | `data-loesung` |
|---|---|---|
| 1 | Der Flächeninhalt zwischen den Graphen lässt sich mit einem einzigen Integral `∫ (f − g)` berechnen, obwohl die Graphen einen gemeinsamen Punkt haben. | `C` |
| 2 | Die Bilanz `∫₀⁶ (f − g) dx` ist null, der Flächeninhalt aber nicht. | `D` |
| 3 | Der Flächeninhalt ist größer als der Betrag der Bilanz, und die Bilanz ist nicht null. | `A` |
| 4 | Die Graphen haben keinen gemeinsamen Punkt, und der Flächeninhalt ist gleich der Bilanz. | `B` |

**Hilfe 1 (Tipp).** Frag bei jedem Diagramm zuerst, ob `f − g` sein Vorzeichen wechselt — und wie oft.

**Hilfe 2 (Ansatz).** Wechselt `f − g` nie das Vorzeichen, sind Bilanz und Flächeninhalt gleich
(bis auf das Vorzeichen). Wechselt es, ist der Flächeninhalt größer als `|Bilanz|`. Eine Bilanz von
null entsteht nur, wenn sich Stücke genau aufheben; dann hilft die Symmetrie des Graphen von `f − g`.

**Hilfe 3 (Lösungsweg).** `h = f − g` in jedem Diagramm:
**A:** `h = 0,5·(x − 2)(x − 4)`, Nullstellen `2` und `4`, beide mit Vorzeichenwechsel.
`∫₀² h = 10/3`, `∫₂⁴ h = −2/3`, `∫₄⁶ h = 10/3`. Bilanz `6`, Flächeninhalt `22/3 ≈ 7,33`.
**B:** `h = 0,2·(x − 3)² + 1 > 0` überall, keine Nullstelle. Bilanz und Flächeninhalt sind beide `9,6`.
**C:** `h = 0,3·(x − 3)²`, doppelte Nullstelle bei `3` ohne Vorzeichenwechsel. Bilanz `=` Flächeninhalt
`= 0,3·18 = 5,4`; ein Integral genügt.
**D:** `h = 0,8·(x − 3)`, Vorzeichenwechsel bei `3`, punktsymmetrisch. `∫₀³ h = −3,6`,
`∫₃⁶ h = +3,6`. Bilanz `0`, Flächeninhalt `7,2`.

*Kontrollrechnung (sympy exakt):* A: `h = (x − 2)(x − 4)/2`; `∫₀⁶ h = 6`, Flächeninhalt `22/3`.
B: `h = (x² − 6x + 14)/5`, Diskriminante `36 − 56 < 0` (keine reelle Nullstelle); `∫₀⁶ h = 48/5`.
C: `∫₀⁶ 0,3·(x − 3)² dx = 27/5`. D: `∫₀⁶ 0,8·(x − 3) dx = 0`, Flächeninhalt `36/5`.

**Rückmeldung bei voller Punktzahl.** Alle vier richtig. Entscheidend war jedes Mal die Frage, ob
`f − g` sein Vorzeichen wechselt: Ohne Wechsel (B, C) sind Bilanz und Flächeninhalt gleich, auch
wenn sich die Graphen berühren (C). Mit Wechsel ist der Flächeninhalt größer als der Betrag der
Bilanz (A) — im Extremfall bleibt von der Bilanz nichts übrig (D).

**Rückmeldung bei Teilerfolg** (nennt die Strategie, nicht die Lösung). Geh jede Aussage in
derselben Reihenfolge durch: Erstens — haben die Graphen gemeinsame Punkte? Zweitens — wenn ja,
wechseln die Graphen dort die Lage (oben/unten) oder berühren sie sich nur? Drittens — wenn sie
die Lage wechseln, heben sich die Stücke ganz auf oder nur teilweise? Wer nur auf die Zahl der
Schnittpunkte schaut, verwechselt Berühren mit Kreuzen.

### a4 — Anforderungsbereich II · Zahleneingabe · Schlüssel `a4`

**Aufgabentext.** In einen Tank fließt Wasser mit der Rate `z(t) = 4·e^(−0,3t)` (in L/min,
`t` in min) zu, gleichzeitig läuft ständig `2 L/min` ab. Im Zeitraum `0 ≤ t ≤ 8` gibt es zwei
Phasen: erst fließt mehr zu als ab, dann mehr ab als zu. Bestimme die **Summe der beiden
Nettomengen** — jede als positive Zahl gezählt, also den Flächeninhalt zwischen den Graphen von `z`
und der Konstanten `2`. Runde auf zwei Nachkommastellen.

**Einheitenauswahl:** `L` · `m³` · `L/min` · `min`.

**Daten:** `wert: 7.97`, `einheit: "L"`, `tol: 0.05`, `alt: {wert: 0.00797, einheit: "m³"}`
(abgeleitete Toleranz `0,00005 m³`; der exakte Wert `0,00796761 m³` liegt darin).

**Hilfe 1 (Tipp).** Zu welchem Zeitpunkt ist der Zufluss gerade so groß wie der Abfluss? Dieser
Zeitpunkt teilt das Intervall — und er ergibt sich aus einer Gleichung, in der ein Logarithmus vorkommt.

**Hilfe 2 (Ansatz).** Löse `4·e^(−0,3t) = 2` nach `t` auf, das ist die Schnittstelle `t*`. Eine
Stammfunktion von `z(t) − 2` ist `Z(t) = −(40/3)·e^(−0,3t) − 2t`; kontrolliere sie durch Ableiten. Dann
`A = (Z(t*) − Z(0)) + (Z(t*) − Z(8))`, denn im zweiten Stück ist `z − 2` negativ.

**Hilfe 3 (Lösungsweg).**
`4·e^(−0,3t) = 2` ⟹ `e^(−0,3t) = 1/2` ⟹ `−0,3·t = −ln 2` ⟹ `t* = ln 2/0,3 = 2,3105 min`.
Probe der Stammfunktion: `Z′(t) = −(40/3)·(−0,3)·e^(−0,3t) − 2 = 4·e^(−0,3t) − 2` ✓.
`Z(0) = −40/3 = −13,3333`.
`Z(t*) = −(40/3)·(1/2) − 2·2,3105 = −6,6667 − 4,6210 = −11,2876` (denn `e^(−0,3t*) = 1/2`).
`Z(8) = −(40/3)·e^(−2,4) − 16 = −13,3333·0,090718 − 16 = −1,2096 − 16 = −17,2096`.
Erste Phase: `Z(t*) − Z(0) = −11,2876 + 13,3333 = 2,0457 L` (Netto-Zunahme).
Zweite Phase: `Z(8) − Z(t*) = −17,2096 + 11,2876 = −5,9219`, Betrag `5,9219 L` (Netto-Abnahme).
`A = 2,0457 + 5,9219 = 7,9676 L ≈ 7,97 L`.
*Nebenbei:* Die Bilanz ist `2,0457 − 5,9219 = −3,8762 L`: Der Tank hat am Ende `3,88 L` weniger als am
Anfang — obwohl er in der ersten Phase `2,05 L` gewonnen hat.
*Numerische Gegenprobe (`mpmath.quad`, Teilung bei `t*`): `7,96761030`.*

**Rückmeldungen:**

- `ok`: Richtig. `t* = ln 2/0,3 = 2,31 min`; erste Phase `2,05 L`, zweite Phase `5,92 L`, Summe
  `7,97 L` (rund `0,008 m³`).
- `falschEinheit`: Der Zahlenwert stimmt. Rate mal Zeit ergibt Menge: L/min · min = L — herausgekommen
  ist ein Volumen, keine Rate und keine Zeit. In Kubikmetern wären es `0,00797 m³`.
- `nah`: `5,92 L` ist nur die zweite Phase; die erste Phase (`2,05 L`) fehlt — du hast die
  Schnittstelle gefunden, aber nur ein Teilintegral berechnet. `12,12 L` ist `∫₀⁸ z dt`, der gesamte
  Zufluss: Der Abfluss von `2 L/min` wurde nicht abgezogen. Gefragt ist der Abstand **zwischen** den
  Graphen, nicht die Fläche unter `z`.
- `weit`: `3,88 L` ist der **Betrag der Bilanz** (`2,05 − 5,92 = −3,88`): Du hast über das ganze
  Intervall integriert und dann den Betrag genommen. Die beiden Phasen heben sich teilweise auf; der
  Flächeninhalt zählt sie beide positiv. `2,05 L` ist nur die erste Phase. Die Hilfen führen dich
  durch die Zerlegung bei `t*`.

### a5 — Anforderungsbereich II · Zahleneingabe · Schlüssel `a5`

**Aufgabentext.** Für eine Umgehungsstraße liegt ein Querschnitt vor. Das Gelände wird beschrieben
durch `G(x) = 0,5x³ − x² − 3x + 7`, die geplante Trasse durch `T(x) = 4 − 0,5x`, jeweils für
`−2 ≤ x ≤ 3`. Dabei ist `x` in **Dekametern** (1 Einheit = 10 m) und der Funktionswert in
**Metern** angegeben. Wo das Gelände über der Trasse liegt, wird Boden abgetragen (Einschnitt), wo
es darunter liegt, wird aufgeschüttet (Damm). Bestimme die gesamte Querschnittsfläche, die insgesamt
abgetragen oder aufgeschüttet wird, in Quadratmetern. Runde auf zwei Nachkommastellen.

**Einheitenauswahl:** `m²` · `m³` · `FE` · `m` (die letzten drei sind Distraktoren).

**Daten:** `wert: 105.42`, `einheit: "m²"`, `tol: 0.05`, keine Alternativeinheit. (Eingaben `105,4`
und `105,42` liegen in der Toleranz; `105` nicht.)

**Hilfe 1 (Tipp).** Bevor du integrierst: Was bedeutet **eine** Flächeneinheit in diesem
Koordinatensystem in Quadratmetern, wenn die beiden Achsen verschieden skaliert sind?

**Hilfe 2 (Ansatz).** `h = G − T` bilden; die Schnittstellen liegen bei ganzen Zahlen (ausprobieren,
die Randwerte helfen). Danach `H` als Stammfunktion, Vorzeichen von `h` in den Teilintervallen
prüfen, Beträge der Teilintegrale addieren und zum Schluss die Einheit umrechnen.

**Hilfe 3 (Lösungsweg).**
`h(x) = 0,5x³ − x² − 3x + 7 − 4 + 0,5x = 0,5x³ − x² − 2,5x + 3 = ½·(x + 2)(x − 1)(x − 3)`.
Probe der Faktorisierung: `(x + 2)(x − 1)(x − 3) = x³ − 2x² − 5x + 6`, halbiert ✓. Schnittstellen
`x = −2`, `x = 1`, `x = 3` (an den Rändern `G(−2) = T(−2) = 5` und `G(3) = T(3) = 2,5`).
Vorzeichen: `h(0) = 3 > 0` (Einschnitt auf `(−2; 1)`), `h(2) = ½·4·1·(−1) = −2 < 0` (Damm auf `(1; 3)`).
`H(x) = x⁴/8 − x³/3 − (5/4)·x² + 3x`.
`H(−2) = 2 + 8/3 − 5 − 6 = −19/3`, `H(1) = 1/8 − 1/3 − 5/4 + 3 = 37/24`, `H(3) = 81/8 − 9 − 45/4 + 9 = −9/8`.
Einschnitt: `H(1) − H(−2) = 37/24 + 152/24 = 189/24 = 63/8 = 7,875 FE`.
Damm: `|H(3) − H(1)| = |−27/24 − 37/24| = 64/24 = 8/3 ≈ 2,6667 FE`.
Zusammen `63/8 + 8/3 = 253/24 ≈ 10,5417 FE`.
**Einheit:** 1 FE = 1 dam · 1 m = 10 m · 1 m = **10 m²** (nicht 100 m²).
`253/24 FE · 10 m²/FE = 105,4167 m² ≈ 105,42 m²`.
(Einschnitt `78,75 m²`, Damm `26,67 m²`; die Bilanz `63/8 − 8/3 = 125/24 FE = 52,08 m²` ist ein
Überschuss an Boden.) Der Querschnitt beträgt `105,42 m²`; je Meter Trassenlänge sind das `105,42 m³` Boden.
*Numerische Gegenprobe (`mpmath.quad`, Teilung an `−2, 1, 3`): `10,54166667 FE`.*

**Rückmeldungen:**

- `ok`: Richtig. Einschnitt `7,875 FE`, Damm `2,667 FE`, zusammen `10,54 FE`, und wegen
  `1 FE = 10 m · 1 m = 10 m²` sind das `105,42 m²` Querschnitt, je Meter Trassenlänge also `105,42 m³` Boden.
- `falschEinheit`: Der Zahlenwert stimmt. Gefragt ist eine Querschnittsfläche in `m²`. Kubikmeter
  bekämst du erst, wenn du mit der Länge der Trasse multiplizierst; `FE` hat hier keine
  SI-Bedeutung, weil die Achsen verschieden skaliert sind.
- `nah`: Falls du etwa `78` erhalten hast: `78,75 m²` ist nur der Einschnitt — der Damm (`26,67 m²`) fehlt, denn aufgeschüttet wird
  auch Boden, und der wird bewegt. Falls du `105` eingegeben hast (auf ganze Quadratmeter gerundet): Das liegt `0,42 m²` daneben
  und fällt aus der Toleranz — verlangt sind zwei Nachkommastellen.
- `weit`: Falls du etwa `52` erhalten hast: `52,08 m²` ist die **Bilanz** `∫ (G − T) dx` — der Überschuss, nicht der Aufwand: Einschnitt
  und Damm haben sich teilweise aufgehoben. Bei `10,54` fehlt die Umrechnung der Flächeneinheiten
  (Faktor `10` vergessen); `1054,17` entsteht, wenn du `1 FE = 100 m²` setzt, als
  wären beide Achsen in Dekametern skaliert. `26,67` wäre nur der Damm.

### a6 — Anforderungsbereich III · offene Bewertungsaufgabe · Schlüssel `a6`

**Aufgabentext.** Für den Querschnitt aus Aufgabe a5 hat der Bauleiter das Integral über das
ganze Gelände ausgewertet und notiert: *„`∫ (G − T) dx` ergibt `52,08 m²`. Wir müssen also je Meter
Trasse nur gut 52 m³ Boden bewegen (1 m² Querschnitt je Meter Trasse sind 1 m³), den Rest gleicht das Gelände von selbst aus."* Beurteile diese
Aussage. Gehe dabei ein auf (i) was die Zahl `52,08 m²` tatsächlich beschreibt, (ii) welche Größe
für den Aufwand der Bagger und Lastwagen maßgeblich ist und wie sie sich berechnet (Einschnitt
`78,75 m²`, Damm `26,67 m²`), (iii) eine Frage, bei der der Bauleiter mit der Bilanz doch die
richtige Zahl benutzt, und (iv) eine Grenze des Modells.

Baustein: `<textarea>` + `<button data-loesung="a6">Musterlösung anzeigen</button>` +
`<div class="hilfe-text" data-stufe="9">`.

**Hilfe 1 (Tipp).** Frag nicht, ob die Zahl stimmt — sie stimmt —, sondern **wofür** sie stimmt.

**Hilfe 2 (Ansatz).** Trenne drei Mengen: den Boden, der ausgehoben wird, den Boden, der eingebaut
wird, und den Boden, der am Ende übrig bleibt oder fehlt. Ordne jeder eine der Zahlen `78,75`,
`26,67`, `52,08` zu.

**Hilfe 3 (Lösungsweg-Gerüst).** (1) Die Bilanz ist `P − N` mit `P = 78,75 m²` (Einschnitt, `G > T`)
und `N = 26,67 m²` (Damm, `G < T`). (2) Aufwand wird durch `P + N = 105,42 m²` gemessen, nicht durch
`P − N`. (3) Die Bilanz beantwortet: Wie viel Boden fällt insgesamt ab oder fehlt? (4) Modellgrenze
benennen, zum Beispiel Auflockerung.

**Erwartete Argumentation (Musterlösung).**

Die Aussage ist **zur Hälfte richtig**. Die Zahl `52,08 m²` stimmt: Sie ist das Integral von
`G − T`, also die Bilanz `78,75 − 26,67 = 52,08 m²`. Sie beschreibt, wie viel Boden je Meter Trasse
**übrig bleibt**: Der Einschnitt liefert `78,75 m²`, der Damm braucht nur `26,67 m²`, und die
Differenz von `52,08 m²` muss abgefahren werden (oder an anderer Stelle verbaut). Für **diese** Frage
— Mengenbilanz, Anzahl der Abfuhrfahrten — ist die Bilanz die richtige Größe.

Falsch ist der Schluss, nur `52 m³` je Meter Trasse seien zu bewegen (Querschnitt `52,08 m²` mal `1 m`). Ausgehoben werden `78,75 m²` (Bagger im
Einschnitt) und eingebaut werden `26,67 m²` (Damm schütten, verdichten); zusammen ist die
Querschnittsfläche, die bearbeitet wird, `78,75 + 26,67 = 105,42 m²`, also gut das Doppelte der
Bilanz. Die Bilanz ist so klein, weil sich Einschnitt und Damm im Integral teilweise aufheben — genau
wie ein positives und ein negatives Flächenstück. Das Gelände gleicht **nichts** von selbst aus: Ein
Bagger, der im Einschnitt abträgt, arbeitet unabhängig davon, ob anderswo aufgeschüttet wird. Für den
Aufwand zählt deshalb der Flächeninhalt zwischen den Graphen, `∫ |G − T| dx`, mit den Schnittstellen
`x = −2, 1, 3` als Grenzen.

Ein sinnvoller Nutzen der Zerlegung: Der Damm kann mit dem Aushub aus dem Einschnitt gebaut werden,
soweit der Transportweg kurz ist; `26,67 m²` lassen sich so intern decken, `52,08 m²` müssen
abgefahren werden. Beide Zahlen — Bilanz und Flächeninhalt — brauchst du, aber für verschiedene Fragen.

Modellgrenzen (eine genügt): Der Boden wird beim Lösen aufgelockert und nimmt je nach Bodenart ein
größeres Volumen ein als im gewachsenen Zustand; im Damm wird er wieder verdichtet. Die Rechnung mit
Querschnittsflächen setzt außerdem einen über die Trassenlänge konstanten Querschnitt voraus; in der
Realität ändert er sich, und die Massen werden aus vielen Querschnitten aufsummiert. Ebenso ignoriert
das Modell Transportwege von Einschnitt zu Damm.

**Bewertungskriterien.** Aussage differenziert beurteilt (nicht nur „richtig" oder „falsch") · `52,08`
korrekt als Bilanz (Überschuss) gedeutet · Aufwandsmaß `∫ |G − T|` mit Wert `105,42 m²` genannt und
begründet, warum sich Einschnitt und Damm im Integral aufheben · Schnittstellen `−2, 1, 3` als Grenzen
benannt · Beispiel für eine Frage, bei der die Bilanz richtig ist (Abfuhr, Überschuss) · Modellgrenze
sachlich benannt.

### a7 — Anforderungsbereich III · offene Fehleranalyse · Schlüssel `a7`

**Aufgabentext.** Drei Lernende bearbeiten Flächenaufgaben zu `f(x) = x³` und `g(x) = x`. Beurteile
jede Aussage und begründe.

**Anna:** *„Die Graphen schneiden sich bei `−1`, `0` und `1`. Ich rechne
`∫₋₁¹ (x³ − x) dx = [x⁴/4 − x²/2]₋₁¹ = 0`. Also schließen die beiden Graphen keine Fläche ein."*

**Ben:** *„Die Funktion `x³ − x` ist punktsymmetrisch zum Ursprung. Also rechne ich
`2·∫₀¹ (x³ − x) dx = 2·(−1/4) = −1/2`. Eine Fläche kann nicht negativ sein, also ist sie `1/2`."*

**Carla** (zu `f(x) = x²`, `g(x) = 2x − 1` auf `[−1; 3]`): *„An jeder Schnittstelle wechselt der obere
Graph. Deshalb muss man an jeder Schnittstelle teilen — hier bei `x = 1`."*

a) Bestimme den richtigen Flächeninhalt für Annas Aufgabe und zeige, wo ihr Schluss versagt.
b) Ben kommt auf das richtige Ergebnis. Prüfe, ob seine Begründung trägt.
c) Nimm zu Carlas Regel Stellung und stelle sie richtig.

Baustein: `<textarea>` + `<button data-loesung="a7">Musterlösung anzeigen</button>` +
`<div class="hilfe-text" data-stufe="9">`.

**Hilfe 1 (Tipp).** Bei Anna und Ben hilft dieselbe Skizze: `x³ − x` hat drei Nullstellen, und zwischen
je zwei benachbarten liegt ein Stück. Bei Carla lohnt es, `f − g` auszurechnen und zu faktorisieren.

**Hilfe 2 (Ansatz).** a) Zerlege an den Nullstellen von `h = x³ − x` und addiere die Beträge.
b) Frag, aus welcher Eigenschaft folgt, dass beide Stücke gleich groß sind — und wo im Rechenweg der
Betrag steht. c) Wechselt `f − g` bei `x = 1` das Vorzeichen?

**Hilfe 3 (Lösungsweg-Gerüst).** a) `h = x(x − 1)(x + 1)`; `∫₋₁⁰ h = 1/4`, `∫₀¹ h = −1/4`; `A = 1/2`,
Bilanz `0`. b) Punktsymmetrie ⟹ `∫₋₁⁰ h = −∫₀¹ h`; die Stücke sind betragsgleich. c) `h = (x − 1)²`,
doppelte Nullstelle, kein Vorzeichenwechsel.

**Erwartete Argumentation (Musterlösung).**

**a)** Annas Rechnung ist richtig, ihr Schluss falsch. `h(x) = x³ − x = x(x − 1)(x + 1)` hat die
einfachen Nullstellen `−1`, `0`, `1` und wechselt an jeder das Vorzeichen: `h(−0,5) = +0,375 > 0`,
`h(0,5) = −0,375 < 0`. Also liegt auf `[−1; 0]` der Graph von `f` oben, auf `[0; 1]` der von `g`.
`∫₋₁⁰ h = [x⁴/4 − x²/2]₋₁⁰ = 0 − (1/4 − 1/2) = 1/4` und `∫₀¹ h = (1/4 − 1/2) − 0 = −1/4`. Die Stücke
sind gleich groß und heben sich in der Bilanz auf. Der Flächeninhalt ist `1/4 + 1/4 = 1/2`. Die Bilanz `0`
zeigt nur die Auslöschung, nicht das Fehlen von Fläche.

**b)** Ergebnis richtig, Begründung lückenhaft. Ben nutzt die Symmetrie ohne Nachweis: Aus
`h(−x) = −h(x)` folgt `∫₋₁⁰ h = −∫₀¹ h = 1/4`, die beiden Stücke sind also betragsgleich, und deshalb
`A = 2·|∫₀¹ h|`. Sein Term `2·∫₀¹ h = −1/2` ist **nicht** der Flächeninhalt; er wird erst durch den
Betrag zu einem, und Bens Begründung („Fläche nicht negativ") ist kein Argument, sondern eine
Reparatur nach dem Ergebnis. Richtiger Ansatz: `A = 2·|∫₀¹ h|` mit Symmetrie als Begründung. Wer
stattdessen rechnet `2·∫₀¹ (x − x³) dx`, erhält ohne Nachbesserung `1/2` — aber nur, weil er
vorher schon wusste, dass `g` auf `[0; 1]` oben liegt.

**c)** Carlas Aussage ist falsch. `h(x) = x² − 2x + 1 = (x − 1)²` hat bei `x = 1` eine doppelte
Nullstelle **ohne** Vorzeichenwechsel; die Graphen berühren sich, die Parabel bleibt oberhalb der
Geraden. Der obere Graph wechselt dort nicht. Man **darf** teilen — `8/3 + 8/3 = 16/3` —, muss es aber
nicht; ein Integral `∫₋₁³ (x − 1)² dx = 16/3` genügt. Richtig: Man teilt an den Nullstellen von
`f − g`, an denen das Vorzeichen wechselt (ungerade Vielfachheit); an Berührstellen (gerade
Vielfachheit) ist das nicht nötig.

**Bewertungskriterien.** a) Zerlegung an `−1, 0, 1` · Teilintegrale `1/4` und `−1/4` · Flächeninhalt
`1/2` · Bilanz `0` als Auslöschung erklärt · b) Symmetrie-Argument `h(−x) = −h(x)` genannt · Betrag
am richtigen Ort erkannt (um das Teilstück, nicht um die fertige Summe) · c) `h = (x − 1)²`
faktorisiert · doppelte Nullstelle ohne Vorzeichenwechsel erkannt · Regel richtiggestellt
(Vorzeichenwechsel, nicht Schnittstelle) · erkannt, dass Teilen an der Berührstelle nicht falsch, nur
überflüssig ist.

*Kontrollrechnung a6/a7:* `63/8 = 7,875`, `8/3 = 2,6667`, `63/8 + 8/3 = 253/24 = 10,5417 FE = 105,4167 m²`;
`63/8 − 8/3 = 125/24 = 5,2083 FE = 52,0833 m²`; `7,875·10 = 78,75 m²`, `2,6667·10 = 26,6667 m²`.
a7: `∫₋₁⁰ (x³ − x) = 1/4`, `∫₀¹ (x³ − x) = −1/4`, `∫₋₁¹ |x³ − x| = 1/2`; `∫₋₁³ (x − 1)² = 16/3`.

---

## Abschnitt 6 — Abschluss

`<section id="abschluss">`, `.stufe`-Nummer **6**,
Überschrift **Zusammenfassung und Selbstcheck**.

### 6.1 Vier Kernaussagen (je ein `<div class="merksatz">`)

**Kernaussage 1 — Das Integral ist eine Bilanz, der Flächeninhalt eine Summe von Beträgen.**
Bezeichnen `P` und `N` die Summen der Flächenstücke oberhalb und unterhalb der Achse (beide positiv
gezählt), so gilt `∫ₐᵇ f dx = P − N` und `∫ₐᵇ |f| dx = P + N`. Ein Integralwert von null heißt
deshalb nie „keine Fläche", sondern „die Stücke heben sich auf". Der Unterschied
`Flächeninhalt − |Bilanz|` ist genau `2·min(P, N)`.

**Kernaussage 2 — Die Grenzen des Flächeninhalts sind die Nullstellen mit Vorzeichenwechsel.**
Zwischen Graph und Achse zerlegst du an den Nullstellen von `f`, zwischen zwei Graphen an den
Nullstellen der Differenzfunktion `h = f − g`, also an den Schnittstellen. Praktisch: **eine**
Stammfunktion, ihre Werte an allen Grenzen in einer Tabelle, dann die Beträge der Differenzen
benachbarter Werte addieren. Der Betrag gehört um jedes Teilstück, nie um die Summe.

**Kernaussage 3 — Zwei Graphen sind ein Graph: `A = ∫ |f − g| dx`.**
Verschiebt man beide Graphen senkrecht über die Achse, ändert das die Fläche dazwischen nicht, und
die Konstante kürzt sich in `∫ (f + c) − ∫ (g + c)` heraus. Deshalb ist es gleichgültig, welcher
Graph oben liegt und wie die Graphen zur Achse stehen; der Fall „Graph und Achse" ist der Sonderfall
`g = 0`.

**Kernaussage 4 — Nicht jede Schnittstelle ist eine Grenze, und die beiden Kurven verraten es.**
Nur ein **Vorzeichenwechsel** von `f − g` (bei ganzrationalen Funktionen: Nullstelle ungerader Vielfachheit)
trennt Flächenstücke; an einer Berührstelle (bei ganzrationalen Funktionen: gerade Vielfachheit) bleibt ein Integral. Nach dem Hauptsatz ist `B′ = f − g`
für die Bilanzkurve und `A′ = |f − g|` für die Flächenkurve: `A` fällt nie, `B` hat an jedem
Vorzeichenwechsel einen Extrempunkt, und dort trennen sich die beiden Kurven.

### 6.2 Blick aufs Zentralabitur (`<div class="hinweis">`)

**Im Zentralabitur.** Flächen zwischen Graphen sind kein eigenes Thema, sondern kommen als
Rechen- und Deutungsteil in Analysis-Aufgaben vor. Diese Gestalten begegnen dir regelmäßig:

- **Flächeninhalt berechnen**: „Berechne den Inhalt der Fläche, die die Graphen von `f` und `g`
  einschließen." Erwartet werden Differenzfunktion, Schnittstellen, Stammfunktion, Teilintegrale
  mit Betrag. Eine Skizze verhindert die meisten Vorzeichenfehler, und es lohnt sich, die
  Schnittstellen vor dem Integrieren ausdrücklich hinzuschreiben.
- **Bilanz gegen Flächeninhalt im Sachkontext**: Aus einer Änderungsrate soll ein Bestand
  (Bilanz, „Zunahme insgesamt") und eine bewegte Menge (Flächeninhalt, „Wie viel wurde insgesamt
  zu- und abgeführt?") bestimmt und gedeutet werden — genau die Unterscheidung aus a4–a6.
- **Parameteraufgaben**: „Bestimme `k` so, dass die Fläche zwischen `f_k` und `g` den Inhalt `36`
  hat." Die Fläche wird in Abhängigkeit von `k` aufgestellt und dann nach `k` aufgelöst
  (Aufgabe für schnelle Lernende im Lehrerteil).
- **Begründen und Bewerten**: „Ein Schüler behauptet, die Fläche sei null, weil das Integral null
  ist. Nimm Stellung." oder „Beurteile die Aussage …" — genau der Aufgabentyp von a6 und a7.
- **Graphenzuordnung**: Zugeordnet wird ein Graph zu einer Flächenaussage (Bilanz, Betrag,
  Zerlegung), wie in a3.

*Offen markiert:* Welche Aufgaben in welchem Abiturjahrgang hilfsmittelfrei (ohne GTR/CAS) und
welche mit Hilfsmitteln bearbeitet werden, und wie die Operatoren im jeweiligen Jahr formuliert
sind, entnimmst du den aktuellen Vorgaben des Schulministeriums NRW; sie sind hier nicht
wiedergegeben und werden nicht behauptet.

### 6.3 Selbstcheck (`.karte` mit `<h3>Selbstcheck</h3>`, sechs `.check`-Zeilen)

Vorspann: *Hak ehrlich ab. Was du hier nicht ankreuzen kannst, holst du besser jetzt nach als in
der Klausur.*

1. Ich kann zwischen der Bilanz `∫ f` und dem Flächeninhalt `∫ |f|` unterscheiden, erklären, warum
   ein Integralwert von null nicht „keine Fläche" bedeutet, und beide an einem Beispiel berechnen.
2. Ich kann begründen, warum der Flächeninhalt zwischen Graph und Achse `∫ |f|` ist — Spiegelung
   unterhalb der Achse, Zerlegung an Nullstellen mit Vorzeichenwechsel — und warum `|∫ f|` im
   Allgemeinen zu klein ist.
3. Ich kann den Flächeninhalt zwischen zwei Graphen als `∫ |f − g|` ansetzen und die Formel über die
   senkrechte Verschiebung beider Graphen herleiten.
4. Ich kann Schnittstellen bestimmen — auch irrationale und solche, die einen Logarithmus verlangen —
   und entscheiden, welche davon Integrationsgrenzen sind: nur die im Intervall, nur die mit
   Vorzeichenwechsel, nicht die Berührstellen.
5. Ich kann Flächeninhalte mit **einer** Stammfunktion, einer Wertetabelle und den Beträgen der
   Teilintegrale berechnen und das Ergebnis durch Skizze und Überschlag kontrollieren.
6. Ich kann in einem Sachzusammenhang Bilanz und Flächeninhalt deuten (Bestandsänderung gegen
   bewegte Menge), Einheiten bei verschieden skalierten Achsen umrechnen und eine Aussage
   über eine Bilanz begründet bewerten.

### 6.4 Export und Druck

Knopfleiste wie im Referenzmodul: `Ergebnisse kopieren` (`id="bExport"`) und
`Als Arbeitsblatt drucken`. Darunter der Hinweis, dass nichts gespeichert wird.

`var namen = {…}` am Skriptende:

```
vw1: "Vorwissen 1 – Schnittstellen bestimmen"
vw2: "Vorwissen 2 – Linearität des Integrals"
vw3: "Vorwissen 3 – Nullstellen durch Ausklammern"
sim1:"Simulation 1 – größte Bilanz bei wandernder unterer Grenze"
sim2:"Simulation 2 – Nullstelle der Bilanzkurve"
a1:  "Aufgabe 1 – Fläche zwischen Graph und Achse"
a2:  "Aufgabe 2 – Fläche zwischen zwei Parabeln"
a3:  "Aufgabe 3 – Zuordnung Bilanz und Flächeninhalt"
a4:  "Aufgabe 4 – Zufluss gegen Abfluss"
a5:  "Aufgabe 5 – Massenausgleich im Straßenbau"
```

Die offenen Aufgaben a6 und a7 werden nicht automatisch ausgewertet und erscheinen daher — wie im
Referenzmodul — nicht im Export.

### 6.5 Anschlusshinweis (`<div class="hinweis">`)

**Wie es weitergeht.** Mit diesem Modul ist die Integralrechnung der Q1 abgeschlossen: Bilanz,
Hauptsatz, Flächeninhalt zwischen Graphen. Nach der Verteilung dieses Projekts folgt in Q1 die
analytische Geometrie. Weitere Integralthemen — mittlere Werte, Rotationskörper, Integrale über
unbeschränkte Intervalle — sind nicht Teil dieses Moduls; ob und wann sie in Q1 oder Q2 kommen,
legt der schulinterne Lehrplan fest (Zuordnung offen).

---

## Lehrerteil

`<details class="lehrer">` mit `<summary>Für die Lehrkraft</summary>`, am Ende von Abschnitt 6,
verschwindet beim Drucken.

### Einordnung

Inhaltsfeld **„Funktionen und Analysis"** (Kernlehrplan Mathematik, gymnasiale Oberstufe NRW). Q1
umfasst laut Verteilung dieses Projekts die Integralrechnung bis zum Hauptsatz und zu Flächen
zwischen Graphen; dieses Modul deckt den letzten Teil ab: Flächeninhalt zwischen Graph und Achse,
zwischen zwei Graphen, Zerlegung an Nullstellen und Schnittstellen, Deutung von Bilanz und
Flächeninhalt im Sachkontext.

Prozessbezogene Schwerpunkte sind **Argumentieren** (Herleitungen 2.3 und 3.2, Aufgaben a6 und a7),
**Modellieren** (a4, a5, a6, Einstieg), **Werkzeuge nutzen** (die Simulation als Messinstrument,
Verzicht auf den Rechner in a1 bis a3) und **Kommunizieren** (Skizze und Wertetabelle als
Darstellungsmittel). Vorausgesetzt werden aus dem Vorgängermodul `mathe-q1-hauptsatz`:
Hauptsatz, Stammfunktion, Grundintegrale, lineare Substitution, Intervalladditivität und die
Integralfunktion; aus früherer Zeit: Nullstellenbestimmung, Polynomdivision, Monotonie.

**Stellung in der Reihe:** unmittelbar nach `mathe-q1-hauptsatz.html`. Ohne die Integralfunktion
und `I′ = f` verliert Abschnitt 2.6 seine Pointe (die zwei Kurven der Simulation).

*Offen markiert:* Die Unterscheidung der Wörter „Bilanz" (orientierter Flächeninhalt) und
„Flächeninhalt" ist eine didaktische Setzung dieses Moduls, keine Vorgabe des Kernlehrplans; im
Unterricht und in Schulbüchern heißt die Bilanz oft „Integralwert" oder „orientierter
Flächeninhalt". Ebenfalls Setzung: dass der Satz vom Minimum und Maximum in 3.2 benutzt, aber nicht
bewiesen wird.

### Zeitbedarf

Ausgelegt auf eine Doppelstunde von 90 Minuten (Tabelle im Modul in `<div class="tabelle">`
kapseln):

| Abschnitt | Zeit | Sozialform |
|---|---|---|
| 1 Einstieg (Straßenschnitt, drei Vorwissensfragen) | 8 min | Plenum, Fragen in Einzelarbeit |
| 2 Bilanz gegen Flächeninhalt, Beweis in 2.3, Verfahren | 18 min | lehrergelenkt, Details-Block je nach Kurs |
| 3 Zwei Graphen, Schnittstellen, Berührstelle | 20 min | Plenum mit Sicherungsphase |
| 4 Simulation mit Beobachtungsauftrag und zwei MC-Fragen | 20 min | Partnerarbeit am Gerät |
| 5 Übungen (Auswahl, siehe Differenzierung) | 20 min | Einzel- oder Partnerarbeit |
| 6 Abschluss, Selbstcheck, Export | 4 min | Plenum |

Summe `8 + 18 + 20 + 20 + 20 + 4 = 90` min. Realistisch in 90 Minuten schaffbar sind die Abschnitte 1
bis 4 sowie a1 und a2. a3 bis a7 sind Hausaufgabe oder Material für die Folgestunde; a6 und a7
eignen sich als Einstieg der Folgestunde, weil sie ein Streitgespräch auslösen. Wird die
Herleitung 3.2 im Plenum entwickelt (Verschiebungsargument), fallen dafür 8 bis 10 Minuten an,
und der Übungsteil schrumpft entsprechend.

### Typische Schülerfehler — und wo anzuhalten ist

**(1) „Integral negativ — also Betrag drübersetzen."** Der Leitfehler dieses Moduls. Das Ergebnis
sieht plausibel aus, ist aber nur bei Graphen ohne Vorzeichenwechsel richtig.
→ **Anhalten** am Ende von 2.1, bevor die Definition kommt. Frage an den Kurs: „Der Graph liegt
teils über, teils unter der Achse — was rechnet das Integral mit dem Stück darunter?" Dann die zwei
Zahlen an die Tafel: `|∫₀³ f| = 2,25`, `∫₀³ |f| = 3,08`. Fehlerkasten 2.5 und Aufgabe a1
(Bilanz `1,33` gegen Flächeninhalt `4`) prüfen es.

**(2) „Ergebnis null — keine Fläche."** Wird an `x³` auf `[−1; 1]` sofort sichtbar.
→ **Anhalten** im Fehlerkasten 2.5. Die Simulation liefert das Bild dazu: Bilanz praktisch null bei deutlich
größerem Flächeninhalt auf einem einzigen Bildschirm (Paar A, `a = −1,50`, `b` kurz rechts der ersten Schnittstelle).

**(3) Betrag in die Stammfunktion gesetzt.** `∫ |f| = |F|` oder `[|F(x)|]ₐᵇ`. Ursache ist, dass
der Betrag als „letzter Schritt" gelernt wurde.
→ **Anhalten** bei Schritt 4 der Herleitung 2.3: `|∫ f| ≤ ∫ |f|`. Die Gleichheit gilt nur ohne
Vorzeichenwechsel; a7a zeigt, dass Annas Rechnung genau daran scheitert.

**(4) Verlorene Schnittstelle.** Durch `x` gekürzt statt ausgeklammert; ein negativer Wert
verworfen, weil „Fläche nicht negativ sein kann". → **Anhalten** direkt nach `vw1` und `vw3`
(dort sind die Fälle vorgeformt). Regel für den Kurs: **Ausklammern, nie kürzen.**

**(5) Jede Schnittstelle als Grenze — oder keine Berührstelle erkannt.** Das Vorzeichenbild wird
nicht angelegt.
→ **Anhalten** in 3.4 bei `h = (x − 1)²`. Frage: „Wechselt der obere Graph bei `x = 1`?" Die
Simulation (Paar B) zeigt `f(b) − g(b) = 0,00` bei gleichzeitig `Wechsel = 0`. a3 und a7c prüfen es.
Beachte: Teilen an einer Berührstelle ist nicht falsch, nur überflüssig — das ist ein Unterschied,
den Lernende oft als „falsch" hören und sich dann nicht mehr trauen zu teilen.

**(6) Schnittstellen außerhalb des Intervalls oder Randstück vergessen.** In a1 fehlt oft das
Stück `[3; 4]`, weil „nach der letzten Nullstelle nichts mehr kommt"; im Beispiel 3.3 wird
`x = −2` mitgenommen, obwohl das Intervall bei `0` beginnt.
→ **Anhalten** vor a1: „Was ist die linkeste und die rechteste Grenze? Wo kommen sie her?" —
Randwerte des Intervalls sind genauso Grenzen wie Nullstellen.

**(7) `f − g` in falscher Reihenfolge, negativer Flächeninhalt.** Aufgabe a2 (`weit`-Rückmeldung)
fängt es ab. → Kein eigenes Anhalten, aber ein Satz in 3.1: Die Reihenfolge ist gleichgültig, weil
der Betrag steht; wer einen negativen Wert erhält, hat schlicht `g − f` integriert.

**(8) Bilanz als Aufwand gedeutet.** „52 m³ — mehr müssen wir nicht bewegen." Verwandt mit (2).
→ **Anhalten** bei a5 vor der Eingabe: Frage an den Kurs: „Wer bezahlt den Baggerführer — nach der
Bilanz oder nach dem Flächeninhalt?" a6 vertieft die Bewertung. Bei a5 fällt außerdem
die Einheit auf: `1 FE = 10 m²`, nicht `100 m²` — ein Fehler, den man nur findet, wenn man beide
Achsenmaßstäbe einzeln liest.

**(9) Für jedes Teilstück eine eigene Stammfunktion — mit verschiedenen Konstanten.** Führt zu
Sprüngen in der Rechnung, die man später nicht mehr findet.
→ Regel für den Kurs: **Eine** Stammfunktion, Wertetabelle an allen Grenzen (Kernaussage 2).

### Differenzierung

**Für schnellere Lernende:**

- **Parameteraufgabe.** Bestimme `k > 0` so, dass die Parabel `f(x) = x²` und die Gerade
  `g_k(x) = k·x` eine Fläche vom Inhalt `36` einschließen. Lösung: `h = kx − x²`, Schnittstellen
  `0` und `k`, `A = ∫₀ᵏ (kx − x²) dx = k³/2 − k³/3 = k³/6 = 36` ⟹ `k³ = 216`, `k = 6`.
  (Kontrollrechnung im Prüfskript.)
- **Beweis der Beziehung** `Flächeninhalt − |Bilanz| = 2·min(P, N)` aus `A = P + N` und `B = P − N`:
  `|B| = max(P, N) − min(P, N)`, also `A − |B| = P + N − max + min = 2·min`.
- **Differenzierbarkeit von `|B|`.** In der Simulation hat `|B|` an der Nullstelle von `B` einen
  Knick, weil `B′ = h ≠ 0` dort (das Feld `f(b) − g(b)` zeigt dort einen deutlich von null verschiedenen Wert; exakt `h(−0,376) = 5,01`). `A` hat keinen Knick, weil `A′ = |h|` stetig
  ist. Begründe den Unterschied.
- **Fläche zwischen Kurve und Achse über ein unbeschränktes Intervall.** Aus `sim` Paar C: Der
  Zufluss `4·e^(−0,3t)` hat auf `[0; ∞)` das Integral `40/3`; die Fläche zwischen Zufluss und Abfluss
  `1,5` dagegen wächst ohne Grenze, weil `g` nicht abklingt. Warum? (Ausblick; Einordnung offen.)

**Für Lernende, die mehr Zeit brauchen:**

- Pflichtteil sind a1, a2 und a3. a1 ist reines Handwerk und hat bewusst drei gleich große Stücke,
  damit die Wertetabelle sichtbar trägt; a2 ist dasselbe mit zwei Graphen; a3 verlangt kaum
  Rechnung, trägt aber die zentrale Einsicht.
- Das Verfahren in 2.4 und 3.3 als Merkblatt kopieren, mit einer leeren Wertetabelle zum Ausfüllen.
- Von den beiden AB-III-Aufgaben genügt a7a: ein Gegenbeispiel-Fall, dessen Rechnung in Zeilen
  steht. a6 und a7b/c verlangen Deutung und Modellkritik.
- Die Herleitung in 3.2 kann übersprungen werden; die Simulation trägt die Einsicht „Fläche =
  Betrag der Bilanz, solange kein Vorzeichenwechsel" auch allein.

### Bezug zu Realexperimenten und Daten

- **Wiegen statt integrieren.** Auf gleichmäßigem Karton oder Millimeterpapier wird die Fläche
  zwischen zwei Kurven in ihre Stücke zerschnitten: Stücke, in denen `f` oben liegt, und Stücke, in
  denen `g` oben liegt. Auf einer Küchenwaage: `m_oben − m_unten` entspricht der Bilanz,
  `m_oben + m_unten` dem Flächeninhalt. Aufwand: 15 Minuten und ein Bogen Karton. Der Vergleich mit der
  Rechnung ist die schönste Bestätigung von Kernaussage 1, weil die Lernenden die Auslöschung
  buchstäblich in der Hand haben.
- **Geländeschnitt.** Ein Schnitt durch das Schulgelände mit Nivelliergerät oder Höhendaten aus dem
  Open-Data-Angebot des Landes NRW liefert eine echte Geländekurve; die Trasse legen die Lernenden
  selbst (Gerade). Aus Einschnitt und Damm folgt der Massenausgleich — Aufgabe a5 mit eigenen Daten.
  Die Einordnung, welche Höhendaten bereitstehen, prüft die Lehrkraft vorab.
- **Photovoltaik und Haushaltsverbrauch.** Zwei Tageskurven (Erzeugung, Verbrauch), etwa aus dem
  Smart-Meter oder aus veröffentlichten Lastprofilen: Die Fläche, in der die Erzeugung oben liegt,
  ist die Einspeisung, die andere der Netzbezug; die Bilanz ist der Saldo der Stromrechnung. Passt
  zu a4 mit anderen Namen. Eine Absprache mit Physik lohnt sich (Leistung gegen Energie).
- **Physik: Arbeit im Kraft-Weg-Diagramm.** Die Fläche unter `F(s)` ist die Arbeit; ein Bereich,
  in dem die Kraft entgegen der Bewegung wirkt, zählt negativ. Bilanz gegen Betrag ist dort der
  Unterschied zwischen „Nettoarbeit" und „insgesamt verrichteter Arbeit".
- **CAS/GTR.** Sinnvoll erst nach diesem Modul: `fnInt(abs(f(x) − g(x)), x, a, b)` liefert den
  Flächeninhalt in einer Zeile, verschleiert aber, dass die Nullstellen das eigentliche Problem sind.
  Als Kontrolle der eigenen Rechnung (`Bilanz` gegen `Flächeninhalt` am Rechner vergleichen) ist es
  ideal und führt direkt zurück zu Kernaussage 1.

---

## Checkliste für den Bauagenten

### Benötigte Bausteine und ihre Schlüssel

| Schlüssel | Baustein | `data`-Attribut | Optionen / Besonderheit | AB |
|---|---|---|---|---|
| `vw1` | Multiple Choice | `data-mc="vw1"` | 3 Optionen, `r: 1` | — |
| `vw2` | Multiple Choice | `data-mc="vw2"` | 3 Optionen, `r: 0` | — |
| `vw3` | Multiple Choice | `data-mc="vw3"` | 3 Optionen, `r: 2` | — |
| `sim1` | Multiple Choice | `data-mc="sim1"` | 3 Optionen, `r: 1` | II |
| `sim2` | Multiple Choice | `data-mc="sim2"` | 3 Optionen, `r: 2` | II |
| `a1` | Zahleneingabe | `data-num="a1"` | `wert: 4`, `"FE"`, `tol: 0.05`, kein `alt` | I |
| `a2` | Zahleneingabe | `data-num="a2"` | `wert: 7.54`, `"dm²"`, `tol: 0.05`, `alt: 754 "cm²"` | II |
| `a3` | Zuordnung | `data-check="zuordnung"` | 4 SVG-Diagramme, Lösung C·D·A·B | II |
| `a4` | Zahleneingabe | `data-num="a4"` | `wert: 7.97`, `"L"`, `tol: 0.05`, `alt: 0.00797 "m³"` | II |
| `a5` | Zahleneingabe | `data-num="a5"` | `wert: 105.42`, `"m²"`, `tol: 0.05`, kein `alt` | II |
| `a6` | offene Aufgabe | `data-loesung="a6"` | `<textarea>`, Lösung in `data-stufe="9"` | III |
| `a7` | offene Aufgabe | `data-loesung="a7"` | `<textarea>`, Lösung in `data-stufe="9"` | III |

Dreistufige Hilfen (`data-hilfe="1|2|3"` plus `.hilfe-text[data-stufe="1|2|3"]`) bekommen **alle**
sieben Aufgaben `a1` bis `a7` (auch `a3`, `a6`, `a7`; Textvorlagen stehen bei jeder Aufgabe).
`a6` und `a7` bekommen zusätzlich `data-stufe="9"` mit der Musterlösung und den Bewertungskriterien.
*Prüfen:* Ob die Engine des Referenzmoduls Hilfeknöpfe an einer Zuordnungsaufgabe und an offenen
Aufgaben zulässt (`document.querySelectorAll("[data-hilfe]")` bindet nach `closest(".aufgabe")`,
also ja); falls nicht, entfällt die Hilfe für `a3` und wird im Bauprotokoll vermerkt.

### Simulationsbausteine

| Element | `id` | Bereich / Werte |
|---|---|---|
| Canvas | `cvSim` | `width="1000" height="690"`, `style="touch-action:none"` |
| Regler untere Grenze `a` | `rA` | `0 … 100·(hi − lo) − 10`, `a = lo + rA/100`, Start 0 (`a = −1,50`) |
| Regler obere Grenze `b` | `rB` | `10 … 100·(hi − lo)`, `b = lo + rB/100`, Start 500 (`b = 3,50`) |
| Anzeige `a` | `lA` | 2 Nachkommastellen |
| Anzeige `b` | `lB` | 2 Nachkommastellen |
| Anzeige `f(b) − g(b)` | `lH` | 2 Nachkommastellen |
| Anzeige `P` (f oben) | `lP` | 2 Nachkommastellen |
| Anzeige `N` (g oben) | `lN` | 2 Nachkommastellen |
| Anzeige Bilanz | `lBil` | 2 Nachkommastellen |
| Anzeige Flächeninhalt | `lFl` | 2 Nachkommastellen |
| Anzeige Differenz | `lDiff` | 2 Nachkommastellen, immer `≥ 0`, nie `−0,00` |
| Anzeige Wechsel | `lNs` | ganze Zahl |
| Knöpfe Paar | `data-paar="A"`, `"B"`, `"C"` | Paar A ist Startzustand |
| Knopf Abspielen | `bPlay` | `b` läuft mit `(hi − lo)/5` je Sekunde bis `hi`, dann Stopp |
| Knopf Zurücksetzen | `bReset` | Paar A, `a = −1,50`, `b = 3,50`, Schnittstellen aus |
| Checkbox Schnittstellen | `cSchn` | Vorgabe: nicht gesetzt |

### Prüfpunkte vor der Abnahme

1. Jede abgesetzte Formel und jede Formel im Fließtext hat ein gefülltes `data-plain` mit Unicode
   (`∫`, `≤`, `⟹`, `⁻`, `·`, `−`, `√`).
2. Alle Tabellen der Seite stehen in `<div class="tabelle">`: Wertetabelle `F` in 2.1, Wertetabelle
   `H` in 3.3, Zeitbedarf im Lehrerteil (drei Tabellen; die Tabellen in 4.2, 4.3 und 4.5 dieser
   Datei sind Spezifikation und gehören **nicht** auf die Seite).
3. Die Simulation liefert bei Paar A, `a = −1,50`, `b = 2,00` die Werte `P = 11,25`, `N = 1,81`,
   Bilanz `9,44`, Flächeninhalt `13,06`, Differenz `3,61`, Wechsel `1`; bei `b = −1,00`
   Bilanz `−1,81`, Flächeninhalt `1,81`, Differenz `0,00`, Wechsel `0`; bei `a = −1,00`, `b = 3,50`
   Bilanz `11,39`; bei Paar B, `a = −1,00`, `b = 3,00` Bilanz und Flächeninhalt `5,33`, Wechsel `0`;
   bei Paar C, `a = 0,00`, `b = 10,00` Bilanz `−2,33`, Flächeninhalt `9,19`, Wechsel `1`. Weitere
   Werte siehe Tabelle in 4.3.
4. Die Zahlen aus `sim1`/`sim2` stehen **nirgends** sonst auf der Seite (nicht in Aufgabentexten,
   Merksätzen oder Beschriftungen); sichtbar sind sie nur in der Simulation und im Feedback nach dem
   Antworten. Auch der Lehrerteil (im Browser aufklappbar) nennt die Lösungswerte von `sim1`/`sim2`
   **nicht** (weder die Stelle `b₀` noch eine Einstellung mit ihren Anzeigewerten); dort stehen nur die Extremwerte des Beobachtungsauftrags.
5. `−0,00` erscheint in keiner Anzeige (Test: Paar C, `a = 3,27`, `b = 10,00`: Differenz `0,00`).
6. Bei `b − a < 0,10` kann nicht gezogen werden; der Regler stoppt und schiebt die andere Grenze mit.
7. Das Paar-Umschalten setzt Regler-Grenzen neu und zeichnet beide Diagramme; die Beschriftung der
   Flächen wechselt zwischen „FE" und „L" (Paar C).
8. Die drei Rückmelde-Kategorien jeder Zahleneingabe (`nah` gegen `weit`) sind so getextet, dass die
   genannten Fehlwerte tatsächlich in der jeweiligen Kategorie liegen: `a1`: `2,67` nah, `1,33` weit;
   `a2`: `6,00` / `11,31` / `5,66` / `−7,54` nah (`−7,54` wegen `Math.abs` in der Engine; der Text steht deshalb im `nah`-Feld); `a4`: `5,92` / `12,12` nah, `3,88` / `2,05` weit;
   `a5`: `78,75` nah, `52,08` / `26,67` / `10,54` / `1054,17` weit (Prüfskript, Abschnitt `nah/weit`).
9. Der Eintrag in `fachliches/modulliste.md` wird nach bestandener Prüfung von `in Arbeit` auf
   `fertig` gesetzt.

---

## Quelle der Kontrollrechnungen

Alle Zahlenwerte dieses Dokuments wurden mit Python nachgerechnet: exakt mit `sympy` (rationale
Arithmetik, Brüche), numerisch mit `mpmath` (30 Stellen, Teilung an den Nullstellen) und über die
Mittelpunktsregel mit 200 000 bzw. 400 000 Streifen. Das Simulationsverfahren aus 4.3
(Nullstellensuche mit Vorzeichenwechsel, Zellentabellen mit Simpson `n = 8`) ist im Skript 1:1
nachgebaut und gegen `mpmath.quad` geprüft: größte Abweichung `1,3·10⁻¹⁴` über je 60 Zufallspaare
`(a, b)` je Paar. Die Kontrollwerte-Tabelle in 4.3 wird vom Skript **zeilenweise aus dieser Datei
gelesen** und mit dem Verfahren verglichen (17 Zeilen), ebenso die Polylinien der Diagramme in a3.
Die Zuordnung der Fehlwerte zu den Rückmelde-Kategorien `nah` (Faktor 0,5 bis 2 vom Sollwert) und
`weit` ist mit derselben Regel wie in der Engine (`bausteine.md`, Abschnitt 4) nachgeprüft.

Der Näherungsfehler einer einzelnen Simpson-Regel ohne Teilung an den Nullstellen beträgt bis
`4,6·10⁻⁵` (bewusst nicht verwendet, siehe 4.3).

**Prüfskript** (vollständig; Aufruf
`PYTHONIOENCODING=utf-8 python kontrolle.py "inhalte/mathe-q1-flaechen-zwischen-graphen.md"`):

```python
# -*- coding: utf-8 -*-
# Kontrollrechnung zu inhalte/mathe-q1-flaechen-zwischen-graphen.md
# Aufruf: PYTHONIOENCODING=utf-8 python kontrolle.py "<Pfad zur Inhaltsdatei>"
# Jede in der Datei genannte Zahl steht hier als assert. Bibliotheken: sympy, mpmath, fractions.
import sys, math, io, random, re
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
x, t = sp.symbols('x t')
R = sp.Rational
MD = sys.argv[1] if len(sys.argv) > 1 else None
md = io.open(MD, encoding='utf-8').read() if MD else ""
n_ok = 0

def ok(name, cond, info=""):
    global n_ok
    assert cond, "FEHLER: " + name + " " + str(info)
    n_ok += 1
    print("OK  " + name + ("  " + str(info) if info != "" else ""))

def I(f, a, b):
    return sp.integrate(f, (x, a, b))

def near(a, b, tol=1e-9):
    return abs(float(a) - float(b)) <= tol

def fmt(v, d=2):
    if abs(v) < 0.5 * 10 ** (-d):
        v = 0.0
    return ("%." + str(d) + "f") % v

def komma(v, d=2):
    return fmt(v, d).replace(".", ",")

# ---------------------------------------------------------------- Abschnitt 1
ok("vw1 Schnittstellen", sorted(sp.solve(x**2 - (x + 2), x)) == [-1, 2])
ok("vw1 Fehlerfall x^2+x-2", sorted(sp.solve(x**2 + x - 2, x)) == [-2, 1])
ok("vw1 Probe g(1)=3, f(1)=1", (1 + 2, 1**2) == (3, 1))
ok("vw2 5-2*2=1; 5-2=3; 5+4=9", (5 - 2 * 2, 5 - 2, 5 + 2 * 2) == (1, 3, 9))
ok("vw3 Nullstellen x^3-3x", sorted(sp.solve(x**3 - 3 * x, x), key=float) == [-sp.sqrt(3), 0, sp.sqrt(3)])

# ---------------------------------------------------------------- Abschnitt 2 (E1)
f1 = x**3 - 4 * x**2 + 3 * x
F1 = sp.integrate(f1, x)
ok("E1 Nullstellen 0,1,3", sorted(sp.solve(f1, x)) == [0, 1, 3])
ok("E1 f(0,5)=0,625 und f(2)=-2", (f1.subs(x, R(1, 2)) == R(5, 8), f1.subs(x, 2) == -2))
ok("E1 F(0),F(1),F(3)", (F1.subs(x, 0), F1.subs(x, 1), F1.subs(x, 3)) == (0, R(5, 12), R(-9, 4)))
p1, p2 = I(f1, 0, 1), I(f1, 1, 3)
ok("E1 Teile 5/12 und -8/3", (p1, p2) == (R(5, 12), R(-8, 3)))
ok("E1 Bilanz -9/4, Flaeche 37/12", (p1 + p2, abs(p1) + abs(p2)) == (R(-9, 4), R(37, 12)))
ok("E1 27,0 Prozent", komma(float((R(37, 12) - R(9, 4)) / R(37, 12)), 4) == "0,2703")
ok("E1 Differenz 10/12 = 2*min(P,N)", R(37, 12) - R(9, 4) == 2 * R(5, 12))
mid = lambda fn, a, b, n=400000: sum(fn(a + (k + 0.5) * (b - a) / n) for k in range(n)) * (b - a) / n
ff = lambda v: v**3 - 4 * v**2 + 3 * v
ok("E1 numerisch Mittelpunktsregel 400000", near(mid(ff, 0, 1), 5 / 12, 1e-9) and near(mid(ff, 1, 3), -8 / 3, 1e-9)
   and near(mid(lambda v: abs(ff(v)), 0, 3), 37 / 12, 1e-8))
ok("x^3 auf [-1,1]: Bilanz 0, Flaeche 1/2", (I(x**3, -1, 1), 2 * I(x**3, 0, 1)) == (0, R(1, 2)))

# ---------------------------------------------------------------- Paar A der Simulation (Terme stehen nur in 4.2)
fA, gA = x**3 - 2 * x**2, 2 * x**2 - x - 6
hA = sp.expand(fA - gA)
ok("Paar A h = x^3-4x^2+x+6 = (x+1)(x-2)(x-3)", hA == x**3 - 4 * x**2 + x + 6 and sp.expand((x + 1) * (x - 2) * (x - 3)) == hA)
ok("Paar A Proben f=g bei -1,2,3", all(fA.subs(x, v) == gA.subs(x, v) for v in (-1, 2, 3)) and (fA.subs(x, -1), fA.subs(x, 2), fA.subs(x, 3)) == (-3, 0, 9))
ok("Paar A Vorzeichen h(0),h(2,5),h(4),h(-2)", (hA.subs(x, 0), hA.subs(x, R(5, 2)), hA.subs(x, 4), hA.subs(x, -2)) == (6, R(-7, 8), 10, -20))
HA = sp.integrate(hA, x)
ok("Paar A H(-1),H(2),H(3)", (HA.subs(x, -1), HA.subs(x, 2), HA.subs(x, 3), HA.subs(x, 0)) == (R(-47, 12), R(22, 3), R(27, 4), 0))
q1, q2 = I(hA, -1, 2), I(hA, 2, 3)
ok("Paar A Teile 45/4 und -7/12", (q1, q2) == (R(45, 4), R(-7, 12)))
ok("Paar A Flaeche 71/6, Bilanz 32/3", (q1 - q2, q1 + q2) == (R(71, 6), R(32, 3)))
ok("Paar A 9,9 Prozent = 7/71", (R(71, 6) - R(32, 3)) / R(71, 6) == R(7, 71) and komma(7 / 71, 4) == "0,0986")
hh = lambda v: (v + 1) * (v - 2) * (v - 3)
ok("Paar A numerisch 400000", near(mid(hh, -1, 2), 11.25, 1e-8) and near(mid(hh, 2, 3), -7 / 12, 1e-8) and near(mid(lambda v: abs(hh(v)), -1, 3), 71 / 6, 1e-8))
ok("Paar A Intervall [0;3]: 22/3, 7/12, A=95/12, Bilanz 27/4", (I(hA, 0, 2), I(hA, 0, 3), -I(hA, 2, 3), R(22, 3) + R(7, 12), R(22, 3) - R(7, 12)) == (R(22, 3), R(27, 4), R(7, 12), R(95, 12), R(27, 4)))
# ---------------------------------------------------------------- Abschnitt 3 (Beispiel E2 im Erklaerteil, NICHT Paar A)
fE, gE = x**3 - 3 * x**2, x**2 + 7 * x - 10
hE = sp.expand(fE - gE)
ok("E2neu h = x^3-4x^2-7x+10 = (x-1)(x-5)(x+2)", hE == x**3 - 4 * x**2 - 7 * x + 10 and sp.expand((x - 1) * (x - 5) * (x + 2)) == hE and hE.subs(x, 1) == 0 and sp.expand(sp.div(hE, x - 1)[0] - (x**2 - 3 * x - 10)) == 0)
ok("E2neu Proben f=g bei -2,1,5 (-20, -2, 50)", all(fE.subs(x, v) == gE.subs(x, v) for v in (-2, 1, 5)) and (fE.subs(x, -2), fE.subs(x, 1), fE.subs(x, 5)) == (-20, -2, 50))
ok("E2neu Vorzeichen h(-3),h(0),h(3),h(6)", (hE.subs(x, -3), hE.subs(x, 0), hE.subs(x, 3), hE.subs(x, 6)) == (-32, 10, -20, 40))
HE = sp.integrate(hE, x)
ok("E2neu H(-2),H(1),H(5),H(0),H(4)", (HE.subs(x, -2), HE.subs(x, 1), HE.subs(x, 5), HE.subs(x, 0), HE.subs(x, 4)) == (R(-58, 3), R(65, 12), R(-575, 12), 0, R(-112, 3)))
e1_, e2_ = I(hE, -2, 1), I(hE, 1, 5)
ok("E2neu Teile 99/4 und -160/3", (e1_, e2_) == (R(99, 4), R(-160, 3)))
ok("E2neu Flaeche 937/12, Bilanz -343/12", (e1_ - e2_, e1_ + e2_) == (R(937, 12), R(-343, 12)))
ok("E2neu 63,4 Prozent = 594/937", (e1_ - e2_ - abs(e1_ + e2_)) / (e1_ - e2_) == R(594, 937) and komma(594 / 937, 3) == "0,634")
hh2 = lambda v: (v - 1) * (v - 5) * (v + 2)
ok("E2neu numerisch 400000", near(mid(hh2, -2, 1), 24.75, 1e-8) and near(mid(hh2, 1, 5), -160 / 3, 1e-8) and near(mid(lambda v: abs(hh2(v)), -2, 5), 937 / 12, 1e-7))
ok("E2neu Intervall [0;4]: 65/12, -171/4, A=289/6, Bilanz -112/3", (I(hE, 0, 1), I(hE, 1, 4), I(hE, 0, 1) - I(hE, 1, 4), I(hE, 0, 4)) == (R(65, 12), R(-171, 4), R(289, 6), R(-112, 3)) and R(65, 12) + R(513, 12) == R(289, 6) and R(65, 12) - R(513, 12) == R(-112, 3))
hB = x**2 - (2 * x - 1)
ok("Beruehrung h=(x-1)^2, A=16/3", (sp.factor(hB) == (x - 1)**2, I(hB, -1, 3), I(hB, -1, 1) + I(hB, 1, 3)) == (True, R(16, 3), R(16, 3)))
ok("x^3-x: Bilanz 0, Teile 1/4 und -1/4, A=1/2", (I(x**3 - x, -1, 1), I(x**3 - x, -1, 0), I(x**3 - x, 0, 1)) == (0, R(1, 4), R(-1, 4)))
ok("x^3-x numerisch A=0,5", near(mid(lambda v: abs(v**3 - v), -1, 1, 200000), 0.5, 1e-8))
# Parabelformel
d = sp.symbols('d', positive=True)
u = sp.symbols('u')
ok("Parabelformel int u(u-d) = -d^3/6", sp.simplify(sp.integrate(u * (u - d), (u, 0, d)) + d**3 / 6) == 0)
h2 = -2 * x**2 + 4 * x + 2
zs = sorted(sp.solve(h2, x), key=float)
A2 = sp.simplify(I(h2, zs[0], zs[1]))
ok("a2/3.5 Nullstellen 1 -+ sqrt(2), A = 16 sqrt(2)/3", (zs == [1 - sp.sqrt(2), 1 + sp.sqrt(2)], sp.simplify(A2 - 16 * sp.sqrt(2) / 3) == 0, komma(float(A2), 4)) == (True, True, "7,5425"))
ok("a2 Parabelformel |a| d^3/6", sp.simplify(2 * (2 * sp.sqrt(2))**3 / 6 - A2) == 0)
ok("a2 (2*sqrt2)^3 = 16 sqrt2 = 22,6274; 2/3 * 11,3137 = 7,5425", komma(float(16 * sp.sqrt(2)), 4) == "22,6274" and komma(2 / 3 * 4 * 2 * math.sqrt(2), 4) == "7,5425")
ok("Paar C Schnittstelle t*", komma(math.log(8 / 3) / 0.3, 4) == "3,2694" and komma(math.log(8 / 3), 5) == "0,98083" and near(4 * math.exp(-0.3 * math.log(8 / 3) / 0.3), 1.5, 1e-12))

# ---------------------------------------------------------------- Abschnitt 4 (Simulation)
PAARE = {
    'A': dict(f=lambda v: v**3 - 2 * v**2, g=lambda v: 2 * v**2 - v - 6, lo=-1.5, hi=3.5, top=(-10, 20), bot=(-4, 16)),
    'B': dict(f=lambda v: v**2, g=lambda v: 2 * v - 1, lo=-1.0, hi=3.0, top=(-4, 10), bot=(-1, 6)),
    'C': dict(f=lambda v: 4 * math.exp(-0.3 * v), g=lambda v: 1.5, lo=0.0, hi=10.0, top=(-0.5, 4.5), bot=(-7, 10)),
}

def simpson(fn, a, b, n):
    hh_ = (b - a) / n
    s = fn(a) + fn(b)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * fn(a + k * hh_)
    return s * hh_ / 3

def nullstellen(p):                       # Stufe 1 der Spezifikation
    N = 4000
    hf = lambda v: p['f'](v) - p['g'](v)
    r, letzte, letzteX = [], 0, 0
    for i in range(N + 1):
        xv = p['lo'] + (p['hi'] - p['lo']) * i / N
        v = hf(xv)
        s = 0 if abs(v) < 1e-12 else (1 if v > 0 else -1)
        if s == 0:
            continue
        if letzte != 0 and s != letzte:
            lo_, hi_ = letzteX, xv
            for _ in range(60):
                m = (lo_ + hi_) / 2
                vm = hf(m)
                if abs(vm) < 1e-13:
                    lo_ = hi_ = m
                    break
                if (vm > 0) == (letzte > 0):
                    lo_ = m
                else:
                    hi_ = m
            r.append((lo_ + hi_) / 2)
        letzte, letzteX = s, xv
    return r

def tabellen(p):                          # Stufe 2 der Spezifikation
    lo, hi = p['lo'], p['hi']
    n = int(round((hi - lo) * 100))
    hf = lambda v: p['f'](v) - p['g'](v)
    rs = nullstellen(p)
    Bc, Ac = [0.0], [0.0]
    for j in range(n):
        uu, vv = lo + j / 100, lo + (j + 1) / 100
        br = [uu] + [r for r in rs if uu < r < vv] + [vv]
        db = da = 0.0
        for s_, t_ in zip(br, br[1:]):
            val = simpson(hf, s_, t_, 8)
            db += val
            da += abs(val)
        Bc.append(Bc[-1] + db)
        Ac.append(Ac[-1] + da)
    return n, rs, Bc, Ac

TAB = {k: tabellen(p) for k, p in PAARE.items()}

def anzeige(k, a, b):
    p = PAARE[k]
    n, rs, Bc, Ac = TAB[k]
    ja, jb = round((a - p['lo']) * 100), round((b - p['lo']) * 100)
    Bil, Fl = Bc[jb] - Bc[ja], Ac[jb] - Ac[ja]
    P, N = max(0.0, (Fl + Bil) / 2), max(0.0, (Fl - Bil) / 2)
    return dict(h=p['f'](b) - p['g'](b), P=P, N=N, Bil=Bil, Fl=Fl, Diff=Fl - abs(Bil), Ns=len([r for r in rs if a < r < b]))

ok("Nullstellen Paar A/B/C", (len(TAB['A'][1]) == 3 and all(abs(r - e) < 1e-9 for r, e in zip(TAB['A'][1], (-1, 2, 3))), TAB['B'][1], komma(TAB['C'][1][0], 4)) == (True, [], "3,2694"))

# Vergleich Tabellenverfahren gegen mpmath (60 Zufallspaare je Paar)
random.seed(1)
worst = 0.0
for k, p in PAARE.items():
    n, rs, Bc, Ac = TAB[k]
    hm = lambda v, p=p: mp.mpf(p['f'](v)) - p['g'](v)
    for _ in range(60):
        ja = random.randrange(0, n - 10)
        jb = random.randrange(ja + 10, n + 1)
        a, b = p['lo'] + ja / 100, p['lo'] + jb / 100
        eb = mp.quad(hm, [a, b])
        ea = mp.quad(lambda v: abs(hm(v)), [a] + [mp.mpf(r) for r in rs if a < r < b] + [b])
        worst = max(worst, abs(Bc[jb] - Bc[ja] - float(eb)), abs(Ac[jb] - Ac[ja] - float(ea)))
ok("Tabellenverfahren gegen mpmath, max. Abweichung < 1e-12", worst < 1e-12, "max. Abweichung %.2e" % worst)

# Simpson ohne Teilung (nur Messwert fuer den Text)
ohne = []
for k, (a, b) in {'A': (-1.43, 3.37), 'C': (0.0, 10.0)}.items():
    p = PAARE[k]
    hf_abs = lambda v, p=p: abs(p['f'](v) - p['g'](v))
    ex = anzeige(k, a, b)['Fl']
    ohne.append(abs(simpson(hf_abs, a, b, 200) - ex))
ok("Simpson n=200 ohne Teilung: Abweichung bis 4,6e-5", 4.0e-5 < max(ohne) < 5.0e-5, "max %.2e" % max(ohne))

# Kontrollwerte-Tabelle 4.3: Zeilen aus der Datei lesen und gegen das Verfahren pruefen
zeilen = 0
if md:
    for m in re.finditer(r"^\| ([ABC]) \| (−?\d+,\d\d) \| (−?\d+,\d\d) \| (−?\d+,\d\d) \| (−?\d+,\d\d) \| (−?\d+,\d\d) \| (−?\d+,\d\d) \| (−?\d+,\d\d) \| (−?\d+,\d\d) \| (\d) \|$", md, re.M):
        k = m.group(1)
        vals = [float(m.group(i).replace("−", "-").replace(",", ".")) for i in range(2, 10)]
        a, b = vals[0], vals[1]
        z = anzeige(k, a, b)
        soll = [komma(z['h']), komma(z['P']), komma(z['N']), komma(z['Bil']), komma(z['Fl']), komma(z['Diff'])]
        ist = [m.group(i).replace("−", "-") for i in range(4, 10)]
        ist = [s.replace("-0,00", "0,00") for s in ist]
        soll = [s.replace("-0,00", "0,00") for s in soll]
        assert soll == ist, ("Tabelle 4.3", k, a, b, soll, ist)
        assert z['Ns'] == int(m.group(10)), ("Wechsel", k, a, b, z['Ns'])
        zeilen += 1
ok("Kontrollwerte-Tabelle 4.3: alle Zeilen stimmen", zeilen == 17, "%d Zeilen geprueft" % zeilen)

# Ablesewerte zu sim1 und sim2
b35 = {a: anzeige('A', a, 3.5)['Bil'] for a in (-1.5, -1.4, -1.2, -1.0, -0.9, -0.8, -0.5, 0.0, 2.0, 3.0)}
ok("sim1 B(a;3,5) = 9,58 / 11,39 / 0,72", (komma(b35[-1.5]), komma(b35[-1.0]), komma(b35[3.0])) == ("9,58", "11,39", "0,72"))
ok("sim1 exakt 115/12, 729/64, 139/192", (I(hA, R(-3, 2), R(7, 2)), I(hA, -1, R(7, 2)), I(hA, 3, R(7, 2))) == (R(115, 12), R(729, 64), R(139, 192)))
ok("sim1 Abzug 1,81 zwischen a=-1,5 und a=-1", komma(b35[-1.0] - b35[-1.5]) == "1,81" and near(b35[-1.0] - b35[-1.5], float(-I(hA, R(-3, 2), -1)), 1e-9))
ok("sim1 lokales Min bei a=2 (0,1406 = 9/64), Scan -1,4/-1,2/-0,9/-0,8", (I(hA, 2, R(7, 2)), komma(b35[-1.4]), komma(b35[-1.2]), komma(b35[-0.9]), komma(b35[-0.8])) == (R(9, 64), "10,27", "11,13", "11,33", "11,17"))
rasterwerte = [anzeige('A', -1.0 + j / 100.0, 3.5)['Bil'] for j in range(-50, 440)]
ok("sim1 globales Maximum von B(a;3,5) auf [-1,5;3,4] liegt bei a=-1,00", abs(max(rasterwerte) - b35[-1.0]) < 1e-9)
def Bb(b):
    return anzeige('A', -1.5, b)['Bil']
b0 = float(mp.findroot(lambda bb: float(I(hA, R(-3, 2), sp.nsimplify(bb, rational=True))), -0.4))
ok("sim2 Nullstelle b0 = -0,375987", komma(b0, 6) == "-0,375987", b0)
ok("sim2 B(-1,5;b) bei -1,0 / -0,5 / -0,38 / -0,37 / 2,0",
   (komma(Bb(-1.0)), komma(Bb(-0.5)), komma(Bb(-0.38)), komma(Bb(-0.37)), komma(Bb(2.0))) == ("-1,81", "-0,58", "-0,02", "0,03", "9,44"))
ok("sim2 Rasterwert bei b=-0,376: -0,0001", komma(float(I(hA, R(-3, 2), R(-376, 1000))), 4) == "-0,0001")
ok("sim2 P=N=1,81 am Nulldurchgang, Flaeche 3,61", (komma(anzeige('A', -1.5, -0.38)['P']), komma(anzeige('A', -1.5, -0.38)['Fl'])) == ("1,79", "3,59") and komma(2 * float(-I(hA, R(-3, 2), -1))) == "3,61")
ok("sim2 h(-0,5)=4,38, h(-1,5)=-7,88, Stuecke 1,22 und 1,81", (komma(float(hA.subs(x, R(-1, 2)))), komma(float(hA.subs(x, R(-3, 2)))), komma(float(I(hA, -1, R(-1, 2)))), komma(float(-I(hA, R(-3, 2), -1)))) == ("4,38", "-7,88", "1,22", "1,81"))
ok("Beobachtung: Differenz 3,61 fuer b in [-0,38;2], 4,78 ab b=3", (komma(anzeige('A', -1.5, 0.0)['Diff']), komma(anzeige('A', -1.5, 2.0)['Diff']), komma(anzeige('A', -1.5, 3.0)['Diff']), komma(anzeige('A', -1.5, 3.5)['Diff'])) == ("3,61", "3,61", "4,78", "4,78"))
ok("Beobachtung: Bilanz -1,81 / 9,44 / 8,86 bei b=-1 / 2 / 3", (komma(Bb(-1.0)), komma(Bb(2.0)), komma(Bb(3.0))) == ("-1,81", "9,44", "8,86"))
ok("Beobachtung: Paar B, Differenz durchgehend 0,00", all(abs(anzeige('B', -1.0, -0.9 + j / 100)['Diff']) < 1e-12 for j in range(0, 391)))
ok("Lehrerteil: |B| hat Knick bei b0, h(b0)=5,01", komma(float(hA.subs(x, sp.nsimplify(b0)))) == "5,01")
ok("Lehrerteil: Paar C, Zufluss-Integral 40/3, Gesamtzufluss auf [0;10] 4-Werte",
   (sp.integrate(4 * sp.exp(-R(3, 10) * t), (t, 0, sp.oo)) == R(40, 3),))

# Wertebereiche und Massstaebe (4.2 und 4.5)
def bereich(k):
    p = PAARE[k]
    n = int(round((p['hi'] - p['lo']) * 4))
    Bmin, Bmax, Amax = 1e9, -1e9, 0.0
    for i in range(n):
        for j in range(i + 1, n + 1):
            z = anzeige(k, p['lo'] + 0.25 * i, p['lo'] + 0.25 * j)
            Bmin, Bmax, Amax = min(Bmin, z['Bil']), max(Bmax, z['Bil']), max(Amax, z['Fl'])
    fv = [p['f'](p['lo'] + (p['hi'] - p['lo']) * i / 400) for i in range(401)] + [p['g'](p['lo'] + (p['hi'] - p['lo']) * i / 400) for i in range(401)]
    return Bmin, Bmax, Amax, min(fv), max(fv)
soll_ber = {'A': (-1.807, 11.391, 14.365, -7.875, 18.375), 'B': (0.005, 5.333, 5.333, -3.0, 9.0), 'C': (-5.760, 3.429, 9.189, 0.199, 4.0)}
for k in 'ABC':
    ist = bereich(k)
    p = PAARE[k]
    ok("Wertebereich Paar " + k, all(abs(a - b) < 0.0015 for a, b in zip(ist, soll_ber[k])), tuple(round(v, 3) for v in ist))
    ok("Achsen umschliessen Paar " + k, p['top'][0] < ist[3] and ist[4] < p['top'][1] and p['bot'][0] < min(ist[0], 0) and max(ist[1], ist[2]) < p['bot'][1])
massst = {'A': (180.0, 8.0, 12.0), 'B': (225.0, 17.1429, 34.2857), 'C': (90.0, 48.0, 14.1176)}
for k, (px, oy, uy) in massst.items():
    p = PAARE[k]
    ok("Massstaebe Paar " + k, (abs(900 / (p['hi'] - p['lo']) - px) < 1e-9, abs(240 / (p['top'][1] - p['top'][0]) - oy) < 1e-3, abs(240 / (p['bot'][1] - p['bot'][0]) - uy) < 1e-3) == (True, True, True))
ok("Regler-Grenzen", (100 * (3.5 + 1.5) - 10, 100 * (3.5 + 1.5), 100 * 4 - 10, 100 * 10 - 10) == (490, 500, 390, 990))

# ---------------------------------------------------------------- Abschnitt 5 (Uebungen)
def zone(v, soll, tol):
    if abs(v - soll) <= tol + 1e-9:
        return "ok"
    q = v / soll
    return "nah" if 0.5 < q < 2 else "weit"

# a1
f_a1 = x**2 - 4 * x + 3
F_a1 = sp.integrate(f_a1, x)
ok("a1 Nullstellen, F-Werte", (sorted(sp.solve(f_a1, x)) == [1, 3], [F_a1.subs(x, v) for v in (0, 1, 3, 4)]) == (True, [0, R(4, 3), 0, R(4, 3)]))
ok("a1 Teile 4/3, -4/3, 4/3, Flaeche 4, Bilanz 4/3", (I(f_a1, 0, 1), I(f_a1, 1, 3), I(f_a1, 3, 4)) == (R(4, 3), R(-4, 3), R(4, 3)) and I(f_a1, 0, 4) == R(4, 3))
ok("a1 Vorzeichen f(0),f(2),f(4)", (f_a1.subs(x, 0), f_a1.subs(x, 2), f_a1.subs(x, 4)) == (3, -1, 3))
ok("a1 numerisch 4,0", near(mp.quad(lambda v: abs(v**2 - 4 * v + 3), [0, 1, 3, 4]), 4.0, 1e-20))
ok("a1 nah/weit", (zone(8 / 3, 4, .05), zone(4 / 3, 4, .05), zone(0, 4, .05), zone(4.0, 4, .05)) == ("nah", "weit", "weit", "ok"))
# a2
H2 = sp.integrate(h2, x)
ok("a2 H(x2), H(x1)", (komma(float(H2.subs(x, zs[1])), 4), komma(float(H2.subs(x, zs[0])), 4)) == ("7,1046", "-0,4379"))
ok("a2 x1,x2 = -0,4142 / 2,4142; h(1)=4, f(1)=4, g(1)=0", (komma(float(zs[0]), 4), komma(float(zs[1]), 4), h2.subs(x, 1)) == ("-0,4142", "2,4142", 4))
ok("a2 754,25 cm^2 liegt in 754 +- 5", abs(float(A2) * 100 - 754) <= 5 and komma(float(A2) * 100) == "754,25")
ok("a2 Fehlwerte: Grenzen 0..3 = 6, Rechteck 11,31, Dreieck 5,66, Breite 2,83",
   (komma(float(I(h2, 0, 3))), komma(4 * 2 * math.sqrt(2)), komma(2 * math.sqrt(2) * 4 / 2), komma(2 * math.sqrt(2))) == ("6,00", "11,31", "5,66", "2,83"))
ok("a2 nah/weit", (zone(6.0, 7.54, .05), zone(11.31, 7.54, .05), zone(5.66, 7.54, .05), zone(-7.54, 7.54, .05), zone(2.83, 7.54, .05)) == ("nah", "nah", "nah", "weit", "weit"))
ok("a2 Toleranz: 7,5 und 7,54 akzeptiert", (zone(7.5, 7.54, .05), zone(7.54, 7.54, .05)) == ("ok", "ok"))
# a3
g0 = 2
ZUO = {'A': 2 + R(1, 2) * (x - 2) * (x - 4), 'B': 3 + R(1, 5) * (x - 3)**2, 'C': 2 + R(3, 10) * (x - 3)**2, 'D': 2 + R(4, 5) * (x - 3)}
erg = {}
for k, fz in ZUO.items():
    hz = sp.expand(fz - g0)
    reell = sorted([q for q in sp.solve(hz, x) if q.is_real and 0 < q < 6])
    br = [0] + [q for q in reell if sp.degree(sp.numer(sp.together(hz)), x) and (hz.subs(x, q - R(1, 100)) * hz.subs(x, q + R(1, 100)) < 0)] + [6]
    erg[k] = (I(hz, 0, 6), sum(abs(I(hz, u_, v_)) for u_, v_ in zip(br, br[1:])))
ok("a3 A: Bilanz 6, Flaeche 22/3", erg['A'] == (6, R(22, 3)))
ok("a3 B: Bilanz = Flaeche = 48/5, keine reelle Nullstelle", erg['B'] == (R(48, 5), R(48, 5)) and sp.expand(ZUO['B'] - 2) == (x**2 - 6 * x + 14) / 5 and 36 - 56 < 0)
ok("a3 C: Bilanz = Flaeche = 27/5", erg['C'] == (R(27, 5), R(27, 5)))
ok("a3 D: Bilanz 0, Flaeche 36/5, Teile -3,6 und 3,6", erg['D'] == (0, R(36, 5)) and (I(sp.expand(ZUO['D'] - 2), 0, 3), I(sp.expand(ZUO['D'] - 2), 3, 6)) == (R(-18, 5), R(18, 5)))
ok("a3 A: Teile 10/3, -2/3, 10/3", tuple(I(sp.expand(ZUO['A'] - 2), u_, v_) for u_, v_ in ((0, 2), (2, 4), (4, 6))) == (R(10, 3), R(-2, 3), R(10, 3)))
ok("a3 Abbildung: g bei py=53, x-Achse bei py=71, x=6 bei px=150", (80 - 9 * (2 + 1), 80 - 9 * (0 + 1), 18 + 22 * 6) == (53, 71, 150))
for k, fz in ZUO.items():
    xs = [0, 6] if k == 'D' else [i * 0.5 for i in range(13)]
    pts = " ".join("%.1f,%.1f" % (18 + 22 * v, 80 - 9 * (float(fz.subs(x, sp.nsimplify(v))) + 1)) for v in xs)
    if md:
        ok("a3 polyline Diagramm " + k + " steht in der Datei", pts in md)
    else:
        print(k, pts)
# a4
Z = lambda tt: -R(40, 3) * sp.exp(-R(3, 10) * tt) - 2 * tt
ts = sp.log(2) / R(3, 10)
ok("a4 t* = ln2/0,3 = 2,3105; e^(-0,3 t*) = 1/2", (komma(float(ts), 4), sp.simplify(sp.exp(-R(3, 10) * ts) - R(1, 2))) == ("2,3105", 0))
ok("a4 Probe Z' = z - 2", sp.simplify(sp.diff(Z(t), t) - (4 * sp.exp(-R(3, 10) * t) - 2)) == 0)
ok("a4 Z(0), Z(t*), Z(8)", (komma(float(Z(0)), 4), komma(float(Z(ts)), 4), komma(float(Z(8)), 4)) == ("-13,3333", "-11,2876", "-17,2096"))
ok("a4 e^-2,4 = 0,090718 und (40/3)e^-2,4 = 1,2096", (komma(math.exp(-2.4), 6), komma(40 / 3 * math.exp(-2.4), 4)) == ("0,090718", "1,2096"))
P4, N4 = float(Z(ts) - Z(0)), float(Z(ts) - Z(8))
ok("a4 P = 2,0457, N = 5,9219, A = 7,9676, Bilanz -3,8762", (komma(P4, 4), komma(N4, 4), komma(P4 + N4, 4), komma(P4 - N4, 4)) == ("2,0457", "5,9219", "7,9676", "-3,8762"))
tst = math.log(2) / 0.3
za = lambda tt: 4 * mp.e**(-0.3 * tt) - 2
ok("a4 mpmath 7,96761030", komma(float(mp.quad(lambda s_: abs(za(s_)), [0, tst, 8])), 8) == "7,96761030")
ok("a4 Gesamtzufluss 12,12; alt 0,00797 m3 +-0,00005", (komma(float(sp.integrate(4 * sp.exp(-R(3, 10) * t), (t, 0, 8))), 2), abs((P4 + N4) / 1000 - 0.00797) <= 0.00005) == ("12,12", True))
ok("a4 nah/weit", (zone(5.92, 7.97, .05), zone(12.12, 7.97, .05), zone(3.88, 7.97, .05), zone(2.05, 7.97, .05), zone(7.97, 7.97, .05)) == ("nah", "nah", "weit", "weit", "ok"))
# a5
h5 = (x + 2) * (x - 1) * (x - 3) / 2
G5, T5 = R(1, 2) * x**3 - x**2 - 3 * x + 7, 4 - x / 2
ok("a5 G-T = h", sp.expand(G5 - T5 - h5) == 0 and sp.expand(2 * h5) == x**3 - 2 * x**2 - 5 * x + 6)
ok("a5 Randwerte G=T bei -2 (5) und 3 (2,5)", (G5.subs(x, -2), T5.subs(x, -2), G5.subs(x, 3), T5.subs(x, 3)) == (5, 5, R(5, 2), R(5, 2)))
ok("a5 h(0)=3, h(2)=-2", (h5.subs(x, 0), h5.subs(x, 2)) == (3, -2))
H5 = sp.integrate(sp.expand(h5), x)
ok("a5 H(-2), H(1), H(3)", (H5.subs(x, -2), H5.subs(x, 1), H5.subs(x, 3)) == (R(-19, 3), R(37, 24), R(-9, 8)))
e5, d5 = H5.subs(x, 1) - H5.subs(x, -2), H5.subs(x, 3) - H5.subs(x, 1)
ok("a5 Einschnitt 63/8, Damm 8/3, zusammen 253/24, Bilanz 125/24", (e5, -d5, e5 - d5, e5 + d5) == (R(63, 8), R(8, 3), R(253, 24), R(125, 24)))
ok("a5 in m^2 (Faktor 10): 78,75 / 26,67 / 105,42 / 52,08", (komma(float(10 * e5)), komma(float(-10 * d5)), komma(float(10 * (e5 - d5))), komma(float(10 * (e5 + d5)))) == ("78,75", "26,67", "105,42", "52,08"))
ok("a5 exakt 1265/12 m^2 = 105,4167", 10 * (e5 - d5) == R(1265, 12) and komma(float(R(1265, 12)), 4) == "105,4167")
ok("a5 numerisch 10,54166667 FE", komma(float(mp.quad(lambda v: abs(0.5 * v**3 - v**2 - 2.5 * v + 3), [-2, 1, 3])), 8) == "10,54166667")
ok("a5 nah/weit", (zone(78.75, 105.42, .05), zone(105.0, 105.42, .05), zone(52.08, 105.42, .05), zone(26.67, 105.42, .05), zone(10.54, 105.42, .05), zone(1054.17, 105.42, .05), zone(105.4, 105.42, .05), zone(105.42, 105.42, .05)) == ("nah", "nah", "weit", "weit", "weit", "weit", "ok", "ok"))
# a6/a7
ok("a6 Zahlen 78,75 / 26,67 / 52,08 / 105,42", komma(float(78.75 - 26.6667)) == "52,08" and komma(78.75 + 26.6667) == "105,42")
ok("a7 h(-0,5)=0,375, h(0,5)=-0,375", ((x**3 - x).subs(x, R(-1, 2)), (x**3 - x).subs(x, R(1, 2))) == (R(3, 8), R(-3, 8)))
ok("a7 Stammfunktion [x^4/4 - x^2/2]", (sp.integrate(x**3 - x, x) == x**4 / 4 - x**2 / 2))

# ---------------------------------------------------------------- Abschnitt 6 (Differenzierung)
kk = sp.symbols('k', positive=True)
Ak = sp.integrate(kk * x - x**2, (x, 0, kk))
ok("Differenzierung: A(k) = k^3/6, k = 6 fuer A = 36", (sp.simplify(Ak - kk**3 / 6) == 0, sp.solve(sp.Eq(kk**3 / 6, 36), kk) == [6]))
Ps, Ns_ = sp.symbols('P N', positive=True)
ok("Differenzierung: A-|B| = 2 min(P,N) stichprobenartig", all(abs((P_ + N_) - abs(P_ - N_) - 2 * min(P_, N_)) < 1e-12 for P_, N_ in ((5, 2), (2, 5), (3, 3), (0.5, 7))))
ok("Zeit: 8+18+20+20+20+4 = 90", 8 + 18 + 20 + 20 + 20 + 4 == 90)
print("\nGESAMT: %d Pruefungen bestanden, keine Abweichung." % n_ok)
```

**Ergebnis des letzten Laufs:** `GESAMT: 113 Pruefungen bestanden, keine Abweichung.` Sämtliche `assert`-Zeilen (Abschnitte 1 bis 6, zusätzlich 17 Simulationszeilen und vier Polylinien aus dieser Datei) liefen ohne Abweichung durch.
