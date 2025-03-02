# "Ganzheitliche Aufgabe I – Themenübersicht"

Termin: Mittwoch, 24. November 2021

---

## Inhaltsverzeichnis

- [1. UML-Diagramme: Zustands- und Anwendungsfalldiagramm](#1-uml-diagramme-zustands--und-anwendungsfalldiagramm)
- [2. Objektorientierte Programmierung und Pseudocode](#2-objektorientierte-programmierung-und-pseudocode)
- [3. UML-Modellierung für ein Smartphone-Dashboard--observer-pattern](#3-uml-modellierung-für-ein-smartphone-dashboard--observer-pattern)
- [4. ER-Modellierung und Datenbankstruktur](#4-er-modellierung-und-datenbankstruktur)
- [5. SQL-Abfragen-und-tabellenmanipulation](#5-sql-abfragen-und-tabellenmanipulation)

---

## Ganzheitliche Aufgabe I – Themenübersicht

Nachfolgend sind die fachlichen Schwerpunkte aus der ganzheitlichen Aufgabe I für Fachinformatiker/innen Anwendungsentwicklung zusammengefasst. Alle prüfungsrelevanten Inhalte sind in fünf Handlungsschritte (Aufgabenkomplexe) gegliedert.

---

## 1. UML-Diagramme: Zustands- und Anwendungsfalldiagramm

- **Zustandsdiagramm** (State Machine Diagram) für eine automatisierte Lichtsteuerung  
  - Zustände (z. B. „wartend“, „auto“, „manuell“, „zeitgesteuert“)  
  - Übergänge (Sensorerkennung, zeitgesteuerte Abschaltung, manueller Eingriff)  
  - Aktionen (Licht ein-/ausschalten)  

- **Anwendungsfalldiagramm** (Use-Case-Diagramm) für das Gebäudemanagement  
  - Akteure (Wartungsmitarbeiter, Administrator, allgemeine Mitarbeiter)  
  - Anwendungsfälle (Login, Sensordaten lesen/auswerten, Wartungsaufgaben)  

---

## 2. Objektorientierte Programmierung und Pseudocode

- **Methoden zur Temperaturerfassung**  
  - `onNewValue(...)`: Messwerte in einer Liste speichern  
  - `maxPeriod(...)`: Längste Sequenz an Messwerten oberhalb eines Mindestwertes ermitteln  
- **Pseudocode-Elemente**: Schleifen, Bedingungen, Methodenaufrufe, Objektinstanziierung  

---

## 3. UML-Modellierung für ein Smartphone-Dashboard & Observer Pattern

- **UML-Klassendiagramm** für die Klasse `Tank`  
  - Instanzvariablen (z. B. `bezeichner`, `fuellstand`, `fassungsvermoegen`)  
  - Konstruktor, Getter/Setter  
- **Observer-Muster** (TankDaten, Dashboard, History)  
  - Interface `Observer` (Methode `update()`)  
  - Interface `ObservedSubject` (`addObserver()`, `removeObserver()`, `notifyObservers()`)  
- **UML-Sequenzdiagramm**  
  - Objekterzeugung (Client → `TankDaten`/`Dashboard`)  
  - Aufrufketten (`addObserver`, `setDaten`, `notifyObservers`, `update`, `display`)  

---

## 4. ER-Modellierung und Datenbankstruktur

- **Entity-Relationship-Modell** für Sensordaten  
  - Entitäten (Sensor, Sensor-Art, Standort, Messung, Aktion usw.)  
  - Beziehungstypen und Kardinalitäten  
- **Problem bei Reduktion der Tabelle `Aktion-Art`**  
  - Mögliche Redundanzen oder Verletzung der Normalisierung  

---

## 5. SQL-Abfragen und Tabellenmanipulation

- **Aktualisieren und Abfragen von Datensätzen**  
  - `UPDATE` zur Korrektur einer fehlerhaften Erfassung  
  - `SELECT` zur Ermittlung von Urlaubstagen im Jahr 2021  
- **Anpassen der Datenbankstruktur**  
  - `DROP TABLE`, `CREATE TABLE`, Fremdschlüsselbeziehungen (`REFERENCES`)  
  - Neuer Aufbau für Tabellen (`Fehlzeit`, `Fehlzeitgrund`)  

---

> **Hinweis**: Von den fünf Handlungsschritten sind nur vier zu bearbeiten. Jeder Schritt umfasst ein eigenes Themengebiet (UML, OOP, Datenbankmodellierung, SQL). Die hier aufgeführten Schwerpunkte zeigen, welche Kompetenzen (z. B. Modellierung, Programmierung, SQL, ER-Diagramme) relevant sind.
