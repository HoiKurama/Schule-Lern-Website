# Modulinhalt: Selbstinduktion — Induktivität, Ein- und Ausschaltvorgang, Energie im Magnetfeld

Modul: `physik-q1-selbstinduktion`
Fach: Physik, Leistungskurs Q1
Inhaltsfeld (Chip im Seitenkopf, **wörtlich**): **Ladungen, Felder und Induktion**
Akzentfarben: `--akzent: #1d4ed8`, `--akzent-hell: #eff6ff`, `--akzent-rand: #bfdbfe`
Titel der Seite: *Selbstinduktion*
Untertitel im Kopf: *Warum sich eine Spule gegen jede Stromänderung wehrt — und was das beim Ausschalten bedeutet*
Chips: `Physik LK · Q1` · `Inhaltsfeld: Ladungen, Felder und Induktion` · `ca. 120 Minuten`

**Lesehinweis für den Bauagenten.** Formeln im Fließtext sind hier als Kürzel
`<span class="m">…</span>` geschrieben. Der Bauagent macht daraus `data-tex` und `data-plain`
(Unicode, ohne LaTeX-Rest). Abgesetzte Formeln und alle Formeln, bei denen ein Bruch, ein Index
oder ein Integral vorkommt, sind mit `data-tex` und `data-plain` **wörtlich vorgegeben**. Blöcke,
die mit *„nur Bauagent"* überschrieben sind, gehören **nicht** auf die Seite. Alles Übrige ist
Seiteninhalt.

**Einordnung im Kernlehrplan — offen markiert.** Der Chip nennt das Inhaltsfeld wörtlich nach
`fachliches/kernlehrplan-nrw.md`. **Offen und nicht verifiziert:** ob „Selbstinduktion",
„Induktivität" und „Energie des Magnetfeldes" im Kernlehrplan des Landes wörtlich als
Kompetenzerwartung stehen. Die Zuordnung zu Q1 folgt der Projektfestlegung (Q1 = Inhaltsfelder 1
und 2) und dem Anschlusshinweis im Referenzmodul (*„Anschlussthemen sind Selbstinduktion und der
elektromagnetische Schwingkreis"*). Es steht deshalb **kein** Kernlehrplan-Zitat im Modul; die
Kompetenzsätze im Selbstcheck sind eigene Formulierungen.

**Abgrenzung — verbindlich.**

| Gehört in dieses Modul | Gehört **nicht** hierher |
|---|---|
| Selbstinduktion als Anwendung von <span class="m">U_ind = −N·dΦ/dt</span> auf den eigenen Fluss | Gegeninduktion zweier Spulen, Transformator |
| Induktivität <span class="m">L</span>, Einheit Henry, <span class="m">U_ind = −L·dI/dt</span> | Wechselstromwiderstand der Spule (<span class="m">X_L = ω·L</span>), Impedanz |
| <span class="m">L</span> der langen Spule, <span class="m">L = µ₀·µ_r·N²·A/l</span> | Ferromagnetismus quantitativ, Hysterese, Sättigungskurve (nur als Modellgrenze genannt) |
| Ein- und Ausschaltvorgang im RL-Kreis, <span class="m">τ = L/R</span>, Abklingen und Anwachsen | Elektromagnetischer Schwingkreis (Folgemodul `physik-q1-schwingkreis`) |
| Spannungsspitze beim Ausschalten, Funke, Schutzbeschaltung (qualitativ) | Bauteilauslegung von Freilaufdioden, Snubber-Netzwerke |
| Energie im Magnetfeld <span class="m">W = ½·L·I²</span>, Energiedichte <span class="m">w = B²/(2·µ₀·µ_r)</span> | Poynting-Vektor, Feldenergie im Wechselfeld |

**Stellung im Curriculum.** Das Modul baut **unmittelbar** auf `module/physik-q1-induktion.html`
auf: Es setzt das Induktionsgesetz <span class="m">U_ind = −N·dΦ/dt</span>, den magnetischen Fluss
<span class="m">Φ = B·A</span> und die Lenzsche Regel als bekannt voraus. Notation und Vorzeichenkonvention
werden **unverändert** übernommen; das Minuszeichen steht in jeder Formel, wo es hingehört. Wo
das Modul auf den Schwingkreis zeigt, geschieht das als **Ausblick in einem Satz** ohne Rechnung.

**Quellen für empirische und historische Angaben** (per Websuche geprüft, Stand 09/2026):

- Selbstinduktion beim Ausschalten mit Glimmlampe, Aufbau (Spule mit 1000 Windungen und
  geschlossenem Eisenkern), **Zündspannung der Glimmlampe 80 bis 100 V**:
  Landesbildungsserver Baden-Württemberg,
  https://www.schule-bw.de/faecher-und-schularten/mathematisch-naturwissenschaftliche-faecher/physik/unterrichtsmaterialien/e_lehre_2/selbstinduktion/selbstind_aus.htm
- Dieselbe Versuchsanordnung mit Quelle von wenigen Volt (Suchzusammenfassung zu LEIFIphysik und
  Didaktik der Physik LMU München; die LEIFI-Seite selbst war per Abruf nicht erreichbar,
  HTTP 403). Der Seitentext sagt deshalb nur „wenige Volt", nicht „4 V".
- Joseph Henry entdeckte die Selbstinduktion 1832 unabhängig von Michael Faraday; die Einheit
  Henry ist nach ihm benannt (Britannica, Encyclopedia.com, Smithsonian Institution Archives über
  die Suchergebnisse bestätigt). Die Jahreszahl 1832 steht so im Seitentext.
- <span class="m">µ₀</span> ist seit der SI-Revision 2019 nicht mehr exakt
  <span class="m">4π·10⁻⁷</span>; CODATA 2018: <span class="m">µ₀ = 1,256 637 062 12·10⁻⁶ N/A²</span>,
  Verhältnis zu <span class="m">4π·10⁻⁷</span> gleich 1,000 000 000 55 (NIST, physics.nist.gov/cuu).
- **Ungeprüft und als Richtwert gekennzeichnet:** Größenordnung der Permeabilitätszahl weicher
  Eisenkerne (mehrere Hundert bis einige Tausend), Sättigungsflussdichte von Eisen (etwa 2 T),
  Flussspannung einer Siliziumdiode (etwa 0,7 V), Typischkeit von Freilaufdioden an Relaisspulen.
  Diese Angaben stehen im Seitentext ausdrücklich als „Richtwert" beziehungsweise „typisch".

---

## 0 · Konventionen, Konstanten und Formelzeichen

**Diese Festlegungen gelten für jede Abbildung, jede Simulation, jede Aufgabe und jede
Musterlösung des Moduls. Der Bauagent weicht davon nicht ab.**

### 0.1 Konstanten (überall mit genau diesen Werten rechnen)

<div class="tabelle">

| Größe | Zeichen | Wert | Einheit |
|---|---|---|---|
| magnetische Feldkonstante | µ₀ | 4π · 10⁻⁷ ≈ 1,2566 · 10⁻⁶ | V·s/(A·m) = H/m |
| Durchschlagsfeldstärke trockener Luft (aus dem Modul *Elektrisches Feld*) | E_max | ≈ 3 · 10⁶ | V/m = 3 kV/mm |
| Lichtbogen-Ersatzwiderstand (nur Simulation, Modellannahme) | R_Bogen | 5000 | Ω |

</div>

- `data-tex`: `\mu_0 = 4\pi\cdot10^{-7}\,\dfrac{\mathrm{V\,s}}{\mathrm{A\,m}} \approx 1{,}2566\cdot10^{-6}\,\dfrac{\mathrm{V\,s}}{\mathrm{A\,m}}`
- `data-plain`: `µ₀ = 4π · 10⁻⁷ V·s/(A·m) ≈ 1,2566 · 10⁻⁶ V·s/(A·m)`

**Achtung Schreibweise.** In `data-tex` heißt die Feldkonstante `\mu_0`, die Permeabilitätszahl
`\mu_\mathrm{r}`, beides mit dem TeX-Befehl `\mu`, niemals mit dem Unicode-Zeichen im TeX-String. In
`data-plain` steht `µ₀` und `µ_r` mit dem Mikro-Zeichen U+00B5 oder dem griechischen µ U+03BC
(einheitlich wählen). Die Schreibweise von 4π·10⁻⁷ ist eine Rechengröße für die Schule; die
Abweichung von rund 5,5·10⁻¹⁰ (relativ) ist ohne Bedeutung und wird **nicht** im Seitentext
erwähnt, nur hier.

### 0.2 Formelzeichen

<div class="tabelle">

| Zeichen | Bedeutung | Einheit | Anmerkung |
|---|---|---|---|
| <span class="m">L</span> | Induktivität einer Spule | H (Henry) = V·s/A = Wb/A | kursives **L**; Länge der Spule ist **kleines** <span class="m">l</span> |
| <span class="m">U_ind</span> | induzierte Spannung (bei Selbstinduktion: Selbstinduktionsspannung) | V | **einziges** Zeichen, es gibt kein <span class="m">U_L</span> |
| <span class="m">U₀</span> | Quellenspannung (Gleichspannung) | V | |
| <span class="m">I</span> | Stromstärke im Kreis | A, mA | |
| <span class="m">I_∞</span> | Endstrom beim Einschalten, <span class="m">I_∞ = U₀/R</span> | A, mA | |
| <span class="m">I₀</span> | Strom im Moment des Öffnens des Schalters | A, mA | im Beharrungszustand <span class="m">I₀ = I_∞</span> |
| <span class="m">R</span> | Gesamtwiderstand des Einschaltkreises (Spulendraht plus etwaiger Vorwiderstand) | Ω | |
| <span class="m">R_S</span> | Schutzwiderstand (zusätzlich, beim Ausschalten parallel zur Spule) | Ω | nur Simulation und Aufgaben |
| <span class="m">R_F</span> | Gesamtwiderstand des Ausschaltkreises („Freilaufkreis"), <span class="m">R_F = R + R_S</span> | Ω | enthält den Spulendraht **mit** |
| <span class="m">τ</span> | Zeitkonstante, <span class="m">τ_ein = L/R</span>, <span class="m">τ_aus = L/R_F</span> | s, ms | |
| <span class="m">N</span> | Windungszahl | 1 | |
| <span class="m">A</span> | Querschnittsfläche der Spule | m² | |
| <span class="m">l</span> | Länge der Spule | m | **kleines** l |
| <span class="m">µ_r</span> | Permeabilitätszahl des Spulenkerns | 1 | Luft: <span class="m">µ_r = 1</span> |
| <span class="m">B</span> | Flussdichte im Spuleninneren | T | |
| <span class="m">Φ</span> | magnetischer Fluss **durch eine Windung** | Wb | |
| <span class="m">W_mag</span> | im Magnetfeld gespeicherte Energie | J, mJ | |
| <span class="m">w_mag</span> | Energiedichte <span class="m">w_mag = W_mag/V</span> | J/m³ | |

</div>

**Kollisionswarnung an den Bauagenten.** Das Zeichen `L` steht für die **Induktivität** (groß,
kursiv). Die Länge der Spule ist ein kleines, kursives `l`, in Aufgabentexten oft als
<span class="m">l = 25 cm</span>. In `data-tex` ist das kleine l bewusst `l` (nicht `\ell`), damit
es in der Anzeige nicht mit der Ziffer 1 verwechselt wird, wird aber im Fließtext **nie** neben
einer Zahl ohne Leerraum gesetzt (also `l = 0,25 m`, nie `l=0,25m`). Der Buchstabe `I` ist die
Stromstärke, nie die Ziffer 1. Die Einheit Henry wird aufrecht gesetzt: `\mathrm{H}`.

### 0.3 Vorzeichenkonvention — verbindlich, im ganzen Modul gleich

Das Referenzmodul schreibt <span class="m">U_ind = −N·dΦ/dt</span>. Für die Selbstinduktion gilt
mit <span class="m">N·Φ = L·I</span> unverändert

- `data-tex`: `U_{\text{ind}} = -N\,\dfrac{\mathrm{d}\Phi}{\mathrm{d}t} = -L\,\dfrac{\mathrm{d}I}{\mathrm{d}t}`
- `data-plain`: `U_ind = −N · dΦ/dt = −L · dI/dt`

**Der Zählpfeil von <span class="m">U_ind</span> zeigt in Stromrichtung** (so, wie man den Pfeil einer
Quelle im Kreis zeichnet). Damit lautet die Maschenregel im Einschaltkreis

- `data-tex`: `U_0 + U_{\text{ind}} = R \cdot I`
- `data-plain`: `U₀ + U_ind = R · I`

und im Ausschaltkreis (Quelle vom Kreis getrennt, <span class="m">U₀</span> entfällt)

- `data-tex`: `U_{\text{ind}} = R_F \cdot I`
- `data-plain`: `U_ind = R_F · I`

<div class="tabelle">

| Situation | <span class="m">dI/dt</span> | <span class="m">U_ind = −L·dI/dt</span> | Lenz: wirkt … |
|---|---|---|---|
| Einschalten, <span class="m">I</span> wächst | > 0 | **< 0** | der Quelle entgegen, bremst den Anstieg |
| Beharrung, <span class="m">I</span> konstant | = 0 | **= 0** | gar nicht |
| Ausschalten, <span class="m">I</span> fällt | < 0 | **> 0** | in Stromrichtung, hält den Strom aufrecht |

</div>

Diese Vorzeichen gelten für jede Formel, jede Simulationsanzeige, jedes Diagramm und jede
Musterlösung. **Das Minuszeichen wird nirgends stillschweigend weggelassen.** Wird in einer
Aufgabe ausdrücklich nur der **Betrag** verlangt, steht das Wort „Betrag" im Aufgabentext und die
Formel wird mit Betragsstrichen <span class="m">|U_ind|</span> geschrieben.

### 0.4 Farben im Diagramm und im Schaltbild

<div class="tabelle">

| Objekt | Festlegung |
|---|---|
| Kurve <span class="m">I(t)</span> | Akzentblau `#1d4ed8`, 3 px |
| Kurve <span class="m">U_ind(t)</span> | Orange `#b45309`, 3 px |
| Nulllinie, Achsen, Gitter | `#94a3b8`, 1 px, Gitter gestrichelt `#e2e8f0` |
| Endwert <span class="m">I_∞</span>, Hilfslinie <span class="m">±U₀</span> | gestrichelt, `#475569` |
| Anfangstangente an <span class="m">I(t)</span> | gestrichelt, `#1d4ed8`, 1,5 px |
| Energie <span class="m">W_mag</span> (Anzeige, Feldlinien in der Spule) | Grün `#0d7a52` |
| Funke am Schalter | Gelb `#f59e0b` |
| Leitungen ohne Strom / mit Strom | `#94a3b8` / `#1d4ed8`, Strichstärke 2 px bis 5 px proportional zu <span class="m">I</span> |

</div>

### 0.5 Einheiten und Zahlendarstellung

- Dezimaltrennzeichen **Komma**, auch in jeder Simulationsanzeige (`fmt()`).
- Vorsätze so wählen, dass der Zahlenwert zwischen 0,1 und 1000 liegt: **µH, mH, H** für die
  Induktivität, **mA, A** für die Stromstärke, **µs, ms, s** für die Zeit, **V, kV** für die
  Spannung, **µJ, mJ, J** für die Energie.
- Zwischen Zahl und Einheit steht ein schmaler Abstand (U+202F). Die Bruchschreibweise der Einheit
  ist `V·s/A`, nicht `Vs/A`.
- <span class="m">1 H = 1 V·s/A = 1 Wb/A = 1 Ω·s</span> wird in 2.2 einmal gezeigt und danach benutzt.

---

## 1 · Einstieg

Geht so in `<section id="einstieg">`, `.stufe`-Nummer **1**, Überschrift **Einstieg**.

### 1.1 Aufhänger (zwei Absätze, kein Lehrbuchton)

**Absatz 1:**

> Ein Klassiker aus fast jeder Physiksammlung: Eine Spule mit Eisenkern hängt über einen Schalter
> an einer Quelle mit nur wenigen Volt. Parallel zur Spule sitzt eine kleine Glimmlampe, und die
> braucht zum Zünden 80 bis 100 Volt. Schließt du den Schalter, bleibt sie dunkel — kein Wunder,
> so viel Spannung liegt ja gar nicht an. Öffnest du ihn, blitzt sie hell auf. Für einen
> Augenblick liegt an der Lampe ein Vielfaches der Quellenspannung, und das an einer Stelle des
> Kreises, an der überhaupt keine Quelle mehr angeschlossen ist.

**Absatz 2:**

> Dasselbe steckt hinter einem Alltagseffekt: Wenn du im Dunkeln bei einem laufenden Gerät mit
> Motor den Stecker ziehst, siehst du manchmal einen kleinen Funken an den Kontakten. Und wer
> Schaltungen mit Relais baut, lötet fast immer eine Diode parallel zur Relaisspule, damit
> Schalter und Transistoren das Abschalten überleben. Auf dieser Seite klärst du drei Fragen:
> Wie kann beim Öffnen eines Schalters eine höhere Spannung entstehen, als die Quelle liefert?
> Warum passiert das nur beim Ausschalten, während der Strom beim Einschalten ganz gemächlich
> anwächst? Und woher nimmt der Funke seine Energie?

**Hinweis für den Bauagenten:** In diesem Aufhänger stehen **keine** eigenen Rechenwerte außer den
Literaturwerten „80 bis 100 Volt" (Quelle oben). Es gibt deshalb keine Kontrollrechnung für den
Aufhänger. Die Auflösung des Glimmlampenversuchs mit Zahlen folgt in 3.2 („Zurück zum Einstieg")
und ist dort gerechnet (K4h bis K4l im Kontrollskript).

### 1.2 Vorwissensfragen

Kopf der Karte wie im Referenzmodul:
`<div class="karte"><h3>Vorwissen prüfen</h3>` mit dem grauen Hinweissatz
*„Drei Fragen aus der Sekundarstufe I und der Einführungsphase. Wenn du hier hängst, lohnt sich ein
Blick zurück, bevor du weitermachst."*

Alle drei als `<div class="aufgabe" data-mc="…" style="border:none;padding:0;…">`, jeweils drei
Optionen. Jede Frage bereitet einen Schritt des Erklärteils vor; das steht im Feedback zur
richtigen Option.

---

#### vw1 — Reihenschaltung und Ohmsches Gesetz (Sek I)

**Frage:**

> Eine Spule mit dem Drahtwiderstand <span class="m">30 Ω</span> liegt in Reihe mit einem
> Widerstand von <span class="m">18 Ω</span> an einer Gleichspannungsquelle mit
> <span class="m">24 V</span>. Nach sehr langer Zeit fließt ein zeitlich konstanter Strom. Wie groß
> ist er?

<div class="tabelle">

| `data-i` | Option |
|---|---|
| 0 | <span class="m">0,80 A</span> |
| 1 | <span class="m">0,50 A</span> |
| 2 | <span class="m">1,33 A</span> |

</div>

`r: 1`

**Feedback (`fb`), je Eintrag ein eigener Denkfehler:**

- `fb[0]`: „Hier steht nur der Spulendraht im Nenner (24 V / 30 Ω = 0,80 A). Der zweite Widerstand
  liegt aber in Reihe und gehört dazu: In der Reihenschaltung addieren sich die Widerstände zu
  30 Ω + 18 Ω = 48 Ω."
- `fb[1]`: „Richtig. I = U/(R₁ + R₂) = 24 V / 48 Ω = 0,50 A. Merke dir den Gedanken: Ein
  konstanter Strom sieht in der Spule nur ihren Drahtwiderstand. Dass das nicht selbstverständlich
  ist, sondern eine Folge dessen, was auf dieser Seite kommt, siehst du gleich."
- `fb[2]`: „24 V / 18 Ω = 1,33 A würde fließen, wenn die Spule nur ein Stück widerstandsloser Draht
  wäre. Ihr Draht hat aber 30 Ω; der Gesamtwiderstand ist die Summe 48 Ω."

---

#### vw2 — Kinetische Energie (Einführungsphase)

**Frage:**

> Ein Wagen fährt mit der Geschwindigkeit <span class="m">v</span>. Seine Geschwindigkeit wird
> verdreifacht. Wie ändert sich seine kinetische Energie?

<div class="tabelle">

| `data-i` | Option |
|---|---|
| 0 | Sie wird dreimal so groß. |
| 1 | Sie wird neunmal so groß. |
| 2 | Sie wird sechsmal so groß. |

</div>

`r: 1`

**Feedback:**

- `fb[0]`: „Das gälte, wenn die Energie proportional zu v wäre. In E_kin = ½·m·v² steht die
  Geschwindigkeit aber im Quadrat: Aus 3v wird (3v)² = 9v²."
- `fb[1]`: „Richtig. E_kin = ½·m·v², also (3v)² = 9·v². Ein Zusammenhang, bei dem die Energie mit
  dem Quadrat einer Größe wächst, kommt gleich in der Spule wieder: dort ist die Größe die
  Stromstärke."
- `fb[2]`: „3 · 2 = 6 rechnet die Verdreifachung mit dem Faktor 2 aus ½·m·v². Der Faktor ½ ist
  aber eine Konstante und ändert sich nicht; nur v wird verdreifacht und dabei quadriert: 3² = 9."

---

#### vw3 — Trägheit und zweites Newtonsches Gesetz (Einführungsphase)

**Frage:**

> Zwei Wagen mit den Massen <span class="m">m</span> und <span class="m">3m</span> werden aus der
> Ruhe von derselben konstanten Kraft <span class="m">F</span> angeschoben. Was gilt nach der
> gleichen Zeit <span class="m">t</span> für ihre Geschwindigkeiten?

<div class="tabelle">

| `data-i` | Option |
|---|---|
| 0 | Beide Wagen sind gleich schnell, weil dieselbe Kraft wirkt. |
| 1 | Der schwerere Wagen hat nur ein Drittel der Geschwindigkeit des leichteren. |
| 2 | Der schwerere Wagen hat nur ein Neuntel der Geschwindigkeit des leichteren. |

</div>

`r: 1`

**Feedback:**

- `fb[0]`: „Die Kraft ist gleich, aber sie muss verschieden viel Masse in Bewegung setzen. Aus
  F = m·a folgt a = F/m: Die dreifache Masse bekommt nur ein Drittel der Beschleunigung."
- `fb[1]`: „Richtig. a = F/m, also v = a·t = (F/m)·t. Bei dreifacher Masse ist die Beschleunigung
  ein Drittel, und nach gleicher Zeit auch die Geschwindigkeit. Die Masse ist das Maß dafür, wie
  sehr sich ein Körper einer Änderung seiner Geschwindigkeit widersetzt. Für die Spule gibt es
  gleich ein genaues Gegenstück."
- `fb[2]`: „Hier ist die Masse quadriert worden (3² = 9). Die Masse steht in a = F/m aber nur
  einfach im Nenner; das Quadrat gehört zur Energie ½·m·v², nicht zur Beschleunigung."

**Kontrollrechnung (nur Bauagent):** vw1: 24 V / 48 Ω = 0,50 A, Distraktoren 24/30 = 0,80 A und
24/18 = 1,3333 A; vw2: 3² = 9; vw3: v ∼ 1/m, also 1/3 (Kontrollskript K7).

---
