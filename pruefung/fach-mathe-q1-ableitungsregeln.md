# Fachprüfung: module/mathe-q1-ableitungsregeln.html

## Urteil: **Nacharbeit nötig** (keine Blocker, 12 Mängel – davon 3 mit Wirkung auf die Lernenden)

Fachlich fehlerfrei; die Nacharbeit betrifft einen nicht ausführbaren Reglerschritt im
Beobachtungsauftrag, eine falsch gerundete Zahl in einer richtigen Antwortoption und die
Anzeige des Umsatzmaximums. Details unter „Mängel".

Prüfdatum: 18.09.2026 · Prüfgegenstand: `module/mathe-q1-ableitungsregeln.html`
Inhaltsquelle: `inhalte/mathe-q1-ableitungsregeln.md` · Regelwerk: `Schule/CLAUDE.md`,
`fachliches/kernlehrplan-nrw.md`

Alle Zahlenwerte wurden mit sympy/python unabhängig nachgerechnet. Der Bericht wurde
abschnittsweise fortgeschrieben.

---

## Nachgerechnet – Abschnitte 1 bis 3 (Einstieg, Erklärteil, Vertiefung)

| Fundstelle | Behauptung in der Datei | Nachrechnung | Urteil |
|---|---|---|---|
| Z. 212-214 (vw1) | f(x)=3x⁴−5x²+2x−9 → f′=12x³−10x+2 (Option 1) | 12x³−10x+2 | richtig |
| Z. 222-224 (vw2) | (1/x³)′ = −3/x⁴ (Option 0) | −3x⁻⁴ | richtig |
| Z. 285-286 | (x³−2x)(4x+5) → 16x³+15x²−16x−10; f′(1)=5; f′(2)=146 | identisch | richtig |
| Z. 286 | ausmultipliziert 4x⁴+5x³−8x²−10x | identisch | richtig |
| Z. 295 | U′(0)=0,10·400+5,00·(−6)=40−30=10 | 10 | richtig |
| Z. 331 | (2x−1)³ → 6(2x−1)²; Ausmult. 8x³−12x²+6x−1; f′(2)=54 | identisch | richtig |
| Z. 333-334 | (√(x²+1))′ = x/√(x²+1); f′(2)=2/√5≈0,8944 | 0,894427… | richtig |
| Z. 382-383 | ((x²+1)/(x−2))′ = (x²−4x−1)/(x−2)²; f′(3)=−4; f′(0)=−0,25 | identisch | richtig |
| Z. 402-404 | (x²√(2x+1))′ = x(5x+2)/√(2x+1); f(4)=48; f′(4)=88/3≈29,33 | identisch | richtig |
| Z. 404 | Tangente in x=4: y=(88/3)x−208/3 | 88/3·4−208/3 = 48 ✓ | richtig |
| Z. 408-409 | ((3x²+1)^{3/2})′ = 9x√(3x²+1); f(1)=8; f′(1)=18; f′(0)=0; f′(2)=18√13≈64,90 | 64,8998… | richtig |

## Nachgerechnet – Abschnitt 4 (Simulationen)

Die im Quelltext verwendeten Beziehungen wurden aus dem Skript abgeleitet und mit der Fachtheorie
verglichen; alle Anzeigewerte wurden unabhängig nachgerechnet.

**Simulation 1 – Umsatzrechteck.** Reglerumrechnung: `dt = rDt·0,25` (0,25 … 4,00 Tage),
`b = rB/100` (−0,15 … 0,30 €/Tag), `d = rD` (−12 … 8), `t = rT/10` (0 … 21 Tage).
Modell `p(t)=5+bt`, `n(t)=400+dt`, `U=p·n`, `U′=b·n+p·d`, `sek=(U(t+Δt)−U(t))/Δt`,
`eck=b·d·Δt` (Z. 1182-1193). Das entspricht exakt der Theorie; die Legende
`p·Δn + n·Δp + Δp·Δn = ΔU` ist eine algebraische Identität und wurde für zwei Zustände geprüft.

| Fundstelle | Anzeige laut Datei | Nachrechnung | Urteil |
|---|---|---|---|
| Z. 459-467 (Startzustand t=0, Δt=1) | p=5,00 €; n=400,0; U=2000,00 €; p′n=40,00; pn′=−30,00; U′=10,00; Sekante 9,40; Eck −0,60 | identisch (U(1)−U(0)=9,4; b·d·Δt=−0,6) | richtig |
| Z. 916-921 (Lehrer-Erwartungstabelle) | Sekante 7,60/8,80/9,40/9,70/9,85, Eck −2,40/−1,20/−0,60/−0,30/−0,15 | identisch für Δt=4/2/1/0,5/0,25 | richtig |
| Z. 1185 `tStern()` | t* = −(b·N₀+P₀·d)/(2bd) | Scheitel von U(t)=P₀N₀+(bN₀+P₀d)t+bd·t² – korrekt | richtig |
| Z. 512/994 | t*≈8,3 Tage, Beiträge +35,00 / −35,00 €/Tag | t*=25/3=8,333…; 0,1·350=35, (35/6)·(−6)=−35 | rechnerisch richtig, Anzeige siehe Mangel M1 |
| Z. 1232 Bereichsprüfung | Knopf reagiert nur für 0 ≤ t* ≤ 21 | vollständiger Reglerscan (46×21 Kombinationen): kein Fall, in dem t* ein **Minimum** ist und im Bereich liegt (t*=200/\|d\|+2,5/\|b\| ≥ 33,3 Tage) | robust, gut |

**Simulation 2 – Ölring.** `r=r₀+c·t`, `A=πr²`, `dA/dr=2πr`, `dA/dt=2πr·c`,
`ex=π((r+Δr)²−r²)`, `na=2πr·Δr`, `fe=π·Δr²`, `rel=fe/ex` (Z. 1416-1420). Fachlich korrekt,
`ex = na + fe` ist eine Identität.

| Fundstelle | Anzeige laut Datei | Nachrechnung | Urteil |
|---|---|---|---|
| Z. 549-556 (Start r₀=5, c=0,5, t=20, Δt=1) | r=15,000; A=706,858; 2πr=94,2478; dA/dt=47,1239; Ring exakt 47,90929; genähert 47,12389; Differenz 0,78540 (1,639 %) | identisch | richtig |
| Z. 923 (Lehrerteil, t=40 s) | r=25 m; A=1963,50 m² (2,78-fach); dA/dt=78,5398 (25/15-fach) | 625/225=2,7778; 78,5398/47,1239=1,6667 | richtig |
| Z. 923 Fehlerreihe | 3,14159 / 0,78540 / 0,19635 / 0,04909 m²; relativ 3,226 / 1,639 / 0,826 / 0,415 % | identisch | richtig |
| Z. 588 (Antwortoption sim3) | relativ „3,23 % → 1,64 % → 0,83 % → **0,42 %**" | 0,415 % → gerundet 0,41 % | siehe Mangel M2 |

## Nachgerechnet – Abschnitt 5 (Übungen) und Abschnitt 6

| Fundstelle | Behauptung in der Datei | Nachrechnung | Urteil |
|---|---|---|---|
| Z. 627 / 1028 (Aufg. 1) | A′(0)=3·25+40·2=155 m²/Jahr; A(t)=6t²+155t+1000; A(1)−A(0)=161 | identisch | richtig |
| Z. 652 / 1033 (Aufg. 2) | dV/dt(4)=4π·16·0,5=32π≈100,53 cm³/s; V(4)=256π/3≈268,08 | 100,53096; 268,0826; Verhältnis 0,375 („gut ein Drittel") | richtig |
| Z. 1037 (Feedback) | 201,06 = 64π (fehlende innere Ableitung); 25,13 mit r=2 | 201,0619; 8π=25,1327 | richtig |
| Z. 660/1005 (Aufg. 3, mc1) | f′(x)=8(2x−3)³, Option 1 richtig | identisch | richtig |
| Z. 689 / 1038 (Aufg. 4) | c′(t)=(80−20t²)/(t²+4)²; c′(1)=60/25=2,4; Max bei t=2 mit c(2)=5 | identisch | richtig |
| Z. 1042 (Feedback) | 10 aus u′/v′=20/(2t); 12 bei nicht quadriertem Nenner | 20/2=10; 60/5=12 | richtig |
| Z. 714 / 1043 (Aufg. 5) | V′(5)=π(28−8)=20π≈62,83 cm³/s; V(5)=280π≈879,65 | 62,8319; 879,6459 | richtig |
| Z. 1046/1047 (Feedback) | 87,96=28π; 414,69 bei (r²)′=2r; −25,13 nur zweiter Summand | 87,9646; 132π=414,690; −8π=−25,1327 | richtig |
| Z. 722-736 (Zuordnung) | x³/(2x+1)→D, (2x+1)³→C, (2x+1)/x³→B, x³(2x+1)→A | alle vier bestätigt (u. a. (2x+1)/x³ → −(4x+3)/x⁴) | richtig |
| Z. 764 / 1048 (Aufg. 7) | U′(t)=40−2t; t*=20 Tage; U″=−2; U(20)=1600 €; U(t)=−t²+40t+1200 | identisch | richtig |
| Z. 1052 (Feedback) | „U′ ohne t, etwa die Konstante 80" bei falschem Vorzeichen von n′ | 0,2(300−5t)+(4+0,2t)·(+5)=80 | richtig und treffend |
| Z. 781 (Aufg. 8, AB III) | u=t, v=t−10: (uv)′(1)=1·(−9)+1·1=−8; uv=t²−10t, Scheitel t=5 | identisch | richtig |
| Z. 782 | U′(12)=−4,40 €/Tag | 10−1,2·12=−4,4 | richtig |
| Z. 838 (Kernaussage 1) | „Vorzeichen und Faktor 17": +10,00 gegen −0,60 | 10/0,6 = 16,67 | siehe Mangel M6 |

**Toleranzen der Zahleneingaben** (Z. 1028-1052): a1 155 ± 0,5 · a2 100,53 ± 0,15 (32π = 100,5310)
· a3 2,4 ± 0,02 · a4 62,83 ± 0,1 (20π = 62,8319) · a5 20 ± 0,2 Tage, alternativ 480 ± 4,8 Stunden.
Alle Toleranzen sind eng genug, dass kein typischer Rechenfehler durchrutscht: Die nächstgelegenen
Fehlwerte (75/80; 87,96; 12; 25,13) liegen um Größenordnungen außerhalb. Die Alternativeinheit bei
a5 wird mit mitskalierter Toleranz geprüft. **Keine Beanstandung.**

---

## Blocker

**Keine.** Es wurde kein fachlicher Fehler, kein falscher Zahlenwert und kein erfundener
Lehrplanbezug gefunden. Alle nachgerechneten Werte stimmen. Die drei Herleitungen sind
mathematisch tragfähig, die Simulationen bilden die Theorie korrekt ab.

## Mängel

**M1 · „Zum Umsatzmaximum" rechnet mit 8,333, zeigt aber 8,3 an** — Z. 1234/1203, Z. 512.
Der Knopf setzt `tExakt = t* = 25/3`, die Anzeige rundet auf eine Nachkommastelle. Die
angezeigten Beiträge +35,00/−35,00 €/Tag gehören zu 8,3333, nicht zu 8,3: Wer die Anzeige
nachrechnet, erhält 0,10·(400−6·8,3) = **35,02** und 5,83·(−6) = **−34,98** und hält die
Simulation für ungenau. Genau diese Nachrechnung verlangt der Beobachtungsauftrag (3). Im
Lehrerteil (Z. 923) ist die Abweichung sauber dokumentiert, auf der Schülerseite nicht. Die
Umsetzung weicht bewusst vom Plan ab (`inhalte/…md` Z. 816: „gerundet auf 0,1 Tage"); die
Entscheidung ist fachlich die bessere – nur zieht die Anzeige nicht mit.
*Korrektur:* bei gesetztem `tExakt` zwei Nachkommastellen zeigen (8,33) und in Z. 512
`t* = 25/3 ≈ 8,33` schreiben. Ebenso Z. 993/994: „5,83 · (−6) = −35,00" geht als Rechnung nicht
auf; besser „p(t*) = 35/6 € ≈ 5,83".

**M2 · Falsch gerundeter relativer Fehler in der als richtig markierten Option** — Z. 588
(Option 0 zu `sim3`): „3,23 % → 1,64 % → 0,83 % → **0,42 %**". Der Code rechnet
`rel = fe/ex` (Z. 1420); für Δt = 0,25 s ist das 0,125/30,125 = **0,415 %**, gerundet 0,41 %.
Der Lehrerteil (Z. 923) nennt korrekt 0,415 %, die Antwortoption widerspricht ihm. Der Fehler
stammt aus der Inhaltsquelle (dort Z. 1145 gegen die eigene Kontrolltabelle Z. 124).
*Korrektur:* „0,42 %" → „0,41 %". Nebenbei: „der relative Fehler halbiert sich" gilt nur
näherungsweise (Faktoren 1,97 / 1,98 / 1,99) – ein „nahezu" wäre präziser.

**M3 · Beobachtungsauftrag Simulation 1, Teil (2) ist nicht ausführbar** — Z. 447-448.
(1) endet bei Δt = 0,25 Tagen, (2) verlangt „Halbiere Δt **noch einmal** … bevor du liest".
Der Regler `rDt` hat `min="1"` bei `Δt = Wert·0,25` (Z. 478/1197); 0,25 Tage **ist** das Minimum.
Δt = 0,125 lässt sich nicht einstellen, es gibt nichts zu lesen.
*Korrektur:* Reihenfolge umdrehen – in (1) nur bis 0,50 notieren, in (2) den Wert für 0,25
vorhersagen lassen. Alternativ `min=1, max=32` bei `Δt = Wert·0,125`; t + Δt ≤ 25 bleibt gewahrt.

**M4 · Falsche Fehlermeldung bei der häufigsten Teillösung von Aufgabe 1** — Z. 1031/1032 mit
Z. 1091-1093. Der „nah"-Text greift nur für 0,5 < |Antwort/Sollwert| < 2. Die Antwort **75**
(nur der erste Summand) liegt mit 75/155 = **0,484** knapp darunter und erhält den „weit"-Text,
der mit „6 m²/Jahr wäre das Produkt der beiden Ableitungen" beginnt – ein Fehler, den diese
Schülerin nicht gemacht hat. Der eigens für 75 und 80 geschriebene „nah"-Text greift nur bei 80
(0,516). Dasselbe bei Aufgabe 7: t = 40 (aus U′ = 40 − t) liegt mit Faktor genau 2,0 außerhalb,
obwohl der „nah"-Text (Z. 1051) genau diesen Fall bespricht.
*Korrektur:* die Erklärungen zusätzlich in den „weit"-Text aufnehmen oder das Fenster weiten.
Die Engine selbst stammt aus dem Referenzmodul und wird nicht beanstandet – wohl aber, dass die
Feedbacktexte an ihren Schwellen vorbeigeschrieben sind.

**M5 · Die Aufgaben tragen auf der Seite keine sichtbare Nummer** — Abschnitt 5 durchgehend.
Der Schülertext verweist mehrfach auf Nummern: „in den **Aufgaben 8, 9 und 10** bearbeitet"
(Z. 865), „wie in **Aufgabe 7**" (Z. 861), „aus **Aufgabe 4**" (Z. 860). Über den Aufgabenkästen
steht aber nur der Anforderungsbereichs-Chip; die Zählung existiert allein im Lehrerteil und in
der Exportliste (Z. 1477-1491). Die Verweise laufen für die Lernenden ins Leere. Im Export heißen
die drei offenen Aufgaben zudem „Offene Aufgabe 1 bis 3" (Z. 1506), im Text 8 bis 10.
*Korrektur:* sichtbare Nummer je Kasten und im Export dieselbe Zählung.

**M6 · „Faktor 17" ist gerundet, ohne so gekennzeichnet zu sein** — Z. 203 und Z. 838:
10,00/0,60 = 16,67. In einem Modul, das sonst jede Zahl auf zwei Stellen verantwortet, fällt die
glatte 17 auf. *Korrektur:* „rund der Faktor 17" oder „der Faktor 16,7".

**M7 · Momentanrate und Tageszuwachs im Einstieg gleichgesetzt** — Z. 203: „In Wirklichkeit
steigt der Umsatz **am ersten Tag um 10 € pro Tag**." U′(0) = 10 €/Tag ist die Momentanrate;
der tatsächliche Zuwachs des ersten Tages ist U(1) − U(0) = **9,40 €**. Genau diese Differenz von
0,60 € ist später der Kern von Simulation 1 (Sekante gegen Tangente) – im Einstieg wird sie
eingeebnet. *Korrektur:* „steigt der Umsatz zu Beginn **mit** 10 € pro Tag"; der Hinweis, dass
der Zuwachs des ersten Tages etwas darunter liegt, wäre ein guter Vorgriff auf Abschnitt 4.

**M8 · Unbenannte Beweislücke bei der Reziprokenregel** — Z. 357-360. Aus v·w = 1 werden beide
Seiten abgeleitet; das setzt voraus, dass **w = 1/v überhaupt differenzierbar ist**. Genau diese
Existenzaussage liefert der Weg über die Kettenregel mit, hier wird sie stillschweigend
angenommen. Der behauptete „Vorzug gegenüber dem v⁻¹-Weg" (Z. 360) ist deshalb nur die halbe
Wahrheit. Bei der Kettenregel benennt das Modul seine Lücke vorbildlich (Z. 327) – hier fehlt
der entsprechende Satz. *Korrektur:* „Vorausgesetzt ist dabei, dass 1/v an dieser Stelle
differenzierbar ist; das zeigt man separat über den Differenzenquotienten von 1/v."

**M9 · Voraussetzungen im Kettenregel-Merksatz nicht genannt** — Z. 317-320. Der
Produktregel-Merksatz beginnt mit „Für differenzierbare Funktionen u und v", die Quotientenregel
führt v(x) ≠ 0 mit (Z. 374). Beim Kettenregel-Merksatz fehlt die Angabe (u differenzierbar an x,
v differenzierbar an u(x)); sie steckt nur implizit im Details-Block. Für einen LK ist das eine
erkennbare Ungleichbehandlung der drei Regeln.

**M10 · Widersprüchliche Meldung am Rand des Reglerbereichs** — Z. 1238 gegen Z. 1345/1367.
Das Umsatzdiagramm zeichnet die gestrichelte Linie „Maximum", sobald t* ≤ 25 Tage liegt; der
Knopf meldet dagegen ab t* > 21: „In diesem Zeitraum gibt es kein Maximum — der Umsatz ist
durchgehend monoton." Für 19 einstellbare Reglerkombinationen (z. B. b = 0,22 €/Tag, d = −6 →
t* = 21,97) steht beides gleichzeitig auf dem Bildschirm. Für den einstellbaren Bereich ist die
Aussage richtig, dem Bild widerspricht sie trotzdem. *Korrektur:* „… gibt es im einstellbaren
Zeitraum bis 21 Tage kein Maximum" oder die Hilfslinie ebenfalls bei 21 Tagen abschneiden.

**M11 · Die Simulationsfragen sind auch ohne Simulation lösbar** — Z. 498-520, Z. 584-594.
`CLAUDE.md` verlangt Fragen, „die sich **nur** mit der Simulation beantworten lassen". Alle drei
sind rein rechnerisch entscheidbar: b·d·Δt steht in der Tabelle Z. 436, t* und die ±35 sind eine
Zweizeilenrechnung, π·Δr² steht Z. 534. Die konkreten Zahlen in den Optionen binden die Fragen
immerhin an die Anzeige, und drei statt zwei Fragen sind ein Plus. Echten Simulationszwang
erzeugte eine Frage nach einem Zustand, den man nur durch Verstellen findet („Ab welchem d
verschwindet das Maximum aus dem Zeitraum?").

**M12 · Offener Punkt der Definition of Done** — `fachliches/modulliste.md` Z. 28 steht auf
„in Arbeit". Nach Einarbeitung der Korrekturen und bestandenem `modulcheck.py` auf „fertig" setzen.

---

## Bestanden – geprüft und ohne Befund

**Lehrplanbezug** (gegen `fachliches/kernlehrplan-nrw.md`). Der Chip Z. 188 nennt
„Inhaltsfeld: Funktionen und Analysis" – wörtlich so wie in der Referenz (dort Z. 38). Die
Einordnung in Q1 ist gedeckt: Die Referenz nennt die Ableitungsregeln ausdrücklich als Teil der
Q1-Analysis (Z. 42-44). **Kein einziges erfundenes Zitat.** Im Gegenteil: Der Zentralabitur-Kasten
verweigert die Zitation ausdrücklich („Der genaue Zuschnitt dieses Teils wird jährlich in den
Vorgaben des Landes festgelegt; er ist hier bewusst nicht zitiert", Z. 864), und der Lehrerteil
markiert die eigenen didaktischen Setzungen als solche (Z. 897: Reihenfolge der Regeln, Verzicht
auf den lückenlosen Kettenregelbeweis, Platzierung am Q1-Anfang). Das ist genau das in `CLAUDE.md`
geforderte Verhalten und sollte Vorbild für die übrigen Module sein. Die prozessbezogenen
Kompetenzen (Argumentieren, Problemlösen, Modellieren, Werkzeuge nutzen) werden nicht nur genannt,
sondern durch konkrete Aufgaben belegt.

**Anforderungsniveau.** Eigene Zuordnung, Aufgabe für Aufgabe: 1 → AB I; 2 → AB I/II; 3 bis 7
→ AB II; 8, 9, 10 → AB III. Bis auf Aufgabe 2 deckungsgleich mit der Auszeichnung in der Datei.
Der übliche Befund – als AB III ausgewiesene Aufgaben, die nur länger rechnen lassen – **trifft
hier nicht zu**: Alle drei AB-III-Aufgaben sind echte Bewertungs- bzw. Begründungsaufgaben
(zwei Merksätze prüfen; „Die Quotientenregel ist überflüssig" bewerten; eine Behauptung über die
Entbehrlichkeit der Kettenregel widerlegen), jede mit Musterlösung **und** eigenen
Bewertungskriterien (Z. 783, 807, 827). Aufgabe 2 (Wetterballon) verlangt Transfer auf die
Kugelformel, die Identifikation von innen/außen und die richtige Auswertungsstelle r(4); das ist
eher AB II als AB I. Die zu niedrige Einstufung schadet nicht, sie unterschätzt das Modul nur.
Das Niveau insgesamt entspricht dem Leistungskurs: zwei vollständige Herleitungen, eine benannte
Beweislücke, Verschachtelung zweier Regeln, Extremwertbetrachtung mit Vorzeichenargument.

**Fachliche Substanz.** Der Produktregelbeweis über den ergänzten Nullterm ist vollständig und
nennt die gebrauchte Stetigkeit von v ausdrücklich (Z. 278). Die Kettenregel-Herleitung benennt
die k ≠ 0-Lücke und den Ausweg über die lineare Näherung, ohne ihn zu verlangen (Z. 327) – das ist
fachlich ehrlich und für einen LK genau richtig dosiert. Der Aufbau Produktregel → Reziprokenregel
→ Quotientenregel ist stimmig; die Quotientenregel wird konsequent als Folgerung geführt und nicht
als viertes Gesetz. Die Bedingung v(x) ≠ 0 wird bei der Formel (Z. 374), in der Herleitung (Z. 371)
und in der Musterlösung (Z. 804) mitgeführt. Vorzeichen sind über die ganze Datei hinweg konsistent
(u′v − uv′, nie vertauscht; negative Raten durchgehend mit dem typografischen Minus −).

**Simulationscode.** Beide Simulationen bilden exakt die Fachtheorie ab; die Pixelumrechnungen
(SX = 1,4 px/Besucher, SY = 24 px/€, 1 m = 1 px) sind als Konstanten dokumentiert, und die
Reglergrenzen sind so gewählt, dass keine Größe den Achsenbereich verlässt (nachgerechnet: p ≤ 12,50
bei Achse 14; n ≤ 600 bei Achse 600; r ≤ 120 px bei Mittelpunkt 240/170). Die Legende
p·Δn + n·Δp + Δp·Δn = ΔU ist eine exakte Identität, nicht eine Näherung – das trägt die ganze
didaktische Pointe. `tStern()` ist korrekt hergeleitet und kann im gesamten Reglerraum kein
Minimum als „Maximum" ausgeben (vollständig durchgerechnet). Die Vorzeichenbehandlung ist
sorgfältig: `fmt()` fängt „−0,00" ab, `vz()` setzt Pluszeichen, negative Beiträge werden rot
statt grün eingefärbt.

**Didaktik.** Jeder der 18 Distraktoren (7 Multiple-Choice-Aufgaben, 25 Optionen) hat ein eigenes, inhaltliches Feedback, das den Denkfehler
benennt – kein einziges „Leider falsch". Mehrere Rückmeldungen nennen sogar den Zahlenwert, der
bei genau diesem Fehler herauskommt (201,06 bei fehlender innerer Ableitung; 132π = 414,69, wenn
r² wie r behandelt wird; die Konstante 80 bei doppelt gezähltem Minus) – alle drei nachgerechnet
und richtig. Die Hilfestufen sind echt abgestuft: Der Tipp bleibt begrifflich („Kläre zuerst,
welche Größe die innere ist"), der Ansatz gibt die Formel ohne Werte, erst der Lösungsweg rechnet.
Bei den AB-III-Aufgaben gibt Stufe 3 nur die **Gliederung** der Antwort und die Musterlösung liegt
hinter einem eigenen Knopf – besser als im Referenzmodul, wo die offenen Aufgaben nur eine
Hilfestufe haben. Der Lehrerteil ist kein Allgemeinplatz: Zeitraster mit Sozialformen, zwei
alternative Schnitte für Einzelstunden, neun benannte Schülerfehler **mit Angabe, wo im Ablauf
anzuhalten ist**, Differenzierung nach oben (Dreifaktorregel, Induktion, Umkehrfunktion) und unten
(Pflichtauswahl), dazu tragfähige Experimente (DIN-A4-Blatt mit zwei Schnitten, Tinte auf
Löschpapier mit dem ehrlichen Hinweis, dass r(t) dort nicht linear ist, Fahrradübersetzung).

**Sprache und Form.** Durchgehend geduzt; die vier Treffer für „Sie/Ihre" sind Pronomen
(„Sie ist keine vierte Regel"), keine Anrede. Durchgehend Deutsch, auch in den Codekommentaren.
Dezimalkomma überall: Im Skript läuft jede Zahlenausgabe über `fmt()` mit
`toFixed(n).replace(".", ",")`; im Fließtext wurden keine Dezimalpunkte gefunden. Fachbegriffe
einheitlich (innere/äußere Funktion, Auswertungsstelle, Term zweiter Ordnung, Änderungsrate gegen
Funktionswert). Alle 454 Formelspannen tragen `data-plain`. Der CSS-Block ist bis auf die drei
vorgeschriebenen Farbtokens und den Kopfverlauf zeichengleich mit dem Referenzmodul (diff: 15
Zeilen, ausschließlich Farbwerte).

## Kurzfazit

Fachlich ist das Modul in ausgezeichnetem Zustand: Jede Musterlösung, jeder Feedbackwert, jeder
Simulationszustand und jede Lehrerteil-Tabelle wurde nachgerechnet und stimmt, der Lehrplanbezug
ist echt und an den unsicheren Stellen ausdrücklich als Setzung markiert, und die drei
AB-III-Aufgaben sind – anders als üblich – wirklich Bewertungsaufgaben mit Kriterien. Es gibt
keinen Blocker. Nacharbeit nötig ist trotzdem, und zwar an drei Stellen, die Lernende unmittelbar
treffen: Der Beobachtungsauftrag verlangt einen Reglerwert, den es nicht gibt (M3), die als richtig
markierte Option zu Simulation 2 nennt 0,42 % statt der angezeigten 0,415 % (M2), und das
Umsatzmaximum zeigt 8,3 Tage an, während es mit 8,333 rechnet, sodass die Kontrollrechnung der
Lernenden 35,02 statt 35,00 ergibt (M1). Die übrigen neun Punkte sind Textkorrekturen von je
ein bis zwei Sätzen – die Verwechslung von Momentanrate und Tageszuwachs im Einstieg (M7), die
unbenannte Differenzierbarkeitslücke bei der Reziprokenregel (M8) und die fehlende sichtbare
Aufgabennummerierung, auf die der Schülertext verweist (M5), sind die inhaltlich lohnendsten.
Nach diesen Korrekturen und einem erfolgreichen `modulcheck.py`-Lauf kann das Modul ohne Vorbehalt
in den Unterricht.
