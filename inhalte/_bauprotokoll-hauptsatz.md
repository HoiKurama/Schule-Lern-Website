# Bauprotokoll `module/mathe-q1-hauptsatz.html`

Quelle: `inhalte/mathe-q1-hauptsatz.md`. Referenz: `module/physik-q1-induktion.html` (nur lesen).

## fertig

- Kopf, Farbtokens (`#0d7a52` / `#e7f6ef` / `#b5e0cd`), Kopfverlauf, Chips, Titel, Footer-Zeile.
- Abschnitt 4 (Simulation): Markup war bereits vorhanden und passt zur Spezifikation
  (Canvas `cvSim` 1000×560, Regler `rA`/`rX`, Anzeigen `lA lX lF lI lM lD`, Knöpfe
  `data-rate`, `bPlay`, `bReset`, Checkbox `cTan`, Beobachtungsauftrag, MC `sim1`/`sim2`).
- **Simulations-IIFE neu geschrieben** (ersetzt die Induktions-IIFEs `cvSim`-Leiterschleife und
  `cvLenz`): Simpson-Regel n = 200, zentrale Differenz ±0,02, Maßstäbe als Konstanten
  dokumentiert (75 px/h, obere Fläche y 30…260, untere y 320…540), Pointer-Ereignisse mit
  `setPointerCapture`, `dt`-Begrenzung, `fmt()` mit Komma.
  Gegen Handrechnung geprüft (alle Werte stimmen):
  A/a=0: x=4 → I 15,73 · m 5,00; x=6 → 25,20 · 4,20; x=9 → 32,40 · 0,00;
  x=10,5 → 29,93 · −3,45; x=12 → 21,60 · −7,80.
  B/a=0: x=4 → −6,40 · 0,00; x=12 → 19,20 · 6,40. C/a=0: x=5 → 10,36 · 0,89; x=12 → 12,97.
  a>x: A/a=9, x=3 → −21,60. A/a=3, x=12 → 10,80. B/a=2, x=8 → 4,80.
  Feld „Unterschied" steht in allen Fällen auf 0,000. Abspielen stoppt bei x = 12,00.

- Abschnitte 1-3 (Markup) stehen vollstaendig in der Datei, Abschnitt `lenz` gestrichen (Stufen 1..5 bis Uebungen).

## als Nächstes (Stand: Abschnitt 1-4 fertig; offen ab Punkt 1: Uebungen)

1. Markup Abschnitt 1 (Einstieg, vw1–vw3), 2 (Integralfunktion), 3 (Stammfunktion),
   5 (Übungen a1–a7) — die Reste des Induktionsmoduls sind dort noch drin.
2. Abschnitt „lenz" ersatzlos streichen, Stufennummern auf 1…6 bringen.
3. `mcDaten`, `numDaten`, Zuordnungs-Rückmeldungen, Export-Namensliste.
4. Abschnitt 6 (Zusammenfassung, Zentralabitur, Selbstcheck, Lehrerteil).
5. `PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/mathe-q1-hauptsatz.html"`,
   alle blocker/maengel beheben. Modulliste **nicht** selbst auf `fertig` setzen.
- Uebungen/Abschluss-Markup wird gerade ersetzt (Marker @@NEU@@ in der Datei). mcDaten, numDaten, Zuordnungstexte, Export-Namen fertig.
- Uebungen a1-a7 Markup fertig; als Naechstes Abschnitt 6 (Marker @@NEU@@), dann Modulcheck.
- Abschnitt 6 + Lehrerteil fertig. Als Naechstes: Modulcheck, Maengel beheben.
- Modulcheck: blocker [], maengel []. Modulliste NICHT auf fertig gesetzt (Auftrag).
FORTSCHRITT: Nacharbeit-Start. Bereits vorher in Datei erledigt: S1 (Zehntel Kubikmeter), M1. Offen: M2,M3,M4,M5,M6,M7,M8,M9,M10,Titel-Unicode,390px, Modulcheck.
FORTSCHRITT: erledigt M2,M5,M6,M7,M8,M10,Titel-Unicode (per Skript). Offen: M3/M9 (sim1/sim2 neu), 390px, Modulcheck.
FORTSCHRITT: erledigt M3/M9 (sim1/sim2 neu, mcDaten, Export-Namen). Offen: 390px (Canvas-Schrift, Touchziele), Modulcheck.
FORTSCHRITT: erledigt 390px (kk()-Schriftfaktor, Touch-CSS <=600px). Offen: Modulcheck, Screenshot 390.
FORTSCHRITT: Nacharbeit komplett. Modulcheck blocker [], maengel []. Simwerte nachgerechnet (B a=2: I(2)=0, I(4)=-1,60, I(6)=0, I(0)=4,80; C: I(12)=12,97, f(12)=0,11, f(6)=0,66). Modulliste nicht auf fertig.
FORTSCHRITT: Restpunkte-Start (N1-N8). Noch nichts erledigt.
FORTSCHRITT: erledigt in HTML N1,N2,N4,N5,N6,N7,N8, sim2 (N3). Offen: Spiegel inhalte/*.md, Modulcheck, Playwright-Ablesung.
FORTSCHRITT: Spiegel inhalte/mathe-q1-hauptsatz.md erledigt. Offen: Modulcheck, Playwright-Ablesung.
FORTSCHRITT: Restpunkte komplett. Modulcheck blocker [], maengel []. Playwright: Rate C x=12 -> 12,97 / 0,11 / 0,11 (Hand 12,969 / 0,1093), sim2 richtig=Index 1, Feedback ok. Modulliste unberuehrt.
