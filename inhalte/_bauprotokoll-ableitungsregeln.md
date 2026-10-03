# Bauprotokoll `module/mathe-q1-ableitungsregeln.html`

Quelle: `inhalte/mathe-q1-ableitungsregeln.md` (vollstaendig, K1–K29).
Vorlage: `module/physik-q1-induktion.html` (unveraendert gelassen).

## fertig

- Referenzmodul auf `module/mathe-q1-ableitungsregeln.html` kopiert
- Farbtokens, Kopfverlauf, title, Seitenkopf (h1, Chips) getauscht (geprueft per diff)

## als Naechstes

- Sektionsinhalte ersetzen (Reihenfolge: Simulation zuerst), mcDaten/numDaten, Export-Namen, ergebnisse.z1 in Zuordnungs-Engine

- Abschnitt 4 Markup (beide Simulationen, MC sim1-3, Auftraege) eingesetzt; lenz-Sektion entfernt. Simulations-JS noch offen (Skript alt).
- Simulations-JS (beide IIFEs) eingesetzt. Noch zu pruefen per Playwright (Handrechnung K12/K14/K16/K17).
- Simulation geprueft (Playwright ab/simtest.py): K12, K13, K14, K15 (Max exakt bei t*, 35,00/−35,00; Abweichung von Spez: t exakt statt gerundet, weil sonst 35,02/−34,98), K16, K17 stimmen; Identitaet 40 Zufallszustaende ok; keine Konsolenfehler.
- Scratchpad wird von anderem Agent geteilt: eigene Dateien nur in scratchpad/ab/.
- Als Naechstes: Abschnitte 1-3 Markup, dann 5, 6, mcDaten/numDaten/Export/z1-Fix.
- Abschnitt 1 Markup fertig.
- Abschnitt 2 Markup fertig (ersetzt alte grundlagen+gesetz-Sektionen). Abschnitt 3 (id=kombination) muss vor "4 INTERAKTIVER" eingefuegt werden.
- Abschnitt 3 Markup fertig. Naechstes: Abschnitt 5 (Uebungen), 6 (Abschluss), JS-Daten.
- Abschnitt 5 Markup (10 Aufgaben, Zuordnung ohne data-num) fertig. Naechstes: Abschnitt 6 Abschluss+Lehrerteil, dann JS-Daten (mcDaten, numDaten, z1-Fix, Export).
- Abschnitt 6 Markup + Lehrerteil fertig. Offen: JS-Daten (mcDaten, numDaten, z1-Fix + Rueckmeldungstexte, Export-Namen/Titel), modulcheck.
- mcDaten, numDaten, z1-Fix + Rueckmeldungen, Export-Namen/Titel eingesetzt. Offen: modulcheck + Restpruefung (Elektro/Physik-Reste, alte Texte).
- modulcheck: blocker [] / maengel [] (nach Ersatz von 	ext{Euro} in KaTeX). Modul inhaltlich komplett. Modulliste NICHT auf fertig gesetzt. Offene Punkte: t*-Knopf setzt Zeit exakt statt auf 0,1 gerundet (Abweichung von Spez, bewusst); _bau_basis.md loeschbar.
FORTSCHRITT: Nacharbeit Touch-CSS (max-width:600px) erledigt. Rest: M1-M12 Texte, Canvas kk()
FORTSCHRITT: Nacharbeit Canvas kk() erledigt (Screenshot-Pruefung 390px noch offen). Rest: M1-M12 Texte
FORTSCHRITT: M1-M10 im HTML eingebaut (edit.py), Export-Nummern angepasst. Rest: inhalte-md 0,42, M11 (bewusst offen), Playwright/modulcheck, Screenshot 390
FORTSCHRITT: Nacharbeit abgeschlossen: M1-M10, Touch, Canvas kk(), inhalte-md M2; modulcheck blocker [] maengel []. Offen: M11 (Simulationsfragen bewusst unveraendert), M12 Modulliste (nicht auf fertig gesetzt).
FORTSCHRITT: M11 gestartet (sim1/sim2 ersetzen; sim3 bleibt)
FORTSCHRITT: M11 HTML+mcDaten+Export-Titel geaendert; offen: Playwright-Ablesen, modulcheck, inhalte-md
FORTSCHRITT: M11 HTML fertig, Sim-Werte per Playwright (17,60 / 3,57 Tage 2008,93) bestaetigt; offen: inhalte-md
FORTSCHRITT: M11 abgeschlossen (sim1/sim2 ersetzt, modulcheck leer, inhalte-md gespiegelt). sim3 unveraendert.
FORTSCHRITT: N1,N2,N3,N4 im HTML editiert (md N2 gespiegelt); offen: Playwright, modulcheck
FORTSCHRITT: N1-N4 fertig, Playwright (3,57 -> 3,6 nach Regler -> 3,57; 2008,93) ok, modulcheck siehe Bericht
FORTSCHRITT: N1-N4 abgeschlossen; N4 mit € ausserhalb des Formelspans (KaTeX-Warnung sonst); modulcheck blocker [] maengel []
FORTSCHRITT: Auftrag sim3-Ersatz gestartet (Plan: r0=8,c=1,2,t=15,dt=1,50; Frage exakte Ringflaeche)
FORTSCHRITT: sim3 neu in HTML+md geschrieben; offen: Playwright, modulcheck, Lehrerteil-Verweise
FORTSCHRITT: sim3-Ersatz abgeschlossen, Playwright (304,23/294,05) ok, modulcheck blocker [] maengel []; md Z.229 gespiegelt
