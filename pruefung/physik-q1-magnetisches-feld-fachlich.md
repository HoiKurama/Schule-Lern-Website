# Prüfbericht: physik-q1-magnetisches-feld.html

Prüfdatum: 07.09.2026 · Fachprüfung Physik LK Q1
Geprüfte Datei: `module/physik-q1-magnetisches-feld.html` (2128 Zeilen)
Referenzen: `inhalte/physik-q1-magnetisches-feld.md`, `fachliches/kernlehrplan-nrw.md`,
`module/physik-q1-induktion.html`
Werkzeuge: Python 3.13 (Nachrechnung), Playwright/Chromium (Simulation ausgelesen und
Boris-Integrator Zeile für Zeile in Python nachgebaut).

## Urteil

**Nacharbeit nötig.**

Der Erklär- und Übungsteil ist fachlich in Ordnung; sämtliche Musterlösungen sind nachgerechnet
und stimmen. Der Modus 1 der Simulation (Kreisbahn) ist korrekt und trägt die zentrale didaktische
Aussage sauber. **Modus 2 (Wien-Filter) ist dagegen unbrauchbar in der Form, in der er beschrieben
wird**: Die gewählte Geometrie lässt das Teilchen im Filter mehr als einen vollen Zyklotronumlauf
machen, dadurch ist die Durchlassbedingung weder scharf noch eindeutig, und drei ausdrückliche
Aussagen des Moduls über den Filter sind am Bildschirm nachprüfbar falsch. Dazu kommt, dass der
Beobachtungsauftrag Teil C durch das automatische Zurücksetzen des B-Reglers nicht ausführbar ist.

## Schwere Fehler

### S1 — Der B-Regler springt beim Teilchenwechsel, Beobachtungsauftrag Teil C ist nicht ausführbar

Fundstelle: Zeile 663 (Beobachtungsauftrag Teil C), Zeile 767 (sim2), Zeilen 2014–2027
(`setzeBRegler`, Handler von `selTeilchen`).

Der Auftrag lautet wörtlich: „Stelle *Proton*, **B = 200 mT**, **U = 450 V** ein und schiebe U_P,
bis das Proton durch die Blende geht. Ändere jetzt **nichts** am Filter, sondern wechsle auf
*Alphateilchen*."

Der Änderungs-Handler von `selTeilchen` ruft `setzeBRegler()` auf; dort steht
`rB.value = t.bstart`. Beim Wechsel von `proton` (bstart 130) auf `alpha` (bstart 185) wird der
B-Regler also **zwangsweise** von 200 mT auf 185 mT gestellt. Im Browser nachgemessen:

| | B-Regler | U | U_P | Status | ε |
|---|---|---|---|---|---|
| Proton eingestellt | 200 mT | 450 V | 1174 V | kommt durch | −0,039 % |
| nach Wechsel auf Alpha | **185 mT** | 450 V | 1174 V | von der Platte verschluckt | +52,3 % |

Der Filter hat sich also sehr wohl geändert. Die Schülerin, die der Anweisung folgt, findet
anschließend nicht die im Modul genannten 890 V, sondern rund 1040 V (bei B = 185 mT ist
v_d = 1174 V/(0,0200 m · 0,185 T) = 317,3 km/s). Damit ist auch die Prämisse der Verständnisfrage
sim2 („dieselbe Filtereinstellung (B = 200 mT, U_P = 1174 V) ließ sowohl das Proton bei U = 450 V
als auch das Alphateilchen bei U = 890 V durch") am Gerät nicht reproduzierbar — genau die
Beobachtung, auf der die ganze Aufgabe steht.

**Korrekturvorschlag:** `setzeBRegler()` soll den bisherigen Zahlenwert beibehalten und nur in den
neuen Bereich klemmen, statt auf `bstart` zu springen:
`rB.value = Math.min(t.bmax, Math.max(t.bmin, alterWert));` — 200 mT liegt in beiden Bereichen
(Proton 110–300, Alpha 150–420), der Wechsel wäre dann tatsächlich neutral. Alternativ im
Wien-Modus einen eigenen, teilchenunabhängigen B-Regler verwenden.

### S2 — Der Wien-Filter der Simulation filtert nicht: zweites Durchlassfenster bei 25 % falscher Geschwindigkeit

Fundstelle: Zeilen 1604–1613 (Geometrie), 1707–1741 (`integriereWien`), dazu die Textaussagen in
Zeile 566, Zeile 570 (Merksatz) und Zeile 741.

Der Boris-Integrator selbst ist **richtig** implementiert (halber E-Stoß, magnetische Drehung,
halber E-Stoß; Vorzeichen von E_y = −E und B_z = −B passen zur Konvention des Moduls). Falsch ist
die **Geometrie**: Die Platten sind L = 10,0 cm lang, der Zyklotronradius des Protons beträgt bei
B = 200 mT und U = 450 V aber nur r = 1,53 cm. Das Teilchen legt im Filter **1,04 volle
Zyklotronumläufe** zurück. Die Bahn ist damit keine schwach gekrümmte Parabel, sondern eine
Zykloide, die periodisch auf die Achse zurückkehrt.

Ich habe den Integrator des Moduls in Python nachgebaut und den Plattenspannungsbereich
durchgefahren (Proton, U = 450 V, B = 200 mT, Blende ± 4,0 mm):

| U_P | ε | y am Schirm (Code) | Status |
|---|---|---|---|
| 792 … 958 V | **−32,6 % … −18,4 %** | ≤ 4 mm | **kommt durch** |
| 1132 … 1262 V | −3,6 % … +7,5 % | ≤ 4 mm | kommt durch |
| sonst | | > 4 mm | verfehlt die Blende |

Es gibt also ein **zweites Durchlassfenster**, in dem ein Proton mit bis zu 25 % falscher
Geschwindigkeit die Blende trifft. Das widerlegt am Bildschirm genau den Merksatz, den die
Simulation stützen soll: „Nur das Passende trifft die Austrittsblende" (Zeile 566) und
„sortiert … **ausschließlich nach Geschwindigkeit**" (Zeile 570).

**Korrekturvorschlag:** Den Filter im Regime L ≪ r betreiben, wie es die Lehrbuchbeschreibung
voraussetzt. Konkret: die Plattenlänge auf 2 cm verkürzen **oder** B im Wien-Modus um etwa den
Faktor 10 senken (bei B = 20 mT ist r = 15,3 cm ≫ L). Dann wächst die Ablenkung monoton mit |ε|,
das zweite Fenster verschwindet, und die Textaussagen stimmen wieder. Die Voraussetzung
„Ablenkung klein gegen den Zyklotronradius" gehört zusätzlich als Satz in den Erklärteil.

### S3 — Die Ablenkrichtung im Wien-Modus wechselt das Vorzeichen, entgegen der Textaussage

Fundstelle: Zeile 566 („Alles, was schneller ist, hat eine zu große Lorentzkraft und wird zur
einen Seite abgelenkt; alles Langsamere folgt der elektrischen Kraft zur anderen.") gegen
`integriereWien`, Zeilen 1707–1741.

Aus derselben Ursache wie S2: Weil die Bahn eine Zykloide ist, hängt das Vorzeichen der Ablenkung
am Schirm nicht mehr am Vorzeichen von ε, sondern an der Zykloidenphase beim Plattenaustritt.
Nachgemessen (Proton, U = 450 V, B = 200 mT):

| U_P | ε | y am Schirm |
|---|---|---|
| 1200 V | +2,17 % | **−0,53 mm** |
| 1250 V | +6,43 % | **+2,38 mm** |

Gleiches Vorzeichen von ε, entgegengesetzte Ablenkrichtung. Die Schülerin, die dem Text glaubt
und aus der Ablenkrichtung auf „zu schnell" oder „zu langsam" schließt, wird von der Simulation
in die Irre geführt. Behebt sich mit derselben Maßnahme wie S2.

### S4 — Die Toleranzangabe „ungefähr ein Drittel Prozent" ist falsch

Fundstelle: Zeile 741, Bedienhinweis zum Wien-Modus: „Wie klein ‚klein genug' ist, findest du
selbst heraus — der Filter verzeiht ungefähr ein Drittel Prozent."

Gemessen verzeiht der Filter im Hauptfenster **−3,6 % bis +7,5 %**, also rund das
Zwanzigfache. Für das Alphateilchen bei fester Filtereinstellung (B = 200 mT, U_P = 1174 V) kommen
**alle** Beschleunigungsspannungen von U = 700 V bis U = 1210 V durch — der Auftrag „Finde durch
Probieren die Spannung U, bei der auch das Alphateilchen durchkommt" (Zeile 663) hat also gar
keine eindeutige Antwort, sondern 52 Reglerstellungen. Die im Modul genannten 890 V (Zeilen 767,
1089) sind nur eine davon; die exakte Anpassung läge bei 893 V.

**Korrekturvorschlag:** Nach der Geometriekorrektur aus S2 die tatsächliche Toleranz neu bestimmen
und in Zeile 741 eintragen; den Auftrag in Teil C auf „stelle ε so klein wie möglich ein" umformulieren,
damit er eine eindeutige Antwort hat.

## Mängel

### M1 — Abweichung von der abgenommenen Inhaltsdatei bei den Filterwerten

Fundstelle: `inhalte/physik-q1-magnetisches-feld.md`, Zeilen 1030–1049 und 1146–1148, gegen die
Anzeige `#aY` des Moduls.

Die Inhaltsdatei gibt für Modus 2 die Kontrollformel
`y_Schirm = (q/m) · B · (v − v_d) · L · (L/2 + D) / v²` vor und fordert als Abnahmeprobe, dass
der integrierte Endwert damit „auf **besser als 1 %**" übereinstimmt (Zeile 1047 f.). Gemessen:

| Fall | Inhaltsdatei (K-21) | Modul (Browser) | Faktor |
|---|---|---|---|
| Proton, U = 450 V, U_P = 1174 V | y = +0,72 mm | **+0,02 mm** | 33 |
| Alphateilchen, U = 890 V, U_P = 1174 V | y = −1,64 mm | **−0,05 mm** | 33 |

Die Abnahmeprobe ist klar verfehlt. Ursache ist nicht der Integrator, sondern die Kontrollformel:
Sie unterstellt eine Parabelbahn und gilt nur für L ≪ r, was hier verletzt ist (siehe S2). Der
Befund gehört trotzdem in den Bericht, weil die Inhaltsdatei die Referenz ist — beide Seiten
müssen zusammengeführt werden, und zwar über die Geometriekorrektur, nicht über eine Anpassung
der Zahlen.

### M2 — Zwischenwerte folgen nicht aus den angegebenen Konstanten

Fundstellen: Zeilen 819 und 824 (ue1), 856 und 858 (ue2), 899 f. (ue3), 1083 (ue6), 1133 (ue7),
Tabelle Zeilen 621–629.

Die „Gegeben"-Zeilen nennen gerundete Konstanten (e = 1,602·10⁻¹⁹ C, m_p = 1,673·10⁻²⁷ kg,
m_e = 9,109·10⁻³¹ kg), gerechnet wurde aber durchweg mit CODATA-Werten. Wer die Rechnung mit den
angegebenen Zahlen nachvollzieht, bekommt in der vierten Stelle etwas anderes:

| Stelle | Datei | mit den angegebenen Konstanten |
|---|---|---|
| ue2, Zähler 2π·m_p | 1,0510·10⁻²⁶ | 1,0512·10⁻²⁶ |
| ue2, Nenner e·B | 2,0828·10⁻²⁰ | 2,0826·10⁻²⁰ |
| ue2, Ergebnis | 504,6 ns | **504,7 ns** |
| ue1, Radius | 3,554·10⁻² m | 3,5547·10⁻² m, gerundet 3,555 |
| ue3, Zähler | 1,2112·10⁻²³ | 1,2111·10⁻²³ |
| ue3, Ergebnis | 13 297 km/s | 13 296 km/s |
| Tabelle Z. 625, Proton | 9,579·10⁷ C/kg | 9,576·10⁷ C/kg |
| Tabelle Z. 628, Ne-22 | 4,386·10⁶ C/kg | 4,385·10⁶ C/kg |

Fachlich sind die Dateiwerte die genaueren, und alle Endergebnisse liegen innerhalb der
Eingabetoleranz. Der Mangel ist didaktisch: Der Lehrerteil verlangt in Zeile 1358 ausdrücklich,
dass „in Hilfe 3 jeder Zwischenwert **mit Einheit** notiert wird" — dann muss der Zwischenwert
auch aus den genannten Konstanten folgen. **Korrektur:** entweder die genaueren Konstanten in den
„Gegeben"-Zeilen nennen oder die Zwischenwerte mit den gerundeten neu rechnen.

### M3 — Die Rückmeldung zu ue1 nennt eine falsche Startstellung der Simulation

Fundstelle: Zeile 1471, `numDaten.ue1.ok`: „… r = 3,55 cm. **Das ist genau die Startstellung der
Simulation** — stell sie ein und miss den Kreis am Maßstabsbalken nach."

Die Simulation startet mit U = 450 V und B = 3,0 mT (Zeilen 719 und 723); das ergibt r = 2,38 cm,
nicht 3,55 cm (im Browser nachgemessen). Die 3,55 cm bekommt man erst bei U = 1000 V.
**Korrektur:** „Stell in der Simulation U = 1000 V und B = 3,0 mT ein und miss nach."

### M4 — Die Aufgaben tragen keine sichtbare Nummer

Fundstellen: alle `.aufgabe`-Blöcke ab Zeile 785; zwanzig Textverweise, unter anderem Zeile 824
(„in Aufgabe 5"), 1025 und 1076 („in Aufgabe 1"), 1149, 1156 („Fortsetzung von Aufgabe 7"),
1283–1285 und der gesamte Lehrerteil.

Im Kopf jeder Aufgabe steht nur der Anforderungsbereich. Die Schülerin muss durchzählen, und das
Zählen ist nicht offensichtlich, weil die Zuordnungsaufgabe (ohne Nummer und ohne das Wort
„Aufgabe") als Aufgabe 4 zählt. Das Referenzmodul hat dieselbe Bauweise, dort aber sieben
Aufgaben und kaum Querverweise; hier sind es zehn Aufgaben und zwanzig Verweise.
**Korrektur:** die Nummer in den AB-Chip aufnehmen, etwa „Aufgabe 5 · Anforderungsbereich II".

### M5 — Die 890 V des Alphateilchens folgen aus keiner der genannten Begründungen

Fundstellen: Zeile 767 (sim2), Zeile 1089 (ue6, Hilfe 3), Zeile 663 (Beobachtungsauftrag Teil C).

Zeile 1089 begründet: „das wäre bei U = 890 V der Fall, denn es hat die doppelte Ladung und die
vierfache Masse". Mit exakt vierfacher Masse ergäbe die Rechnung
U_alpha = U_p · m_alpha / (2 · m_p) = 450 V · 4/2 = **900 V**; mit der wirklichen Alphamasse
(3,972 · m_p) sind es **894 V**. Die Datei nennt 890 V — plausibel als Reglerwert (Schrittweite
10 V), aber die angegebene Begründung führt nicht dahin. **Korrektur:** „bei U = 894 V, am Regler
also 890 V" schreiben und mit der tatsächlichen Alphamasse begründen.

### M6 — ue10 a) ist Reproduktion, nicht Anforderungsbereich III

Fundstelle: Zeilen 1208–1213, Musterlösung 1218–1221.

Teilaufgabe a) („Begründe, warum die Umlaufdauer trotzdem bei jedem Umlauf dieselbe bleibt")
verlangt exakt die Herleitung, die im Erklärteil zwei Bildschirmseiten vorher vollständig
dasteht — einschließlich des anschaulichen Satzes über Umfang und Geschwindigkeit (Zeilen
474–481). Die Musterlösung wiederholt ihn wörtlich. Das ist AB I bis II; das AB-III-Niveau der
Aufgabe trägt allein c). **Korrektur:** a) auf einen Transfer umstellen, zum Beispiel „Begründe,
warum man aus demselben Grund kein Zyklotron für Elektronen baut".

### M7 — ue3 ist als Anforderungsbereich I ausgezeichnet

Fundstelle: Zeile 872, „Anforderungsbereich I (mit Auswertungsschritt)".

Die Aufgabe verlangt, eine Formel umzustellen, einen Messwert (Durchmesser) in die passende Größe
(Radius) zu überführen und zu erkennen, dass die fehlende Spannung nicht gebraucht wird. Das ist
Anwenden in verändertem Zusammenhang, also AB II; der Klammerzusatz ist ein Notbehelf.
**Korrektur:** auf AB II heraufstufen. Die Verteilung bliebe mit 2 × I, 6 × II, 3 × III tragfähig.

### M8 — Stufe 1 der Hilfen nimmt bei ue3 und ue7 den Denkschritt vorweg

Fundstellen: Zeile 891 und Zeile 1116.

ue3, Tipp: „Zwei Fallen in einem Satz: Der Maßstab misst den Durchmesser, nicht den Radius — und
die Beschleunigungsspannung brauchst du für diesen Weg überhaupt nicht." Damit sind genau die
beiden Hürden benannt, die der Abiturhinweis in Zeile 1283 als *die* Stolpersteine ausweist.
ue7, Tipp: „Das schwerere Ion ist nicht nur träger, es ist auch langsamer … Und: Der Detektor
sieht nicht die Radien, sondern die Durchmesser." Das ist die halbe Lösung.
**Korrektur:** Stufe 1 auf eine Rückfrage reduzieren („Was hast du gemessen, und was steht in der
Formel?"), die Auflösung nach Stufe 2 verschieben. Bei ue1, ue2, ue5 und ue6 ist die Abstufung
dagegen vorbildlich.

### M9 — Punkt als Dezimaltrenner im Eingabehinweis

Fundstelle: Zeile 1004: „Eingabehinweis: Schreib den Wert wissenschaftlich, zum Beispiel
1.76e11." Widerspricht der Projektregel „Komma als Dezimaltrennzeichen". Die Prüfroutine
akzeptiert auch das Komma, weil sie es vor dem Parsen ersetzt.
**Korrektur:** „zum Beispiel 1,76e11 (der Punkt geht auch)".

### M10 — Die Simulation reicht nicht bis zu den Aufgabenwerten

Fundstelle: Zeile 719, Regler `rU` mit `max="1800"`. Die Vertiefung (Zeile 596) und ue7 rechnen
mit U = 2,00 kV; das lässt sich am Regler nicht einstellen, obwohl der Text an mehreren Stellen
zum Nachstellen einlädt (Zeilen 1471, 1494, 1362). **Korrektur:** `max="2500"`. Der größte Kreis
wäre dann Ne-20 bei 480 mT mit r = 6,4 cm = 160 px und passte noch ins Bild (Quellpunkt bei
y = 320 px, unterer Rand bei 640 px).

### M11 — Kleinigkeit: Rundung im Beobachtungsauftrag

Die Anzeige rundet r auf zwei Nachkommastellen: 2,38 cm bei 450 V, 4,77 cm bei 1800 V. Wer den
Faktor exakt 2 erwartet, findet 2,004. Ein Halbsatz im Auftrag („die Anzeige rundet") fängt die
Rückfrage ab.

## Nachgerechnet

Alle Werte mit Python nachgerechnet (Skripte im Arbeitsordner), die Simulationswerte zusätzlich
per Playwright aus dem laufenden Modul ausgelesen. „mein Wert" ist mit den CODATA-Konstanten
gerechnet, die auch die Simulation benutzt.

### Erklärteil und Vertiefung

| Zeile | Größe | Datei | mein Wert | Urteil |
|---|---|---|---|---|
| 272 | F = 0,25 T · 3,5 A · 0,120 m | 0,105 N | 0,105 N | ✔ |
| 466 | v (Elektron, 1000 V) | 1,876·10⁷ m/s | 1,87554·10⁷ m/s | ✔ |
| 467 | r (Elektron, 1000 V, 3,00 mT) | 3,55·10⁻² m | 3,5545·10⁻² m | ✔ |
| 468 | Kreisdurchmesser | 7,1 cm | 7,109 cm | ✔ |
| 470 | v/c | rund 6 % | 6,26 % | ✔ |
| 489 | 200 V: v / r / T | 8 388 km/s · 1,59 cm · 11,91 ns | 8 387,4 · 1,5897 · 11,9088 | ✔ |
| 490 | 800 V: v / r / T | 16 775 km/s · 3,18 cm · 11,91 ns | 16 774,7 · 3,1794 · 11,9088 | ✔ |
| 491 | 2000 V: v / r / T | 26 524 km/s · 5,03 cm · 11,91 ns | 26 523,2 · 5,0270 · 11,9088 | ✔ |
| 500 | f_c Elektron bei 3,00 mT | 84,0 MHz | 83,97 MHz | ✔ |
| 500 | f_c Proton bei 3,00 mT | 45,7 kHz | 45,72 kHz | ✔ |
| 500 | Massenverhältnis p/e | 1836 | 1836,15 | ✔ |
| 566 | v = 1,2·10⁴ / 4,0·10⁻³ | 3000 km/s | 3000,0 km/s | ✔ |
| 594 | √(22/20) | 1,0488 | 1,04881 | ✔ |
| 602 | 2r (Ne-20, 2 kV, 600 mT) | 9,598 cm | 9,5987 cm | ✔ |
| 603 | 2r (Ne-22) | 10,067 cm | 10,0672 cm | ✔ |
| 604 | Differenz | 0,469 cm | 0,4685 cm | ✔ |
| 609 | Radiusunterschied bei 10 % Masse | 4,9 % | 4,881 % | ✔ |
| 623 | |q|/m Elektron | 1,759·10¹¹ C/kg | 1,7588·10¹¹ | ✔ |
| 625 | |q|/m Proton | 9,579·10⁷ C/kg | 9,5788·10⁷ (CODATA) / 9,576·10⁷ (Dateikonstanten) | ✔ / M2 |
| 626 | |q|/m Alphateilchen | 4,822·10⁷ C/kg | 4,8225·10⁷ | ✔ |
| 627 | |q|/m Ne-20 | 4,824·10⁶ C/kg | 4,8243·10⁶ | ✔ |
| 628 | |q|/m Ne-22 | 4,386·10⁶ C/kg | 4,3857·10⁶ (CODATA) / 4,385·10⁶ (Dateikonstanten) | ✔ / M2 |
| 636 | Alpha rund halb so groß wie Proton | „ungefähr die Hälfte" | 0,504 | ✔ |

### Übungen

| Zeile | Größe | Datei | mein Wert | Urteil |
|---|---|---|---|---|
| 819 | ue1, Zwischenwert r | 3,554·10⁻² m | 3,5545·10⁻² m | ✔ (Rundung, M2) |
| 821 | **ue1 Ergebnis** | **3,55 cm** | **3,5545 cm** | ✔ |
| 856 | ue2, Zähler 2π·m_p | 1,0510·10⁻²⁶ | 1,05093·10⁻²⁶ | ✔ |
| 856 | ue2, Nenner e·B | 2,0828·10⁻²⁰ | 2,08283·10⁻²⁰ | ✔ |
| 858 | **ue2 Ergebnis T** | **504,6 ns** | **504,57 ns** | ✔ |
| 858 | ue2, f_c | 1,982 MHz | 1,98189 MHz | ✔ |
| 863 | ue2 Gegenprobe 1000 V | v 4,377·10⁵ · r 3,515 cm | 4,3769·10⁵ · 3,5149 cm | ✔ |
| 864 | ue2 Gegenprobe 200 V | v 1,957·10⁵ · r 1,572 cm | 1,9575·10⁵ · 1,5718 cm | ✔ |
| 900 | **ue3 Ergebnis v** | **13 297 km/s** | **13 296,7 km/s** | ✔ |
| 904 | ue3, v/c | 4,4 % | 4,435 % | ✔ |
| 905 | ue3, Rückrechnung U | 503 V | 502,9 V | ✔ |
| 1037 | ue5, r²·B² | 2,8388·10⁻⁹ | 2,83876·10⁻⁹ | ✔ |
| 1040 | **ue5 Ergebnis** | **1,761·10¹¹ C/kg** | **1,76133·10¹¹ C/kg** | ✔ |
| 1043 | ue5, Abweichung zum Literaturwert | +0,14 % | +0,144 % | ✔ |
| 1044 | ue5, m_e aus Millikan | 9,10·10⁻³¹ kg | 9,0954·10⁻³¹ kg | ✔ |
| 1081 | ue6, v (Proton, 450 V) | 2,936·10⁵ m/s | 2,93565·10⁵ m/s | ✔ |
| 1085 | **ue6 Ergebnis E** | **58,7 kV/m** | **58,715 kV/m** | ✔ |
| 1087 | ue6, U_P | 1174 V | 1174,3 V | ✔ |
| 1088 | ue6, F_el = F_L | 9,408·10⁻¹⁵ N | 9,4066·10⁻¹⁵ N | ✔ |
| 1132 | ue7, v₂₀ | 1,3891·10⁵ m/s | 1,38908·10⁵ | ✔ |
| 1133 | ue7, v₂₂ | 1,3245·10⁵ m/s | 1,32443·10⁵ | ✔ (Rundung) |
| 1138 | ue7, r₂₀ | 4,799 cm | 4,7993 cm | ✔ |
| 1139 | ue7, r₂₂ | 5,033 cm | 5,0336 cm | ✔ |
| 1141 | ue7, Δr | 2,342 mm | 2,3425 mm | ✔ |
| 1142 | **ue7 Ergebnis Δs** | **4,68 mm** | **4,685 mm** | ✔ |
| 1163 | ue8, Δs / Streifenbreite | 2,3 | 2,343 | ✔ |
| 1163 | ue8, freie Lücke | 3,7 mm | 3,685 mm | ✔ |
| 1166 | ue8, Δs bei 8,00 kV | 9,37 mm | 9,370 mm | ✔ |
| 1168 | ue8, Δs bei 900 mT | 3,12 mm | 3,123 mm | ✔ |
| 1194 | ue9, Umläufe pro Sekunde bei 3,0 mT | 84 Mio | 83,97 Mio | ✔ |
| 1224 | ue10, f_c und T (Proton, 1,5 T) | 22,9 MHz · 43,7 ns | 22,860 MHz · 43,744 ns | ✔ |
| 1231 | ue10, 1 MeV: γ / v/c / ΔT | 1,0011 · 0,046 · +0,11 % | 1,00107 · 0,0461 · +0,107 % | ✔ |
| 1232 | ue10, 10 MeV | 1,0107 · 0,145 · +1,07 % | 1,01066 · 0,1448 · +1,066 % | ✔ |
| 1233 | ue10, 20 MeV | 1,0213 · 0,203 · +2,13 % | 1,02132 · 0,2032 · +2,132 % | ✔ |
| 1237 | ue10, r für 20-MeV-Proton bei 1,5 T | 43 cm | 43,3 cm | ✔ |
| 1356 | Lehrerteil, linear gerechnet | 9,6 mm | 9,598 mm | ✔ |
| 1376 | Helmholtz N=130, R=0,150 m, I=2,05 A | B = 1,60 mT | 1,5975 mT | ✔ |
| 1376 | daraus 2r bei U = 250 V | 6,66 cm | 6,665 cm | ✔ |
| 1376 | I = 1,0 A | 2r = 13,7 cm | 13,684 cm | ✔ |
| 1443 | sim1-Rückmeldung, Bildschirm-Umlaufdauer | 2,38 s | 2,382 s (T · Z) | ✔ |
| 1446 | sim2-Rückmeldung, 450 eV gegen 1780 eV | „fast das Vierfache" | 3,956 | ✔ |
| 654 | Maßstabsbalken 125 px | 5 cm | 5,00 cm | ✔ |

