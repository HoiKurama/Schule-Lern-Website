# Baustein: Druck mit oder ohne Lösungen

Implementiert im Referenzmodul `module/physik-q1-induktion.html`, zusammen mit der Formelleiste
(`baustein-formelleiste.md`), deren Formelsammlung am Ende jedes Ausdrucks steht.

## Knöpfe im Abschluss

Zwei Knöpfe ersetzen den alten `<button onclick="window.print()">Als Arbeitsblatt drucken</button>`.
Sie setzen eine Klasse am `<body>` und rufen `window.print()` auf; `afterprint` räumt sie wieder
ab. Der Hinweis steht direkt nach der `.knopfleiste` und wird **wörtlich samt `style`** aus der
Referenz übernommen:

```html
<button type="button" data-druck="arbeitsblatt">Arbeitsblatt drucken</button>
<button type="button" data-druck="loesungen">Mit Lösungen drucken</button>
…
<p class="druck-wahl" style="font-size:14px;color:var(--grau);margin:10px 0 0">Das Arbeitsblatt enthält alle Aufgaben mit Schreiblinien, aber keine Hilfen und Lösungen. „Mit Lösungen drucken“ gibt zusätzlich alle Hilfestufen, Musterlösungen und die richtigen Antworten aus. Der Lehrerteil wird in beiden Fällen nicht gedruckt, die Formelsammlung steht jeweils am Ende.</p>
```

## Die beiden Fassungen

| | Arbeitsblatt (`.druck-arbeitsblatt`) | Mit Lösungen (`.druck-loesungen`, auch Strg+P) |
|---|---|---|
| Hilfen, Musterlösungen | aus | alle Stufen |
| Auswahlaufgaben | leere Kreise | richtige Option mit ✓, darunter die Begründung |
| Zuordnung | Schreiblinie je Zeile | Lösungsbuchstabe je Zeile |
| Zahl- und Textaufgaben | Schreiblinien statt Feld | Lösungsweg bzw. Musterlösung |

In beiden Fassungen fehlen Lehrerteil, Eingabefelder, Knöpfe, Rückmeldungen und die Leiste. Der
Bearbeitungsstand (angeklickte Optionen, eingetippte Werte, Farben) kommt nicht aufs Papier.
Lange Formeln brechen im Druck am Gleichheits- oder Rechenzeichen um. Merksätze, Hinweise und
Beobachtungsaufträge werden nicht über eine Seitengrenze getrennt.

## Regeln für den Inhalt

- **Die Begründung zur Auswahlaufgabe ist `mcDaten[k].fb[r]`.** Ein führendes „Richtig",
  „Genau" oder „Stimmt" mit Satzzeichen fällt weg. Was bleibt, muss allein als Begründung
  tragen: Es nennt den Grund und hängt nicht an einem weggeschnittenen Satzanfang
  („Und genau hier liegt …" trägt nicht). Die fachliche Prüfung liest jede Lösungszeile.
- **Schreiblinien:** 6 unter Zahlaufgaben, 10 unter Textaufgaben, anders per `data-linien="8"` an
  der `.aufgabe`.
- **`nur-loesung`:** Lösungen außerhalb von `.hilfe-text`, etwa eine Lösungstabelle, bekommen
  diese Klasse; das Arbeitsblatt blendet sie aus. Jeder Text, der nur im Druck erscheint, auf dem
  Bildschirm aber nicht, gilt als Leck.

## Kopieranleitung für ein bestehendes Modul

Die CSS-Schritte stehen in `baustein-formelleiste.md` (Schritte 1 und 2). Dazu kommen:

1. Im Abschluss den alten Druckknopf durch die beiden Knöpfe ersetzen und den Hinweis `druck-wahl`
   wörtlich direkt nach der `.knopfleiste` einfügen.
2. Den Skriptbaustein `/* ============ Druck mit oder ohne Lösungen (generisch) ============ */`
   unverändert **direkt nach der Zuordnungs-Engine und vor der ersten Simulation** einfügen. Er
   braucht `mcDaten`.
3. Jede `fb[r]` in `mcDaten` darauf lesen, ob sie ohne „Richtig." allein trägt.

## Was der Modulcheck prüft

Zuerst den Bildschirm im Anfangszustand: Keine Lösungszeile, keine Schreiblinie, keine
Formelsammlung und kein Lösungstext dürfen sichtbar sein. Dann „bearbeitet" er die Seite
absichtlich. Auswahlaufgaben und Zuordnungszeilen werden abwechselnd richtig und falsch
beantwortet, alle Hilfen, Musterlösungen und Herleitungen aufgeklappt, Werte und Text
eingetragen. Gedruckt wird über die Knöpfe wie im Browser: `beforeprint`, Druckbild bei
A4-Satzbreite (680 px), `afterprint`.

- **Arbeitsblatt:** keine Hilfe, keine Lösungszeile, kein Lösungstext, keine Zeile Text, die im
  Anfangszustand nicht zu sehen war. Keine erkennbare richtige oder angeklickte Option (Farbe,
  Rahmen, Schrift, Zeichen davor), keine Eingabefelder, Schreiblinien bei jeder Aufgabe mit Feld.
- **Mit Lösungen und Strg+P:** alle Hilfen, jede Auswahlaufgabe mit Lösungszeile und eindeutig
  markierter Option, Lösungsbuchstaben in der Zuordnung.
- **Beide:** Formelsammlung mit allen Formeln, keine Leiste, kein Lehrerteil, nichts fest
  Positioniertes. Nach dem Drucken bleibt keine Druckklasse am `<body>`.

Mit zweitem Argument legt der Check beide Fassungen als PDF mit echtem KaTeX ab, ausgelöst über die Knöpfe.
