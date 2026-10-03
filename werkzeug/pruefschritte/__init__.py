# -*- coding: utf-8 -*-
"""Pruefschritte des Modulchecks, ausgelagert, damit modulcheck.py unter 400 Zeilen bleibt.

    browser       Browserstart mit Rueckfall auf Chrome und Edge
    formelleiste  Formelleiste: Datenvertrag, Erklaerungen, Sprunglinks, Hervorhebung, Schublade
    druckmodi     Druck als Arbeitsblatt und mit Loesungen, optional als PDF

Jeder Pruefschritt bekommt die Funktionen B (Blocker) und M (Mangel) uebergeben und legt
Messwerte in das Woerterbuch notiz.
"""
from .browser import browser_starten
from .formelleiste import formelleiste_pruefen
from .druckmodi import druckmodi_pruefen
