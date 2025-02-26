# README – Ganzheitliche Aufgabe I (Winter 2021/22)

---

## Projektsituation

Die Handlungsschritte 1 bis 5 beziehen sich auf die folgende Ausgangssituation:

> Die WärL Chemie GmbH expandiert und plant in diesem Zusammenhang ein neues Gebäude. Für dieses Projekt übernimmt die IT-Abteilung der WärL Chemie GmbH selbst die Realisierung der Gebäudesteuerung und Wartungsarbeiten.  
> Sie sollen vier der folgenden fünf Aufgaben in diesem Projekt erledigen:
>
> 1. Zustandsdiagramm und Anwendungsfalldiagramm für Controller und Lichtsteuerung erstellen  
> 2. OOP-Methoden für die Auswertung von Temperaturmessungen implementieren  
> 3. UML-Modellierung für ein Smartphone-Dashboard zur Anzeige von Tankfüllständen anfertigen  
> 4. ER-Modell zur Speicherung von Sensordaten anlegen  
> 5. SQL-Abfragen für eine Zeiterfassungsdatenbank formulieren

---

## 1. Handlungsschritt (25 Punkte)

### a) Zustandsdiagramm für Lichtsteuerung (15 Punkte)

Für jeden Flur der Gebäude der WärL Chemie GmbH soll eine automatisierte Lichtsteuerung eingerichtet werden.  
Der Controller zur Lichtsteuerung kann sich in einem der Zustände

- „wartend“  
- „auto“  
- „manuell“  
- „zeitgesteuert“  

befinden. Hierzu gelten u. a. folgende Regeln:

- Initialzustand: „wartend“ (Licht aus)  
- Wechselt zu „auto“, wenn Personen erkannt werden (Licht an)  
- Von „auto“ zu „zeitgesteuert“, sobald keine Personen mehr erkannt werden  
- Erneutes Erkennen von Personen im Zustand „zeitgesteuert“ → zurück zu „auto“  
- Bleiben Personen aus, endet „zeitgesteuert“ in „wartend“ (Licht aus)  
- Manuelles Einschalten (Übergang von „auto“ zu „manuell“) in einer kurzen Verzögerungsphase  
- Manuelles Ausschalten: zurück zu „wartend“ oder ggf. Übergang zu „zeitgesteuert“  

--

**Aufgabe**: Erstellen Sie ein Zustandsdiagramm für den Controller der Lichtsteuerung.

### b) Anwendungsfalldiagramm (Use-Case) für Gebäudemanagement (10 Punkte)

Neue Aufgaben:

- Wartungsmitarbeiter: Wartung/Kalibrierung von Sensoren (Login erforderlich, falls nicht vorhanden)  
- Administratoren: Sensordaten auswerten (Lesen + Login erforderlich, falls nicht vorhanden)  
- Jeder Mitarbeiter: Sensordaten auslesen  

**Aufgabe**: Erstellen Sie ein Anwendungsfalldiagramm für die oben beschriebene Situation.

---

## 2. Handlungsschritt (25 Punkte)

In einem Gebäudeteil messen Sensoren in unregelmäßigen Abständen Temperaturwerte. Für die Auswertung stehen zwei Methoden an.

**Gegebene Klassen**:

```plaintext
Value
- sensor_id : Integer
- value     : Double
- time      : Long

+ Konstruktor(sensor_id: Integer, value: Double, time: Long)
+ getId()    : Integer
+ getValue() : Double
+ getTime()  : Long

---

TempList
+ setValue(value: Value)
+ getValue(sensor_id, pos: Integer) : Value
+ getSize(sensor_id: Integer)       : Integer
```

Speichert ein Value-Objekt chronologisch in einer Liste.
Die Objekte werden für jeden Sensor getrennt gespeichert.
Liefert für den Sensor mit der übergebenen sensor_id das Value-Objekt an der Position pos.
Liefert die Anzahl der gespeicherten Value-Objekte für den Sensor (sensor_id).

a) onNewValue(...) (5 Punkte)

Sobald neue Messwerte eintreffen, wird

onNewValue(sensor_id: Integer, value: Double, time: Long)

aufgerufen. Die Methode soll:

1. Ein Value-Objekt mit den Parametern erzeugen
2. Das Value-Objekt mittels tempList.setValue(...) speichern

Aufgabe: Implementieren Sie onNewValue(...) in Pseudocode.

b) maxPeriod(...) (20 Punkte)

Die Methode

maxPeriod(sensor_id: Integer, mindestwert: Double) : Integer

ermittelt die längste Folge von Werten eines Sensors in tempList, die ununterbrochen über dem mindestwert liegen.

Beispiel:
Werte: 20, 22, 23, 21, 19, 18, 20, 22, 23, 23, 24, 22, 21
Maximal zusammenhängende Werte ≥ 22 → 5

Aufgabe: Implementieren Sie maxPeriod(...) in Pseudocode.

---

## 3. Handlungsschritt (25 Punkte)

Smartphone-Dashboard & Observer Pattern

Eine Smartphone-App soll verschiedene Ansichten für Tankfüllstände bieten:

- „Dashboard“-Anzeige: Füllstände aller Tanks
- „History“-Anzeige: Zeitliche Verläufe

a) Klasse Tank
	1.	Instanzvariablen: bezeichner, fuellstand, fassungsvermoegen (jeweils private)
	2.	Konstruktor zur Initialisierung
	3.	Set-/Get-Methoden (Beispiel für fuellstand)

Aufgabe:
	•	aa) Erstellen Sie das UML-Klassendiagramm für Tank. (7 Punkte)
	•	ab) Implementieren Sie Set-/Get-Methoden für fuellstand in Pseudocode. (4 Punkte)

b) Observer-Muster

Die Füllstände werden stündlich aktualisiert. Ein Entwurf nach dem Observer Pattern:

TankDaten                <<interface>>
                         Observer
observers : Observer[]
fuellstaende : int[]
- fuellstaende_datum : String[10]

+ setDaten(int[], String[]) : void
+ getFuellstaende() : int[]
+ notifyObservers() : void
---------------------------------------

Dashboard        History
+ Dashboard(o : ObservedSubject)    - History(o : ObservedSubject)
+ display() : void                  + display() : void

<<interface>>
ObservedSubject
+ addObserver(o: Observer)    : void
+ removeObserver(o: Observer) : void
+ notifyObservers()           : void

	•	ba) Ergänzen Sie das Klassendiagramm in TankDaten, Dashboard, History (z. B. fehlende Implementierung, Beziehungen). (4 Punkte)
	•	bb) Erläutern Sie die Art der Beziehung zwischen TankDaten und ObservedSubject. (2 Punkte)

c) UML-Sequenzdiagramm

ca) Erweitern Sie das Sequenzdiagramm. (6 Punkte)
Ablauf:
	1.	Client erzeugt TankDaten und Dashboard
	2.	Konstruktor Dashboard ruft addObserver(...) auf
	3.	Client ruft setDaten(...) auf
	4.	In setDaten wird notifyObservers gestartet
	5.	notifyObservers → update
	6.	update → getFuellstaende → display
	7.	Rückkehr zum Client

Client
create :TankDaten
create :Dashboard
addObserver(Observer)
...
setDaten(int[], String[])
...

cb) Implementieren Sie notifyObservers in Pseudocode. (2 Punkte)

4. Handlungsschritt (25 Punkte)

ER-Modell für Sensordaten
	•	Jeder Sensor hat eine eigene Sensor-Art
	•	Mehrere Sensoren können von derselben Sensor-Art sein
	•	Sensoren sind an bestimmten Standorten, mit jeweils mehreren Sensoren pro Standort
	•	Messungen (mehrere pro Sensor)
	•	Aktionen (können von unterschiedlichen Messungen ausgelöst werden)
	•	Zu jeder Aktion gehört genau ein Eintrag im Aktionsprotokoll
	•	Es gibt mehrere Aktions-Arten, die von einer Aktion ausgelöst werden

Aufgabe:
a) Erstellen Sie ein ER-Modell (Attribute sind nicht erforderlich). (20 Punkte)
b) Die Tabelle Aktion-Art soll entfernt werden, stattdessen wird die Beschreibung in Aktion eingefügt.
Beschreiben Sie das Problem, das dadurch entsteht. (5 Punkte)

5. Handlungsschritt (25 Punkte)

SQL-Abfragen Zeiterfassungsdatenbank

Tabellen:
	1.	Mitarbeiter (MAID, Nachname, Vorname, Geburtsdatum, Tagesarbeitszeit)
	2.	Fehlzeit (FZ_ID, MAID, Von_Datum, Bis_Datum, Grund, Fehltage)

Beispiel:

FZ_ID	MAID	Von_Datum	Bis_Datum	Grund	Fehltage
1	811	18.10.2021	22.10.2021	Krank	5
2	902	18.10.2021	05.11.2021	Krank	16
3	811	30.12.2021	31.12.2021	Urlaub	2
…	…	…	…	…	…

a) Korrektur eines Datensatzes (5 Punkte)

Für Ulrich Schmidt (815) wurde statt einer zweitägigen „Dienstreise“ (30.06.–01.07.2022) fälschlich ein eintägiger „Urlaub“ (30.06.2021) gebucht.
Aufgabe: Erstellen Sie eine UPDATE-SQL-Anweisung zur Korrektur.

b) Urlaubstage aller Mitarbeiter im Jahr 2021 (10 Punkte)

Aufgabe: Erstellen Sie eine SQL-Abfrage, die die im Jahr 2021 genommenen Urlaubstage summiert und nach MA auflistet.

Beispielausgabe:

811  Müller Jens   5
812  Scholz Birgit 0
815  Schmidt Ulrich 2
817  Storck Hans   0
841  Ullmann Franz 10
...

c) Datenbankänderungen (insgesamt 10 Punkte)
	•	ca) DROP TABLE Fehlzeit (2 Punkte)
	•	cb) Neue Tabelle Fehlzeitgrund(Grund_ID, Grund) (3 Punkte)
	•	cc) Neue Tabelle Fehlzeit (FZ_ID, MA_ID, Von_Datum, Bis_Datum, Grund_ID, Fehltage) mit Grund_ID als Fremdschlüssel zu Fehlzeitgrund. (5 Punkte)


