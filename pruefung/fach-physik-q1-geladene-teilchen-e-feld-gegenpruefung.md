# Gegenprüfung `module/physik-q1-geladene-teilchen-e-feld.html`

Prüfer: fachpruefung. Von der Hauptsitzung gekürzt abgelegt (Agent darf keine Dateien schreiben).

**Urteil: freigabefähig.** Kein Blocker, kein Physikfehler; ca. 90 Zahlenwerte (alle Musterlösungen, beide Diagramme, alle vier Tröpfchen, Sim beider Modi live) nachgerechnet, keine Abweichung. Echtes KaTeX (Netz an): 486 Formeln gerendert, 0 `.katex-error`. Modulcheck `blocker: []`, `maengel: []`. S1, S2, M1–M11 und Technik 1–5, 9, 10 behoben (Reste siehe unten).

## Restmängel

Behoben durch den Bauagenten (Modulcheck und KaTeX-Prüfung danach erneut sauber): R1 veraltete Export-Namen (mittel), R2 Text „ruht nur bei 409 V“ (T3 ruht bei 409 und 410 V; Lehrerteil ergänzt), R3 überlappende Kraftpfeil-Labels bei 390 px, R5 Pause + Regler setzt Teilchen zurück, R6 Modus-Radios 16 px per Inline-Stil (jetzt 24 px), R9 Vorzeichen-/Betragsschreibweise in ue4/ue7/Lehrerteil.

Zur Kenntnis, nicht geändert: R4 Strahlszene bei 390 px eng, aber lesbar; R7 Druckansicht enthält alle 21 Hilfetexte inklusive Musterlösungen (Print-CSS unverändert aus der Vorlage, an die Referenz zurückmelden; `modulcheck.py` erkennt das nicht); R8 sim1 rechnerisch teilweise umgehbar (Grenze 111 V folgt aus Herleitung Schritt 8), für AB II vertretbar; R10 `data-plain` mit gemischten Unterstrich-/Unicode-Indizes.
