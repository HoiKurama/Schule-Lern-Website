# Gegenprüfung nach Nacharbeit – module/physik-q1-elektrisches-feld.html

Prüfdatum 18.09.2026 · Prüfer: Fachprüfer-Agent (Gegenprüfung, 2. Durchgang)
Grundlage: Erstbefund `pruefung/fach-physik-q1-elektrisches-feld.md` (B1, B2, M1–M7),
Bauprotokoll `inhalte/_bauprotokoll-elektrisches-feld.md` (FORTSCHRITT-Zeilen 12–16),
Maßstab `CLAUDE.md` (Schule) und `fachliches/kernlehrplan-nrw.md`.
Das Modul wurde **nicht verändert**.

Vorgehen: (1) B1/B2 und M1–M7 einzeln gegen den Quelltext, (2) alle geänderten und neuen
Zahlenwerte per Python nachgerechnet, (3) Suche nach neu entstandenen Widersprüchen
zwischen Fließtext, Rückmeldungen, Lehrerteil und Simulationskern, (4) Prüfung, ob die
beiden Simulationsfragen jetzt tatsächlich die Simulation verlangen.

---

## 1 · Die beiden Blocker

### B1 – Größenordnung im Einstieg · **behoben**

Zeile 214 lautet jetzt: „… ergibt das C = 10,6 pF – gut ein **Zehnmillionstel** der Kapazität im
Defibrillator. Dass ein Bauteil über **knapp sieben** Zehnerpotenzen dieselbe Physik zeigt …“

Nachgerechnet: C = ε₀ · 6,0 · 1,0·10⁻⁴ m² / 0,50·10⁻³ m = 1,06248·10⁻¹¹ F.
C/100 µF = 1,0625·10⁻⁷, also 1 : 9,41 Millionen → „gut ein Zehnmillionstel“ ist korrekt
(der Wert liegt knapp **über** 10⁻⁷). log₁₀(100 µF / C) = 6,97 → „knapp sieben Zehnerpotenzen“
ist ebenfalls korrekt. Beide Halbsätze sind jetzt untereinander widerspruchsfrei.

### B2 – Begründung der Feldhomogenität · **behoben, an allen drei Stellen, und zusätzlich abgesichert**

Das falsche Kompensationsargument („eigener Beitrag wächst, fremder schrumpft“) ist an keiner
Stelle mehr vorhanden. Geprüft wurden alle drei Fundstellen des Erstbefunds und darüber hinaus
der gesamte Text per Volltextsuche nach „Beitrag“, „kompens“, „Superposition“:

| Fundstelle | Stand jetzt |
|---|---|
| 2.3, Z. 341 | „Jede Platte erzeugt für sich ein Feld; zwischen den Platten zeigen beide Beiträge in dieselbe Richtung und addieren sich, außerhalb zeigen sie entgegengesetzt und heben sich auf. **Warum jeder einzelne Beitrag vom Abstand unabhängig ist, klärt Abschnitt 3.1.**“ – richtig und mit sauberem Vorwärtsverweis |
| 3.1, Z. 399 | Vollständig ersetzt durch das Flächenelement-Argument: „E = σ/(2ε₀) … hängt vom Abstand zur Platte gar nicht ab. Entfernt man sich, wirkt zwar jedes einzelne Flächenelement schwächer (∼ 1/r²), dafür tragen entsprechend mehr Flächenelemente bei (∼ r²) … Beide Platten zusammen ergeben zwischen sich überall E = σ/ε₀ und außerhalb null. Nur am Rand … bricht dieses Argument zusammen – das ist das Streufeld.“ – fachlich korrekt |
| Lehrerteil, Z. 1038 | Enthält jetzt das richtige Argument **und** eine ausdrückliche Warnung: „Vorsicht: Das oft gehörte Kompensationsargument ‚eigener Beitrag wächst, fremder schrumpft‘ ist **falsch**, denn beide Beiträge sind einzeln abstandsunabhängig.“ |

Die Warnung im Lehrerteil geht über die Forderung des Erstbefunds hinaus und ist eine echte
Verbesserung: Die Lehrkraft wird jetzt gegen genau die Fehlvorstellung immunisiert, die vorher
im Modul stand. Der Widerspruch zur Differenzierung (Z. 1050, „E = σ/(2ε₀) … zwei Ebenen ergeben
σ/ε₀“) ist damit aufgelöst – alle vier Stellen sagen jetzt dasselbe.

**Beide Blocker sind erledigt.**

---

## 2 · Die sieben Mängel

| # | Befund im Erstbericht | Stand | Fundstelle jetzt |
|---|---|---|---|
| M1 | Beobachtungsauftrag nicht eindeutig | **behoben** | Z. 566–569 |
| M2 | „vier angezeigte Größen“, es sind fünf | **behoben** | Z. 566, 618–620 |
| M3 | Simulationsfragen ohne Simulation lösbar | **teilweise behoben** | Z. 618–639 (s. u. Abschnitt 4) |
| M4 | ue6: unvollständige Lösung gilt als richtig | **behoben** | Z. 846, 865–878, 1170–1180 |
| M5 | Toleranzgrenze macht „nah“ unerreichbar | **behoben** | Z. 1227 |
| M6 | ue3 als AB II ausgewiesen | **behoben** | Z. 712 |
| M7 | sechs Einzelpunkte | **fünf behoben, einer bewusst offen** | s. u. |

**M1.** Der Auftrag lautet jetzt: „Notiere C, Q, U, E und W … Zwei der **fünf** Größen bleiben in
Durchgang 2 gegenüber dem Start exakt gleich. Bei der einen ist das die Definition des Abtrennens,
bei der anderen das eigentlich Überraschende. Benenne beide und schreib auf: erstens, warum die
zweite trotz des Ziehens unverändert bleibt; zweitens, warum die gespeicherte Energie im einen
Durchgang steigt und im anderen sinkt.“ Das ist exakt der Vorschlag des Erstbefunds, sogar um die
Energiefrage erweitert. Gegengeprüft an der Messwerttabelle des Lehrerteils (Z. 1027–1032):
Von Start (17,71 pF · 3,542 nC · 200,0 V · 10,00 kV/m · 0,3542 µJ) bleiben in Durchgang 2
tatsächlich **genau zwei** Größen gleich, Q (3,542 nC) und E (10,00 kV/m). C, U und W ändern sich.
Der Auftrag ist damit eindeutig **und** vollständig beantwortbar. Die Differenzierung (Z. 1062)
bietet zusätzlich eine Halbierung des Auftrags an.

**M2.** Der Fragestamm nennt keine Zahl mehr, sondern benennt die Größen einzeln: „Vergleiche die
Anzeigen für U, E und Q vor und nach dem Ziehen“ (Z. 620). Die Falschangabe „vier“ ist weg.

**M4.** Der Abstand wird jetzt auf das **Dreifache** vergrößert (Z. 846). Nachgerechnet:
Q = 20 nC · W₁ = 2,0 µJ · C₂ = 33,33 pF · U₂ = 600 V · W₂ = 6,0 µJ · ΔW = **4,0 µJ**.
Damit ist der Sollwert von beiden Zwischenwerten verschieden. Zusätzlich fängt ein neuer
`sonder`-Block (Z. 1173–1178) die vier typischen Fehlwerte einzeln ab: 2,0 µJ (nur W₁),
6,0 µJ (nur W₂), −1,33 µJ (mit fester Spannung weitergerechnet) und 0,67 µJ (W₂ bei fester
Spannung). Alle vier nachgerechnet: W₂(U fest) = ½·33,33 pF·(200 V)² = 0,6667 µJ, Differenz
= −1,3333 µJ. Die Sonderwerte −1,33 und 0,67 liegen mit 0,0033 gut innerhalb der Toleranz 0,05.
Die Gegenprobe über die Kraft geht weiter exakt auf: d₁ = 3,5416 mm, E = 56,47 kV/m,
F = 564,72 µN, Δd = 2·d₁ = 7,0832 mm, F·Δd = 4,0000 µJ. **Das ist deutlich mehr als verlangt war.**

**M5.** Die Bedingung lautet jetzt `faktor >= 0.5 - eps && faktor <= 2 + eps` (Z. 1227), zusätzlich
ist der Sonderfallweg vorgeschaltet. Die Randwerte 2,0 und 8,0 µJ fallen damit in `nah`,
und die beiden praktisch wichtigen Fehlwerte haben ohnehin eigenen Text. Erledigt.

**M6.** ue3 ist auf `Anforderungsbereich I` gesetzt (Z. 712). Eigene Einstufung: Wiedererkennen
von vier Aussagen gegen die Regeltabelle aus 2.4 – AB I ist zutreffend. Die alternative
Lösung (Feldlinienbild mit eingebautem Fehler) wurde nicht gewählt; das ist zulässig, der
Zentralabitur-Hinweis (Z. 964) benennt die Aufgabenform weiterhin, ohne sie einzulösen.

**M7 im Einzelnen:**

- *Liniendichte statt Linienzahl* (Z. 363): jetzt „dort wächst die **Liniendichte** proportional
  zur Feldstärke“. Gegen den Code geprüft: n = round(E·L/100/400), Bildhöhe h = 10·L px, also
  n/h = E/400 000 je Pixel – unabhängig von L. Die Aussage ist jetzt exakt richtig.
- *Betragsstriche in vw1* (Z. 1105): jetzt „F = 1/(4π·ε₀) · |q₁|·|q₂|/r²“. Konvention
  durchgängig.
- *ε_r = 4,5 in ue5* (Z. 809): jetzt „Kunststofffolie (etwa aus PVC oder Polyamid; der Wert
  streut je nach Sorte)“. Der Wert ist damit belegt statt gegriffen. Fachlich vertretbar
  (PVC 3–4, Polyamid 4–5 je nach Feuchte).
- *Einheitenvorsätze in Extremzuständen* (Z. 1343/1344): jetzt umschaltend –
  `w.E >= 1e6 ? MV/m : kV/m` und `w.W >= 1e-3 ? mJ : µJ`. Im Durchschlagszustand des
  Lehrerteils zeigt die Simulation damit **5,40 MV/m** und **6,455 mJ** (nachgerechnet:
  E = 5,3999…·10⁶ V/m, W = 6,45457·10⁻³ J). Behoben.
- *Regler nach dem Abtrennen* (Z. 1345): `rU.style.opacity = z.modus === "quelle" ? "1" : "0.5"`,
  zusammen mit dem Label-Zusatz „(folgt aus Q)“. Behoben.
- *AB III ohne dreistufige Hilfe*: unverändert (ue7–ue9 bieten nur „Musterlösung anzeigen“).
  Das war im Erstbefund ausdrücklich als Hausstandard-Frage und **nicht** als Mangel dieses
  Moduls markiert. Bleibt zu Recht offen.

---

## 3 · Nachgerechnet – alle geänderten und neuen Werte

Python, ε₀ = 8,854·10⁻¹² F/m. Die Anzeigeformate der Simulation wurden mitgerechnet
(`toFixed(2)` für C, `toFixed(3)` für Q, `toFixed(1)` für U, `toFixed(2)` für E, `toFixed(4)` für W).

| Fundstelle | Größe | Datei | nachgerechnet | Urteil |
|---|---|---|---|---|
| Z. 214 | C Fingerkuppe (1,0 cm², 0,50 mm, ε_r = 6,0) | 10,6 pF | 1,06248·10⁻¹¹ F | ✓ |
| Z. 214 | C_Finger / C_Defi (100 µF) | „gut ein Zehnmillionstel“ | 1,0625·10⁻⁷ = 1 : 9,41 Mio. | ✓ |
| Z. 214 | Zehnerpotenzen | „knapp sieben“ | 6,974 | ✓ |
| Z. 620/1121 | sim1 Start, Glas: C | (Anzeige) | 106,248 pF → „106,25 pF“ | ✓ |
| Z. 1120/1121/1123 | sim1: Q mit Glas | 21,250 nC | 2,12496·10⁻⁸ C → „21,250 nC“ | ✓ |
| Z. 1123 | sim1: Q mit Luft zum Vergleich | 3,542 nC | 3,5416 nC | ✓ |
| Z. 623 | sim1: U nach dem Ziehen (abgetrennt) | 400 V | Q/C′ = 400,0 V exakt | ✓ |
| Z. 623/1121 | sim1: E vor und nach dem Ziehen | 10,00 kV/m | 10 000 V/m beide Male | ✓ |
| Z. 622/1120 | sim1 Distraktor 0: E angeschlossen | 5,00 kV/m | 200 V / 0,040 m = 5 000 V/m | ✓ |
| Z. 624/1122 | sim1 Distraktor 2 | 20,00 kV/m wäre falsch, richtig 10,00 | 400/0,040 = 10 000 V/m | ✓ |
| Z. 625 | sim1 Distraktor 3 | „etwa 1,67 kV/m“ | 10,00/6 = 1,667 kV/m | ✓ |
| Z. 632/634 | sim2: W Start mit Glas | 2,1250 µJ | 2,12496·10⁻⁶ J → „2,1250 µJ“ | ✓ |
| Z. 634/1126 | sim2: W abgetrennt, d = 40 mm | 4,2499 µJ | Q²/(2C′) = 4,24992·10⁻⁶ J → „4,2499 µJ“ | ✓ |
| Z. 634/1126 | sim2: W angeschlossen, d = 40 mm | 1,0625 µJ | ½C′U² = 1,06248·10⁻⁶ J → „1,0625 µJ“ | ✓ |
| Z. 1127 | sim2 fb[1]: „Faktor 4 zwischen beiden Endwerten“ | Faktor 4 | 4,24992/1,06248 = 4,0000 | ✓ |
| Z. 846/878 | ue6: Q bei C₁ = 100 pF, U₁ = 200 V | 20 nC | 2,0·10⁻⁸ C | ✓ |
| Z. 872 | ue6: W₁ | 2,0 µJ | 2,0000·10⁻⁶ J | ✓ |
| Z. 873 | ue6: C₂ = C₁/3, U₂ | 33,3 pF, 600 V | 33,333 pF, 600,0 V | ✓ |
| Z. 875 | ue6: W₂ | 6,0 µJ | 6,0000·10⁻⁶ J | ✓ |
| Z. 876/1170 | ue6: ΔW (Sollwert der Eingabe) | 4,0 µJ | 4,0000·10⁻⁶ J | ✓ |
| Z. 878 | ue6 Gegenprobe: d₁ bei A = 400 cm² | 3,54 mm | 3,5416 mm | ✓ |
| Z. 878 | ue6 Gegenprobe: E, F, Δd, F·Δd | 56,5 kV/m · 565 µN · 7,08 mm · 4,0 µJ | 56,472 kV/m · 564,72 µN · 7,0832 mm · 4,0000 µJ | ✓ |
| Z. 1176 | ue6 Sonderfall: Differenz bei fester Spannung | −1,33 µJ | −1,3333 µJ | ✓ |
| Z. 1176/1177 | ue6 Sonderfall: W₂ bei fester Spannung | 0,67 µJ | 0,66667 µJ | ✓ |
| Z. 1042 | Lehrerteil: Fehlerergebnis ue6 | „−1,3 µJ statt +4,0 µJ“ | −1,3333 µJ | ✓ |
| Z. 1170 | ue6 Alternativeinheit + Toleranz | 4000 nJ, altTol = 50 nJ | 0,05 µJ = 50 nJ, Faktor stimmt | ✓ |
| Z. 1343 | Anzeige E im Durchschlagszustand | „5,40 MV/m“ | 5,3999…·10⁶ V/m | ✓ |
| Z. 1344 | Anzeige W im Durchschlagszustand | „6,455 mJ“ | 6,45457·10⁻³ J | ✓ |
| Z. 1043 | Lehrerteil: „Bei 26 Linien ist Schluss“ | 26 | `N_MAX = 26`; roh = 75 im genannten Zustand | ✓ |
| Z. 1052 | Differenzierung: Reihenschaltung d/2 Glas | 30,36 pF gegen 106,25 pF | 30,357 pF; 106,248 pF | ✓ |
| Z. 1045 | Lehrerteil: ε_r im Nenner → Faktor 4,5² | 20,25 | 20,25 | ✓ |
| Z. 1009–1018 | Lehrerteil: Summe der Zeitangaben | 135 min (Chip Z. 197) | 10+25+35+25+30+10 = 135 | ✓ |
| Z. 1027–1032 | Messwerttabelle zum Beobachtungsauftrag | 15 Felder | Simulationsnachbau zeichengenau identisch | ✓ |

**Alle nachgerechneten Werte stimmen. Kein einziger Rechenfehler, auch nicht in den neu
eingefügten Sonderfalltexten.** Die Rundung „4,2499“ (statt 4,2500) ist korrekt: der exakte Wert
ist 4,24992 µJ, `toFixed(4)` liefert 4,2499. Fragestamm, Option und Rückmeldung nennen alle
denselben String.

### Simulationskern gegen Handrechnung (zwei neue Zustände)

| Zustand | Simulation (`rechne()` nachgebaut) | Handrechnung | Urteil |
|---|---|---|---|
| Glas, 200 V, 20 mm, 20 cm, angeschlossen | C 106,25 pF · Q 21,250 nC · U 200,0 V · E 10,00 kV/m · W 2,1250 µJ | C = ε₀·6·0,04/0,020 = 1,06248·10⁻¹⁰ F; Q = CU; E = U/d; W = ½CU² | ✓ |
| Glas, abgetrennt, auf 40 mm gezogen | C 53,12 pF · Q 21,250 nC · U 400,0 V · E 10,00 kV/m · W 4,2499 µJ | U = Q/C′ = 400 V; E = Q/(ε₀ε_rA) = 10 kV/m; W = Q²/(2C′) | ✓ |

Die Vorzeichenkonvention ist über die ganze Datei einheitlich: Q und E werden durchgehend als
Beträge geführt (Tabelle Z. 273–275), die positive Platte liegt immer links, Feldlinien zeigen
nach rechts (Z. 286), und das einzige vorzeichenbehaftete Ergebnis – die Zugarbeit in ue6 – wird
im Sonderfalltext ausdrücklich diskutiert („Ein negatives Ergebnis hätte bedeutet, dass beim
Ziehen Energie frei wird“). Konsistent.

---

## 4 · Sind die Simulationsfragen jetzt nur mit der Simulation lösbar?

**Kurzantwort: sim2 ja, sim1 nein.** Das war der einzige Punkt des Erstbefunds, dessen
Lösungsvorschlag nicht aufgegriffen wurde.

**sim1 (Z. 618–625).** Die richtige Option 1 lautet: „Die Spannung steigt von 200 V auf 400 V,
die Feldstärke bleibt bei 10,00 kV/m.“ Beide Zahlen stehen **wörtlich** in der Tabelle in 3.7
(Z. 538: „400 V“, Z. 540: „10,0 kV/m (unverändert!)“). Der Wechsel des Dielektrikums auf Glas
ändert daran nichts, weil E = U/d von ε_r nicht abhängt – die Glasvariante liefert genau
dieselben U- und E-Werte wie die Luftvariante in 3.7. Der einzige neue Zahlenwert (Q = 21,250 nC)
steht nur in den Rückmeldungen, nicht im Optionstext. Wer 3.7 gelesen hat, beantwortet sim1 ohne
die Simulation anzufassen. Die Vorgabe aus `CLAUDE.md` („Verständnisfragen, die sich **nur** mit
der Simulation beantworten lassen“) ist für sim1 nicht erfüllt.

*Vorschlag, klein und wirksam:* Den Fragestamm auf eine Größe legen, die in 3.7 nicht tabelliert
ist, zum Beispiel die **Energie im Vergleich zum Luftfall** („Um welchen Faktor unterscheidet
sich W bei Glas vom Wert bei Luft, und woran in der Anzeige liest du das ab?“), oder die im
Erstbefund vorgeschlagene Durchschlagsfrage – die Durchschlagsmeldung ist implementiert, wird im
Lehrerteil (Z. 1070) mit einem exakten Bedienrezept beschrieben und von **keiner** Aufgabe genutzt.

**sim2 (Z. 630–636).** Hier sind die drei Zahlen 2,1250 / 4,2499 / 1,0625 µJ in keinem Abschnitt
der Seite vorweggenommen; sie sind nur durch Ablesen oder durch eigenes Rechnen (C = 106,25 pF)
zu bekommen. Die *qualitative* Richtung (abgetrennt steigt, angeschlossen sinkt) steht allerdings
im Merksatz Z. 953. Weil alle drei Optionen aber auch numerisch verschieden sind, muss zumindest
einmal nachgesehen oder nachgerechnet werden. Für sim2 ist die Forderung im Wesentlichen erfüllt.

---

## 5 · Neu entstandene Fehler und Widersprüche

Ich habe die gesamte Datei nach Folgefehlern der Nacharbeit durchsucht: alle Querverweise auf
Aufgabe 3, 6 und 8, alle Vorkommen von „verdoppel/verdreifach“, alle Zahlenwerte aus 3.7 und ue6,
den Abgleich Fragestamm ↔ Option ↔ Rückmeldung ↔ Lehrerteil für sim1, sim2 und ue6 sowie die
Engine-Verträge.

**Keine fachlichen Widersprüche gefunden.** Im Einzelnen geprüft und in Ordnung:

- Der Lehrerteil (Z. 1042) ist auf den neuen ue6-Zuschnitt nachgezogen („−1,3 µJ statt +4,0 µJ“)
  und rechnerisch richtig. Kein anderer Querverweis nennt noch den alten Wert 2,0 µJ als Lösung.
- Die Messwerttabelle des Lehrerteils (Z. 1027–1032) passt zeichengenau zum neuen, fünfzeiligen
  Beobachtungsauftrag, und die Differenzierung (Z. 1062) verweist widerspruchsfrei darauf.
- Der Lehrerteil nennt ue3 nur noch unter „Kommunikation“ (Z. 998), nicht mehr mit einer
  AB-Stufe – die Umstufung auf AB I erzeugt keinen Widerspruch.
- Die Deckelungsangabe „Bei 26 Linien ist Schluss“ (Z. 1043) stimmt mit `N_MAX = 26` überein.
- Engine-Verträge unverändert intakt: Optionszahl = Zahl der Rückmeldungstexte (3/3/3/**4**/3/**4**),
  `data-i` lückenlos, Radio-Namen eindeutig, 446 Formeln alle mit `data-plain`.
- Sprache: durchgehend geduzt, deutsch, Komma als Dezimaltrennzeichen. Alle Punkt-Treffer im
  Fließtext sind Abschnittsnummern (2.4, 3.7 …) oder CSS. Keine Siez-Form.

**Drei neue Kleinigkeiten, alle unterhalb der Blocker-Schwelle:**

### N1 · sim1: Eine falsche Bedienreihenfolge erzeugt genau den Distraktorwert (Z. 625, 1123)

Der Fragestamm sagt „Stell Glas ein, sonst die Startwerte. Trenne die Quelle ab und zieh …“.
Wer die Reihenfolge vertauscht – also **erst** abtrennt und **dann** Glas einlegt – bekommt einen
physikalisch völlig korrekten, aber anderen Zustand: Q bleibt bei 3,542 nC (Luftwert), und die
Anzeige zeigt (nachgerechnet) U = 33,3 V und **E = 1,67 kV/m** bei 20 mm, nach dem Ziehen
U = 66,7 V und wieder E = 1,67 kV/m. Der Wert 1,67 kV/m ist **exakt** der Zahlenwert des
Distraktors 3. Ein Lernender, der so vorgeht, sieht seine „falsche“ Antwort auf dem Bildschirm
bestätigt und bekommt dann eine Rückmeldung, die den Denkfehler „Faktor 6 doppelt gezählt“
unterstellt – den er gar nicht begangen hat. (Der Zustand ist übrigens genau Fall 2 aus ue8.)
*Vorschlag:* Im Fragestamm „Setz zuerst zurück, stell dann Glas ein …“ ergänzen und in fb[3] einen
Satz anhängen: „Zeigt deine Anzeige wirklich 1,67 kV/m, hast du das Glas erst **nach** dem
Abtrennen eingelegt – dann bleibt die kleinere Luftladung eingefroren. Setz zurück und beginne neu.“

### N2 · ue6: Der Betrag 1,33 µJ wird nicht als Sonderfall erkannt (Z. 1173–1178)

Der Sonderfallblock fängt −1,33 µJ ab. Die Aufgabe fragt aber nach „der mechanischen Arbeit, die
verrichtet werden **muss**“ – wer mit fester Spannung rechnet und anschließend den Betrag angibt,
tippt **+1,33** ein. Dieser Wert fällt durch das Raster: Faktor 1,33/4,0 = 0,33 < 0,5, also läuft
er in den allgemeinen `weit`-Text. Der ist zwar sachlich passend, nennt den Denkfehler aber nicht.
*Vorschlag:* einen fünften Sonderfall `{wert:1.33, …}` mit demselben Text ergänzen, oder im
Sonderfallvergleich den Betrag prüfen.

### N3 · Die Inhaltsdatei ist beim Beobachtungsauftrag nicht nachgezogen

`inhalte/physik-q1-elektrisches-feld.md` Z. 986–1000 enthält noch die alte, zweideutige Fassung
(„Notiere C, Q, E und W … Eine der **vier** Größen …“), während das Modul die korrigierte
Fünf-Größen-Fassung führt. Alle anderen Korrekturen sind dort nachgezogen: B1 (Z. 151/152),
B2 (Z. 457, 2021–2024), ue6 mit Dreifachem Abstand (Z. 1535 ff.), sim1/sim2 mit Glas (Z. 1024 ff.),
Liniendichte, |q₁|·|q₂|, PVC-Hinweis, ue3 als AB I (Z. 1255, 2192). Das ist keine Fehlerquelle für
den Unterricht, aber die Inhaltsdatei ist laut Projektregel der Zwischenstand, aus dem gebaut wird –
eine abweichende Stelle führt beim nächsten Zugriff zurück in den alten Fehler.
Nebenbei: Die Behauptung in `inhalte` Z. 1015 („Sie sind **nur mit der Simulation** zu beantworten“)
trifft für sim1 nicht zu, siehe Abschnitt 4.

---

## 6 · Anforderungsniveau und Didaktik nach der Nacharbeit

**Eigene Einstufung, unabhängig von der Auszeichnung in der Datei:**

| Aufgabe | Datei | mein Urteil | Begründung |
|---|---|---|---|
| ue1 | I | I | Formel einsetzen, Einheiten umrechnen |
| ue2 | I | I | eine Multiplikation mit gegebenem C |
| ue3 | **I** | **I** | Wiedererkennen der Regeltabelle aus 2.4 – Umstufung war richtig |
| ue4 | II | II | Betriebsart erkennen, Formel umstellen, Funktionstyp ablesen; vier Zeilen, keine Rechnung |
| ue5 | II | II | zweistufige Rechnung mit Zwischengröße |
| ue6 | II | II | Fallunterscheidung plus Energiedifferenz; durch den Faktor 3 jetzt nicht mehr durch den Anfangswert abkürzbar |
| ue7 | III | III | Beurteilen einer Aussage in zwei Teilen **und** einer Analogie, mit Zahlenbeleg |
| ue8 | III | III | Fallunterscheidung, Energiebilanz mit benannter Quelle, Urteil über Entscheidbarkeit |
| ue9 | III | III | wissenschaftstheoretische Stellungnahme, zwei eigenständige Argumente |
| sim1 | II | I–II | grenzwertig, s. Abschnitt 4: die Antwort steht in 3.7 |
| sim2 | II | II | Zahlen müssen abgelesen oder selbst gerechnet werden |

Die Verteilung nach der Umstufung ist AB I: ue1–ue3 · AB II: ue4–ue6, sim1, sim2 · AB III:
ue7–ue9. Damit sind alle drei Anforderungsbereiche mit mindestens drei Aufgaben besetzt; die
Forderung aus `CLAUDE.md` ist erfüllt. Die drei AB-III-Aufgaben sind weiterhin echte Begründungs-
und Bewertungsaufgaben mit Musterlösung **und** operationalisierten Bewertungskriterien
(Z. 892, 908, 924) – keine verlängerten Rechnungen. Das ist LK-Niveau.

**Didaktik der neuen Teile.**

- *Distraktor-Feedback:* Jede der vier neuen sim1-Optionen und jede der drei sim2-Optionen hat
  einen Text, der den Denkfehler benennt und den Zahlenwert nennt, auf den er führt („Ein
  zusätzlicher Faktor 6 würde die Wirkung des Dielektrikums doppelt zählen“). Kein „Leider falsch“.
- *Hilfestufen ue6:* Stufe 1 stellt zwei Fragen ohne jede Formel („Was kann sich nach dem
  Abtrennen überhaupt noch ändern? Wo soll die Energie herkommen?“), Stufe 2 nennt die beiden
  Formeln ohne Zahlen, Stufe 3 rechnet vollständig mit Gegenprobe. Echt abgestuft, der Tipp
  verrät nichts.
- *Sonderfalltexte ue6:* Die vier neuen Texte sind das didaktisch stärkste Stück der Nacharbeit.
  Sie unterscheiden „nur W₁ gerechnet“, „nur W₂ gerechnet“, „mit fester Spannung gerechnet“ und
  „W₂ mit fester Spannung“ – vier verschiedene Denkfehler, vier verschiedene Antworten. Das geht
  weit über das hinaus, was der Erstbefund verlangt hatte.
- *Beobachtungsauftrag:* jetzt eindeutig, vollständig beantwortbar, und die Doppelfrage
  (welche Größe · warum die Energie einmal steigt und einmal sinkt) deckt beide Kernpunkte ab.
- *Lehrerteil:* unverändert stark und durch die neue Warnung vor dem Kompensationsargument
  (Z. 1038) sachlich verbessert.

---

## 7 · Gut gelöst – zur Übernahme in andere Module

1. **Die Blocker wurden nicht minimal, sondern gründlich behoben.** B2 ist an drei Stellen
   ersetzt worden *und* hat im Lehrerteil eine ausdrückliche Warnung vor dem alten, falschen
   Argument bekommen. So verhindert man Rückfälle.
2. **Der `sonder`-Block in der Zahleneingabe** (Z. 1173–1178) ist ein neuer Baustein, der in
   `vorlage/bausteine.md` gehört: typische Fehlwerte werden namentlich abgefangen und diagnostiziert,
   statt nur „nah“ oder „weit“ zu melden.
3. **Die Wahl des Faktors 3 statt 2 in ue6** löst das Konstruktionsproblem elegant: Alle
   Zwischenwerte bleiben glatt (20 nC, 2,0 µJ, 600 V, 6,0 µJ), die Gegenprobe über F·Δd geht
   weiter exakt auf, und die unvollständige Lösung ist nicht mehr als richtig zu tippen.
   Das ist die Art Aufgabenkonstruktion, die man sich merken sollte: **Kein Zwischenwert darf
   mit dem Ergebnis zusammenfallen.**
4. **Die umschaltenden Einheitenvorsätze** (Z. 1343/1344) mit sauberer Schwelle bei 10⁶ bzw. 10⁻³.
5. **Der Kommentar zur Toleranzgrenze** (Z. 1197–1205, 1214–1221) dokumentiert jetzt drei behobene
   Fallen im Quelltext. Solche Notizen sparen der nächsten Prüfung Zeit.
6. **Der Lehrplanbezug** ist unverändert einwandfrei: Der Chip (Z. 196) nennt „Inhaltsfeld:
   Ladungen, Felder und Induktion“ wörtlich wie `fachliches/kernlehrplan-nrw.md` Z. 15, die
   Q1-Zuordnung folgt Z. 21, die Kompetenzbereiche (Z. 998) decken sich wörtlich mit Z. 24.
   Kein erfundenes Zitat; didaktische Setzungen sind als solche markiert (Z. 1001–1006).

---

## Urteil

**Abnahmefähig – mit drei kleinen Nachträgen, die den Unterrichtseinsatz nicht aufhalten.**

Beide Blocker sind vollständig und sauber behoben, und die Korrektur von B2 geht über das
Geforderte hinaus, weil der Lehrerteil die Lehrkraft jetzt ausdrücklich vor dem falschen
Kompensationsargument warnt. Von den sieben Mängeln sind sechs erledigt, der siebte (M3,
„nur mit der Simulation lösbar“) ist für sim2 gelöst und für sim1 offen geblieben, weil dessen
Zahlenwerte unverändert in der Tabelle in 3.7 stehen. Ich habe alle geänderten und neuen
Zahlenwerte einzeln in Python nachgerechnet – vom Zehnmillionstel im Einstieg über die
Glas-Zustände der Simulation (106,25 pF · 21,250 nC · 2,1250 → 4,2499 bzw. 1,0625 µJ) und die
neue ue6 (ΔW = 4,0 µJ, Gegenprobe F·Δd = 4,0000 µJ) bis zu den vier Sonderfallwerten – und
**kein einziger ist falsch**; der Simulationskern liefert in allen geprüften Zuständen exakt die
Handrechnung, einschließlich der Anzeigeformatierung. Neu entstandene Fehler gibt es nicht; die
drei Kleinigkeiten N1 (falsche Bedienreihenfolge erzeugt zufällig den Distraktorwert 1,67 kV/m),
N2 (Betrag 1,33 µJ ohne eigenen Sonderfalltext) und N3 (Beobachtungsauftrag in der Inhaltsdatei
nicht nachgezogen) sind in einer Viertelstunde erledigt und rechtfertigen keine zweite Runde.
Das Modul kann in den Unterricht; der Eintrag in `fachliches/modulliste.md` kann auf **fertig**
gesetzt werden, sobald N1 und N3 eingearbeitet sind – sim1 sollte bei nächster Gelegenheit auf
eine Frage umgestellt werden, die nur am Gerät zu beantworten ist.
