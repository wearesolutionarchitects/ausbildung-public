# Übergeordnete Projektsituation

Alle fünf Handlungsschritte beziehen sich auf ein Szenario bei der „WärL Chemie GmbH“, die für ein neues Gebäude eine automatisierte Gebäudesteuerung einführt. Die IT-Abteilung entwickelt die Steuerungs- und Wartungsprozesse selbst. Die Prüfungsaufgaben sind auf Teilaspekte dieses Projekts zugeschnitten und erfordern jeweils unterschiedliche IT-Fachkenntnisse.

3. Inhalte der fünf Handlungsschritte (Aufgabenkomplexe)

3.1 Handlungsschritt 1 – UML-Diagramme: Zustands- und Anwendungsfalldiagramm
	1.	Zustandsdiagramm (State Machine Diagram) für einen Lichtsteuerungs-Controller:
	•	Zustände „wartend“, „auto“, „manuell“, „zeitgesteuert“
	•	Sensorerkennung und Übergänge (z. B. Licht ein-/ausschalten, verzögertes Einschalten, manuelle Eingriffe)
	•	Typische UML-Notation: Anfangszustand, Endzustand, Übergänge mit Trigger-/Guard-Bedingungen, Aktionen.
	2.	Anwendungsfalldiagramm (Use-Case-Diagramm) für das Gebäudemanagement:
	•	Akteure: verschiedene Mitarbeiter-Rollen (Wartungsmitarbeiter, Administrator, allgemein jeder Mitarbeiter)
	•	Anwendungsfälle: Daten auslesen, Sensordaten auswerten, Login, Wartungsaufgaben etc.

	Themenschwerpunkte: UML-Grundlagen, State Machine Diagrams, Use-Case-Diagrams, Identifikation von Zuständen, Übergängen und Akteuren.

3.2 Handlungsschritt 2 – OOP/Pseudocode: Methoden zur Temperaturerfassung
	1.	Pseudocode für onNewValue(...):
	•	Erstellung eines Value-Objekts (Parameter: sensor_id, value, time)
	•	Speichern in einer TempList (Aufruf von setValue(...))
	•	Methodensignatur: onNewValue(sensor_id: Integer, value: Double, time: Long)
	2.	Pseudocode für maxPeriod(sensor_id: Integer, mindestwert: Double):
	•	Bestimmung der längsten Sequenz nacheinander erfasster Messwerte, die über einem bestimmten Grenzwert liegen.
	•	Beispielwerte werden gegeben (22, 23, 21, …). Ergebnis: maximale aufeinanderfolgende Messreihen oberhalb des Grenzwerts.

	Themenschwerpunkte: Objektorientierung, Klassenstruktur (Value, TempList), Schleifen, If-Bedingungen, Zählen/Sequenzermittlung, allgemeine Pseudocode-Syntax.

3.3 Handlungsschritt 3 – UML-Modellierung fürs Smartphone-Dashboard & Observer Pattern
	1.	UML-Klassendiagramm für die Klasse Tank:
	•	Instanzvariablen (z. B. bezeichner, fuellstand, fassungsvermoegen)
	•	Konstruktor und Methoden (Get-/Set-Methoden)
	•	Datentypen für Attribute und Sichtbarkeiten (private, public etc.)
	2.	Observer-Muster (TankDaten, Dashboard, History):
	•	Interface Observer: update()-Methode
	•	Interface ObservedSubject: addObserver(), removeObserver(), notifyObservers()
	•	Klassen TankDaten, Dashboard, History: Implementierung des Observer Patterns
	•	UML-Sequenzdiagramm: Erzeugung von Objekten (Client → TankDaten / Dashboard), Aufrufe von addObserver, setDaten, notifyObservers, update, display.

	Themenschwerpunkte: UML-Klassendiagramme (Attribute, Methoden, Sichtbarkeiten), Implementierung des Observer Patterns, Sequenzdiagramme, Methodenaufrufe und Interaktionsabläufe.

3.4 Handlungsschritt 4 – ER-Modellierung und Datenbanknormalisierung
	1.	ER-Modell zur Speicherung von Sensordaten:
	•	Entitäten: Sensor, Sensor-Art, Standort, Messung, Aktion, Aktionsprotokoll etc.
	•	Beziehungstypen (z. B. 1:n, m:n) und Besonderheiten (z. B. „Ein Sensor hat genau eine Sensor-Art“, „Von einem Sensor können mehrere Messungen ausgehen“).
	2.	Problem bei Wegfall der Tabelle Aktion-Art:
	•	Entfernen des Fremdschlüssels, Hinzufügen der Beschreibung der Aktionsart in der Tabelle Aktion (führt u. a. zu Redundanzen / Verletzung von Normalformen).

	Themenschwerpunkte: Relationale Datenmodellierung, Entity-Relationship-Diagramme, Normalisierung, Redundanzen vermeiden, Fremdschlüssel.

3.5 Handlungsschritt 5 – SQL-Abfragen und Tabellenmanipulation
	1.	Korrektur fehlerhafter Datensätze via UPDATE
	2.	Abfrage (SELECT) der Urlaubstage aller Mitarbeiter im Jahr 2021
	3.	Datenbankstruktur anpassen:
	•	Tabelle Fehlzeit löschen (DROP TABLE)
	•	Neue Tabelle Fehlzeitgrund erstellen (z. B. Fehlzeitgrund mit ID und Bezeichnung)
	•	Neue Tabelle Fehlzeit anlegen, die über Grund_ID (als Fremdschlüssel) mit Fehlzeitgrund verknüpft ist.

	Themenschwerpunkte: SQL-Grundlagen (DML – SELECT, UPDATE, INSERT, DELETE), DDL (CREATE TABLE, DROP TABLE, ALTER TABLE), Fremdschlüsselbeziehungen, JOIN- und Restrukturierungsaufgaben.

4. Übersicht der abgefragten Kompetenzen
	1.	UML-Kenntnisse
	•	Anwendungsfalldiagramme, Zustandsdiagramme, Klassendiagramme (einschl. Sichtbarkeiten, Methoden/Attribute), Sequenzdiagramme.
	2.	Objektorientierung in Pseudocode
	•	Klassenstrukturen (Konstruktoren, Get/Set), Schleifen, Verzweigungen, methodische Umsetzung in einer Java-ähnlichen Syntax.
	3.	Observer Pattern
	•	Schnittstellendefinition (Observer, ObservedSubject), Implementierung in konkreten Klassen, Ereignisbenachrichtigung (notify, update).
	4.	Relationale Datenbanken
	•	ER-Modellierung (1:n, n:m, Normalisierung, Vermeidung von Redundanz, Fremdschlüssel).
	•	Grundlegende DDL-Befehle (CREATE TABLE, DROP TABLE, ALTER TABLE) und DML-Befehle (SELECT, UPDATE, INSERT, DELETE).
	•	Fremdschlüsseldefinition (REFERENCES), Primärschlüssel.
	5.	Allgemeine Prüfungskompetenzen
	•	Arbeiten nach Vorgaben (z. B. max. Anzahl anzugebenen Items), Genauigkeit bei Syntax, Einhaltung vorgegebener Struktur.
	•	Zeitmanagement (90 Minuten) und Auswahl von 4 aus 5 Aufgaben.

5. Fazit: Prüfungsschwerpunkte

Die Ganzheitliche Aufgabe I ist typisch für die schriftliche Prüfung angehender Fachinformatiker/innen (Anwendungsentwicklung). Sie integriert wesentliche Kompetenzen:
	•	Softwareengineering / Modellierung (UML, Objektorientierung, Datenmodellierung)
	•	Programmierung (Pseudocode, OOP-Konzepte, Methoden)
	•	Datenbanken (ER-Modell, Normalformen, SQL-Queries, DDL, DML)
	•	Grundlagen der Softwarearchitektur (Observer Pattern)

Wer diese Aufgabe bearbeitet, sollte fundierte Kenntnisse in UML-Diagrammarten, Pseudocode-Strukturen, SQL-Befehlen sowie den Entwurf und die Normalisierung von Datenbankschemata haben. Darüber hinaus zeigt die Prüfung, dass Verständnis für die Dokumentation (z. B. Sequenzdiagramm) und für das Zusammenspiel verschiedener Softwarekomponenten (Controller, Observer, Datenhaltung) gefragt ist.

Kurz zusammengefasst

Die PDF-Prüfungsaufgabe testet vor allem UML-Diagramme, objektorientierte Programmierung (Pseudocode), ER-Modellierung, SQL-Abfragen, und klassische Softwarekonzepte (z. B. Observer Pattern). Die Handlungsschritte bauen auf einem praxisnahen Szenario auf (Gebäudeautomation, Sensor-/Messdaten, Wartungs- und Verwaltungsaufgaben) und verdeutlichen, wie vielfältig das Einsatzgebiet von Fachinformatiker/innen für Anwendungsentwicklung ist.