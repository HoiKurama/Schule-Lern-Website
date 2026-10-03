# Modulinhalt: Lineare Datenstrukturen (Liste, Schlange, Stapel)

Datei, die daraus entsteht: `module/info-q1-lineare-strukturen.html`
Fach: Informatik · Leistungskurs Q1 · Akzent `#b45309` / `#fef6e7` / `#f3ddb3`

<!-- GERUEST: wird abschnittsweise gefuellt -->

## 0 Kopfdaten der Seite

**Dateiname:** `module/info-q1-lineare-strukturen.html`

**Titel (h1 im `header.kopf`):** Lineare Datenstrukturen

**Untertitel:** Liste, Schlange und Stapel — und was dahinter wirklich passiert

**Chips im Kopf (in dieser Reihenfolge):**

| Chip | Text |
|---|---|
| 1 | Informatik · Leistungskurs Q1 |
| 2 | Inhaltsfeld: Daten und ihre Strukturierung |
| 3 | Java / BlueJ |
| 4 | ca. 135 Minuten |

Der Wortlaut des zweiten Chips ist dem Kernlehrplan wörtlich entnommen
(`fachliches/kernlehrplan-nrw.md`, Informatik LK, Inhaltsfeld 1).

**Farbtokens** — nur diese drei Zeilen im `:root`-Block gegenüber dem Referenzmodul tauschen,
sonst nichts:

```css
--akzent: #b45309;
--akzent-hell: #fef6e7;
--akzent-rand: #f3ddb3;
```

Der Verlauf in `header.kopf` wird passend zum Akzent auf Brauntöne umgestellt, alles andere
im `<style>`-Block bleibt unverändert.

**Abschnittsfolge und `.stufe`-Nummerierung**

| Nr. | `id` | Überschrift |
|---|---|---|
| 1 | `einstieg` | Einstieg |
| 2 | `knoten` | Knoten und Referenzen |
| 3 | `strukturen` | Die drei Strukturen und ihre Schnittstellen |
| 4 | `laufzeit` | Vertiefung: Laufzeit, Speicher und die Wahl der Struktur |
| 5 | `simulation` | Referenzen selbst umbiegen |
| 6 | `uebungen` | Übungen |
| 7 | `abschluss` | Zusammenfassung und Selbstcheck |

**Hinweis für den Bauagenten zur Codedarstellung.** Java-Code steht in
`<pre><code> … </code></pre>`. Falls der `<style>`-Block des Referenzmoduls keine Regel für
`pre`/`code` enthält, wird **keine neue Klasse erfunden**; stattdessen bekommt jedes `<pre>`
das Inline-Attribut

```html
<pre style="background:var(--akzent-hell);border:1px solid var(--akzent-rand);border-radius:8px;
padding:14px 16px;overflow-x:auto;font-size:14px;line-height:1.55"><code> … </code></pre>
```

Das entspricht dem Muster des Referenzmoduls, das an mehreren Stellen ebenfalls mit
Inline-Styles arbeitet (`#lenzText`, die randlosen Vorwissensaufgaben). Der waagerechte
Scrollbereich (`overflow-x:auto`) ist Pflicht, sonst schiebt langer Code die Seite auf dem
Handy quer.

**Achtung bei allen Java-Schnipseln:** Die Zeichen `<` und `>` der Generics müssen als
`&lt;` und `&gt;` maskiert werden, sonst frisst der Parser `<ContentType>` als Tag.

## 1 Einstieg

### 1.1 Aufhänger (zwei Absätze, wörtlich zu übernehmen)

> Du tippst in einem Editor drei Sätze, löschst versehentlich einen Absatz und drückst
> Strg+Z. Der Absatz ist wieder da. Drückst du noch einmal, verschwindet der Satz davor.
> Der Editor macht die Schritte also in genau der umgekehrten Reihenfolge rückgängig, in
> der du sie gemacht hast — der zuletzt abgelegte kommt zuerst wieder heraus. Zwei Zimmer
> weiter schickt eine ganze Klasse Dokumente an denselben Drucker. Auch dort werden Aufträge
> gesammelt, aber niemand würde akzeptieren, dass der zuletzt gesendete zuerst gedruckt wird.
> Dort gilt: wer zuerst kommt, mahlt zuerst.

> Beide Programme lagern Daten zwischen. Beide brauchen dafür kaum Code. Der einzige
> Unterschied liegt in der Frage, an welcher Stelle etwas hinein- und an welcher Stelle es
> wieder herauskommt — und genau dieser Unterschied entscheidet, ob die Anwendung tut, was
> sie soll. In dieser Einheit baust du die drei Strukturen, die diese Frage beantworten,
> von unten auf: aus einzelnen Objekten, die nichts weiter können, als auf ihren Nachfolger
> zu zeigen. Am Ende weißt du nicht nur, was `push` und `enqueue` tun, sondern welche
> einzelne Referenz sich dabei ändert.

### 1.2 Vorwissensfragen (drei MC-Aufgaben in einer `.karte`)

Einleitender Satz über den Fragen, im Stil des Referenzmoduls
(`color:var(--grau);font-size:15px`):

> Drei Fragen zu Objekten, Referenzen und Arrays aus der Einführungsphase. Wenn du hier
> hängst, lohnt sich ein Blick zurück, bevor du weitermachst.

---

#### `vw1` — Referenzsemantik

**Frage:**
In BlueJ läuft `Knoten k1 = new Knoten("A"); Knoten k2 = k1;`. Anschließend wird
`k2.setzeInhalt("B")` aufgerufen. Was gilt danach?

*Hinweis für den Bauagenten:* Der Code steht als `<code>`-Element im Fließtext der Frage.

**Optionen (feste Reihenfolge):**

| `data-i` | Text |
|---|---|
| 0 | Es gibt zwei Knotenobjekte; `k1` enthält weiterhin `"A"`. |
| 1 | Es gibt ein einziges Knotenobjekt, auf das beide Variablen verweisen; `k1.gibInhalt()` liefert `"B"`. |
| 2 | Es gibt zwei Knotenobjekte, deren Inhalte automatisch gleich gehalten werden. |

**Richtig:** `r: 1`

**Feedback je Option:**

- **0** — Du behandelst die Zuweisung wie das Kopieren eines Wertes. Bei Objekttypen kopiert
  `=` aber nicht das Objekt, sondern nur die Referenz darauf. Ein zweites Objekt entsteht in
  Java ausschließlich durch `new`, und `new` kommt hier nur einmal vor.
- **1** — Richtig. `k1` und `k2` sind zwei Namen für dieselbe Speicheradresse. Genau darauf
  beruht die ganze Einheit: Eine Kette entsteht nicht dadurch, dass Objekte kopiert werden,
  sondern dadurch, dass mehrere Referenzen auf dieselben Objekte zeigen.
- **2** — Eine automatische Synchronisation zwischen getrennten Objekten gibt es in Java
  nicht; das müsste man von Hand programmieren. Der Effekt, den du beschreibst, entsteht hier
  aus einem viel einfacheren Grund: Es gibt gar keine zwei Objekte.

---

#### `vw2` — Grenzen des Arrays

**Frage:**
Ein Array `String[] daten = new String[5];` ist vollständig gefüllt. Nun soll ein sechster
Eintrag hinzukommen. Was ist in Java nötig?

**Optionen (feste Reihenfolge):**

| `data-i` | Text |
|---|---|
| 0 | Nichts Besonderes — das Array vergrößert sich beim Schreiben auf Index 5 von selbst. |
| 1 | Der Eintrag an Index 4 wird überschrieben, mehr geht nicht. |
| 2 | Es muss ein neues, größeres Array angelegt und der alte Inhalt umkopiert werden. |

**Richtig:** `r: 2`

**Feedback je Option:**

- **0** — Das ist das Verhalten dynamischer Listen (etwa `ArrayList`), nicht das eines
  Arrays. Ein Array bekommt seine Länge bei `new` und behält sie bis zum Schluss; ein Zugriff
  auf Index 5 endet in einer `ArrayIndexOutOfBoundsException`.
- **1** — Überschreiben würde Daten vernichten, die noch gebraucht werden. Die Frage ist
  ja gerade, wie man Platz *schafft*, nicht wie man welchen freiräumt.
- **2** — Richtig. Genau dieser Umkopieraufwand ist der Grund, warum es verkettete Strukturen
  gibt: Dort kostet das Anhängen eines Elements nur ein einziges neues Objekt und keine
  Umkopieraktion.

---

#### `vw3` — Bedeutung von `null`

**Frage:**
Eine Objektvariable `Knoten k` hat den Wert `null`. Was passiert beim Aufruf `k.gibInhalt()`?

**Optionen (feste Reihenfolge):**

| `data-i` | Text |
|---|---|
| 0 | Das Programm bricht zur Laufzeit mit einer `NullPointerException` ab. |
| 1 | Der Aufruf liefert `null` zurück, weil es nichts zu holen gibt. |
| 2 | BlueJ meldet schon beim Übersetzen einen Fehler. |

**Richtig:** `r: 0`

**Feedback je Option:**

- **0** — Richtig. `null` heißt: Die Variable verweist auf gar kein Objekt. Ein Methodenaufruf
  braucht aber ein Objekt, an dem er ausgeführt wird. Deshalb beginnt später jede unserer
  Methoden mit der Prüfung, ob die Struktur leer ist.
- **1** — Du verwechselst „die Methode liefert `null`" mit „die Methode kann gar nicht
  aufgerufen werden". Damit ein Rückgabewert entstehen könnte, müsste der Methodenrumpf
  laufen — dazu fehlt aber das Objekt.
- **2** — Der Übersetzer prüft nur den Typ von `k`, und der ist korrekt `Knoten`. Welchen
  Wert die Variable zur Laufzeit trägt, kann er nicht wissen. `null`-Fehler sind
  Laufzeitfehler, und genau das macht sie so lästig.

## 2 Erklärteil

Der Erklärteil verteilt sich auf **zwei** `<section>`-Blöcke: Abschnitt 2 („Knoten und
Referenzen") baut das Bauteil, Abschnitt 3 („Die drei Strukturen und ihre Schnittstellen")
setzt daraus die drei Strukturen zusammen.

---

## 2A · Abschnitt 2: Knoten und Referenzen

### 2A.1 Fließtext (wörtlich)

> Ein Array ist ein durchnummerierter Block im Speicher. Das macht es schnell — du kommst mit
> `daten[742]` in einem Schritt an jedes Element — und zugleich starr: Die Länge steht bei
> `new` fest, und wer vorn etwas einfügen will, muss alles dahinter um eine Stelle
> verschieben.

> Die verkettete Struktur dreht diesen Handel um. Sie gibt die Nummerierung auf. Statt eines
> zusammenhängenden Blocks gibt es viele kleine Objekte, die irgendwo im Speicher liegen
> dürfen, und jedes von ihnen merkt sich, wer als Nächstes kommt. Ein solches Objekt heißt
> **Knoten**. Es trägt zwei Dinge: seinen Inhalt und eine Referenz auf den nächsten Knoten.
> Mehr nicht.

> Der letzte Knoten hat keinen Nachfolger mehr. Seine Referenz hat den Wert `null`. Das ist
> kein Notbehelf, sondern die Abbruchbedingung jeder Schleife, die du in dieser Einheit
> schreiben wirst: Solange `gibNachfolger()` nicht `null` liefert, geht es weiter.

**Java-Block 1 — die Klasse `Knoten`:**

```java
public class Knoten
{
    private String inhalt;
    private Knoten nachfolger;

    public Knoten(String pInhalt)
    {
        inhalt = pInhalt;
        nachfolger = null;
    }

    public String gibInhalt()
    {
        return inhalt;
    }

    public void setzeInhalt(String pInhalt)
    {
        inhalt = pInhalt;
    }

    public Knoten gibNachfolger()
    {
        return nachfolger;
    }

    public void setzeNachfolger(Knoten pKnoten)
    {
        nachfolger = pKnoten;
    }
}
```

> Schau dir die zweite Zeile genau an: Ein `Knoten` hat als Attribut eine Referenz auf einen
> `Knoten`. Eine Klasse verwendet sich selbst. Das ist erlaubt, weil das Attribut kein
> Knotenobjekt *enthält*, sondern nur auf eines *zeigt* — beim Anlegen steht dort `null`,
> und ein `null`-Verweis braucht keinen Platz für ein weiteres Objekt. Diese eine Zeile ist
> der ganze Trick hinter allem, was jetzt folgt.

**Nach dem Codeblock, Fließtext:**

> Aus einzelnen Knoten wird eine Kette, sobald jeder auf den nächsten zeigt. Zusätzlich
> braucht es eine Variable außerhalb der Kette, die auf ihren Anfang zeigt — sonst findet
> das Programm den ersten Knoten nicht wieder. Diese Variable heißt je nach Struktur
> `anfang` oder `kopf`, und sie liegt in der Klasse, die die Kette verwaltet. Die Knoten
> selbst wissen nichts davon; sie kennen nur ihren Nachfolger.

### 2A.2 Merksatz (`.merksatz`)

> **Kernaussage**
> Eine verkettete Struktur besteht aus zwei getrennten Dingen: den Knoten, die den Inhalt
> tragen, und den Zeigern der verwaltenden Klasse, die festlegen, wo man einsteigen darf.
> Alle Operationen dieser Einheit ändern nur Referenzen — kein einziges Inhaltsobjekt wird
> dabei angefasst, verschoben oder kopiert.

### 2A.3 Details-Block: „Warum jede Struktur nur die Zeiger hat, die sie braucht"

**Summary:** Warum jede Struktur genau die Zeiger bekommt, die sie braucht — eine Herleitung

**Inhalt (drei Absätze):**

> Man könnte auf den Gedanken kommen, jeder Struktur vorsichtshalber alle denkbaren Zeiger
> zu geben. Rechne einmal nach, was das kostet, und du siehst, warum das niemand tut. Wir
> leiten die nötige Zeigermenge aus den geforderten Operationen her.

> Der **Stapel** darf nur an einem Ende arbeiten: `push`, `pop` und `top` fassen alle
> dieselbe Stelle an. Ein Zeiger `kopf` genügt also, und alle drei Operationen kommen mit
> einer festen Anzahl Schritte aus, unabhängig davon, wie lang die Kette ist. Die
> **Schlange** dagegen fügt an einem Ende ein und entnimmt am anderen. Mit nur einem Zeiger
> `kopf` müsste `enqueue` jedes Mal bis ans Ende der Kette laufen — bei
> <span class="m" data-tex="n" data-plain="n"></span> Knoten sind das
> <span class="m" data-tex="n" data-plain="n"></span> Knotenbesuche. Ein zweiter Zeiger
> `ende`, der immer auf den letzten Knoten zeigt, drückt diesen Aufwand auf null Besuche.
> Der Preis ist eine einzige zusätzliche Referenz für die ganze Struktur — nicht pro Knoten.
> Das ist ein außerordentlich guter Handel.

> Die **Liste** ist die anspruchsvollste der drei, weil sie an *jeder* Stelle arbeiten soll.
> Dafür führt sie einen wandernden Zeiger `aktuell` ein, das sogenannte aktuelle Objekt.
> Damit lässt sich lesen, ändern und weiterrücken. Zum Löschen reicht `aktuell` aber nicht:
> Wer einen Knoten aus der Kette nehmen will, muss die Referenz seines **Vorgängers**
> umbiegen, und vom aktuellen Knoten aus kommt man nicht rückwärts — die Pfeile zeigen nur
> in eine Richtung. Entweder man läuft für jedes `remove` erneut von vorn los (teuer), oder
> man führt einen dritten Zeiger `vorgaenger` mit, der bei jedem `next()` einfach mitwandert
> (fast gratis). Wir nehmen den dritten Zeiger. Merke dir diese Begründung — sie ist die
> Antwort auf die häufigste Prüfungsfrage zu diesem Thema.

### 2A.4 Hinweiskasten (`.hinweis`) — die zentrale Fehlvorstellung

> **Häufiger Fehler.** „Einen Knoten löscht man, indem man seinen Nachfolger auf `null`
> setzt." Das ist genau falsch herum. `aktuell.setzeNachfolger(null)` hängt nicht den
> aktuellen Knoten ab, sondern **den gesamten Rest der Liste hinter ihm**. Der aktuelle
> Knoten bliebe drin, alles danach wäre weg. Gelöscht wird ein Knoten nie von sich aus,
> sondern immer von seinem Vorgänger her: Der Vorgänger überspringt ihn. Danach zeigt keine
> Referenz mehr auf den Knoten, und der Garbage Collector räumt ihn irgendwann weg — man
> muss in Java nichts freigeben.

---

## 2B · Abschnitt 3: Die drei Strukturen und ihre Schnittstellen

### 2B.1 Einleitender Fließtext

> Die folgenden Schnittstellen sind nicht frei erfunden. Sie stammen aus den Vorgaben zum
> Zentralabitur Informatik in Nordrhein-Westfalen; die Klassen `List`, `Queue` und `Stack`
> werden dort als fertige Java-Klassen bereitgestellt und dürfen in der Prüfung ohne
> Implementierung benutzt werden. Du musst ihre Wirkung kennen und begründen können — und im
> Leistungskurs zusätzlich wissen, wie sie innen funktionieren. Genau das bauen wir hier nach.

> Alle drei Klassen sind generisch, in der Prüfung also etwa `Stack&lt;Auftrag&gt;`. Damit der
> Blick auf die Referenzen frei bleibt, arbeiten wir hier mit `String` als Inhaltstyp und mit
> eigenen Klassennamen (`EinfacherStapel`, `EinfacheSchlange`, `EinfacheListe`). Die
> Methodennamen übernehmen wir eins zu eins — sie sind die verbindliche Schnittstelle.

**Hinweis für den Bauagenten:** In diesem Absatz `&lt;` / `&gt;` verwenden, sonst
verschluckt der Parser `<Auftrag>`.

### 2B.2 Schnittstellentabelle (in `<div class="tabelle">` einschließen!)

**Tabelle 1 — `Stack` (Stapel), LIFO**

| Methode | Wirkung |
|---|---|
| `Stack()` | erzeugt einen leeren Stapel |
| `boolean isEmpty()` | liefert `true`, wenn der Stapel keine Elemente enthält |
| `void push(ContentType pContent)` | legt `pContent` oben auf den Stapel |
| `void pop()` | entfernt das oberste Element; ist der Stapel leer, bleibt er unverändert |
| `ContentType top()` | liefert das oberste Element, ohne es zu entfernen; bei leerem Stapel `null` |

**Tabelle 2 — `Queue` (Schlange), FIFO**

| Methode | Wirkung |
|---|---|
| `Queue()` | erzeugt eine leere Schlange |
| `boolean isEmpty()` | liefert `true`, wenn die Schlange keine Elemente enthält |
| `void enqueue(ContentType pContent)` | hängt `pContent` hinten an |
| `void dequeue()` | entfernt das vorderste Element; ist die Schlange leer, bleibt sie unverändert |
| `ContentType front()` | liefert das vorderste Element, ohne es zu entfernen; bei leerer Schlange `null` |

**Tabelle 3 — `List` (Liste) mit aktuellem Objekt**

| Methode | Wirkung |
|---|---|
| `List()` | erzeugt eine leere Liste ohne aktuelles Objekt |
| `boolean isEmpty()` | liefert `true`, wenn die Liste keine Elemente enthält |
| `boolean hasAccess()` | liefert `true`, wenn es ein aktuelles Objekt gibt |
| `void toFirst()` | macht das erste Element zum aktuellen Objekt; bei leerer Liste passiert nichts |
| `void toLast()` | macht das letzte Element zum aktuellen Objekt; bei leerer Liste passiert nichts |
| `void next()` | rückt zum nachfolgenden Element vor; hinter dem letzten gibt es kein aktuelles Objekt mehr |
| `ContentType getContent()` | liefert den Inhalt des aktuellen Objekts, sonst `null` |
| `void setContent(ContentType pContent)` | ersetzt den Inhalt des aktuellen Objekts |
| `void insert(ContentType pContent)` | fügt **vor** dem aktuellen Objekt ein; das aktuelle Objekt bleibt dasselbe |
| `void append(ContentType pContent)` | hängt am **Ende** der Liste an; das aktuelle Objekt bleibt unverändert |
| `void concat(List pList)` | hängt `pList` hinten an und leert `pList` anschließend |
| `void remove()` | entfernt das aktuelle Objekt; **der Nachfolger wird zum neuen aktuellen Objekt** |

**Kasten `.hinweis` direkt unter Tabelle 3:**

> **Drei Randfälle, an denen im Abitur Punkte hängen.**
> `insert` fügt *vor* dem aktuellen Objekt ein, und das aktuelle Objekt bleibt danach
> dasselbe wie vorher — nicht das neu eingefügte. · Nach `remove` ist der **Nachfolger** des
> gelöschten Knotens das aktuelle Objekt; war der gelöschte Knoten der letzte, gibt es
> danach kein aktuelles Objekt mehr, `hasAccess()` liefert `false`. · Gibt es kein aktuelles
> Objekt und ist die Liste nicht leer, so lässt `insert` die Liste unverändert. Bei leerer
> Liste dagegen wird eingefügt — und es gibt weiterhin kein aktuelles Objekt.

### 2B.3 Die drei Implementierungen

Jeweils Fließtext, dann Java-Block.

---

**Stapel — Fließtext:**

> Der Stapel ist die kürzeste der drei Klassen, weil alles an einer Stelle passiert. Der
> Zeiger `kopf` zeigt auf das oberste Element. Neu ankommende Knoten schieben sich davor:
> Erst zeigt der Neue auf den bisherigen Kopf, dann wandert der Kopfzeiger auf den Neuen.
> Diese Reihenfolge ist zwingend. Machst du es andersherum und setzt zuerst `kopf = neu`,
> hast du die Adresse des alten Kopfes verloren und damit den ganzen restlichen Stapel.

**Java-Block 2:**

```java
public class EinfacherStapel
{
    private Knoten kopf;

    public EinfacherStapel()
    {
        kopf = null;
    }

    public boolean isEmpty()
    {
        return kopf == null;
    }

    public void push(String pInhalt)
    {
        if (pInhalt == null) { return; }
        Knoten neu = new Knoten(pInhalt);   // 1. neuen Knoten anlegen
        neu.setzeNachfolger(kopf);          // 2. er zeigt auf den bisherigen Kopf
        kopf = neu;                         // 3. der Kopfzeiger wandert
    }

    public void pop()
    {
        if (kopf == null) { return; }       // leerer Stapel bleibt unveraendert
        kopf = kopf.gibNachfolger();
    }

    public String top()
    {
        if (kopf == null) { return null; }
        return kopf.gibInhalt();
    }
}
```

> Beachte, dass `pop()` den alten Kopfknoten nirgends „löscht". Es genügt, dass keine
> Referenz mehr auf ihn zeigt. Und beachte, dass die Kette dadurch **umgekehrt** zur
> Einfügereihenfolge im Speicher liegt: Wer zuletzt kam, steht vorn. Das ist LIFO —
> *last in, first out*.

---

**Schlange — Fließtext:**

> Die Schlange braucht zwei Zeiger: `kopf` für die Entnahme, `ende` für das Anhängen. Beide
> zeigen in dieselbe Kette, nur an verschiedene Stellen. Der Sonderfall, an dem
> erfahrungsgemäß die meisten Implementierungen scheitern, ist der Übergang zwischen leer
> und nicht leer — und zwar in beide Richtungen.

**Java-Block 3:**

```java
public class EinfacheSchlange
{
    private Knoten kopf;
    private Knoten ende;

    public EinfacheSchlange()
    {
        kopf = null;
        ende = null;
    }

    public boolean isEmpty()
    {
        return kopf == null;
    }

    public void enqueue(String pInhalt)
    {
        if (pInhalt == null) { return; }
        Knoten neu = new Knoten(pInhalt);
        if (kopf == null)                   // Sonderfall: Schlange war leer
        {
            kopf = neu;
            ende = neu;                     // beide Zeiger auf denselben Knoten
        }
        else
        {
            ende.setzeNachfolger(neu);      // der bisher letzte zeigt auf den neuen
            ende = neu;                     // der Endzeiger wandert
        }
    }

    public void dequeue()
    {
        if (kopf == null) { return; }
        kopf = kopf.gibNachfolger();
        if (kopf == null) { ende = null; }  // war das letzte Element: ende mitfuehren
    }

    public String front()
    {
        if (kopf == null) { return null; }
        return kopf.gibInhalt();
    }
}
```

**Kasten `.hinweis` unter dem Codeblock:**

> **Der teuerste vergessene Zweig.** Lässt man in `dequeue` die letzte Zeile weg, funktioniert
> die Schlange scheinbar tadellos — bis man sie einmal ganz leert und danach wieder etwas
> einfügt. Dann ist `kopf == null`, `enqueue` nimmt den Sonderfallzweig, setzt `kopf` und
> `ende` neu, und alles läuft weiter. Der Fehler fällt also nicht sofort auf. Baut man
> `enqueue` dagegen ohne diesen Sonderfallzweig, hängt `enqueue` das neue Element an den
> längst entfernten alten Knoten — und die Schlange bleibt für immer leer, obwohl man
> einfügt. Beide Fehler gehören zusammen und werden zusammen geprüft.

---

**Liste — Fließtext:**

> Die Liste bekommt drei Zeiger: `anfang` als festen Einstiegspunkt, `aktuell` als
> wandernden Lesezeiger und `vorgaenger` als dessen Schatten, der immer einen Knoten
> zurückliegt. Ist `aktuell` der erste Knoten, so ist `vorgaenger` gleich `null` — das ist
> in jeder Methode der Fall, den du getrennt behandeln musst, weil es dann keinen Knoten
> gibt, dessen Referenz man umbiegen könnte. Stattdessen wird `anfang` umgebogen.

**Java-Block 4:**

```java
public class EinfacheListe
{
    private Knoten anfang;
    private Knoten aktuell;
    private Knoten vorgaenger;

    public EinfacheListe()
    {
        anfang = null;
        aktuell = null;
        vorgaenger = null;
    }

    public boolean isEmpty()
    {
        return anfang == null;
    }

    public boolean hasAccess()
    {
        return aktuell != null;
    }

    public void toFirst()
    {
        aktuell = anfang;
        vorgaenger = null;
    }

    public void toLast()
    {
        if (anfang == null) { return; }
        aktuell = anfang;
        vorgaenger = null;
        while (aktuell.gibNachfolger() != null)
        {
            vorgaenger = aktuell;
            aktuell = aktuell.gibNachfolger();
        }
    }

    public void next()
    {
        if (aktuell == null) { return; }
        vorgaenger = aktuell;               // der Schatten rueckt nach
        aktuell = aktuell.gibNachfolger();
    }

    public String getContent()
    {
        if (aktuell == null) { return null; }
        return aktuell.gibInhalt();
    }

    public void setContent(String pInhalt)
    {
        if (aktuell == null || pInhalt == null) { return; }
        aktuell.setzeInhalt(pInhalt);
    }

    public void append(String pInhalt)
    {
        if (pInhalt == null) { return; }
        Knoten neu = new Knoten(pInhalt);
        if (anfang == null)
        {
            anfang = neu;
            return;
        }
        Knoten lauf = anfang;               // Hilfszeiger, laeuft bis ans Ende
        while (lauf.gibNachfolger() != null)
        {
            lauf = lauf.gibNachfolger();
        }
        lauf.setzeNachfolger(neu);
    }

    public void insert(String pInhalt)
    {
        if (pInhalt == null) { return; }
        if (aktuell == null)
        {
            if (anfang == null)             // leere Liste: einfuegen, kein aktuelles Objekt
            {
                anfang = new Knoten(pInhalt);
            }
            return;                         // sonst: Liste bleibt unveraendert
        }
        Knoten neu = new Knoten(pInhalt);
        neu.setzeNachfolger(aktuell);       // 1. der Neue zeigt auf das aktuelle Objekt
        if (vorgaenger == null)
        {
            anfang = neu;                   // 2a. vorne einfuegen
        }
        else
        {
            vorgaenger.setzeNachfolger(neu);// 2b. der Vorgaenger zeigt auf den Neuen
        }
        vorgaenger = neu;                   // 3. der Neue ist jetzt der Vorgaenger
    }

    public void remove()
    {
        if (aktuell == null) { return; }
        if (vorgaenger == null)
        {
            anfang = aktuell.gibNachfolger();               // erster Knoten faellt weg
        }
        else
        {
            vorgaenger.setzeNachfolger(aktuell.gibNachfolger()); // Vorgaenger ueberspringt
        }
        aktuell = aktuell.gibNachfolger();                  // Nachfolger wird aktuell
    }
}
```

**Fließtext nach dem Codeblock:**

> Vergleiche `insert` und `remove` Zeile für Zeile. Beide bestehen aus derselben
> Fallunterscheidung — „gibt es einen Vorgänger oder ist das aktuelle Objekt der erste
> Knoten?" — und beide ändern danach genau die Referenz, die auf den betroffenen Knoten
> zeigt. Wenn du diese eine Struktur verstanden hast, hast du alle Einfüge- und
> Löschoperationen einfach verketteter Listen verstanden.

> Beachte in `remove` die Reihenfolge der letzten beiden Anweisungen. Der abgehängte Knoten
> zeigt selbst weiterhin auf seinen alten Nachfolger; deshalb liefert
> `aktuell.gibNachfolger()` auch nach dem Umbiegen noch den richtigen Knoten. Das ist kein
> Zufall, sondern der Grund, warum man hier keine Hilfsvariable braucht.

### 2B.4 Details-Block: `concat`

**Summary:** Die zwölfte Methode: `concat` — und warum sie die andere Liste leert

**Inhalt:**

> `concat(pList)` hängt eine zweite Liste hinten an und macht `pList` anschließend leer.
> Der zweite Teil klingt nach Schikane, ist aber notwendig: Nach dem Anhängen zeigen zwei
> Listenobjekte auf dieselben Knoten. Ein `remove` in der einen Liste würde die andere
> stillschweigend verändern. Indem `concat` die Quelle leert, kann dieser Zustand gar nicht
> erst entstehen.

```java
public void concat(EinfacheListe pListe)
{
    if (pListe == null || pListe == this || pListe.isEmpty()) { return; }
    if (anfang == null)
    {
        anfang = pListe.anfang;
    }
    else
    {
        Knoten lauf = anfang;
        while (lauf.gibNachfolger() != null)
        {
            lauf = lauf.gibNachfolger();
        }
        lauf.setzeNachfolger(pListe.anfang);
    }
    pListe.anfang = null;       // Quelle leeren: erlaubt, da gleiche Klasse
    pListe.aktuell = null;
    pListe.vorgaenger = null;
}
```

> Die drei Zuweisungen am Schluss greifen auf private Attribute eines *anderen* Objekts zu.
> Das ist in Java erlaubt, solange beide Objekte zur selben Klasse gehören — der
> Zugriffsschutz gilt pro Klasse, nicht pro Objekt.

### 2B.5 Merksatz (`.merksatz`)

> **Kernaussage**
> Stapel, Schlange und Liste speichern dieselben Daten in derselben Art von Kette. Sie
> unterscheiden sich einzig darin, welche Zugriffsstellen ihre Schnittstelle nach außen
> freigibt. Eine Struktur zu wählen heißt deshalb nicht, Speicher zu wählen, sondern sich
> auf eine Zugriffsdisziplin festzulegen — und genau diese Beschränkung ist der Gewinn.

### 2B.6 Hinweiskasten (`.hinweis`) — zweite Fehlvorstellung

> **Häufiger Fehler.** „`aktuell` ist so etwas wie ein Index." Nein. `aktuell` ist eine
> Referenz auf ein Knotenobjekt, keine Zahl. Es gibt in einer verketteten Liste kein
> „Element Nummer 7", das man direkt ansteuern könnte. Wer zum siebten Element will, ruft
> `toFirst()` und danach sechsmal `next()` auf — und besucht dabei sieben Knoten. Genau
> deshalb steht in der Laufzeittabelle im nächsten Abschnitt beim Zugriff ein
> <span class="m" data-tex="\mathcal{O}(n)" data-plain="O(n)"></span> und kein
> <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span>.

## 3 Vertiefung

Abschnitt 4 der Seite, `id="laufzeit"`, Überschrift **„Vertiefung: Laufzeit, Speicher und die
Wahl der Struktur"**.

### 3.1 Einleitender Fließtext (wörtlich)

> Bis hierhin funktionieren alle drei Strukturen. Die Frage ist jetzt eine andere: Was
> kosten sie? Im Leistungskurs misst man das nicht in Sekunden — die hängen vom Rechner ab,
> vom Betriebssystem und davon, was sonst gerade läuft. Man misst in **Knotenbesuchen**:
> Wie oft muss das Programm einem Nachfolgerzeiger folgen, bis es an der Stelle ist, an der
> es arbeiten will? Diese Zahl hängt nur vom Algorithmus ab und lässt sich abzählen, ohne
> das Programm überhaupt zu starten.

> Schau dir dazu noch einmal die drei Implementierungen an. In `push`, `pop`, `top`,
> `enqueue`, `dequeue` und `front` steht keine einzige Schleife. Diese sechs Methoden
> arbeiten immer an einem Zeiger, den die Struktur ohnehin schon in der Hand hält, und
> brauchen deshalb stets gleich viele Schritte — egal, ob die Kette drei Knoten hat oder
> drei Millionen. Man schreibt das als
> <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> und sagt „konstante
> Laufzeit". In `append` und `toLast` steht dagegen eine `while`-Schleife, die bis ans Ende
> läuft. Ihre Kosten wachsen proportional zur Länge der Kette:
> <span class="m" data-tex="\mathcal{O}(n)" data-plain="O(n)"></span>.

### 3.2 Laufzeittabelle

**Wichtig für den Bauagenten:** Diese Tabelle hat fünf Spalten und **muss** in
`<div class="tabelle">` eingeschlossen werden.

| Operation | Stapel | Schlange | Liste | Grund |
|---|---|---|---|---|
| einfügen an der Zugriffsstelle | <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> | <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> | <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> | `push` / `enqueue` / `insert`: der nötige Zeiger ist schon bekannt |
| entnehmen | <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> | <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> | <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> | `pop` / `dequeue` / `remove`: es werden nur Referenzen umgebogen |
| hinten anhängen | — | <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> | <span class="m" data-tex="\mathcal{O}(n)" data-plain="O(n)"></span> | die Schlange führt `ende` mit, die Liste muss das Ende suchen |
| Zugriff auf das <span class="m" data-tex="k" data-plain="k"></span>-te Element | — | — | <span class="m" data-tex="\mathcal{O}(n)" data-plain="O(n)"></span> | kein Index, nur `toFirst()` und wiederholtes `next()` |
| Speicher je Element | 2 Referenzen | 2 Referenzen | 2 Referenzen | Inhalt und Nachfolger |

**Hinweis für den Bauagenten:** Der Gedankenstrich „—" bedeutet „diese Operation gibt es in
dieser Struktur nicht". Das steht als Fußnote in
`<p style="color:var(--grau);font-size:14px">` unter der Tabelle:

> Ein „—" heißt nicht „langsam", sondern: Diese Struktur bietet die Operation gar nicht an.
> Genau darin besteht ihre Zugriffsdisziplin.

### 3.3 Details-Block: Warum eine Liste, die man mit `append` aufbaut, quadratisch wächst

**Summary:** Der teuerste Anfängerfehler: eine Liste mit `append` in einer Schleife aufbauen

**Inhalt:**

> Unser `append` läuft jedes Mal von `anfang` bis ans Ende. Das kostet bei einer Liste mit
> <span class="m" data-tex="n" data-plain="n"></span> Knoten genau
> <span class="m" data-tex="n" data-plain="n"></span> Knotenbesuche — einen für
> `lauf = anfang` und <span class="m" data-tex="n-1" data-plain="n−1"></span> weitere im
> Schleifenrumpf. Baut man nun eine Liste von null an mit
> <span class="m" data-tex="n" data-plain="n"></span> Aufrufen auf, so ist die Liste beim
> <span class="m" data-tex="i" data-plain="i"></span>-ten Aufruf erst
> <span class="m" data-tex="i-1" data-plain="i−1"></span> Knoten lang. Die Gesamtkosten sind
> also die Summe der Zahlen von 0 bis <span class="m" data-tex="n-1" data-plain="n−1"></span>:

<div class="m block" data-tex="0 + 1 + 2 + \dots + (n-1) = \frac{n\,(n-1)}{2}"
     data-plain="0 + 1 + 2 + … + (n−1) = n · (n−1) / 2"></div>

> Für <span class="m" data-tex="n = 1200" data-plain="n = 1200"></span> sind das
> <span class="m" data-tex="\frac{1200 \cdot 1199}{2} = 719\,400" data-plain="1200 · 1199 / 2 = 719 400"></span>
> Knotenbesuche, nur um 1200 Elemente einzufügen. Verdoppelst du die Anzahl der Elemente, so
> vervierfacht sich der Aufwand — das ist quadratisches Wachstum,
> <span class="m" data-tex="\mathcal{O}(n^2)" data-plain="O(n²)"></span>.

> Die Abhilfe kennst du bereits: Ein zusätzlicher Endzeiger, wie ihn die Schlange führt,
> drückt jedes einzelne `append` auf null Knotenbesuche und damit den Aufbau der gesamten
> Liste auf <span class="m" data-tex="\mathcal{O}(n)" data-plain="O(n)"></span>. Unsere
> `EinfacheListe` verzichtet bewusst darauf, damit an dieser Stelle sichtbar wird, was ein
> Endzeiger überhaupt einspart. Merke dir die Zahl 719 400 — sie ist ein gutes Argument in
> jeder Bewertungsaufgabe.

### 3.4 Speicher: Was die Verkettung kostet

**Fließtext:**

> Geschwindigkeit ist nicht umsonst. Jeder Knoten trägt neben seinem Inhalt eine zweite
> Referenz, die im Array niemand braucht. Rechnen wir das an einem Modell durch: Ein
> Bibliothekssystem verwaltet 1200 ausgeliehene Medien, und eine Referenz belege 4 Byte.

<div class="m block" data-tex="S_{\text{Kette}} = 1200 \cdot (4\,\mathrm{B} + 4\,\mathrm{B}) = 9600\,\mathrm{B} = 9{,}6\,\mathrm{kB}"
     data-plain="S_Kette = 1200 · (4 B + 4 B) = 9600 B = 9,6 kB"></div>

<div class="m block" data-tex="S_{\text{Array}} = 1200 \cdot 4\,\mathrm{B} = 4800\,\mathrm{B} = 4{,}8\,\mathrm{kB}"
     data-plain="S_Array = 1200 · 4 B = 4800 B = 4,8 kB"></div>

> Die Verkettung braucht in diesem Modell doppelt so viel Verwaltungsspeicher wie das Array,
> also 4,8 kB mehr. Das ist bei heutigen Speichergrößen wenig — und man kauft sich dafür
> etwas, das ein Array nicht liefern kann: Einfügen und Löschen an einer bekannten Stelle
> ohne jedes Umkopieren.

**Kasten `.hinweis` direkt darunter:**

> **Was diese Modellrechnung nicht sagt.** Sie zählt ausschließlich die Referenzen. Ein
> echtes Java-Objekt trägt zusätzlich einen Objektkopf von typischerweise 12 bis 16 Byte,
> und der belegte Speicher wird auf 8-Byte-Grenzen aufgerundet. In der Praxis kostet ein
> Knoten daher eher das Vier- bis Fünffache einer Arrayzelle, nicht das Doppelte. Für den
> Vergleich der Größenordnungen genügt das einfache Modell; behaupte in einer Klausur aber
> nie, du habest den *tatsächlichen* Speicherbedarf berechnet. Sage: „in diesem Modell".

### 3.5 Der Zugriff auf das k-te Element

**Fließtext:**

> Die auffälligste Schwäche der verketteten Liste steht in der vierten Zeile der Tabelle.
> Weil es keinen Index gibt, kostet der Weg zum Element mit Index
> <span class="m" data-tex="k" data-plain="k"></span> genau
> <span class="m" data-tex="k+1" data-plain="k+1"></span> Knotenbesuche: einen für
> `toFirst()` und <span class="m" data-tex="k" data-plain="k"></span> weitere für die
> `next()`-Aufrufe. Beim ersten Element ist das 1 Besuch, beim letzten der 1200er-Liste sind
> es 1200. Greift man auf gleichverteilt zufällige Positionen zu, liegt der Mittelwert bei

<div class="m block" data-tex="\overline{b} = \frac{1 + 1200}{2} = 600{,}5"
     data-plain="b̄ = (1 + 1200) / 2 = 600,5"></div>

> Knotenbesuchen — für **einen einzigen** Zugriff, den ein Array in genau einem Schritt
> erledigt. Wer viel wahlfrei zugreift und selten einfügt, ist mit einem Array besser
> bedient. Wer viel einfügt und löscht und dabei ohnehin schon an der richtigen Stelle
> steht, mit der Liste. Diese Abwägung, nicht die Frage „was ist schneller", ist die
> eigentliche Prüfungsfrage.

### 3.6 Der Anwendungsfall: derselbe Algorithmus, zwei Strukturen

**Fließtext:**

> Jetzt der Punkt, an dem der Unterschied zwischen LIFO und FIFO aufhört, Geschmackssache zu
> sein. Ein Roboter soll in einem Gitter aus freien und blockierten Feldern einen Weg von
> links oben nach rechts unten finden. Der Algorithmus ist in beiden Fällen **wörtlich
> derselbe**:

**Pseudocode-Block** (`<pre>` mit der in Abschnitt 0 festgelegten Inline-Formatierung):

```
Startfeld in den Behaelter legen
solange der Behaelter nicht leer ist:
    Feld aus dem Behaelter entnehmen
    wenn es das Ziel ist: fertig
    jeden freien, noch nicht besuchten Nachbarn
        als besucht markieren und in den Behaelter legen
```

> In diesem Text steht kein Wort darüber, ob der Behälter eine Schlange oder ein Stapel ist.
> Tauscht man nur diese eine Entscheidung aus, ändert sich das Verhalten grundlegend.

> Mit der **Schlange** werden die Felder in genau der Reihenfolge abgearbeitet, in der sie
> entdeckt wurden. Der Suchbereich wächst deshalb wie ein Ring gleichmäßig nach außen: erst
> alle Felder in einem Schritt Entfernung, dann alle in zwei Schritten, und so weiter. Das
> Ziel wird dadurch zwangsläufig auf einem **kürzesten** Weg erreicht — das ist die
> Breitensuche.

> Mit dem **Stapel** wird stets der zuletzt entdeckte Nachbar zuerst weiterverfolgt. Die
> Suche rennt in eine Richtung, bis es nicht mehr weitergeht, und kehrt erst dann zur
> letzten Abzweigung zurück — das ist die Tiefensuche. Sie findet ebenfalls ein Ziel, aber
> der gefundene Weg ist im Allgemeinen **nicht** der kürzeste.

**Gitter als `<pre>`-Block** (`#` blockiert, `.` frei, Start links oben, Ziel rechts unten):

```
  Spalte  0 1 2 3 4 5
Zeile 0   . . . . . .
Zeile 1   . # # # # .
Zeile 2   . # . . . .
Zeile 3   . # . # # .
Zeile 4   . . . # . .
Zeile 5   . # . . . .
```

> Die Nachbarn werden in beiden Fällen in derselben Reihenfolge betrachtet: rechts, unten,
> links, oben. Nur der Behälter unterscheidet sich.

**Ergebnistabelle** (in `<div class="tabelle">`):

| Behälter | Suchverfahren | gefundener Weg | Länge |
|---|---|---|---|
| Schlange (FIFO) | Breitensuche | (0,0) → (0,1) → (0,2) → (0,3) → (0,4) → (0,5) → (1,5) → (2,5) → (3,5) → (4,5) → (5,5) | **10 Schritte** |
| Stapel (LIFO) | Tiefensuche | (0,0) → (1,0) → (2,0) → (3,0) → (4,0) → (4,1) → (4,2) → (3,2) → (2,2) → (2,3) → (2,4) → (2,5) → (3,5) → (4,5) → (5,5) | **14 Schritte** |

**Hinweis für den Bauagenten:** Die Wegspalte ist lang. Die Tabelle unbedingt in
`<div class="tabelle">` setzen, sonst schiebt sie die Seite auf dem Handy quer.

**Merksatz `.merksatz` zum Abschluss des Abschnitts:**

> **Kernaussage**
> Der Behälter ist kein Detail der Umsetzung, sondern Teil des Algorithmus. Dieselben
> Programmzeilen liefern mit einer Schlange garantiert einen kürzesten Weg und mit einem
> Stapel irgendeinen Weg — hier einen um 4 Schritte längeren. Wer eine Datenstruktur wählt,
> legt damit eine Eigenschaft des Ergebnisses fest, nicht bloß die Geschwindigkeit.

**Kasten `.hinweis` als Abschluss des Abschnitts:**

> **Häufiger Fehler.** „Die Breitensuche ist besser." Nein — sie ist *anders*. Die
> Tiefensuche kommt mit deutlich weniger gleichzeitig gemerkten Feldern aus und ist überall
> dort im Vorteil, wo der Speicher knapp ist oder wo *irgendeine* Lösung genügt: bei der
> Labyrinth-Erzeugung, beim Backtracking, im Sudokulöser. Die richtige Antwort auf „welche
> ist besser?" beginnt immer mit einer Gegenfrage: „Wofür?"

## 4 Interaktiver Kern: Simulation

Abschnitt 5 der Seite, `id="simulation"`, Überschrift **„Referenzen selbst umbiegen"**.

Dies ist der einzige Teil, den der Bauagent wirklich neu schreibt. Die Vorgaben hier sind
verbindlich; wo eine Zahl steht, ist sie in Abschnitt 8 nachgerechnet.

### 4.1 Einleitender Fließtext (wörtlich, vor dem Beobachtungsauftrag)

> Unten siehst du dieselben Knotenobjekte, die du gerade in Java gelesen hast — als Kästen
> mit zwei Feldern: links der Inhalt, rechts die Referenz auf den Nachfolger. Die Zeiger der
> verwaltenden Klasse hängen als beschriftete Pfeile darüber und darunter.

> Wichtig: Hier läuft keine abgespielte Animation. Unter der Zeichnung arbeitet dasselbe
> Modell, das du in Java gebaut hast — echte Objekte mit echten Nachfolgerreferenzen. Wenn
> du im Schrittmodus arbeitest, wird pro Klick **genau eine Java-Zeile** ausgeführt und die
> Referenz, die sich dabei ändert, rot hervorgehoben. Was du siehst, ist der Zustand des
> Modells, nicht ein Bild davon.

### 4.2 Beobachtungsauftrag (`.auftrag`, wörtlich)

> **Beobachtungsauftrag**
> Setze die Simulation zurück und wähle **Stapel**. Füge nacheinander A, B, C, D und E ein.
> Notiere die Reihenfolge der Kette von links nach rechts sowie beide Zähler. Wiederhole das
> Ganze — jedes Mal nach *Zurücksetzen* — für **Schlange** und für **Liste**, jeweils mit
> derselben Eingabefolge und der jeweiligen Einfügeoperation (`push`, `enqueue`, `append`).
> Zwei der drei Ketten sehen am Ende gleich aus, eine nicht. Und genau die Struktur mit der
> abweichenden Kette hat den Zähler „besuchte Knoten" auf null. Schreibe einen Satz auf, der
> beides zugleich erklärt.

Direkt danach folgen die beiden MC-Aufgaben `sim1` und `sim2` (Abschnitt 4.9).

### 4.3 Zustandsmodell (verbindlich)

Ein Knoten ist ein echtes JavaScript-Objekt, kein Eintrag in einem Array. Die Reihenfolge in
der Zeichnung entsteht **ausschließlich** dadurch, dass die Zeichenroutine der Kette von
`kopf` aus folgt.

```js
var idZaehler = 0;

function Knoten(inhalt){
  this.inhalt = inhalt;
  this.nachfolger = null;   // Referenz auf Knoten oder null
  this.id = ++idZaehler;    // nur zum Wiedererkennen beim Zeichnen
}

// Zeiger der verwaltenden Klasse. Alle vier halten Knotenobjekte oder null.
var S = { kopf:null, ende:null, aktuell:null, vorgaenger:null };

var struktur = "stapel";    // "stapel" | "schlange" | "liste"
var zRef = 0;               // Zaehler: Referenzaenderungen (kumuliert)
var zBes = 0;               // Zaehler: besuchte Knoten (kumuliert)
var letzterWert = "—";      // Rueckgabewert von top()/front()/getContent()
var neuerKnoten = null;     // frisch erzeugter, noch nicht verketteter Knoten
var entfernt = null;        // gerade abgehaengter Knoten (nur zur Anzeige)
var laufZeiger = null;      // Hilfszeiger waehrend append()
```

**Beschriftung der Zeiger je nach Struktur** — das Feld heißt intern immer gleich, die
Beschriftung in der Zeichnung richtet sich nach dem Java-Quelltext des jeweiligen Abschnitts:

| Feld | Stapel | Schlange | Liste |
|---|---|---|---|
| `S.kopf` | `kopf` | `kopf` | `anfang` |
| `S.ende` | — | `ende` | — |
| `S.aktuell` | — | — | `aktuell` |
| `S.vorgaenger` | — | — | `vorgaenger` |

Nicht benutzte Zeiger werden weder gezeichnet noch angezeigt.

**Obergrenze.** `MAX_KNOTEN = 6`. Wird eine Einfügeoperation bei sechs Knoten ausgelöst,
passiert nichts am Modell; stattdessen erscheint im Protokollfeld:

> Für die Zeichnung ist bei sechs Knoten Schluss. Nimm erst etwas heraus.

### 4.4 Schrittmodell

Jede Operation wird in eine Liste atomarer Schritte zerlegt. Ein Schritt ist ein Objekt:

```js
{ code: "neu.setzeNachfolger(kopf);",     // die Java-Zeile, monospace angezeigt
  text: "Der neue Knoten zeigt jetzt auf den bisherigen Kopf.",
  hebe: {von: <Knoten|"kopf"|"ende"|"aktuell"|"vorgaenger"|"anfang">,
         nach: <Knoten|null>},            // welche Referenz sich aendert; null = keine
  tu:   function(){ /* fuehrt die Aenderung am Modell aus */ } }
```

Ablauf der Engine:

1. Klick auf eine Operationsschaltfläche baut die Schrittliste und setzt `schrittIndex = 0`.
2. Ist der Schrittmodus **an**, wird nur gezeichnet: Der anstehende Schritt wird mit seiner
   `hebe`-Angabe **rot gestrichelt** vorgezeichnet, `code` und `text` erscheinen im
   Protokollfeld, die Schaltfläche „Nächster Schritt" wird aktiv.
3. Jeder Klick auf „Nächster Schritt" ruft `tu()` des aktuellen Schritts auf, zeichnet neu
   (die soeben geänderte Referenz **rot durchgezogen**), erhöht `schrittIndex` und zeigt den
   nächsten Schritt gestrichelt vor.
4. Ist der Schrittmodus **aus**, werden alle `tu()` sofort nacheinander ausgeführt und nur
   das Endergebnis gezeichnet; das Protokollfeld zeigt die Zeilen untereinander.
5. Nach dem letzten Schritt werden `neuerKnoten`, `entfernt` und `laufZeiger` auf `null`
   gesetzt und ein letztes Mal gezeichnet.

Solange eine Schrittliste nicht abgearbeitet ist, sind alle anderen Operationsschaltflächen
deaktiviert. Das verhindert, dass sich zwei Operationen überlagern.

### 4.5 Schrittfolgen aller Operationen (verbindlich)

Die Spalte **ΔRef** zählt die Referenzänderungen dieses Schritts (Erhöhung von `zRef`), die
Spalte **ΔBes** die Knotenbesuche (Erhöhung von `zBes`). Das Anlegen eines Knotens mit `new`
ist **keine** Referenzänderung und **kein** Knotenbesuch.

---

#### Stapel — `push(x)`

| # | `code` | Wirkung auf das Modell | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `Knoten neu = new Knoten("x");` | `neuerKnoten = new Knoten(x)` — erscheint frei über der Kette | 0 | 0 |
| 2 | `neu.setzeNachfolger(kopf);` | `neuerKnoten.nachfolger = S.kopf` | 1 | 0 |
| 3 | `kopf = neu;` | `S.kopf = neuerKnoten` | 1 | 0 |

`text` zu Schritt 2: „Der neue Knoten zeigt auf den bisherigen Kopf. Diese Reihenfolge ist
zwingend — andersherum wäre die Adresse des alten Kopfes verloren."
`text` zu Schritt 3: „Erst jetzt wandert der Kopfzeiger. Der neue Knoten steht vorn."
**Summe: 2 Referenzänderungen, 0 Knotenbesuche.**

#### Stapel — `pop()`

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `if (kopf == null) { return; }` | nur Prüfung; bei leerem Stapel bricht die Liste hier ab | 0 | 0 |
| 2 | `kopf = kopf.gibNachfolger();` | `entfernt = S.kopf; S.kopf = S.kopf.nachfolger` | 1 | 0 |

Bei leerem Stapel lautet der `text` zu Schritt 1: „Der Stapel ist leer. `pop()` lässt ihn
unverändert — das ist kein Fehler, sondern die vereinbarte Wirkung."
**Summe (nicht leer): 1 Referenzänderung, 0 Knotenbesuche.**

#### Stapel — `top()`

Ein einziger Schritt, `code: "return kopf.gibInhalt();"`. Der Kopfknoten wird hervorgehoben
(dickerer Rand in `--akzent`), `letzterWert` wird gesetzt. Bei leerem Stapel `letzterWert = "null"`.
**Summe: 0 Referenzänderungen, 0 Knotenbesuche.** `text`: „Lesen ändert nichts. Der Knoten
bleibt, wo er ist — deshalb bewegen sich beide Zähler nicht."

---

#### Schlange — `enqueue(x)`

**Fall A, die Schlange ist leer** (`S.kopf === null`):

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `Knoten neu = new Knoten("x");` | `neuerKnoten` entsteht | 0 | 0 |
| 2 | `kopf = neu;` | `S.kopf = neuerKnoten` | 1 | 0 |
| 3 | `ende = neu;` | `S.ende = neuerKnoten` | 1 | 0 |

`text` zu Schritt 3: „Beim allerersten Element zeigen beide Zeiger auf denselben Knoten. Wer
diesen Zweig vergisst, hängt später ins Leere."

**Fall B, die Schlange ist nicht leer:**

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `Knoten neu = new Knoten("x");` | `neuerKnoten` entsteht | 0 | 0 |
| 2 | `ende.setzeNachfolger(neu);` | `S.ende.nachfolger = neuerKnoten` | 1 | 0 |
| 3 | `ende = neu;` | `S.ende = neuerKnoten` | 1 | 0 |

`text` zu Schritt 2: „Der Endzeiger erspart die Suche: Der letzte Knoten ist bereits bekannt,
es wird kein einziger Knoten abgelaufen."
**Summe in beiden Fällen: 2 Referenzänderungen, 0 Knotenbesuche.**

#### Schlange — `dequeue()`

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `if (kopf == null) { return; }` | Prüfung | 0 | 0 |
| 2 | `kopf = kopf.gibNachfolger();` | `entfernt = S.kopf; S.kopf = S.kopf.nachfolger` | 1 | 0 |
| 3 | `if (kopf == null) { ende = null; }` | **nur wenn `S.kopf === null`:** `S.ende = null` | 1 | 0 |

Schritt 3 wird immer angezeigt, aber nur ausgeführt, wenn die Bedingung zutrifft. Trifft sie
nicht zu, lautet der `text`: „Die Bedingung ist falsch, es bleibt alles, wie es ist." Trifft
sie zu: „Das war das letzte Element. Der Endzeiger muss mit zurückgesetzt werden, sonst zeigt
er auf einen Knoten, den es nicht mehr gibt."
**Summe: 1 Referenzänderung (2, wenn die Schlange dabei leer wird), 0 Knotenbesuche.**

#### Schlange — `front()`

Wie `top()`: ein Schritt, `code: "return kopf.gibInhalt();"`, 0 / 0.

---

#### Liste — `toFirst()`

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `aktuell = anfang;` | `S.aktuell = S.kopf` | 1 | 0 |
| 2 | `vorgaenger = null;` | `S.vorgaenger = null` | 1 | 0 |

**Summe: 2 Referenzänderungen, 0 Knotenbesuche.**

#### Liste — `next()`

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `if (aktuell == null) { return; }` | Prüfung | 0 | 0 |
| 2 | `vorgaenger = aktuell;` | `S.vorgaenger = S.aktuell` | 1 | 0 |
| 3 | `aktuell = aktuell.gibNachfolger();` | `S.aktuell = S.aktuell.nachfolger` | 1 | 0 |

`text` zu Schritt 2: „Der Schatten rückt zuerst nach. Genau dadurch ist der Vorgänger später
beim Löschen kostenlos verfügbar."
**Summe: 2 Referenzänderungen, 0 Knotenbesuche.**

#### Liste — `toLast()`

Erzeugt dieselbe Schrittfolge wie `toFirst()` gefolgt von so vielen `next()`, bis
`S.aktuell.nachfolger === null`. Jeder dieser Durchläufe zählt **1 Knotenbesuch** (das
Auswerten von `aktuell.gibNachfolger()` in der Schleifenbedingung) und 2 Referenzänderungen.
Bei leerer Liste besteht die Schrittfolge nur aus `if (anfang == null) { return; }`.

#### Liste — `append(x)`

**Fall A, die Liste ist leer:**

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `Knoten neu = new Knoten("x");` | `neuerKnoten` entsteht | 0 | 0 |
| 2 | `anfang = neu;` | `S.kopf = neuerKnoten` | 1 | 0 |

**Fall B, die Liste hat <span class="m" data-tex="n \ge 1" data-plain="n ≥ 1"></span> Knoten:**

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `Knoten neu = new Knoten("x");` | `neuerKnoten` entsteht | 0 | 0 |
| 2 | `Knoten lauf = anfang;` | `laufZeiger = S.kopf` | 0 | **1** |
| 3…| `lauf = lauf.gibNachfolger();` | `laufZeiger = laufZeiger.nachfolger` — **je einmal wiederholt, bis `laufZeiger.nachfolger === null`**, also <span class="m" data-tex="n-1" data-plain="n−1"></span> mal | 0 | **1 je Durchlauf** |
| letzter | `lauf.setzeNachfolger(neu);` | `laufZeiger.nachfolger = neuerKnoten` | 1 | 0 |

`text` zu den Schritten 3…: „Der Hilfszeiger `lauf` wandert. Jeder dieser Klicks ist ein
Knotenbesuch — und der Grund, warum `append` teuer ist."
**Summe: 1 Referenzänderung, <span class="m" data-tex="n" data-plain="n"></span> Knotenbesuche
bei <span class="m" data-tex="n" data-plain="n"></span> Knoten** (bei leerer Liste 0 Besuche).

#### Liste — `insert(x)`

Vorbedingung: Es gibt ein aktuelles Objekt. Ist `S.aktuell === null` und die Liste nicht leer,
besteht die Schrittfolge nur aus einer Prüfzeile mit dem `text`: „Ohne aktuelles Objekt fügt
`insert` in eine nicht leere Liste nichts ein. Setze erst `toFirst()`."

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `Knoten neu = new Knoten("x");` | `neuerKnoten` entsteht | 0 | 0 |
| 2 | `neu.setzeNachfolger(aktuell);` | `neuerKnoten.nachfolger = S.aktuell` | 1 | 0 |
| 3 | `anfang = neu;` **oder** `vorgaenger.setzeNachfolger(neu);` | wenn `S.vorgaenger === null`: `S.kopf = neuerKnoten`, sonst `S.vorgaenger.nachfolger = neuerKnoten` | 1 | 0 |
| 4 | `vorgaenger = neu;` | `S.vorgaenger = neuerKnoten` | 1 | 0 |

`text` zu Schritt 4: „Das aktuelle Objekt bleibt dasselbe wie vorher — der neue Knoten wird
sein Vorgänger. Das ist die Stelle, an der im Abitur die meisten Punkte verloren gehen."
**Summe: 3 Referenzänderungen, 0 Knotenbesuche.**

#### Liste — `remove()`  ·  **das ist der Kern der Simulation**

| # | `code` | Wirkung | ΔRef | ΔBes |
|---|---|---|---|---|
| 1 | `if (aktuell == null) { return; }` | Prüfung | 0 | 0 |
| 2 | `vorgaenger.setzeNachfolger(aktuell.gibNachfolger());` **oder** `anfang = aktuell.gibNachfolger();` | wenn `S.vorgaenger !== null`: `S.vorgaenger.nachfolger = S.aktuell.nachfolger`, sonst `S.kopf = S.aktuell.nachfolger` | 1 | 0 |
| 3 | `aktuell = aktuell.gibNachfolger();` | `entfernt = S.aktuell; S.aktuell = S.aktuell.nachfolger` | 1 | 0 |

**Zeichnerische Sonderbehandlung von Schritt 2 — verbindlich.** Dieser Schritt ist der
didaktische Kern der ganzen Seite und muss sichtbar sein:

- Vor der Ausführung wird der **bestehende** Pfeil vom Vorgängerknoten zum aktuellen Knoten
  rot gestrichelt hervorgehoben, und daneben wird der **künftige** Pfeil vom Vorgängerknoten
  über den aktuellen Knoten hinweg zum übernächsten Knoten als roter, gestrichelter Bogen
  **oberhalb** der Kastenreihe angedeutet (Scheitel bei y = 128).
- Nach der Ausführung wird dieser Bogen rot durchgezogen gezeichnet. Der aktuelle Knoten
  bleibt zunächst an seinem Platz stehen, ist aber nun **von keinem Pfeil mehr erreicht**.
- Erst Schritt 3 setzt `entfernt` und lässt den Knoten in die graue Zone bei y = 285 fallen,
  mit der Bildunterschrift: „entfernt — keine Referenz zeigt mehr hierher".

`text` zu Schritt 2: „Der Vorgänger überspringt den aktuellen Knoten. Beachte, dass der
aktuelle Knoten selbst weiterhin auf seinen alten Nachfolger zeigt — deshalb liefert
`aktuell.gibNachfolger()` im nächsten Schritt noch den richtigen Knoten."
`text` zu Schritt 3: „Der Nachfolger wird zum neuen aktuellen Objekt. War der entfernte Knoten
der letzte, ist `aktuell` jetzt `null` und `hasAccess()` liefert `false`."
**Summe: 2 Referenzänderungen, 0 Knotenbesuche.**

#### Liste — `getContent()` und `setContent(x)`

`getContent()`: ein Schritt, `code: "return aktuell.gibInhalt();"`, setzt `letzterWert`. 0 / 0.

`setContent(x)`: ein Schritt, `code: "aktuell.setzeInhalt(\"x\");"`, setzt
`S.aktuell.inhalt = x`. **0 Referenzänderungen, 0 Knotenbesuche.** `text`: „Der Inhalt ändert
sich, die Kette nicht. Beide Zähler bleiben stehen — Inhalt und Verkettung sind zwei
getrennte Dinge."

### 4.6 Zeichnung: Maße und Farben (verbindlich)

Canvas `id="cvSim"`, `width="1000"`, `height="340"`, per CSS `width:100%`.

```js
var CV_B = 1000, CV_H = 340;
var X0     = 55;    // linke Kante des ersten Kastens
var RASTER = 145;   // Abstand von Kastenanfang zu Kastenanfang
var K_B    = 105;   // Kastenbreite  = 70 + 35
var K_H    = 60;    // Kastenhoehe
var K_Y    = 150;   // Oberkante der Kastenreihe
var F_INH  = 70;    // Breite des Inhaltsfeldes
var F_REF  = 35;    // Breite des Referenzfeldes
var P_X    = 87;    // Pfeilstart, relativ zum Kastenanfang (Mitte des Referenzfeldes)
var P_L    = 58;    // Pfeillaenge bis zum naechsten Kastenanfang (145 - 87)
var MAX_KNOTEN = 6;
```

Kastenposition des <span class="m" data-tex="i" data-plain="i"></span>-ten Knotens der Kette
(<span class="m" data-tex="i = 0 \dots 5" data-plain="i = 0 … 5"></span>):

<div class="m block" data-tex="x_i = 55 + i \cdot 145" data-plain="x_i = 55 + i · 145"></div>

Damit liegt der sechste Knoten bei <span class="m" data-tex="x_5 = 780" data-plain="x₅ = 780"></span>,
seine rechte Kante bei 885 px. Die verbleibenden 115 px tragen das `null`-Zeichen.
(Nachgerechnet in Abschnitt 8, Rechnung R6.)

**Ein Knoten wird so gezeichnet:**

1. Rechteck `(x, 150, 105, 60)`, Eckradius 6, Füllung `#fef6e7`, Rand `#b45309`, 2 px.
2. Senkrechte Trennlinie bei `x + 70` von `y = 150` bis `y = 210`, 1 px, `#f3ddb3`.
3. Inhalt zentriert bei `(x + 35, 188)`, Schrift `bold 24px system-ui`, Farbe `#111827`.
4. Im Referenzfeld: hat der Knoten einen Nachfolger, ein gefüllter Kreis mit Radius 5 bei
   `(x + 87, 180)`; sonst das Zeichen `∅` zentriert bei `(x + 87, 188)` in `#6b7280`.
5. Bei vorhandenem Nachfolger ein waagerechter Pfeil von `(x + 87, 180)` nach
   `(x + 145, 180)`, 2 px, `#b45309`, mit gefüllter Spitze (Länge 9, halbe Breite 5).
6. Beim letzten Knoten der Kette zusätzlich das Wort `null` in `italic 15px`, `#6b7280`,
   bei `(x + 120, 185)`.

**Die vier Zeiger** werden als senkrechte Pfeile mit Beschriftung gezeichnet. Der
Kastenanfang des Zielknotens heißt `xz`:

| Zeiger | Pfeil-x | von y | bis y | Beschriftung bei y | Farbe |
|---|---|---|---|---|---|
| `kopf` / `anfang` | `xz + 30` | 126 | 148 | 120 | `#b45309` |
| `ende` | `xz + 75` | 100 | 148 | 94 | `#0d7a52` |
| `aktuell` | `xz + 30` | 240 | 214 | 256 | `#1d4ed8` |
| `vorgaenger` | `xz + 75` | 272 | 214 | 288 | `#6b7280` |
| `lauf` (nur bei `append`) | `xz + 52` | 300 | 214 | 315 | `#b45309`, gestrichelt |

Die versetzten x-Werte sorgen dafür, dass `kopf` und `ende` auch dann unterscheidbar bleiben,
wenn sie auf denselben Knoten zeigen — genau das ist bei einer Schlange mit einem Element der
Fall und soll sichtbar sein. Zeiger mit dem Wert `null` werden als Beschriftung ganz links
bei `x = 10` mit dem Text `kopf = null` (usw.) in Grau gesetzt, ohne Pfeil.

**Der freie neue Knoten** (`neuerKnoten`, nach `new` und vor der Verkettung) wird bei
`(X0 + n·145, 20)` mit Höhe 60 gezeichnet, wobei `n` die aktuelle Kettenlänge ist, Rand
gestrichelt in `#b45309`, links daneben die Beschriftung `neu`.

**Der entfernte Knoten** (`entfernt`) wird bei `(x, 285)` mit Höhe 45 in Grau (`#9ca3af` Rand,
`#f3f4f6` Füllung) gezeichnet, darunter bei `(x + 52, 332)` in `12px` die Zeile
„entfernt — keine Referenz zeigt mehr hierher". Der Bereich unterhalb von `y = 280` wird von
`entfernt` und `lauf` geteilt; beide treten nie gleichzeitig auf (`remove` gegen `append`).

**Hervorhebung der sich ändernden Referenz:** Farbe `#dc2626`, 3 px. Vor der Ausführung
gestrichelt (`setLineDash([6,4])`), nach der Ausführung durchgezogen. Nur genau eine Referenz
je Schritt.

### 4.7 Bedienelemente

**`.knopfleiste` 1 — Strukturwahl** (drei Schaltflächen; die aktive trägt die Klasse
`primaer`; ein Wechsel setzt das Modell und beide Zähler zurück):

`Stapel` · `Schlange` · `Liste`

**`.regler`-Bereich — kein Schieberegler, sondern:**

- Textfeld `#eInhalt`, `maxlength="3"`, Breite ca. 90 px, Startwert `A`. Nach jedem
  erfolgreichen Einfügen rückt der Wert automatisch zum nächsten Großbuchstaben vor
  (`A → B → … → Z → A`).
- Kontrollkästchen `#cSchritt`, Beschriftung „Schritt für Schritt", **standardmäßig
  angehakt**.

**`.knopfleiste` 2 — Operationen** (Beschriftung und Sichtbarkeit hängen von `struktur` ab):

| Struktur | Schaltflächen |
|---|---|
| Stapel | `push(x)` · `pop()` · `top()` |
| Schlange | `enqueue(x)` · `dequeue()` · `front()` |
| Liste | `toFirst()` · `next()` · `append(x)` · `insert(x)` · `remove()` · `setContent(x)` · `getContent()` |

**`.knopfleiste` 3 — Ablauf:** `Nächster Schritt` (nur im Schrittmodus aktiv, sonst
deaktiviert) · `Zurücksetzen`

### 4.8 Anzeigen und Protokoll

**`.anzeige` unter dem Canvas — fünf Felder:**

| Beschriftung | Inhalt | Startwert |
|---|---|---|
| Struktur | `Stapel` / `Schlange` / `Liste` | Stapel |
| Knoten in der Kette | ganze Zahl | 0 |
| Referenzänderungen | ganze Zahl, kumuliert seit dem Zurücksetzen | 0 |
| besuchte Knoten | ganze Zahl, kumuliert seit dem Zurücksetzen | 0 |
| letzter Rückgabewert | Zeichenkette oder `null` | — |

Alle Zahlen sind ganzzahlig; die `fmt`-Funktion mit Komma wird hier **nicht** gebraucht, weil
in dieser Simulation ausschließlich abzählbare Größen vorkommen. Das ist der einzige
begründete Abweichungspunkt von der Kommaregel — es gibt keine Nachkommastellen.

**Protokollfeld** direkt unter der `.anzeige`, `id="pProtokoll"`, mit Inline-Stil
`background:#fff;border:1px solid var(--akzent-rand);border-radius:8px;padding:12px 14px;min-height:78px`:

- Zeile 1: die Java-Zeile des aktuellen Schritts in `<code>`, bei anstehendem Schritt in
  `#dc2626`, bei ausgeführtem Schritt in `#111827`.
- Zeile 2: der `text` des Schritts in normaler Schrift, `font-size:15px`.
- Zeile 3, nur im Schrittmodus: `Schritt 2 von 3`.

### 4.9 Die beiden Verständnisfragen zur Simulation

---

#### `sim1` — Anforderungsbereich II

**Frage:**
Du hast in jede der drei Strukturen aus dem leeren Zustand nacheinander A, B, C, D und E
eingefügt. In welchen Strukturen steht danach A am Kopf der Kette — also dort, wohin
`kopf` beziehungsweise `anfang` zeigt?

**Optionen (feste Reihenfolge):**

| `data-i` | Text |
|---|---|
| 0 | Nur im Stapel, weil A zuerst eingefügt wurde und deshalb ganz vorn liegt. |
| 1 | In der Schlange und in der Liste; im Stapel zeigt `kopf` auf E. |
| 2 | In allen drei Strukturen, weil alle A als Erstes aufgenommen haben. |

**Richtig:** `r: 1`

**Feedback je Option:**

- **0** — Genau umgekehrt. `push` schiebt jeden neuen Knoten **vor** den bisherigen Kopf.
  A wurde zwar zuerst eingefügt, ist damit aber ans Kettenende gerutscht; der Kopfzeiger
  steht am Ende auf E. Stelle den Stapel ein und sieh dir an, wohin der braune Pfeil zeigt.
- **1** — Richtig. `enqueue` und `append` hängen hinten an, der Kopf bleibt also unangetastet
  auf A stehen. `push` fügt vorn ein und verschiebt den Kopf bei jedem Aufruf.
- **2** — Die Simulation widerlegt das unmittelbar: Beim Stapel zeigt `kopf` nach dem fünften
  `push` auf E, und die Kette liest sich E, D, C, B, A. Nur weil ein Element zuerst
  aufgenommen wurde, steht es nicht vorn — das entscheidet allein die Einfügeoperation.

---

#### `sim2` — Anforderungsbereich II

**Frage:**
Du hast die Zähler vor jedem Durchgang zurückgesetzt und dann fünfmal eingefügt. Welche Werte
zeigt der Zähler **„besuchte Knoten"** anschließend an?

**Optionen (feste Reihenfolge):**

| `data-i` | Text |
|---|---|
| 0 | Liste 10, Schlange 0, Stapel 0 |
| 1 | Liste 5, Schlange 5, Stapel 5 |
| 2 | Liste 0, Schlange 10, Stapel 10 |

**Richtig:** `r: 0`

**Feedback je Option:**

- **0** — Richtig. `append` muss jedes Mal von `anfang` bis ans Ende laufen; bei Listenlängen
  von 0, 1, 2, 3 und 4 sind das 0 + 1 + 2 + 3 + 4 = 10 Besuche. `enqueue` und `push` arbeiten
  an einem Zeiger, den die Struktur bereits hält, und laufen deshalb nie ab.
- **1** — Du zählst je Einfügung einen Besuch, also einen pro Aufruf. Der Zähler erfasst aber
  nicht das Anlegen eines Knotens, sondern nur das Ablaufen der Kette entlang der
  Nachfolgerzeiger. Beim ersten `append` in die leere Liste wird gar nichts abgelaufen — dort
  steht 0, nicht 1.
- **2** — Du hast die beiden Zähler vertauscht. Die 10 gehört zu den *Referenzänderungen* von
  Schlange und Stapel (je 2 pro Einfügen). Bei den *Knotenbesuchen* stehen beide auf 0, und
  die Liste hat dort die 10 — sie ändert je `append` nur eine Referenz, läuft dafür aber
  jedes Mal die Kette ab.

### 4.10 Pflichtprüfung vor der Auslieferung

Der Bauagent prüft die Simulation gegen die Handrechnung aus Abschnitt 8:

1. Struktur **Stapel**, zurücksetzen, fünfmal `push` mit A, B, C, D, E →
   Kette muss `E D C B A` lauten, Referenzänderungen **10**, besuchte Knoten **0**.
2. Struktur **Schlange**, zurücksetzen, fünfmal `enqueue` mit A…E →
   Kette `A B C D E`, Referenzänderungen **10**, besuchte Knoten **0**.
   Danach dreimal `dequeue`, dann `enqueue("D")` → Kette muss `D` lauten und `front()` muss
   `D` liefern (Endzeiger-Sonderfall).
3. Struktur **Liste**, zurücksetzen, fünfmal `append` mit A…E →
   Kette `A B C D E`, Referenzänderungen **5**, besuchte Knoten **10**.
4. Struktur **Liste**, zurücksetzen, viermal `append` mit A, B, C, D, dann `toFirst()`,
   `next()`, `remove()` → Kette `A C D`, `aktuell` zeigt auf **C**, `vorgaenger` auf **A**.
5. Struktur **Liste**, Kette `A B C`, `toFirst()`, `next()`, `insert("X")` →
   Kette `A X B C`, `aktuell` weiterhin auf **B**, `vorgaenger` auf **X**.

## 5 Übungen

Abschnitt 6 der Seite, `id="uebungen"`, Überschrift **„Übungen"**.

Acht Aufgaben, verteilt auf die Anforderungsbereiche I (a1, a2), II (a3, a4, a5, a6) und
III (a7, a8). Sämtliche Zahlenwerte sind in Abschnitt 8 nachgerechnet und durch
`vorarbeit/info/aufgaben.py` maschinell bestätigt.

**Einleitender Satz über den Aufgaben:**

> Acht Aufgaben, vom Nachvollziehen bis zum Bewerten. Bei den letzten beiden gibt es keine
> Zahl als Lösung, sondern eine Begründung — und die Bewertungskriterien stehen dabei, damit
> du selbst prüfen kannst, ob deine Antwort trägt.

---

### `a1` — Anforderungsbereich I — Zahleneingabe

**Aufgabentext:**

> Auf einen leeren Stapel wird folgende Befehlsfolge angewendet:
> `push("A")`, `push("B")`, `pop()`, `push("C")`, `push("D")`, `pop()`, `pop()`, `push("E")`.
> Wie viele Elemente enthält der Stapel danach?

**Einheitenliste im `<select>` (in dieser Reihenfolge):**
`Elemente` · `Knotenbesuche` · `Referenzänderungen` · `Byte`

`Byte` ist der fachlich falsche Distraktor: Eine Anzahl von Elementen ist keine Speichergröße.

**`numDaten`-Eintrag:**

```js
a1:{ wert:2, einheit:"Elemente", tol:0.5,
     ok:"Richtig. Die Kette lautet von unten nach oben A, E — es bleiben 2 Elemente, und top() liefert E.",
     falschEinheit:"Der Zahlenwert stimmt. Gefragt ist aber eine Stückzahl: Wie viele Knoten haengen noch in der Kette? Das ist weder eine Speichergroesse noch ein Zaehler fuer Besuche.",
     nah:"Du bist um ein Element daneben. Zaehle die Befehlsfolge noch einmal Schritt fuer Schritt ab und achte auf das dritte pop(): Es entfernt D, nicht A.",
     weit:"Zaehle nicht die Anzahl der Befehle, sondern fuehre sie nacheinander aus. Fuenf push und drei pop ergeben 5 − 3 Elemente — vorausgesetzt, kein pop trifft auf einen leeren Stapel. Pruefe das mit dem Tipp." }
```

**Hilfen:**

- **Stufe 1 (Tipp):** Schreibe den Stapel nach jedem einzelnen Befehl als Liste von unten nach
  oben auf. Acht Zeilen, mehr braucht es nicht.
- **Stufe 2 (Ansatz):** Jedes `push` legt genau ein Element oben auf, jedes `pop` nimmt genau
  eines oben weg. Prüfe bei jedem `pop`, ob der Stapel überhaupt etwas enthält — sonst
  passiert nichts. Zähle am Ende, was übrig ist.
- **Stufe 3 (Lösungsweg):**
  `push("A")` → A · `push("B")` → A, B · `pop()` → A · `push("C")` → A, C ·
  `push("D")` → A, C, D · `pop()` → A, C · `pop()` → A · `push("E")` → A, E.
  Kein `pop` trifft auf einen leeren Stapel. Es bleiben **2 Elemente**; `top()` liefert `"E"`,
  darunter liegt `"A"`. Beachte: `"A"` ist nie entfernt worden, obwohl es zuerst eingefügt
  wurde — das ist LIFO.

---

### `a2` — Anforderungsbereich I — Zahleneingabe

**Aufgabentext:**

> Eine `EinfacheListe` enthält die Elemente A, B, C. Es wird `toFirst()` und danach `next()`
> aufgerufen; anschließend `insert("X")`. Wie viele Referenzen werden **allein durch den
> Aufruf von `insert`** verändert?

**Einheitenliste im `<select>`:**
`Referenzänderungen` · `Knotenbesuche` · `Knoten` · `Byte`

**`numDaten`-Eintrag:**

```js
a2:{ wert:3, einheit:"Referenzänderungen", tol:0.5,
     ok:"Richtig. neu.setzeNachfolger(aktuell), vorgaenger.setzeNachfolger(neu) und vorgaenger = neu — genau drei. Die Liste lautet danach A, X, B, C, und das aktuelle Objekt ist weiterhin B.",
     falschEinheit:"Die Zahl stimmt. Gefragt ist aber, wie oft eine Referenz umgebogen wird — nicht, wie viele Knoten dabei besucht oder angelegt werden. insert besucht uebrigens null Knoten.",
     nah:"Dir fehlt eine der drei Zuweisungen. Am haeufigsten wird die letzte vergessen: Nach dem Einfuegen muss auch der vorgaenger-Zeiger nachgefuehrt werden, sonst zeigt er auf einen Knoten, der nicht mehr direkt vor dem aktuellen Objekt steht.",
     weit:"Zaehle nicht die Knoten der Liste, sondern die Zuweisungen im Rumpf von insert(). Sieh dir den Java-Block in Abschnitt 3 an: Wie viele Zeilen darin aendern eine Referenz? Das Anlegen des Knotens mit new zaehlt nicht mit." }
```

**Hilfen:**

- **Stufe 1 (Tipp):** Stelle zuerst fest, welcher Knoten nach `toFirst(); next()` das aktuelle
  Objekt ist und wer sein Vorgänger ist. Erst dann schau in den Rumpf von `insert`.
- **Stufe 2 (Ansatz):** Zähle im Rumpf von `insert` genau die Zuweisungen, deren linke Seite
  ein Referenzfeld ist: `neu.nachfolger`, dann entweder `anfang` oder
  `vorgaenger.nachfolger`, und schließlich `vorgaenger` selbst. `new Knoten(...)` ist keine
  Referenzänderung.
- **Stufe 3 (Lösungsweg):** Nach `toFirst()` ist `aktuell` = A und `vorgaenger` = `null`;
  nach `next()` ist `aktuell` = B und `vorgaenger` = A. `insert("X")` führt aus:
  (1) `neu.setzeNachfolger(aktuell)` — X zeigt auf B;
  (2) `vorgaenger` ist nicht `null`, also `vorgaenger.setzeNachfolger(neu)` — A zeigt auf X;
  (3) `vorgaenger = neu` — X ist der neue Vorgänger.
  Das sind **3 Referenzänderungen** und 0 Knotenbesuche. Ergebnis: A, X, B, C; das aktuelle
  Objekt ist unverändert B.

---

### `a3` — Anforderungsbereich II — Zahleneingabe

**Aufgabentext:**

> Eine `EinfacheListe` in der Fassung aus Abschnitt 3 — also **ohne** Endzeiger — enthält
> 1200 Knoten. Nun wird dreimal hintereinander `append` aufgerufen. Wie viele Knotenbesuche
> fallen dabei insgesamt an? Ein Knotenbesuch ist jede Auswertung, die den Hilfszeiger `lauf`
> auf einen Knoten setzt, `lauf = anfang` eingeschlossen.

**Einheitenliste im `<select>`:**
`Knotenbesuche` · `Referenzänderungen` · `Byte` · `kB`

**`numDaten`-Eintrag:**

```js
a3:{ wert:3603, einheit:"Knotenbesuche", tol:0.5,
     ok:"Richtig. 1200 + 1201 + 1202 = 3603. Die Liste waechst zwischen den Aufrufen mit, deshalb wird jeder Aufruf ein Stueck teurer.",
     falschEinheit:"Die Zahl stimmt. Knotenbesuche sind aber eine Anzahl von Schritten, keine Speichergroesse — mit Byte oder kB waere die Frage nach dem Platzbedarf gemeint, nicht nach dem Aufwand.",
     nah:"Du bist dicht dran, hast aber vermutlich mit einer konstanten Listenlaenge gerechnet: 3 · 1200 = 3600. Die Liste ist beim zweiten Aufruf aber schon 1201 und beim dritten 1202 Knoten lang.",
     weit:"Rechne nicht mit der Zahl der Aufrufe, sondern mit der Laenge der Liste. Ein einziges append an eine Liste mit n Knoten kostet n Besuche — und n waechst nach jedem Aufruf um eins. Sieh dir Stufe 2 an." }
```

**Hilfen:**

- **Stufe 1 (Tipp):** Die Liste ist nach dem ersten `append` nicht mehr 1200 Knoten lang.
  Schreibe die drei Aufrufe einzeln untereinander.
- **Stufe 2 (Ansatz):** Ein `append` an eine Liste mit
  <span class="m" data-tex="n" data-plain="n"></span> Knoten kostet genau
  <span class="m" data-tex="n" data-plain="n"></span> Besuche: einen für `lauf = anfang` und
  <span class="m" data-tex="n-1" data-plain="n−1"></span> weitere im Schleifenrumpf. Addiere
  die drei Werte für <span class="m" data-tex="n = 1200,\ 1201,\ 1202" data-plain="n = 1200, 1201, 1202"></span>.
- **Stufe 3 (Lösungsweg):**
  1. Aufruf: Liste hat 1200 Knoten → 1200 Besuche.
  2. Aufruf: Liste hat 1201 Knoten → 1201 Besuche.
  3. Aufruf: Liste hat 1202 Knoten → 1202 Besuche.
  Summe: <span class="m" data-tex="1200 + 1201 + 1202 = 3603" data-plain="1200 + 1201 + 1202 = 3603"></span> **Knotenbesuche**.
  Gegenprobe über den mittleren Wert: <span class="m" data-tex="3 \cdot 1201 = 3603" data-plain="3 · 1201 = 3603"></span>.
  Mit einem Endzeiger wären es **0** Besuche gewesen — für drei zusätzliche Zeilen Code.

---

### `a4` — Anforderungsbereich II — Zahleneingabe

**Aufgabentext:**

> Ein Bibliothekssystem verwaltet 1200 ausgeliehene Medien. Verglichen werden eine verkettete
> Liste, bei der jeder Knoten eine Inhalts- und eine Nachfolgerreferenz trägt, und ein Array,
> das nur die Inhaltsreferenzen speichert. Eine Referenz belege 4 Byte; Objektköpfe und
> Ausrichtung bleiben in diesem Modell unberücksichtigt. Wie viel Speicher braucht die
> verkettete Liste **mehr** als das Array?

**Einheitenliste im `<select>`:**
`B` · `kB` · `MB` · `Knoten`

`Knoten` ist der fachlich falsche Distraktor: Ein Speicherbedarf ist keine Stückzahl.

**`numDaten`-Eintrag:**

```js
a4:{ wert:4800, einheit:"B", tol:1,
     alt:{wert:4.8, einheit:"kB"},
     ok:"Richtig. 9600 B − 4800 B = 4800 B = 4,8 kB. Die Verkettung kostet in diesem Modell genau das Doppelte — der Aufschlag ist die zweite Referenz je Knoten.",
     falschEinheit:"Der Zahlenwert passt zu einer anderen Einheit als der gewaehlten. 4800 gehoert zu Byte, 4,8 zu Kilobyte. Die Einheit Knoten scheidet aus: Gefragt ist Speicher, nicht Stueckzahl.",
     nah:"Vermutlich hast du den Gesamtbedarf der Kette statt des Mehrbedarfs angegeben — das waeren 9600 B. Gefragt ist die Differenz zum Array.",
     weit:"Rechne beide Groessen getrennt aus: Die Kette braucht je Knoten zwei Referenzen, das Array je Element eine. Bilde erst danach die Differenz. Stufe 2 zeigt den Ansatz." }
```

**Hilfen:**

- **Stufe 1 (Tipp):** Zähle zuerst, wie viele Referenzen ein einzelner Knoten trägt und wie
  viele eine Arrayzelle. Der Unterschied ist eine einzige Referenz.
- **Stufe 2 (Ansatz):** <span class="m" data-tex="S_{\text{Kette}} = n \cdot 2 \cdot 4\,\mathrm{B}" data-plain="S_Kette = n · 2 · 4 B"></span>
  und <span class="m" data-tex="S_{\text{Array}} = n \cdot 4\,\mathrm{B}" data-plain="S_Array = n · 4 B"></span>.
  Gesucht ist <span class="m" data-tex="S_{\text{Kette}} - S_{\text{Array}}" data-plain="S_Kette − S_Array"></span>.
  Rechne mit <span class="m" data-tex="1\,\mathrm{kB} = 1000\,\mathrm{B}" data-plain="1 kB = 1000 B"></span>.
- **Stufe 3 (Lösungsweg):**
  <span class="m" data-tex="S_{\text{Kette}} = 1200 \cdot (4\,\mathrm{B} + 4\,\mathrm{B}) = 9600\,\mathrm{B}" data-plain="S_Kette = 1200 · (4 B + 4 B) = 9600 B"></span>;
  <span class="m" data-tex="S_{\text{Array}} = 1200 \cdot 4\,\mathrm{B} = 4800\,\mathrm{B}" data-plain="S_Array = 1200 · 4 B = 4800 B"></span>.
  Mehrbedarf: <span class="m" data-tex="9600\,\mathrm{B} - 4800\,\mathrm{B} = 4800\,\mathrm{B} = 4{,}8\,\mathrm{kB}" data-plain="9600 B − 4800 B = 4800 B = 4,8 kB"></span>,
  also **Faktor 2**. Zur Einordnung: Für diesen Aufschlag bekommt man Einfügen und Löschen an
  bekannter Stelle ohne jedes Umkopieren. In einem echten Java-Programm fiele der Aufschlag
  wegen der Objektköpfe deutlich größer aus — deshalb steht „in diesem Modell" in der Aufgabe.

---

### `a5` — Anforderungsbereich II — Multiple Choice

**Frage:**

> In der Methode `dequeue()` der `EinfacheSchlange` wird die letzte Zeile
> `if (kopf == null) { ende = null; }` vergessen. Alles andere bleibt wie im Java-Block aus
> Abschnitt 3. Wie wirkt sich dieser Fehler aus?

**Optionen (feste Reihenfolge):**

| `data-i` | Text |
|---|---|
| 0 | Sofort: Nach dem letzten `dequeue()` liefert `front()` einen falschen Wert statt `null`. |
| 1 | Erst später und nur indirekt: `enqueue` repariert beide Zeiger über seinen Leer-Zweig, aber bis dahin hält `ende` einen Knoten fest, der die Schlange längst verlassen hat. |
| 2 | Gar nicht: `ende` wird bei jedem `enqueue` ohnehin neu gesetzt, die Zeile kann ersatzlos entfallen. |

**Richtig:** `r: 1`

**Feedback je Option:**

- **0** — `front()` liest `kopf`, nicht `ende`. Und `kopf` ist nach dem letzten `dequeue()`
  korrekt `null`, also liefert `front()` korrekt `null`. Der Fehler sitzt nicht im Lesen,
  sondern in einem Zeiger, den anschließend niemand mehr überprüft — genau das macht ihn so
  schwer zu finden.
- **1** — Richtig. `enqueue` prüft den Leerfall über `kopf == null` und setzt in diesem Zweig
  `kopf` **und** `ende` neu. Das Verhalten nach außen bleibt deshalb korrekt. Der veraltete
  `ende`-Verweis hält den entfernten Knoten aber am Leben — der Garbage Collector kann ihn
  nicht abräumen, obwohl er logisch nicht mehr zur Schlange gehört.
- **2** — Das Ergebnis stimmt hier nur zufällig, weil `enqueue` seinen Leerfall über `kopf`
  abfragt. Fragte `enqueue` stattdessen `ende == null` ab — eine völlig naheliegende
  Variante —, liefe die Methode in den Else-Zweig und hängte den neuen Knoten an einen
  längst entfernten. Eine Zeile, deren Entbehrlichkeit von der Implementierung einer
  *anderen* Methode abhängt, ist nicht überflüssig, sondern gefährlich.

---

### `a6` — Anforderungsbereich II — Zuordnungsaufgabe

Dies ist die **einzige** Zuordnungsaufgabe des Moduls; die Engine läuft laut
`vorlage/bausteine.md` über einen festen Selektor und darf unverändert übernommen werden.

**Aufgabentext:**

> Ordne jeder Anwendung die Struktur zu, die zu ihrem Zugriffsmuster passt. Die vier Skizzen
> A bis D zeigen dieselben Daten mit unterschiedlichen Zugriffsstellen.

**Die vier Skizzen als Inline-SVG in `.diagramme`** — jeweils rund 200 × 110 px, dieselben
vier Kästen mit den Inhalten P, Q, R, S, unterschiedlich beschriftet:

| Skizze | Darstellung |
|---|---|
| **A** | Kette P → Q → R → S mit **einem** Zeiger `kopf` auf P; darüber zwei gebogene Pfeile am selben Ende, beschriftet `push` (hinein) und `pop` (heraus) |
| **B** | Kette P → Q → R → S mit `kopf` auf P und `ende` auf S; Pfeil `enqueue` zeigt rechts hinein, Pfeil `dequeue` links heraus |
| **C** | Kette P → Q → R → S mit `anfang` auf P und zusätzlich `aktuell` auf R sowie `vorgaenger` auf Q; Pfeile `insert`/`remove` setzen mitten an R an |
| **D** | Vier **lückenlos aneinandergesetzte** Kästen ohne Verbindungspfeile, darunter die Indizes 0, 1, 2, 3; ein Pfeil beschriftet `daten[2]` zeigt direkt auf den dritten Kasten |

**Die Zeilen (Reihenfolge bewusst nicht wie A, B, C, D):**

| Zeile | Text | `data-loesung` |
|---|---|---|
| 1 | Die Rückgängig-Funktion eines Editors nimmt stets den zuletzt ausgeführten Arbeitsschritt zuerst zurück. | `A` |
| 2 | Ein Bild wird als Raster gespeichert; das Programm greift ständig auf beliebige Bildpunkte zu, und die Größe steht von Anfang an fest. | `D` |
| 3 | Eine Kursliste, aus der laufend an beliebiger Stelle Einträge entfernt und eingefügt werden, während man sie ohnehin von vorn durchgeht; auf „Eintrag Nummer 12" wird nie zugegriffen. | `C` |
| 4 | Druckaufträge mehrerer Rechner werden in der Reihenfolge ihres Eingangs abgearbeitet. | `B` |

**Rückmeldung bei Teilerfolg** (nennt die Denkstrategie, nicht die Lösung):

> Noch nicht alles richtig. Geh nicht von der Anwendung aus, sondern von der Frage: An wie
> vielen Stellen wird zugegriffen — an einer, an zweien oder an beliebigen? Und muss dabei
> gerechnet werden können, an welcher Position ein Element liegt? Die Antwort auf diese zwei
> Fragen legt die Struktur schon fest.

**Rückmeldung bei vollständiger Lösung:**

> Alle vier richtig. Beachte den Unterschied zwischen Zeile 2 und Zeile 3: Beide verwalten
> viele gleichartige Daten, aber die eine braucht wahlfreien Zugriff bei fester Größe, die
> andere ständiges Einfügen und Löschen an wandernder Stelle. Genau daran — und nicht an der
> Datenmenge — entscheidet sich die Wahl.

---

### `a7` — Anforderungsbereich III — Begründungsaufgabe (offen)

**Aufgabentext:**

> Ein Programm soll prüfen, ob die runden und eckigen Klammern eines Ausdrucks korrekt
> geschachtelt sind. Der übliche Algorithmus legt jede öffnende Klammer in einen Behälter und
> entnimmt bei jeder schließenden Klammer eine daraus, die zu ihr passen muss. Eine
> Mitschülerin schlägt vor, dafür statt eines Stapels eine Schlange zu verwenden — „das
> speichert schließlich genauso alle offenen Klammern".
>
> Nimm begründet Stellung. Gib dabei **zwei** Gegenbeispiele an: einen korrekt geschachtelten
> Ausdruck, den die Schlangenfassung fälschlich ablehnt, und einen fehlerhaften Ausdruck, den
> sie fälschlich annimmt.

**Musterlösung** (`.hilfe-text[data-stufe="9"]`, umgeschaltet über
`<button data-loesung="a7">`):

*Erwartete Argumentation:*

> Schachtelung heißt: Die zuletzt geöffnete Klammer muss als Erste wieder geschlossen werden.
> Genau diese Reihenfolge ist die LIFO-Disziplin des Stapels — die Struktur bildet die
> Eigenschaft ab, die geprüft werden soll. Eine Schlange gibt die Klammern in der Reihenfolge
> ihres Auftretens zurück (FIFO) und vergleicht damit systematisch die falschen Paare
> miteinander. Der Vorschlag scheitert also nicht an der Speicherung — die Schlange merkt
> sich dieselben Zeichen —, sondern an der Entnahmereihenfolge. Der Behälter ist hier kein
> Zwischenspeicher, sondern der eigentliche Prüfmechanismus.
>
> **Erstes Gegenbeispiel — fälschlich abgelehnt: `([])`.**
> Der Ausdruck ist korrekt geschachtelt. Die Schlange nimmt `(` und `[` auf. Beim ersten
> schließenden Zeichen `]` entnimmt sie vorn `(` — das passt nicht, und sie lehnt ab. Der
> Stapel entnimmt oben `[`, was passt, danach `(` zur `)`, und akzeptiert korrekt.
>
> **Zweites Gegenbeispiel — fälschlich angenommen: `([)]`.**
> Der Ausdruck ist falsch geschachtelt: `(` wird geschlossen, bevor die innere `[` geschlossen
> ist. Die Schlange nimmt `(` und `[` auf; zu `)` entnimmt sie vorn `(` — passt; zu `]`
> entnimmt sie `[` — passt ebenfalls; der Behälter ist leer, sie akzeptiert. Der Stapel
> entnimmt zu `)` oben `[`, stellt den Widerspruch fest und lehnt korrekt ab.
>
> Die Schlangenfassung irrt also **in beide Richtungen**. Sie ist nicht bloß ungenauer,
> sondern prüft eine andere Eigenschaft: nicht die Schachtelung, sondern lediglich, ob die
> öffnenden und schließenden Klammern in gleicher Reihenfolge und Anzahl vorkommen.

*Bewertungskriterien (fett, mit `·` getrennt):*

> **Bewertungskriterien** · benennt LIFO als die Reihenfolge, die Schachtelung überhaupt
> ausmacht, und stellt sie FIFO gegenüber · erkennt, dass nicht die Speicherung, sondern die
> Entnahmereihenfolge das Problem ist · gibt ein korrektes Beispiel an, das die Schlange
> fälschlich ablehnt, und führt dessen Ablauf nachvollziehbar vor · gibt ein fehlerhaftes
> Beispiel an, das die Schlange fälschlich annimmt, und führt dessen Ablauf vor · hält fest,
> dass der Fehler in beide Richtungen auftritt und die Schlangenfassung damit unbrauchbar ist,
> nicht nur schlechter · Sprachliche Anforderung: Die Begründung nennt die Struktureigenschaft
> (LIFO/FIFO), nicht nur das Ergebnis der Beispiele.

**Hilfen (die drei Stufen vor der Musterlösung):**

- **Stufe 1 (Tipp):** Schreibe für einen kurzen Ausdruck Zeichen für Zeichen auf, was im
  Behälter liegt und was bei jeder schließenden Klammer entnommen wird. Nimm einen Ausdruck
  mit **zwei verschiedenen** Klammerarten — mit nur einer Sorte fällt der Unterschied gar
  nicht auf.
- **Stufe 2 (Ansatz):** Frage dich, welche der offenen Klammern beim Lesen einer schließenden
  Klammer die „zuständige" ist: die zuletzt geöffnete oder die zuerst geöffnete? Vergleiche
  dann, welche der beiden Strukturen genau diese herausgibt. Für die Gegenbeispiele brauchst
  du je einen Ausdruck aus vier Zeichen mit zwei Klammerarten.
- **Stufe 3 (Lösungsweg):** Prüfe `([])` und `([)]` von Hand einmal mit Stapel- und einmal mit
  Schlangenverhalten durch, jeweils in einer Tabelle mit den Spalten „gelesenes Zeichen",
  „Behälterinhalt", „entnommen", „passt?". Du wirst sehen, dass die beiden Strukturen bei
  beiden Ausdrücken zu **entgegengesetzten** Urteilen kommen. Formuliere daraus die
  Stellungnahme.

---

### `a8` — Anforderungsbereich III — Bewertungsaufgabe (offen)

**Aufgabentext:**

> Ein Rettungsroboter soll sich in einem eingestürzten Gebäude selbstständig vom Eingang zu
> einer georteten Person durcharbeiten. Das Gebäude ist als Gitter aus begehbaren und
> blockierten Feldern gespeichert. Der Suchalgorithmus ist der aus Abschnitt 4; offen ist nur,
> ob der Behälter eine Schlange oder ein Stapel sein soll.
>
> Team A schlägt den **Stapel** vor: „Die Tiefensuche merkt sich viel weniger Felder
> gleichzeitig, das spart Arbeitsspeicher auf dem Roboter."
> Team B schlägt die **Schlange** vor: „Wir brauchen den kürzesten Weg."
>
> Bewerte beide Vorschläge für diesen Einsatzzweck und entscheide dich begründet. Beziehe die
> Zahlen aus dem Beispielgitter dieses Moduls in deine Argumentation ein.

**Musterlösung** (`.hilfe-text[data-stufe="9"]`, `<button data-loesung="a8">`):

*Erwartete Argumentation:*

> Beide Vorschläge sind fachlich richtig — sie gewichten nur verschiedene Kosten.
>
> **Zum Einwand von Team A.** Er trifft zu: Die Breitensuche hält stets die gesamte
> „Wellenfront" gleichzeitig im Behälter, die Tiefensuche nur einen Pfad samt offener
> Abzweigungen. Im ungünstigen Fall wächst der Speicherbedarf der Breitensuche deshalb mit der
> Fläche des Suchbereichs, der der Tiefensuche nur mit dessen Tiefe. Für ein Gebäudegitter mit
> einigen tausend Feldern liegen beide Werte jedoch weit unterhalb dessen, was ein
> Robotersteuergerät bereitstellt — der Einwand beschreibt einen realen Unterschied, der in
> dieser Größenordnung aber keine Entscheidung trägt.
>
> **Zum Einwand von Team B.** Er wiegt hier schwerer, weil die Weglänge unmittelbar in die
> Zielgröße eingeht: Akkuladung und verstrichene Zeit sind bei einer Rettung die knappen
> Größen, nicht der Arbeitsspeicher. Die Breitensuche liefert garantiert einen kürzesten Weg,
> die Tiefensuche nur irgendeinen. Im Beispielgitter dieses Moduls braucht die Schlange
> 10 Schritte und der Stapel 14 — ein Umweg von 4 Schritten oder **40 Prozent** auf einem
> Gitter von nur 6 × 6 Feldern. In einem größeren Gebäude kann dieser Anteil deutlich
> ungünstiger ausfallen, denn die Tiefensuche kann einen ganzen Flügel durchlaufen, bevor sie
> zur richtigen Abzweigung zurückkehrt.
>
> **Entscheidung.** Die Schlange, also die Breitensuche. Begründung: Die von Team A
> eingesparte Ressource ist im Überfluss vorhanden, die von Team B gesicherte Eigenschaft
> — kürzester Weg — ist genau die, an der der Einsatz gemessen wird. Team A hätte recht,
> wenn der Speicher tatsächlich knapp wäre oder wenn *irgendein* Weg genügte; beides ist hier
> nicht der Fall.
>
> *Zulässige Alternativentscheidung:* Wer sich für den Stapel entscheidet, muss den knappen
> Speicher belegen oder plausibel machen (etwa bei einem sehr großen Gitter auf einem
> Kleinstrechner) und ausdrücklich in Kauf nehmen, dass der gefundene Weg nicht der kürzeste
> ist. Diese Bewertung ist ebenfalls vollwertig, wenn die Abwägung explizit gemacht wird.

*Bewertungskriterien (fett, mit `·` getrennt):*

> **Bewertungskriterien** · gibt beide Einwände korrekt wieder, statt einen von vornherein
> abzutun · benennt die Garantie der Breitensuche auf einen kürzesten Weg als deren
> entscheidende Eigenschaft · benennt den geringeren gleichzeitigen Speicherbedarf der
> Tiefensuche als deren entscheidende Eigenschaft · verwendet die Zahlen des Beispielgitters
> (10 gegen 14 Schritte, Umweg 4 Schritte beziehungsweise 40 %) belegend, nicht schmückend ·
> stellt den Bezug zum Einsatzzweck her: Akku und Zeit sind knapp, Arbeitsspeicher nicht ·
> trifft eine ausdrückliche Entscheidung und begründet sie mit dieser Abwägung, statt beide
> Möglichkeiten nebeneinander stehen zu lassen · eine Entscheidung für den Stapel wird voll
> gewertet, wenn die Speicherknappheit begründet und der Verzicht auf den kürzesten Weg
> ausdrücklich hingenommen wird.

**Hilfen:**

- **Stufe 1 (Tipp):** Eine Bewertung braucht ein Maß. Frage dich zuerst: Was ist bei einem
  Rettungseinsatz tatsächlich knapp — Arbeitsspeicher, Zeit oder Akkuladung?
- **Stufe 2 (Ansatz):** Arbeite in drei Schritten: (1) Was leistet jede der beiden Suchen
  garantiert, was nicht? (2) Welche Ressource verbraucht jede davon stärker? (3) Welche dieser
  Ressourcen ist im geschilderten Fall die knappe? Erst danach entscheiden. Die Zahlen aus dem
  Beispielgitter in Abschnitt 4 gehören in Schritt 1.
- **Stufe 3 (Lösungsweg):** Halte fest: Breitensuche = kürzester Weg garantiert, Speicher
  wächst mit der Fläche der Wellenfront. Tiefensuche = irgendein Weg, Speicher wächst nur mit
  der Pfadtiefe. Beispielgitter: 10 gegen 14 Schritte, also 4 Schritte oder 40 % Umweg.
  Ordne beides dem Einsatzzweck zu — bei einer Rettung sind Zeit und Akku knapp, Speicher
  nicht — und formuliere daraus eine Entscheidung mit ausdrücklicher Abwägung.

## 6 Abschluss

Abschnitt 7 der Seite, `id="abschluss"`, Überschrift **„Zusammenfassung und Selbstcheck"**.
Der Lehrerteil (Kapitel 7 dieser Datei) steht als `<details class="lehrer">` **innerhalb**
dieser Section, ganz am Ende.

### 6.1 Die vier Kernaussagen

Als `.merksatz`-Blöcke untereinander, jeweils mit fetter Überschrift.

> **1 · Ein Knoten trägt Inhalt und genau eine Referenz.**
> Die gesamte Einheit steht auf einer einzigen Zeile Java: `private Knoten nachfolger;`. Eine
> Klasse, die eine Referenz auf sich selbst führt, kann beliebig lange Ketten bilden, ohne
> dass irgendwo eine Länge festgelegt werden müsste. Der letzte Knoten der Kette zeigt auf
> `null`, und das ist die Abbruchbedingung jeder Schleife über eine solche Struktur.

> **2 · Alle Operationen ändern ausschließlich Referenzen.**
> Kein Inhalt wird verschoben, kopiert oder umsortiert. Ein Element „an den Anfang zu setzen"
> heißt: zwei Zeiger umbiegen. Löschen heißt: den Vorgänger den zu löschenden Knoten
> überspringen lassen. Wer sich beim Programmieren fragt „wohin muss der Inhalt?", stellt die
> falsche Frage; sie lautet „welche Referenz muss sich ändern?".

> **3 · Die Struktur ist die Zugriffsdisziplin, nicht der Speicher.**
> Stapel, Schlange und Liste legen dieselben Daten in derselben Art von Kette ab. Sie
> unterscheiden sich nur darin, welche Zeiger die verwaltende Klasse führt und welche
> Zugriffsstellen sie nach außen freigibt. Eine Struktur zu wählen bedeutet, sich freiwillig
> zu beschränken — und genau diese Beschränkung ist der Gewinn, weil sie das Programm
> lesbarer und beweisbar korrekt macht.

> **4 · Die Wahl des Behälters ist Teil des Algorithmus.**
> Derselbe Suchalgorithmus liefert mit einer Schlange garantiert einen kürzesten Weg und mit
> einem Stapel irgendeinen — im Beispielgitter dieses Moduls einen um 4 Schritte längeren.
> Wer eine Datenstruktur austauscht, ändert nicht die Geschwindigkeit eines Programms,
> sondern die Eigenschaften seines Ergebnisses.

### 6.2 Hinweis zum Zentralabitur (`.hinweis`)

**Grundlage.** Der Kernlehrplan Informatik für den Leistungskurs führt „Daten und ihre
Strukturierung" als eines von fünf verbindlichen Inhaltsfeldern; Programmiersprache im
Unterricht ist Java, Entwicklungsumgebung BlueJ
(`fachliches/kernlehrplan-nrw.md`, Abschnitt „Informatik – Leistungskurs").

**Wortlaut für die Seite:**

> **Im Zentralabitur.** Die Klassen `List`, `Queue` und `Stack` gehören zu den Java-Klassen,
> die in der Prüfung als fertige Implementierung bereitgestellt werden. Du programmierst sie
> dort nicht nach, sondern **benutzt** sie — und musst dafür ihre Wirkung genau kennen,
> insbesondere die drei Randfälle bei `insert`, `remove` und `hasAccess`.
>
> Die Aufgabentypen, die dir dazu am häufigsten begegnen, sind:
> **(1)** eine gegebene Befehlsfolge Schritt für Schritt nachvollziehen und den Zustand der
> Struktur angeben; **(2)** eine Methode implementieren, die eine solche Struktur mit
> `toFirst()` und `next()` vollständig durchläuft und dabei etwas aufsammelt, zählt oder
> prüft; **(3)** begründen, warum für einen geschilderten Anwendungsfall genau eine der drei
> Strukturen passt — das ist die typische Argumentationsaufgabe im Anforderungsbereich III.
>
> Der Durchlauf aus Aufgabentyp (2) hat immer dieselbe Form, und es lohnt sich, sie
> auswendig zu können:

```java
liste.toFirst();
while (liste.hasAccess())
{
    // hier mit liste.getContent() arbeiten
    liste.next();
}
```

> Achte auf die Reihenfolge: `next()` steht am **Ende** des Rumpfes. Ein `next()` am Anfang
> überspringt das erste Element — der mit Abstand häufigste Fehler in Klausuren zu diesem
> Thema.

**Als offen markiert.** Die genaue Formulierung der jährlichen Vorgaben zum Zentralabitur
(welche Klassen im jeweiligen Prüfungsjahr bereitgestellt werden und in welcher Fassung) liegt
mir nicht im Wortlaut vor. Die obige Beschreibung nennt deshalb nur Aufgaben*typen* und
zitiert keine Vorgabe. **Rückfrage an die Fachlehrkraft:** Soll die Seite die
Materialklassen des aktuellen Prüfungsjahrgangs namentlich und mit Versionsstand nennen? Dann
bitte den Wortlaut nachreichen — er wird nicht erfunden.

### 6.3 Selbstcheck — sechs „Ich kann …"-Sätze

Als Liste im `.selbstcheck`-Block, jeder Satz mit Kontrollkästchen (reine Selbsteinschätzung,
kein Speichern — `localStorage` ist ausgeschlossen).

1. Ich kann die Klasse `Knoten` mit ihren beiden Attributen aus dem Kopf aufschreiben und
   erklären, warum ein Knoten eine Referenz auf einen Knoten enthalten darf.
2. Ich kann die Schnittstellen von `Stack`, `Queue` und `List` benennen und zu jeder Methode
   angeben, welche Wirkung sie hat — einschließlich der Randfälle bei leerer Struktur.
3. Ich kann `push`, `enqueue`, `insert` und `remove` als Folge einzelner Referenzänderungen
   beschreiben und dabei angeben, in welcher Reihenfolge sie ausgeführt werden müssen.
4. Ich kann begründen, warum beim Löschen aus einer einfach verketteten Liste der Vorgänger
   umgebogen werden muss und warum die Liste dafür einen eigenen `vorgaenger`-Zeiger mitführt.
5. Ich kann die Laufzeit der wichtigsten Operationen als
   <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> oder
   <span class="m" data-tex="\mathcal{O}(n)" data-plain="O(n)"></span> einordnen und meine
   Einordnung an der Stelle im Quelltext festmachen, an der die Schleife steht.
6. Ich kann für einen geschilderten Anwendungsfall begründet entscheiden, ob Stapel, Schlange,
   Liste oder Array passt, und meine Entscheidung gegen einen Gegenvorschlag verteidigen.

### 6.4 Export

Der Kopieren-Knopf `#bExport` wird unverändert aus dem Referenzmodul übernommen. Die
Namensliste am Skriptende lautet für dieses Modul:

```js
var namen = {
  vw1:"Vorwissen 1 – Referenzsemantik",
  vw2:"Vorwissen 2 – Grenzen des Arrays",
  vw3:"Vorwissen 3 – Bedeutung von null",
  sim1:"Simulation 1 – Lage von A nach fünf Einfügungen",
  sim2:"Simulation 2 – Zähler „besuchte Knoten“",
  a1:"Aufgabe 1 – Stapel-Trace (AB I)",
  a2:"Aufgabe 2 – Referenzänderungen bei insert (AB I)",
  a3:"Aufgabe 3 – Knotenbesuche bei append (AB II)",
  a4:"Aufgabe 4 – Speicher-Mehrbedarf (AB II)",
  a5:"Aufgabe 5 – vergessener Endzeiger (AB II)",
  a6:"Aufgabe 6 – Zuordnung Anwendung zu Struktur (AB II)",
  a7:"Aufgabe 7 – Klammerprüfung: Stapel statt Schlange (AB III)",
  a8:"Aufgabe 8 – Rettungsroboter: Breiten- oder Tiefensuche (AB III)"
};
```

**Hinweis für den Bauagenten:** In den Werten von `namen` stehen typografische
Anführungszeichen (`„…“`). Sie sind in einem mit `"` begrenzten JavaScript-String
unproblematisch. Die offenen Aufgaben `a7` und `a8` liefern keinen prüfbaren Wert; sie
erscheinen im Export mit dem Vermerk „offene Aufgabe – Musterlösung eingesehen: ja/nein",
sofern die Engine des Referenzmoduls das bereits so vorsieht. Tut sie es nicht, werden sie
aus `namen` **nicht** entfernt, sondern die Engine bleibt unverändert und die beiden Einträge
tauchen schlicht nicht auf — die Engine wird für dieses Modul nicht umgebaut.

## 7 Lehrerteil

Steht als `<details class="lehrer">` am Ende der Abschluss-Section und verschwindet beim
Drucken (`@media print` des Referenzmoduls, unverändert übernehmen).

**Summary-Text:** Für die Lehrkraft: Einordnung, Zeitbedarf, typische Fehler, Differenzierung

### 7.1 Einordnung

Das Modul gehört zum Inhaltsfeld **„Daten und ihre Strukturierung"** des Kernlehrplans
Informatik für den Leistungskurs und deckt daraus die linearen Strukturen ab. Es setzt die
objektorientierte Modellierung voraus — Klasse, Objekt, Attribut, Referenz, `null` — und ist
die unmittelbare Voraussetzung für die anschließende Einheit zu **Bäumen**: Ein Binärbaumknoten
unterscheidet sich vom hier gebauten Knoten allein dadurch, dass er zwei Nachfolgerreferenzen
trägt statt einer. Wer `remove` an der verketteten Liste verstanden hat, versteht das Löschen
im Suchbaum als dieselbe Handlung mit einer Fallunterscheidung mehr.

Nach hinten schließt das Modul an die Einheit zu **Sortier- und Suchverfahren** an: Die
Laufzeitbetrachtung in Abschnitt 4 führt die Landau-Notation an einem Gegenstand ein, bei dem
sich <span class="m" data-tex="\mathcal{O}(1)" data-plain="O(1)"></span> und
<span class="m" data-tex="\mathcal{O}(n)" data-plain="O(n)"></span> noch abzählen lassen. Der
Kontrast Breitensuche/Tiefensuche in Abschnitt 4.6 nimmt die Graphenalgorithmen vorweg, ohne
sie zu behandeln — er dient hier ausschließlich der Begründung, dass die Wahl des Behälters
das Ergebnis bestimmt.

**Abgrenzung.** Nicht behandelt werden: doppelt verkettete Listen, generische Typparameter in
der Implementierung (sie werden nur in der Schnittstellentabelle erwähnt), `ArrayList` und das
Java-Collections-Framework, amortisierte Laufzeitanalyse.

### 7.2 Zeitbedarf

Auslegung auf **drei Unterrichtsstunden à 45 Minuten**, insgesamt 135 Minuten reine Arbeitszeit.

| Abschnitt der Seite | Minuten | Sozialform |
|---|---|---|
| 1 Einstieg mit Vorwissensfragen | 10 | Plenum, Fragen einzeln |
| 2 Knoten und Referenzen | 20 | Lehrervortrag mit Tafelskizze, dann Lesen |
| 3 Die drei Strukturen und ihre Schnittstellen | 30 | Lesen in Partnerarbeit, Sicherung im Plenum |
| 4 Vertiefung: Laufzeit, Speicher, Wahl der Struktur | 20 | Plenum; der Details-Block als Hausaufgabe |
| 5 Simulation mit Beobachtungsauftrag | 25 | Partnerarbeit am Gerät, Sicherung im Plenum |
| 6 Übungen a1 bis a6 | 20 | Einzelarbeit |
| 7 Abschluss und Selbstcheck | 10 | Plenum |

Die beiden Aufgaben im Anforderungsbereich III (**a7**, **a8**) sind **nicht** in diesen
135 Minuten enthalten. Sie sind als schriftliche Hausaufgabe mit anschließender Besprechung
gedacht — je etwa 20 Minuten Bearbeitung. Wer sie im Unterricht bearbeiten lässt, plant eine
vierte Stunde ein; die Bewertungskriterien eignen sich dann gut für eine gegenseitige
Korrektur in Partnerarbeit.

**Wenn die Zeit knapp wird**, entfällt zuerst der Details-Block zu `concat` (2B.4), danach
Abschnitt 4.5 (Zugriff auf das k-te Element). Beide sind nicht Voraussetzung für die
Simulation. Der Details-Block zum quadratischen Wachstum (3.3) sollte dagegen nicht entfallen —
er trägt die Argumentation von a3 und a8.

### 7.3 Typische Schülerfehler und wo anzuhalten ist

**1 · Referenz gleich Objekt.** Die Vorstellung, `k2 = k1` erzeuge ein zweites Objekt, hält
sich hartnäckig und macht jede spätere Zeigeroperation unverständlich.
*Anhalten:* direkt nach `vw1`, unabhängig vom Ergebnis. An der Tafel zwei Namensschilder auf
**eine** Kiste legen. Diese Skizze bleibt die ganze Reihe über stehen.

**2 · Das Löschen wird am falschen Knoten angesetzt.** Schülerinnen und Schüler schreiben
`aktuell.setzeNachfolger(null)` und meinen damit „diesen Knoten entfernen". Tatsächlich hängen
sie den gesamten Rest der Liste ab.
*Anhalten:* vor dem Java-Block zu `remove`. Den Fehler bewusst an der Tafel ausführen lassen
und die Kette danach gemeinsam ablesen — die Wirkung ist so drastisch, dass sie sitzt. Danach
in der Simulation `remove()` im Schrittmodus vorführen: Schritt 2 zeigt den umgebogenen
Vorgängerpfeil isoliert, bevor der Knoten überhaupt verschwindet. Das ist der wichtigste
einzelne Moment der Doppelstunde.

**3 · Reihenfolge der Zuweisungen in `push`.** `kopf = neu;` zuerst, dann
`neu.setzeNachfolger(kopf);` — das Ergebnis ist ein Knoten, der auf sich selbst zeigt, und der
Rest des Stapels ist unerreichbar.
*Anhalten:* beim Java-Block zum Stapel. Die falsche Reihenfolge an der Tafel durchspielen und
fragen: „Wo steht jetzt noch die Adresse des alten Kopfes?" Die Antwort „nirgends" ist die
Begründung.

**4 · `aktuell` wird für einen Index gehalten.** Daraus folgen Fragen wie „wie komme ich zum
fünften Element?" mit der Erwartung, es gebe dafür eine Methode.
*Anhalten:* nach der Schnittstellentabelle. Der Hinweiskasten 2B.6 greift das auf; im Gespräch
zählen lassen, wie viele Knoten für das siebte Element besucht werden müssen.

**5 · Der `next()`-Aufruf steht am Anfang der Schleife.** In eigenen Durchlaufmethoden wird
das erste Element übersprungen. Der Fehler kostet in Klausuren regelmäßig Punkte, weil er
nicht zum Absturz führt, sondern nur zu einem stillschweigend falschen Ergebnis.
*Anhalten:* im Abschluss, beim Schleifenmuster in 6.2. Das Muster an die Tafel und stehen
lassen.

**6 · „Die Liste ist schneller als das Array."** Pauschalurteile ohne Bezug zur Operation.
*Anhalten:* bei der Laufzeittabelle in 3.2. Die Gegenfrage lautet immer: „Bei welcher
Operation?" Ohne diese Rückfrage ist keine Antwort in AB III vollständig.

**7 · Zähler verwechselt.** In der Simulation werden „Referenzänderungen" und „besuchte Knoten"
gleichgesetzt. Genau darauf zielt `sim2`.
*Anhalten:* bei der Auswertung des Beobachtungsauftrags. Beide Zähler an der Tafel als Tabelle
für alle drei Strukturen sammeln — das Ergebnis (Liste 10/5, Schlange 0/10, Stapel 0/10) ist
für die meisten überraschend und trägt die ganze Laufzeitdiskussion.

### 7.4 Differenzierung

**Für schnellere Lernende:**

- Den Details-Block zu `concat` (2B.4) lesen und die Frage beantworten, warum das Leeren der
  Quelle nicht bloß Höflichkeit, sondern Notwendigkeit ist.
- `EinfacheListe` um einen Endzeiger erweitern und angeben, **welche** der zwölf Methoden
  dadurch angepasst werden müssen. (Erwartete Antwort: `append`, `insert`, `remove`, `concat`
  und `toLast` — überall dort, wo das Ende der Kette entstehen, wegfallen oder gefunden werden
  kann. Das ist eine anspruchsvolle Aufgabe: Der häufigste Fehler ist, `remove` zu vergessen.)
- Eine Methode `int anzahl()` für die `EinfacheListe` schreiben, ohne `aktuell` und
  `vorgaenger` zu verändern — also mit einem eigenen Hilfszeiger. Die Auflage ist der Kern der
  Aufgabe.
- Aufgabe a7 verschärfen: Reicht ein Stapel auch dann, wenn drei Klammerarten und zusätzlich
  Anführungszeichenpaare geprüft werden sollen? (Bei den Klammern ja; bei Anführungszeichen
  nicht ohne Weiteres, weil öffnendes und schließendes Zeichen identisch sind und sich nicht
  schachteln lassen — eine gute Gelegenheit, die Grenze des Verfahrens zu zeigen.)

**Für Lernende mit Schwierigkeiten:**

- Den Schrittmodus der Simulation zur Pflicht machen und nach **jedem** Klick die Frage stellen
  lassen: „Welcher Pfeil hat sich gerade geändert?" Der schnelle Modus wird erst danach
  freigegeben.
- Die Java-Blöcke mit dem Finger auf dem Bildschirm mitverfolgen lassen, während eine Partnerin
  die Simulation bedient. Ein Leser, eine Bedienerin, dann tauschen.
- Auf a3 und a4 zunächst verzichten und stattdessen a1 und a2 mit anderen Zahlen wiederholen
  lassen; die Rechenaufgaben tragen erst, wenn das Zeigerbild steht.
- Ein Ausdruck auf Papier: sechs leere Knotenkästen und Pfeile, die von Hand eingezeichnet und
  durchgestrichen werden. Für viele ist das körperliche Umbiegen der Pfeile der entscheidende
  Schritt.

### 7.5 Bezug zu Realexperimenten und Unterrichtsmaterial

Ein Realexperiment im physikalischen Sinne gibt es hier nicht. An seine Stelle treten drei
Formen der Handlungserfahrung, die sich im Unterricht bewährt haben:

**1 · Das Menschenmodell.** Sechs Lernende stellen sich als Knoten auf, jeder legt eine Hand
auf die Schulter genau eines anderen — das ist die Nachfolgerreferenz. Eine siebte Person ist
der `kopf`-Zeiger. Nun werden `push`, `pop`, `enqueue` und `dequeue` körperlich ausgeführt.
Beim `remove` aus der Mitte wird sofort erfahrbar, dass die Person selbst gar nichts tun kann:
Ihr Vorgänger muss die Hand umlegen. Zeitbedarf etwa 10 Minuten, am wirksamsten unmittelbar
vor dem Java-Block zu `remove`.

**2 · Karteikarten mit Adressen.** Jede Karte trägt einen Inhalt und in der Ecke eine Nummer;
im Referenzfeld steht die Nummer der nächsten Karte. Die Karten werden anschließend
**gemischt** auf den Tisch gelegt — die Kette bleibt trotzdem lesbar, weil die Reihenfolge in
den Referenzen steht und nicht in der Lage auf dem Tisch. Das räumt die Vorstellung ab,
verkettete Knoten lägen im Speicher hintereinander. Zeitbedarf etwa 5 Minuten, passend zu
Abschnitt 2A.

**3 · BlueJ als Werkzeug am Objekt.** Die vier Klassen (`Knoten`, `EinfacherStapel`,
`EinfacheSchlange`, `EinfacheListe`) lassen sich abtippen und in BlueJ direkt bedienen: Objekte
per Rechtsklick erzeugen, Methoden einzeln aufrufen, den Zustand über den Objektinspektor
ansehen. Der Inspektor zeigt die Nachfolgerreferenz als anklickbaren Verweis — man kann sich
also **durch die Kette hindurchklicken**. Das ist die beste verfügbare Entsprechung zu einem
Messgerät und sollte mindestens einmal vorgeführt werden. Die Klassen sind bewusst
`String`-basiert und ohne Generics geschrieben, damit sie sich ohne Anpassung übersetzen
lassen.

**Materialhinweis.** Die Seite ist ohne Netzverbindung lauffähig; ohne KaTeX werden alle
Formeln über `data-plain` lesbar dargestellt. Für den Einsatz im Computerraum genügt es, die
HTML-Datei lokal zu verteilen. Die Druckansicht enthält die Aufgaben ohne Bedienelemente und
ohne diesen Lehrerteil und eignet sich als Arbeitsblatt.

## 8 Kontrollrechnungen im Klartext

Jeder Zahlenwert, der irgendwo auf der Seite erscheint, steht hier mit seiner Rechnung. Alle
Werte sind zusätzlich maschinell geprüft; die Skripte liegen in
`vorarbeit/info/` (`kontrolle.py`, `java_sim.py`, `irrgarten.py`, `nachpruefung.py`,
`aufgaben.py`). `nachpruefung.py` und `aufgaben.py` enthalten Zusicherungen und brechen ab,
wenn ein Wert nicht stimmt; beide laufen fehlerfrei durch.

---

**R1 — Stapel-Trace (Aufgabe a1).**
Leerer Stapel, Notation von unten nach oben.
`push("A")` → A · `push("B")` → A, B · `pop()` → A · `push("C")` → A, C ·
`push("D")` → A, C, D · `pop()` → A, C · `pop()` → A · `push("E")` → A, E.
Fünf `push`, drei `pop`, kein `pop` auf leerem Stapel, also 5 − 3 = **2 Elemente**.
`top()` liefert **"E"**, darunter liegt "A".
Gegenprobe: Das zuerst eingefügte "A" ist nie entfernt worden — genau das erwartet man bei
LIFO, wenn nie bis zum Grund abgeräumt wird.

**R2 — Referenzänderungen bei `insert` (Aufgabe a2).**
Ausgangsliste A, B, C. Nach `toFirst()`: `aktuell` = A, `vorgaenger` = null.
Nach `next()`: `aktuell` = B, `vorgaenger` = A.
`insert("X")` führt drei Referenzzuweisungen aus:
(1) `neu.setzeNachfolger(aktuell)` — X → B;
(2) `vorgaenger.setzeNachfolger(neu)` — A → X (der Else-Zweig, da `vorgaenger` ≠ null);
(3) `vorgaenger = neu` — X wird Vorgänger.
Also **3 Referenzänderungen**, **0 Knotenbesuche**.
Endzustand: Kette **A, X, B, C**; aktuelles Objekt weiterhin **B**; Vorgänger **X**.
Gegenprobe: Die Kettenlänge steigt um genau 1, und das aktuelle Objekt hat sich nicht
geändert — beides ist die in der Schnittstellentabelle festgelegte Wirkung von `insert`.

**R3 — Knotenbesuche bei dreimaligem `append` (Aufgabe a3).**
Kostenmodell: `append` an eine Liste mit n Knoten kostet n Besuche — einer für
`lauf = anfang`, weitere (n − 1) im Schleifenrumpf. Für n = 1 ergibt das 1 Besuch (die
Schleifenbedingung ist sofort falsch), für n = 0 ergibt es 0 Besuche (der Sonderfallzweig
greift, die Schleife wird nie betreten).
1. Aufruf: n = 1200 → 1200 Besuche.
2. Aufruf: n = 1201 → 1201 Besuche.
3. Aufruf: n = 1202 → 1202 Besuche.
Summe: 1200 + 1201 + 1202 = **3603 Knotenbesuche**.
Gegenprobe über den mittleren Wert: 3 · 1201 = 3603. ✔
Zweite Gegenprobe: In `aufgaben.py` wird die Schleife tatsächlich durchlaufen und mitgezählt;
das Ergebnis stimmt mit der geschlossenen Formel überein.

**R4 — Speicher-Modellrechnung (Aufgabe a4 und Abschnitt 3.4).**
n = 1200, eine Referenz = 4 B, 1 kB = 1000 B. Objektköpfe und Ausrichtung bleiben
unberücksichtigt — das ist ausdrücklich ein Modell.
Verkettete Liste: 1200 · (4 B + 4 B) = 1200 · 8 B = **9600 B = 9,6 kB**.
Array: 1200 · 4 B = **4800 B = 4,8 kB**.
Mehrbedarf: 9600 B − 4800 B = **4800 B = 4,8 kB**; Verhältnis 9600 / 4800 = **2,0**.
Gegenprobe: Der Mehrbedarf ist genau eine Referenz je Element, also 1200 · 4 B = 4800 B. ✔

**R5 — Aufbau einer Liste mit n `append` aus dem Leeren (Abschnitt 3.3).**
Beim i-ten Aufruf ist die Liste (i − 1) Knoten lang, kostet also (i − 1) Besuche.
Gesamt: 0 + 1 + 2 + … + (n − 1) = n(n − 1)/2.
Für n = 1200: 1200 · 1199 / 2 = 1 438 800 / 2 = **719 400 Knotenbesuche**.
Gegenproben aus `nachpruefung.py`, jeweils durch Abzählen im Programm bestätigt:
n = 5 → 10 (Formel 5 · 4 / 2 = 10) ✔ · n = 10 → 45 (10 · 9 / 2 = 45) ✔ ·
n = 1200 → 719 400 ✔

**R6 — Canvas-Geometrie (Abschnitt 4.6).**
Kastenbreite = Inhaltsfeld 70 px + Referenzfeld 35 px = **105 px**. ✔
Raster = Kastenbreite 105 px + Lücke 40 px = **145 px**.
Position des i-ten Knotens: x_i = 55 + i · 145.
x₀ = 55 · x₁ = 200 · x₂ = 345 · x₃ = 490 · x₄ = 635 · x₅ = **780**.
Rechte Kante des sechsten Knotens: 780 + 105 = **885 px** bei 1000 px Canvasbreite. Es bleiben
115 px für das `null`-Zeichen — passt. Damit ist `MAX_KNOTEN = 6` begründet.
Pfeil: Start bei x + 87 (Mitte des Referenzfeldes: 70 + 35/2 = 87,5, abgerundet auf 87),
Ende beim nächsten Kastenanfang x + 145. Pfeillänge = 145 − 87 = **58 px**. ✔

**R7 — Zähler je Operation (Abschnitt 4.5).**
Abgezählt an den Java-Blöcken aus Abschnitt 3, Zeile für Zeile; gezählt wird jede Zuweisung,
deren linke Seite ein Referenzfeld oder ein Zeiger der verwaltenden Klasse ist. `new` zählt
nicht.

| Operation | Referenzänderungen | Knotenbesuche |
|---|---|---|
| `push(x)` | 2 | 0 |
| `pop()` (nicht leer) | 1 | 0 |
| `top()` / `front()` / `getContent()` | 0 | 0 |
| `setContent(x)` | 0 | 0 |
| `enqueue(x)`, beide Fälle | 2 | 0 |
| `dequeue()`, Rest bleibt | 1 | 0 |
| `dequeue()`, wird dabei leer | 2 | 0 |
| `toFirst()` | 2 | 0 |
| `next()` | 2 | 0 |
| `append(x)` bei n Knoten | 1 | n |
| `insert(x)` mit aktuellem Objekt | 3 | 0 |
| `remove()` | 2 | 0 |

**R8 — Werte des Beobachtungsauftrags (Abschnitt 4.2, Fragen `sim1` und `sim2`).**
Jeweils aus dem leeren Zustand, fünfmal A, B, C, D, E eingefügt, Zähler vorher zurückgesetzt.

| Struktur | Operation | Kette danach | Referenzänderungen | besuchte Knoten |
|---|---|---|---|---|
| Stapel | `push` | E, D, C, B, A | 5 · 2 = **10** | **0** |
| Schlange | `enqueue` | A, B, C, D, E | 5 · 2 = **10** | **0** |
| Liste | `append` | A, B, C, D, E | 5 · 1 = **5** | **10** |

Die 10 Knotenbesuche der Liste: Die Listenlängen vor den fünf Aufrufen sind 0, 1, 2, 3, 4;
Summe 0 + 1 + 2 + 3 + 4 = **10**. ✔ (Das ist R5 mit n = 5.)
Der Kettenaufbau des Stapels ist gegenläufig, weil `push` jeden Knoten vor den bisherigen
Kopf schiebt; nach dem fünften `push` zeigt `kopf` auf E. Das ist die Grundlage von `sim1`.

**R9 — Mittlerer Aufwand für den Zugriff auf das k-te Element (Abschnitt 3.5).**
Kosten für Index k: k + 1 Besuche (einer für `toFirst()`, k für die `next()`-Aufrufe).
Für k = 0 also 1 Besuch, für k = 1199 also 1200 Besuche.
Mittelwert über alle 1200 gleichwahrscheinlichen Indizes:
(1 + 1200) / 2 = 1201 / 2 = **600,5 Knotenbesuche**.
Gegenprobe in `nachpruefung.py`: arithmetisches Mittel der 1200 Einzelwerte = 600,5. ✔

**R10 — Klammerprüfung, Gegenbeispiele (Aufgabe a7).**
Geprüft mit zwei unabhängigen Implementierungen — Entnahme oben (Stapel) beziehungsweise
vorn (Schlange).

| Ausdruck | mit Stapel | mit Schlange | korrekt geschachtelt? |
|---|---|---|---|
| `([])` | akzeptiert | **abgelehnt** | ja |
| `([)]` | abgelehnt | **akzeptiert** | nein |
| `(()` | abgelehnt | abgelehnt | nein |
| `a*(b+[c-d])` | akzeptiert | abgelehnt | ja |
| `(]` | abgelehnt | abgelehnt | nein |

Die Schlange irrt damit **in beide Richtungen**: Sie lehnt `([])` fälschlich ab und akzeptiert
`([)]` fälschlich. Der Stapel entscheidet alle fünf Fälle korrekt. Das sind genau die beiden
in der Musterlösung zu a7 verlangten Gegenbeispiele.

**R11 — Irrgarten, Breiten- gegen Tiefensuche (Abschnitt 3.6 und Aufgabe a8).**
Gitter 6 × 6, Start (0,0), Ziel (5,5), Nachbarreihenfolge rechts, unten, links, oben.
Belegte Felder: (1,1), (1,2), (1,3), (1,4), (2,1), (3,1), (3,3), (3,4), (4,3), (5,1).

- Schlange (FIFO, Breitensuche): Weg mit **10 Schritten**, 25 Felder entnommen.
- Stapel (LIFO, Tiefensuche): Weg mit **14 Schritten**, 24 Felder entnommen.
- Umweg des Stapels: 14 − 10 = **4 Schritte**, relativ 4 / 10 = **40 %**.

Gegenprobe: Eine unabhängige Berechnung der Abstände vom Start (reine Distanzwelle, ohne
Wegverfolgung) liefert für das Zielfeld ebenfalls 10 — die von der Schlange gefundene Länge ist
also tatsächlich die kürzestmögliche. ✔

---

**Was hier bewusst nicht gerechnet wird.** Der tatsächliche Speicherbedarf eines Java-Objekts
(Objektkopf, Ausrichtung auf 8-Byte-Grenzen) wird nirgends behauptet; Abschnitt 3.4 nennt das
ausdrücklich als Grenze des Modells. Ebenso wird keine Laufzeit in Sekunden angegeben —
gemessen wird durchgehend in Knotenbesuchen.

## 9 Checkliste der Bausteine

Diese Liste ist das Inhaltsverzeichnis für den Bauagenten. Sie führt jeden Baustein auf, der in
den Abschnitten 1 bis 7 beschrieben ist — mit seinem Schlüssel, seiner Bauform und den Werten,
die im HTML stehen müssen. Sie fügt nichts hinzu: Findet sich hier ein Schlüssel, steht der
zugehörige Wortlaut weiter oben; steht oben etwas, taucht es hier auf.

**Gesamtzahl der prüfbaren Bausteine:** 6 Multiple Choice + 4 Zahleneingaben + 1 Zuordnung
+ 2 offene Aufgaben = **13 Bausteine**, dazu 1 Canvas, 18 Hilfe-Knöpfe und 2 Lösungs-Knöpfe
(siehe 9.5) sowie die drei Bedienleisten der Simulation.

---

### 9.1 Multiple-Choice-Aufgaben (`data-mc`)

Bauform je Aufgabe nach `vorlage/bausteine.md`, Abschnitt 4: `<div class="aufgabe" data-mc="…">`,
darin `<label class="opt" data-i="0|1|2">` mit `<input type="radio" name="…">`. **Der `name`
des Radios ist identisch mit dem Wert von `data-mc`.** Jede Option trägt ihren eigenen
Rückmeldetext; ein bloßes „falsch" kommt nirgends vor.

| Schlüssel | Ort auf der Seite | Optionen | richtig (`r`) | Kurzinhalt |
|---|---|---|---|---|
| `vw1` | Abschnitt 1, Einstieg | 3 | **1** | Referenzsemantik: `k2 = k1` kopiert kein Objekt |
| `vw2` | Abschnitt 1, Einstieg | 3 | **2** | Array ist in der Länge fest, es muss umkopiert werden |
| `vw3` | Abschnitt 1, Einstieg | 3 | **0** | `null` + Methodenaufruf ⇒ `NullPointerException` zur Laufzeit |
| `sim1` | Abschnitt 5, unter der Simulation | 3 | **1** | Wohin `kopf`/`anfang` nach fünf Einfügungen zeigt |
| `sim2` | Abschnitt 5, unter der Simulation | 3 | **0** | Zähler „besuchte Knoten": Liste 10, Schlange 0, Stapel 0 |
| `a5` | Abschnitt 6, Übungen (AB II) | 3 | **1** | Folge der vergessenen Zeile `if (kopf == null) { ende = null; }` |

Alle sechs Aufgaben haben genau drei Optionen in fester, oben festgelegter Reihenfolge. Die
Reihenfolge wird **nicht** gemischt — die Rückmeldetexte beziehen sich aufeinander
(„genau umgekehrt", „du hast die beiden Zähler vertauscht").

---

### 9.2 Zahleneingaben (`data-num`)

Bauform nach `vorlage/bausteine.md`, Abschnitt 5: `<div class="aufgabe" data-num="…">` mit
Zahlenfeld und `<select>` für die Einheit. Jeder Eintrag in `numDaten` hat die vier
Rückmeldetexte `ok`, `falschEinheit`, `nah`, `weit`; die Einheitenliste enthält je mindestens
einen fachlich falschen Distraktor.

| Schlüssel | Sollwert | Einheit | Toleranz | Alternativeinheit | Einheitenliste im `<select>` | falscher Distraktor |
|---|---|---|---|---|---|---|
| `a1` | **2** | Elemente | 0,5 | — | Elemente · Knotenbesuche · Referenzänderungen · Byte | `Byte` |
| `a2` | **3** | Referenzänderungen | 0,5 | — | Referenzänderungen · Knotenbesuche · Knoten · Byte | `Byte` |
| `a3` | **3603** | Knotenbesuche | 0,5 | — | Knotenbesuche · Referenzänderungen · Byte · kB | `Byte`, `kB` |
| `a4` | **4800** | B | 1 | `{wert: 4.8, einheit: "kB"}` | B · kB · MB · Knoten | `Knoten` |

Nachgerechnet in Abschnitt 8 (R1 bis R4) und maschinell in `vorarbeit/info/aufgaben.py`
bestätigt. `a4` ist die einzige Aufgabe mit Alternativeinheit; ihr Zahlenwert wird in der
Rückmeldung als `4,8 kB` mit Komma ausgegeben.

---

### 9.3 Zuordnungsaufgabe (`data-check="zuordnung"`)

Genau **eine** im Modul — mehr sieht die Engine nicht vor. Bauform nach
`vorlage/bausteine.md`, Abschnitt 6: `<div class="zuordnung">` mit vier Zeilen, jede Zeile ein
`<select>` über A bis D, darunter `<button class="primaer" data-check="zuordnung">Prüfen</button>`.

| Zeile | Kurzfassung des Zeilentextes | `data-loesung` |
|---|---|---|
| 1 | Rückgängig-Funktion eines Editors | **A** (Stapel) |
| 2 | Bild als Raster, wahlfreier Zugriff, feste Größe | **D** (Array) |
| 3 | Kursliste, laufendes Einfügen und Löschen an wandernder Stelle | **C** (Liste) |
| 4 | Druckaufträge in Eingangsreihenfolge | **B** (Schlange) |

Lösungsbuchstaben in Zeilenreihenfolge: **A – D – C – B**. Die Skizzen A bis D stehen als
vier Inline-SVG von je rund 200 × 110 px in einem `.diagramme`-Block über der Aufgabe;
ihr Inhalt ist in Abschnitt 5, `a6`, festgelegt. Zwei Rückmeldetexte sind vorbereitet:
einer für Teilerfolg (nennt die Denkstrategie, nicht die Lösung) und einer für die
vollständige Lösung.

---

### 9.4 Offene Aufgaben mit Musterlösung (`data-stufe="9"`)

Bauform: `<div class="aufgabe">` ohne `data-mc`/`data-num`, Musterlösung als
`.hilfe-text[data-stufe="9"]`, umgeschaltet über `<button data-loesung="…">`.

| Schlüssel | AB | Aufgabentyp | Inhalt der Musterlösung |
|---|---|---|---|
| `a7` | III | Begründungsaufgabe | Klammerprüfung: Stapel statt Schlange, mit den beiden geforderten Gegenbeispielen `([])` (fälschlich abgelehnt) und `([)]` (fälschlich angenommen) |
| `a8` | III | Bewertungsaufgabe | Rettungsroboter: Breiten- oder Tiefensuche, Bewertung beider Teamvorschläge mit den Zahlen des Beispielgitters (10 gegen 14 Schritte) |

Beide Musterlösungen bestehen aus zwei Teilen, die im HTML sichtbar getrennt bleiben:
*erwartete Argumentation* und *Bewertungskriterien* (fett, mit `·` getrennt). Keine der
beiden Aufgaben verlangt eine längere Rechnung.

---

### 9.5 Hilfeblöcke (dreistufig, `data-stufe="1|2|3"`)

| Schlüssel | Stufe 1 Tipp | Stufe 2 Ansatz | Stufe 3 Lösungsweg |
|---|---|---|---|
| `a1` | ja | ja | ja |
| `a2` | ja | ja | ja |
| `a3` | ja | ja | ja |
| `a4` | ja | ja | ja |
| `a5` | — | — | — |
| `a6` | — | — | — |
| `a7` | ja | ja | ja (+ Stufe 9) |
| `a8` | ja | ja | ja (+ Stufe 9) |

Sechs Aufgaben mit Hilfeblock, also **18 Hilfe-Knöpfe** plus **2 Lösungs-Knöpfe**
(`data-loesung="a7"`, `data-loesung="a8"`). `a5` und `a6` tragen keinen Hilfeblock: Dort
übernimmt das Rückmeldesystem der Engine diese Rolle — bei `a5` das Feedback je Option, bei
`a6` die Rückmeldung bei Teilerfolg. Siehe dazu die Auffälligkeiten am Ende.

---

### 9.6 Namensliste für die Exportfunktion

Der Kopieren-Knopf `#bExport` und die Exportfunktion werden unverändert aus dem Referenzmodul
übernommen. Nur die Zuordnung Schlüssel → Klartextname ist modulspezifisch:

| Schlüssel | Klartextname im Export |
|---|---|
| `vw1` | Vorwissen 1 – Referenzsemantik |
| `vw2` | Vorwissen 2 – Grenzen des Arrays |
| `vw3` | Vorwissen 3 – Bedeutung von null |
| `sim1` | Simulation 1 – Lage von A nach fünf Einfügungen |
| `sim2` | Simulation 2 – Zähler „besuchte Knoten“ |
| `a1` | Aufgabe 1 – Stapel-Trace (AB I) |
| `a2` | Aufgabe 2 – Referenzänderungen bei insert (AB I) |
| `a3` | Aufgabe 3 – Knotenbesuche bei append (AB II) |
| `a4` | Aufgabe 4 – Speicher-Mehrbedarf (AB II) |
| `a5` | Aufgabe 5 – vergessener Endzeiger (AB II) |
| `a6` | Aufgabe 6 – Zuordnung Anwendung zu Struktur (AB II) |
| `a7` | Aufgabe 7 – Klammerprüfung: Stapel statt Schlange (AB III) |
| `a8` | Aufgabe 8 – Rettungsroboter: Breiten- oder Tiefensuche (AB III) |

Der fertige `namen`-Block steht wörtlich in Abschnitt 6.4 und wird von dort übernommen.
Dreizehn Einträge, kein Schlüssel doppelt.

---

### 9.7 Canvas, Regler und Bedienelemente der Simulation

**Canvas: genau eines.**

| `id` | `width` | `height` | CSS | Zweck |
|---|---|---|---|---|
| `cvSim` | 1000 | 340 | `width:100%` | Knotenkette, die vier bzw. fünf Zeiger, freier neuer Knoten, entfernter Knoten |

Feste interne Maße, Skalierung ausschließlich über CSS. Geometrie und Farben sind in
Abschnitt 4.6 verbindlich festgelegt und in Abschnitt 8, Rechnung R6, nachgerechnet
(sechster Knoten bei <span class="m" data-tex="x_5 = 780" data-plain="x₅ = 780"></span> px,
rechte Kante 885 px, 115 px Rest für das `null`-Zeichen). Es gibt **kein zweites Canvas** —
die vier Skizzen der Zuordnungsaufgabe und alle übrigen Abbildungen sind Inline-SVG oder
`<pre>`-Blöcke.

**Regler: keine Schieberegler.** Der `.regler`-Bereich enthält stattdessen zwei
Eingabeelemente:

| `id` | Element | Vorgaben | Wirkung |
|---|---|---|---|
| `eInhalt` | `<input type="text">` | `maxlength="3"`, Breite ca. 90 px, Startwert `A` | Inhalt des nächsten einzufügenden Knotens; rückt nach erfolgreichem Einfügen automatisch vor (`A → B → … → Z → A`) |
| `cSchritt` | `<input type="checkbox">` | standardmäßig **angehakt**, Beschriftung „Schritt für Schritt" | schaltet zwischen Einzelschritt und Sofortausführung |

**Drei `.knopfleiste`-Blöcke:**

1. **Strukturwahl** — 3 Schaltflächen: `Stapel` · `Schlange` · `Liste`. Die aktive trägt
   `primaer`; ein Wechsel setzt Modell und beide Zähler zurück.
2. **Operationen** — Beschriftung und Sichtbarkeit hängen von der gewählten Struktur ab:
   Stapel 3 Schaltflächen (`push(x)` · `pop()` · `top()`), Schlange 3 (`enqueue(x)` ·
   `dequeue()` · `front()`), Liste 7 (`toFirst()` · `next()` · `append(x)` · `insert(x)` ·
   `remove()` · `setContent(x)` · `getContent()`). Insgesamt **13** Operationsknöpfe im Markup.
3. **Ablauf** — 2 Schaltflächen: `Nächster Schritt` (nur im Schrittmodus aktiv) · `Zurücksetzen`.

**Anzeigen:** ein `.anzeige`-Block mit fünf Feldern (Struktur · Knoten in der Kette ·
Referenzänderungen · besuchte Knoten · letzter Rückgabewert), darunter das Protokollfeld
`id="pProtokoll"` mit dreizeiligem Aufbau (Java-Zeile in `<code>`, Klartext, Schrittzähler).

**Weitere `id`s im Modul:** `bExport` (Kopieren-Knopf, aus dem Referenzmodul). Darüber hinaus
vergibt dieses Modul keine eigenen `id`s; alles andere läuft über Klassen und Datenattribute.

---

### Auffälligkeiten

Beim Durchgehen sind vier Punkte aufgefallen. Keiner davon ist stillschweigend geändert
worden — sie stehen hier, damit der Bauagent sie bewusst entscheidet.

1. **`a6` steht in der Namensliste, hat aber keinen `data-mc`/`data-num`-Schlüssel.** Die
   Zuordnungsaufgabe läuft über `[data-check="zuordnung"]`. Sammelt die Exportfunktion des
   Referenzmoduls nur `[data-mc]` und `[data-num]` ein, taucht `a6` im Export nicht auf,
   obwohl ein Klartextname hinterlegt ist. Das ist derselbe Fall, den Abschnitt 6.4 für `a7`
   und `a8` bereits ausdrücklich regelt: Die Engine wird **nicht** umgebaut, der Eintrag
   bleibt in `namen` stehen und läuft gegebenenfalls ins Leere. Der Bauagent prüft beim
   Übernehmen der Engine, ob das zutrifft, und ändert nichts daran.

2. **`a5` und `a6` haben keinen dreistufigen Hilfeblock**, während `a1` bis `a4`, `a7` und
   `a8` einen tragen. Das ist so beabsichtigt — bei einer Multiple-Choice- und einer
   Zuordnungsaufgabe würde eine Hilfestufe die Lösung vorwegnehmen, und beide haben
   stattdessen inhaltliches Feedback je Option beziehungsweise bei Teilerfolg. Der
   Vollständigkeitsprüfer sollte die beiden Aufgaben deshalb nicht als „Hilfe fehlt" melden.

3. **Der `.regler`-Bereich enthält keinen Schieberegler.** Der Baustein heißt in
   `vorlage/bausteine.md` so, weil im Referenzmodul dort Schieberegler stehen. Für diese
   Simulation gibt es keine stetig veränderliche Größe — geregelt werden ein Zeicheninhalt und
   ein Schaltzustand. Klassenname und Rahmenbau bleiben unverändert, nur der Inhalt ist ein
   Textfeld und ein Kontrollkästchen.

4. **Die `fmt`-Funktion mit Kommaausgabe wird in der Simulation nicht aufgerufen.** Alle fünf
   Anzeigefelder führen abzählbare Größen ohne Nachkommastellen. Die Kommaregel gilt
   unverändert für alle übrigen Zahlen der Seite — insbesondere für `4,8 kB` in der Rückmeldung
   zu `a4`. Die Funktion selbst wird trotzdem unverändert aus dem Referenzmodul übernommen und
   nicht entfernt.
