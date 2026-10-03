# Exponentialfunktionen — Inhaltsprotokoll

Stand: gebautes Modul `module/mathe-q1-exponentialfunktionen.html` (Mathematik LK Q1, Inhaltsfeld Funktionen und Analysis,
ca. 135 Minuten). Modulcheck ohne Blocker und Mängel, 409 von 409 Formeln gesetzt, kein Querscrollen bei 390, 900 und 1280 px.
Gebaut auf der Vorlage `mathe-q1-flaechen-zwischen-graphen.html`.

## Aufbau

| Abschnitt | Inhalt |
|---|---|
| 1 Einstieg | Vorwissen vw1 (linear oder exponentiell), vw2 (Kettenregel), vw3 (negative Exponenten) |
| 2 Grundlagen | f(x) = c·a^x mit Wachstumsfaktor, a = 1 + p/100, e über m(a) = lim (a^h − 1)/h, (e^x)′ = e^x, a^x = e^(x·ln a), (a^x)′ = ln a·a^x, Kettenregel für e^g, Exponentialgleichungen mit ln |
| 3 Vertiefung | f′ = k·f, Eindeutigkeit über (f·e^(−kt))′ = 0, k = ln a, Verdopplungs- und Halbwertszeit T = ln 2/\|k\|, beschränktes Wachstum f = S − (S − B₀)e^(−kt), Modellprüfung |
| 4 Simulation | Modelle an Messwerten prüfen, drei Datensätze, zwei Diagramme |
| 5 Übungen | a1 bis a7; a3 ist die Zuordnungsaufgabe, a4/a5 mit Alternativeinheit |
| 6 Abschluss | Selbstcheck, Hinweis auf Zentralabitur, Export und Druck, Lehrerteil |

Formelleiste: 12 Einträge in zwei Gruppen, bewusst **ohne** „gleiche Quotienten“ und 2^(−3) (beides sind Lösungen der
Vorwissensfragen vw1 und vw3).

## Simulation

Oben Messwerte und Modellkurve (exponentiell oder beschränkt, Stelle t₀ ziehbar, optional Tangente und logarithmische
senkrechte Achse). Unten Änderungsrate gegen Bestand: schwarze Punkte sind Differenzenquotienten der Messwerte, die
Gerade gehört zum Modell, der goldene Punkt zur Stelle t₀.

| Datensatz | Konstruktion | Streuung |
|---|---|---|
| Bakterienkultur, t = 0 bis 7 h | 2,0·e^(0,5t) | Faktoren 0,96 bis 1,05 |
| Koffein im Blut, t = 0 bis 10 h | 80·e^(−ln 2/5·t), Halbwertszeit 5 h | Faktoren 0,97 bis 1,03 |
| Tasse Kaffee, t = 0 bis 30 min (Schritt 2) | 20 + 65·e^(−0,07t) | ± 0,5 °C additiv |

Regler: B₀ (je Datensatz), k von −0,6 bis 0,6 (Schritt 0,005), S 0 bis 120, t₀ 0 bis 100 %. „Bestanpassung zeigen“ sucht die
Werte mit der kleinsten mittleren Abweichung (Wurzel aus dem Mittel der quadrierten Abstände, **absolute** Abweichungen,
keine logarithmierten). Beim Wechsel von exponentiell auf beschränkt wird ein negatives k positiv, damit der Abfall auf
null (S = 0) als Sonderfall sichtbar wird.

Nachgeprüfte Aussagen der Simulationsaufgaben: sim1 (Kaffee, exponentiell: kleinste Abweichung etwa 2,0 °C bei Streuung
0,3 °C), sim2 (Koffein, beschränkt: S ≈ 0,1 mg).

## Aufgabenzahlen (nachgerechnet)

| Aufgabe | Ergebnis |
|---|---|
| a1 | 500·1,12⁶ ≈ 987 Zellen |
| a2 | B′(2) = 1,5·e ≈ 4,08 g/h |
| a4 | T = ln 2/0,035 ≈ 19,8 d (≈ 475 h) |
| a5 | t = ln 3/ln 1,12 ≈ 9,69 h (≈ 582 min) |

## Technische Notizen

- Formeln mit Euro-Zeichen: `€` in `data-tex` erzeugt KaTeX-Warnungen, stattdessen `\text{Euro}`.
- Legende im oberen Diagramm bei 30 % der Breite, damit sie bei fallenden Kurven den ersten Messpunkt nicht verdeckt.
- Die Formelleiste hat keine `einheit`-Felder (Mathematikmodul).

## Offen

- Kernlehrplan: Gehört logistisches Wachstum in die Q1 des LK? Ist ln als eigene Funktion samt Ableitung Q1-Stoff? Wird e
  über den Differenzenquotienten (hier) oder als Grenzwert von (1 + 1/n)ⁿ eingeführt? Keine Zitate erfunden, Stellen im
  Kernlehrplan sind zu klären.
- Die drei Datensätze sind konstruiert, keine Realmessungen. Das steht im Modultext.
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
