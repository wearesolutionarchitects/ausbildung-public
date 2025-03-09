# README.md

## Aufgabe: 3 Normalform umsetzen innerhalb der Northwind Database

### Grundlage Northwind Database
Sie erhalten die Northwind Database von Ihrem Chef. Im Zuge der Normalisierung sollen folgende Felder bearbeitet in der Tabelle Customers erweitert und geändert werden. Erstellen Sie zuerst ein Backup.

### Aufgabe 1
Im Feld „ContactName“ finden Sie den Vor- Nachname z. B. Maria Anders. Hier sollen zwei neue Felder angelegt werden mit den Bezeichnungen Firstname und Lastname. Der Name soll gesplittet werden. Das Ergebnis soll wie folgt aussehen „Firstname = Maria und Lastname = Anders.

### Aufgabe 2
PostalCode und Country soll mit einem Fremdschlüssel abgebildet werden. Dabei soll der jeweilige Primärschlüssel den Ort, die Postleitzahl und das Land abbilden. Überlegen Sie zuerst wie Sie dies realisieren können. Besprechen Sie das im Team und anschließend mit Ihrem Dozenten. Welche Hilfsmittel stehen Ihnen dabei zur Verfügung.

### Aufgabe 3
In der Tabelle Customers wird als Primärschlüssel die CustomerID [nchar(5)] verwendet. Diese ist nicht mehr Zeitgemäß, da sie nicht den Ansprüchen einer modernen Datenbank entspricht. Erstellen Sie in der Tabelle Customers eine ID (INT).

### Aufgabe 4
Die Orders Tabelle verfügt ebenfalls über einen Fremdschlüssel CustomerID [nchar(5)] dieser verweist auf die Customer Tabelle. Fügen Sie hier eine neue CustomID ein und füllen Sie diese mit den von Ihnen generierten ID aus der Customers Tabelle ab. Stellen Sie sicher, dass nach dem Abfüllen des Feldes auch die richtigen Bestellungen zum richtigen Kunden (Customer) verfügbar sind.
