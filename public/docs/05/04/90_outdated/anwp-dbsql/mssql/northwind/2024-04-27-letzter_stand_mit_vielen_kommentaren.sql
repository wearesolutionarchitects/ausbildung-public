/* Am Anfang Rücksicherung der Ursprungs-Datei von Markus Trefzer aus dem Backupverzeichnis in der virtuellen oder lokalen Maschine: */
USE master
GO
ALTER DATABASE Northwind
SET SINGLE_USER
WITH ROLLBACK IMMEDIATE
GO
RESTORE DATABASE Northwind
FROM DISK = 'C:\\Backup\\northwind_30_11_2020.bak'
WITH REPLACE
GO
ALTER DATABASE Northwind
SET MULTI_USER
GO
USE Northwind
GO
/* Aufgabe 1.1: Erweitern der Tabelle Customers um die Spalten "Firstname" und "Lastname" */
ALTER TABLE Customers
ADD FirstName varchar(255), LastName varchar(255)
GO
/* Dieser T-SQL-Befehl fügt der `Customers` Tabelle in der `northwind` Datenbank zwei neue Spalten hinzu. Der Befehl `USE northwind` wechselt zur Northwind-Datenbank. `ALTER TABLE Customers` bereitet die `Customers` Tabelle auf eine Änderung vor. `ADD Firstname varchar(255), Lastname varchar(255)` fügt zwei neue Spalten `Firstname` und `Lastname` hinzu, beide vom Typ `varchar(255)`, was bedeutet, dass sie Text bis zu 255 Zeichen speichern können. */

/* Aufgabe 1.2: Aktualisierung der Spalte Firstname aus den Zeichen aus der Spalte ContactName bis zum Leerzeichen, Aktualisierung der Spalte Lastename aus den Zeichen aus der Spalte ContactName ab dem Leerzeichen. */

UPDATE Customers 											
SET	FirstName = SUBSTRING(ContactName, 1, CHARINDEX(' ', ContactName) - 1),	LastName = SUBSTRING(ContactName, CHARINDEX(' ', ContactName) + 1, LEN(ContactName)) WHERE ContactName LIKE '% %'
GO
/* Dieser T-SQL-Befehl aktualisiert die `FirstName` und `LastName` Spalten in der `Customers` Tabelle. 
- `UPDATE Customers` bereitet die `Customers` Tabelle auf eine Aktualisierung vor.
- `SET FirstName = SUBSTRING(ContactName, 1, CHARINDEX(' ', ContactName) - 1), LastName = SUBSTRING(ContactName, CHARINDEX(' ', ContactName) + 1, LEN(ContactName))` teilt den `ContactName` an der Stelle des ersten Leerzeichens auf und setzt `FirstName` auf den Teil vor dem Leerzeichen und `LastName` auf den Teil danach.
- `WHERE ContactName LIKE '% %'` beschränkt die Aktualisierung auf Zeilen, in denen `ContactName` mindestens ein Leerzeichen enthält.
Insgesamt teilt dieser Befehl den `ContactName` in `FirstName` und `LastName` auf, vorausgesetzt, der `ContactName` enthält mindestens ein Leerzeichen.*/

/*Aufgabe 2.1: Ergänzung der Tabelle Customers um den neuen Fremdschlüssel PostalCodeID*/

ALTER TABLE Customers
ADD PostalCodeID INT
GO
/*Dieser T-SQL-Befehl fügt der `Customers` Tabelle eine neue Spalte namens `PostalCodeID` hinzu. 
- `ALTER TABLE Customers` bereitet die `Customers` Tabelle auf eine Änderung vor.
- `ADD PostalCodeID INT` fügt eine neue Spalte `PostalCodeID` vom Datentyp `INT` (Integer) hinzu.
Insgesamt fügt dieser Befehl der `Customers` Tabelle eine neue Spalte `PostalCodeID` hinzu, in der Ganzzahlen gespeichert werden können. */

/* Aufgabe 2.2: Abbildung von PostalCode, City,  Region und Country mit einem Fremdschlüssel (foreign key) -\> mit anschließender Tabellenerstellungsabfrage SELECT INTO in Kombination mit der GROUP BY ANWEISUNG und HAVING mit der Bedingung PostalCode IS NOT NULL. */

SELECT PostalCode, City, Region, Country
INTO PostalCode
FROM Customers
GROUP BY PostalCode, City, Region, Country HAVING (PostalCode IS NOT NULL)
GO
/* Dieser T-SQL-Befehl erstellt eine neue Tabelle namens `PostalCode` aus der bestehenden `Customers` Tabelle. 
- `SELECT PostalCode, City, Region, Country` wählt die Spalten `PostalCode`, `City`, `Region` und `Country` aus.
- `INTO PostalCode` erstellt eine neue Tabelle `PostalCode` mit den ausgewählten Spalten.
- `FROM Customers` gibt an, dass die Daten aus der `Customers` Tabelle stammen.
- `GROUP BY PostalCode, City, Region, Country` gruppiert die Daten nach den Werten in den Spalten `PostalCode`, `City`, `Region` und `Country`.
- `HAVING (PostalCode IS NOT NULL)` ist eine Bedingung, die nur Zeilen auswählt, in denen `PostalCode` nicht NULL ist.
Insgesamt erstellt dieser Befehl eine neue Tabelle `PostalCode` aus der `Customers` Tabelle, wobei die Daten nach `PostalCode`, `City`, `Region` und `Country` gruppiert werden und nur Zeilen mit nicht NULL `PostalCode` berücksichtigt werden. */

/* Aufgabe 2.3: In der gerade erstellte PostalCode Tabelle noch einen Primär-Schlüsse (ID) hinzufügen */

ALTER TABLE PostalCode
ADD ID INT PRIMARY KEY IDENTITY (1,1)
GO
/*Dieser T-SQL-Code führt eine Änderung an der Tabelle `PostalCode` durch, indem er eine neue Spalte namens `ID` hinzufügt. Hier sind die Details:
- `ALTER TABLE PostalCode`: Dieser Befehl ändert die Struktur der Tabelle `PostalCode`.
- `ADD ID INT`: Fügt eine neue Spalte namens `ID` hinzu, die Ganzzahlen (`INT`) speichert.
- `PRIMARY KEY`: Legt fest, dass die `ID`-Spalte als Primärschlüssel der Tabelle dient. Ein Primärschlüssel identifiziert eindeutig jeden Datensatz in der Tabelle.
- `IDENTITY (1,1)`: Dies ist eine Eigenschaft, die auf die `ID`-Spalte angewendet wird. Sie erzeugt automatisch einen eindeutigen Wert für jede neue Zeile. Der erste Wert ist `1`, und jeder nachfolgende Wert wird um `1` erhöht. 
Zusammengefasst fügt dieser Code der `PostalCode`-Tabelle eine neue Spalte `ID` hinzu, die automatisch eindeutige Ganzzahlen generiert und als Primärschlüssel dient. */

/* 2.4: Aktualisierung des neuen Schlüssels PostalCodes in der Tabelle Customers */

UPDATE Customers
SET PostalCodeID = PostalCode.ID 
FROM Customers 
INNER JOIN PostalCode on Customers.PostalCode = PostalCode.PostalCode
GO

/* Dieser T-SQL-Code aktualisiert die `PostalCodeID`-Spalte in der `Customers`-Tabelle basierend auf einem `INNER JOIN` mit der `PostalCode`-Tabelle. Hier sind die Details:
- `UPDATE Customers`: Dieser Befehl aktualisiert die `Customers`-Tabelle.
- `SET PostalCodeID = PostalCode.ID`: Dieser Teil des Befehls setzt den Wert der `PostalCodeID`-Spalte in der `Customers`-Tabelle auf den Wert der `ID`-Spalte in der `PostalCode`-Tabelle.
- `FROM Customers INNER JOIN PostalCode on Customers.PostalCode = PostalCode.PostalCode`: Dieser Teil des Befehls führt einen `INNER JOIN` zwischen den `Customers`- und `PostalCode`-Tabellen durch, wobei die `PostalCode`-Spalte in beiden Tabellen übereinstimmen muss.
Zusammengefasst aktualisiert dieser Code die `PostalCodeID`-Spalte in der `Customers`-Tabelle mit den entsprechenden `ID`-Werten aus der `PostalCode`-Tabelle, basierend auf übereinstimmenden `PostalCode`-Werten in beiden Tabellen. */

/* Aufgabe 3: In der Tabelle Customers wird als Primärschlüssel die CustomerID [nchar(5)] verwendet. Diese ist nicht mehr Zeitgemäß, da sie nicht den Ansprüchen einer modernen Datenbank entspricht. Erstellen Sie in derTabelle Customers eine ID (INT).   
Vorher müssen in den Tabellen Orders und CustomerCustomerDemo die Beziehungen als Fremdschlüssel zur alten CustomerID entfernt werden. */

ALTER TABLE Orders
DROP CONSTRAINT FK_Orders_Customers
GO
/* Die T-SQL-Anweisung, die Sie bereitgestellt haben, ist eine Anweisung zum Löschen eines Constraints (Einschränkung) aus einer Tabelle in einer SQL-Datenbank. Hier ist eine kurze Erklärung:
- `ALTER TABLE Orders`: Dieser Teil der Anweisung wählt die Tabelle aus, die geändert werden soll. In diesem Fall ist es die Tabelle `Orders`.
- `DROP CONSTRAINT FK_Orders_Customers`: Dieser Teil der Anweisung löscht das Constraint mit dem Namen `FK_Orders_Customers` aus der Tabelle `Orders`.
Zusammengefasst, diese Anweisung entfernt das Constraint `FK_Orders_Customers` aus der Tabelle `Orders`. Es ist wichtig zu beachten, dass das Löschen eines Constraints Auswirkungen auf die Datenintegrität haben kann und daher mit Vorsicht durchgeführt werden sollte. */

ALTER TABLE CustomerCustomerDemo
DROP CONSTRAINT FK_CustomerCustomerDemo_Customers
GO

ALTER TABLE Customers
DROP CONSTRAINT PK_Customers
GO

ALTER TABLE Customers
ADD ID INT PRIMARY KEY IDENTITY (1,1)
GO

/* 4.1: Die Orders Tabelle verfügt ebenfalls über einen Fremdschlüssel  CustomerID [nchar(5)], dieser verweist auf die Customer Tabelle. 
Fügen Sie hier eine neue CustomID ein */

ALTER TABLE Orders
ADD CustomID INT
GO
/*Dieser T-SQL-Code fügt der `Orders`-Tabelle eine neue Spalte namens `CustomID` hinzu. Hier sind die Details:
- `ALTER TABLE Orders`: Dieser Befehl ändert die Struktur der `Orders`-Tabelle.
- `ADD CustomID INT`: Dieser Teil des Befehls fügt eine neue Spalte namens `CustomID` vom Datentyp `INT` (Integer) zur `Orders`-Tabelle hinzu.
Zusammengefasst fügt dieser Code der `Orders`-Tabelle eine neue Spalte `CustomID` hinzu, die Integer-Werte speichern kann. */

/* 4.2: Aktualisierung der neuen CustomID in der Tabelle Orders mit den Daten aus der Customers-Tabelle */

UPDATE Orders
SET	CustomID = Customers.ID 
FROM Customers 
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GO
/*Die bereitgestellte T-SQL-Anweisung ist eine `UPDATE`-Anweisung, die zum Aktualisieren von Datensätzen in einer Tabelle verwendet wird. Hier ist eine kurze Erklärung:
- `UPDATE Orders`: Dieser Teil der Anweisung wählt die Tabelle `Orders` aus, in der die Aktualisierung vorgenommen werden soll.
- `SET CustomID = Customers.ID`: Dieser Teil der Anweisung aktualisiert den Wert der `CustomID`-Spalte in der `Orders`-Tabelle auf den Wert der `ID`-Spalte in der `Customers`-Tabelle.
- `FROM Customers INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID`: Dieser Teil der Anweisung führt einen `INNER JOIN` zwischen den Tabellen `Customers` und `Orders` basierend auf der Bedingung aus, dass `CustomerID` in beiden Tabellen gleich ist.
Zusammengefasst, diese Anweisung aktualisiert die `CustomID`-Spalte in der `Orders`-Tabelle mit den `ID`-Werten aus der `Customers`-Tabelle, wobei die Zeilen basierend auf der Übereinstimmung der `CustomerID` in beiden Tabellen ausgewählt werden. Es ist wichtig zu beachten, dass diese Anweisung alle Zeilen in der `Orders`-Tabelle aktualisiert, für die eine Übereinstimmung gefunden wird. Wenn keine Übereinstimmung gefunden wird, bleibt die `CustomID` unverändert. */

/* Nachdem alle T-SQL Anweisungen abgearbeitet wurden, kann man in der Tabelle Customers die überfälligen Spalten per Script löschen. Hierzu müssen vorher die Indizies entfernt werden. */

DROP INDEX IF EXISTS City ON Customers
GO

DROP INDEX IF EXISTS PostalCode ON Customers
GO

DROP INDEX IF EXISTS Region ON Customers
GO

ALTER TABLE Customers
DROP COLUMN City, Country, PostalCode, Region
GO
/*
Dieses T-SQL-Skript führt eine Änderung an der Tabelle `Customers` durch. Es entfernt die Spalten `City`, `PostalCode`, `Region` und `Country` aus der Tabelle. Nachdem dieses Skript ausgeführt wurde, werden diese Spalten und alle darin enthaltenen Daten nicht mehr in der Tabelle `Customers` vorhanden sein. Bitte beachten Sie, dass diese Aktion nicht rückgängig gemacht werden kann.
*/