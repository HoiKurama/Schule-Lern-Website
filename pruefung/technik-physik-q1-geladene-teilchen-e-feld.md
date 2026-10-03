# Technikprüfung `module/physik-q1-geladene-teilchen-e-feld.html`

Prüfer: qa-technik (Playwright). Bericht von der Hauptsitzung abgelegt, weil der Agent keine Dateien schreiben darf.

**Urteil: Nacharbeit nötig, kein Blocker.** `modulcheck.py`: `blocker: []`, `maengel: []`.

## Mängel

| Nr. | Schwere | Befund |
|---|---|---|
| 1 | hoch | 390 px: Canvas-Beschriftung kaum lesbar und teils abgeschnitten. Canvas auf Faktor 0,348 verkleinert, `kk()` (Z. 1264) hebt Schrift höchstens um 1,9 an → 7,3 px in `cvSim`, 8,0 px in `cvD1`/`cvD2`, beide Modi. Im Millikan-Bild laufen die Textzeilen am rechten Rand aus dem Canvas (Block ab Z. 1562, `dx = 722`: „Viskosität η = …“, „Tröpfchen vergrößert dargestellt“), „unterer Platte“ wird von der Fußzeile „Pfeile …“ überlagert, Kraftdiagramm kaum entzifferbar. Bei 1280/900 px sauber. Parameter stehen zusätzlich als DOM-Text. |
| 2 | mittel | Umschalter „Strahl im Querfeld / Millikan-Versuch“: Labels 143×23 und 133×23 px, Radio-Punkte 16×16 px; `button{min-height:44px}` (Z. 169) erfasst sie nicht. Hauptbedienelement der Simulation. |
| 3 | mittel | Range-Regler `rUB`, `rUA`, `rUM` 32 px hoch (Z. 170); Zuordnungs-Selects 36×36 px (`min-height:36px`); Selects der Zahlenaufgaben 41 px. |
| 4 | gering | Radio-Punkte/Checkboxen in MC-Optionen und Selbstcheck 13×13 bis 13×17 px (26 Elemente); umgebende Labels groß genug. |
| 5 | gering | Kein Pause-Knopf, keine Ziehinteraktion: Strahl-Modus läuft als Schleife (3,1 s), Millikan-Tropfen bewegt sich dauernd. Vorhanden: Zurücksetzen, Echtzeit/5-fach, Spur löschen. Pause wäre bei der Auswertung der Tröpfchenbahn hilfreich; ggf. Konzeptfrage. |
| 6 | gering | `touch-action` am Canvas `auto`; unkritisch, solange nichts gezogen wird. |
| 7 | gering | Keine Zeitachse in den Diagrammen (Strahl: v/c gegen U_B und Y gegen U_A; Millikan: v gegen U, Kraft-Balken); Kurven bleiben im sichtbaren Bereich. Kein Mangel. |
| 8 | gering | Druck: 8 Bedienelemente der Aufgaben (Selects, Prüfen) sichtbar, 21 Hilfetexte eingeblendet; Print-CSS stammt unverändert aus der Vorlage. |
| 9 | gering | `data-plain` teils mit Unterstrichen („U_B = 65 kV“, „m_e“, „ρ_L“), auch in Fließtext/Musterlösungen („U_A“, „y_a“, „v_s“); lesbar, nicht Unicode-sauber. |
| 10 | gering | Grammatik: „Es fehlen noch 1 Zuordnungen.“ |

## Testabdeckung

- Laden ohne Fehler; Offline: 480 Formeln, 0 leere, keine LaTeX-Reste.
- 20 MC-Optionen einzeln, je eigenes Feedback; Zahleneingaben ue1, ue2, ue5, ue6 (richtig, falsche Einheit, Faktor 100, leer, Alternativeinheit); Zuordnung (4 / 3 / leer); 21 Hilfe-Zyklen; Export.
- Regler `rUB` 0–300, `rUA` −200–200, `rUM` 0–1000 über den ganzen Bereich; Strahl für alle drei Teilchen, Millikan für alle vier Tröpfchen, 5-fach und Echtzeit: keine NaN/Infinity/undefined.
- Kein waagerechtes Scrollen bei 1280/900/390 px; kein `localStorage`/`sessionStorage`/Cookie/`TODO`.
- Nicht geprüft: Mathematik der Musterlösungen und physikalische Werte (Aufgabe der Fachprüfung).
- Screenshots: `C:\Users\49176\AppData\Local\Temp\claude\C--Users-49176-Documents-Claude-Projects-Schule\a4e21d4f-5e40-4a28-8031-ae2059d6cc04\scratchpad\shots\`.
