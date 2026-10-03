# Technische Pruefung: module/info-q1-lineare-strukturen.html

## Urteil

**Nacharbeit noetig.**

Das Modul ist technisch, funktional und fachlich sehr solide (Engine-Vertraege korrekt,
alle Formeln offline lesbar, saubere Interaktion, korrekt gerechnete Musterloesungen,
inhaltliches statt pauschales Feedback bei allen Multiple-Choice-Optionen). Es gibt aber
einen klaren, leicht behebbaren Inhaltsfehler (Copy-Paste-Rest aus dem Referenzmodul in
der Fusszeile, siehe Blocker), der vor dem produktiven Einsatz korrigiert werden muss,
weil er auf jeder Bildschirmansicht und auf jedem Ausdruck sichtbar ist und ein falsches
Fach und Thema behauptet. Da der Fix trivial ist (eine Zeile) und sonst nichts gefunden
wurde, das den Unterrichtseinsatz inhaltlich oder technisch verhindert, ist die
Einstufung "Nacharbeit noetig" statt "durchgefallen".

## Blocker

- **Fusszeile nennt falsches Fach und falsches Thema (Copy-Paste-Rest aus dem
  Referenzmodul).** Fundstelle: module/info-q1-lineare-strukturen.html, Zeile 1146,
  im footer-Element am Ende von Abschnitt 7 (Abschluss). Text lautet wortwoertlich:
  "Physik LK Q1 - Elektromagnetische Induktion - erstellt fuer den Unterricht nach dem
  Kernlehrplan NRW fuer die gymnasiale Oberstufe." - das ist unveraendert die Fusszeile
  aus physik-q1-induktion.html (dort Zeile 577, identischer Wortlaut per Diff bestaetigt).
  Erwartet: ein Hinweistext zum tatsaechlichen Modul, z. B. "Informatik LK Q1 - Lineare
  Datenstrukturen - erstellt fuer den Unterricht nach dem Kernlehrplan NRW fuer die
  gymnasiale Oberstufe." Reproduktion: Seite in einem beliebigen Browser oeffnen, ganz
  nach unten scrollen (unterhalb "Didaktische Hinweise (Lehrkraft)"); der Fehler steht
  dort im Klartext.
  Per Playwright bestaetigt: document.querySelector('footer').textContent liefert den
  falschen Text sowohl im normalen Bildschirmmodus als auch nach
  emulateMedia({media:'print'}) (display: block, sichtbar) - der Fehler landet also
  auch auf dem gedruckten Arbeitsblatt. Alle anderen Stellen, die beim Kopieren haetten
  mitgezogen werden koennen (title-Tag, Export-Kopfzeile im Skript), wurden korrekt auf
  "Lineare Datenstrukturen" bzw. "Informatik LK Q1" angepasst - es handelt sich also um
  eine isolierte, beim Kopieren uebersehene Stelle, nicht um ein systematisches Problem.

## Maengel

- Keine weiteren gefunden. Insbesondere: keine NaN/undefined/Infinity in irgendeiner
  Anzeige nach systematischem Durchklicken; keine doppelten oder leeren Feedbacktexte;
  keine Konsole- oder pageerror-Meldungen in beiden Laufmodi (online/offline); kein
  waagerechtes Scrollen bei 1280/900/390 px; Formelfallback vollstaendig (79 von 79
  .m-Elementen mit Text, kein LaTeX-Rest); Zahleneingaben liefern in allen getesteten
  Faellen unterschiedliche, inhaltlich passende Rueckmeldungen; Zuordnung unterscheidet
  korrekt zwischen "nichts ausgewaehlt", "teilweise richtig" und "vollstaendig richtig";
  Export wirft nie und liefert einen korrekt formatierten Text mit deutschem Datumsformat;
  Musterloesungswerte nachgerechnet und korrekt (siehe Testabdeckung).
- Kleinere Beobachtung, kein eigener Mangel: Bei 390 px Breite sind einzelne Beschriftungen
  im Canvas der Simulation (z. B. das kleine "null" rechts neben dem letzten Knoten, das
  kopf-Label) recht klein, weil das Canvas mit width:100% aus 1000 px internem Format
  herunterskaliert wird. Das ist dieselbe, im Referenzmodul akzeptierte Technik
  (width="1000" plus width:100% per CSS) und damit keine modulspezifische Abweichung von
  der Vorlage; auf 1280/900 px gut lesbar, auf 390 px an der unteren Grenze, aber noch
  entzifferbar (siehe Screenshot slices390/sim-gefuellt2.png).

## Testabdeckung

**Automatischer Grundcheck** (modulcheck.py der Projektleitung, vor den eigenen Tests
gelaufen): 0 Blocker, 0 Maengel gemeldet. Deckt ab: Konsole/pageerror beim Laden,
Formelfallback offline (79 Formeln), MC-Engine-Vertraege, alle 7 Zahleneingaben mit je 4
Standardfaellen (richtig mit richtiger Einheit, richtig mit falscher Einheit, grob
falsch, leer), Zuordnung (vollstaendig-richtig-Fall plus Reihenfolgen-Check gegen
Diagrammreihenfolge), alle Hilfen und Loesungen aufgeklappt, Regler (keine vorhanden,
siehe unten), Export, Druckansicht, Dezimalkomma, Querscrollen bei 1280/900/390 px.

**Eigene ergaenzende Tests** (mehrere Playwright-Skripte im Arbeitsordner, siehe unten):

- Simulation im Betrieb: Alle drei Strukturen (Stapel, Schlange, Liste) je einzeln
  ausgewaehlt und alle zugehoerigen Operationsknoepfe (13 verschiedene insgesamt:
  push/pop/top, enqueue/dequeue/front, toFirst/next/append/insert/remove/setContent/
  getContent) mehrfach im Direktmodus geklickt (6 Runden je Struktur) - keine
  NaN/undefined/Infinity in Struktur-, Knoten-, Referenzaenderungs-, Besuchs- oder
  Rueckgabewert-Anzeige. Zuruecksetzen 5x hintereinander geklickt. Schritt-fuer-
  Schritt-Modus mit push("X") bis zum letzten Einzelschritt durchgeklickt (3 Schritte).
  Umschalten von Schrittmodus auf Direktmodus waehrend eine Operation laeuft getestet
  (die automatische restAusfuehren-Fortsetzung greift korrekt, kein Haengenbleiben).
  Randfall pop() auf leerem Stapel getestet: Struktur bleibt unveraendert (0/0/0/-),
  kein Fehler. Kein Ziehmodus und kein pointerdown/pointermove im Modul vorhanden
  (Quelltext durchsucht, keine Treffer) - dieser Pruefpunkt entfaellt fuer dieses Modul.
- Visuelle Obergrenze der Kette: 18 append-Aufrufe in Folge auf die Liste abgesetzt.
  Das Modul deckelt die Zeichnung bewusst bei 6 Knoten und zeigt dann den Hinweistext
  "Fuer die Zeichnung ist bei sechs Knoten Schluss. Nimm erst etwas heraus." - keine
  ueberlaufende oder abgeschnittene Zeichnung, Zaehler bleiben korrekt (Knoten 6,
  Referenzaenderungen 6, besuchte Knoten 15 = 0+1+2+3+4+5, rechnerisch nachgeprueft).
  Erholung nach dem Limit getestet: remove() senkt auf 5 Knoten, ein erneutes append
  fuellt wieder auf 6 - kein dauerhaft blockierter Zustand.
- Zuordnungsaufgabe, alle drei Zustaende: 4 Zeilen mit allen vier Loesungsoptionen
  getestet in den Zustaenden "nichts ausgewaehlt" (Rueckmeldung: "Es fehlen noch 4
  Zuordnungen"), "1 von 4 richtig" (inhaltliches Feedback zum Denkfehler, CSS-Klasse
  nein) und "4 von 4 richtig" ("Alle vier richtig", CSS-Klasse ok) - alle drei klar
  unterscheidbar.
- Mehrfachbedienung: MC vw1 zweimal mit unterschiedlichen Optionen beantwortet,
  Rueckmeldungstext aktualisiert sich korrekt. Erste Hilfe-Schaltflaeche 4x auf/zu
  geklickt ohne Fehler. Export-Knopf 3x hintereinander geklickt, wirft nie, liefert
  jedes Mal denselben korrekt formatierten Text (deutsches Datumsformat, korrekter
  Titel "Lineare Strukturen: Stapel, Schlange, Liste - Informatik LK Q1").
- Musterloesungen nachgerechnet (Werte aus numDaten ausgelesen und von Hand
  verifiziert): a1 = 2 Elemente (Kette A,E nach 5x push und 3x pop, stimmt); a2 = 3
  Referenzaenderungen bei insert mit Vorgaenger (stimmt); a3 = 3603 Knotenbesuche fuer
  3x append an eine wachsende 1200er-Liste ohne Endzeiger (1200+1201+1202=3603,
  stimmt); a4 = 4800 B / 4,8 kB Mehrbedarf der Verkettung gegenueber dem Array bei
  1200 Elementen und 4 B je Referenz (9600 minus 4800 gleich 4800, stimmt). Alle vier
  passen zu den im Erklaerteil hergeleiteten Formeln.
- Feedbackqualitaet MC: Alle 6 MC-Bloecke (18 Optionen insgesamt, je 3 Optionen)
  inhaltlich gelesen: jede falsche Option benennt einen konkreten Denkfehler (z. B.
  "Du behandelst die Zuweisung wie das Kopieren eines Wertes", "Du hast die beiden
  Zaehler vertauscht"), kein pauschales "Leider falsch".
- Tastatur: Tab-Navigation geprueft: Fokus erreicht turnusmaessig Eingabeelemente
  (erstes Tab-Ziel ist ein INPUT) und summary-Elemente von details-Bloecken
  (Textausschnitt "Der teuerste Anfaengerfehler...") - Fokusreihenfolge
  nachvollziehbar, keine Fokusfallen beobachtet.
- Regler: Das Modul hat keine input[type=range]-Regler (durch Grundcheck und eigene
  Zaehlung bestaetigt: 0 Stueck). Die Steuerung erfolgt ueber ein Textfeld ("Inhalt
  des naechsten Knotens"), eine Checkbox ("Schritt fuer Schritt") und Buttons -
  passend zum diskreten, schrittweisen Charakter des Themas (keine kontinuierliche
  physikalische Groesse). Der Pruefpunkt "Regler ueber den gesamten Bereich fahren"
  entfaellt daher inhaltlich; stattdessen wurden alle 13 Operationsknoepfe und alle 3
  Strukturknoepfe systematisch durchgeklickt (siehe oben). Ebenso hat das Diagramm
  keine mitwachsende Zeitachse (kein Zeitverlauf, sondern Zustandsdarstellung einer
  Kette) - stattdessen wurde die Obergrenze der Zeichenflaeche (6 Knoten) wie oben
  beschrieben geprueft.
- Zahlen im Ueberblick: 6 MC-Bloecke a 3 Optionen (18 Optionen einzeln angeklickt
  durch den Grundcheck), 7 Zahleneingaben a 4 Grundfaelle plus 1 Alternativeinheit-
  Fall bei a4 (29 Einzelpruefungen durch den Grundcheck), 1 Zuordnungsaufgabe mit 4
  Zeilen in 3 getesteten Gesamtzustaenden, 18 Hilfe-Schaltflaechen, 2 Musterloesungs-
  Schaltflaechen (AFB-III-Aufgaben mit Textarea), 13 Aufgaben insgesamt, 13 Operations-
  und 3 Strukturknoepfe der Simulation, 3 Screenshot-Breiten (1280/900/390 px) plus 19
  Bildschirmausschnitte der 900-px-Vollansicht einzeln angesehen, 1 Druckansichts-Lauf.

## Screenshots

Ablageort (Arbeitsordner, nicht im Projekt):
C:/Users/49176/AppData/Local/Temp/claude/C--Users-49176-Documents-Claude-Projects-Schule/5616889e-4b92-41aa-b192-9ce54df721fb/scratchpad/pruef/shots-info/

- info-q1-lineare-strukturen-1280.png, -900.png (Volldarstellung, 20938 px hoch - in
  19 Ausschnitten unter slices/slice-00.png bis slice-18.png einzeln angesehen),
  -390.png: Layout auf allen drei Breiten sauber, keine ueberlappenden Beschriftungen,
  keine abgeschnittenen Tabellen oder Diagrammachsen, Java-Codebloecke und
  KaTeX-Formeln (O(1), O(n), Speicherformeln mit korrektem Dezimalkomma wie "9,6 kB",
  "600,5") rendern korrekt auf allen Breiten. Einzig auffaellig: der unter Blocker
  beschriebene Fusszeilenfehler, sichtbar in slice-18.png (unterster Ausschnitt der
  900-px-Ansicht) und in slices390/footer.png (390 px).
- slices390/sim-top.png, sim-gefuellt2.png: Simulationsbereich bei 390 px -
  Struktur-Knoepfe, Operationsknoepfe und Anzeige-Kacheln brechen sauber um, wirken
  ausreichend gross fuer Touch-Bedienung; Canvas-Inhalt (Kette mit Knoten A bis D,
  Pfeile, kopf-Label) lesbar, kleine Labels wie oben erwaehnt an der unteren
  Groessengrenze.
- viele-knoten-liste.png: Zeigt die bewusste 6-Knoten-Obergrenze der Zeichnung mit
  Hinweistext, keine ueberlaufende Darstellung.
- druck-1280.png: Druckansicht - Reglerbereich, Knopfleisten, Hilfe-Knoepfe und
  Lehrerteil korrekt ausgeblendet, alle 13 Aufgaben sichtbar, Hilfetexte sichtbar,
  keine abgeschnittenen Kaesten. Die fehlerhafte Fusszeile ist in der Druckansicht
  ebenfalls sichtbar (siehe Blocker).

Testskripte im Arbeitsordner (zur Nachvollziehbarkeit, nicht Teil der Abgabe):
eigen_test.py, zuordnung_test.py, mc_feedback.py, num_daten.py, export_test.py,
druck_test.py, viele_knoten.py, nach_limit.py, slice900.py, slice390.py,
slice390b.py, slice390c.py.
