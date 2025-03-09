-- 1. Erstellen der Datenbank ProjektDB
-- 1.INSERT INTOCreate the database ProjektDB

-- CREATE DATABASE ProjektDB;
-- USE ProjektDB;

--Dieses Skript kann immer wieder ausgeführt werden, wenn Du Deine Datenbank neu erstellen möchtest
--this script can be run over and over if you would like to rebuild your database at anytime
DROP TABLE IF EXISTS Aufgaben;
DROP TABLE IF EXISTS Mitarbeiter;
DROP TABLE IF EXISTS Projekte;

-- 2. Erstellen der Tabelle Projekte
-- 2. Create the table Projekte 
CREATE TABLE Projekte
(
ID SERIAL PRIMARY KEY,
Projektname VARCHAR(255) NOT NULL,
Startdatum DATE,
Enddatum DATE,
Budget NUMERIC(18, 2)
);

-- 3. Erstellen der Tabelle Mitarbeiter
-- 3. Create the table Mitarbeiter
CREATE TABLE Mitarbeiter
(
ID SERIAL PRIMARY KEY,
Vorname VARCHAR(50),
Nachname VARCHAR(50),
Abteilung VARCHAR(100)
);

-- 4. Erstellen der Tabelle Aufgaben mit Fremdschlüsseln auf Projekte und Mitarbeiter
-- 4. Create the table Aufgaben with foreign keys to Projekte and Mitarbeiter
CREATE TABLE Aufgaben
(
ID SERIAL PRIMARY KEY,
Aufgabenname VARCHAR(255) NOT NULL,
Beschreibung TEXT,
Startdatum DATE,
Enddatum DATE,
Status VARCHAR(50),
ProjektID INT REFERENCES Projekte(ID), -- Fremdschlüssel auf Projekte / Foreign key to Projekte
MitarbeiterID INT REFERENCES Mitarbeiter(ID) -- Fremdschlüssel auf Mitarbeiter / Foreign key to Mitarbeiter
);

-- 5. Einfügen von 5 Projekten in die Tabelle Projekte
-- 5. Insert 5 projects into the table Projekte

INSERT INTO Projekte (Projektname, Startdatum, Enddatum, Budget) VALUES  
('Unbenanntes Projekt', '2024-05-09', '2024-06-15', 10000.00),
('Android und iOS App-Entwicklung für unbenanntes Projekt', '2024-06-16', '2024-07-31', 15000.00),
('Webshop-Entwicklung für unbennantes Projekt', '2024-08-01', '2024-12-31', 20000.00),
('HHIB MegaApp', '2025-01-01', '2025-02-28', 25000.00),
('HHIB MegaStore', '2026-01-02', '2026-07-31', 30000.00);

-- 6. Einfügen von 3 Datensätzen in die Tabelle Mitarbeiter unter Beachtung der Referenzen
-- 6. Insert 3 datasets into the table Mitarbeiter in compliance with the references

INSERT INTO Mitarbeiter (Vorname, Nachname, Abteilung) VALUES
('Heiko', 'Fanieng', 'SolArc'),
('Hiba', 'Al Ansari', 'UI/UX-Design'),
('Irina', 'Zittlau', 'DevOps'),
('Puya ', 'Khandany', 'Projectmanagemment');

-- 7. Einfügen von 10 Datensätzen in die Tabelle Aufgaben unter Beachtung der Referenzen
-- 7. Insert 10 datasets into the table Aufgaben in compliance with the references

INSERT INTO Aufgaben (Aufgabenname, Beschreibung, Startdatum, Enddatum, Status, ProjektID, MitarbeiterID) VALUES
('Projektthema', 'Festlegen eines Projektthemas', '2024-05-09', '2024-05-24', 'In Bearbeitung', 1, 1),
('Projektthema', 'Festlegen eines Projektthemas', '2024-05-09', '2024-05-24', 'In Bearbeitung', 1, 2),
('Projektthema', 'Festlegen eines Projektthemas', '2024-05-09', '2024-05-24', 'In Bearbeitung', 1, 3),
('Projektthema', 'Festlegen eines Projektthemas', '2024-05-09', '2024-05-24', 'In Bearbeitung', 1, 4),
('Rollen', 'Rollenzuweisung im Team', '2024-05-27', '2024-05-28', 'In Bearbeitung', 1, 1),
('Rollen', 'Rollenzuweisung im Team', '2024-05-27', '2024-05-28', 'In Bearbeitung', 1, 2),
('Rollen', 'Rollenzuweisung im Team', '2024-05-27', '2024-05-28', 'In Bearbeitung', 1, 3),
('Rollen', 'Rollenzuweisung im Team', '2024-05-27', '2024-05-28', 'In Bearbeitung', 1, 4),
('Projektplan', 'Erstellen eines Projektplanes', '2024-05-29', '2024-06-15', 'In Bearbeitung', 1, 1),
('Projektplan', 'Erstellen eines Projektplanes', '2024-05-29', '2024-06-15', 'In Bearbeitung', 1, 2),
('Projektplan', 'Erstellen eines Projektplanes', '2024-05-29', '2024-06-15', 'In Bearbeitung', 1, 3),
('Projektplan', 'Erstellen eines Projektplanes', '2024-05-29', '2024-06-15', 'In Bearbeitung', 1, 4);


-- 8. Erstellen eines Scriptes, welches den Login User mit dem Namen 'ProjektAdmin' und dem Passwort 'Test1234!' erstellt und dem User die Berechtigung "db_owner" gibt.
-- 8. Create a script that creates the login user with the name 'ProjektAdmin' and the password 'Test1234!' and gives the user the permission "db_owner"

-- In PostgreSQL, es gibt keine direkte Entsprechung für den SQL Server Befehl 'CREATE LOGIN'. 
-- Sie können einen neuen Benutzer (oder 'ROLE' in PostgreSQL) mit dem Befehl 'CREATE ROLE' erstellen.
-- Die Berechtigung 'db_owner' entspricht der Rolle 'OWNER' in PostgreSQL.

CREATE ROLE ProjektAdmin WITH LOGIN PASSWORD 'Test1234!';
ALTER DATABASE ProjektDB OWNER TO ProjektAdmin;
