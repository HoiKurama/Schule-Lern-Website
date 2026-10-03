# -*- coding: utf-8 -*-
"""Browser-Seite des Pruefschritts Formelleiste: die JS-Funktionen, die formelleiste.py aufruft.

Vertrag in vorlage/baustein-formelleiste.md.
"""

JS_VERTRAG = r"""({physik}) => {
  const r = {vorhanden: typeof formelDaten !== "undefined", fehler: [], maengel: [], formeln: 0, gruppen: 0};
  if (!r.vorhanden) return r;
  if (!Array.isArray(formelDaten) || !formelDaten.length) { r.fehler.push("formelDaten ist leer oder kein Array"); return r; }
  const leer = v => v == null || !String(v).trim();
  const latex = v => /\\[a-zA-Z]/.test(String(v || ""));
  // Steuerzeichen entstehen, wenn ein Backslash im JS-String nicht verdoppelt wurde: "\frac" wird zu Seitenvorschub + "rac"
  const steuer = v => /[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(String(v || ""));
  // "\dfrac" ohne Verdopplung wird still zu "dfrac": LaTeX-Befehlswort ohne Backslash davor
  const nackt = v => { const m = String(v || "").replace(/\\text\{[^}]*\}/g, "")
      .match(/(^|[^\\A-Za-z])(frac|dfrac|tfrac|cdot|cdots|ldots|mathrm|mathbb|sqrt|vec|Delta|Phi|alpha|varphi|omega|approx|infty|operatorname|qquad|quad|int|lim|sum|left|right)(?![A-Za-z])/);
      return m ? m[2] : null; };
  const kennung = /^[a-z0-9-]+$/;
  const norm = s => String(s || "").replace(/[\s   ]/g, "").replace(/-/g, "−");
  const ids = new Set(), ziele = new Set();
  const abschnitte = new Set([...document.querySelectorAll(".wrap > section[id]")].map(s => s.id));
  const soll = [];
  formelDaten.forEach((g, gi) => {
    r.gruppen++;
    const wo = "Gruppe '" + (g.titel || gi) + "'";
    if (leer(g.abschnitt) || !abschnitte.has(g.abschnitt)) r.fehler.push(wo + ": abschnitt '" + g.abschnitt + "' ist keine <section id> der Seite");
    if (leer(g.titel)) r.fehler.push(wo + ": titel fehlt");
    else if (steuer(g.titel)) r.fehler.push(wo + ": Steuerzeichen im titel");
    if (!Array.isArray(g.formeln) || !g.formeln.length) { r.fehler.push(wo + ": keine Formeln"); return; }
    g.formeln.forEach((f, fi) => {
      r.formeln++;
      const w = "Formel '" + (f.id || (gi + "." + fi)) + "'";
      if (leer(f.id)) r.fehler.push(w + ": id fehlt");
      else if (!kennung.test(f.id)) r.fehler.push(w + ": id nur aus Kleinbuchstaben, Ziffern und Bindestrich");
      else if (ids.has(f.id)) r.fehler.push(w + ": id doppelt");
      else ids.add(f.id);
      ["tex", "plain", "gilt", "fehler", "ziel"].forEach(k => { if (leer(f[k])) r.fehler.push(w + ": " + k + " fehlt"); });
      ["tex", "plain", "gilt", "fehler"].forEach(k => { if (steuer(f[k])) r.fehler.push(w + ": Steuerzeichen in " + k + " (Backslash nicht verdoppelt?)"); });
      if (nackt(f.tex)) r.fehler.push(w + ": in tex steht '" + nackt(f.tex) + "' ohne Backslash (im JS-String \\\\ verdoppeln)");
      if (latex(f.plain)) r.fehler.push(w + ": LaTeX-Rest in plain: " + f.plain);
      ["gilt", "fehler"].forEach(k => {
        if (!leer(f[k]) && String(f[k]).trim().length < 25) r.maengel.push(w + ": " + k + " ist zu knapp");
        if (/<[a-z]/i.test(String(f[k] || ""))) r.fehler.push(w + ": HTML in " + k + " (Texte werden als Klartext gesetzt)");
      });
      const zeichen = Array.isArray(f.zeichen) ? f.zeichen : [];
      soll.push({id: f.id, zeichen: zeichen.length, einheiten: zeichen.filter(z => !leer(z.einheit)).length});
      if (!zeichen.length) r.fehler.push(w + ": zeichen fehlt");
      zeichen.forEach((z, zi) => {
        const wz = w + ", Zeichen '" + (z.plain || zi) + "'";
        ["tex", "plain", "text"].concat(physik ? ["einheit"] : []).forEach(k => { if (leer(z[k])) r.fehler.push(wz + ": " + k + " fehlt"); });
        ["tex", "plain", "text", "einheit"].forEach(k => { if (steuer(z[k])) r.fehler.push(wz + ": Steuerzeichen in " + k); });
        if (nackt(z.tex)) r.fehler.push(wz + ": in tex steht '" + nackt(z.tex) + "' ohne Backslash");
        if (latex(z.plain)) r.fehler.push(wz + ": LaTeX-Rest in plain");
      });
      if (leer(f.ziel)) return;
      ziele.add(f.ziel);
      if (!kennung.test(f.ziel)) r.fehler.push(w + ": ziel '" + f.ziel + "' nur aus Kleinbuchstaben, Ziffern und Bindestrich");
      else if (!/^f-/.test(f.ziel)) r.maengel.push(w + ": ziel '" + f.ziel + "' ohne Praefix f-");
      const ziel = document.getElementById(f.ziel);
      if (!ziel) { r.fehler.push(w + ": Sprungziel #" + f.ziel + " existiert nicht"); return; }
      if (ziel.closest(".formelleiste, .formelsammlung")) r.fehler.push(w + ": Sprungziel liegt in der Leiste oder Formelsammlung");
      const sec = ziel.closest("section[id]");
      if (sec && !leer(g.abschnitt) && sec.id !== g.abschnitt)
        r.maengel.push(w + ": Sprungziel liegt in #" + sec.id + ", die Gruppe gehoert zu #" + g.abschnitt);
      const m = ziel.classList.contains("m") ? ziel : ziel.querySelector(".m");
      if (!m) r.maengel.push(w + ": Sprungziel #" + f.ziel + " enthaelt keine Formel");
      else if (!leer(f.plain) && !norm(m.getAttribute("data-plain")).startsWith(norm(f.plain)))
        r.maengel.push(w + ": plain '" + f.plain + "' weicht von der Formel am Sprungziel ab ('" + m.getAttribute("data-plain") + "')");
    });
  });
  // Jede Formel mit Sprungziel-id im Text gehoert in die Leiste
  document.querySelectorAll('[id^="f-"]').forEach(e => {
    if (!e.closest(".formelleiste, .formelsammlung") && !ziele.has(e.id))
      r.fehler.push("#" + e.id + " sieht wie ein Sprungziel aus, hat aber keinen Eintrag in formelDaten");
  });
  const alle = {};
  document.querySelectorAll("[id]").forEach(e => { alle[e.id] = (alle[e.id] || 0) + 1; });
  Object.keys(alle).filter(k => alle[k] > 1).forEach(k => r.fehler.push("id '" + k + "' kommt " + alle[k] + "-mal vor"));
  const knoepfe = [...document.querySelectorAll(".formelleiste .fl-info")];
  r.eintraege = document.querySelectorAll(".formelleiste .fl-eintrag").length;
  r.knoepfe = knoepfe.length;
  knoepfe.forEach(b => {
    const erk = document.getElementById(b.getAttribute("aria-controls") || "");
    if (b.tagName !== "BUTTON") r.fehler.push("i-Knopf ist kein <button>");
    if (b.getAttribute("aria-expanded") !== "false") r.fehler.push("i-Knopf startet nicht mit aria-expanded=false");
    if (!erk) r.fehler.push("i-Knopf: aria-controls zeigt ins Leere");
    else if (!erk.hidden) r.fehler.push("Erklaerung " + erk.id + " ist beim Laden schon offen");
  });
  // Formelsammlung: letztes Stueck des Inhalts, je Formel eine Zeile, je Zeichen eine Angabe
  const fs = document.getElementById("formelsammlung");
  if (!fs) r.fehler.push("Formelsammlung fehlt (div#formelsammlung am Ende von .wrap)");
  else {
    if ([...document.querySelectorAll(".wrap > section")].some(s => fs.compareDocumentPosition(s) & Node.DOCUMENT_POSITION_FOLLOWING))
      r.fehler.push("Formelsammlung steht nicht am Ende: danach folgt noch eine <section>");
    const zeilen = [...fs.querySelectorAll(".fs-zeile")];
    if (zeilen.length !== r.formeln) r.fehler.push("Formelsammlung hat " + zeilen.length + " Zeilen fuer " + r.formeln + " Formeln");
    zeilen.forEach((z, i) => {
      const s = soll[i]; if (!s) return;
      const n = z.querySelectorAll(".fs-z").length;
      if (n !== s.zeichen) r.fehler.push("Formelsammlung, Zeile " + (i + 1) + ": " + n + " von " + s.zeichen + " Zeichenbedeutungen");
    });
  }
  r.soll = soll;
  return r;
}"""

JS_ERKLAERUNG = r"""(i) => {
  const b = document.querySelectorAll(".formelleiste .fl-info")[i];
  const erk = document.getElementById(b.getAttribute("aria-controls"));
  const li = b.closest(".fl-eintrag");
  const t = (erk.innerText || "").replace(/\s+/g, " ");
  return {id: erk.id, formel: li ? li.dataset.formel : null, expanded: b.getAttribute("aria-expanded"), hidden: erk.hidden,
          sichtbar: erk.getClientRects().length > 0 && erk.getBoundingClientRect().height > 20,
          zeichen: erk.querySelectorAll(".fl-zeichen dt").length,
          einheiten: [...erk.querySelectorAll(".fl-zeichen dd .fl-einheit")].filter(e => e.textContent.replace(/Einheit:/, "").trim()).length,
          laenge: t.length, gilt: /Gültigkeit/.test(t), fehler: /Typischer Fehler/.test(t),
          link: erk.querySelector("a.fl-link") ? erk.querySelector("a.fl-link").getAttribute("href") : null};
}"""

JS_ZIEL = r"""(href) => {
  const z = document.getElementById(href.slice(1));
  if (!z) return {da: false};
  const r = z.getBoundingClientRect();
  return {da: true, gerendert: z.getClientRects().length > 0 && r.height > 0,
          imBild: r.top >= -2 && r.bottom <= innerHeight + 2, top: Math.round(r.top),
          zu: !!z.closest("details:not([open])")};
}"""

JS_AKTIV = r"""() => [...document.querySelectorAll('.fl-eintrag.aktiv')].map(e => e.dataset.formel)"""

# id = null: kein Eintrag darf hervorgehoben sein
JS_AKTIV_IST = r"""(id) => { const a = [...document.querySelectorAll('.fl-eintrag.aktiv')].map(e => e.dataset.formel);
  return id === null ? a.length === 0 : (a.length === 1 && a[0] === id); }"""

JS_GROESSE = r"""(sel) => [...document.querySelectorAll(sel)].filter(e => e.getClientRects().length)
  .map(e => { const r = e.getBoundingClientRect(); return [Math.round(r.width), Math.round(r.height)]; })"""

JS_SCHUBLADE = r"""() => {
  const l = document.querySelector(".formelleiste"), k = document.querySelector(".fl-knopf");
  const s = document.querySelector(".fl-schleier"), cs = getComputedStyle(l), r = l.getBoundingClientRect();
  return {offen: l.classList.contains("offen"), sichtbar: cs.visibility !== "hidden" && r.left < innerWidth - 1 && r.width > 0,
          links: Math.round(r.left), rechts: Math.round(r.right), breite: innerWidth,
          knopf: k ? getComputedStyle(k).display !== "none" : false, expanded: k ? k.getAttribute("aria-expanded") : null,
          rolle: l.getAttribute("role"), schleier: s ? !s.hidden : false,
          fokusDrin: l.contains(document.activeElement), fokusKnopf: document.activeElement === k,
          ueberlauf: document.documentElement.scrollWidth - document.documentElement.clientWidth};
}"""

# Harter Rueckweg in den Grundzustand, damit ein Fehler keine Folgemeldungen erzeugt
JS_ZURUECK = r"""() => {
  const l = document.querySelector(".formelleiste"); if (!l) return;
  l.classList.remove("offen"); l.removeAttribute("role"); l.removeAttribute("aria-modal");
  const s = document.querySelector(".fl-schleier"); if (s) s.hidden = true;
  const k = document.querySelector(".fl-knopf"); if (k) k.setAttribute("aria-expanded", "false");
  l.querySelectorAll(".fl-info").forEach(b => { const e = document.getElementById(b.getAttribute("aria-controls") || "");
    if (e) e.hidden = true; b.setAttribute("aria-expanded", "false"); });
  if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
}"""

# Formeln, die ihre Box ueberragen (braucht echtes KaTeX); sel waehlt die zu pruefenden .m
JS_UEBERLAUF = r"""(sel) => [...document.querySelectorAll(sel)]
  .filter(m => m.getClientRects().length && getComputedStyle(m).visibility !== "hidden")
  .filter(m => m.scrollWidth > m.clientWidth + 2 || m.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
  .map(m => (m.getAttribute("data-plain") || "").slice(0, 60) + " (" + m.scrollWidth + " statt " + m.clientWidth + " px)")"""
