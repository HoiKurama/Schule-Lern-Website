# Arbeitsstand — Durchgang 2

> **Nachtrag 03.10.2026.** Auf Wunsch des Nutzers ist die Regel „kein `localStorage`“ gelockert.
> Alle 19 Module haben den Link „← Zur Übersicht“ im Kopf und am Skriptende den generischen
> Speicherblock (`vorlage/bausteine.md` § 9): Stand je Modul unter `q1lernen:<datei>.html`,
> Wiederherstellung durch nachgespielte Klicks, Löschknopf neben dem Export. `index.html` zeigt je
> Kachel „Dein Stand: x von y Aufgaben richtig“ und hat einen Löschknopf für alle Module.
> Beobachtet beim Einbau, nicht behoben: Die Hilfe-Engine hängt ihren Musterlösungs-Klick an
> `[data-loesung]`, das trifft auch `.zeile[data-loesung]` der Zuordnung. Folgenlos, solange die
> Zuordnungsaufgabe keinen `.hilfe-text[data-stufe="9"]` hat.
> Einschränkung: Firefox trennt `file://`-Seiten in eigene Ursprünge – dort sieht die Übersicht
> den Stand der Module nur, wenn die Seiten über einen Webserver laufen.

> **Nachtrag 29.09.2026.** Der Rest dieser Datei beschreibt den Stand vom 16.09. Seitdem gilt:
> Durchgang 2 und 3 sind fertig (10 Module, siehe `fachliches/modulliste.md`), Durchgang 4 ist
> noch nicht gestartet. Die aktuelle Übergabe steht in `.claude/handoff/latest.md`.
>
> - Formelleiste und Druckmodi existieren nur im Referenzmodul `physik-q1-induktion`. Die drei
>   Prüferbefunde dazu sind behoben: Die Simulation zeigt Φ je Windung (N geht nur in U ein), die
>   Vorwissensfrage nach der Einheit von B ist durch eine Frage zur Bahnform im Magnetfeld ersetzt,
>   die Gültigkeit von U = −N·B·l·v war bereits ergänzt. Modulcheck: keine Blocker, keine Mängel.
> - **Formelleiste und Druckmodi stehen jetzt in allen zehn fertigen Modulen**; der Modulcheck meldet
>   überall `blocker: []` und `maengel: []`. Die Zeilenenden der Module sind unverändert. Bei der
>   Übernahme wurde `formelDaten` gegen jede Vorwissens- und Simulationsfrage geprüft. Deshalb fehlen
>   bewusst: im E-Feld-Modul das Coulombgesetz, E(r) und das Potenzial (Vorwissensfragen 1 und 2
>   fragen genau danach), im Magnetfeld-Modul F = B·I·l und B = F/(I·l) (Vorwissensfrage 2), im
>   Teilchenmodul y(x) im Querfeld ist enthalten, aber ohne den Satz „Ladung und Masse kürzen sich
>   heraus“. Wer die Leiste dort erweitern will, muss die Frage austauschen.
> - Altfehler beim Übernehmen: In `mathe-q1-hauptsatz` stand ein BEL-Zeichen (0x07) in einer Formel
>   (`\approx` war zu `\a` + `pprox` geworden). Behoben.
> - Der Modulcheck wartet beim Sprunglink-Test jetzt, bis das weiche Scrollen zur Ruhe gekommen ist
>   (`_warte_ruhe` in `werkzeug/pruefschritte/formelleiste.py`). Vorher gab es auf langen Seiten
>   Fehlalarme („Ziel steht nicht im Bild“).
> - Die Portierung liegt als Skript im Verlauf dieser Sitzung; für neue Module gilt weiter die
>   Kopieranleitung in `vorlage/baustein-formelleiste.md`.
> - `index.html` ist jetzt ein Lernpfad: nummerierte Schritte je Inhaltsfeld, Voraussetzung je
>   Schritt, geplante Module ein- und ausblendbar, Zähler und Zeiten aus dem Markup berechnet.
> - Playwrights eigenes Chromium fehlt; `werkzeug/pruefschritte/browser.py` weicht auf Chrome/Edge
>   aus. Eigene Prüfskripte sollten `browser_starten(p)` von dort benutzen.

Stand: 16.09.2026. Übergabe an die nächste Sitzung. Was fertig ist, was läuft, und welche
Fallstricke schon bezahlt wurden.

---

## 1 · Kurzfassung

**Durchgang 1 ist abgeschlossen und abgenommen.** Vier Module und die Übersichtsseite stehen:

| Modul | Status |
|---|---|
| `physik-q1-induktion` | **fertig** (Referenzmodul, war schon vorher fertig) |
| `mathe-q1-integral-rekonstruktion` | **fertig** |
| `info-q1-lineare-strukturen` | **fertig** |
| `physik-q1-magnetisches-feld` | **fertig** — Wien-Filter am 16.09. abgenommen |
| `index.html` | **fertig** |

**Durchgang 2 läuft.** Auf ausdrückliche Weisung des Nutzers wird **Informatik vorerst nicht
weiterbearbeitet** — nur Physik und Mathematik. Drei Module sind in Arbeit:

| Modul | Fach | Stufe |
|---|---|---|
| `physik-q1-elektrisches-feld` | Physik | 1 – Inhalt (`fachdidaktik`) |
| `mathe-q1-hauptsatz` | Mathematik | 1 – Inhalt (`fachdidaktik`) |
| `mathe-q1-ableitungsregeln` | Mathematik | 1 – Inhalt (`fachdidaktik`) |

Als Erstes prüfen, ob die Inhaltsdateien in `inhalte/` liegen und was `git status` zeigt:

```bash
cd "C:/Users/49176/Documents/Claude Projects" && git status --short Schule
```

---

## 2 · Was als Nächstes zu tun ist

1. Die drei Inhaltsdateien in `inhalte/` **selbst lesen** und zurückweisen, wenn
   Musterlösungen ungerechnet sind, Distraktoren kein inhaltliches Feedback haben oder das
   Niveau unter Leistungskurs liegt.
2. Stufe 2: je ein `modulbauer` pro Modul, Simulation zuerst (siehe Abschnitt 5).
3. Stufe 3: `fachpruefung` und `qa-technik` parallel, dazu `werkzeug/modulcheck.py`.
4. Stufe 4: Befunde gebündelt zurück an `modulbauer`, danach nur die beanstandeten Punkte
   erneut prüfen.
5. `index.html` um die neuen Kacheln ergänzen und die Zähler („2 von 9 Modulen") anpassen.
   Diese Datei und `fachliches/modulliste.md` schreibt **ausschließlich die Projektleitung**,
   nie ein Subagent.

Danach in der Reihenfolge des Schuljahres weiter, weiterhin ohne Informatik:
`physik-q1-geladene-teilchen-e-feld`, `mathe-q1-funktionsuntersuchung`,
`mathe-q1-exponentialfunktionen`, `mathe-q1-flaechen-zwischen-graphen`,
`physik-q1-selbstinduktion`, dann Vektorgeometrie sowie Schwingungen und Wellen.

---

## 3 · Umgebung (spart die teuersten Sackgassen)

- **Node.js und npm gibt es auf diesem Rechner nicht.** Playwright liegt als **Python-Paket**
  vor, Chromium ist installiert: `from playwright.sync_api import sync_playwright`
- Python 3.13 liegt als `python` im PATH. **`numpy` ist nicht installiert** — Rechnungen
  laufen mit der Standardbibliothek.
- Bei Sonderzeichen in der Konsolenausgabe **`PYTHONIOENCODING=utf-8`** setzen, sonst bricht
  es mit `UnicodeEncodeError` ab.
- Die vier Subagenten unter `.claude/agents/` sind namentlich aufrufbar:
  `fachdidaktik`, `modulbauer`, `fachpruefung`, `qa-technik`.
- Git-Wurzel ist `Claude Projects`, nicht `Schule`. Also `git add Schule`, nicht `git add .`.

### Skripte nie über ein Heredoc an Python geben

`python - <<'PY' … PY` **frisst Backslashes**: aus `\\varepsilon` wird `\varepsilon` und
daraus in Python ein Vertikaltabulator plus `arepsilon`. So landen unsichtbare Steuerzeichen
in `data-tex`, und KaTeX meldet wegen `throwOnError:false` nichts. Genau dieser Fehler ist am
16.09. entstanden und musste zurückgenommen werden. Richtig: das Skript mit `Write` als Datei
anlegen und dann aufrufen. Eine Zusicherung am Ende jedes Ersetzungsskripts kostet nichts:

```python
schlecht = [hex(ord(c)) for c in s if ord(c) < 32 and c not in "\n\r"]
assert not schlecht, "Steuerzeichen im Dokument: %s" % schlecht
```

### Prüfwerkzeug

`werkzeug/modulcheck.py` liegt jetzt **im Repository** und überlebt die Sitzung:

```bash
PYTHONIOENCODING=utf-8 python werkzeug/modulcheck.py "module/DATEI.html"
```

Er prüft Konsole und `pageerror`, die Engine-Verträge (Optionszahl gegen Feedbackzahl,
`data-i`-Lücken, radio-Namen), alle Fälle jeder Zahleneingabe, die Zuordnung, alle Hilfen,
jeden Regler über seinen ganzen Bereich, den Export, die Druckansicht, den Offline-Fallback und
waagerechtes Scrollen bei 1280, 900 und 390 px. Ein zweites Argument legt einen Ordner für
Bildschirmfotos an. Ausgabe ist JSON mit `blocker` und `maengel`.

**Maßstab:** Alle vier fertigen Module laufen ohne Blocker und ohne Mängel durch.

---

## 4 · Der Wien-Filter, abgeschlossen am 16.09.

Der Befund aus Durchgang 1 lautete: Die Platten waren mit L = 10,0 cm länger als der
Zyklotronradius (r = 1,53 cm beim Proton), das Teilchen lief 1,04 volle Umläufe und traf die
Blende deshalb ein **zweites Mal** bei 792 bis 958 V — mit bis zu 32 % falscher Geschwindigkeit.
Die Simulation widerlegte damit genau den Merksatz, den sie stützen sollte.

Die neue Geometrie: **L = 8,0 mm, d = 2,0 cm, Driftstrecke D = 32,4 cm, Blende ± 2,0 mm.**

Nachgerechnet wurde nicht mit dem Integrator der Seite, sondern unabhängig gegen die **exakte
Zykloidenlösung** der gekreuzten Felder:

    vx = v_d + u₀·cos(ωt)      x = v_d·t + (u₀/ω)·sin(ωt)
    vy =       u₀·sin(ωt)      y = (u₀/ω)·(1 − cos(ωt))       u₀ = v − v_d,  ω = qB/m

84 Fälle: vier Teilchenarten × drei Flussdichten (Reglerminimum, Startwert, Maximum) × sieben
Beschleunigungsspannungen von 200 bis 1800 V. Ergebnis in **jedem** Fall genau ein
zusammenhängendes Durchlassfenster um U_P = v·B·d, größte Randabweichung 4,34 %. Kriterien
erfüllt.

Aus derselben Rechnung folgt die Toleranz in geschlossener Form — sie wird in der nächsten
Prüfung gebraucht und hat zwei Textfehler aufgedeckt:

    |ε|_max ≈ y_B · r / ( L · (L/2 + D) )

- Der Bedienhinweis behauptete, der Filter verzeihe „ungefähr ein Drittel Prozent". Tatsächlich
  sind es je nach Einstellung 0,5 bis 4,3 %. Korrigiert und zugleich zum Beobachtungsauftrag
  umgebaut.
- Der Lehrerteil behauptete, ein **kleineres** B mache den Filter schärfer. Die Formel sagt das
  Gegenteil: Die Toleranz wächst mit r, also macht ein **größeres** B den Filter schärfer.
  Probe in der Simulation: Proton bei U = 450 V verzeiht bei B = 110 mT rund 1,9 %, bei
  B = 300 mT nur noch 0,8 %. Korrigiert, mit Herleitung im Text.

Der zweite Befund — der B-Regler sprang beim Teilchenwechsel auf den Startwert der neuen Art
und machte Teil C des Beobachtungsauftrags unausführbar — ist ebenfalls behoben: `setzeBRegler`
behält den alten Wert und klemmt ihn nur in den neuen Bereich.

---

## 5 · Fachliche Abnahmekriterien der fertigen Module

Von der Projektleitung unabhängig nachgerechnet. Jedes deckt die Falle auf, in die eine falsch
gebaute Simulation läuft.

**Mathe** — die Ratenfunktion `f(t) = −0,2 t² + 1,6 t + 1,8` ist nicht monoton, Scheitel bei
`t = 4,0`. Bei `b = 6,0` und `n = 4`:

    U₄ = 21,825    O₄ = 27,750    O₄ − U₄ = 5,925

Ohne Scheitelbehandlung kommt `O₄ = 27,675` heraus — beides sieht plausibel aus, nur eines ist
richtig. Weiter: `n = 8 → 2,9906`, `n = 12 → 2,000`, `n = 16 → 1,4988`. Exakt `I(6) = 25,2`.
**Der Hauptsatz ist dort noch nicht eingeführt** — kein Text darf `∫f = F(b) − F(a)` behaupten.
Genau diese Lücke schließt das laufende Modul `mathe-q1-hauptsatz`.

**Info** — die Kette muss durch Verfolgen der Referenzen entstehen, nicht aus einem Array. Ein
Array sähe identisch aus und wäre fachlich falsch. Prüfbar über die Zähler:

| fünfmal auf die leere Struktur | Kette | Referenzänderungen | Knotenbesuche |
|---|---|---|---|
| `push` (Stapel) | E, D, C, B, A | 10 | 0 |
| `enqueue` (Schlange) | A, B, C, D, E | 10 | 0 |
| `append` (Liste) | A, B, C, D, E | 5 | 10 |

Gleiche Kette bei `enqueue` und `append`, aber unterschiedliche Zähler — das ist der didaktische
Kern. Zusätzlich: `toFirst()` plus dreimal `next()` ergibt 4 Knotenbesuche (k+1 für k = 3).

**Physik** — `v = √(2|q|U/m)`, `r = m·v/(|q|B)`, `T = 2π·m/(|q|B)`:

| Fall | v | r | T |
|---|---|---|---|
| Elektron, U = 1000 V, B = 3,00 mT | 1,875537·10⁷ m/s | 3,5545 cm | 11,908 ns |
| Proton, U = 1000 V, B = 130 mT | 4,376947·10⁵ m/s | 3,5149 cm | 504,57 ns |
| Neon-20, U = 2000 V, B = 600 mT | 1,389139·10⁵ m/s | 4,7991 cm | 2,1707 µs |

**Wichtigste Probe:** `T` darf sich beim Verstellen von `U` nicht ändern. Vervierfacht man `U`,
verdoppeln sich `v` und `r`, `T` bleibt gleich.

---

## 6 · Was an der gemeinsamen Vorlage geändert wurde

Alles vom Nutzer ausdrücklich freigegeben, jeweils in **allen** Modulen nachgezogen, damit CSS
und Engine überall identisch bleiben. Die Verträge stehen in `vorlage/bausteine.md`.

**Querscrollen bei 390 px, in drei Schritten behoben.** Erst bekamen Blockformeln und Tabellen
einen eigenen Scrollbereich, dazu den Wrapper `<div class="tabelle">` — der muss von Hand
gesetzt werden. Dann zeigte sich, dass auch lange Formeln im Fließtext schoben: `.m` trägt
`white-space:nowrap` und ist deshalb ein `inline-block` mit eigenem Scrollbereich. Zuletzt
blieben 3 px vom Tabellen-Wrapper; die Mindestbreite steht nun auf `min(420px, 100%)`.

**Zahlen-Engine, zwei Korrekturen.** Sie prüfte die Alternativeinheit relativ mit 3 %, die
Haupteinheit absolut — 26500 Wh galten als richtig (2,9 % daneben), 25,80 kWh als falsch
(0,19 % daneben). Jetzt wird die Toleranz mit demselben Faktor umgerechnet wie der Sollwert;
steht in `alt` eine eigene `tol`, gilt die. Dazu fängt eine Schranke `eps` den Grenzfall ab, an
dem `Math.abs(v - wert) <= tol` an der Fließkommadarstellung scheitert. Zweite Korrektur: Die
Weiche zwischen „knapp daneben" und „weit daneben" maß immer am Hauptwert; sie bezieht sich
jetzt auf die Einheit, in der geantwortet wurde.

---

## 7 · Fallstricke, die schon Zeit gekostet haben

**Das Nutzungslimit trifft ohne Vorwarnung und hat in einer Sitzung rund fünfzehn Agenten
mitten in der Arbeit beendet.** Der einzige wirksame Schutz ist Zwischenspeichern: Datei zuerst
anlegen, dann abschnittsweise mit `Edit` füllen, nie mehr als sechs bis acht Werkzeugaufrufe
ohne gespeicherten Stand. Parallele Agenten verbrauchen **nicht** mehr Token als sequenzielle,
nur schneller — Serialisierung verhindert keinen einzigen Abbruch und kostet nur Wartezeit.

**Bauagenten arbeiten von oben nach unten und sterben vor dem Skript.** Die Simulation steht am
Dateiende, deshalb fehlte sie dreimal hintereinander — der teuerste Teil. Konsequenz:
**Simulation zuerst bauen**, Markup-Aufräumen danach.

**Ein Agentenbericht ist eine Behauptung.** Ein Bauagent meldete ein Modul als fertig, das ab
Abschnitt 5 noch die Lenzsche Regel aus dem Referenzmodul enthielt und beim Laden einen
`getContext`-Fehler warf. Jedes Ergebnis selbst nachmessen. Auch der Wien-Filter-Umbau galt als
erledigt und enthielt noch zwei falsche Textaussagen, die erst die eigene Rechnung aufdeckte.

**Was Prüfagenten gefunden haben, das kein automatischer Check erwischt:**
- ein **literales Tabulatorzeichen** in `data-tex`; KaTeX läuft mit `throwOnError:false` und
  meldete nichts, im Browser stand sichtbar „vext−t-Diagramm"
- die Fußzeile des Referenzmoduls in einem Informatikmodul, auch im Ausdruck sichtbar
- Vorwissensfragen mit den **Antwortschlüsseln des Referenzmoduls**: zwei von drei hätten die
  falsche Antwort als richtig gewertet
- ein Widerspruch zwischen Text und Simulation: derselbe Zeigerschritt zählte einmal als
  Knotenbesuch, einmal als Referenzänderung

**Engine-Verträge, die tatsächlich gebrochen wurden:** Die Zahl der Feedbacktexte in `mcDaten`
muss der Zahl der Optionen im Markup entsprechen. `var ergebnisse` wird am **Skriptende**
deklariert, in den Engines darüber aber benutzt — das funktioniert nur wegen `var`-Hoisting, die
Reihenfolge darf nicht geändert werden. Pro Modul ist nur **eine** Zuordnungsaufgabe möglich
(`querySelector`, Einzahl).
> - **Durchgang 4, Modul 1: `physik-q1-selbstinduktion` ist fertig** (Modulcheck ohne Befund, in `index.html`
>   und `fachliches/modulliste.md` eingetragen). Simulation: RL-Kreis mit Einschalten, Ausschalten, Glimmlampe,
>   Freilaufzweig R_S und Funke (Modellannahme 5000 Ω). Die Zahlen der Aufgaben sind nachgerechnet.
>   Noch offen: fachliche Gegenprobe der Erklärtexte durch eine zweite Person. Als Nächstes:
>   `physik-q1-mechanische-schwingungen`, `mathe-q1-exponentialfunktionen`, `mathe-q1-vektoren-grundlagen`.
> - **Durchgang 4, Modul 2: `physik-q1-mechanische-schwingungen` ist fertig** (Modulcheck ohne Blocker und Mängel,
>   in `index.html` und `fachliches/modulliste.md` eingetragen). Simulation: Federpendel mit RK4, Dämpfung,
>   Erregung, x-t-Diagramm mit Hüllkurve, Resonanzkurve aus der Formel; gemessene Amplitude stimmt mit der
>   Formel überein (Probe bei vier Einstellungen). Aufgabenzahlen nachgerechnet.
>   **Formelleiste bewusst ohne** F = −D·x, Energiesumme und f = 1/T (sie wären Lösungen der Vorwissensfragen).
>   **KaTeX-Falle:** ein Leisteneintrag, der mit einem Subskript beginnt (`x_{\max} = …`), überdeckt mit seinen
>   `pstrut`-Spans den Sprunglink des Eintrags darüber (Playwright: „intercepts pointer events"). Die Reihenfolge
>   ändert daran nichts. Abhilfe ohne Vorlagen-CSS: Eintrag mit `\hat{x}` beginnen; bei Überbreite `\small`.
>   Dafür steht die Amplitude der erzwungenen Schwingung dort als x̂ (im Text erklärt).
>   Noch offen: fachliche Gegenprobe der Erklärtexte durch eine zweite Person; Kernlehrplan-Fragen (Stellung von
>   Dämpfung/Resonanz in Q1, log. Dekrement Pflicht?, Abiturverbindlichkeit). Als Nächstes:
>   `mathe-q1-exponentialfunktionen`, `mathe-q1-vektoren-grundlagen`, `physik-q1-schwingkreis`.
> - **Durchgang 4, Modul 3: `mathe-q1-exponentialfunktionen` ist fertig** (Modulcheck ohne Blocker und Mängel, 409 von
>   409 Formeln, in `index.html` und `fachliches/modulliste.md` eingetragen, Protokoll in
>   `inhalte/mathe-q1-exponentialfunktionen.md`). Simulation: drei konstruierte Messreihen (Bakterien, Koffein, Kaffee),
>   exponentielles und beschränktes Modell, oberes Diagramm Modell gegen Messwerte, unteres Änderungsrate gegen Bestand,
>   Bestanpassung nach kleinster mittlerer Abweichung. Zahlen der Aufgaben nachgerechnet, sim1/sim2 in der Oberfläche geprüft.
>   Formelleiste bewusst ohne „gleiche Quotienten“ und 2^(−3). **KaTeX-Falle:** `€` in `data-tex` erzeugt Warnungen,
>   `\text{Euro}` verwenden.
>   Noch offen: Kernlehrplan-Fragen (logistisches Wachstum in Q1 LK?, ln als Funktion samt Ableitung?, e über Differenzen-
>   quotient oder (1+1/n)ⁿ), fachliche Gegenprobe der Texte. Als Nächstes nur auf Wunsch:
>   `mathe-q1-vektoren-grundlagen`, `physik-q1-schwingkreis`.
> - **Durchgang 4, Modul 4: `mathe-q1-vektoren-grundlagen` ist fertig** (Modulcheck ohne Blocker und Mängel, 403 von
>   403 Formeln, in `index.html` und `fachliches/modulliste.md` eingetragen, Protokoll in
>   `inhalte/mathe-q1-vektoren-grundlagen.md`). Simulation: Pfeilkette r·a, s·b, t·c im Schrägbild zu einem Zielpunkt,
>   drei Datensätze (unabhängig, c = a − b, b = −2a) mit je zwei Zielpunkten; alle Anzeigen gegen exakte Handrechnung
>   geprüft. Drei Abbildungen im Erklärteil als Inline-SVG. Formelleiste mit 10 Einträgen, bewusst ohne die Regeltabelle.
>   **Fallen:** `\vec{p}\,'` ist in KaTeX ungültig (anderen Buchstaben nehmen); Formeln, die auf `\vec{d}` enden, ragen im
>   Druck 3 px über den Rand (`\;` ans Ende); Tipp-Texte dürfen nicht wortgleich mit sichtbaren Sätzen beginnen;
>   Vorzeichen nach `|` brauchen `{-}`, sonst entsteht eine Lücke wie bei einer Subtraktion.
>   Noch offen: Kernlehrplan-Tiefe zu linearer Unabhängigkeit, Basis und Komplanarität, fachliche Gegenprobe der Texte.
>   Als Nächstes nur auf Wunsch: `physik-q1-schwingkreis`; in der Mathematik `mathe-q1-geraden-ebenen`.
> - **Durchgang 4, Modul 5: `physik-q1-schwingkreis` ist fertig** (Modulcheck ohne Blocker und Mängel, 440 von 440 Formeln,
>   in `index.html` und `fachliches/modulliste.md` eingetragen, Protokoll in `inhalte/physik-q1-schwingkreis.md`). Gebaut auf der
>   Vorlage `physik-q1-mechanische-schwingungen.html`. Simulation: Reihenkreis mit RK4, Schaltbild (Ladung, Feld, Strom),
>   U_C(t) und I(t), unteres Diagramm wahlweise gestapelte Energien oder Resonanzkurve; Zeitlupe 1 s = 5 ms. Alle Anzeigen im
>   Browser gegen die exakte Lösung geprüft (Energie, Imax, Periode, Î in der Resonanz). Formelleiste mit 10 Einträgen, bewusst
>   ohne I_max = U₀·√(C/L) und ohne Î_res = U₀/R (sie würden sim1 und sim2 beantworten).
>   **Fallen:** Ein Leisteneintrag mit `\small` und langer Wurzel war 210 statt 204 px breit, `\footnotesize` löst es.
>   Vorzeichen: I zählt positiv, wenn sie die obere Platte auflädt (I = Q'); steht so im Text und im Lehrerteil.
>   Noch offen: Einordnung des Schwingkreises im Kernlehrplan (Chip nennt „Schwingende Systeme und Wellen“), Pflichtstatus von
>   Rückkopplung und Resonanzbreite, fachliche Gegenprobe der Erklärtexte. Als Nächstes nur auf Wunsch: `mathe-q1-geraden-ebenen`
>   oder `physik-q1-wellen`.
> - **Durchgang 4, Modul 6: `mathe-q1-geraden-ebenen` ist fertig** (Modulcheck ohne Blocker und Mängel, 504 von 504 Formeln,
>   in `index.html` und `fachliches/modulliste.md` eingetragen, Protokoll in `inhalte/mathe-q1-geraden-ebenen.md`). Gebaut auf
>   der Vorlage `mathe-q1-flaechen-zwischen-graphen.html` mit dem Bauskript des Vektoren-Moduls. Simulation: Ebene in
>   Parameterform im Schrägbild mit Normalenvektor und Probepunkt Q, drei Datensätze; Maßstab und Mitte werden je Datensatz
>   berechnet. Alle Anzeigen im Browser gegen exakte Rechnung geprüft (n∘X ist bei 49 Einstellungen konstant gleich d, Q1 wird
>   getroffen, Q2 nicht). Formelleiste mit 8 Einträgen, drei Abbildungen als Inline-SVG.
>   **Fallen:** In `formelDaten` muss `abschnitt` genau die `id` der `<section>` sein, sonst meldet der Check einen Blocker und
>   alle Sprungziele als Mangel. Koordinatentupel wie `(3|2)` bekommen im Bauskript automatisch `\,|\,` (`koordstrich`).
>   **Entscheidung ohne Rückfrage:** Das Skalarprodukt steht schon hier minimal (Komponentenformel, Orthogonalität), weil die
>   Normalenform es braucht; die Planung nennt es erst im Modul „Abstände und Winkel“.
>   Noch offen: Einordnung des Skalarprodukts in der Unterrichtsfolge, Pflichtstatus von Kreuzprodukt und Achsenabschnittsform,
>   fachliche Gegenprobe der Erklärtexte. Als Nächstes nur auf Wunsch: `mathe-q1-lagebeziehungen` oder `physik-q1-wellen`.
>
> - **Durchgang 4, Modul 7: `mathe-q1-lagebeziehungen` ist fertig** (Modulcheck ohne Blocker und Mängel, 352 von 352 Formeln,
>   kein Querscrollen, in `index.html` und `fachliches/modulliste.md` eingetragen, Protokoll in `inhalte/mathe-q1-lagebeziehungen.md`).
>   Gebaut mit dem Bauskript des Moduls „Geraden und Ebenen“. Simulation: Gerade und Ebene im Schrägbild, Anzeige von n∘X − d
>   entlang der Geraden, drei Datensätze (ein Schnittpunkt, parallel, Gerade liegt in E); im Browser gegen exakte Rechnung geprüft
>   (alle Anzeigen bei 9 Reglerstellungen je Datensatz, keine Konsolenfehler). Gerade/Gerade und Ebene/Ebene stehen nur im Text
>   und in Abbildungen, ohne Simulation. Alle Zahlen in Text und Aufgaben mit `zahlen.py` nachgerechnet.
>   **Entscheidung ohne Rückfrage:** Gleichungssysteme nur durch Einsetzen und Addieren, Gauß-Verfahren und Kreuzprodukt nicht eingeführt.
>   Noch offen: Gauß-Verfahren in Q1 (Kernlehrplan), Ebenen in Parameterform ohne Umwandlung, fachliche Gegenprobe der Erklärtexte.
>   Als Nächstes nur auf Wunsch: `physik-q1-wellen` oder `mathe-q1-abstaende-winkel`.
>
> - **Durchgang 4, Modul 8: `physik-q1-wellen` ist fertig** (Modulcheck ohne Blocker und Mängel, 341 von 341 Formeln, kein
>   Querscrollen, in `index.html` und `fachliches/modulliste.md` eingetragen, Protokoll in `inhalte/physik-q1-wellen.md`).
>   Gebaut auf der Vorlage `physik-q1-mechanische-schwingungen.html` mit dem Bauskript des Schwingkreis-Moduls. Inhalt: Welle als
>   Kette von Schwingungen, c = λ·f, Wellenfunktion, Superposition, Gangunterschied, Reflexion (festes/loses Ende), stehende Welle
>   aus Superposition hergeleitet, Saite und Pfeife. Simulation „Seilwelle“ in drei Einstellungen (laufende Welle, zwei Wellen,
>   stehende Welle am Seil), Momentaufnahme oben, Zeitverlauf an einem Ort unten; alle Kurven werden aus den Formeln berechnet.
>   Im Browser gegen exakte Rechnung geprüft (alle Anzeigen, Amplituden und Gangunterschiede, keine Konsolenfehler).
>   **Falle:** Umschaltknöpfe (`aria-pressed`) haben im Grundgerüst kein sichtbares Aktiv-Zeichen. Das Bauskript ergänzt
>   eine CSS-Regel; im Schwingkreis (Energien/Resonanzkurve) ist sie nachgetragen und im Browser geprüft. „Mechanische
>   Schwingungen“ hat keine solchen Knöpfe und war nicht betroffen.
>   **Entscheidung ohne Rückfrage:** c = √(F/μ) für die Saite steht ohne Herleitung im Text; Gangunterschied nur eindimensional.
>   Noch offen: Kernlehrplan-Tiefe (Wellenfunktion, Saiten und Pfeifen), fachliche Gegenprobe der Erklärtexte.
>   Als Nächstes nur auf Wunsch: `physik-q1-doppelspalt-gitter` oder `mathe-q1-abstaende-winkel`.
>
> - **Durchgang 4, Modul 9: `physik-q1-doppelspalt-gitter` ist fertig** (Modulcheck ohne Blocker und Mängel, kein Querscrollen
>   bei 390, 900 und 1280 px, in `index.html` und `fachliches/modulliste.md` eingetragen, Protokoll in
>   `inhalte/physik-q1-doppelspalt-gitter.md`). Gebaut auf der Vorlage `physik-q1-mechanische-schwingungen.html` mit dem Bauskript
>   des Wellen-Moduls (jetzt sechs Teildateien). Inhalt: Kreiswellen und Huygens’sches Prinzip, Beugung, Gangunterschied in der
>   Ebene (Hyperbeln als Details), Kohärenz, Doppelspalt (Δs = g·sin α im Fernfeld, Maxima und Minima, Lage auf dem Schirm,
>   Wellenlängenbestimmung, Intensität und Einhüllende als Details), Gitter (d = 1/z, scharfe Maxima, höchste Ordnung, Spektren
>   und Überlappung). Simulation in drei Einstellungen: Wellenwanne mit zwei Quellen (Messpunkt P, Hyperbeln, Zeitverlauf der
>   Teilwellen), Doppelspalt und Gitter (Schirmbild und Intensität aus den Fernfeldformeln, auch weißes Licht).
>   Im Browser gegen exakte Rechnung geprüft (Anzeigen der Wellenwanne, Lage der Maxima in Schirmbild und Kurve, Farbreihenfolge).
>   **Entscheidung ohne Rückfrage:** Das Gitter ist in der Simulation auf N = 12 Spalte begrenzt und die Spaltbreite auf 0,2·d
>   festgelegt (sonst fallen höhere Ordnungen aus); bei weißem Licht ist die Helligkeit der Spektren um den Faktor 5 angehoben.
>   Noch offen: Einordnung von Doppelspalt und Gitter im schulinternen Lehrplan (Inhaltsfeld und Jahrgang), Tiefe der
>   Intensitätsverteilung, fachliche Gegenprobe der Erklärtexte.
>   Als Nächstes nur auf Wunsch: `mathe-q1-abstaende-winkel` oder ein Informatik-Modul.
