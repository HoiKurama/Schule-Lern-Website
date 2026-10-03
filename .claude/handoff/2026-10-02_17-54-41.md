# Sitzungs-Handoff

_PreCompact (auto) – 2026-10-02 17:54_

## Stand
- Schulordner (Q1 LK NRW, interaktive HTML-Module) weitergebaut; auf „weiter“ jeweils selbst das nächste Modul gewählt.
- **Fertig, geprüft, im Index eingetragen:**
  - `mathe-q1-geraden-ebenen`
  - `mathe-q1-lagebeziehungen` (Geraden/Ebenen im Raum; Simulation nur für Gerade und Ebene)
  - `physik-q1-wellen` (Simulation „Seilwelle“ mit drei Modi)
- Modulcheck bei allen ohne Blocker und Mängel.
- Reparatur im Schwingkreis: Umschaltknöpfe „Energien“/„Resonanzkurve“ zeigen jetzt den aktiven Zustand (eine CSS-Zeile im Bauskript, Modul neu gebaut, Modulcheck sauber). „Mechanische Schwingungen“ hat keine Umschaltknöpfe und war nicht betroffen.
- Commit `ac74d8d` (nur `Schule/` ohne Handoff-Dateien): Module, `index.html`, `fachliches`, `inhalte`, `ARBEITSSTAND.md`.
- Gestartet: `physik-q1-doppelspalt-gitter`. Arbeitsordner `scratchpad\dg` ist angelegt, mehr nicht.

## Offen
- `physik-q1-doppelspalt-gitter` bauen: Textteile, `daten.py`, `sim.js`, `baue.py`, Abbildungen, Zahlenprüfung, Browsertest, Modulcheck, Eintrag in `index.html`, `modulliste.md`, `ARBEITSSTAND.md` und Protokoll in `inhalte/`.
- Weitere Module nicht begonnen: `mathe-q1-abstaende-winkel`, Info- und Mathe-EK-Module.
- Offene fachliche Fragen:
  - Gauß-Verfahren und Kreuzprodukt im Kernlehrplan.
  - Wellenfunktion, Saiten und Pfeifen im Kernlehrplan.
  - c = √(F/μ) steht ohne Herleitung im Wellenmodul.
  - Zweite Person soll die Erklärtexte gegenlesen.
- Connectoren (Brightdeck, Coursera, Unsplash, Whimsical, Asana, Atlassian, ClickUp, Linear, Monday, Notion, Slack) sind nicht angemeldet. Freigabe über claude.ai-Connector-Einstellungen oder `/mcp`.

## Notizen
- Modulpipeline pro Modul: `baue.py`, `daten.py`, `sim.js` und `teil1–6.html` im Scratchpad, Vorlage `module/mathe-q1-flaechen-zwischen-graphen.html`.
- Modulcheck: `python werkzeug/modulcheck.py "module/DATEI.html" > check.json`, dauert 5–10 Minuten, im Hintergrund laufen lassen.
- Wellenmodul: Frequenz und Wellenlänge sind im Modus „Laufende Welle“ unabhängig einstellbar, obwohl das Medium die Geschwindigkeit festlegt. Das steht im Lehrerteil.
- Der Gangunterschied ist im Wellenmodul nur eindimensional eingeführt; die Ebene folgt im Modul Doppelspalt/Gitter.
- Betroffene Dateien der Reparatur: `physik-q1-schwingkreis.html`, `ARBEITSSTAND.md`, `inhalte/physik-q1-wellen.md`, `inhalte/physik-q1-schwingkreis.md`.
