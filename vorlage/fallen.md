# Bekannte Fallen beim Modulbau

Gesammelt in Durchgang 1 bis 4 (bis 03.10.2026). Jede hat schon einmal Zeit oder einen Prüfbefund
gekostet. Ergänzungen kommen hier dazu, nicht in eine Übergabenotiz.

## Arbeitsweise
- **Simulation zuerst bauen.** Sie steht am Dateiende und fehlte dreimal, weil der Bau vorher abbrach.
- **Zwischenstand sichern:** Datei früh anlegen, dann abschnittsweise füllen. Nie mehr als sechs bis
  acht Werkzeugaufrufe ohne gespeicherten Stand.
- **Python-Skripte nie per Heredoc** (`python - <<'PY'`). Die Shell frisst Backslashes, aus
  `\\varepsilon` wird ein Vertikaltabulator plus `arepsilon`. Skript als Datei schreiben, dann
  aufrufen. Am Ende jedes Ersetzungsskripts prüfen:
  `assert not [c for c in s if ord(c) < 32 and c not in "\n\r"]`
- `numpy` ist nicht installiert, gerechnet wird mit der Standardbibliothek.
- Eigene Prüfskripte starten den Browser mit `browser_starten(p)` aus
  `werkzeug/pruefschritte/browser.py`. Fehlt Playwrights Chromium, weicht es auf Chrome oder Edge aus.
  Aus `output/<modul>/` heraus vorher `sys.path.insert(0, "projekte/q1-lernplattform/werkzeug")`,
  dann `from pruefschritte import browser_starten`. Ausgaben mit Sonderzeichen brauchen
  `sys.stdout.reconfigure(encoding="utf-8")`.
- Ein Bericht über ein fertiges Modul ist eine Behauptung. Nachmessen, nicht glauben.

## Engine-Verträge, die schon gebrochen wurden
- Zahl der Feedbacktexte in `mcDaten` = Zahl der Optionen im Markup.
- `var ergebnisse` steht am Skriptende und wird darüber benutzt (Hoisting). Reihenfolge nicht ändern.
- Nur **eine** Zuordnungsaufgabe pro Modul (`querySelector`, Einzahl).
- Die Hilfe-Engine hängt den Musterlösungs-Klick an jedes `[data-loesung]`, auch an
  `.zeile[data-loesung]` der Zuordnung. Deshalb bekommt die Zuordnung keinen
  `.hilfe-text[data-stufe="9"]`.
- In `formelDaten` muss `abschnitt` genau die `id` der `<section>` sein.
- Die Formelleiste zeigt keine Formel, nach der eine Vorwissens- oder Simulationsfrage fragt.
- Umschaltknöpfe mit `aria-pressed` brauchen eine eigene CSS-Regel für den aktiven Zustand.

## Was nur ein Mensch oder Prüfer findet
- literaler Tabulator in `data-tex` (KaTeX läuft mit `throwOnError:false` und meldet nichts)
- Fußzeile oder Texte des Referenzmoduls, die im neuen Modul stehen geblieben sind
- Vorwissensfragen mit den Antwortschlüsseln des Referenzmoduls
- Widerspruch zwischen Erklärtext und Simulation

## KaTeX
- Ein Leisteneintrag, der mit einem Subskript beginnt (`x_{\max} = …`), überdeckt den Sprunglink
  darüber. Abhilfe: mit `\hat{x}` beginnen, bei Überbreite `\small` oder `\footnotesize`.
- `€` erzeugt Warnungen, `\text{Euro}` nehmen.
- `\vec{p}\,'` ist ungültig, anderen Buchstaben wählen.
- Formeln, die auf `\vec{d}` enden, ragen im Druck über den Rand. `\;` ans Ende.
- Vorzeichen nach `|` als `{-}` schreiben, sonst entsteht eine Lücke wie bei einer Subtraktion.
- Koordinatentupel wie `(3|2)` mit `\,|\,` setzen.
- Tipp-Texte beginnen nicht wortgleich mit einem sichtbaren Satz.
