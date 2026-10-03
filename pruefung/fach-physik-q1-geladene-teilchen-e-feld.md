# Fachprüfung `module/physik-q1-geladene-teilchen-e-feld.html`

Prüfer: fachpruefung. Bericht von der Hauptsitzung abgelegt (Agent darf keine Dateien schreiben), gekürzt auf Urteil und Mängel.

**Urteil: Nacharbeit nötig.** Von rund 70 nachgerechneten Zahlenwerten stimmen alle bis auf eine Rundungsstelle (M6); alle Simulationszustände beider Modi (21 im Browser ausgelesen), alle Musterlösungen und alle Tröpfchen-Zonen halten stand. Lehrplanbezug wörtlich belegt, keine erfundenen Zitate, offene Punkte markiert. AB III echt (ue7–ue9 mit Bewertungskriterien). ue7–ue9 nur mit Musterlösung ist Nutzerentscheidung, kein Mangel.

## Schwere Fehler

- **S1 – Fünf Formeln rendern als KaTeX-Parsefehler** (Zeilen 283, 359, 780, 857, 873). In `data-tex` steht doppelt maskiertes `&amp;gt;` / `&amp;lt;` (Zeichenkette `&gt;`/`&lt;` wird nach HTML-Parsing zu `&amp;gt;` → ParseError). Lernende sehen roten Rohtext: Konventionskasten (zweimal), Schritt 1 der Parabelherleitung, Kontrolle in ue5, Musterlösung ue9, Abschluss-Merksatz. `data-plain` korrekt, deshalb findet `modulcheck.py` (Offline-Fallback) es nicht. Korrektur: in `data-tex` einfach maskieren (`&gt;`, `&lt;`), so wie im Modul `physik-q1-magnetisches-feld.html`. Danach mit echtem KaTeX (Netz an) auf `.katex-error` prüfen.
- **S2 – ue3, Rückmeldung zu Distraktor 0 (Z. 1062) falsch:** „Sie beschleunigt es in Feldrichtung“ – bei einem Elektron entgegen der Feldrichtung; widerspricht 2.1, Konventionskasten und der richtigen Option. Ersetzen durch: „Sie beschleunigt es längs der Feldlinien – beim Elektron entgegen der Feldrichtung – und ändert dabei Betrag und Richtung der Geschwindigkeit.“

## Mängel

| Nr. | Schwere | Befund und Vorschlag |
|---|---|---|
| M1 | hoch | Vorzeichenkonvention bei `tan θ` und `Y` unvollständig (Z. 355, 369, 879): `y_a = −sgn(q)·U_A·L²/(4·d·U_B)` ist vorzeichenbehaftet, `tan θ = U_A·L/(2·d·U_B) = 2·\|y_a\|/L` und `\|Y\| = tan θ·(L/2 + D)` nicht; Proton bei +100 V ergäbe +0,075, die Sim zeigt θ = −4,29°, Y = −17,25 mm. Schritt 6 der Herleitung mischt `2·y_a/L` und `2·\|y_a\|/L`. Korrektur: `tan θ = −sgn(q)·U_A·L/(2·d·U_B) = 2·y_a/L`, `Y = tan θ·(L/2 + D)`; Betragsstriche nur, wo ein Betrag gemeint ist (ue5). |
| M2 | hoch | sim1 und sim2 lassen sich ohne Simulation beantworten. sim2: Details-Block „Steig-Sink-Methode“ in 3.2 nennt wörtlich „bei U = 2·U_s genau +v_s“ und „bei 748 V … 0,1053 mm/s“ – die Frage fragt genau das. sim1: Merksatz „Bahn kennt weder Ladung noch Masse“ + Zahlenbeispiel Y = 17,25 mm + Fehlvorstellung 3 + Konventionskasten + Tabelle 2.2 beantworten es vollständig. Vorschlag: Werte abfragen, die nirgends im Text stehen, z. B. Tröpfchen 3 bei 200 V, Elektron bei 65 kV (klassisch vs. relativistisch, Diagramm 1) oder Plattentreffer (U_B = 1 kV, U_A = +100 V: Treffer bei x = 2,0 cm, Anzeigen „—“); Text der Erklärung entsprechend entschärfen oder Zahlen ändern. |
| M3 | mittel | Beobachtungsauftrag Teil B („bis das Tröpfchen ruht“) für Tröpfchen 2 (U_s = 298,73 V) und 4 (484,79 V) nicht wörtlich ausführbar: Regler 1 V, „ruht“ nur bei \|v\| < 0,05 µm/s (298 V sinkt, 299 V +0,11 µm/s; 484 V sinkt, 485 V +0,06 µm/s). Abhilfe: `step="0.5"` oder Ruhe-Band auf 0,2 µm/s weiten; oder Formulierung „bis es von Sinken zu Steigen wechselt“. |
| M4 | mittel | Relativitätswarnung deckt nur v₀ ab: bei 100 kV sind auch Flugzeit, y_a, Y, θ klassisch gerechnet und falsch, ohne Hinweis. Halbsatz ergänzen. |
| M5 | mittel | Unbeschriftete graue Feldpfeile in der Beschleunigungsstrecke (Z. 1366–1369); beim Elektron zeigen sie nach links, das Teilchen läuft nach rechts (Fehlvorstellung „Feldlinie = Bahn“). „E“/„Feldlinien“ beschriften. |
| M6 | klein | Zahlenbeispiel 3.2 (Z. 441): mit m = 3,665·10⁻¹⁵ kg und U_s = 374,1 V ergibt sich \|q\| = 4,805·10⁻¹⁹ C = 2,9996 e, nicht 4,806·10⁻¹⁹ C. `U_s = 374,07 V` angeben oder `4,805·10⁻¹⁹ C` schreiben. |
| M7 | klein | Cunningham (Z. 459): mit C ≈ 1,085 sind Radius +4,2 % und Ladung +13,1 % zu groß; Text „gut 12 %“ → „rund 13 %“ (stimmt mit 1,8·10⁻¹⁹ C zwei Sätze später überein). |
| M8 | klein | 2.4 verweist auf „Vorwissensfrage 2“, die Fragen sind nicht sichtbar nummeriert. |
| M9 | klein | Einstieg: Millikan hielt Tröpfchen „in der Schwebe“; überwiegend Steig-Sink-Methode. Halbsatz ergänzen. Belegstand (Websuche): Beginn 1909 (Millikan/Fletcher), Millikans Wert 1,592·10⁻¹⁹ C (0,6 % unter heute), Luftviskosität als üblich genannte Ursache sind belegt; die vorsichtigen Formulierungen im Modul sind gedeckt und dürfen präzisiert werden. 65 kV Zahnarztröhre im üblichen Bereich; 0,07 µm mittlere freie Weglänge Standardwert. |
| M10 | sehr klein | „Tröpfchen von einem Tausendstel Millimeter Durchmesser“: r = 1 µm ⇒ Durchmesser 2 µm. |
| M11 | kosmetisch | Kommentar `/* ---------- Druck ---------- */` steht über dem eingeschobenen Touch-Block (Z. 166 f.). |

Quellen: Wikipedia „Oil drop experiment“, APS News (Aug. 2006) „Robert Millikan Reports His Oil Drop Results“, Oxford Physics for Chemists „Millikan“, Britannica „Millikan oil-drop experiment“.
