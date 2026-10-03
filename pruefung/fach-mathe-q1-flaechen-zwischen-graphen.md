# Fachprüfung `module/mathe-q1-flaechen-zwischen-graphen.html`

Prüfer: fachpruefung. Bericht von der Hauptsitzung abgelegt (Agent darf keine Dateien schreiben); hier gekürzt auf Urteil und Mängel.

**Urteil: Nacharbeit nötig, eng umgrenzt.** Kein fachlicher Fehler: 46 Zahlenwerte mit sympy nachgerechnet (alle Musterlösungen, Einheitenumrechnungen, 45 SVG-Stützpunkte, 18 live ausgelesene Simulationszustände), alle richtig. Lehrplanbezug wörtlich belegt, a6/a7 echte AB-III-Aufgaben mit Bewertungskriterien, Engine und CSS bis auf Akzentfarben identisch zum Referenzmodul, `modulcheck.py` leer.

## Mängel

| Nr. | Schwere | Befund und Vorschlag |
|---|---|---|
| M1 | hoch | Lehrerteil Z. 828 verrät die Lösungen von sim1/sim2 (Ablesewerte 9,58 / 11,39 / 0,72; b₀ ≈ −0,376) und behauptet im selben Satz, sie stünden nirgends auf der Seite. Der `details.lehrer` ist im Browser aufklappbar. Z. 828 streichen; in Z. 827 „nirgends auf der Seite“ entfernen, Extremwerte des Beobachtungsauftrags dürfen bleiben. |
| M2 | mittel | `mcDaten.sim2.fb[2]` (Z. 881) nennt Flächeninhalt 3,61 und P = 1,81 bei b = −0,38; die Anzeige zeigt 3,59 und P = 1,79 (b₀ = −0,375987 ist nicht einstellbar, Raster 0,01). Lehrerteil Z. 799 nennt 3,59. Korrigieren: „3,59“ und „P = 1,79 – praktisch gleich N = 1,81“. |
| M3 | niedrig | Differenz-Plateau beginnt bei b = −0,37 (3,61), bei −0,38 zeigt das Feld 3,57. Z. 827 und Inhaltsdatei Z. 726–729 („für −0,38 ≤ b ≤ 2,00“) auf −0,37 ändern. |
| M4 | mittel | a2: −7,54 landet wegen `Math.abs` in der unveränderten Engine im `nah`-Text; Verschieben der Erklärung dorthin war unter „Engine unverändert“ richtig, aber der Text (730 Zeichen, vier Fehldiagnosen) verwässert. Satz zu −7,54 an den Anfang und jeden Fall mit seinem Zahlenwert voranstellen („**−7,54:** g − f statt f − g …“). |
| M5 | niedrig–mittel | sim1/sim2: richtige Option formal erkennbar (sim1 Option 1 als einzige ohne „denn“-Nachsatz; sim2 einzige mit „≈“). Optionen angleichen, z. B. sim1 Option 1 „bei a = −1,00, denn dort wechselt f − g das Vorzeichen.“ |
| M6 | niedrig | Anzeigefeld „Vorzeichenwechsel in [a; b]“ zählt das offene Intervall (a; b) (bei a = −1,00, b = 3,50 zeigt es 2 statt 3). Beschriftung in „in (a; b)“ ändern (Z. 460). |
| M7 | niedrig | Vielfachheits-Kriterium (Z. 409, Kernaussage 4 Z. 737) ohne Geltungsbereich; nur für ganzrationale Funktionen. Halbsatz ergänzen. |
| M8 | niedrig | a5: Aufgabentext „Runde auf eine Nachkommastelle“, Sollwert 105.42 und ok-Text 105,42. Entweder zwei Nachkommastellen fordern oder `wert: 105.4`. |
| M9 | niedrig | Einstieg (Z. 202) spricht von Längsschnitt, a5/a6 rechnen im Querschnitt; G und T unbenannt. „Querschnitt“ und „(Gelände G, Trasse T)“. |
| M10 | niedrig | Engine-bedingt: Eingabe 754 mit Einheit dm² (a2) bzw. 0,00797 mit L (a4) liefert „Der Zahlenwert stimmt …“; nur zur Kenntnis. |
| M11 | niedrig | Paar C: `lA`/`lB` ohne Einheit „min“; Feld heißt „f(b) − g(b)“, Diagramm nennt z(t) und „Abfluss 1,5“. |
| M12 | niedrig | Paar C: Marken a und b überlappen bei Mindestabstand (9 px gegen 14 px Kästchen). Kosmetik. |
| M13 | Prozess | Inhaltsdatei nicht nachgeführt (a2-nah/weit, Kernaussage 4 „A wächst nie“ falsch → „fällt nie“, 4.6 −0,38/−0,37); `modulliste.md` und `index.html` noch nicht auf fertig. |

Weitere Anmerkung: a2 Stufe 2 und a4 Stufe 2 nehmen viel vorweg (flachere Abstufung als bei a1, a5, a7); vertretbar.
