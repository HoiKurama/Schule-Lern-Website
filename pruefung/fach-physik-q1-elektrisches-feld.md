# Fachprüfung – module/physik-q1-elektrisches-feld.html

Prüfdatum 18.09.2026 · Prüfer: Fachprüfer-Agent · Quelle der Inhalte: `inhalte/physik-q1-elektrisches-feld.md`,
Bauprotokoll `inhalte/_bauprotokoll-elektrisches-feld.md` · Maßstab: `CLAUDE.md` (Schule) und
`fachliches/kernlehrplan-nrw.md`. Das Modul wurde **nicht verändert**.

---

## Blocker

### B1 · Falsche Größenordnung im Einstieg (Zeile 208)

> „… ergibt das C = 10,6 pF – gut ein **Hunderttausendstel** der Kapazität im Defibrillator.“

Das Modul legt die Defibrillator-Kapazität in 3.5 (Zeile 494) selbst auf **100 µF** fest
(„100 µF statt 17,7 pF ist ein Faktor von rund 5,6 Millionen“). Damit ist

    10,6 pF / 100 µF = 1,06·10⁻¹¹ F / 1,0·10⁻⁴ F = 1,06·10⁻⁷

also rund **ein Zehnmillionstel**, nicht ein Hunderttausendstel. Der Fehler beträgt einen
Faktor 100. Er widerspricht außerdem dem übernächsten Halbsatz derselben Zeile („über sechs
Zehnerpotenzen“ – tatsächlich sind es 7,0 Zehnerpotenzen; ein Hunderttausendstel wären 5).

**Korrektur:** „gut ein Zehnmillionstel der Kapazität im Defibrillator“ (und wahlweise
„über sieben Zehnerpotenzen“). Die Aussage stammt unverändert aus der Inhaltsdatei
(`inhalte/physik-q1-elektrisches-feld.md`, Zeile 151) und muss dort mitkorrigiert werden.

### B2 · Falsche Begründung für die Homogenität des Feldes (Zeilen 335, 393 und 1032)

Das Modul begründet dreimal, warum das Feld im Plattenkondensator überall gleich stark ist,
und zwar jedes Mal mit einem **Kompensationsargument zwischen den beiden Platten**:

> (2.3, Zeile 335) „… warum das Feld zwischen zwei großen, entgegengesetzt geladenen Platten
> überall gleich aussieht: Was die eine Platte an einer Stelle weniger beiträgt, steuert die
> andere mehr bei.“
>
> (3.1, Häufiger Fehler, Zeile 393) „Nähert man sich der positiven Platte, wird ihr eigener
> Beitrag tatsächlich größer – der Beitrag der weiter entfernten negativen Platte wird aber im
> selben Maß kleiner. Die Summe bleibt konstant.“
>
> (Lehrerteil, typischer Fehler 2, Zeile 1032) „Das Argument über die Superposition (eigener
> Beitrag wächst, Beitrag der Gegenplatte schrumpft im selben Maß) **gemeinsam entwickeln
> lassen, nicht vorsagen**.“

Das ist in dem Modell, mit dem das ganze Modul rechnet, **falsch**. Eine ausgedehnte geladene
Ebene erzeugt das Feld

    E = σ / (2 ε₀),

und dieser Wert hängt vom Abstand **gar nicht** ab. Der Beitrag der nahen Platte wird also beim
Annähern *nicht* größer, und der der fernen Platte wird *nicht* kleiner. Die Behauptung, beides
ändere sich „im selben Maß“, ist zudem in sich widersprüchlich: Zwei konstante Summanden ändern
sich überhaupt nicht.

Das Modul kennt den richtigen Sachverhalt selbst – die Differenzierung im Lehrerteil (Zeile 1044)
schreibt korrekt: „Eine einzelne geladene Ebene erzeugt E = σ/(2ε₀); zwei entgegengesetzt
geladene Ebenen ergeben zwischen sich E = σ/ε₀ und außerhalb null.“ Damit steht die
Fehlvorstellungs-Box in 3.1 im direkten Widerspruch zum eigenen Lehrerteil. Besonders
gravierend ist Fundstelle 1032, weil die Lehrkraft dort ausdrücklich angehalten wird, das
falsche Argument mit dem Kurs an der Tafel zu entwickeln.

**Korrekturvorschlag** (die Kompensation liegt nicht zwischen den Platten, sondern zwischen
Abstandsgesetz und beitragender Fläche):

> Jede Platte für sich erzeugt ein Feld, das vom Abstand nicht abhängt: Entfernt man sich, wirkt
> zwar jedes einzelne Flächenelement schwächer (1/r²), dafür tragen immer mehr Flächenelemente
> bei (∼ r²) – beides hebt sich exakt auf, und es bleibt E = σ/(2ε₀). Beide Platten zusammen
> ergeben zwischen sich überall E = σ/ε₀ und außerhalb null. Nur am Rand, wo die Platte nicht
> mehr „groß“ gegen den Abstand ist, bricht das Argument zusammen – das ist das Streufeld.

Diese Fassung ist für den LK sogar der bessere Weg, weil sie 3.1 direkt mit der Nebenformel
E = σ/(ε₀ε_r) aus 3.4 verzahnt, die ohnehin gebraucht wird.

---

## Mängel

### M1 · Beobachtungsauftrag ist nicht eindeutig lösbar (Zeile 560–563)

Der Auftrag lautet: „Notiere C, Q, E und W … Eine der vier Größen verhält sich in den beiden
Durchgängen auffällig anders als die übrigen – sie ändert sich im einen Fall und bleibt im
anderen exakt gleich.“ Nachgerechnet (und von der Simulation so angezeigt):

| Größe | Start | Durchgang 1 (angeschlossen) | Durchgang 2 (abgetrennt) |
|---|---|---|---|
| C | 17,71 pF | 8,85 pF | 8,85 pF |
| Q | 3,542 nC | 1,771 nC | **3,542 nC (gleich)** |
| E | 10,00 kV/m | 5,00 kV/m | **10,00 kV/m (gleich)** |
| W | 0,3542 µJ | 0,1771 µJ | 0,7083 µJ |

**Zwei** der vier Größen – Q und E – erfüllen das Kriterium wörtlich. Gemeint ist E; Q ist
trivialerweise konstant, weil abgetrennt wurde. Aufmerksame Lernende notieren Q und haben nach
dem Wortlaut recht.
**Vorschlag:** „Zwei der vier Größen bleiben in Durchgang 2 gleich. Bei einer davon ist das die
Definition des Abtrennens – bei der anderen ist es das eigentlich Überraschende. Benenne beide
und erkläre die zweite.“ Das macht den Auftrag eindeutig und gewinnt sogar an Tiefe.

### M2 · Simulationsfrage sim1: „vier angezeigte Größen“ – es sind fünf (Zeile 614)

Die Anzeige führt C, Q, U, E und W (Zeilen 574–578). Die Frage spricht von „den vier angezeigten
Größen“ und bietet vier Optionen (U, E, C, W) – Q fehlt, obwohl Q angezeigt wird und ebenfalls
exakt konstant bleibt. Die Frage ist über die Optionen eindeutig, der Fragestamm aber falsch.
**Vorschlag:** „Welche Größe außer der Ladung bleibt exakt unverändert?“

### M3 · Beide Simulationsfragen sind ohne die Simulation beantwortbar

`CLAUDE.md` verlangt „zwei anschließenden Verständnisfragen, die sich **nur** mit der Simulation
beantworten lassen“. Die Tabelle in 3.7 (Zeilen 528–537) enthält die vollständige Antwort auf
sim1 (E „10,0 kV/m (unverändert!)“) und auf sim2 sogar mit denselben Zahlen (0,354 → 0,708 bzw.
0,177 µJ), die in der Fragestellung von sim2 wörtlich wiederholt werden. Wer 3.7 gelesen hat,
braucht die Simulation nicht anzufassen.
**Vorschlag:** Mindestens eine der beiden Fragen auf einen Zustand legen, der in 3.7 nicht
tabelliert ist – zum Beispiel: „Stell L = 30 cm und Glas ein, trenne ab und schalte auf Luft.
Ab welchem Plattenabstand meldet die Simulation einen Durchschlag, und passt das zu
E_max = 3 MV/m?“ Das ist nur am Gerät zu beantworten und nutzt eine Funktion, die sonst
ungenutzt bleibt.

### M4 · Aufgabe 6: Die unvollständige Lösung wird als richtig gewertet (Zeilen 838–872, 1164)

Gefragt ist die Zugarbeit W₂ − W₁. Weil der Abstand **verdoppelt** wird, gilt W₂ = 2·W₁ und
damit ΔW = W₁ = 2,0 µJ. Wer also nur den **Anfangswert** W₁ = ½C₁U₁² = 2,0 µJ ausrechnet und
dort stehen bleibt, gibt 2,0 µJ ein und bekommt von der Prüfroutine „Richtig“ – obwohl er die
eigentliche Aufgabe (Fallunterscheidung, Energiedifferenz) nicht gelöst hat. Die Toleranz
(±0,05 µJ) kann daran nichts ändern, das ist ein Konstruktionsproblem der Zahlenwerte.
**Vorschlag:** Abstand statt auf das Doppelte auf das **Dreifache** vergrößern. Dann ist
W₂ = 3·W₁ = 6,0 µJ und ΔW = 4,0 µJ ≠ W₁; alle Zwischenwerte (20 nC, 2,0 µJ, 600 V, 6,0 µJ)
bleiben glatt, und die Gegenprobe über F·Δd = 565 µN · 7,083 mm = 4,0 µJ geht weiter auf.

### M5 · Toleranzgrenze macht die passgenaue Rückmeldung in ue6 unerreichbar (Zeilen 1167, 1209)

Der häufigste Fehler in ue6 ist das Weiterrechnen mit fester Spannung; er führt auf 1,0 µJ.
Die Rückmeldung `nah` ist genau darauf zugeschnitten („Mit konstanter Spannung käme man auf
1,0 µJ“), greift aber nie: Die Bedingung lautet `faktor > 0.5 && faktor < 2`, und 1,0/2,0 ist
exakt 0,5. Ausgegeben wird stattdessen `weit`. Der Text dort ist zwar auch brauchbar, die
zielgenaue Diagnose geht aber verloren. Dasselbe gilt am oberen Rand für die Eingabe 4,0 µJ
(Faktor exakt 2). **Vorschlag:** `faktor >= 0.5 && faktor <= 2` oder – konsequenter – die
beiden typischen Fehlwerte 1,0 und 4,0 als eigene Fälle mit eigenem Text abfangen.

### M6 · Aufgabe 3 ist als AB II ausgewiesen, liegt aber bei AB I–II (Zeilen 705–712)

Die als richtig zu erkennende Aussage 2 steht in 2.4 wörtlich in der Regeltabelle (Zeile 353:
„Eine Tangentialkomponente würde die frei beweglichen Ladungen im Leiter verschieben, und zwar
so lange, bis sie verschwunden ist“) – die Option wiederholt diese Begründung fast unverändert.
Auch die drei Distraktoren sind die drei Fehlvorstellungen aus denselben Absätzen. Verlangt ist
damit Wiedererkennen, nicht Übertragen. Als AB II hält die Aufgabe nur durch, weil vier
Aussagen zu prüfen sind. **Vorschlag:** entweder als AB I ausweisen oder ein Feldlinienbild mit
einem eingebauten Fehler zeigen und beurteilen lassen – letzteres wird im eigenen
Zentralabitur-Hinweis (Zeile 958) als typische Aufgabenform benannt und fehlt bisher.

### M7 · Kleinere Unstimmigkeiten

- **Zeile 357:** „dort wächst die Zahl der Linien proportional zur Feldstärke“. Im Code ist
  `roh = round(E · L/400)`, die Linienzahl wächst also proportional zu **E·L**; konstant
  proportional zu E ist die Linien*dichte* (Nachrechnung: Dichte = n/h = E/400 000 je Pixel,
  unabhängig von L). Fachlich ist der Code richtig, der Satz ist ungenau.
  **Vorschlag:** „dort wächst die Liniendichte proportional zur Feldstärke“.
- **Zeile 1099 (Rückmeldung vw1):** „F = 1/(4π·ε₀) · q₁·q₂/r²“ – ohne Betragsstriche, während
  das Modul sonst konsequent |q₁|·|q₂| schreibt (Zeilen 287, 329). Die Konvention wird an
  genau einer Stelle durchbrochen.
- **Zeile 803 (ue5):** ε_r = 4,5 für „Kunststofffolie“ steht in keiner der Tabellen des Moduls
  (Zeile 442–448 nennt PE 2,3; Papier 2,0 bis 2,5). Der Wert ist für PVC oder Polyamid
  vertretbar, sollte aber benannt werden, sonst wirkt er gegriffen.
- **Anzeige in Extremzuständen:** Die Einheitenvorsätze sind fest verdrahtet. Im
  Durchschlagsfall zeigt die Simulation „E = 5400,00 kV/m“ und „W = 6454,5660 µJ“ statt
  5,40 MV/m und 6,45 mJ. Fachlich richtig, für den LK aber unschön – und es ist genau der
  Zustand, den der Lehrerteil (Zeile 1064) im Unterricht vorführen lässt.
- **Regler „Spannung U“ nach dem Abtrennen:** Der Reglerknopf bleibt auf 200 stehen, während
  das Label „400 V (folgt aus Q)“ anzeigt. Der Zusatztext entschärft das, eine optische
  Ausgrauung des Reglers wäre sauberer.
- **AB III ohne dreistufige Hilfe:** ue7–ue9 bieten nur „Musterlösung anzeigen“. Das entspricht
  dem Referenzmodul (`physik-q1-induktion.html`, Zeilen 507–522) und ist damit Hausstandard –
  der Wortlaut in `CLAUDE.md` („jede mit dreistufigem Hilfesystem“) ist davon abweichend.
  Kein Vorwurf an dieses Modul, aber die Regel und der Standard sollten angeglichen werden.

---

## Nachgerechnet

Alle Werte mit ε₀ = 8,854·10⁻¹² F/m, e = 1,602·10⁻¹⁹ C in Python nachgerechnet.

| Fundstelle | Größe | Datei | nachgerechnet | Urteil |
|---|---|---|---|---|
| Z. 202 | Defibrillator-Leistung 200 J / 10 ms | 20 kW | 20 000 W | ✓ |
| Z. 202 | 40 kJ / 200 J | 200-fach | 200 | ✓ |
| Z. 208/209 | C Fingerkuppe (1,0 cm², 0,50 mm, ε_r = 6) | 1,06·10⁻¹¹ F = 10,6 pF | 1,0625·10⁻¹¹ F | ✓ |
| Z. 208 | C_Finger / C_Defi (100 µF) | „ein Hunderttausendstel“ | 1,06·10⁻⁷ | **✗ B1** |
| Z. 321 | E einer Punktladung 1,0 nC in 5,0 cm | 3,6·10³ V/m | 3 595 V/m | ✓ |
| Z. 323 | F = q·E für q = 1,0 nC | 3,6 µN | 3,595 µN | ✓ |
| Z. 415 | E = 200 V / 0,020 m | 10 kV/m | 10 000 V/m | ✓ |
| Z. 415 | Durchschlagsspannung bei 20 mm | rund 60 kV | 60 000 V | ✓ |
| Z. 427 | 1 C in Elementarladungen | rund 6·10¹⁸ | 6,24·10¹⁸ | ✓ |
| Z. 463 | σ und E = σ/ε₀ (Startwerte) | 8,854·10⁻⁸ C/m²; 10 000 V/m | identisch | ✓ |
| Z. 494 | W Startwerte | 3,54·10⁻⁷ J = 0,354 µJ | 3,5416·10⁻⁷ J | ✓ |
| Z. 494 | 200 J / W_start | „Sechshundertmillionenfache“ | 5,65·10⁸ | ✓ |
| Z. 494 | 100 µF / 17,708 pF | rund 5,6 Millionen | 5,647·10⁶ | ✓ |
| Z. 509 | w = ½ε₀E²; w·V | 4,43·10⁻⁴ J/m³; 3,54·10⁻⁷ J | 4,427·10⁻⁴; 3,5416·10⁻⁷ | ✓ |
| Z. 531–535 | Tabelle d = 40 mm, angeschlossen | 8,85 pF · 200 V · 1,77 nC · 5,00 kV/m · 0,177 µJ | 8,854 pF · 200 V · 1,7708 nC · 5 000 V/m · 0,17708 µJ | ✓ |
| Z. 531–535 | Tabelle d = 40 mm, abgetrennt | 8,85 pF · 400 V · 3,54 nC · 10,0 kV/m · 0,708 µJ | 8,854 pF · 400 V · 3,5416 nC · 10 000 V/m · 0,70832 µJ | ✓ |
| Z. 544/545 | F = ½QE und W = F·Δd | 17,7 µN; 0,354 µJ | 17,708 µN; 0,35416 µJ | ✓ |
| Z. 666–668 | ue1: C = ε₀A/d | 2,656·10⁻¹⁰ F = 265,6 pF | 2,6562·10⁻¹⁰ F | ✓ |
| Z. 668 | ue1: Faktor bis 1 µF | „fast viertausendfach“ | 3 765 | ✓ |
| Z. 698–701 | ue2: Q = C·U | 6,375 nC | 6,3749 nC | ✓ |
| Z. 701 | ue2: E = U/d; n = Q/e | 48 kV/m; 3,98·10¹⁰ | 48 000 V/m; 3,979·10¹⁰ | ✓ |
| Z. 1158 | ue2: Fehlerwert C/U und Faktor 24² | 1,107·10⁻¹¹; 576 | 1,1068·10⁻¹¹; 576,0 | ✓ |
| Z. 792–795 | ue4: alle zwölf Kontrollzahlen (Q(A), E(d), W(U), Q(d)) | s. Datei | alle identisch | ✓ |
| Z. 829–834 | ue5: C = 2W/U²; A = C·d/(ε₀ε_r) | 8,0·10⁻⁷ F; 2,01 m² | 8,0·10⁻⁷ F; 2,0079 m² | ✓ |
| Z. 834 | ue5: √A; Streifenlänge; E in der Folie | 1,42 m; 40,2 m; 0,50 MV/m | 1,417 m; 40,16 m; 5,0·10⁵ V/m | ✓ |
| Z. 864–871 | ue6: Q, W₁, U₂, W₂, ΔW | 20 nC · 2,0 · 400 V · 4,0 · 2,0 µJ | identisch | ✓ |
| Z. 872 | ue6: Gegenprobe d₁, E, F, F·Δd | 3,54 mm · 56,5 kV/m · 565 µN · 2,0 µJ | 3,5416 mm · 56,47 kV/m · 564,7 µN · 2,0000 µJ | ✓ |
| Z. 1036 | Lehrerteil: Fehlerergebnis „−1,0 µJ“ | −1,0 µJ | −1,0 µJ | ✓ |
| Z. 882/883 | ue7: Q und W bei 200 V / 400 V | 3,542 / 7,083 nC; 0,3542 / 1,4166 µJ | identisch | ✓ |
| Z. 897–901 | ue8: C′, Q′, W′, ΔQ (U fest) | 106,2 pF · 21,25 nC · 2,125 µJ · 17,71 nC | 106,248 pF · 21,2496 nC · 2,12496 µJ · 17,708 nC | ✓ |
| Z. 899 | ue8: W′, U′, E′ (Q fest) | 0,0590 µJ · 33,3 V · 1,67 kV/m | 0,05903 µJ · 33,333 V · 1 666,7 V/m | ✓ |
| Z. 901 | ue8: ΔQ·U und Zuwachs | 3,542 µJ; 1,771 µJ | 3,5416 µJ; 1,7708 µJ | ✓ |
| Z. 1046 | Differenzierung: Reihenschaltung d/2 Glas | 30,36 pF gegen 106,25 pF | 30,357 pF; 106,248 pF | ✓ |
| Z. 1022–1026 | Lehrerteil: erwartete Messwerte | alle 15 Felder | Simulationsnachbau identisch | ✓ |

### Simulation gegen Handrechnung

Die Rechenkerne `rechne()` (Z. 1302–1310) und `feldlinienZahl()` (Z. 1312–1316) wurden in Python
nachgebaut und gegen eigene Handrechnungen geprüft.

| Zustand | Simulation | Handrechnung | Urteil |
|---|---|---|---|
| Start (200 V, 20 mm, 20 cm, Luft) | C 17,71 pF · Q 3,542 nC · U 200,0 V · E 10,00 kV/m · W 0,3542 µJ | C = ε₀A/d = 17,708 pF; Q = CU = 3,5416 nC; E = U/d = 10 kV/m; W = ½CU² = 0,35416 µJ | ✓ |
| d = 40 mm, angeschlossen | 8,85 pF · 1,771 nC · 200,0 V · 5,00 kV/m · 0,1771 µJ | identisch | ✓ |
| d = 40 mm, abgetrennt | 8,85 pF · 3,542 nC · 400,0 V · 10,00 kV/m · 0,7083 µJ | U = Q/C = 400 V; E = Q/(ε₀A) = 10 kV/m; W = Q²/2C = 0,70832 µJ | ✓ |
| Durchschlagsrezept des Lehrerteils (Glas, L = 30, d = 5, 500 V → abtrennen → Luft → L = 10) | E = 5 400 kV/m, Meldung erscheint | Q = 478,1 nC; C = 17,708 pF; U = 27 000 V; E = 5,40·10⁶ V/m > 3·10⁶ V/m | ✓ |
| U = 0 | n = 0 Feldlinien, „U = 0: kein Feld“, keine Division durch null | E = 0 | ✓ |

Weitere geprüfte Details der Simulation:

- **Maßstab Pixel ↔ Physik:** PX_D = 5 px/mm waagerecht gegen PX_L = 10 px/cm = 1 px/mm senkrecht
  – die Beschriftung „Plattenabstand fünffach überhöht“ (Z. 1544) stimmt. Die beiden
  Maßstabsbalken (50 px für 10 mm bzw. 50 px für 5 cm, Z. 1537–1543) sind beide korrekt.
- **Ziehen der Platte:** `d = round(|x − XM| · 2 / PX_D)` (Z. 1416) ist die exakte Umkehrung von
  `halb = PX_D · d/2` (Z. 1459). ✓
- **Homogenitätswarnung:** `z.d > z.L` (Z. 1336) prüft mm gegen cm und kodiert damit genau
  d > L/10 – passend zur Faustregel in 3.1 (Z. 385). ✓ Elegant und richtig.
- **Durchschlagsmeldung:** Sie spricht von Luft. Eine Vollsuche über alle erreichbaren Zustände
  zeigt: Die größte einfrierbare Ladung ist 478,1 nC, und E > 3 MV/m ist damit **nur** bei
  ε_r = 1 erreichbar (Papier höchstens 2,46 MV/m, Glas höchstens 0,90 MV/m). Die Meldung kann
  also nie fälschlich bei eingelegtem Dielektrikum erscheinen. ✓ Sehr sorgfältig.
- **Feldliniendichte:** n/h = E/400 000 je Pixel, unabhängig von L – die Liniendichte ist damit
  korrekt proportional zu E, und der Vergleich innerhalb eines Bildes (Regel 4 in 2.4) trägt. ✓
- **Diagramme:** Das Energiedreieck in `zeichneQU()` (Z. 1618–1623) hat die Katheten U und Q, die
  Hypotenuse fällt mit der Geraden Q = C·U zusammen – die Fläche ist tatsächlich ½QU. In der
  Betriebsart „abgetrennt“ dreht sich die Gerade um den Ursprung, während der Arbeitspunkt auf
  der Waagerechten „Q bleibt fest“ wandert. Das ist die physikalisch richtige Darstellung. ✓
- **Engine-Verträge:** 6 MC-Blöcke, Optionszahl = Zahl der Rückmeldungstexte (3/3/3/4/3/4),
  `data-i` lückenlos, Radio-Namen eindeutig. 433 Formeln, alle mit `data-plain`. Im Fließtext
  kein Dezimalpunkt (die Treffer „2.4“, „3.7“ usw. sind Abschnittsnummern). Kein Siezen.

---

## Bestanden / gut gelöst

**Lehrplanbezug – geprüft und einwandfrei.**
Der Chip (Z. 190) nennt „Inhaltsfeld: Ladungen, Felder und Induktion“ **wörtlich** so, wie es in
`fachliches/kernlehrplan-nrw.md` Zeile 15 steht. Die Zuordnung zur Q1 ist korrekt (Inhaltsfeld 1
liegt laut Zeile 21 in der Q1). Die im Lehrerteil (Z. 992) genannten Kompetenzbereiche „Umgang
mit Fachwissen · Erkenntnisgewinnung · Kommunikation · Bewertung“ decken sich wörtlich mit
Zeile 24 der Referenz. **Kein einziges erfundenes Zitat.** Vorbildlich ist der Block ab Z. 995:
Was didaktische Setzung und nicht Vorgabe des Kernlehrplans ist (Reihenfolge, Aufteilung auf die
Folgemodule, Verzicht auf die mikroskopische Polarisation), wird ausdrücklich als solche
markiert – genau das verlangt `CLAUDE.md`. Das sollte für alle weiteren Module übernommen werden.

**Anforderungsbereiche.** Eigene Einstufung: ue1 I · ue2 I · ue3 I–II (siehe M6) · ue4 II ·
ue5 II · ue6 II · ue7 III · ue8 III · ue9 III. Bis auf ue3 stimmt die Auszeichnung. Die drei
AB-III-Aufgaben sind **echte** Bewertungsaufgaben und keine verlängerten Rechnungen: ue7
beurteilt eine Analogie, ue8 verlangt eine Fallunterscheidung mit Energiebilanz, ue9 ist eine
wissenschaftstheoretische Stellungnahme. Alle drei haben Musterlösung **und**
Bewertungskriterien (Z. 886, 902, 918), und die Kriterien sind operationalisiert
(„Faktor 4 mit Zahlenwerten belegt“), nicht floskelhaft. Das ist LK-Niveau.

**Besonders gelungen und zur Übernahme empfohlen:**

- Die **Energiebilanzen** gehen jedes Mal exakt auf und werden auch vorgerechnet: F·Δd = ΔW in
  3.7 (Z. 545), die Doppelrechnung über Energie und Kraft in ue6 (Z. 872), und in ue8 der
  Zusatz, dass die Quelle 3,542 µJ liefert, aber nur 1,771 µJ im Feld landen (Z. 901). Der
  letzte Punkt ist inhaltlich anspruchsvoll und korrekt – viele Schulbücher lassen ihn weg.
- Die **Nebenformel E = σ/(ε₀ε_r)** wird hergeleitet (Z. 452–464) und danach überall dort
  benutzt, wo die Ladung festgehalten wird. Damit ist die Fallunterscheidung in 3.7 nicht nur
  auswendig zu lernen, sondern begründet.
- Die **Distraktor-Rückmeldungen** benennen durchgehend den Denkfehler und nennen oft sogar den
  Zahlenwert, auf den der Fehler führt (vw1: „3 + 3 = 6 statt 3 · 3 = 9“; sim2: „ein Faktor 4 –
  das sind keine Rundungseffekte“; ue2: „Faktor 576 = 24²“). Kein einziges „Leider falsch“.
- Die **Hilfestufen** sind echt abgestuft: Der Tipp nennt nie die Formel (ue5: „Das ist keine
  Aufgabe, sondern zwei“), der Ansatz nennt die Formel ohne Zahlen, der Lösungsweg rechnet mit
  Einheitenprobe und Einordnung.
- Der **Lehrerteil** ist kein Allgemeinplatz-Text: neun typische Schülerfehler, jeweils mit
  einer konkreten Stelle zum Anhalten und einer Tafelhandlung; Schnittstellen für Doppel- oder
  Einzelstunden; eine Pflichtaufgabenauswahl für beide Differenzierungsrichtungen; sieben
  Realexperimente mit Aufwand und Stolperstellen (die Bemerkung zur feuchten Luft und zum
  Streufeld, das ε₀ um 10 bis 20 % zu hoch misst, verrät Praxiserfahrung).
- Die **Kommentare im Simulations- und Prüfcode** (Z. 1185–1188, 1202–1205) dokumentieren zwei
  bereits behobene Fallen – Toleranz in der Alternativeinheit und Bezugsgröße für die
  „nah/weit“-Entscheidung. Solche Notizen gehören in jedes Modul.
- Der Kondensator wird über **sechs Zehnerpotenzen** durchgehalten: Touchscreen (pF) im
  Einstieg, Simulationswerte (pF), Folienkondensator (nF, ue5), Defibrillator (µF). Die Seite
  hat dadurch einen roten Faden statt einer Aufgabensammlung.

---

## Kurzfazit

**Urteil: Nacharbeit nötig.**

Fachlich ist dieses Modul auf ungewöhnlich hohem Niveau: Ich habe über vierzig Zahlenwerte
einzeln nachgerechnet, darunter jede Musterlösung, jede Zwischengröße und jede Kontrollzahl der
Zuordnungsaufgabe, und **kein einziger Rechenwert ist falsch**; auch der Simulationskern liefert
in allen geprüften Zuständen exakt das, was die Handrechnung ergibt. Nachgearbeitet werden muss
trotzdem an zwei Stellen: die Größenordnungsangabe im Einstieg ist um den Faktor 100 daneben
(B1), und die dreimal wiederholte Begründung für die Homogenität des Feldes ist physikalisch
falsch und widerspricht dem eigenen Lehrerteil (B2) – letzteres wiegt schwerer, weil die
Lehrkraft ausdrücklich angehalten wird, das falsche Argument mit dem Kurs zu entwickeln. Die
sieben Mängel sind allesamt in einer Arbeitssitzung zu beheben; am wichtigsten sind der
zweideutige Beobachtungsauftrag (M1) und Aufgabe 6, in der die unvollständige Lösung als richtig
durchgeht (M4). Sind B1, B2, M1 und M4 erledigt, kann die Seite ohne weitere Vorbehalte in den
Unterricht – bis dahin bleibt der Eintrag in `fachliches/modulliste.md` zu Recht auf „in Arbeit“.
