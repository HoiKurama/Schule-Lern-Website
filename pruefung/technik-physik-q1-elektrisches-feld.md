# Technikprüfung physik-q1-elektrisches-feld.html

## Schritt 1: werkzeug/modulcheck.py
- Blocker: 0, Mängel: 0.
- Zählung: 6 MC, 8 Zahleneingaben, 1 Zuordnung, 18 Hilfeknöpfe, 3 Musterlösungen, 433 Formeln.
- Regler (3): rU 0–500 (Schritt 10), rD 5–50, rL 10–30; alle ohne Fehler durchfahren.
- Export: "In die Zwischenablage kopiert." Druck: 0 Bedienelemente, 0 Lehrerteil, 14/14 Aufgaben.
- Querscrollen 1280/900/390: 0. Offline: 0 von 433 leer.

## Schritt 2: eigenes Skript (Konsole, Simulation, Ziehen, Offline, Scrollen)
- Konsole online: 0 Fehler, 0 pageerror (auch nach allen Interaktionen).
- Simulation: 2 Modi x 3 Materialien x alle Stufen der 3 Regler (rU 0-500, rD 5-50, rL 10-30): jeweils ohne NaN/Infinity/undefined, kein Punkt als Dezimalzeichen in den Anzeigen (Bestanden).
- Handrechnung: Start 17,71 pF / 3,542 nC / 10,00 kV/m / 0,3542 µJ stimmt. d=40 mm angeschlossen: 8,85 pF, 1,771 nC, 5,00 kV/m, 0,1771 µJ (Bestanden). d=40 mm abgetrennt: 8,85 pF, 3,542 nC, 400,0 V, 10,00 kV/m, 0,7083 µJ (Bestanden, Q und E konstant, W steigt).
- Ziehen (pointerdown/move/up mit pointerType touch): d folgt (x=520 -> 8 mm, x=500 -> 5 mm geklemmt, x=300 -> 50 mm geklemmt), nach pointerup keine Änderung mehr (Bestanden).
- Offline (jsdelivr abgebrochen): 433 .m im DOM = 433 im Markup, 0 leer, 0 mit LaTeX-Rest, kein \frac/\cdot im Text, alle mit data-plain. Nur "Failed to load resource" (erwartet).
- Querscrollen 1280/900/390: keines.
- Kleine Touchziele (<32 px): Range-Input 16 px hoch, Selects 36x19 px, Radios 13x17 px (Mangel, s. Ende).

## Schritt 3: Durchschlag und Canvas-Darstellung
- Durchschlag-Szenario aus Lehrerteil (Glas, L=30, d=5, 500 V, abtrennen, Luft, L=10): Q=478,116 nC, U=27000 V, E=5400 kV/m, Meldung "Funke überschlagen" und Feldlinienfarbe orange erscheinen (Bestanden). Rechnung stimmt (6·ε0·0,09/0,005·500 = 478 nC).
- Diagrammwerte nachgerechnet: Glas, L=30, d=5, 500 V -> C=956,23 pF, W=119,5290 µJ (Bestanden). Achsen wachsen mit (Q-Achse 1 nC bei 200 V/Luft, 1000 nC bei Glas), Punkt bleibt im Bild.
- Mangel M1 (Canvas cvKond, Zeile 1512): Beschriftung "ε_r = 6,00" zeigt den Unterstrich literal ("ε_r") statt tiefgestelltem r, und sie liegt bei L=30 cm, d=5 mm auf der untersten Feldlinie/Plattenunterkante (Überlappung, schwer lesbar). Screenshot shots/k_b.png.
- Mangel M2 (cvKond): Bei L=30 cm reichen Platten und "+U"/"0 V"-Beschriftung bis fast an den oberen Canvasrand (Beschriftung bei y~10 px), und bei schmalem d (5 mm) sind "+U" und "0 V" dicht beieinander. Kosmetisch.
- Mangel M3 (cvCd): Beschriftung "956,23 pF bei 5 mm" liegt bei d=5 mm auf der Kurve. Kosmetisch.
- Hinweis: Bei abgetrennter Quelle zeigt das Reglerlabel "27000 V", der Regler selbst geht nur bis 500 (durch "(folgt aus Q)" erklärt, kein Fehler).

## Schritt 4: Darstellung, Druck, Regeltreue
- Screenshots (Ablage: C:/Users/49176/AppData/Local/Temp/claude/C--Users-49176-Documents-Claude-Projects-Schule/e67708d5-877c-4b65-8d0e-d553a557c247/scratchpad/shots/): sim_1280.png, sim_900.png, sim_390.png, k_a/k_b/k_c.png, cd_*.png, qu_*.png, print.png, modulcheck-Bilder *-1280/900/390.png.
- 1280 px: Simulation sauber, Beschriftungen lesbar, Feldlinien erkennbar.
- Mangel M4 (390 px): Die drei Canvas werden auf ca. 350 px verkleinert; Canvas-Beschriftungen (Achsen, "17,71 pF bei 20 mm", Legende, Maßstab) erscheinen dadurch nur ca. 4-5 px hoch und sind auf dem Handy nicht lesbar (sim_390.png). Empfehlung: größere Canvas-Schrift oder höhere Canvas bei schmalem Viewport.
- Mangel M5 (Touchziele): Bereichsregler 16 px hoch, Selects im Zuordnungsteil 36x19 px, Radios 13x17 px; Buttons/Optionen selbst ausreichend groß. Die Ziehfläche der Platten (24 Canvas-Pixel Toleranz) entspricht bei 390 px nur ca. 8 CSS-Pixeln, das Ziehen mit dem Finger ist dort schwer zu treffen (Regler bleiben als Alternative).
- Druck: Bedienelemente 0, Lehrerteil 0, alle 14 Aufgaben sichtbar; Regler/Knöpfe der Simulation ausgeblendet, Canvas und Anzeigen bleiben (Bestanden).
- Regeltreue per Textsuche: kein localStorage/sessionStorage/Cookie, keine externen Verweise außer jsdelivr/KaTeX, keine TODO/Lorem, kein englischer Text gefunden, kein Punkt als Dezimaltrenner in Anzeigen (Bestanden).

## Kurzfazit
Urteil: bestanden mit kleinen Mängeln (Nacharbeit optional).
Blocker: keine. modulcheck.py: 0 Blocker, 0 Mängel. Konsole fehlerfrei, 433/433 Formeln offline lesbar, 708 Simulationszustände ohne NaN, Handrechnungen und Durchschlag stimmen, Ziehen per Pointer-Events funktioniert, Druck korrekt, kein Querscrollen.
Mängel: M1 "ε_r" mit literalem Unterstrich und Überlappung im Canvas (Zeile 1512, besser "εr" oder Unicode-Tiefstellung und höhere Position), M2/M3 kosmetische Enge bei extremen Einstellungen, M4 Canvas-Schrift bei 390 px zu klein, M5 kleine Touchziele/Plattenziehfläche am Handy.
Das Modul wurde nicht verändert.
