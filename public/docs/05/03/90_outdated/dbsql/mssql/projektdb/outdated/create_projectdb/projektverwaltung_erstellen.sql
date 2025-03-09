-- Prüfen ob Datenbank vorhanden / 1. Erstellen der Datenbank ProjektDB
-- Check if database exists / 1. Create the database ProjektDB
if not exists (select name from sys.databases where name = N'ProjektDB')
create database ProjektDB;
go
use ProjektDB

--Dieses Skript kann immer wieder ausgeführt werden, wenn Du Deine Datenbank neu erstellen möchtest
--this script can be run over and over if you would like to rebuild your database at anytime
drop table if exists Aufgaben
drop table if exists Mitarbeiter
drop table if exists Projekte

-- 2. Erstellen der Tabelle Projekte
-- 2. Create the table Projekte 
create table Projekte
(
ID INT PRIMARY KEY  IDENTITY(1,1),
Projektname NVARCHAR(255) NOT NULL,
Startdatum DATE,
Enddatum DATE,
Budget DECIMAL(18, 2)
);

-- 3. Erstellen der Tabelle Mitarbeiter
-- 3. Create the table Mitarbeiter
create table Mitarbeiter
(
ID INT PRIMARY KEY IDENTITY(1,1),
Vorname NVARCHAR(50),
Nachname NVARCHAR(50),
Abteilung NVARCHAR(100)
);

-- 4. Erstellen der Tabelle Aufgaben mit Fremdschlüsseln auf Projekte und Mitarbeiter
-- 4. Create the table Aufgaben with foreign keys to Projekte and Mitarbeiter
create table Aufgaben
(
ID INT PRIMARY KEY IDENTITY(1,1),
Aufgabenname NVARCHAR(255) NOT NULL,
Beschreibung TEXT,
Startdatum DATE,
Enddatum DATE,
Status NVARCHAR(50),
ProjektID INT FOREIGN KEY REFERENCES Projekte(ID), -- Fremdschlüssel auf Projekte / Foreign key to Projekte
MitarbeiterID INT FOREIGN KEY REFERENCES Mitarbeiter(ID) -- Fremdschlüssel auf Mitarbeiter / Foreign key to Mitarbeiter
);

-- 5. Einfügen von 5 Projekten in die Tabelle Projekte
-- 5. Insert 5 projects into the table Projekte

insert into Projekte (Projektname, Startdatum, Enddatum, Budget) values  
('Strukturierung SQL in der Umschulung', '2024-02-01', '2024-02-29', 10000.00),
('Umsetzung MS-SQL innerhalb der Umschulung', '2024-03-01', '2024-03-29', 15000.00),
('Realisierung von MS-SQL Datenbanken in der Umschulung', '2024-04-01', '2024-04-14', 20000.00),
('Übertragung von MS-SQL auf PostgreeSQL', '2024-04-15', '2024-04-30', 25000.00),
('Bestehen der IHK-Abschlussprüfung', '2026-01-02', '2026-02-03', 30000.00);

-- 6. Einfügen von 3 Datensätzen in die Tabelle Mitarbeiter unter Beachtung der Referenzen
-- 6. Insert 3 datasets into the table Mitarbeiter in compliance with the references

insert into Mitarbeiter (Vorname, Nachname, Abteilung) VALUES
('Irina', 'Zittlau', 'Leitungs-Assistenz'),
('Rafaela', 'Fuhrman', 'Art director'),
('Abdel', 'El Bouanani', 'Head of Logic'),
('Michael', 'Reetz', 'BGP-Expert'),
('Heiko', 'Fanieng', 'Head of IT');

-- 7. Einfügen von 10 Datensätzen in die Tabelle Aufgaben unter Beachtung der Referenzen
-- 7. Insert 10 datasets into the table Aufgaben in compliance with the references

insert into Aufgaben (Aufgabenname, Beschreibung, Startdatum, Enddatum, Status, ProjektID, MitarbeiterID) VALUES
('Erstellen der Datenbankstruktur', 'Erstellen der Tabellen und Beziehungen in der Datenbank', '2024-02-01', '2024-02-10', 'In Bearbeitung', 1, 1),
('Importieren von Daten', 'Importieren von Testdaten in die Datenbank', '2024-02-11', '2024-02-15', 'In Bearbeitung', 1, 2),
('Erstellen von Abfragen', 'Erstellen von SELECT-Abfragen zur Datenanalyse', '2024-02-16', '2024-02-20', 'In Bearbeitung', 1, 3),
('Optimierung der Datenbank', 'Optimierung von Indizes und Abfragen', '2024-02-21', '2024-02-25', 'In Bearbeitung', 1, 4),
('Erstellen der Datenbankstruktur', 'Erstellen der Tabellen und Beziehungen in der Datenbank', '2024-03-01', '2024-03-10', 'In Bearbeitung', 2, 1),
('Importieren von Daten', 'Importieren von Testdaten in die Datenbank', '2024-03-11', '2024-03-15', 'In Bearbeitung', 2, 2),
('Erstellen von Abfragen', 'Erstellen von SELECT-Abfragen zur Datenanalyse', '2024-03-16', '2024-03-20', 'In Bearbeitung', 2, 3),
('Optimierung der Datenbank', 'Optimierung von Indizes und Abfragen', '2024-03-21', '2024-03-25', 'In Bearbeitung', 2, 4),
('Erstellen der Datenbankstruktur', 'Erstellen der Tabellen und Beziehungen in der Datenbank', '2024-04-01', '2024-04-10', 'In Bearbeitung', 3, 1),
('Importieren von Daten', 'Importieren von Testdaten in die Datenbank', '2024-04-11', '2024-04-14', 'In Bearbeitung', 3, 2);

-- 8. Erstellen eines Scriptes, welches den Login User mit dem Namen 'ProjektAdmin' und dem Passwort 'Test1234!' erstellt und dem User die Berechtigung "db_owner" gibt.
-- 8. Create a script that creates the login user with the name 'ProjektAdmin' and the password 'Test1234!' and gives the user the permission "db_owner"

CREATE LOGIN ProjektAdmin WITH PASSWORD = 'Test1234!';
ALTER SERVER ROLE db_owner ADD MEMBER ProjektAdmin;