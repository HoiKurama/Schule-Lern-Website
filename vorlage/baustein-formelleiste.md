# Baustein: Formelleiste mit Erklär-Knopf

Implementiert im Referenzmodul `module/physik-q1-induktion.html`. Diese Datei beschreibt den
Datenvertrag, die Kopieranleitung für bestehende Module und was der Modulcheck prüft. Der
Druck mit oder ohne Lösungen steht in `baustein-druck.md` und wird im selben Durchgang übernommen.

## Was der Baustein tut

- Ab 1100 px läuft rechts neben dem Inhalt eine Leiste mit allen Formeln des Moduls mit
  (`position:sticky`), gruppiert nach Abschnitt, Kopfzeile „Nr · Titel".
- Darunter öffnet der feste Knopf „Σ Formeln" (unten rechts) die Leiste als Schublade. Schließen
  per ×, Esc oder Klick daneben; der Fokus bleibt in der offenen Schublade.
- Jede Formel hat einen ⓘ-Knopf (echter `<button>`, 44 px, `aria-expanded`). Er klappt auf: jedes
  Formelzeichen mit Bedeutung und Einheit, die Gültigkeit, einen typischen Fehler und den Link
  „↗ im Text". Der Link öffnet zugeklappte Herleitungen und setzt die Formel an die Lesestelle.
- Die Formel an der Lesestelle (40 % der Fensterhöhe) ist hervorgehoben (IntersectionObserver).
- Im Druck fehlt die Leiste. Am Ende steht auf eigener Seite eine Formelsammlung: Formel und
  Zeichenbedeutungen mit Einheit.

Alles wird aus dem Objekt `formelDaten` erzeugt. Am CSS und am Skriptbaustein wird nichts geändert.

## Markup

Der Inhalt steckt in `<div class="seite">`, die Leiste folgt nach der `.wrap` des Inhalts. Gemeint
ist die `.wrap` mit den Sections, **nicht** die im `header.kopf`.

```html
<div class="seite">
<div class="wrap">
  … Sections, Footer …
  <div class="formelsammlung" id="formelsammlung"></div>   <!-- letztes Kind von .wrap -->
</div>
<aside class="formelleiste" id="formelleiste" aria-labelledby="fl-titel">
  <div class="fl-kopf">
    <h2 id="fl-titel">Formeln dieses Moduls</h2>
    <button type="button" class="fl-zu" aria-label="Formelleiste schließen">×</button>
  </div>
  <div class="fl-inhalt"></div>
</aside>
</div>
<button type="button" class="fl-knopf primaer" aria-controls="formelleiste" aria-expanded="false"><span aria-hidden="true">Σ</span> Formeln</button>
<div class="fl-schleier" hidden></div>
```

**Sprungziele.** Die Formel im Text bekommt eine `id` mit Präfix `f-`, an der vorhandenen
`.m`-Formel selbst, nicht an einem Absatz: `<div class="m block" id="f-fluss" data-tex=… data-plain=…>`.
Jede `id="f-…"` im Text braucht einen Eintrag in `formelDaten`, sonst meldet der Check einen Blocker.

## Datenvertrag

`formelDaten` steht im Skript direkt vor dem Leistenbaustein:

```js
var formelDaten = [
  {abschnitt:"grundlagen", titel:"Der magnetische Fluss", formeln:[
    {id:"fluss", ziel:"f-fluss", tex:"\\Phi = B \\cdot A", plain:"Φ = B · A",
     zeichen:[
       {tex:"\\Phi", plain:"Φ", text:"magnetischer Fluss durch die Fläche", einheit:"Wb = T·m²"},
       {tex:"B", plain:"B", text:"magnetische Flussdichte", einheit:"T"},
       {tex:"A", plain:"A", text:"Fläche, die vom Feld durchsetzt wird", einheit:"m²"}],
     gilt:"Ein bis drei Sätze: unter welchen Bedingungen die Formel gilt.",
     fehler:"Ein typischer Schülerfehler, als Handlung benannt, mit dem Grund, warum er falsch ist."}
  ]}
];
```

| Feld | Pflicht | Inhalt |
|---|---|---|
| `abschnitt` | ja | `id` der `<section>`, zu der die Gruppe gehört |
| `titel` | ja | kurzer Gruppentitel, meist der Abschnittstitel |
| `id` | ja | eindeutig im Modul, nur Kleinbuchstaben, Ziffern und Bindestrich |
| `ziel` | ja | `id` der Formel im Text (`f-…`), im Abschnitt `abschnitt` |
| `tex` | ja | Kernformel wie in `data-tex`; im JS-String **jeden Backslash verdoppeln** |
| `plain` | ja | beginnt genau wie das `data-plain` am Sprungziel (Leerzeichen zählen nicht) |
| `zeichen` | ja | jedes Zeichen der Formel mit `tex`, `plain`, `text` (Bedeutung) und `einheit` |
| `gilt`, `fehler` | ja | Klartext ohne HTML, Unicode wie in `data-plain`, Dezimalkomma, duzen |

**`tex` und `plain`.** Sie geben die Kernformel des Textes wieder: gleiche Zeichen, gleiche
Reihenfolge, gleiche Vorzeichen. Einheitenangaben, Definitionsbereiche und Zusatzgleichungen
dürfen entfallen, `\frac` darf als `\dfrac` stehen. Beim Kopieren aus `data-tex` wird aus `\` im
JS-String `\\`. Ein vergessener Backslash fällt sonst nicht auf: `"\dfrac"` wird still zu
`dfrac`, `"\frac"` zu einem Steuerzeichen. Der Check meldet beides als Blocker. Kontrolle im
Browser: In der Leiste erscheint die Formel gesetzt, nicht als Buchstabenfolge.

**`einheit`.** In der Physik Pflicht: die SI-Einheit, bei Größen ohne Einheit `dimensionslos`. In
Mathematik und Informatik wird das Feld weggelassen, dann entfallen die Einheitenzeile in der
Erklärung und die Klammer in der Formelsammlung. Nur wenn eine Formel im Modul an einen
Sachkontext gebunden ist, steht dessen Einheit (etwa `m³/h` für eine Zuflussrate).

## Welche Formeln hinein

Alle Gesetze, Definitionen und Beziehungen, die Erklärteil und Vertiefung einführen, auch das
Ergebnis einer Herleitung. Nicht hinein: Zahlenbeispiele, Zwischenschritte,
Einheitenumrechnungen, Formeln aus Aufgaben und Musterlösungen. Die Reihenfolge folgt dem Text.
Richtwert: 5 bis 12 Einträge.

- **Kernformel kurz halten.** Die Leiste hat rund 200 px Platz. Lange Formeln brechen dort und
  in der Formelsammlung am Gleichheits- oder Rechenzeichen um. Zusatzschreibweisen wie
  „= [F(x)] von a bis b" gehören nicht in `tex`.
- **Regeltabellen** (Grundintegrale, Ableitungsregeln) gehen nicht Zeile für Zeile hinein.
  Aufgenommen wird eine Zeile nur, wenn sie im Erklärteil als eigene Regel eingeführt und in den
  Übungen gebraucht wird. Dann bekommt die `.m` ihrer Zelle die `id="f-…"`.

## Nichts verraten

Die Erklärungen stehen jederzeit offen, am Bildschirm neben den Fragen und gedruckt am Ende des
Arbeitsblatts. Deshalb gilt:

- Keine Antwort einer Vorwissens- oder Simulationsfrage, kein Zahlenwert aus einer Übung. Ein
  Satz wie „Liegt die Schleife ganz im Feld, ist U = 0" wäre im Induktionsmodul die Antwort auf `sim1`.
- **Vorwissensfragen fragen nicht nach Bedeutung oder Einheit eines Zeichens, das die Leiste
  erklärt.** Die Einheit steht in der Leiste und in der Formelsammlung. Beim Übernehmen in ein
  bestehendes Modul wird `formelDaten` gegen jede Frage und jede richtige Option in `mcDaten`
  abgeglichen. Kollidiert ein Leistentext, wird er umformuliert. Lässt sich die Kollision nur
  mit einer neuen Frage lösen, wird das gemeldet und nicht eigenmächtig geändert.
- Der typische Fehler nimmt keine Hilfestufe wörtlich vorweg, sonst verliert die Stufung ihren Sinn.
- Eine Gültigkeitsbedingung wird trotzdem vollständig angegeben, auch wenn sie eine
  Simulationsfrage berührt. Sie darf die Antwort nur nicht wörtlich enthalten.

## Kopieranleitung für ein bestehendes Modul

§ 1 von `bausteine.md` („kompletter `<style>`-Block") gilt hier **nicht**. Das Modul behält sein
CSS, getauscht werden nur die genannten Blöcke. Die Datei wird nur mit Edit geändert, nie neu
geschrieben, damit ihre Zeilenenden (CRLF oder LF) erhalten bleiben.

1. **CSS Leiste:** den Block ab `/* ---------- Formelleiste ---------- */` bis vor
   `/* ---------- Druck ---------- */` aus der Referenz direkt **vor** den Druck-Kommentar der
   Zieldatei einfügen, in jedem Fall vor `@media print`. Danach stehende Bildschirmregeln würden
   die Druckregeln überschreiben.
2. **CSS Druck:** nur den Block `@media print{…}` samt Kommentar darüber durch den der Referenz
   ersetzen. Andere Blöcke unter dem Druck-Kommentar, etwa `@media (max-width:600px)`, bleiben.
3. **Hover-Farbe:** Der Knopf „Σ Formeln" trägt `.primaer`. Weicht `button.primaer:hover` von der
   Fachfarbe ab, wird es angeglichen: Physik `#1a43b8`, Mathematik `#0b6845`, Informatik `#92400e`.
4. **Markup** wie oben: `.seite` um die `.wrap` des Inhalts, Formelsammlung als letztes Kind,
   dahinter Leiste, Knopf und Schleier.
5. **Sprungziele:** an jeder aufgenommenen Formel im Text `id="f-…"` setzen.
6. **Skript:** `formelDaten` und den Baustein `/* Formelleiste: Aufbau und Bedienung (generisch) */`
   unverändert direkt nach `setTimeout(formelnRendern, 1500);` einfügen. Die Leiste muss vor dem
   `load`-Ereignis gebaut sein, sonst setzt KaTeX ihre Formeln nicht.
7. **Druck** nach `baustein-druck.md` umstellen (Knöpfe, Hinweis, Skriptbaustein).
8. **Prüfen:** `PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/DATEI.html"`. Blocker
   und Mängel müssen leer sein, `katex_gesetzt` meldet alle Formeln und `katex_fehler` ist 0.

**Altfehler.** Meldet der Check einen Blocker, der nicht vom Baustein stammt, gilt: Technische
Fehler wie ein Steuerzeichen im Quelltext oder ein KaTeX-Fehler werden in derselben Runde behoben
und im Bauprotokoll unter „Altfehler" vermerkt. Fachliche Änderungen am Bestand werden gemeldet,
nicht eigenmächtig vorgenommen.

## Was der Modulcheck prüft

- **Vertrag:** Pflichtfelder, ids, Backslashes, Steuerzeichen, `plain` passend zur Formel am
  Sprungziel, jede `id="f-…"` mit Eintrag, Formelsammlung am Ende mit je einer Zeile pro Formel
  und einer Angabe pro Zeichen. Bei `physik-`-Modulen ist `einheit` Pflicht.
- **Erklärungen:** Jede klappt auf und zu, `aria-expanded` stimmt, alle Zeichen und Einheiten
  werden angezeigt.
- **Sprunglinks** bei 1280 px, mit weichem Scrollen und in der Schublade bei 390 px: Das Ziel steht
  im Bild, und genau diese Formel ist hervorgehoben.
- **Hervorhebung** an der Lesestelle, keine Hervorhebung in Abschnitten ohne Formeln.
- **Leiste** bei 1280 und 1100 px. **Schublade** bei 1099, 900 und 390 px: Öffnen, Schließen auf
  drei Wegen, Fokus, Fokusfalle, Doppelklick, Trefferflächen ≥ 44 px, kein Querscrollen.
- **Überlauf** mit echtem KaTeX: Keine Formel überragt die Leiste oder im Druck (A4) den Rand.

Jeder Teilschritt meldet eine Ausnahme als Blocker, statt den Lauf abzubrechen. Das JSON kommt immer.

## Regel für die Vorwissensfragen

Die Leiste steht ab dem Einstieg am Rand, der Arbeitsblatt-Druck enthält die Formelsammlung. Eine
Vorwissensfrage nach einer Einheit, einem Formelzeichen oder dem Aufbau einer Formel, die in
`formelDaten` steht, verrät sich deshalb selbst. Vorwissensfragen im Einstieg prüfen Begriffe und
Zusammenhänge (Bahnform, Richtung, Proportionalität), nie Einheiten aus dem Formelbestand. Im
Referenzmodul wurde aus diesem Grund die Einheitenfrage zur Flussdichte durch eine Frage zur
Bahnform im Magnetfeld ersetzt. Vor der Übernahme in ein Modul jede `vw`-Frage gegen die
`zeichen`-Einträge und `einheit`-Felder prüfen.

## Sprungziele und Lösungstexte beim Übernehmen

- **Kein Sprungziel in einer `<summary>`.** Steht die Formel nur in der Überschrift einer zugeklappten
  Herleitung, ist sie als Ziel unbrauchbar. Dann die Formel im Fließtext davor oder das Ergebnis
  der Herleitung nehmen oder den Eintrag weglassen.
- **Breite Formeln kürzen.** Ketten wie „A = … = …“ oder „Bilanz = P − N und Flächeninhalt = P + N“
  ragen über die 204 px der Leiste. `plain` darf ein Anfangsstück von `data-plain` sein; die volle
  Formel bleibt im Text.
- **Lösungstexte müssen ohne „Richtig.“ tragen.** Beginnt `fb[r]` mit „Richtig, und das …“ oder "Richtig, das ist …", bleibt im
  Lösungsdruck ein Satzrest übrig. Solche Texte werden umformuliert (Beispiel: „Richtig. Die vollständige
  Begründung lautet: …“).
