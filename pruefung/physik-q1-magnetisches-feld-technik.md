# Technische Prüfung: physik-q1-magnetisches-feld.html

Prüfdatum: 07.09.2026 · Technische Prüfung (Playwright/Chromium, Python)
Diese Prüfung deckt ausschließlich die **technische** Seite ab (Laden, Formelfallback,
Interaktionen, Simulation, Darstellung, Druck, Regeltreue). Die fachliche Prüfung liegt separat
unter `pruefung/physik-q1-magnetisches-feld-fachlich.md` vor (Urteil dort: „Nacharbeit nötig“,
wegen algorithmischer Mängel des Wien-Filters — S1–S4). Diese Befunde werden hier **nicht**
wiederholt bewertet, nur wo sie technisch sichtbar wurden, kurz bestätigt.

Grundstand der Projektleitung (generischer Modulcheck, erneut ausgeführt und reproduziert):
0 Blocker, 1 Mangel („bei 390 px: Seite scrollt 3 px waagerecht“). Dieser Bericht bestätigt den
Grundstand, präzisiert eine Ursache und ergänzt Befunde, die der generische Check nicht prüfen
kann (Screenshots angesehen, Simulation durchgespielt, Bahnradius/Maßstab nachgemessen).

## Urteil

**Bestanden** (technisch, mit Mängeln). Kein Blocker gefunden: Die Seite lädt fehlerfrei mit und
ohne Netz, jede Formel hat einen funktionierenden Klartext-Fallback, alle Multiple-Choice-,
Zahleneingabe-, Zuordnungs-, Hilfe- und Exportelemente reagieren korrekt und mehrfach
wiederholbar, die Simulation liefert in keiner geprüften Reglerstellung NaN/Infinity/undefined,
und die Druckansicht blendet Bedienelemente und Lehrerteil korrekt aus. Die gefundenen Mängel
sind kosmetisch bzw. Erbstücke der gemeinsamen Vorlage und verhindern den Unterrichtseinsatz
nicht. Der Gesamteinsatz des Moduls bleibt trotzdem gesperrt, weil die fachliche Prüfung den
Wien-Filter-Modus als inhaltlich unbrauchbar einstuft — das ist ein fachlicher, kein technischer
Befund.

## Blocker

Keine gefunden.

## Mängel

### T1 — Die 3 px waagerechtes Scrollen bei 390 px stammen von den `.tabelle`-Containern, nicht von den Formelblöcken

Fundstelle: CSS-Zeile 155 `.tabelle{overflow-x:auto;margin-bottom:14px}`, betrifft alle acht
`.tabelle`-Vorkommen im Erklär-, Vertiefungs- und Lehrerteil.

Nachgemessen bei 390 px Breite: `document.documentElement.scrollWidth − clientWidth = 3`.
Per Skript gezielt einzelne Elementklassen ausgeblendet und neu gemessen:

| Ausgeblendet | Differenz danach |
|---|---|
| nichts (Ausgangszustand) | 3 px |
| alle `.m.block` (KaTeX-Formelzeilen) | 3 px (unverändert) |
| alle `.tabelle` | 0 px |
| alle `.m.block` **und** `.tabelle` zusammen | 0 px |
| zusätzlich alle inline `.m` | 0 px |

Die Formelblöcke sind also nicht die Ursache; einzig das Ausblenden der Datentabellen beseitigt
den Überlauf. Innerhalb der `.tabelle`-Container selbst ist der Inhalt bis zu 95 px breiter als
der Container (z. B. die Teilchentabelle in der Vertiefung: `scrollWidth 445` gegen
`clientWidth 350`), das ist aber durch `overflow-x:auto` korrekt gekapselt und erzeugt einen
eigenen, unauffälligen Scrollbalken **innerhalb** der Tabelle (sichtbar z. B. in
`shots/390_tabelle.png`, dort läuft die Kopfzeile am rechten Rand sichtbar ab). Die 3 px am
Dokument sind ein Randeffekt dieser Kapselung selbst, keine sichtbare Bildstörung — in keinem
Screenshot ist ein horizontales Scrollen der Gesamtseite optisch bemerkbar. Einstufung wie bei
der Projektleitung: Mangel, kein Blocker. Neu gegenüber dem Grundstand ist nur die genauere
Lokalisierung (Tabellen statt Formeln), die einen gezielteren Korrekturansatz erlaubt (z. B.
`table-layout` der Tabellenkopfzeilen prüfen oder den Kapsel-Rand um 1–2 px vergrößern).

### T2 — Canvas-Beschriftung bei 390 px praktisch unlesbar

Fundstelle: `#cvSim`, interne Auflösung 1000 × 640 px, feste Schriftgrößen 14–16 px in
`zeichneKreis()` (Zeilen 1838 ff.) und `zeichneWien()` (Zeilen 1909 ff.), Canvas eingebunden mit
`width:100%` gemäß Projektvorgabe.

Bei 390 px Viewportbreite wird das Canvas auf 348 px CSS-Breite herunterskaliert (Faktor 0,348).
Die internen 15–16-px-Beschriftungen (B in die Bildebene hinein, Teilchenname und
Zeitlupenfaktor oben rechts, Quelle, r = Wert cm im Kreismodus; E nach unten, B in die
Bildebene hinein, Schirm-Blende-Angabe, Platten-Maße im Wien-Modus) werden dadurch auf effektiv
rund 5 bis 6 CSS-Pixel verkleinert und sind auf einem Telefon-Bildschirm kaum noch zu entziffern
(siehe `shots/canvas_kreis_maxradius_390.png`, `shots/canvas_wien_390.png`, zum Vergleich
3-fach vergrößert in `shots/canvas_kreis_maxradius_390_3x.png`). Die textuellen Anzeigefelder
außerhalb des Canvas (aV, aR, aT und so weiter, normales HTML) bleiben davon unberührt und sind
bei 390 px weiterhin gut lesbar (siehe `shots/390_simulation_regler.png`).

Das Referenzmodul physik-q1-induktion.html verwendet dieselbe Technik (Canvas mit
width="1000", feste Schriftgrößen 12 bis 17 px, width:100% per CSS) und dürfte bei 390 px
dieselbe Verkleinerung zeigen — es handelt sich also um eine Eigenschaft der gemeinsamen Vorlage,
nicht um einen modulspezifischen Fehler. Trotzdem ist der Effekt in diesem Modul stärker spürbar,
weil das Canvas hier mit vier gleichzeitig sichtbaren Textzeilen und einem dichten
Kreuz-Raster dichter beschriftet ist als zum Beispiel das Induktionsmodul. Empfehlung an die
Projektleitung: für die Vorlage einen Mindest-Skalierungsfaktor oder eine responsive Schriftgröße
im Canvas erwägen, nicht nur für dieses Modul.

### T3 — Auswahlfelder der Zuordnungsaufgabe sind kleine Touchziele (36 mal 19 px)

Fundstelle: CSS-Zeile 142 (`.zeile{display:grid;grid-template-columns:1fr auto;...}`), kein
eigener Stil für das select darin. Gemessen bei 390 px und bei 1280 px identisch:
36 mal 19 px pro Auswahlfeld (vier Zeilen in der Zuordnungsaufgabe Bild A bis D). Das liegt
deutlich unter der gängigen 44 mal 44 px Richtgröße für Touchziele und ist kleiner als jedes
andere Bedienelement der Seite (Buttons und übrige Selects messen 39 bis 44 px Höhe). Die
Bedienung funktioniert trotzdem einwandfrei (per Playwright wie auch beim Antippen mit
ausreichender Zielgenauigkeit), es ist aber auf einem Touchscreen unbequem zu treffen. Dieselbe
`.zeile`-Regel existiert unverändert im Referenzmodul (physik-q1-induktion.html, Zeile 142), es
handelt sich also ebenfalls um ein Vorlagen-Erbe, kein modulspezifischer Fehler.

### T4 — Bestätigung, kein neuer Befund: B-Regler-Sprung beim Teilchenwechsel technisch nachvollzogen

Bereits im fachlichen Bericht als S1 dokumentiert. Technisch bestätigt: Bei Wechsel von Proton
(rB 200 mT) auf Alphateilchen springt der Regler automatisch auf 185 mT (bstart des neuen
Teilchens), die Anzeige lB folgt korrekt dem tatsächlichen Reglerwert — die Anzeige selbst zeigt
den ungewollten Sprung korrekt an, verfälscht ihn nicht zusätzlich. Kein zusätzlicher
technischer Fehler, nur Bestätigung des fachlichen Befunds aus technischer Beobachtung.

## Testabdeckung

**Laden.** Zwei Durchläufe. Mit Netz: 0 Konsolenfehler, 0 pageerror. Mit blockiertem jsdelivr:
genau 2 console.error (Failed to load resource: net::ERR_FAILED, für Skript und Stylesheet von
KaTeX) — das ist die erwartete, zulässige Meldung für eine blockierte CDN-Anfrage, keine
weiteren Fehler.

**Formelfallback.** 434 .m- und .m.block-Elemente im Markup, 434 im DOM (Übereinstimmung). Mit
blockiertem Netz: 0 Elemente mit leerem textContent. Im sichtbaren Ausgangszustand zeigen 274
Elemente sichtbaren Text (der Rest liegt in geschlossenen details, ungeöffneten Hilfe-Stufen
oder im aktuell nicht aktiven Wien-Modus). Nach programmatischem Öffnen aller details, aller
Hilfetexte und Umschalten in den Wien-Modus sind alle 434 Elemente sichtbar und keines davon
leer. Keine LaTeX-Reste (\frac, \cdot, \dfrac, \mathrm, \text) im sichtbaren Seitentext
gefunden.

**Multiple Choice.** 5 Aufgaben (vw1, vw2, vw3, sim1, sim2) mal 3 Optionen gleich 15
Einzelklicks. Bei jedem Klick: genau eine Option wird richtig (grün), die angeklickte falsch
(rot) sofern nicht korrekt, die Rückmeldung erscheint mit eigenem, inhaltlichem Text pro Option
(keine Wiederholung), jede Optionsbeschriftung ist einzeln lesbar. 0 pageerror.

**Zahleneingaben.** 6 Aufgaben (ue1, ue2, ue3, ue5, ue6, ue7) mal 4 Fälle gleich 24 Prüfungen:
richtiger Wert und richtige Einheit ergibt ok mit Lösungsweg-Text; richtiger Wert und falsche
Einheit ergibt eigenen Einheiten-Text; grob falscher Wert (Faktor über 2 in beiden Richtungen
getestet) ergibt eigenen weit-Text; leeres Feld ergibt Bitte Zahlenwert und Einheit angeben.
In allen 6 Aufgaben sind die vier Rückmeldungen paarweise unterschiedlich.

**Zuordnung.** 3 Durchläufe der 4-Zeilen-Aufgabe: vollständig richtig (4 von 4, alle Zeilen
grün), teilweise richtig (3 von 4, erste Zeile rot), und erneutes vollständiges Prüfen nach
Korrektur (wieder 4 von 4) — mehrfaches Prüfen funktioniert ohne Zustandsfehler.

**Hilfen und Musterlösungen.** 6 Aufgaben mal 3 Hilfestufen mal 2 Klicks (auf/zu) gleich 36
Klicks, jede Stufe schaltet zuverlässig um. 3 Musterlösungs-Knöpfe mal 2 Klicks gleich 6 Klicks,
Button-Beschriftung wechselt korrekt zwischen den beiden Zuständen.

**Export.** 3 mal hintereinander ausgelöst, jedes Mal Meldung über erfolgreiches Kopieren ohne
Exception.

**Simulation.**
- Moduswechsel Kreis zu Wien 4 mal hintereinander, keine verbotenen Werte (NaN, Infinity,
  undefined) in den Anzeigefeldern.
- Teilchenwechsel durch alle 4 Teilchen (Elektron, Proton, Alpha, Ne-20), B-Regler-Grenzen und
  Wert nach jedem Wechsel geprüft (Sprung siehe T4/S1, keine NaN).
- Vorzeichenwechsel für jedes der 4 Teilchen mal 2 Vorzeichen gleich 8 Kombinationen, alle Namen
  (Proton/Antiproton und so weiter) korrekt und laut Ladung.
- Kreisbahn: 4 Teilchen mal U-Extrem (200 V/1800 V) mal B-Extrem (Teilchen-Minimum/Maximum)
  gleich 16 Kombinationen, jeweils Anzeige gelesen, keine verbotenen Werte.
- Wien-Filter: 2 Teilchen (Proton, Alpha) mal U-Extrem mal B-Extrem mal U_P-Extrem gleich 16
  Kombinationen, keine verbotenen Werte, keine Konsolenfehler.
- Start/Pause/Zurücksetzen: 2 vollständige Zyklen (Start, 900 ms laufen lassen, Pause,
  Zurücksetzen), Button-Beschriftung jedes Mal korrekt, 0 Fehler.
- Ziehmodus: entfällt für dieses Modul, es gibt keine pointerdown- oder pointermove-Handler auf
  dem Canvas; die Bedienung läuft ausschließlich über Regler und Auswahlfelder. Kein Befund.
- Wachsende Zeitachse: entfällt ebenfalls, dieses Modul zeichnet eine Kreisbahn beziehungsweise
  eine einmalig berechnete Flugbahn, kein Streifendiagramm mit mitwachsender Zeitachse. Kein
  Befund.

**Bahnradius im Bild.** Für alle 16 Kreisbahn-Extremkombinationen (siehe oben) den Radius in
Pixel sowohl per Handrechnung (Python, CODATA-Konstanten) als auch aus der laufenden Seite
ausgelesen — beide stimmen exakt überein. Größter Radius: Alphateilchen bei U gleich 1800 V,
B gleich 150 mT, r gleich 5,76 cm gleich 144,00 px. Die geometrische Grenze liegt bei 160 px
(aus Y_QUELLE gleich 320, Kreismittelpunkt bei 320 minus oder plus r_px, der von der Quelle
abgewandte Bogenpunkt bei 320 minus oder plus 2 mal r_px, muss zwischen 0 und 640 bleiben, also
r_px kleiner 160). 144 px liegt mit 16 px Reserve sicher darunter, für alle vier Teilchenarten
und unabhängig vom Ladungsvorzeichen (das Vorzeichen ändert nur die Richtung, nicht den Betrag).
Per Screenshot bestätigt (canvas_kreis_maxradius_1280.png): Der Kreis bleibt vollständig im
Bild, keine Überschneidung mit den Randbeschriftungen.

**Maßstabsbalken.** Codeprüfung: 125 px mal 4,00e-4 m/px gleich 0,0500 m gleich 5,00 cm,
Beschriftung 5 cm fest im Code (Zeile 1829). Zusätzlich im Screenshot bei 1280 px nachgemessen:
Bildgröße 818 mal 524 px (Canvas dort auf 81,8 Prozent skaliert), gemessene Balkenlänge 102 px —
das entspricht 102 geteilt durch 0,818 gleich 124,7, also rund 125 interne Pixel. Länge und
Beschriftung passen zusammen.

**Screenshots.** Aufgenommen und angesehen bei 1280, 900 und 390 px Breite: je eine
Vollseiten-Aufnahme, Canvas-Nahaufnahmen (Kreisbahn bei maximalem Radius, Wien-Filter) bei allen
drei Breiten, dazu bei 390 px gezielte Ausschnitte von Kopfbereich, Simulationsbereich (Anzeige
und Regler), Zuordnungsaufgabe und einer Tabelle. Auffällig: waagerechtes Scrollen exakt 3 px
bei 390 px (siehe T1), keine überlappenden Beschriftungen außerhalb des Canvas, keine
abgeschnittenen Diagrammachsen, aber unlesbare Canvas-Beschriftung bei 390 px (siehe T2). Bei
900 und 1280 px ist die Canvas-Beschriftung in allen Modi klar lesbar.

**Druckansicht.** Per emulateMedia print und DOM-Abfrage geprüft: Regler rU und rB,
Start-/Reset-Button, Teilchen-Auswahl, Export-Button, details.lehrer sind alle unsichtbar
(display:none über die gemeinsame Regel für .steuer, .knopfleiste, .hilfen, .lehrer).
Aufgabentext bleibt sichtbar, Hilfetexte werden über eine eigene Regel unabhängig vom
Aufklapp-Zustand erzwungen sichtbar geschaltet — auch ungeöffnete Tipps drucken mit. Das Canvas
selbst bleibt als Standbild im aktuellen Simulationszustand sichtbar (kein Blocker, aber kein
interaktives Element mehr). Per Screenshot dreier Bereiche (Simulationsbox, Abschlussbereich mit
Zentralabitur-Hinweis, Selbstcheck) keine abgeschnittenen Kästen gefunden.

**Regeltreue.** Kein localStorage, sessionStorage, document.cookie, kein TODO, kein Lorem ipsum
(Grep, 0 Treffer). Einzige externe Referenz ist der KaTeX-CDN-Pfad (vom generischen Modulcheck
bestätigt). Zahlenausgabe läuft ausnahmslos über eine einzige Formatierfunktion, die bei jedem
Aufruf den Dezimalpunkt durch ein Komma ersetzt (einzige toFixed-Verwendung im gesamten Skript)
— Komma statt Punkt ist damit strukturell garantiert, nicht nur stichprobenartig geprüft.

## Screenshots

Ablageort: C:/Users/49176/AppData/Local/Temp/claude/C--Users-49176-Documents-Claude-Projects-Schule/5616889e-4b92-41aa-b192-9ce54df721fb/scratchpad/nacharbeit/shots/
(temporäres Arbeitsverzeichnis, nicht im Projektordner).

- seite_1280.png, seite_900.png, seite_390.png — Vollseiten-Aufnahmen der drei Breiten. Layout
  bei 1280/900 unauffällig. Bei 390 px durchgängig einspaltig, keine Überlappungen außerhalb des
  Canvas.
- canvas_kreis_maxradius_1280.png, _900.png, _390.png — Kreisbahn bei Alphateilchen, U gleich
  1800 V, B gleich 150 mT (größter vorkommender Radius). Bei 1280/900 gut lesbar, Kreis bleibt
  sicher im Bild (siehe Bahnradius-Nachweis oben). Bei 390 px Beschriftung kaum lesbar (T2),
  3-fach vergrößerte Version in canvas_kreis_maxradius_390_3x.png.
- canvas_wien_1280.png, _900.png, _390.png — Wien-Filter-Ansicht, Proton. Gleiches Befundmuster
  wie oben: bei 390 px sind die Blenden- und Plattenangaben nicht mehr entzifferbar.
- 390_kopf.png — Kopfbereich bei 390 px, Chips und Überschrift sauber umgebrochen, keine
  Überlappung.
- 390_simulation_oben.png, 390_simulation_regler.png — Anzeigefelder und Regler bei 390 px: gut
  lesbar, Regler und Buttons ausreichend groß, kein Überlappen von Beschriftung und
  Schieberegler.
- 390_zuordnung.png — Zuordnungsaufgabe bei 390 px: Bahnbild und Zeilen klar getrennt, die
  kleinen Auswahlfelder (T3) sind erkennbar, aber optisch unauffällig, da rechtsbündig mit viel
  Weißraum drumherum.
- 390_tabelle.png — Eine Tabelle aus dem Erklärteil bei 390 px: intern abgeschnittene rechte
  Spalte sichtbar, Beleg für T1, gekapselter Scrollbereich der Tabelle selbst.
- druck_sim_bereich.png, druck_abschluss_bereich.png, druck_abschluss_ende.png — Druckansicht
  dreier Bereiche: Simulationsbox mit Standbild-Canvas und ausgeblendeten Reglern,
  Zentralabitur-Hinweis-Box und Selbstcheck-Liste am Dokumentende. Keine abgeschnittenen Kästen,
  Lehrerteil taucht nirgends auf.

Alle Skripte, mit denen diese Befunde erzeugt wurden, liegen im selben Arbeitsverzeichnis
(Unterordner nacharbeit, Dateien 01_laden.py bis 14_start_pause_reset.py); die Projektdatei
selbst wurde zu keinem Zeitpunkt verändert.
