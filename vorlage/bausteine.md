# Aufgabenbausteine und Engine-Verträge

Alle Bausteine sind im Referenzmodul `module/physik-q1-induktion.html` implementiert.
Diese Datei beschreibt, was beim Kopieren unverändert bleibt und was ausgetauscht wird.

---

## 1 · Was aus dem Referenzmodul unverändert übernommen wird

**Vollständig kopieren, nicht anfassen:**

| Block | Fundstelle | Zweck |
|---|---|---|
| kompletter `<style>`-Block | Kopf | Design, Layout, Druckansicht |
| `formelnRendern()` | Skriptanfang | KaTeX mit Fallback |
| MC-Engine (`document.querySelectorAll("[data-mc]")…`) | Skript | Multiple Choice |
| Zahlen-Engine (`document.querySelectorAll("[data-num]")…`) | Skript | Zahleneingabe mit Einheit |
| Hilfesystem (`[data-hilfe]`, `[data-loesung]`) | Skript | dreistufige Hilfen, Musterlösung |
| Zuordnungs-Engine (`[data-check="zuordnung"]`) | Skript | Zuordnungsaufgabe |
| Formelleiste (`/* Formelleiste: Aufbau und Bedienung (generisch) */`) | direkt nach `formelnRendern()` | Leiste, Schublade, Formelsammlung, siehe § 10 |
| Druckmodi (`/* Druck mit oder ohne Lösungen (generisch) */`) | nach der Zuordnungs-Engine, vor der ersten Simulation | Arbeitsblatt und Lösungsdruck, siehe § 11 |
| Export-Funktion (`#bExport`) | Skriptende | Ergebnis in die Zwischenablage |
| Speicherblock (`/* Bearbeitungsstand im Browser speichern (generisch) */`) | ganz am Skriptende, nach dem Export | Stand im `localStorage`, Löschknopf, Hinweis, siehe § 9 |

Einzige erlaubte Änderung im `<style>`: die drei Akzent-Tokens in `:root` und der Verlauf in
`header.kopf`, gemäß Farbtabelle in `CLAUDE.md`. Das gilt für neue Module. Bestehende Module
behalten ihr CSS und tauschen nur einzelne Blöcke, siehe Kopieranleitung in § 10.

**Breite Inhalte kapseln.** Zwei Dinge schrumpfen nicht unter ihre Inhaltsbreite und schieben
sonst die ganze Seite auf dem Handy zur Seite: von KaTeX gesetzte Blockformeln und Tabellen ab
etwa vier Spalten. Beide haben deshalb einen eigenen waagerechten Scrollbereich. Für Formeln
erledigt das `.m.block` von selbst; **jede `<table>` wird von Hand in einen Wrapper gesetzt**:

```html
<div class="tabelle">
  <table> … </table>
</div>
```

Ohne diesen Wrapper scrollt die Seite bei 390 px Breite quer, und das ist ein Mangel.

Die Mindestbreite der Tabelle steht auf `min(420px, 100%)`, nicht auf `420px`. Auf breiten
Bildschirmen greift die 420er-Schranke und hält die Tabelle lesbar; auf einem 350 px breiten
Container sinkt der Mindestwert auf die Containerbreite, sodass der Wrapper nicht selbst zum
Überläufer wird. Mit festen 420 px blieben sonst 3 px Überlauf am Dokument stehen.

Dasselbe gilt für **Formeln im Fließtext**. `.m` trägt `white-space:nowrap`, damit eine Formel
nicht mitten im Symbol umbricht — eine lange Formel schiebt damit aber die ganze Seite zur
Seite. Deshalb ist `.m` ein `inline-block` mit eigenem waagerechtem Scrollbereich:

```css
.m{white-space:nowrap;display:inline-block;max-width:100%;overflow-x:auto;overflow-y:hidden;vertical-align:bottom}
```

Das ist Teil des kopierten CSS-Blocks und muss nicht von Hand gesetzt werden. Es heißt aber:
Eine sehr lange Formel im Fließtext bleibt lesbar, ist auf schmalen Geräten jedoch nur durch
Wischen ganz zu sehen. Wo eine Formel länger als etwa eine halbe Zeile wird, gehört sie
ohnehin besser als `<div class="m block">` abgesetzt. Im Druck und in der Formelleiste bricht
`.m` am Gleichheits- oder Rechenzeichen um, weil Papier nicht scrollt.

**Modulspezifisch neu geschrieben wird:**

- der gesamte Inhalt der `<section>`-Blöcke
- das Objekt `mcDaten`
- das Objekt `numDaten`
- das Objekt `formelDaten` und die `id="f-…"` an den Formeln im Text (§ 10)
- die Simulations-IIFE
- die Namensliste im Export (`var namen = {…}`)

---

## 2 · Formeln

Jede Formel ist ein Element mit beiden Attributen. `data-plain` ist Pflicht.

```html
<!-- im Fließtext -->
<span class="m" data-tex="\Phi = B \cdot A" data-plain="Φ = B · A"></span>

<!-- abgesetzt, zentriert -->
<div class="m block" data-tex="U_{\text{ind}} = -N \cdot \frac{\mathrm{d}\Phi}{\mathrm{d}t}"
     data-plain="U_ind = −N · dΦ/dt"></div>
```

`data-plain` wird angezeigt, wenn KaTeX nicht geladen werden kann. Es muss ohne Nachdenken
lesbar sein: Unicode für griechische Buchstaben, Hochzahlen (`10⁻⁴`), Malpunkt `·`, Minus `−`.
Brüche als `a/b` schreiben, nicht als LaTeX-Rest.

Nach jedem dynamischen Einfügen von Markup mit Formeln muss `formelnRendern()` erneut
aufgerufen werden.

---

## 3 · Multiple Choice mit Distraktor-Feedback

**Markup** – die `data-i`-Indizes beginnen bei 0 und entsprechen der Reihenfolge in `mcDaten`:

```html
<div class="aufgabe" data-mc="sim1">
  <span class="ab">Anforderungsbereich II</span>
  <div class="frage">Frage im Klartext …</div>
  <div class="optionen">
    <label class="opt" data-i="0"><input type="radio" name="sim1"><span>Option A</span></label>
    <label class="opt" data-i="1"><input type="radio" name="sim1"><span>Option B</span></label>
    <label class="opt" data-i="2"><input type="radio" name="sim1"><span>Option C</span></label>
  </div>
  <div class="rueck"></div>
</div>
```

`name` des Radios und der Wert von `data-mc` müssen identisch sein.

**Daten:**

```js
var mcDaten = {
  sim1:{ r:1, fb:[
    "Feedback zu Option A – benennt den Denkfehler.",
    "Richtig. Kurze Begründung, warum es stimmt.",
    "Feedback zu Option C – benennt den Denkfehler."
  ]}
};
```

`r` ist der Index der richtigen Option. Das Feedback-Array hat genau so viele Einträge wie
Optionen. Jeder Distraktor braucht einen eigenen, inhaltlichen Text: Was hat der Schüler
vermutlich gedacht, und warum trägt das nicht? Formulierungen wie „Leider falsch" oder
„Versuch es noch einmal" sind nicht zulässig.

---

## 4 · Zahleneingabe mit Einheitenprüfung

**Markup:**

```html
<div class="aufgabe" data-num="a1">
  <span class="ab">Anforderungsbereich I</span>
  <div class="frage">Berechne …</div>
  <div class="eingabe">
    <input type="number" step="any" placeholder="Zahlenwert">
    <select>
      <option value="">Einheit…</option>
      <option value="Wb">Wb</option>
      <option value="mWb">mWb</option>
      <option value="T">T</option>
    </select>
    <button class="primaer">Prüfen</button>
  </div>
  <div class="rueck"></div>
  <div class="hilfen">
    <button data-hilfe="1">Tipp</button>
    <button data-hilfe="2">Ansatz</button>
    <button data-hilfe="3">Lösungsweg</button>
  </div>
  <div class="hilfe-text" data-stufe="1">…</div>
  <div class="hilfe-text" data-stufe="2">…</div>
  <div class="hilfe-text" data-stufe="3">…</div>
</div>
```

Die Einheitenliste enthält immer mindestens eine physikalisch falsche Einheit als Distraktor.

**Daten:**

```js
var numDaten = {
  a1:{ wert:2.0, einheit:"mWb", tol:0.05,
       alt:{wert:0.002, einheit:"Wb"},          // dieselbe Größe in anderer Einheit, optional
       ok:"Richtig. Rechnung in einer Zeile.",
       falschEinheit:"Zahlenwert passt, Einheit nicht – Hinweis worauf.",
       nah:"Rückmeldung, wenn der Wert um Faktor 0,5 bis 2 danebenliegt.",
       weit:"Rückmeldung bei grobem Fehler, verweist auf die Hilfen." }
};
```

`tol` ist die absolute Toleranz in der Hauptheinheit. Sie wird so gewählt, dass sinnvolles
Runden akzeptiert wird, ein Rechenfehler aber nicht.

**Die Alternativeinheit erbt dieselbe Strenge.** Die Engine rechnet `tol` mit demselben Faktor
in die Alternativeinheit um, mit dem auch der Sollwert umgerechnet ist. Bei `wert:2.0` mit
`tol:0.05` und `alt:{wert:0.002}` gilt in Weber also die Toleranz 0,00005 — nicht mehr und nicht
weniger. Man muss die Toleranz somit nur **einmal** festlegen.

Das war nicht immer so: Ursprünglich prüfte die Engine die Alternativeinheit relativ mit drei
Prozent. Das war zugleich zu lax und unfair — bei einer Aufgabe mit Sollwert 25,75 kWh wurden
26500 Wh (2,9 % daneben) als richtig gewertet, 25,80 kWh (0,19 % daneben) dagegen abgelehnt.
Der Vergleich trägt seither außerdem eine Schranke `eps`, weil `Math.abs(v - wert) <= tol` sonst
genau auf der Toleranzgrenze an der Fließkommadarstellung scheitert: 25,80 − 25,75 ergibt binär
0,050000000000000710 und wäre ohne diese Schranke „falsch".

---

## 5 · Dreistufiges Hilfesystem

Die drei Stufen haben feste Rollen und dürfen nicht ineinanderfallen:

| Stufe | Rolle | Faustregel |
|---|---|---|
| 1 Tipp | räumt eine Hürde weg | eine Zeile, nennt keine Formel |
| 2 Ansatz | gibt die Formel und den Weg | zwei bis drei Zeilen, rechnet nicht |
| 3 Lösungsweg | vollständige Rechnung mit Ergebnis | mit Zwischenschritten und Einheiten |

Musterlösungen offener Aufgaben liegen in `.hilfe-text[data-stufe="9"]` und werden über
`<button data-loesung="…">` umgeschaltet. Sie enthalten immer zwei Teile: die erwartete
Argumentation und darunter fett die **Bewertungskriterien** als Aufzählung mit `·` getrennt.

---

## 6 · Zuordnungsaufgabe

Diagramme als Inline-SVG in `.diagramme`, darunter die Zeilen mit `data-loesung`:

```html
<div class="zuordnung">
  <div class="zeile" data-loesung="A"><span>Situationsbeschreibung</span>
    <select><option value="">…</option><option>A</option><option>B</option>
            <option>C</option><option>D</option></select></div>
</div>
<div class="knopfleiste"><button class="primaer" data-check="zuordnung">Prüfen</button></div>
<div class="rueck"></div>
```

Die Reihenfolge der Situationen darf nicht der Reihenfolge der Diagramme entsprechen.
Die Rückmeldung bei Teilerfolg nennt die Denkstrategie, nicht die Lösung.

Pro Modul ist nur **eine** Zuordnungsaufgabe vorgesehen, weil die Engine über einen festen
Selektor läuft. Werden mehrere gebraucht, wird die Engine vorher auf `querySelectorAll`
umgestellt und der Selektor pro Aufgabe gebunden.

---

## 7 · Simulation

Die Simulation ist der einzige Teil, der pro Modul wirklich neu entsteht. Vorgaben:

- eigene IIFE, kein globaler Zustand außer `ergebnisse`
- Canvas mit festen internen Maßen, `width="1000"`, Höhe nach Bedarf
- feste Umrechnung zwischen Pixeln und physikalischer Größe, oben als Konstante dokumentiert
- Regler in `.regler`, Momentanwerte in `.anzeige`, Bedienknöpfe in `.knopfleiste`
- `requestAnimationFrame`-Schleife mit `dt`-Begrenzung (`Math.min(0.05, …)`), damit ein
  Tabwechsel keinen Sprung erzeugt
- Ziehen über `pointerdown`/`pointermove` mit `setPointerCapture`, damit es am Tablet läuft
- alle angezeigten Zahlen über eine `fmt(zahl, stellen)`-Funktion mit Komma
- **Diagramme, die sich mit aufbauen**, sind der didaktische Kern: Sie zeigen den Zusammenhang
  zwischen Größe und Änderungsrate. Wo das Thema es hergibt, wird dieses Muster übernommen.

Vor der Auslieferung wird die Simulation gegen eine Handrechnung geprüft: mindestens ein
Wertepaar aus den Momentanwerten wird nachgerechnet und muss übereinstimmen.

---

## 8 · Beobachtungsauftrag

Jede Simulation bekommt darüber einen Kasten:

```html
<div class="auftrag">
  <b>Beobachtungsauftrag</b><br>
  Konkrete Handlungsanweisung, was einzustellen ist, worauf zu achten ist und
  welcher Satz am Ende formuliert werden soll.
</div>
```

Nicht „probiere ein bisschen herum", sondern eine Frage, die sich nur durch das Experiment
beantworten lässt. Direkt danach folgen zwei Multiple-Choice-Fragen, die genau darauf zielen.

---

## 9 · Selbstcheck und Export

Der Selbstcheck listet Kompetenzen als „Ich kann …"-Sätze, formuliert nah an den
Kompetenzerwartungen des Kernlehrplans. Die Export-Funktion sammelt die Ergebnisse aus dem
Objekt `ergebnisse`; jeder Aufgabenschlüssel muss deshalb in `var namen = {…}` am Skriptende
eingetragen sein, sonst taucht die Aufgabe im Export nicht auf.

Der **Speicherblock** steht unverändert als letzter Block im Skript. Er liest den Stand aus dem
DOM (gewählte Option, Zahleneingaben, Zuordnungen, geöffnete Hilfestufen, Textfelder, Selbstcheck)
und spielt ihn beim Laden als Klicks nach – deshalb muss er nach allen Engines stehen. Er setzt
die Verträge der Engines voraus: `.opt.richtig/.falsch`, `.rueck.zeig`, `.hilfe-text[data-stufe]`,
`button[data-loesung]` für Stufe 9. Für die Bilanz der Übersicht zählen nur selbstprüfende
Aufgaben: `[data-mc]`, `[data-num]` mit Zahlenfeld und `[data-check]`. Ändert sich die Anzahl
dieser Elemente, verwirft er einen alten Stand. Knopf und Hinweistext erzeugt er selbst; im
Druck-CSS steht dafür `.speicherhinweis` in der Ausblendliste.

---

## 10 · Formelleiste mit Erklär-Knopf

Mitlaufende Leiste mit allen Formeln des Moduls, ⓘ-Erklärung je Formel, Schublade unter 1100 px,
Formelsammlung im Druck. Datenvertrag `formelDaten`, Kopieranleitung für bestehende Module und
Prüfumfang stehen in **`vorlage/baustein-formelleiste.md`**.

---

## 11 · Druck mit oder ohne Lösungen

Zwei Knöpfe im Abschluss: „Arbeitsblatt drucken" (Schreiblinien, keine Hilfen und Lösungen) und
„Mit Lösungen drucken". Knöpfe, Regeln für `fb[r]`, Kopieranleitung und Prüfumfang stehen in
**`vorlage/baustein-druck.md`**.
