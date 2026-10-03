# Prüfbericht (fachlich): `module/mathe-q1-integral-rekonstruktion.html`

Mathematik · Leistungskurs Q1 · Inhaltsfeld: Funktionen und Analysis
Geprüft am 07.09.2026
Grundlagen: `inhalte/mathe-q1-integral-rekonstruktion.md`, `fachliches/kernlehrplan-nrw.md`,
`CLAUDE.md`, Referenzmodul `module/physik-q1-induktion.html`
Werkzeuge: unabhängige Neuimplementierung von Unter- und Obersumme in Python (exakte
Brucharithmetik), Playwright/Chromium gegen die ausgelieferte Datei (Regler gesetzt, alle Optionen
geklickt, Zahleneingaben an den Toleranzgrenzen getippt, Druckmedium emuliert, Canvas-Pixel gelesen).

---

## Urteil

**Nacharbeit nötig.**

Der Kern trägt: Die Simulation ist richtig gebaut — der Scheitel im Streifeninneren wird sauber
behandelt, das harte Prüfkriterium (b = 6,0 · n = 4 → U₄ = 21,825 · O₄ = 27,750 · Schere 5,925) ist
erfüllt, und alle nachgerechneten Zahlenwerte stimmen bis auf die letzte angezeigte Stelle. Der
Hauptsatz wird nirgends als Verfahren behauptet, keine Übungsaufgabe braucht eine Stammfunktion, der
Lehrplanbezug ist echt. Nachzuarbeiten sind zwei Stellen: ein zerstörtes `data-tex` in Zeile 230, das
im Browser sichtbar falsche Notation erzeugt, und ein fachlich falsch formulierter Satz in Zeile 425.
Beides sind Einzeiler; danach kann die Datei ohne Vorbehalt in den Unterricht.

---

## Schwere Fehler

### SF-1 · Zeile 230 — zerstörtes `data-tex`, sichtbar falsche Notation

Der Attributwert lautet `data-tex="v<TAB>ext{-}t"`: Zwischen `v` und `ext{-}t` steht ein **literales
Tabulatorzeichen**; aus `\text{-}` ist beim Schreiben der Datei `<TAB>ext{-}` geworden. Eine gezielte
Suche nach Steuerzeichen in `data-tex` und `data-plain` über die ganze Datei liefert genau diesen
einen Treffer; an den Vergleichsstellen (Zeile 253 `P\text{-}t`, Zeile 912 zweimal `v\text{-}t`)
steht es korrekt.

Wirkung, im Browser nachgestellt (Playwright, gerenderter Text der dritten Vorwissensfrage):

> „Was entspricht im **vext−t**-Diagramm dem zurückgelegten Weg?"

KaTeX läuft mit `throwOnError:false` und wirft deshalb keinen Konsolenfehler, sondern setzt e, x und
t als drei kursive Variablen. Der Fehler steht damit unbemerkt in der ersten Minute der Stunde. Ohne
KaTeX (Fallback über `data-plain`) erscheint korrekt „v-t-Diagramm" — er zeigt sich also **nur** im
Normalbetrieb.

**Korrektur:** `data-tex="v\text{-}t"`, wörtlich wie in Zeile 912.

### SF-2 · Zeile 425 — mathematisch falsche Aussage über Nullstellen

Wörtlich: „Ein Integral kann null sein, obwohl der Graph nirgends auf der Achse liegt — dann heben
sich Zufluss und Abfluss genau auf."

Gemeint ist offensichtlich „obwohl die Rate nicht durchgehend null ist". Wörtlich steht dort aber: Es
gebe Funktionen ohne jede Nullstelle mit Integral null. Für **stetige** Integranden ist das falsch —
und stetig sind sie in diesem Modul per Definition (Zeile 374: „Ist f auf [a;b] stetig …"). Wenn sich
Zufluss und Abfluss aufheben, wechselt f das Vorzeichen, und nach dem Zwischenwertsatz hat f dann
zwingend eine Nullstelle; der Graph liegt also sehr wohl irgendwo auf der Achse. Der Satz ist in sich
widersprüchlich und widerspricht zusätzlich der eigenen Argumentation des Moduls (Zeile 435,
Zeile 841: Zerlegung **an den Nullstellen** der Rate), auf der die Aufgaben a6 und a8 aufbauen. Im
Leistungskurs ist das genau die Sorte Satz, die in der mündlichen Prüfung zurückkommt.

Der Fehler stammt nicht vom Bauagenten: Er steht wortgleich in der abgenommenen Inhaltsdatei
(`inhalte/mathe-q1-integral-rekonstruktion.md`, Zeilen 510–511). Die Korrektur gehört an beide
Stellen.

**Korrekturvorschlag:** „Ein Integral kann null sein, obwohl die Rate nicht durchgehend null ist —
dann heben sich Zufluss und Abfluss über das Intervall genau auf. Weil die Rate dafür ihr Vorzeichen
wechseln muss, hat sie in diesem Fall mindestens eine Nullstelle im Inneren."

---

## Mängel

### M-1 · Zeile 330 — „nur für monotone f" ist zu weit gefasst

Die Formel `O_n − U_n = Δx · (f(b) − f(a))` steht mit dem Zusatz „(nur für monotone f)". Für monoton
**fallendes** f liefert die rechte Seite einen negativen Wert, während die linke Seite nie negativ
ist. Richtig ist entweder „nur für monoton wachsende f" oder `Δx · |f(b) − f(a)|`. Die Musterlösung
zu a7 (Zeile 782) hat es korrekt („bei monoton fallendem f … also mit |f(b) − f(a)|") — die
Merksatzformel im Erklärteil, die die Lernenden abschreiben, hat es nicht. Da a3 und a7 direkt auf
dieser Formel aufsetzen, sollte sie an der Quelle stimmen.

### M-2 · Zeile 1039 (Engine) mit Zeilen 997–1021 — Toleranz für die Alternativeinheit viel zu großzügig

Die Engine prüft die Alternativeinheit mit `Math.abs(v - d.alt.wert) <= d.alt.wert * 0.03`, also mit
3 % relativ, während der Hauptwert absolut mit `tol` geprüft wird. Weil die Alternativwerte hier die
Liter- und Wattstundenangaben und damit vierstellig sind, wird daraus ein sehr breites Fenster. Im
Browser nachgestellt:

| Eingabe | Fenster | Reaktion der Seite |
|---|---|---|
| 26 500 Wh (a1) | 24 977,5 … 26 522,5 | **Richtig.** … = 25,75 kWh |
| 25 000 Wh (a1) | dito | **Richtig.** … |
| 25,80 kWh (a1) | 25,70 … 25,80 (tol 0,05) | falsch: „Du bist in der richtigen Größenordnung …" |
| 10 500 L (a6) | 10 476 … 11 124 | **Richtig.** … Abgeflossen sind also 10,8 m³. |
| 18 500 L (a2o) | 18 430 … 19 570 | **Richtig.** … |

Eine um 2,9 % falsche Antwort wird also gelobt, eine um 0,2 % falsche verworfen — je nachdem, welche
Einheit gewählt wurde. Das ist keine Eigenheit dieses Moduls, sondern der aus
`module/physik-q1-induktion.html` unverändert übernommenen Zahlen-Engine (dort Zeile 675), die laut
`CLAUDE.md` nicht angetastet werden darf. Deshalb kein schwerer Fehler, aber ein Befund für die
Projektleitung: Entweder bekommt `alt` in der Engine dieselbe absolute Toleranz wie der Hauptwert,
mit dem Umrechnungsfaktor skaliert, oder die `alt`-Einträge entfallen und die Literangabe wird über
`falschEinheit` abgefangen. Die Haupttoleranzen selbst sind sauber gewählt: 0,05 bei a1, a2u, a2o und
a6 — dort fallen 19,0 statt 11,0 und 21,6 statt 10,8 verlässlich durch — sowie 0,5 bei a3, wo 319 und
321 abgelehnt werden (geprüft).

### M-3 · Zeilen 723 und 1020 — a6: die naheliegendste Fehleingabe bekommt die falsche Rückmeldung

Wer die Aufgabe rechnerisch vollständig richtig löst und den **vorzeichenbehafteten** Wert −10,8
einträgt (die Musterlösung selbst führt auf ∫ = −10,8 m³), erhält den `nah`-Text: „Prüfe, welche
beiden Zahlen du voneinander abziehst. 21,6 m³ ist der Zuwachs von 0 h bis 12 h …". Das unterstellt
einen Fehler, den die Schülerin nicht gemacht hat, und lenkt vom eigentlichen Punkt ab. Getestet und
bestätigt.

**Vorschlag:** In `numDaten.a6` den `nah`-Text um einen ersten Satz ergänzen, der den Vorzeichenfall
abräumt: Steht bei dir −10,8, dann hast du richtig gerechnet — gefragt ist aber die abgeflossene
Menge, also der Betrag. Andernfalls prüfe, welche beiden Zahlen du abziehst.

### M-4 · Zeile 596 — a2o verlangt zwei Dinge, nimmt aber nur eines entgegen

„Berechne … die Obersumme O₄ **und gib damit an, in welchem Bereich der tatsächliche Zufluss sicher
liegt**." Die Eingabe besteht aus einem Zahlenfeld und einer Einheitenliste; der zweite Auftrag kann
nicht abgegeben und nicht geprüft werden, er taucht erst in der Lösungswegstufe wieder auf. Entweder
den Zusatz als ausdrücklich schriftlichen Nebenauftrag kennzeichnen — notiere die Einschachtelung in
dein Heft — oder streichen.

### M-5 · Zeile 869 — Verweis auf „Aufgabe 4" ohne sichtbare Nummerierung

Der Abschlusstext duzt die Lernenden: „Du hast in Aufgabe 4 ausgerechnet, dass du 320 Streifen
brauchst." Die Übungen tragen auf der Seite aber keine Nummern; nummeriert wird erst im Export
(Zeilen 1516–1522) und im Lehrerteil. Die Zählung stimmt zwar — a3 ist der vierte Aufgabenblock —,
sie ist für die Lernenden aber nicht nachvollziehbar. Vorschlag: „bei der Aufgabe zur geforderten
Genauigkeit" statt der Nummer, oder die Aufgaben sichtbar nummerieren, was dann auch das
Referenzmodul beträfe.

### M-6 · Zeile 614 — a2o, Tipp nimmt den Ansatz vorweg

„Es sind dieselben vier Streifen wie eben. Nur die Seite, an der du ablesen musst, wechselt." Damit
ist die einzige Denkleistung der Aufgabe (rechter statt linker Randwert) schon auf Stufe 1 erledigt;
Stufe 2 fügt nur noch die Formel hinzu. Bei allen übrigen Aufgaben ist die Abstufung sauber — a1,
a2u, a3, a6 sowie a5, a7, a8 mit Tipp, Ansatz, Strukturhilfe und getrennter Musterlösung. Vorschlag
für Stufe 1: „Dieselben vier Streifen, dieselben fünf Funktionswerte — was ändert sich an der Frage?"

---

## Nachgerechnet

Alle Werte unabhängig in Python nachgerechnet (exakte Brüche); Spalte „Seite" ist der im Browser
abgelesene oder in der Datei stehende Wert.

### Simulation (Playwright, Werte aus `#anzU`, `#anzO`, `#anzSchere`, `#anzGrenz`, `#anzBestand`)

| Einstellung | Größe | mein Wert | Seite | Urteil |
|---|---|---|---|---|
| b = 6,0 · n = 4 | U₄ | 21,825 | 21,825 m³ | ✓ |
| b = 6,0 · n = 4 | O₄ | 27,750 | 27,750 m³ | ✓ **nicht 27,675 — Scheitel korrekt behandelt** |
| b = 6,0 · n = 4 | O₄ − U₄ | 5,925 | 5,925 m³ | ✓ |
| b = 6,0 · n = 4 | Δt | 1,5000 h | 1,5000 h | ✓ |
| b = 6,0 · n = 4 | Grenzwert I(6) | 25,2 | 25,200 m³ | ✓ |
| b = 6,0 · n = 4 | Bestand V(6) | 37,2 | 37,20 m³ | ✓ |
| b = 6,0 · n = 1 | U / O / Schere | 10,800 / 30,000 / 19,200 | identisch | ✓ |
| b = 6,0 · n = 2 | U / O / Schere | 18,000 / 29,400 / 11,400 | identisch | ✓ |
| b = 6,0 · n = 8 | Schere | 2,9906 | 2,991 m³ | ✓ |
| b = 6,0 · n = 12 | Schere | 2,0000 | 2,000 m³ | ✓ |
| b = 6,0 · n = 16 | Schere | 1,4988 | 1,499 m³ | ✓ |
| b = 6,0 · n = 32 | Schere | 0,7499 | 0,750 m³ | ✓ |
| Quotienten 2→4→8→16→32 | Halbierung | 1,9241 · 1,9812 · 1,9953 · 1,9988 | Z. 962 und 901: 1,924 · 1,981 · 1,995 · 1,999 | ✓ |
| b = 9,0 · n = 12 | U / O / I(9) / V | 29,166 / 35,306 / 32,400 / 44,40 | identisch | ✓ |
| b = 12,0 · n = 12 | U / O / I(12) / V | 13,200 / 29,200 / 21,600 / 33,60 | identisch | ✓ Einschachtelung 13,2 ≤ 21,6 ≤ 29,2 hält |
| b = 3,0 · n = 4 | Schere | 2,250 | 2,250 m³ | ✓ gleich Δt·(f(3) − f(0)), monotoner Fall |
| b = 1,0 · n = 1 | U / O / I(1) | 1,800 / 3,200 / 2,5333 | 1,800 / 3,200 / 2,533 | ✓ |

Quelltextprüfung der Simulation (Zeilen 1138–1153): `werte = [f(tl), f(tr)]`, ergänzt um
`f(T_SCHEITEL)` genau dann, wenn `tl < 4.0 && 4.0 < tr`; Minimum und Maximum werden **getrennt** aus
derselben Liste gezogen. Das ist die fachlich richtige Definition — Minimum und Maximum auf dem
ganzen Streifen, nicht die Randwertregel — und entspricht Punkt für Punkt dem Pseudocode der
Inhaltsdatei. Kein `Math.abs`, kein Abschneiden negativer Beiträge; bei b = 12 nachgeprüft.

Pixel-zu-Größen-Umrechnung von Hand nachgerechnet: `x(t) = 70 + 75·t` (t = 12 → 970, rechter Rand ✓),
`y(v) = 20 + 30·(6 − v)` (v = 6 → 20, v = −8 → 440, v = 0 → 200 ✓), `y2(v) = 20 + 3·(80 − v)`
(v = 0 → 260 ✓). Gegenprobe an den Canvas-Pixeln bei b = 6, n = 4: Das Obersummen-Rechteck des
**dritten** Streifens (x = 350) beginnt zwischen y = 45 (weiß) und y = 53 (bernstein), also bei
y = 50, das sind 5,00 m³/h; beim **vierten** Streifen (x = 460) erst zwischen y = 48 und y = 55, also
bei y ≈ 51,5, das sind 4,95 m³/h. Die Zeichnung bestätigt die Zahlen: Nur der Streifen mit dem
Scheitel im Inneren ragt auf 5,00. Unterhalb der Nulllinie (y = 205) ist bei b = 6 nichts gefüllt ✓.

### Erklär- und Vertiefungsteil

| Fundstelle | Größe | mein Wert | Seite | Urteil |
|---|---|---|---|---|
| Z. 253 | 11 kW · 1,5 h | 16,5 kWh | 16,5 kWh | ✓ |
| Z. 273–277 | Produktsumme Treppenrate | 4,0 + 3,5 + 9,0 + 2,5 = 19,0 m³ | 19,0 m³ | ✓ |
| Z. 285 | „mehr als ein Drittel daneben" | (19,0 − 12,5)/19,0 = 34,2 % | mehr als ein Drittel | ✓ |
| Z. 287 | mittlere Rate | 19,0/6 = 3,1667 | ≈ 3,17 m³/h | ✓ |
| Z. 322 | U₃ / O₃ für x² auf [0;3] | 5 / 14 | 5 / 14 | ✓ |
| Z. 324, 326 | Klammern, U₆ / O₆ | 13,75 / 22,75 → 6,875 / 11,375 | identisch | ✓ |
| Z. 332 | 27/n; U₁₀₀ / O₁₀₀ | 0,27; 8,86545 / 9,13545 | identisch | ✓ |
| Z. 359, 363 | geschlossene Form | 9 − 13,5/n + 4,5/n² und 9 + 13,5/n + 4,5/n² | identisch | ✓ Proben n = 3, 6, 100 stimmen |
| Z. 446, 448 | Scheitel, Nullstelle, Randwert | t_S = 4,0 · f(4) = 5,0 · t₀ = 9,0 · f(12) = −7,8 | identisch | ✓ |

### Übungen

| Aufgabe | Größe | mein Wert | Seite | Urteil |
|---|---|---|---|---|
| a1 | Wallbox gesamt | 16,50 + 7,40 + 1,85 = 25,75 kWh = 25 750 Wh | 25,75 kWh | ✓ |
| a1 Feedback | Distraktorweg | 22,1 kW · 1 h = 7,3667 kW · 3 h = 22,1 kWh | identisch | ✓ |
| a1 Feedback | mittlere Leistung | 25,75/3,0 = 8,583 kW | ≈ 8,58 kW | ✓ |
| a2u | U₄ für q(t) = 0,5 t² + 1 | 1·(1,0+1,5+3,0+5,5) = 11,0 m³ | 11,0 m³ | ✓ |
| a2o | O₄ | 1·(1,5+3,0+5,5+9,0) = 19,0 m³ | 19,0 m³ | ✓ |
| a2o | Schere über Teleskopformel | 8,0 = 1·(9,0 − 1,0) | 8,0 m³ | ✓ |
| a3 | kleinstes n | 32/n ≤ 0,10 → n = 320 | 320 | ✓ |
| a3 | Probe, Streifenbreite | 32/320 = 0,100 · 32/319 = 0,10031 · 4 h/320 = 45 s | identisch | ✓ |
| a4 | 12 L/min · 0,25 h | 12 · 15 min = 180 L; Distraktoren 3 und 720 richtig hergeleitet | 180 L | ✓ |
| z1 | Zuordnung | B kreuzt die Nulllinie bei x = 152, das entspricht t = 4,0 h | A, C, D, B | ✓ alle vier |
| a6 | Integral von 9 bis 12 | 21,6 − 32,4 = −10,8, abgeflossen 10,8 m³ | 10,8 m³ | ✓ |
| a6 | Bestände, bewegte Menge | 44,4 · 33,6 · 32,4 + 10,8 = 43,2 m³ | identisch | ✓ |
| a5 | U₂ / O₂ / Mittel / exakt | 1 / 5 / 3 / 2,6667, Abweichung 1/3 | identisch | ✓ |
| a5 | Mittelwerte n = 4, 8 | 2,750 (Abw. 0,0833) · 2,6875 (Abw. 0,0208) | 2,750 (0,083) · 2,6875 (0,021) | ✓ |
| a5 | halbe Schere n = 2 | 2 ≥ 1/3 | 2 | ✓ |
| a7 a) | Kontrolle monotoner Fall | O₄ − U₄ = 2,250 = 0,75 · 3,0 | identisch | ✓ |
| a7 b) | Formelwert gegen Wirklichkeit | 1,5 · (4,2 − 1,8) = 3,600 gegen 5,925 | identisch | ✓ |
| a7 b) | Gesamtschwankung als Schranke | 3,2 + 0,8 = 4,0; 6,000 ≥ 5,925 · 3,000 ≥ 2,991 · 1,500 ≥ 1,499 | identisch | ✓ |
| a8 | Bestand, Einschachtelung | 12 + 25,2 = 37,2; 33,825 bis 39,750 | identisch | ✓ |
| a8 | „knapp ein Drittel" | 12/37,2 = 32,3 % | knapp ein Drittel | ✓ |
| sim2 Feedback | Obersumme bei n = 1, M₁ | 5,00 · 6 = 30,000 m³; M₁ = 3,75 m³/h | identisch | ✓ |
| Lehrerteil Z. 901 | Messreihe | 11,400 · 5,925 · 2,991 · 1,499 · 0,750 | identisch | ✓ |
| Lehrerteil Z. 905 | I(3) / I(6) / I(9) / I(12) | 10,8 / 25,2 / 32,4 / 21,6 | identisch | ✓ |
| Lehrerteil Z. 905 | Differenzierung | aus 32/n ≤ ε folgt n ≥ 32/ε | n ≥ 32/ε | ✓ |
| Lehrerteil Z. 883–892 | Zeittabelle | 8+20+17+20+19+6 = 90 min | ca. 90 Minuten | ✓ |

**Kein einziger falscher Zahlenwert gefunden.** Auch die Lösungsschlüssel stimmen: Für vw1, vw2, vw3,
sim1, sim2 und a4 wurde jede Option einzeln angeklickt; nur der jeweils vorgesehene Index liefert die
Rückmeldung „richtig", alle übrigen die passende Fehlermeldung.

---

## Weitere geprüfte Punkte, die in Ordnung sind

- **Hauptsatz nicht vorweggenommen.** Nirgends steht die Regel Integral gleich F(b) minus F(a) oder
  ein gleichwertiges Verfahren. Die Erwähnungen (Z. 438, 520, 528, 869, 875, 877) benennen den
  Hauptsatz ausschließlich als noch nicht verfügbar. Z. 528 sagt es den Lernenden direkt („In dieser
  Einheit gibt es noch keine Stammfunktionen"), Z. 520 markiert das Feld „Grenzwert (exakt)"
  ausdrücklich als vorweggenommen, im Skript trägt `function exakt(b)` (Z. 1115–1116) den Kommentar
  „Vergleichswert, im Modul noch nicht herleitbar". Genau die verlangte Trennung.
- **Lösbarkeit ohne Stammfunktion**, Aufgabe für Aufgabe geprüft: a1 Produktsumme · a2u und a2o
  Summen über fünf gegebene Funktionswerte · a3 eine Ungleichung aus der Teleskopformel · a4
  Einheitenumrechnung · z1 qualitativ · a6 Intervalladditivität mit zwei **abgelesenen** Werten ·
  a5 zwei Summen, der exakte Wert 8/3 ist in der Aufgabenstellung **vorgegeben** · a7 Teleskopsumme
  und Simulationswerte · a8 reine Interpretation. Keine Aufgabe verlangt eine Integration.
- **Lehrplanbezug.** „Funktionen und Analysis" steht wörtlich so in `fachliches/kernlehrplan-nrw.md`
  (Zeile 38); die Zuordnung zur Q1 („Fortführung der Analysis … Integralrechnung bis zum Hauptsatz",
  Zeilen 42–44) trägt das Thema. Kein erfundenes Zitat, keine erfundene Kompetenzformulierung.
  Zeile 878 markiert die Feingliederung „Rekonstruktion vor Integralbegriff" ausdrücklich als
  Unterrichtsentscheidung und nicht als Vorgabe — genau das, was `CLAUDE.md` bei unklarer Zuordnung
  verlangt. Die Kompetenzbereiche gehen über das Rechnen hinaus: Modellieren (Rate und Bestand im
  Sachkontext), Argumentieren (drei Aufgaben im Anforderungsbereich III), Werkzeuge nutzen (die
  Simulation als Erkenntnisinstrument), Kommunizieren (Stellungnahmen zu Schüleraussagen).
- **Anforderungsbereiche**, unabhängig zugeordnet: a1, a2u, a2o = I ✓ · a3, a4, z1, a6, sim1, sim2 =
  II ✓ · a5, a7, a8 = III ✓. Die drei AB-III-Aufgaben sind echte Beurteilungs- und
  Begründungsaufgaben — eine Schüleraussage widerlegen, den Gültigkeitsbereich einer Formel
  begründen, Zuwachs gegen Bestand abgrenzen —, keine längeren Rechnungen, und jede hat Musterlösung
  **und** Bewertungskriterien. Keine Aufgabe ist zu hoch ausgezeichnet; der sonst häufigste Befund
  liegt hier nicht vor. Das LK-Niveau ist erreicht: Summenformel für die Quadratzahlen, geschlossene
  Form von U_n und O_n, Beschränktheit der Gesamtschwankung, Epsilon-Verallgemeinerung in der
  Differenzierung.
- **Distraktoren.** Alle 21 falschen MC-Optionen haben ein Feedback, das den Denkfehler benennt und
  meist mit einer Gegenrechnung widerlegt (sim2, Option 2: „Dann wäre die Obersumme 30,000 m³ — das
  ist der Wert für n = 1"). Kein bloßes „Leider falsch".
- **Beobachtungsauftrag** (Z. 452–457) ist mit der Simulation beantwortbar: n = 2 ist einstellbar,
  „n verdoppeln" führt bis 32 (getestet, Deckel bei 40), die Quotienten ergeben 1,92 · 1,98 · 2,00 ·
  2,00; der zweite Teil zum dritten Streifen (3,0 bis 4,5 h) ist an Anzeige und Zeichnung ablesbar.
- **Sprache.** Durchgehend geduzt, kein „Sie" in Anredefunktion; durchgehend Deutsch einschließlich
  der Codekommentare; Komma als Dezimaltrennzeichen in allen angezeigten Zahlen (`fmt()` mit
  `replace(".", ",")`, auch in den statischen Startwerten); Fachbegriffe einheitlich: Untersumme,
  Obersumme, Schere, Produktsumme, orientierter Flächeninhalt, Intervalladditivität.
- **Technik, soweit sie fachlich wirkt:** keine Konsolenfehler und keine Warnungen; alle 324
  `.m`-Elemente haben `data-plain`; im Druckmedium sind Regler, Hilfeknöpfe, Knopfleisten und der
  Lehrerteil ausgeblendet, alle 15 Aufgabenblöcke bleiben sichtbar; der CSS-Block ist gegenüber
  `module/physik-q1-induktion.html` bis auf die vier Farbzeilen (`--akzent`, `--akzent-hell`,
  `--akzent-rand`, Kopfverlauf) zeichengleich.
- **Abweichungen von der Inhaltsdatei:** keine inhaltlichen. Reihenfolge der Aufgaben, Schlüssel,
  `numDaten`-Einträge, Reglergrenzen, Zeichenreihenfolge und Farbwerte entsprechen der Vorgabe; das
  Abnahmekriterium aus Abschnitt 4.4 (27,750 statt 27,675) ist erfüllt, der zweite Testfall aus 4.5
  (b = 12, n = 12 mit 13,200 / 29,200 / 21,600) ebenfalls.

---

## Gut gelöst

- **Die Simulation ist der didaktische Kern und nicht Dekoration.** Der Scheitel liegt bei b = 6 und
  n = 4 mitten im dritten Streifen — die Startkonfiguration ist so gewählt, dass die falsche Regel
  „links ist das Minimum, rechts das Maximum" sofort auffliegt. Hinweiskasten (Z. 312), zweite
  MC-Frage (Z. 507–517), Beobachtungsauftrag und Lehrerhinweis (Z. 898) ziehen alle an derselben
  Stelle. Übernahmewürdig für jedes weitere Modul mit Simulation.
- **Der bernsteinfarbene Saum.** Obersummen-Rechtecke hinten, Untersummen-Rechtecke darüber: Die
  Schere ist als sichtbarer Rand am Bild ablesbar und schrumpft beim Verdoppeln vor den Augen.
  Zusammen mit Zahlenfeld und Balken entsteht die Verbindung von Zahl und Bild ohne Erklärtext.
- **Der Verzicht auf den Hauptsatz wird ausgesprochen statt verschwiegen.** Z. 528 und der
  Hinweiskasten „Was die Simulation nicht beweist" (Z. 519–521) machen die Beschränkung zum Thema.
  Das nimmt der Simulation genau die Beweiskraft, die sie nicht hat, und bereitet das Folgemodul vor.
- **Aufgabe a8** trennt sauber Rate, Zuwachs und Bestand und lässt eine zweite Schülerin einen
  halbrichtigen Einwand vortragen („25,2 ist bloß geraten"). Die erwartete Antwort muss zwischen
  „nicht widerlegt" und „bewiesen" unterscheiden — Wissenschaftspropädeutik im besten Sinn und im
  Leistungskurs richtig platziert.
- **Der Lehrerteil** ist kein Allgemeinplatz: sieben typische Fehler, jeder mit konkreter
  Anhaltestelle, Frage an den Kurs und zugehöriger Zahl (12,5 statt 19,0; 25,2 statt 37,2; 4,95 statt
  5,00). Die Zeittabelle summiert sich auf und benennt ehrlich, was in 90 Minuten nicht hineinpasst.
  Der Experimentbezug — Stromzähler, Eimer mit Stoppuhr, Pegelstände samt Aufbereitungszeit — ist am
  selben Nachmittag umsetzbar.
- **Die Feedbacktexte der Zahleneingaben** unterscheiden zwischen „richtige Größenordnung, falscher
  Ansatz" und „weit daneben" und benennen im ersten Fall den konkreten Fehlweg mitsamt Zahl:
  22,1 kWh bei a1, 19,0 statt 11,0 bei a2u. Das ist mehr, als die Vorgabe verlangt.

---

## Fazit

Das Modul ist fachlich solide gearbeitet: Ich habe jede Zahl unabhängig nachgerechnet und keine
einzige falsche gefunden, und die Simulation besteht das harte Prüfkriterium mit U₄ = 21,825 und
O₄ = 27,750 — der Scheitel im Streifeninneren ist im Code wie in der Zeichnung korrekt behandelt, und
die Schere halbiert sich bei jeder Verdopplung von n. Der Hauptsatz wird konsequent ausgespart, keine
Übungsaufgabe lässt sich nur mit einer Stammfunktion lösen, und der Lehrplanbezug ist echt und an der
einen unklaren Stelle ausdrücklich als Unterrichtsentscheidung markiert. Zwei Stellen müssen vor dem
Einsatz korrigiert werden: das durch ein Tabulatorzeichen zerstörte `data-tex` in Zeile 230, das im
Browser sichtbar „vext−t" erzeugt, und der wörtlich falsche Satz über Nullstellen in Zeile 425, der
auch in der abgenommenen Inhaltsdatei steht. Beide Korrekturen sind Einzeiler, und die sechs Mängel
lassen sich in einer halben Stunde abarbeiten. Mit diesen Änderungen — und möglichst auch mit der
geschärften Monotoniebedingung in Zeile 330 — kann das Modul in die Doppelstunde gehen.


---

## Gegenprüfung nach der Nacharbeit

Geprüft am 07.09.2026 gegen `module/mathe-q1-integral-rekonstruktion.html` (1575 Zeilen, Stand Commit `2e8b2b7`).
Grundlage: Diff `b0717de..HEAD`, Playwright/Chromium gegen die ausgelieferte Datei, Nachrechnung der
Engine-Arithmetik in IEEE754 (Python-Doubles = JS-Doubles). Keine Vollprüfung — nur die Befunde des
obigen Berichts plus gezielte Regressionssuche.

### Befund für Befund

| Befund | Status | Fundstelle · Begründung |
|---|---|---|
| **SF-1** Tabulator in `data-tex` | **behoben** | Z. 230 lautet jetzt `data-tex="v\text{-}t"`. Im Browser gerendert: „Was entspricht im *v-t*-Diagramm dem zurückgelegten Weg?" Gegenprobe über alle vier Module: null Tabulatorzeichen (`grep -c $'\t'` = 0 je Datei), null Steuerzeichen in irgendeinem `data-tex`/`data-plain`. Export schreibt korrekt „Vorwissen 3 – Weg im v-t-Diagramm". |
| **SF-2** Aussage über Nullstellen | **behoben, fachlich sauber** | Z. 425. Die neue Fassung ist beweisbar richtig: Ist f auf [a;b] stetig (Z. 374 setzt das voraus), ∫f = 0 und f nicht identisch null, so muss f beide Vorzeichen annehmen — sonst wäre f ≥ 0 mit Integral null, also f ≡ 0 —, und der Zwischenwertsatz liefert eine Nullstelle **echt zwischen** den beiden Stellen, also im Inneren. Auch der Zusatz „im Inneren" hält, selbst wenn die Vorzeichenstellen die Randpunkte a und b sind. Passt zur Argumentation der Aufgaben: der Hinweiskasten Z. 426 („an den Nullstellen der Rate zerlegen"), a6 mit der Nullstelle t = 9,0 h der Simulationsrate (−0,2t² + 1,6t + 1,8 = 0 ⇒ t = 9 oder t = −1, nachgerechnet) und a8 stehen jetzt widerspruchsfrei zum Erklärtext. |
| **M-1** Merksatzformel mit Betrag | **behoben, an allen zitierenden Stellen mitgezogen** | Z. 330 `Δx·\|f(b) − f(a)\|` (KaTeX-Rendering per Screenshot bestätigt), Z. 332 begründet den Betrag zusätzlich richtig („bei monoton *fallendem* f negativ … die Schere dagegen nie"), Z. 769 zitiert die Formel in a7 jetzt mit Betragsstrichen. Vollständige Nachsuche nach `f(b)`/`f(a)`: keine weitere Zitierstelle. Z. 782 (Musterlösung a7 a) leitet für wachsendes f ohne Betrag her und ergänzt „bei monoton fallendem f … also mit \|f(b) − f(a)\|" — das ergänzt die Formel jetzt, statt ihr zu widersprechen. Nachgerechnet: bei fallendem f teleskopiert M_k − m_k = f(x_{k−1}) − f(x_k) zu f(a) − f(b) = \|f(b) − f(a)\| ✓. |
| **M-2** Toleranz der Alternativeinheit | **behoben** | Z. 1038–1046. Im Browser nachgestellt: 26 500 Wh, 25 000 Wh (a1), 10 500 L (a6), 18 500 L (a2o) — alle vier vormals fälschlich gelobten Eingaben werden jetzt **abgelehnt**. Umgekehrt ist der Grenzfall repariert: 25,80 kWh gilt jetzt als richtig (vorher abgelehnt, weil 25,80 − 25,75 binär 0,050000000000000710 ergibt), genau wie 25 800 Wh. |
| **M-3** a6, Rückmeldung bei −10,8 | **behoben** | Z. 1020. Eingabe −10,8 mit m³ ausgelöst: Der Text beginnt jetzt mit „Steht bei dir −10,8, dann hast du richtig gerechnet …" und leitet erst danach zum eigentlichen Fehlweg über. Der `nah`-Zweig greift zuverlässig, weil faktor = \|−10,8/10,8\| = 1 im Fenster (0,5; 2) liegt. |
| **M-4** a2o, zwei Aufträge | **behoben** | Z. 596: „Geprüft wird hier nur dieser Wert." plus ausgewiesener **Schriftlicher Nebenauftrag**. Prüfbarkeit und Auftrag sind jetzt getrennt benannt. |
| **M-5** Verweis auf „Aufgabe 4" | **behoben (Schülertext)** | Z. 869 lautet jetzt „bei der Aufgabe zur geforderten Genauigkeit". |
| **M-6** a2o, Tipp verrät den Ansatz | **behoben** | Z. 614 wortgleich mit dem Vorschlag: „Dieselben vier Streifen, dieselben fünf Funktionswerte — was ändert sich an der Frage?" Die Denkleistung bleibt bei der Schülerin, Stufe 2 liefert erst die Formel. |

### Neu entstanden bzw. nach der Korrektur übrig

- **N-1 · Z. 1050 (Engine) — die `nah`/`weit`-Weiche kennt die Alternativeinheit nicht.** *neu sichtbar geworden.*
  `faktor = Math.abs(v / d.wert)` misst immer am **Hauptwert**. Wer in der Alternativeinheit antwortet und
  knapp danebenliegt, bekommt deshalb faktor ≈ 1000 und damit den „weit daneben"-Text. Belegt im Browser:
  25 801 Wh (0,2 % daneben) → „Rechne zuerst eine einzige Phase …"; 11 100 L (0,9 %) → „Schreib dir zuerst
  die fünf Werte auf"; 18 500 L und 10 500 L ebenso. Sachlich ist die Ablehnung richtig, die *Begründung*
  ist es nicht. Das Verhalten gab es vorher auch, es traf durch das 3-%-Fenster nur seltener zu; durch die
  jetzt korrekt verengte Annahme ist es der Normalfall. Ein Zweizeiler in der gemeinsamen Engine räumt es
  ab: `var bezug = (d.alt && e === d.alt.einheit) ? d.alt.wert : d.wert;` und dann `faktor = Math.abs(v / bezug)`.
  Kein Blocker für den Unterricht, aber der letzte verbliebene didaktische Bruch der Zahlenaufgaben.
- **N-2 · Z. 905 (Lehrerteil) — „Aufgabe 4 allgemein lösen".** *teilweise behoben.* Der Schülertext ist
  bereinigt, die Differenzierungsnotiz nennt weiterhin eine Nummer. Für die Lehrkraft über die Exportliste
  auflösbar (Z. 1528: „Aufgabe 4 – benötigte Streifenzahl"), also vertretbar; sauber wäre „Aufgabe zur
  geforderten Streifenzahl".
- **N-3 · Z. 596 — letzter Satz des Nebenauftrags.** „Die Lösungswegstufe zeigt sie dir anschließend"
  nimmt dem Nebenauftrag einen Teil seiner Verbindlichkeit. Streichen genügt; die Lösungswegstufe zeigt
  die Einschachtelung ohnehin.
- **N-4 · `inhalte/mathe-q1-integral-rekonstruktion.md`, Z. 510.** Die Inhaltsdatei wurde ebenfalls
  korrigiert, aber mit anderer Formulierung: „obwohl die Rate **nirgends dauerhaft null** ist". Als
  Existenzaussage ist das nicht falsch (f(x) = x auf [−1;1]), es ist aber die schwächere Bedingung; die
  ausgelieferte HTML-Fassung („nicht durchgehend null") ist die bessere. Nur ein Hinweis: die Inhaltsdatei
  nennt zusätzlich den **Zwischenwertsatz** beim Namen, die HTML-Fassung nicht. Im Leistungskurs wäre die
  Nennung ein Gewinn — das ist genau das Argument, das die Aussage trägt.
- Randnotiz ohne Befundcharakter: Wer im Zahlenfeld die deutsche Tausenderschreibweise „25.750" tippt,
  wird als 25,75 gelesen und bekommt den `falschEinheit`-Text („Der Zahlenwert stimmt …"). Eigenheit von
  `input[type=number]`, unverändert gegenüber dem Referenzmodul, führt inhaltlich nicht in die Irre.
  Ein getipptes Leerzeichen („25 750") entfernt Chromium selbst, die Eingabe wird als richtig gewertet.

### Antwort auf die Regressionsfrage: braucht a1 eine eigene `alt.tol`?

**Nein — und eine eigene `alt.tol` wäre hier ein Rückschritt.** Begründung in vier Punkten:

1. **Die umgerechnete Toleranz ist exakt, nicht bloß ungefähr.** `Math.abs(d.tol * d.alt.wert / d.wert)`
   ergibt in IEEE754 für alle vier Aufgaben mit `alt` **genau 50,0** — nachgerechnet, kein Rundungsrest.
   Die relative Toleranz ist damit in beiden Einheiten identisch (a1 0,194 %, a2u 0,455 %, a2o 0,263 %,
   a6 0,463 %). Genau diese Gleichbehandlung war der Kern von M-2: Dieselbe Antwort muss dieselbe
   Bewertung bekommen, egal in welcher Einheit sie steht.
2. **Alle Sollwerte sind exakt, es ist nichts zu runden.** 25 750 Wh entsteht aus 16 500 + 7 400 + 1 850,
   11 000 L aus 1 h · (1000 + 1500 + 3000 + 5500) L/h, 10 800 L aus 32 400 − 21 600. Kein
   Zwischenschritt zwingt zu einer Rundung, deren Fehler die Toleranz auffangen müsste. Die 50 Wh sind
   reiner Puffer, kein Rechenspielraum, den jemand braucht.
3. **Der einzige realistische Rundungsweg liegt innerhalb des Fensters.** Wer auf drei geltende Ziffern
   rundet (25,8 kWh), landet bei 25 800 Wh — genau auf der Grenze, und dank `eps` angenommen; im
   Browser bestätigt. Wer auf zwei rundet (26 kWh → 26 000 Wh), wird abgelehnt — in der Haupteinheit
   aber ebenso. Die Strenge ist also nicht *in Wattstunden* streng, sie ist überall gleich streng.
4. **Wann eine eigene `alt.tol` berechtigt wäre:** nur dann, wenn die Alternativangabe eine sachlich
   gröbere Skala ist (Antwort „in vollen Minuten", „auf 100 L genau"), nicht bei reiner
   Einheitenumrechnung. Das ist hier bei keiner der fünf Zahleneingaben der Fall. Ich empfehle
   ausdrücklich, **keine** `alt.tol` einzutragen — und wenn doch je eine gebraucht wird, sie im
   Kommentar an dieses Kriterium zu binden, damit die 3-%-Willkür nicht durch die Hintertür zurückkommt.

Das `eps = 1e-9` ist unbedenklich: Es weitet die Toleranz um 5·10⁻¹¹ Einheiten und wirkt ausschließlich
auf den Fließkomma-Grenzfall.

### Nachgerechnet (Gegenprüfung)

| Prüfpunkt | mein Wert | Seite/Engine | Urteil |
|---|---|---|---|
| `altTol` a1 = \|0,05 · 25750 / 25,75\| | 50,0 (exakt in IEEE754) | 50,0 | ✓ |
| `altTol` a2u / a2o / a6 | 50,0 · 50,0 · 50,0 | identisch | ✓ |
| relative Toleranz Haupt- vs. Alt-Einheit | 0,194 % / 0,455 % / 0,263 % / 0,463 % | in beiden Einheiten gleich (1 ulp) | ✓ |
| a1: 25,75 · 25,70 · 25,80 kWh | alle drei innerhalb tol | alle drei „richtig" | ✓ |
| a1: 25,81 kWh | außerhalb | „nah"-Text | ✓ |
| a1: 25 750 · 25 800 Wh | innerhalb | „richtig" | ✓ |
| a1: 25 801 · 26 500 · 25 000 Wh | außerhalb | abgelehnt (Text: siehe N-1) | ✓ Ablehnung, ✗ Textwahl |
| a2u: 11 000 · 11 050 L · 11,0 m³ | innerhalb | „richtig" | ✓ |
| a2u: 11 100 L · 19,0 m³ | außerhalb | abgelehnt, 19,0 m³ mit passendem „nah"-Text | ✓ |
| a2o: 19 000 · 19 050 L | innerhalb | „richtig" | ✓ |
| a3 (ohne `alt`): 320 · 319 · 321 | 320 richtig, 319/321 falsch | identisch, kein TypeError trotz fehlendem `d.alt` | ✓ |
| a6: 10,8 m³ · 10 800 L · 10 850 L | innerhalb | „richtig" | ✓ |
| a6: −10,8 m³ · 10 500 L · 21,6 m³ | außerhalb | abgelehnt, −10,8 mit neuem Vorzeichentext | ✓ |
| Simulation Start (n = 4, b = 6) | Δt 1,5000 h · U 21,825 · O 27,750 · Schere 5,925 · I 25,200 · V 37,20 | identisch | ✓ unverändert |
| Simulation n = 1 / 2 / 32 bei b = 6 | Schere 19,200 / 11,400 / 0,750 | identisch | ✓ |
| Simulation b = 9 (n = 12) und b = 12 (n = 12) | 29,166 / 35,306 / 32,400 / 44,40 und 13,200 / 29,200 / 21,600 / 33,60 | identisch | ✓ |
| a7 b) mit neuer Formel: Δt·\|f(6) − f(0)\| | 1,5 · \|4,2 − 1,8\| = 3,600 | 3,600 | ✓ Betrag ändert den Zahlenwert nicht |

### Regressionssuche

- **CSS `.tabelle table{min-width:min(420px,100%)}`** (Z. 156, in allen vier Modulen einschließlich des
  Referenzmoduls einheitlich): bei 1280, 900 und 390 px ist `scrollWidth === clientWidth`, also kein
  Querscrollen der Seite. Bei 390 px schrumpfen die zwei schmalen Tabellen auf 350 bzw. 308 px, **ohne
  dass eine einzige Zelle überläuft** (`scrollWidth > clientWidth` für kein `td`/`th`); per Screenshot
  gegengelesen: lesbar, nur „2,0 m³/h" bricht auf zwei Zeilen. Die zwei breiten Tabellen scrollen
  weiterhin innerhalb ihres `.tabelle`-Kastens (414 px in 350 px, 360 px in 316 px). Keine Regression,
  die alte Zwangsbreite ist nur dort weg, wo sie schadete.
- **Druckansicht:** Regler `#regN`/`#regB`, Lehrerteil und sämtliche `.knopfleiste` unsichtbar, alle 15
  Aufgabenkästen sichtbar — unverändert gegenüber der Erstprüfung.
- **Export:** läuft, deutsche Datums- und Statusausgabe, a2o wird als „Aufgabe 3 – Obersumme O₄: richtig",
  a6 als „Aufgabe 7 – Vorzeichenwechsel: noch nicht richtig" geführt.
- **Konsole:** kein `error`, keine `warning`, kein `pageerror` über alle 27 Engine-Eingaben, alle
  Reglerstellungen, Druckemulation und Export hinweg.
- **KaTeX:** die geänderten Formeln (Merksatz Z. 330, a7-Aufgabenstellung Z. 769) rendern korrekt mit
  Betragsstrichen; die `data-plain`-Fallbacks wurden mitgezogen (`O_n − U_n = Δx · |f(b) − f(a)|`).

### Gesamturteil

**Bestanden** — beide schweren Fehler sind sauber und fachlich richtig behoben, alle sechs Mängel sind
abgearbeitet, die verschärfte Zahlen-Engine rechnet exakt und hat weder Layout noch Simulation noch Druck
beschädigt; offen bleibt allein die kosmetische Textwahl der `nah`/`weit`-Weiche bei Antworten in der
Alternativeinheit (N-1), die den Unterrichtseinsatz nicht aufhält.