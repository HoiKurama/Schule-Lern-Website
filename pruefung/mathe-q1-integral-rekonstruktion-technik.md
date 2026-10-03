# Technische Pruefung: mathe-q1-integral-rekonstruktion.html

Status: in Arbeit — Grundlauf (modulcheck.py) erledigt, Sichtpruefung Screenshots laeuft

## Urteil

(wird ergaenzt)

## Blocker

(wird ergaenzt)

## Maengel

1. **Kaputte Formel bei Vorwissensfrage 3 (Einstieg).** Element `[data-mc="vw3"] .frage`,
   Quelltext Zeile 230: `data-tex="v	ext{-}t"` — zwischen `v` und `ext{-}t` steht ein
   **echtes Tab-Zeichen (0x09) statt der Zeichenfolge `\text`**. KaTeX rendert das dadurch
   nicht als "v-t" (kursives v, Bindestrich, kursives t), sondern als fuenf einzelne kursive
   Buchstaben "v e x t" gefolgt von Minus und "t" — sichtbar im Browser als **„vext−t-Diagramm"**
   statt „v-t-Diagramm". `data-plain="v-t"` ist korrekt hinterlegt, wird aber nur im
   Offline-Fallback verwendet, im Normalbetrieb (KaTeX aktiv, Netz vorhanden) sieht jede
   Schuelerin/jeder Schueler die falsche Version. Kein Konsolenfehler, da KaTeX das Tab
   stillschweigend als Leerraum interpretiert statt einen Parse-Fehler zu werfen.
   Reproduktion: Seite oeffnen, Abschnitt 1 „Vorwissen pruefen", dritte Frage lesen.
   Screenshot: `vw3_zoom.png` im Pruefordner.
   Es ist der einzige Fund dieser Art im Dokument (per `grep -c $'\t'` bestaetigt: genau
   eine Tab-Stelle in der ganzen Datei).

## Testabdeckung

- Generischer Modulcheck (modulcheck.py) durchgelaufen: 0 Blocker, 0 Maengel laut Skript.
  324 Formeln gefunden, MC-Fragen: vw1, vw2, vw3, sim1, sim2, a4 (6 Stueck), Zahlenfelder:
  a1, a2u, a2o, a3, a6 (5 Stueck), Regler: regN, regB (2 Stueck), Canvas: cvRate (1000x490),
  cvBestand (1000x310), Selbstcheck: 6 Punkte.
- Screenshots 1280/900/390 px vom Modulcheck erzeugt und mit Read-Werkzeug angesehen
  (Fortsetzung folgt).

## Screenshots

Ablageort: `C:/Users/49176/AppData/Local/Temp/claude/C--Users-49176-Documents-Claude-Projects-Schule/5616889e-4b92-41aa-b192-9ce54df721fb/scratchpad/pruef/shots-mathe/`
- `mathe-q1-integral-rekonstruktion-1280.png`, `-900.png` (vollstaendige Seite, 16303 px hoch),
  `-390.png`
- Segmentierte Ansicht der 900px-Vollseite in `slice900_00..08.png`
- `vw3_zoom.png` — Nachweis Formelfehler vw3

Bisherige Beobachtung bei 900 px: Layout sauber, Tabellen, Kernaussage-Boxen, Simulation
(Canvas-Diagramme, Regler, Buttons) und Uebungsaufgaben (Zahlenfeld + Einheit-Dropdown +
Pruefen-Button, Tipp/Ansatz/Loesungsweg) wirken uebersichtlich, kein Ueberlappen erkennbar.
Weitere Slices und die Breiten 1280/390 werden noch vollstaendig durchgesehen.

## Zwischenstand Interaktionen (MC + Zahleneingaben)

- **Multiple Choice**: 6 Aufgaben (vw1, vw2, vw3, sim1, sim2, a4) mit zusammen 21 Optionen
  systematisch einzeln angeklickt. Jede Option zeigt eigenen Feedbacktext (keine zwei Optionen
  mit identischem Text innerhalb einer Aufgabe), nach Klick auf die als richtig hinterlegte
  Option (`r`-Index) wird genau diese Option gruen (`.opt.richtig`), bei jeder falschen Option
  wird nur die angeklickte Option rot, keine automatische Aufdeckung der richtigen — das ist
  wortgleich das Verhalten des Referenzmoduls `physik-q1-induktion.html` (gleicher Skriptblock),
  also kein modul-spezifischer Fehler.
- **Zahleneingaben**: 5 Felder (a1, a2u, a2o, a3, a6) x 4 Faelle (richtiger Wert mit richtiger
  Einheit / richtiger Wert mit falscher Einheit / grob falscher Wert / leeres Feld) =
  20 Kombinationen geprueft. Alle 20 zeigen jeweils vier unterschiedliche Rueckmeldungstexte
  pro Feld (keine Ueberschneidung). Klassenwechsel `rueck zeig ok` nur beim Volltreffer,
  sonst `rueck zeig nein` mit inhaltlich unterschiedlichem Text (Einheiten-Hinweis vs.
  Naeherungs-Hinweis vs. Weit-daneben-Hinweis vs. „Bitte Zahlenwert und Einheit angeben“).
  Rechnerisch alle Sollwerte nachgerechnet und bestaetigt: a1=25,75 kWh, a2u=11,0 m³,
  a2o=19,0 m³, a3=320 Streifen, a6=10,8 m³, a4 (MC) = 180 L. Alle stimmen mit der Datei
  ueberein.
- Komma-Eingabe per Tastatur in `input[type="number"]` getestet (Zeichen fuer Zeichen simulierte
  Tastendruecke, nicht `.fill()`): Chromium wandelt das getippte Komma selbst in einen Punkt um,
  bevor das Script `parseFloat(...replace(",","."))` ueberhaupt zum Zug kommt. Funktioniert wie
  erwartet, kein Befund.

## Zwischenstand Zuordnung, Hilfen, Musterloesungen

- **Zuordnungsaufgabe** (Ratendiagramm A-D <-> Bestandsbeschreibung, 4 Zeilen): vollstaendig
  richtig getestet (alle 4 Zeilen `zeile richtig`, Rueckmeldung "Alle vier richtig..."),
  teilweise richtig mit 2 von 4 (Rueckmeldung "2 von 4 richtig...", betroffene Zeilen korrekt
  mit `zeile richtig`/`zeile falsch` markiert), und unvollstaendig (eine Zeile auf Platzhalter
  zurueckgesetzt -> "Es fehlen noch 1 Zuordnungen.", Pruefung wird korrekt verweigert).
  Musterloesung der Zeilen mathematisch geprueft: A (konstante Rate) -> Diagramm A (flach),
  C (wachsende Rate) -> Diagramm C (steigend), D (konstant negativ) -> Diagramm D (flach unten),
  B (Vorzeichenwechsel bei t=4h) -> Diagramm B (fallend durch Null) - alle plausibel.
- **Hilfe-Knoepfe**: 24 Tipp/Ansatz/Loesungsweg-Buttons ueber alle 8 Uebungsaufgaben mit
  Hilfesystem einzeln auf- und wieder zugeklappt (`.hilfe-text.zeig`-Klasse korrekt gesetzt/
  entfernt), alle 24 fehlerfrei.
- **Musterloesung-Knoepfe** (Begruendungsaufgaben a5, a7, a8): je Knopf zweimal geoeffnet und
  einmal geschlossen (Text wechselt korrekt zwischen "Musterlösung anzeigen" und
  "Musterlösung ausblenden", auch beim zweiten Oeffnen). Keine Fehler.
- Kein Konsolenfehler/pageerror bei alldem.

## Zwischenstand Simulation, Export, Druck

- **Regler regN** (Streifenzahl, 1-40, step 1): 12 Stichproben ueber den vollen Bereich
  (1,2,3,4,5,8,10,16,20,25,32,40) gefahren, alle 8 Anzeigefelder (lN, lB, anzDt, anzU, anzO,
  anzSchere, anzGrenz, anzBestand) je Schritt gelesen — kein `NaN`, `Infinity`, `undefined`
  oder `null` in irgendeinem Feld.
- **Regler regB** (obere Grenze b, 1-12, step 0,5): alle 23 moeglichen Werte durchgefahren,
  gleiche Pruefung auf alle 8 Felder — keine Auffaelligkeit. Bei b=12,0 h wird die Untersumme
  korrekt negativ (-5,400 m³), das ist rechnerisch bestaetigt richtig (Rate wird ab ca. t=9,7 h
  negativ) und keine falsche Anzeige.
- **Knopf „n verdoppeln“**: 8x in Folge geklickt, Streifenzahl steigt 4→8→16→32→40 und bleibt
  danach korrekt bei der Obergrenze 40 stehen (kein Ueberlauf, keine Endlos-Verdopplung über das
  `max`-Attribut hinaus), Schere sinkt dabei monoton wie erwartet (5,925 → 2,991 → 1,499 → 0,750
  → 0,600 und bleibt dort stabil).
- **Knopf „Zuruecksetzen“**: stellt nach beliebigen vorherigen Reglerstaenden zuverlaessig
  n=4 und b=6,0 h wieder her (Felder exakt wie beim Erstladen: U=21,825 m³, O=27,750 m³,
  Schere=5,925 m³, Grenzwert=25,200 m³, Bestand=37,20 m³).
- Die Zeitachse der beiden Diagramme ist bewusst fest auf [0 h; 12 h] gesetzt (12 h ist zugleich
  das Maximum von regB) — es gibt hier keine laufende Simulationszeit wie im Induktions- oder
  Federmodul, sondern eine statische Funktionsdarstellung mit fixem Definitionsbereich. Deshalb
  entfaellt „Zeitachse waechst mit“ und „Start/Pause“ sachlich; es gibt nur die Regler und
  „Zuruecksetzen“, was zum Thema (Riemann-Summen auf festem Intervall) passt. Kein Ziehmodus
  (kein `pointerdown` im Skript) — die Bedienung erfolgt ausschliesslich über die zwei
  `<input type="range">`-Regler, das ist für diese Aufgabe angemessen.
- **Export** („Ergebnisse kopieren“): einmal und danach zweimal hintereinander ausgeloest,
  wirft in keinem Fall einen Fehler. Zwischenablage-Inhalt geprueft: deutsches Datumsformat
  (“7.9.2026, 16:22:03”), Aufgabenbezeichnungen auf Deutsch, Status je Aufgabe
  korrekt („noch nicht richtig“ / „nicht bearbeitet“).
- **Druckansicht** (`emulateMedia print`): Regler (`#regN`, `#regB`), Knopf „n verdoppeln“,
  Knopf „Zuruecksetzen“, Lehrerteil (`details.lehrer`), Export-Knopf und Druck-Knopf selbst sind
  ausgeblendet. Aufgabentexte, Hilfetexte und Musterloesungen sind sichtbar/lesbar. Volle
  Druck-Screenshot-Kontrolle (`print_view.png`, 19072 px hoch, in 10 Segmente zerlegt und
  gesichtet): keine abgeschnittenen Kaesten, Kernaussage-Boxen und Aufgaben brechen sauber um.
  Einzige Beobachtung: Die „Pruefen“-Buttons der Zahlenaufgaben (`.eingabe button`) bleiben im
  Druckbild sichtbar, weil sie nicht in `.knopfleiste` liegen, sondern in `.eingabe` — das ist
  exakt dasselbe Verhalten wie im Referenzmodul `physik-q1-induktion.html` (identischer
  CSS-Block, per Diff bestaetigt), also keine modul-spezifische Abweichung, sondern ein bereits
  im geprueften Referenzmodul vorhandenes Verhalten.
- **Querscrollen**: bei 1280, 900 und 390 px `scrollWidth === clientWidth` (kein horizontales
  Scrollen) an allen drei Breiten.



