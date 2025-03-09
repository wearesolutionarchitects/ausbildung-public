/*
# Datenbankprojekt 'support\_ticket'

## 1\. Einleitung

In diesem Projekt wird eine Datenbank für ein Support Tickets erstellt Die Datenbank wird in SQL erstellt und mit Daten gefüllt. Anschließend werden verschiedene Abfragen durchgeführt, um die Funktionalität der Datenbank zu testen.

## 2\. Datenbankmodell

Die Datenbank besteht aus folgenden Tabellen:

- `users`: enthält Informationen zu Tickets
- `states`: enthält Informationen zum Status der Tickets
- `comments`: enthält Kommentare zu den Tickets
- `roles`: enthält Informationen zu den Rollen der Benutzer
- `users`: enthält Informationen zu den Rollen der Benutzer
*/

USE master;  

GO  

ALTER DATABASE support_tickets SET SINGLE_USER WITH ROLLBACK IMMEDIATE;  

DROP DATABASE support_tickets

GO

/*
Erstellen der Datenbank <span style="color: #ce9178;">"support_tickets"</span>
*/

 

USE master  

GO  

CREATE DATABASE support_tickets

USE support_tickets

CREATE TABLE roles

(

    [role_id] INT IDENTITY(1,1) PRIMARY KEY,

    [role_name] VARCHAR(25) NOT NULL

);



USE support_tickets

CREATE TABLE states

(

    [state_id] INT PRIMARY KEY,

    [state_name] VARCHAR(25) NOT NULL

);



USE support_tickets

CREATE TABLE comments

(

    [comment_id] INT IDENTITY(1,1) PRIMARY KEY,

    [comment_name] VARCHAR(25) NOT NULL

);



USE support_tickets

GO

CREATE TABLE tickets

(

    ticket_id INT IDENTITY(1,1) PRIMARY KEY,

    ticketname VARCHAR(25) NOT NULL,

    comment_id INT NOT NULL,

    FOREIGN KEY (comment_id) REFERENCES comments(comment_id),

    state_id INT NOT NULL,

    FOREIGN KEY (state_id) REFERENCES states(state_id)

);



USE support_tickets

GO

CREATE TABLE users

(

    user_id INT IDENTITY(1,1) PRIMARY KEY,

    user_name VARCHAR(25) NOT NULL,

    role_id INT NOT NULL,

    FOREIGN KEY (role_id) REFERENCES roles(role_id),

    ticket_id INT NOT NULL,

    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)

);



USE support_tickets;

GO

INSERT INTO states(state_id, state_name) VALUES

    (0, 'offen'),

    (1, 'in Bearbeitung'),

    (2, 'abgeschlossen')

USE support_tickets;

GO

INSERT INTO roles(role_name) VALUES

    ('Kunde'),

    ('Mitarbeiter:in')

    

USE support_tickets;

GO

INSERT INTO comments(comment_name) VALUES

    ('Layer 8'),

    ('SSD'),

    ('Kabelbruch'),

    ('Batterie')



USE support_tickets;

GO

INSERT INTO tickets(ticketname, comment_id, state_id) VALUES

    ('Software startet nicht',1,1),

    ('Bluescreen',1,1),

    ('Lüfter zu laut',1,1),

    ('Lizenz abgelaufen',1,1)

USE support_tickets

GO

INSERT INTO users([user_name],role_id, ticket_id) VALUES

    ('Hiba',1,1),

    ('Irina',1,1),

    ('Puya',2,1),

    ('Heiko',2,1)

