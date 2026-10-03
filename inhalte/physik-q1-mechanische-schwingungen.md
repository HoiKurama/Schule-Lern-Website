# Modulinhalt: Mechanische Schwingungen — Feder- und Fadenpendel, Dämpfung, Resonanz

Modul: `physik-q1-mechanische-schwingungen`
Fach: Physik, Leistungskurs Q1
Inhaltsfeld (Chip im Seitenkopf, **wörtlich** nach `fachliches/kernlehrplan-nrw.md`): **Schwingende Systeme und Wellen**
Akzentfarben: Physik, `--akzent: #1d4ed8`, `--akzent-hell: #eff6ff`, `--akzent-rand: #bfdbfe` (nichts ändern)
Titel der Seite: *Mechanische Schwingungen*
Untertitel im Kopf: *Vom Federpendel zur Resonanz: Wie ein schwingendes System auf Rückstellkraft, Reibung und Antrieb antwortet*
Chips: `Physik LK · Q1` · `Inhaltsfeld: Schwingende Systeme und Wellen` · `ca. 150 Minuten`

**Stand der Einordnung (offen markiert).** `fachliches/kernlehrplan-nrw.md` nennt für Q1 nur den
Namen des Inhaltsfeldes, keine Kompetenzerwartungen im Wortlaut. Deshalb gilt:
- Der Chip nennt das Inhaltsfeld wörtlich. Das ist gesichert.
- Die „Ich kann …"-Sätze in Abschnitt 6 sind **eigene Formulierungen** in Anlehnung an die vier
  Kompetenzbereiche, keine Zitate. Nicht als Kernlehrplan-Text ausgeben.
- **Offen, bitte nachfragen:** (a) Ob Dämpfung, erzwungene Schwingung und Resonanz im schulinternen
  Lehrplan in Q1 stehen oder ins Wellenmodul wandern. (b) Ob das logarithmische Dekrement
  Pflicht ist oder Vertiefung. (c) Exakte Ausdrucksform der Verbindlichkeit
  im Zentralabitur (siehe Abschnitt 6.2).

**Abgrenzung — verbindlich.**

| Gehört in dieses Modul | Gehört **nicht** hierher |
|---|---|
| Rückstellkraft, harmonische Schwingung, Federpendel, Fadenpendel (Kleinwinkel) | Wellen, Wellenausbreitung, Interferenz, stehende Wellen (Folgemodul) |
| Auslenkung, Geschwindigkeit, Beschleunigung als Funktionen der Zeit | Elektromagnetischer Schwingkreis (Verweis als Ausblick in einem Satz) |
| Energieumwandlung <span class="m">E_kin ↔ E_pot</span> | Gekoppelte Pendel, Schwebung |
| Geschwindigkeitsproportionale Dämpfung, Abklingkonstante, Dämpfungsfälle | Nichtlineare Dämpfung (Coulomb-Reibung), chaotisches Pendel |
| Erzwungene Schwingung, Resonanzkurve, Phasenlage, Resonanzfrequenz | Fourier-Zerlegung, Parametrische Anregung |

**Stellung im Curriculum.** Kein Vorgängermodul im Projekt. Voraussetzung ist Mechanik der EF
(Newton II, Energieerhaltung, Kreisbewegung als Winkelgeschwindigkeit). Das Modul steht **vor**
dem geplanten Wellenmodul. Ausblick auf `physik-q1-induktion` (Wirbelstrombremse als Dämpfung) und
den elektromagnetischen Schwingkreis nur als **ein Satz** ohne Rechnung.

---

## 0 · Konventionen, Konstanten und Formelzeichen

**Diese Festlegungen gelten für jede Abbildung, Simulation, Aufgabe und Musterlösung. Der Bauagent
weicht davon nicht ab.**

### 0.1 Konstanten

| Größe | Zeichen | Wert | Einheit |
|---|---|---|---|
| Ortsfaktor (mit dem gerechnet wird) | g | 9,81 | m/s² |
| Kreiszahl | π | 3,14159… | — |

Es gibt keine weiteren Naturkonstanten. Alle übrigen Zahlen sind Aufgabenvorgaben.

### 0.2 Formelzeichen

| Zeichen | Bedeutung | Einheit | Anmerkung |
|---|---|---|---|
| <span class="m">x</span> | Auslenkung aus der Ruhelage | m | vorzeichenbehaftet; Ruhelage <span class="m">x = 0</span> |
| <span class="m">x̂</span> bzw. <span class="m">x_max</span> | Amplitude (Betrag der größten Auslenkung) | m | **im ganzen Modul `x_max`**, für die erzwungene Schwingung `x_max(ω_e)` |
| <span class="m">T</span> | Schwingungsdauer (Periode) | s | |
| <span class="m">f</span> | Frequenz, <span class="m">f = 1/T</span> | Hz = 1/s | |
| <span class="m">ω</span> | Kreisfrequenz, <span class="m">ω = 2π/T = 2π·f</span> | rad/s (= 1/s) | |
| <span class="m">ω₀</span> | Eigenkreisfrequenz des **ungedämpften** Systems | rad/s | <span class="m">f₀ = ω₀/(2π)</span>, <span class="m">T₀ = 2π/ω₀</span> |
| <span class="m">D</span> | Federkonstante (Richtgröße) | N/m | **nicht** mit Kapazität o. Ä. verwechseln |
| <span class="m">b</span> | Reibungskoeffizient, <span class="m">F_R = −b·v</span> | kg/s = N·s/m | |
| <span class="m">δ</span> | Abklingkonstante, <span class="m">δ = b/(2m)</span> | 1/s | |
| <span class="m">ω_d</span> bzw. <span class="m">T_d</span> | Kreisfrequenz bzw. Periode der **gedämpften** freien Schwingung | rad/s bzw. s | <span class="m">ω_d = √(ω₀² − δ²)</span> |
| <span class="m">Λ</span> | logarithmisches Dekrement, <span class="m">Λ = δ·T_d</span> | 1 | dimensionslos |
| <span class="m">F₀</span> | Amplitude der Erregerkraft | N | |
| <span class="m">ω_e</span>, <span class="m">f_e</span> | Kreisfrequenz bzw. Frequenz der Erregung (Index **e** = Erreger) | rad/s bzw. Hz | Zeichen `ω_e` nie ohne Index verwenden |
| <span class="m">ω_res</span> | Kreisfrequenz, bei der die Amplitude maximal wird | rad/s | <span class="m">ω_res = √(ω₀² − 2δ²)</span> |
| <span class="m">φ</span> | Phasenverschiebung der Antwort gegen die Erregung | rad bzw. ° | Antwort **hinkt hinterher**, <span class="m">0 ≤ φ ≤ π</span> |

**Kollisionswarnung an den Bauagenten.**
- `δ` (Abklingkonstante) und `Δ` (Differenz) sind verschiedene Zeichen. `data-tex` immer `\delta`
  bzw. `\Delta`.
- `T` ist Schwingungsdauer, nie die Einheit Tesla. Einheit Tesla kommt im Modul nicht vor.
- `D` ist die Federkonstante. Die Kurzform „D" darf nirgends anders auftauchen.
- Zwei Perioden nie verwechseln: `T₀` (ohne Dämpfung) und `T_d` (mit Dämpfung).

### 0.3 Vorzeichenkonvention (verbindlich)

Die Auslenkung <span class="m">x</span> ist nach **rechts positiv**. Die Rückstellkraft
<span class="m">F = −D·x</span> zeigt der Auslenkung entgegen; das Minuszeichen wird **nie**
weggelassen. Die Newton-Gleichung lautet durchgehend

- `data-tex`: `m\,\ddot{x} = -D\,x - b\,\dot{x} + F_0 \sin(\omega_e t)`
- `data-plain`: `m·x'' = −D·x − b·x' + F₀·sin(ω_e·t)`

mit den Sonderfällen <span class="m">b = 0, F₀ = 0</span> (ungedämpft, frei),
<span class="m">F₀ = 0</span> (gedämpft, frei) und <span class="m">F₀ ≠ 0</span> (erzwungen).
Punkte über Symbolen bedeuten Ableitung nach der Zeit; in `data-plain` stehen Striche
(<span class="m">x'</span>, <span class="m">x''</span>). Geschwindigkeit und Beschleunigung sind
<span class="m">v = ẋ</span> und <span class="m">a = ẍ</span>.

### 0.4 Farben in Abbildungen und Simulation

| Objekt | Farbe |
|---|---|
| Auslenkung x(t) | `#1d4ed8` |
| Geschwindigkeit v(t) | `#0d7a52` |
| Beschleunigung a(t) | `#b42318` |
| Hüllkurve ± x_max·e^(−δt), gestrichelt | `#5b6b7f` |
| Erregerkraft | `#8a6100` |
| kinetische / potentielle / gesamte Energie | `#0d7a52` / `#b42318` / `#0f2135` |

### 0.5 Einheiten und Zahlendarstellung

Dezimalkomma überall, auch in Anzeigen (`fmt`). Auslenkungen in Text und Anzeige in **cm**
(Simulation: „cm"), in Formeln in **m**. Periodendauern in s mit vier gültigen Stellen in
Musterlösungen, in Anzeigen mit drei Nachkommastellen. Einheit `1/s` für δ (nicht „s⁻¹" im Fließtext
der Aufgaben, aber `data-plain` darf `s⁻¹` verwenden).

---

## 1 · Einstieg

`<section id="einstieg">`, `.stufe`-Nummer **1**, Überschrift **Einstieg**.

### 1.1 Aufhänger (zwei Absätze, kein Lehrbuchton)

**Absatz 1:**

> Ein Kind sitzt auf einer Schaukel mit drei Metern langen Ketten und wird angestoßen. Es schwingt
> hin und her, und alle dreieinhalb Sekunden ist es wieder am Ausgangspunkt. Stößt du im richtigen
> Moment nach, schaukelt es mit jedem Mal höher; stößt du im falschen Moment, bremst du es. Und
> hörst du ganz auf, wird die Schaukel von selbst langsamer, obwohl niemand sie bremst. Drei
> Beobachtungen, ein System — und bei keiner sagt der Alltag, warum es so ist.

**Absatz 2:**

> Dieselbe Physik steckt in einer Waschmaschine. Beim Hochfahren der Schleuderdrehzahl schüttelt sie
> sich kurz heftig und wandert über den Boden, bei voller Drehzahl dagegen läuft sie erstaunlich
> ruhig. Schneller heißt hier also nicht stärker, sondern nach einem kurzen Höhepunkt wieder
> schwächer. Auf dieser Seite klärst du drei Fragen: Was legt fest, wie schnell ein System
> schwingt? Warum verschwindet eine Schwingung von selbst? Und warum genügt ein rhythmischer, aber
> schwacher Antrieb, um riesige Ausschläge zu erzeugen — und warum nur zu bestimmten Zeiten?

**Rechnerische Deckung der Zahlen im Aufhänger** (Kontrollrechnung, Abschnitt 7):

| Aussage im Text | Rechnung | Ergebnis |
|---|---|---|
| „alle dreieinhalb Sekunden" | T = 2π·√(3,0 m / 9,81 m/s²) | 3,4746 s ≈ 3,5 s |

Der Bauagent schreibt nur die gerundete Aussage („dreieinhalb Sekunden") in den Fließtext. Darunter
steht ein `<details>` mit Zusammenfassung *Woher die dreieinhalb Sekunden?* und dem Text
„Die Formel dazu leitest du in Abschnitt 2 her: <span class="m">T = 2π·√(l/g)</span>. Für
<span class="m">l = 3,0 m</span> ergibt das <span class="m">T = 3,47 s</span>. Die Waschmaschine
wird in den Aufgaben wieder aufgegriffen." Kein weiterer Zahlenwert zur Waschmaschine (Drehzahlen o. Ä.
sind nicht belegt und bleiben weg).

### 1.2 Vorwissensfragen

Kopf der Karte wie im Referenzmodul: `<div class="karte"><h3>Vorwissen prüfen</h3>` mit dem grauen
Hinweissatz *„Drei Fragen aus der Sekundarstufe I und der Einführungsphase. Wenn du hier hängst,
lohnt sich ein Blick zurück, bevor du weitermachst."* Alle drei als
`<div class="aufgabe" data-mc="…" style="border:none;padding:0;…">`, jeweils mit Radios `name="vwN"`.

---

#### vw1 — Federkraft (Sek I, Hookesches Gesetz)

**Frage:**

> Eine Schraubenfeder folgt dem Hookeschen Gesetz. Du verdreifachst ihre Auslenkung aus der
> Ruhelage. Was geschieht mit der Rückstellkraft?

| `data-i` | Option |
|---|---|
| 0 | Sie bleibt gleich, weil die Federkonstante <span class="m">D</span> sich nicht ändert. |
| 1 | Sie verdreifacht sich, weil <span class="m">F = D·s</span> eine Proportionalität ist. |
| 2 | Sie verneunfacht sich, weil in der Federenergie <span class="m">½·D·s²</span> ein Quadrat steht. |

`r: 1`

**Feedback:**

- `fb[0]`: „Die Federkonstante D bleibt tatsächlich gleich, aber sie ist der Proportionalitätsfaktor,
  nicht die Kraft. Im Gesetz F = D·s steht s selbst im Term: Dreifache Auslenkung heißt dreifache
  Kraft. Bei 4,0 cm und 2,0 N sind es bei 12 cm eben 6,0 N."
- `fb[1]`: „Richtig. Aus F = D·s folgt für 4,0 cm und 2,0 N die Federkonstante D = 50 N/m. Bei
  12 cm wirkt dann 6,0 N. Die Rückstellkraft wächst linear mit der Auslenkung — genau diese
  Eigenschaft macht das Federpendel in Abschnitt 2 harmonisch."
- `fb[2]`: „Das Quadrat gehört zur **Energie** (E = ½·D·s²), nicht zur Kraft. Wer beide
  Formeln verwechselt, bekommt hier 18 N statt 6,0 N. Merke: Kraft ~ s, Energie ~ s²."

---

#### vw2 — Energie beim Pendel (EF Mechanik)

**Frage:**

> Ein Fadenpendel wird ausgelenkt und ohne Anstoß losgelassen. Reibung ist vernachlässigbar. An
> welcher Stelle seiner Bahn ist die Geschwindigkeit des Pendelkörpers am größten?

| `data-i` | Option |
|---|---|
| 0 | Am Umkehrpunkt, weil dort die Auslenkung am größten ist. |
| 1 | An der tiefsten Stelle, weil dort die gesamte Energie kinetische Energie ist. |
| 2 | Überall gleich, weil die Gesamtenergie erhalten bleibt. |

`r: 1`

**Feedback:**

- `fb[0]`: „Am Umkehrpunkt kehrt die Bewegung um, dort ist die Geschwindigkeit für einen Augenblick
  null. Die gesamte Energie steckt dort als Höhenenergie im Körper. Größte Auslenkung heißt größte
  Höhenenergie, nicht größte Geschwindigkeit."
- `fb[1]`: „Richtig. Beim Herabschwingen wird Höhenenergie in Bewegungsenergie umgewandelt; an der
  tiefsten Stelle ist E_pot minimal, also E_kin und damit v maximal. Diese Umwandlung ist der
  Kern des Energiebilds in Abschnitt 2.4."
- `fb[2]`: „Erhalten bleibt die **Summe** aus kinetischer und potentieller Energie, nicht die
  einzelnen Anteile. Sie tauschen sich ständig aus, deshalb ändert sich die Geschwindigkeit
  laufend."

---

#### vw3 — Periode und Frequenz (Sek I)

**Frage:**

> Ein Fadenpendel führt in 8,0 s genau 4 vollständige Schwingungen aus. Wie groß ist seine
> Frequenz?

| `data-i` | Option |
|---|---|
| 0 | 0,50 Hz |
| 1 | 2,0 Hz |
| 2 | 32 Hz |

`r: 0`

**Feedback:**

- `fb[0]`: „Richtig. Eine Schwingung dauert T = 8,0 s / 4 = 2,0 s, und f = 1/T = 0,50 Hz. Zwei Sekunden
  pro Schwingung sind eben eine halbe Schwingung pro Sekunde."
- `fb[1]`: „Die 2,0 sind die **Periode** T in Sekunden. Die Frequenz ist der Kehrwert
  f = 1/T und hat die Einheit Hz = 1/s. Wer die Periode nicht umkehrt, verwechselt „Sekunden pro
  Schwingung" mit „Schwingungen pro Sekunde"."
- `fb[2]`: „Hier wurde 8,0 · 4 gerechnet. Die Frequenz ist die Zahl der Schwingungen **geteilt
  durch** die Zeit, nicht mal die Zeit. Plausibilitätsprobe: 32 Schwingungen pro Sekunde wären
  ein Ton, kein Pendel."

---

## 2 · Erklärteil — von der Rückstellkraft zur harmonischen Schwingung

`<section id="grundlagen">`, `.stufe`-Nummer **2**,
Überschrift **Von der Rückstellkraft zur harmonischen Schwingung**.

### 2.1 Was eine Schwingung ausmacht

**Fließtext:**

> Ein System schwingt, wenn es um eine **Ruhelage** hin und her läuft. Die Ruhelage ist die Stelle,
> an der es ohne Anstoß liegen bleibt. Dort verschwindet die Kraft. Wird das System ausgelenkt,
> wirkt eine **Rückstellkraft**, die zur Ruhelage zeigt. Dazu kommt die Trägheit: Beim Durchgang
> durch die Ruhelage ist die Kraft null, aber der Körper hat Geschwindigkeit und läuft weiter.
> **Rückstellkraft plus Trägheit** — mehr braucht es nicht, damit ein System schwingt.
>
> Beschrieben wird das mit vier Größen. Die **Auslenkung** <span class="m">x(t)</span> gibt den
> Ort relativ zur Ruhelage an. Die **Amplitude** <span class="m">x_max</span> ist ihr größter Betrag.
> Die **Schwingungsdauer** <span class="m">T</span> ist die Zeit für einen vollständigen Hin- und
> Rückweg, die **Frequenz** ist <span class="m">f = 1/T</span>. Weil wir gleich mit Sinus und Kosinus
> rechnen, ist die **Kreisfrequenz** bequemer:
>
> - `data-tex` (Blockformel): `\omega = \dfrac{2\pi}{T} = 2\pi f \qquad [\omega] = 1\,\dfrac{\mathrm{rad}}{\mathrm{s}}`
> - `data-plain`: `ω = 2π/T = 2π·f     [ω] = 1 rad/s`
>
> Ein Beispiel: Bei <span class="m">T = 0,80 s</span> ist <span class="m">f = 1,25 Hz</span> und
> <span class="m">ω = 7,854 rad/s</span>. Die Zahl <span class="m">2π</span> steckt darin, weil
> <span class="m">ω·t</span> der Winkel im Bogenmaß ist, den ein Punkt auf einem Kreis in der Zeit
> <span class="m">t</span> zurücklegt: Eine volle Schwingung entspricht einem vollen Umlauf
> <span class="m">2π</span>.

**Definition (`<div class="merksatz">`, Titel *Harmonische Schwingung*):**

> Eine Schwingung heißt **harmonisch**, wenn die Auslenkung sinusförmig von der Zeit abhängt:
> <span class="m">x(t) = x_max · sin(ω·t + φ₀)</span>. Ob ein reales System so schwingt, ist keine
> Frage der Definition, sondern der Rückstellkraft — das klärt Abschnitt 2.2.

Auslenkung, Geschwindigkeit und Beschleunigung folgen durch Ableiten. Für
<span class="m">x(t) = x_max·sin(ωt)</span>:

- `data-tex` (Blockformel): `x = x_{\max}\sin(\omega t), \quad v = \dot{x} = x_{\max}\,\omega\cos(\omega t), \quad a = \ddot{x} = -x_{\max}\,\omega^2\sin(\omega t)`
- `data-plain`: `x = x_max·sin(ωt),   v = x' = x_max·ω·cos(ωt),   a = x'' = −x_max·ω²·sin(ωt)`

Daraus lesen wir zwei Dinge ab:

- **Höchstwerte:** <span class="m">v_max = ω·x_max</span> und <span class="m">a_max = ω²·x_max</span>.
  Bei <span class="m">x_max = 4,0 cm</span> und <span class="m">T = 0,80 s</span> sind das
  <span class="m">v_max = 0,314 m/s</span> und <span class="m">a_max = 2,47 m/s²</span>.
- **Proportionalität:** <span class="m">a = −ω²·x</span>. Die Beschleunigung ist der Auslenkung
  entgegengesetzt gleichgerichtet proportional. Das ist die Signatur der harmonischen Schwingung.

**Fehlvorstellung 1 — die zentrale Fehlvorstellung des Erklärteils**
(`<div class="hinweis">`, fett beginnend mit *Häufiger Fehler.*):

> **Häufiger Fehler.** „Wo die Auslenkung am größten ist, ist auch die Geschwindigkeit am größten —
> da ist am meisten Bewegung im Spiel." Falsch, und zwar genau umgekehrt. Sieh dir die drei
> Formeln oben an: <span class="m">x</span> ist am größten, wo der Sinus 1 ist, dort ist der
> Kosinus 0, also <span class="m">v = 0</span>. Physikalisch: Im Umkehrpunkt ist die Rückstellkraft
> am größten, sie hat die Bewegung gerade zum Stillstand gebracht und dreht sie um. Durch die
> Ruhelage läuft der Körper dagegen mit größter Geschwindigkeit, obwohl dort die Kraft null ist.
> Kraft und Geschwindigkeit sind bei der Schwingung um eine Viertelperiode gegeneinander
> verschoben. Wer das verinnerlicht hat, versteht später auch die Phasenlage bei der Resonanz.

**Tabelle** (Pflicht: `<div class="tabelle">`):

| Stelle der Bahn | Auslenkung <span class="m">x</span> | Geschwindigkeit <span class="m">v</span> | Beschleunigung <span class="m">a</span> |
|---|---|---|---|
| Umkehrpunkt | <span class="m">±x_max</span> | 0 | <span class="m">∓ω²·x_max</span> (Betrag maximal) |
| Ruhelage | 0 | <span class="m">±ω·x_max</span> (Betrag maximal) | 0 |

### 2.2 Das Federpendel

**Fließtext:**

> Eine Feder, die dem Hookeschen Gesetz folgt, liefert genau die Rückstellkraft, die man braucht:
>
> - `data-tex` (Blockformel): `F = -D\,x`
> - `data-plain`: `F = −D·x`
>
> Die Federkonstante <span class="m">D</span> (Einheit N/m) sagt, wie viel Kraft pro Meter
> Auslenkung nötig ist. Das Minuszeichen ist keine Formalität: Es besagt, dass die Kraft der
> Auslenkung **entgegengerichtet** ist. Sie zeigt immer zur Ruhelage.
>
> Setzt man das ins zweite Newtonsche Gesetz ein, ergibt sich die **Bewegungsgleichung** des
> Federpendels. Wir betrachten eine horizontale, reibungsfreie Anordnung, damit die Gewichtskraft
> keine Rolle spielt (bei senkrechtem Aufhängen verschiebt sie nur die Ruhelage):
>
> - `data-tex` (Blockformel): `m\,\ddot{x} = -D\,x \quad\Longleftrightarrow\quad \ddot{x} + \dfrac{D}{m}\,x = 0`
> - `data-plain`: `m·x'' = −D·x   ⟺   x'' + (D/m)·x = 0`
>
> Das ist eine Gleichung, in der die Funktion <span class="m">x(t)</span> selbst und ihre zweite
> Ableitung vorkommen. Aus 2.1 kennen wir eine Funktion, deren zweite Ableitung ein negatives
> Vielfaches von ihr selbst ist: den Sinus. Ob das die Gleichung löst und welche Kreisfrequenz
> herauskommt, zeigt die Herleitung im nächsten Block.

**Details-Block 1** — Zusammenfassung *Herleitung: Warum das Federpendel harmonisch schwingt und
wie groß T ist* (**erste vollständige Herleitung**):

> **Schritt 1 — Ansatz.** Wir probieren
> <span class="m">x(t) = x_max·sin(ω₀t + φ₀)</span> mit noch unbekanntem
> <span class="m">ω₀</span> und prüfen, ob die Bewegungsgleichung erfüllt werden kann.
>
> **Schritt 2 — Ableiten.**
> - `data-tex`: `\dot{x} = x_{\max}\,\omega_0\cos(\omega_0 t+\varphi_0), \qquad \ddot{x} = -x_{\max}\,\omega_0^2\sin(\omega_0 t+\varphi_0) = -\omega_0^2\,x`
> - `data-plain`: `x' = x_max·ω₀·cos(ω₀t + φ₀),   x'' = −x_max·ω₀²·sin(ω₀t + φ₀) = −ω₀²·x`
>
> **Schritt 3 — Einsetzen.** In <span class="m">x'' + (D/m)·x = 0</span> eingesetzt:
> - `data-tex`: `-\omega_0^2\,x + \dfrac{D}{m}\,x = \left(\dfrac{D}{m}-\omega_0^2\right)x = 0`
> - `data-plain`: `−ω₀²·x + (D/m)·x = (D/m − ω₀²)·x = 0`
>
> Das gilt für **jedes** <span class="m">x(t)</span>, wenn der Klammerausdruck null ist:
>
> - `data-tex`: `\omega_0 = \sqrt{\dfrac{D}{m}}`
> - `data-plain`: `ω₀ = √(D/m)`
>
> Der Ansatz löst die Gleichung also genau für diese Kreisfrequenz. Amplitude
> <span class="m">x_max</span> und Phase <span class="m">φ₀</span> sind frei — sie legen die
> **Anfangsbedingungen** fest (wie weit ausgelenkt, mit welchem Anstoß).
>
> **Schritt 4 — Periode.** Aus <span class="m">ω₀ = 2π/T₀</span> folgt
> - `data-tex`: `T_0 = 2\pi\sqrt{\dfrac{m}{D}}`
> - `data-plain`: `T₀ = 2π·√(m/D)`
>
> **Schritt 5 — Einheitenprobe.** <span class="m">[m/D] = kg / (N/m) = kg·m/(kg·m/s²) = s²</span>,
> die Wurzel liefert Sekunden. ✓
>
> **Was daran auffällt.** Die Amplitude kommt in der Formel für <span class="m">T₀</span> nicht
> vor. Ein Federpendel, das doppelt so weit ausgelenkt wird, braucht für einen Umlauf **genauso
> lange** — es läuft schneller, weil die Rückstellkraft größer ist, und legt einen längeren Weg
> zurück, beides gleicht sich exakt aus. Das gilt nur, weil <span class="m">F ~ x</span> ist.

**Zahlenbeispiel direkt hinter dem Details-Block** (Kontrolle: Abschnitt 7):

> Ein Federpendel mit <span class="m">m = 0,200 kg</span> und <span class="m">D = 8,0 N/m</span>:
> <span class="m">ω₀ = √(8,0 / 0,200) s⁻¹ = √40 s⁻¹ = 6,325 rad/s</span>,
> <span class="m">T₀ = 2π / 6,325 s = 0,9935 s</span> und
> <span class="m">f₀ = 1,007 Hz</span>. Eine numerische Probe bestätigt die Amplitudenunabhängigkeit:
> Bei Anfangsauslenkungen von 2 cm und von 10 cm ergibt sich in beiden Fällen
> <span class="m">T₀ = 0,9935 s</span>.

**Merksatz 1** (Titel *Isochronismus*):

> Beim Federpendel hängt die Schwingungsdauer von der Masse und der Federkonstante ab, **nicht von
> der Amplitude**. Größere Masse macht das Pendel langsamer, härtere Feder macht es schneller.
> Diese Eigenschaft ist keine Naturregel, sondern eine Folge der **linearen** Rückstellkraft
> <span class="m">F ~ x</span>. Sobald die Kraft nichtlinear wird, verliert sie ihre Gültigkeit.

### 2.3 Das Fadenpendel

**Fließtext:**

> Beim Fadenpendel kommt die Rückstellkraft nicht aus einer Feder, sondern aus der Gewichtskraft.
> Ein Pendelkörper der Masse <span class="m">m</span> hängt an einem Faden der Länge
> <span class="m">l</span> und ist um den Winkel <span class="m">θ</span> ausgelenkt. Nur die
> Gewichtskraftkomponente **tangential zur Kreisbahn** treibt die Bewegung an:
> <span class="m">F_t = −m·g·sin θ</span>. Die Komponente längs des Fadens wird vom Faden
> aufgenommen und ändert die Bewegung längs der Bahn nicht.
>
> Für kleine Winkel gilt <span class="m">sin θ ≈ θ</span> (im Bogenmaß). Die Auslenkung längs der
> Bahn ist <span class="m">x = l·θ</span>. Damit wird die Kraft zu
>
> - `data-tex` (Blockformel): `F_t \approx -m g\,\theta = -\dfrac{m g}{l}\,x`
> - `data-plain`: `F_t ≈ −m·g·θ = −(m·g/l)·x`
>
> Das ist ein Kraftgesetz <span class="m">F = −D_eff·x</span> mit
> <span class="m">D_eff = m·g/l</span> — dieselbe Form wie beim Federpendel. Das Ergebnis:
>
> - `data-tex` (Blockformel): `\omega_0 = \sqrt{\dfrac{g}{l}} \qquad T_0 = 2\pi\sqrt{\dfrac{l}{g}}`
> - `data-plain`: `ω₀ = √(g/l)     T₀ = 2π·√(l/g)`

**Details-Block 2** — Zusammenfassung *Herleitung: Fadenpendel, Kleinwinkelnäherung und warum die
Masse fehlt*:

> **Schritt 1 — Kraft längs der Bahn.** Die Gewichtskraft <span class="m">m·g</span> zeigt nach
> unten. Zerlegt man sie am Pendelkörper in eine Komponente längs des Fadens (Betrag
> <span class="m">m·g·cos θ</span>) und eine tangential dazu (<span class="m">m·g·sin θ</span>),
> so ist nur die zweite für die Bewegung längs der Bahn relevant. Sie zeigt zur Ruhelage:
> <span class="m">F_t = −m·g·sin θ</span>.
>
> **Schritt 2 — Bewegungsgleichung.** Mit <span class="m">x = l·θ</span> und
> <span class="m">a_t = ẍ = l·θ̈</span> lautet Newton II längs der Bahn:
> - `data-tex`: `m\,l\,\ddot{\theta} = -m g \sin\theta \quad\Longrightarrow\quad \ddot{\theta} + \dfrac{g}{l}\sin\theta = 0`
> - `data-plain`: `m·l·θ'' = −m·g·sin θ   ⟹   θ'' + (g/l)·sin θ = 0`
>
> **Die Masse kürzt sich heraus.** Kraft (Gewicht) und Trägheit sind beide proportional zu
> <span class="m">m</span>. Darum steht in der Bewegungsgleichung keine Masse. Das ist kein Zufall:
> Es ist die Aussage, dass **schwere und träge Masse gleich sind** (Galilei verglich Pendel mit Blei- und mit
> Korkkugel und fand keinen Unterschied in der Schwingungsdauer; Newton wiederholte den Versuch
> genauer. Beleg: siehe Quellenhinweis am Ende von Abschnitt 6). Beim Federpendel dagegen kommt die Kraft nicht aus
> der Masse, deshalb steht dort <span class="m">m</span> im Ergebnis.
>
> **Schritt 3 — Kleinwinkelnäherung.** Für <span class="m">sin θ ≈ θ</span> (θ im Bogenmaß) wird
> die Gleichung linear: <span class="m">θ'' + (g/l)·θ = 0</span>. Sie hat dieselbe Form wie beim
> Federpendel mit <span class="m">D/m</span> ersetzt durch <span class="m">g/l</span>, also
> <span class="m">ω₀ = √(g/l)</span>.
>
> **Schritt 4 — Wie gut ist die Näherung?** Der relative Fehler von <span class="m">θ</span>
> gegenüber <span class="m">sin θ</span> beträgt bei 5° etwa 0,13 %, bei 10° etwa 0,51 %, bei 15°
> etwa 1,15 % und bei 20° etwa 2,06 %. Die tatsächliche Schwingungsdauer wächst mit der Amplitude
> (exakte Rechnung mit elliptischem Integral, Faktor gegenüber <span class="m">T₀</span>): bei
> 10° etwa 1,0019, bei 30° etwa 1,0174, bei 60° etwa 1,0732. Das Fadenpendel ist also
> **nur näherungsweise** isochron; die Näherung ist bis etwa 10° besser als ein halbes Prozent.

**Zahlenbeispiel:**

> Für <span class="m">l = 1,00 m</span> und <span class="m">g = 9,81 m/s²</span> ist
> <span class="m">T₀ = 2π·√(1,00 / 9,81) s = 2,006 s</span>. Für genau <span class="m">T₀ = 2,000 s</span>
> — ein Pendel, das im Sekundentakt tickt, also je Halbperiode eine Sekunde braucht —
> braucht man <span class="m">l = g·(T/2π)² = 0,994 m</span>.

**Merksatz 2** (Titel *Was die Schwingungsdauer bestimmt*):

> Die Schwingungsdauer eines Fadenpendels hängt nur von der Länge und vom Ortsfaktor ab, **nicht
> von der Masse** und (in der Näherung kleiner Winkel) nicht von der Amplitude. Wer
> <span class="m">T</span> halbieren will, muss die Länge **vierteln**, nicht halbieren. Das
> Federpendel dagegen ist von der Masse abhängig: <span class="m">T ~ √m</span>.

**Fehlvorstellung 2** (`<div class="hinweis">`):

> **Häufiger Fehler.** „Ein schwerer Pendelkörper schwingt langsamer, weil er träger ist." Beim
> Fadenpendel stimmt das nicht: Die größere Masse ist zwar träger, wird aber im gleichen Maß
> stärker von der Erde angezogen. Beide Effekte heben sich auf. Beim Federpendel gilt dagegen
> die Erwartung — dort hängt die Federkraft nicht von der Masse ab, die Trägheit schon. Wer
> beides in einen Topf wirft, hat die Formeln <span class="m">T = 2π√(l/g)</span> und
> <span class="m">T = 2π√(m/D)</span> nicht verstanden, sondern nur gemerkt.

### 2.4 Energie der ungedämpften Schwingung

**Fließtext:**

> Ohne Reibung bleibt die mechanische Energie erhalten. Beim Federpendel setzt sie sich aus der
> Spannenergie der Feder und der Bewegungsenergie des Körpers zusammen:
>
> - `data-tex` (Blockformel): `E = \tfrac{1}{2}\,D\,x^2 + \tfrac{1}{2}\,m\,v^2 = \tfrac{1}{2}\,D\,x_{\max}^2 = \tfrac{1}{2}\,m\,v_{\max}^2`
> - `data-plain`: `E = ½·D·x² + ½·m·v² = ½·D·x_max² = ½·m·v_max²`
>
> Im Umkehrpunkt ist <span class="m">v = 0</span>, also steckt dort alles in der Feder; in der
> Ruhelage ist <span class="m">x = 0</span>, also steckt alles in der Bewegung. Aus den beiden
> Endausdrücken folgt ohne jede Ableitung
>
> - `data-tex`: `v_{\max} = x_{\max}\sqrt{\dfrac{D}{m}} = \omega_0\,x_{\max}`
> - `data-plain`: `v_max = x_max·√(D/m) = ω₀·x_max`
>
> — dasselbe Ergebnis wie in 2.1. Beide Wege stützen sich gegenseitig: Aus der Kinematik
> folgt die Energie, aus der Energie die Kinematik.

**Zahlenbeispiel** (Pendel mit <span class="m">m = 0,200 kg</span>, <span class="m">D = 8,0 N/m</span>,
<span class="m">x_max = 6,0 cm</span>):

> <span class="m">E = ½ · 8,0 N/m · (0,060 m)² = 0,0144 J = 14,4 mJ</span> und
> <span class="m">v_max = 6,325 s⁻¹ · 0,060 m = 0,379 m/s</span>. Bei halber Amplitude
> (<span class="m">x = 3,0 cm</span>) steckt in der Feder nur ein **Viertel** der Energie
> (<span class="m">x² ~ E_pot</span>), also 3,6 mJ; drei Viertel sind Bewegungsenergie und die
> Geschwindigkeit ist <span class="m">v = 0,866·v_max = 0,329 m/s</span> — nicht die halbe
> Höchstgeschwindigkeit.

**Merksatz 3** (Titel *Energie pendelt, Summe bleibt*):

> Bei einer ungedämpften Schwingung pendelt die Energie zweimal je Periode zwischen Spannenergie
> und Bewegungsenergie hin und her, die Summe bleibt konstant. Sie ist proportional zum **Quadrat der
> Amplitude**: Doppelte Amplitude heißt vierfache Energie. Genau diese Aussage brauchst du gleich,
> um zu verstehen, was Reibung mit der Amplitude macht.

---

## 3 · Vertiefung — Dämpfung, erzwungene Schwingung und Resonanz

`<section id="vertiefung">`, `.stufe`-Nummer **3**,
Überschrift **Dämpfung, Antrieb und Resonanz**.

### 3.1 Die gedämpfte Schwingung

**Fließtext:**

> Jede reale Schwingung verliert Energie: Luft bremst, in der Feder entsteht Wärme, das Lager
> reibt. Das einfachste Modell dafür ist eine Reibungskraft, die **proportional zur Geschwindigkeit**
> ist und ihr entgegenwirkt:
>
> - `data-tex` (Blockformel): `F_R = -b\,v \qquad [b] = 1\,\dfrac{\mathrm{N\,s}}{\mathrm{m}} = 1\,\dfrac{\mathrm{kg}}{\mathrm{s}}`
> - `data-plain`: `F_R = −b·v     [b] = 1 N·s/m = 1 kg/s`
>
> Das trifft gut zu, wenn sich ein Körper langsam durch eine Flüssigkeit oder durch Luft bewegt,
> und auch für die Wirbelstrombremse aus dem Induktionsmodul. **Gleitreibung** folgt einem anderen
> Gesetz (konstanter Betrag) und ist hier nicht gemeint. Mit der Rückstellkraft zusammen lautet
> Newton II
>
> - `data-tex` (Blockformel): `m\,\ddot{x} = -D\,x - b\,\dot{x} \quad\Longleftrightarrow\quad \ddot{x} + 2\delta\,\dot{x} + \omega_0^2\,x = 0, \qquad \delta = \dfrac{b}{2m}`
> - `data-plain`: `m·x'' = −D·x − b·x'   ⟺   x'' + 2δ·x' + ω₀²·x = 0,   δ = b/(2m)`
>
> Die Abklingkonstante <span class="m">δ</span> (Einheit 1/s) hat die Rolle, die die Zeitkonstante
> bei einem exponentiellen Abfall hat. Die Gleichung hat, je nachdem, wie groß
> <span class="m">δ</span> gegenüber <span class="m">ω₀</span> ist, drei verschiedene Sorten von Lösungen.
> Die Herleitung im nächsten Block liefert sie alle.

**Details-Block 3** — Zusammenfassung *Herleitung: Die drei Dämpfungsfälle* (**zweite vollständige
Herleitung**):

> **Schritt 1 — Exponentialfaktor abspalten.** Die Reibung lässt die Auslenkung abklingen. Wir
> spalten das ab: <span class="m">x(t) = e^(−δt)·u(t)</span> mit einer noch unbekannten Funktion
> <span class="m">u(t)</span>. Die Produktregel liefert
> - `data-tex`: `\dot{x} = e^{-\delta t}\,(\dot{u} - \delta u), \qquad \ddot{x} = e^{-\delta t}\,(\ddot{u} - 2\delta\dot{u} + \delta^2 u)`
> - `data-plain`: `x' = e^(−δt)·(u' − δ·u),   x'' = e^(−δt)·(u'' − 2δ·u' + δ²·u)`
>
> **Schritt 2 — Einsetzen.** In <span class="m">x'' + 2δ·x' + ω₀²·x = 0</span> eingesetzt und
> durch <span class="m">e^(−δt)</span> geteilt (das ist nie null):
> - `data-tex`: `\ddot{u} - 2\delta\dot{u} + \delta^2 u + 2\delta\dot{u} - 2\delta^2 u + \omega_0^2 u = \ddot{u} + (\omega_0^2 - \delta^2)\,u = 0`
> - `data-plain`: `u'' − 2δ·u' + δ²·u + 2δ·u' − 2δ²·u + ω₀²·u = u'' + (ω₀² − δ²)·u = 0`
>
> Die Terme mit <span class="m">u'</span> heben sich auf. Übrig bleibt eine Gleichung, die wir
> schon kennen — mit einer geänderten Kreisfrequenz.
>
> **Schritt 3 — Drei Fälle.**
> 1. **Schwingfall,** <span class="m">δ < ω₀</span>: <span class="m">ω_d² = ω₀² − δ² > 0</span>.
>    Dann ist <span class="m">u = x_max·cos(ω_d·t + φ₀)</span> (Abschnitt 2.2, Herleitung mit
>    <span class="m">ω_d</span> statt <span class="m">ω₀</span>), also
>    - `data-tex`: `x(t) = x_{\max}\,e^{-\delta t}\cos(\omega_d t + \varphi_0), \qquad \omega_d = \sqrt{\omega_0^2 - \delta^2}`
>    - `data-plain`: `x(t) = x_max·e^(−δt)·cos(ω_d·t + φ₀),   ω_d = √(ω₀² − δ²)`
> 2. **Aperiodischer Grenzfall,** <span class="m">δ = ω₀</span>: Es bleibt
>    <span class="m">u'' = 0</span>, also <span class="m">u = c₁ + c₂·t</span> und
>    <span class="m">x = (c₁ + c₂·t)·e^(−δt)</span>. Keine Schwingung, höchstens ein einziger
>    Nulldurchgang, danach Rückkehr zur Ruhelage.
> 3. **Kriechfall,** <span class="m">δ > ω₀</span>: <span class="m">u'' = κ²·u</span> mit
>    <span class="m">κ = √(δ² − ω₀²)</span>, also Exponentialfunktionen
>    <span class="m">u = A·e^(κt) + B·e^(−κt)</span>. Wegen <span class="m">κ < δ</span> klingen
>    beide Anteile ab; der langsamere mit <span class="m">e^(−(δ−κ)t)</span> bestimmt das späte
>    Verhalten.
>
> **Schritt 4 — Was das heißt.** Im Schwingfall ist der Faktor
> <span class="m">e^(−δt)</span> die **Hüllkurve**: Die Maxima liegen auf
> <span class="m">±x_max·e^(−δt)</span>. Aufeinanderfolgende Maxima im Abstand
> <span class="m">T_d</span> haben ein **festes Verhältnis**:
> - `data-tex`: `\dfrac{x_n}{x_{n+1}} = e^{\delta T_d} =: e^{\Lambda}, \qquad \Lambda = \delta\,T_d = \ln\dfrac{x_n}{x_{n+1}}`
> - `data-plain`: `x_n / x_(n+1) = e^(δ·T_d) =: e^Λ,   Λ = δ·T_d = ln(x_n / x_(n+1))`
>
> Λ heißt **logarithmisches Dekrement**. Es lässt sich direkt aus einem Diagramm bestimmen:
> zwei benachbarte Maxima ablesen, Verhältnis bilden, Logarithmus nehmen.
>
> **Schritt 5 — Energie.** Die Energie ist proportional zum Amplitudenquadrat, also
> <span class="m">E(t) ~ e^(−2δt)</span>. Je Periode bleibt der Bruchteil <span class="m">e^(−2Λ)</span>.
>
> **Nachprobe.** Setzt man <span class="m">x = e^(−δt)·cos(ω_d·t)</span> in die Gleichung ein
> (mit einem Computeralgebrasystem ausgeführt), bleibt für beliebige <span class="m">m, D, b</span>
> der Rest null. Das Ergebnis ist also keine Näherung, sondern exakt.

**Zahlenbeispiel — dasselbe Federpendel wie in 2.2** (<span class="m">m = 0,200 kg</span>,
<span class="m">D = 8,0 N/m</span>, <span class="m">ω₀ = 6,325 rad/s</span>), aber mit
<span class="m">b = 0,20 kg/s</span>:

> <span class="m">δ = b/(2m) = 0,20 / 0,400 s⁻¹ = 0,50 s⁻¹</span>, klein gegen
> <span class="m">ω₀</span>, also Schwingfall. <span class="m">ω_d = √(6,325² − 0,50²) s⁻¹ = 6,305 rad/s</span>,
> <span class="m">T_d = 2π / 6,305 s = 0,9966 s</span> gegenüber
> <span class="m">T₀ = 0,9935 s</span> — die Periode wird um 0,31 % länger. Das logarithmische
> Dekrement ist <span class="m">Λ = 0,50 · 0,9966 = 0,4983</span>; die nächste Amplitude beträgt
> <span class="m">e^(−0,4983) = 60,8 %</span> der vorigen, die Energie nach einer Periode
> <span class="m">36,9 %</span> der vorigen. Nach etwa <span class="m">5/δ = 10 s</span> ist die
> Amplitude auf <span class="m">e^(−5) = 0,67 %</span> gefallen.

**Tabelle der drei Fälle** (Pflicht: `<div class="tabelle">`; Beispielsystem
<span class="m">m = 0,200 kg</span>, <span class="m">D = 8,0 N/m</span>):

| Fall | Bedingung | Reibungskoeffizient im Beispiel | Verhalten |
|---|---|---|---|
| Schwingfall | <span class="m">δ < ω₀</span> | z. B. <span class="m">b = 0,20 kg/s</span> (δ = 0,50 s⁻¹) | schwingt mit abklingender Amplitude |
| aperiodischer Grenzfall | <span class="m">δ = ω₀</span>, d. h. <span class="m">b = 2·√(m·D)</span> | <span class="m">b = 2,530 kg/s</span> (δ = 6,325 s⁻¹) | kein Überschwingen, schnellste Rückkehr |
| Kriechfall | <span class="m">δ > ω₀</span> | z. B. <span class="m">b = 4,0 kg/s</span> (δ = 10 s⁻¹) | kein Überschwingen, langsame Rückkehr |

Zum Grenzfall: <span class="m">b_krit = 2·m·ω₀ = 2·√(m·D) = 2·√(0,200·8,0) kg/s = 2,530 kg/s</span>.
Der Kriechfall ist **langsamer** als der Grenzfall, obwohl die Reibung größer ist: Die große Reibung
bremst auch die Rückkehr. Deshalb sind Türschließer und Stoßdämpfer häufig nahe am Grenzfall
ausgelegt (allgemeiner technischer Sachverhalt, hier nicht einzeln belegt; wenn der Bauagent
Zweifel hat, den Satz weglassen).

**Fehlvorstellung 3** (`<div class="hinweis">`):

> **Häufiger Fehler.** Zwei Denkfehler stehen bei der Dämpfung oft zusammen. Erstens: „Reibung
> ändert nur die Amplitude, die Schwingungsdauer bleibt." Nicht ganz — <span class="m">ω_d < ω₀</span>,
> also ist <span class="m">T_d > T₀</span>. Bei schwacher Dämpfung ist der Unterschied winzig (hier
> 0,31 %), bei starker Dämpfung nicht mehr. Zweitens: „Die Amplitude nimmt mit jeder Schwingung um
> denselben **Betrag** ab." Nein — um denselben **Faktor**. Die Kurve ist exponentiell, nicht linear.
> Mit der Vorstellung vom festen Betrag müsste die Schwingung nach endlich vielen Perioden
> aufhören; tatsächlich wird sie beliebig klein, aber nie null.

**Merksatz 4** (Titel *Dämpfung*):

> Reibung verkleinert die Amplitude bei jeder Schwingung um denselben **Faktor**
> <span class="m">e^(−Λ)</span>; die Energie schrumpft um den Faktor <span class="m">e^(−2Λ)</span>.
> Ob ein System überhaupt noch schwingt, entscheidet allein der Vergleich
> <span class="m">δ</span> gegen <span class="m">ω₀</span>.

### 3.2 Die erzwungene Schwingung

**Fließtext:**

> Schwingt ein System nicht sich selbst überlassen, sondern wird periodisch angetrieben, heißt
> das **erzwungene Schwingung.** Der **Erreger** übt die Kraft
> <span class="m">F(t) = F₀·sin(ω_e·t)</span> aus (Index **e** für Erreger); das schwingende System
> heißt **Resonator.** Die Bewegungsgleichung aus 0.3 gilt nun mit
> <span class="m">F₀ ≠ 0</span>:
>
> - `data-tex` (Blockformel): `\ddot{x} + 2\delta\,\dot{x} + \omega_0^2\,x = \dfrac{F_0}{m}\,\sin(\omega_e t)`
> - `data-plain`: `x'' + 2δ·x' + ω₀²·x = (F₀/m)·sin(ω_e·t)`
>
> Nach dem Start überlagern sich zwei Anteile: die abklingende freie Schwingung des Systems (sie
> ist nach etwa <span class="m">5/δ</span> vergessen) und eine Schwingung, die **bleibt**. Im
> eingeschwungenen Zustand gilt der wichtigste Satz dieses Abschnitts:

**Merksatz 5** (Titel *Eingeschwungener Zustand*):

> Nach dem Einschwingen schwingt das System **mit der Frequenz des Erregers**, nicht mit seiner
> eigenen. Die Eigenfrequenz <span class="m">ω₀</span> bestimmt nur, **wie stark** es dabei
> ausschlägt und **wie weit es dem Erreger hinterherhinkt.**

**Details-Block 4** — Zusammenfassung *Herleitung: Amplitude und Phase der erzwungenen Schwingung*
(**dritte vollständige Herleitung**):

> **Schritt 1 — Ansatz.** Wir suchen die bleibende Lösung in der Form
> <span class="m">x(t) = x_max·sin(ω_e·t − φ)</span> mit unbekannter Amplitude
> <span class="m">x_max</span> und unbekannter Verschiebung <span class="m">φ</span> (positives
> <span class="m">φ</span> heißt: die Antwort **hinkt** dem Erreger hinterher). Zur Abkürzung sei
> <span class="m">θ = ω_e·t − φ</span>. Dann ist
> <span class="m">x = x_max·sin θ</span>, <span class="m">x' = x_max·ω_e·cos θ</span> und
> <span class="m">x'' = −x_max·ω_e²·sin θ</span>.
>
> **Schritt 2 — Einsetzen** in <span class="m">m·x'' + b·x' + D·x = F₀·sin(ω_e·t)</span>, wobei
> <span class="m">ω_e·t = θ + φ</span> ist:
> - `data-tex`: `x_{\max}\Big[(D - m\omega_e^2)\sin\theta + b\omega_e\cos\theta\Big] = F_0\,\big(\sin\theta\cos\varphi + \cos\theta\sin\varphi\big)`
> - `data-plain`: `x_max·[(D − m·ω_e²)·sin θ + b·ω_e·cos θ] = F₀·(sin θ·cos φ + cos θ·sin φ)`
>
> **Schritt 3 — Koeffizientenvergleich.** Die Gleichung muss für **jedes** <span class="m">θ</span>
> gelten, also müssen die Faktoren vor <span class="m">sin θ</span> und vor
> <span class="m">cos θ</span> getrennt übereinstimmen:
> - `data-tex`: `x_{\max}\,(D - m\omega_e^2) = F_0\cos\varphi, \qquad x_{\max}\,b\,\omega_e = F_0\sin\varphi`
> - `data-plain`: `x_max·(D − m·ω_e²) = F₀·cos φ,   x_max·b·ω_e = F₀·sin φ`
>
> **Schritt 4 — Auflösen.** Quadrieren und Addieren (<span class="m">sin² + cos² = 1</span>) gibt die
> Amplitude, Dividieren die Phase:
> - `data-tex`: `x_{\max} = \dfrac{F_0}{\sqrt{(D - m\omega_e^2)^2 + (b\omega_e)^2}}, \qquad \tan\varphi = \dfrac{b\,\omega_e}{D - m\omega_e^2}`
> - `data-plain`: `x_max = F₀ / √((D − m·ω_e²)² + (b·ω_e)²),   tan φ = b·ω_e / (D − m·ω_e²)`
>
> Wegen <span class="m">sin φ ≥ 0</span> liegt <span class="m">φ</span> zwischen 0 und 180°.
> Teilt man durch <span class="m">m</span> und nutzt <span class="m">D/m = ω₀²</span> sowie
> <span class="m">b/m = 2δ</span>:
> - `data-tex`: `x_{\max}(\omega_e) = \dfrac{F_0/m}{\sqrt{(\omega_0^2 - \omega_e^2)^2 + (2\delta\,\omega_e)^2}}, \qquad \tan\varphi = \dfrac{2\delta\,\omega_e}{\omega_0^2 - \omega_e^2}`
> - `data-plain`: `x_max(ω_e) = (F₀/m) / √((ω₀² − ω_e²)² + (2δ·ω_e)²),   tan φ = 2δ·ω_e / (ω₀² − ω_e²)`
>
> **Nachprobe.** Der Ansatz erfüllt die Bewegungsgleichung bei 200 zufälligen Kombinationen von
> <span class="m">m, D, b, F₀, ω_e, t</span> mit einem Rest unter <span class="m">10⁻⁹</span>. Eine
> numerische Integration der Bewegungsgleichung liefert nach dem Einschwingen dieselben Amplituden
> (Abweichung unter 0,2 mm, das ist die Prüftoleranz).

**Die drei Bereiche der Resonanzkurve** (Tabelle, Pflicht: `<div class="tabelle">`):

| Erregung | Näherung | Antwort | Phase <span class="m">φ</span> |
|---|---|---|---|
| tief, <span class="m">ω_e ≪ ω₀</span> | <span class="m">x_max ≈ F₀/D</span> | Feder gibt nach, als würde man **langsam** drücken (quasistatisch) | ≈ 0° (in Phase) |
| Resonanz, <span class="m">ω_e ≈ ω₀</span> | <span class="m">x_max ≈ F₀ / (b·ω₀)</span> | nur die Reibung begrenzt, Höchstwert | ≈ 90° |
| hoch, <span class="m">ω_e ≫ ω₀</span> | <span class="m">x_max ≈ F₀ / (m·ω_e²)</span> | Trägheit dominiert, Körper kann nicht folgen, Amplitude fällt | ≈ 180° (Gegenphase) |

Im hohen Bereich fällt die Amplitude mit dem Quadrat der Erregerfrequenz. Damit ist geklärt, warum
die Waschmaschine bei voller Drehzahl ruhig läuft. Beim Hochfahren durchläuft die
Erregerfrequenz dagegen den Resonanzbereich: kurzzeitig starkes Rütteln. Praktisch bedeutet das,
den Resonanzbereich möglichst schnell zu durchlaufen und darüber zu bleiben.

**Zahlenbeispiel — dasselbe Pendel** (<span class="m">m = 0,200 kg</span>, <span class="m">D = 8,0 N/m</span>,
<span class="m">b = 0,20 kg/s</span>, <span class="m">δ = 0,50 s⁻¹</span>) mit Erregerkraft
<span class="m">F₀ = 0,50 N</span>:

> - **tief:** <span class="m">x_stat = F₀/D = 0,50 N / 8,0 N/m = 6,25 cm</span>.
> - **Resonanz:** <span class="m">x_max(ω₀) = F₀ / (b·ω₀) = 0,50 / (0,20 · 6,325) m = 39,5 cm</span> —
>   das **6,32-fache** der statischen Auslenkung. Dieses Verhältnis ist
>   <span class="m">ω₀/(2δ)</span> = 6,325 s⁻¹ / 1,0 s⁻¹, die **Überhöhung** bei schwacher Dämpfung.
> - **hoch:** bei <span class="m">ω_e = 2·ω₀</span> nur <span class="m">x_max = 2,07 cm</span> — rund 5 % der
>   Resonanzamplitude.
>
> Zur Einordnung: Bei 40 cm Ausschlag ist eine Feder mit <span class="m">D = 8 N/m</span> längst
> nicht mehr im Hookeschen Bereich. Das Zahlenbeispiel zeigt die Formel, nicht das Verhalten
> eines echten Bauteils.

**Details-Block 5** — Zusammenfassung *Wo liegt das Maximum? Resonanzfrequenz und Spitzenhöhe*:

> Die Amplitude ist maximal, wo der Radikand
> <span class="m">R(ω_e) = (ω₀² − ω_e²)² + 4δ²·ω_e²</span> am kleinsten ist. Ableiten:
> - `data-tex`: `\dfrac{\mathrm{d}R}{\mathrm{d}\omega_e} = -4\omega_e(\omega_0^2-\omega_e^2) + 8\delta^2\omega_e = 4\omega_e\,(\omega_e^2 - \omega_0^2 + 2\delta^2)`
> - `data-plain`: `dR/dω_e = −4·ω_e·(ω₀² − ω_e²) + 8·δ²·ω_e = 4·ω_e·(ω_e² − ω₀² + 2δ²)`
>
> Nullsetzen (mit <span class="m">ω_e ≠ 0</span>) liefert
> - `data-tex`: `\omega_{\text{res}} = \sqrt{\omega_0^2 - 2\delta^2}`
> - `data-plain`: `ω_res = √(ω₀² − 2δ²)`
>
> Das Maximum liegt also **unterhalb** von <span class="m">ω₀</span>, und es existiert nur für
> <span class="m">δ < ω₀/√2</span>. Bei stärkerer Dämpfung fällt die Kurve von
> <span class="m">F₀/D</span> aus monoton ab. Setzt man <span class="m">ω_res</span> ein, wird
> <span class="m">R = 4δ²·(ω₀² − δ²)</span> und die Spitzenhöhe
> - `data-tex`: `x_{\max,\text{res}} = \dfrac{F_0/m}{2\delta\sqrt{\omega_0^2 - \delta^2}}`
> - `data-plain`: `x_max,res = (F₀/m) / (2δ·√(ω₀² − δ²))`
>
> Im Beispielsystem: <span class="m">ω_res = √(40 − 0,50) s⁻¹ = 6,285 rad/s</span> (also
> <span class="m">f_res = 1,0003 Hz</span> gegenüber <span class="m">f₀ = 1,0066 Hz</span>) und
> <span class="m">x_max,res = 39,65 cm</span> — nur 0,3 % über dem Wert bei
> <span class="m">ω₀</span>. Bei schwacher Dämpfung darf man <span class="m">ω_res ≈ ω₀</span>
> setzen. Die Spitzenhöhe ist umgekehrt proportional zu <span class="m">δ</span>: **halbe Reibung,
> doppelte Spitze.** Für <span class="m">δ → 0</span> wächst sie über alle Grenzen — das ist die
> Resonanzkatastrophe der idealen, ungedämpften Rechnung. In Wirklichkeit begrenzen
> Dämpfung und das Versagen des linearen Kraftgesetzes den Ausschlag.

**Details-Block 6** — Zusammenfassung *Warum die Schaukel im richtigen Rhythmus hochgeht*
(Energiebilanz, kurz):

> Bei <span class="m">ω_e = ω₀</span> ist <span class="m">φ = 90°</span>. Dann ist
> <span class="m">x = −x_max·cos(ω_e·t)</span>, also <span class="m">v = x_max·ω_e·sin(ω_e·t)</span>:
> Kraft und Geschwindigkeit sind **in Phase**. Der Erreger drückt in jedem Augenblick in die Richtung,
> in die sich das System gerade bewegt, die Leistung <span class="m">P = F·v</span> ist nie
> negativ und die Energieaufnahme maximal. Bei der Schaukel heißt das: Du schiebst, wenn das
> Kind sich von dir weg bewegt, nicht dann, wenn es zurückkommt. Im eingeschwungenen Zustand nimmt die
> Reibung genauso viel Leistung auf, wie der Erreger liefert. Im Beispielsystem: mittlere Leistung
> <span class="m">P = F₀²/(2b) = 0,25 / 0,40 W = 0,625 W</span>, und
> <span class="m">½·b·v_max² = ½ · 0,20 · (2,5 m/s)² = 0,625 W</span> — beide Seiten stimmen überein.

**Fehlvorstellung 4** (`<div class="hinweis">`, zusammenfassend für die Resonanz):

> **Häufiger Fehler.** „Resonanz heißt: Erreger und System schwingen gleich schnell und schaukeln
> sich zu Tode." Drei Dinge sind dabei zu berichtigen. Erstens: Im eingeschwungenen Zustand
> schwingt das System **immer** mit der Erregerfrequenz — auch unterhalb und oberhalb der
> Resonanz. Was sich mit <span class="m">ω_e</span> ändert, ist die **Amplitude** und die **Phase**.
> Zweitens: Das Maximum liegt bei starker Dämpfung merklich **unterhalb** von <span class="m">ω₀</span>,
> nicht exakt darauf. Drittens: Die Amplitude wächst nicht unbegrenzt, sie wird durch die
> Dämpfung begrenzt (<span class="m">x_max ~ 1/δ</span>). Gefährlich wird Resonanz erst, wenn der
> Ausschlag über das hinausgeht, was ein Bauteil aushält. Mit ausreichend Dämpfung oder
> ausreichend Abstand zur Eigenfrequenz ist sie harmlos oder sogar erwünscht (Musikinstrument,
> Schaukel, Radioempfänger).

**Merksatz 6** (Titel *Resonanz*):

> Resonanz ist der Bereich, in dem ein periodisch angetriebenes System die größte Amplitude
> erreicht: Die Erregerfrequenz liegt nahe der Eigenfrequenz, der Erreger liefert Energie in Phase
> mit der Geschwindigkeit, und nur die Dämpfung begrenzt die Höhe. **Weit oberhalb** der Resonanz
> ist das System träge und schlägt kaum noch aus.

**Ausblick (ein Satz, ohne Rechnung):** Dieselbe Gleichung beschreibt den elektromagnetischen
Schwingkreis (Spule und Kondensator) — nur die Namen der Größen ändern sich.
