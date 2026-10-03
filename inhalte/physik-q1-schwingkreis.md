# Elektromagnetischer Schwingkreis — Inhaltsprotokoll

Stand: gebautes Modul `module/physik-q1-schwingkreis.html` (Physik LK Q1, Chip „Inhaltsfeld: Schwingende Systeme und Wellen“,
ca. 120 Minuten). Modulcheck ohne Blocker und Mängel, 440 von 440 Formeln gesetzt, kein Querscrollen bei 390, 900 und 1280 px.
Gebaut auf der Vorlage `physik-q1-mechanische-schwingungen.html`.

## Aufbau

| Abschnitt | Inhalt |
|---|---|
| 1 Einstieg | Warensicherungsetikett (Spule und Kondensator, etwa 8 MHz) und Radioabstimmung; vw1 Selbstinduktion (Strom klingt ab, kein Sprung), vw2 Energie im Feld des Kondensators, vw3 ω = 2π·f |
| 2 Grundlagen | Ablauf in Viertelperioden (Tabelle), Maschenregel −L·dI/dt = Q/C, L·Q'' + Q/C = 0, Thomson-Formel mit Herleitung, Q, U_C, I über der Zeit (SVG), Energie W_C = W₀cos², W_L = W₀sin², Analogie-Wörterbuch |
| 3 Vertiefung | R im Kreis, δ = R/(2L), R_ap = 2√(L/C), Energiebilanz W' = −R·I², Rückkopplung (Meißner 1913), angetriebener Kreis, Î(ω_e) aus der Mechanik übersetzt, Resonanz Î = U₀/R, Breite Δω = R/L, Abstimmung |
| 4 Simulation | Schaltbild, U_C(t) und I(t), unten Energien oder Resonanzkurve; Regler L, C, R, U₀, U_e, f_e |
| 5 Übungen | a1 bis a7; a3 ist die Zuordnungsaufgabe (I(t) gegen Ausgangskreis) |
| 6 Abschluss | Zusammenfassung, Zentralabitur-Hinweis, Selbstcheck, Export und Druck, Lehrerteil |

Formelleiste: 10 Einträge in zwei Gruppen (masche, bew-lc, thomson, schwingung-q, energie · bew-rlc, delta, grenz, energie-ab, istrom).
Nicht drin: I_max = U₀·√(C/L) und Î_res = U₀/R (würden sim1 und sim2 beantworten), ω = 2π·f (vw3).

## Konventionen

- Q ist die Ladung der oberen Platte, I zählt positiv, wenn sie diese Platte auflädt: I = Q'. Dann stimmen x ↔ Q und v ↔ I ohne Vorzeichenwechsel.
- Analogie: x → Q, v → I, m → L, D → 1/C, b → R, F → U_e.
- δ = R/(2L), ω_d = √(ω₀² − δ²); Î = ω_e·Q̂ mit Q̂ aus der Federpendel-Formel.

## Beispielkreis (Simulation und Text)

L = 0,100 H, C = 10 µF: ω₀ = 1000 s⁻¹, T₀ = 6,283 ms, f₀ = 159,15 Hz; U₀ = 10 V: Q₀ = 100 µC, I_max = 0,100 A, W₀ = 0,50 mJ.
R = 20 Ω: δ = 100 s⁻¹, ω_d = 994,99 s⁻¹, T_d = 6,315 ms, Λ = 0,631, Amplitudenfaktor 53,2 %, Energiefaktor 28,3 %. R_ap = 200 Ω.
Erreger U₀ = 5,0 V, R = 20 Ω: Î_res = 250 mA, bei 120 Hz 82 mA, bei 200 Hz 100 mA; Δω = R/L = 200 s⁻¹ (31,8 Hz).

## Aufgabenzahlen (nachgerechnet)

| Aufgabe | Ergebnis |
|---|---|
| a1 | L = 0,25 H, C = 4,7 µF: T₀ = 6,81 ms (f₀ = 146,8 Hz) |
| a2 | 100 MHz, 12 pF: L = 0,211 µH |
| a3 | L → 4L: Periode ×2, Strom ×½ (C); C → 4C: ×2, ×2 (A); L → L/4: ×½, ×2 (D); C → C/4: ×½, ×½ (B) |
| a4 | L = 25 mH, C = 4,0 µF: R_ap = 158 Ω |
| a5 | C = 20 µF, U₀ = 50 V, L = 80 mH: W = 25 mJ, I_max = 0,79 A |
| sim1 | C 5 µF → 20 µF (L = 0,10 H, U₀ = 10 V): T ×2, I_max 70,7 → 141 mA |
| sim2 | R 20 → 40 Ω in der Resonanz: Î 250 → 125 mA |

## Simulation, gegen exakte Rechnung geprüft

Playwright-Test: R = 0 bei sechs Kombinationen (W, I_max, T₀, f₀ stimmen); R = 20 Ω: Energie über acht Zeitpunkte gegen die exakte
Lösung (größte Abweichung 2 µJ bei Rundung der Zeitanzeige); erzwungen bei sechs Einstellungen: gemessene Stromamplitude gleich
Formel. Grenzfall-Knopf stellt 200 Ω ein. Keine Konsolenfehler.

Nachtrag 02.10.2026: Die Knöpfe „Energien“ und „Resonanzkurve“ zeigten nicht an, welche Ansicht aktiv ist. Das Bauskript fügt
jetzt die CSS-Regel `.sim .knopfleiste button[aria-pressed="true"]` ein (aktiver Knopf blau hinterlegt). Neu gebaut, einzige
Änderung im Ergebnis ist diese Zeile; im Browser geprüft, Modulcheck wiederholt.

## Quellen für Angaben im Text (Websuche, Stand 10/2026)

- RF-Warensicherung arbeitet häufig bei 8,2 MHz (Patentschriften, Hersteller); die Werte 5,5 µH und 68 pF im Einstieg sind Rechenbeispiele.
- Alexander Meißner, Rückkopplungsschaltung, Patent 1913 (Deutsche Biographie, Lernhelfer).
- Thomsonsche Schwingungsformel, William Thomson 1853: nicht per Suche geprüft, aus Fachwissen.

## Offen

- Kernlehrplan: Steht der elektromagnetische Schwingkreis im schulinternen Lehrplan bei „Schwingende Systeme und Wellen“ oder bei
  „Ladungen, Felder und Induktion“? Pflichtstatus von Rückkopplung, Resonanzbreite und Dämpfungsfällen im Schwingkreis. Keine Zitate erfunden.
- Vorzeichenkonvention (I = Q') ist eine Festlegung des Moduls; Bücher mit positivem Entladestrom schreiben I = −Q'.
- Fachliche Gegenprobe der Erklärtexte durch eine zweite Person.
