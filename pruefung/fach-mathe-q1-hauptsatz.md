# Fachprüfung `mathe-q1-hauptsatz.html`

Urteil: **Nacharbeit nötig, aber gering.** 40 Werte per Python nachgerechnet (u. a. V(9) = 40,90 m³, V(4) = 24,23 m³, ∫₂⁷f = 68/3 ≈ 22,67, I₀(10,5) = 29,925, a3-Diagramm B, Simulation gegen geschlossene Form): kein Rechenfehler.
Lehrplanbezug wörtlich und echt, Dezimalkomma und Duzen durchgehend, 545/545 `data-plain`.
Gut gelöst: Distraktor-Feedback (15 Wege mit Zahlen widerlegt), zwei echte AB-III-Aufgaben, Beweis in Abschnitt 2, Simulation rechnet numerisch statt aus geschlossener Stammfunktion, Lehrerteil.

## Blocker

- **S1 · Zeile 201 (Einstieg):** „Genauigkeit von einem Zehntelliter … 320 Streifen" ist um Faktor 1000 falsch. Vorgängermodul: 0,10 m³. Zeilen 398 und 806 sagen richtig „Zehntel Kubikmeter". → „einem Zehntel Kubikmeter".

## Mängel

- **M1 · Z. 296, Kernaussage 1:** „Die Integralfunktion ist die Umkehrung des Ableitens" zu stark. Richtig: Ableiten macht das Integrieren rückgängig (steht in Z. 334).
- **M2 · Z. 722, Musterlösung a6:** „alle Produktsummen negativ, also auch ihr Grenzwert" trägt nicht. Besser: f stetig auf [a; x], also Maximum M < 0, also ∫ₐˣ f ≤ M·(x − a) < 0. Zudem liegt die Probe I₀(−3) = 3 außerhalb des Gegenbeispiel-Intervalls [0; 10].
- **M3 · sim1 (Z. 541) und sim2 (Z. 552):** ohne Simulation aus dem Erklärteil beantwortbar (sim2 ist Wiederholung des Fehlerkastens Z. 339–343). Mindestens eine Frage auf Rate B oder C umstellen, z. B. „Warum steht Unterschied bei Rate A exakt auf 0,000, bei Rate C nicht zwangsläufig?"
- **M4 · Z. 495, Beobachtungsauftrag:** Nach Wechsel auf Rate B bleibt x = 6,00, `bPlay` setzt nur bei x ≥ 12 zurück, der Tiefpunkt bei x = 4,00 wird nicht durchlaufen. → im Auftrag „und x = 0,00" ergänzen.
- **M5 · `gitter()` Z. 1127–1129:** Rate-C-Achsen 4,5 / −0,5 / ±14,5 werden als 5 / −1 / ±15 beschriftet. → fMin −1, fMax 5, iMin −15, iMax 15 (umschließt weiter alle Werte). (Deckt sich mit Technikprüfung Mangel 1.)
- **M6 · Z. 1231:** Tangente nutzt `f(x)` statt gemessener Steigung. → `var m = (Isum(f,a,x+0.02)-Isum(f,a,x-0.02))/0.04;`
- **M7 · a4:** Alternativeinheit m³ unerreichbar (0,01 m³ liegt 3,6·10⁻⁴ daneben). → `alt: {…, tol: 0.0005}`.
- **M8 · Gültigkeitsbedingungen:** Z. 411 (xⁿ → xⁿ⁺¹/(n+1)) fehlt x ≠ 0 bei n < 0 und x > 0 bei nicht ganzzahligem n; Z. 424 fehlt k ≠ 0.
- **M9 · sim1/sim2:** als AB II ausgewiesen, sim2 ist AB I. Nach Behebung von M3 passt AB II.
- **M10 · Kleinigkeiten:** Export nennt „Offene Aufgabe 1/2", Seite heißt Aufgabe 6/7. Anzeige „Iₐ(x)" (U+2090) vs. `data-plain` „I_a(x)" uneinheitlich.

Empfehlung: einsatzbereit nach S1, M2, M4, M5; Rest vor dem zweiten Durchlauf, vor allem M3.
