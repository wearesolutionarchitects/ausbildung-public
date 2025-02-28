# Abschlussprüfung Herbst 2024

Termin: Mittwoch, 28. Februar 2024

**Einrichten eines IT-gestützten Arbeitsplatzes.**

**Teil 1 der Abschlussprüfung:**

- 4 Aufgaben
- 90 Minuten Prüfungszeit
- 100 Punkte

---

## Inhaltsverzeichnis – Katalogthemen und Zuordnung zu den Aufgaben

1. **06-04 IT-Sicherheitsmaßnahmen (BSI IT-Grundschutz, Netzwerksegmentierung, Technische / organisatorische Maßnahmen)**
   - **Aufgaben**: 1a (Zutrittskontrolle), 1b (Sicherheitsrisiken), 1c (sicher konfigurierte Präsentationsrechner), 1d (IP-Netztrennung und MAC-Adresse)

2. **01-02 Machbarkeit und Wirtschaftlichkeit von Projekten**  
   - **Aufgaben**: 2a (Fremdvergabe vs. Eigenentwicklung – Argumente), 2f (Kostenberechnung Schließzylinder & Transponder über 5 Jahre)

3. **04-06 Programmiersprachen / Softwareentwicklung**  
   - **Aufgaben**: 2b (Kriterium Programmiersprache), 2c (Compiler vs. Interpreter), 2e (OOP-Funktion checkAuthority und Array-Prüfung)

4. **04-07 Programmierwerkzeuge (UML)**  
   - **Aufgaben**: 2d (UML-Anwendungsfalldiagramm)

5. **03-04 Wirtschaftlichkeit von IT-Systemen (Finanzierung / Leasing, Kostenvergleiche)**  
   - **Aufgaben**: 3a (Ratendarlehen für PCs), 4c und 4d (Vorteile Leasing, Nutzung nach Ablauf)

6. **03-01 Marktgängige IT-Systeme (Hardware, RAM, SSD)**
   - **Aufgaben**: 3b (RAM-Kompatibilität / Empfehlung, SSD-Vorteile)

7. **06-04 IT-Sicherheitsmaßnahmen (Phishing-Schutz)**  
   - **Aufgaben**: 3c (Phishing: Gefahren, Anzeichen, Schutz)

8. **04-01 IT-Systeme konzipieren (Lasten- und Pflichtenheft)**
   - **Aufgaben**: 4a (Zweck und Inhalte Lasten-/Pflichtenheft)

9. **04-08 Grundlagen von relationalen Datenbanken** (bei Datenmodellierung)
   - **Aufgaben**: 4b (ER-Modell ergänzen, redundanzfrei mit Kardinalitäten)

10. **03-01 Marktgängige IT-Systeme (ökologische Aspekte)**
    - **Aufgaben**: 4e (zwei ökologische Aspekte bei Neuinvestition)

## Die Aufgaben 1 bis 4 beziehen sich auf folgende Ausgangssituation

| | |
| :--- |
| **Situation**:  Sie sind Auszubildender der Identify OHG, die sich auf die Herstellung von elektronischen Schlüsselsystemen und Ausweisen unter Beachtung höchster Sicherheitsanforderungen spezialisiert hat. |

---

## 1. Aufgabe (26 Punkte)

Zur Vorbereitung der Absicherung eines Besprechungsraums informieren Sie sich u. a. über Maßnahmen aus dem BSI IT-Grund-schutz-Kompendium und wirken an der Umsetzung mit.

---

### a. Zugangs- und Zugriffskontrolle (3 Punkte)

Zur Absicherung des Besprechungsraums soll u. a. eine automatische Zutrittskontrolle an der Eingangstür eingerichtet werden.
Nennen Sie **drei** technische Möglichkeiten, um eine automatische Zutrittskontrolle zu gewährleisten.

1. ...
2. ...
3. ...

---

### b. Sicherheitsrisiken (3 Punkte)

Beschreiben Sie die Sicherheitsrisiken der folgenden Situationen:

| Situation | Sicherheitsrisiko |
| :--- | :--- |
| Geöffnete Fenster und Türen nach Verlassen des Besprechungsraums | **Beispiel:** Informationen in Papierform oder IT-Geräte können durch Diebstahl in falsche Hände geraten. |
| Nutzung durch externe Personen | |
| Lose verlegte Kabel | |
| Nutzung von BYOD-Geräten (Bring Your Own Device) | |

---

### c. Maßnahmen zur Absicherung (6 Punkte)

Ein PC soll für die Durchführung von Präsentationen mit einem Anzeigegerät verbunden werden. Der BSI-Grundschutz empfiehlt, den Präsentationsrechner in dem Besprechungsraum sicher zu konfigurieren.
Begründen Sie die folgenden vorgeschlagenen Maßnahmen.

Nutzung einer Minimalkonfiguration mit festgelegter Anwendungssoftware:

**Begründung:** ...

Anschluss an ein vom LAN der Institution getrenntes Datennetz:

**Begründung:** ...

---

### d. (3 Punkte)

Sie erhalten vom Netzwerkadministrator der Identify OHG die folgenden Vorgaben für die Netzwerkkonfiguration des Präsenta-
tionsrechners. Die Adressvergabe soll statisch erfolgen, um eine spätere Fernwartung zu vereinfachen.

Netzwerk: 192.168.20.0/24
DHCP-Range: 192.168.20.20 - 192.168.20.254
Router: 192.168.20.1

---

#### da (2 Punkte)

Bei der Analyse des PCs wird Ihnen jedoch die IP-Adresse 169.254.122.115 angezeigt.

Begründen Sie diese „Vorkonfiguration":

**Begründung:** ...

---

#### db (2 Punkte)

Markieren Sie bzw. passen Sie die Konfiguration entsprechend der Vorgaben des Administrators in der folgenden Eingabemaske an.

**Eingabemaske:**

---

#### dc (5 Punkte)

Entsprechend der BSI-Empfehlungen ist das IP-Netz des Präsentationsrechners vom Firmennetz getrennt. Im Besprechungsraum befindet sich eine unbeschriftete Netzwerk-Doppeldose. Hier wird auf der einen Seite das Firmennetz, auf der anderen Seite das Netz für den Präsentationsrechner zur Verfügung gestellt. Ihre Aufgabe besteht nun darin, die richtige RJ-45-Buchse (links oder rechts) der Netzwerkdose zu ermitteln und zu beschriften. Ihnen steht dazu ein Patchkabel und der Präsentationsrechner mit seiner Kommandozeile zur Verfügung. Beschreiben Sie Ihre Vorgehensweise stichpunktartig.

1. ...
2. ...
3. ...
4. ...

---

#### dd 05 Aktivitäten bei Installationen und Konfigurationen kennen und beurteilen (4 Punkte)

Für die Einrichtung weiterer Maßnahmen der IT-Sicherheit im Netzwerk benötigt Ihr Administrator die MAC-Adresse des Präsentationsrechners.

Geben Sie einen möglichen Konsolenbefehl an, um die Adresse zu ermitteln und nennen Sie ein Beispiel für eine MAC-Adresse in strukturierter hexadezimaler Darstellung.

**Konsolenbefehl:** ...

**MAC-Adresse:** ...

---

## 2. Aufgabe (25 Punkte)

Die Identify OHG benötigt eine neue Software für ihre Schließsysteme. Sie arbeiten in der Abteilung Softwareentwicklung bei der
Planung der neuen Software mit. Dabei erstellen Sie auch eine Kostenübersicht für einen Kunden.

### a. Fremdvergabe (2 Punkte)

In der Softwareentwicklungsabteilung des Unternehmens gibt es derzeit einen personellen Engpass. Die Identify OHG denkt über eine Fremdvergabe nach.

Nennen Sie zwei Argumente, die gegen eine Fremdvergabe sprechen.

1. ...
2. ...

---

### b. Progammiersprache (3 Punkte)

Es wird beschlossen, die Software selbst zu entwickeln. Die Entwicklungsabteilung fragt, in welcher Programmiersprache die
Software entwickelt werden soll.

Nennen Sie ein allgemeingültiges Kriterium, welches für die Auswahl der Programmiersprache von Bedeutung ist und geben Sie
dazu eine kurze Begründung an.

**Kriterium:** ...

**Begründung:** ...

---

### c. Compiler und Interpreter (3 Punkte)

Zur Auswahl der Programmiersprachen stehen Compiler- und Interpreter-Sprachen.

Erläutern Sie den wesentlichen Unterschied zwischen den beiden Übersetzungsarten.

**Compiler:** ...

**Interpreter:** ...

### d. UML-Anwendungsfall-Diagramm (5 Punkte)

Sie werden beauftragt, für die Schlüsselsystemsoftware ein UML-Anwendungsfaldiagramm (Use-Case) zu erstellen. Die folgenden Anforderungen liegen vor:

- Der Mitarbeiter kann Türen öffnen und Türen zuschließen. Dabei findet immer eine Berechtigungsprüfung statt.
- Der Administrator kann alles, was ein Mitarbeiter kann. Zusätzlich kann er die Türschlösser programmieren. Dabei findet
immer eine Berechtigungsprüfung statt.

Ergänzen Sie das gegebene UML-Anwendungsfalldiagramm.

---

### e. Array in Pseudocode (6 Punkte)

Ihr Kollege hat gerade die Methode bool checkAuthority (int id, int roomNr) erstelt. Diese übergibt eine Mitarbeiter-ID und eine Raumnummer, um abzufragen, ob für diesen Raum eine Zutritsberechtigung besteht. Ermitteln und begründen Sie den Rückgabewert, der bei Aufruf der Funktion mit id = 3 und romNr = 236 geliefert wird.

Hinweis:
Die Funktion greift auf ein globales zweidimensionales Array keyData [][] zu. In der ersten Spalte steht die Mitarbeiter-ID. Die
folgenden Spalten enthalten die Räume, für die eine Zutrittsberechtigung besteht. Der Zeilen- und Spaltenindex beginnt bei O.
Es gibt **keine Kopfzeile** im Array, sie dient nur zur Erläuterung.

| | Mitarbeiter-ID | Room1 | Room 2 | Room 3 | Room 4 | Room 5 | Room 6 | Roomxx |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 223 | 312 | 154 | 47 | 124 | 236 | 241 | 242 |

---

## 4. Aufgabe (26 Punkte)

### a. Lasten- und Pflichtenheft (6 Punkte)

Ale Vorgänge des Produktionsprozesses müssen dokumentiert werden. Als Grundlage wird ein Datenmodell erstellt.

Bei La Mediterranea ist auch bei **internen Aufträgen** ein Lasten- und Pflichtenheft üblich. Erklären Sie jeweils den Zweck von Lasten- und Pflichtenheft und führen Sie jeweils ein konkretes Beispiel für den Inhalt an. Tragen Sie Ihr Ergebnis in nachfolgende Tabelle ein.

| | Lastenheft | Pflichtenheft |
| :--- | :--- | :--- |
| Zweck | | |
| Beispiel für möglichen Inhalt | | |

[https://bibox2.westermann.de/book/5409/page/220](url)

[https://github.com/devsfiae/teil-1-gap/tree/main/2024-herbst](url)

---

### b. Erweitere das unten angegebene Datenmodell redundanzfrei um die vorliegenden Angaben. Gib Sie auch die Kardinalitäten an

Angaben zur Datenbank:

- Die Bearbeitung eines **Issues** darf immer nur von einem einzigen **Praktikanten** erfolgen.
- Neben seinem Namen ist auch der Vorname zu erfassen.
- Jeder Issue hat einen Beginn und ein Ende der Bearbeitung.
- In jeder Entitätsmenge sol eine eindeutige Identifizierung durch einen Primärschlüssel möglich sein

---
