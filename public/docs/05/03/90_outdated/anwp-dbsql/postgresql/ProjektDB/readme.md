# Erstellen Sie ein einziges SQL-Script mit der folgenden Aufgabe

![ERM](projectdb.pgerd.png)


1. Erstellen Sie eine Datenbank mit dem Namen ProjektDB

2. Tabelle Projekte erstellen (bitte hier alternative Feldtypen recherchieren und verwenden **> ID SERIAL PRIMARY KEY**)
   - ID INT PRIMARY KEY und IDENTITY(1,1)
   - Projektname NVARCHAR(255) NOT NULL
   - Startdatum DATE
   - Enddatum DATE
   - Budget DECIMAL(18, 2)

3. Tabelle Mitarbeiter erstellen
   - ID INT PRIMARY KEY IDENTITY(1,1)
   - Vorname NVARCHAR(50)
   - Nachname NVARCHAR(50)
   - Abteilung NVARCHAR(100)

4. Tabelle Aufgaben erstellen
   - ID INT PRIMARY KEY IDENTITY(1,1)
   - Aufgabenname NVARCHAR(255) NOT NULL
   - Beschreibung TEXT
   - Startdatum DATE
   - Enddatum DATE
   - Status NVARCHAR(50)
   - ProjektID INT
   - MitarbeiterID INT
   - Erstellen Sie einen Fremdschlüssel: (ProjektID) referenziert auf Projekte(ID)
   - Erstellen Sie einen Fremdschlüssel: (MitarbeiterID) referenziert auf Mitarbeiter(ID)

5. Füllen Sie die Tabelle Projekte mit 5 Projekten (Projekt 1 bis 5)

6. Füllen Sie die Tabelle Mitarbeiter mit 3 Datensätzen (Beachten Sie die Referenzen)

7. Füllen Sie die Tabelle Aufgaben mit 10 Datensätzen (Beachten Sie die Referenzen)

8. Erstellen Sie ein Script um Login User und einen User mit dem Namen „ProjektAdmin“ mit dem Passwort „Test1234!“. Geben Sie diesem User die „db_owner“ Berechtigung -> PostgreSQL Variante suchen

9. Bitte notieren Sie die Unterschiede bei den SQL Scripten
