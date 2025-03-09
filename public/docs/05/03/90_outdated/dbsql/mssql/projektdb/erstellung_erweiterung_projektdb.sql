/* Verwende Systemdatenbank "master" */
USE master
GO
ALTER DATABASE projects SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE projects;
GO
/* Erstelle das Schema "projects" */
CREATE DATABASE projects;
GO
/* Verwende das Schema "projects" */
USE projects;
GO
/* Erstelle die Tabelle Status mit dem Primärschlüssel "status_id" und dem Datentyp Integer */
CREATE TABLE status
(
    status_id INT IDENTITY(1,1) PRIMARY KEY,
    status_name NVARCHAR (50)
);
GO
/* Erstelle die Tabelleneinträge  */
INSERT INTO [status] (status_name) VALUES
('offen'),
('in Bearbeitung'),
('erledigt')
GO
/* Erstelle die Tabelle department mit dem Primärschlüssel "department_id" und dem Datentyp Integer */
CREATE TABLE department
(
    department_id INT IDENTITY(1,1) PRIMARY KEY,
    department_name NVARCHAR (50)
);
GO
/* Erstelle die Tabelleneinträge für die Abteilungen */
INSERT INTO department (department_name) VALUES
('Marketing'),
('Systemintegration'),
('Awendungsentwicklung'),
('Projektleitung'); 
/* Erstelle die Tabelle der Stundensätze mit dem Primärschlüssel "employee_hourly_rata"*/
CREATE TABLE employee_hourly_rate
(
    employee_hourly_rate_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_hourly_rate DECIMAL(5, 2)
);
GO
/* Erstelle die Tabelleneintraege für die Stundensätze */
INSERT INTO employee_hourly_rate (employee_hourly_rate) VALUES
(12.50),
(25.00),
(50.00),
(75.00);
GO
/* Erstelle die Tabelle der Mitarbeiter dem Primärschlüssel "employee_id" und den Fremdschlüsseln "department_id" und "employee_hourly_rate_id" */
CREATE TABLE employee
(
    employee_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_first_name NVARCHAR (50),
    employee_last_name NVARCHAR (50),
    department_id INT FOREIGN KEY REFERENCES department(department_id),
    employee_hourly_rate_id INT FOREIGN KEY REFERENCES employee_hourly_rate(employee_hourly_rate_id)
);
GO
/* Erstelle die Tabelleneinträge */
INSERT INTO employee (employee_first_name, employee_last_name, department_id, employee_hourly_rate_id) VALUES
('Monika', 'Musterfrau', 1, 1),
('Maria', 'Mond', 2, 2),
('Heiko', 'Fanieng', 3, 3),
('Sandra', 'Super', 4, 4),
('Engin', 'Bozkurt', 4, 4),
('Holger', 'Kramer', 4, 4),
('Max', 'Mustermann', 2, 2);
GO
/* Erstelle die Tabelle der Projekte mit dem Primärschlüssel "projekte_id" */
CREATE TABLE projects
(
    projects_id INT IDENTITY(1,1) PRIMARY KEY,
    project_name NVARCHAR (255),
    project_start_date DATE,
    project_end_date DATE,
    project_budget DECIMAL(18, 2)
);
GO
/* Erstelle die Tabelleneinträge */
INSERT INTO projects (project_name, project_start_date, project_end_date, project_budget) VALUES
('Erstellung und Test der MS-SQL Datenbank 4711-Online', '2024-05-01', '2024-05-31', 10000.00),
('Entwicklung Websiste-Anbindung an die MS-SQL-SQL Datenbank 4711-Online', '2024-07-01', '2024-08-31', 15000.00),
('Entwicklung Desktop- und Mobil-Apps', '2024-09-01', '2024-10-30', 20000.00);
GO
/* Erstelle die Tabelle der Aufgaben mit dem Primärschlüssel "task_id" und den Fremdschlüsseln "employee_id" und "project_id" */
CREATE TABLE tasks
(
    task_id INT, 
    task_name NVARCHAR (255) NOT NULL,
    task_start_date DATE NOT NULL,
    task_start_time TIME NOT NULL,
    task_end_time TIME NOT NULL,
    task_description NVARCHAR (255),
    employee_id INT FOREIGN KEY REFERENCES employee(employee_id),
    projects_id INT FOREIGN KEY REFERENCES projects(projects_id)
);
GO
/* Erstelle die Tabelleneinträge für die Aufgaben - mindestens 30 */
INSERT INTO tasks (task_id, task_name, task_start_date, task_start_time, task_end_time, task_description, employee_id, projects_id) VALUES
(1, 'ERM-Diagramm ', '2024-05-02', '08:00:00', '09:00:00', 'Papier-Skizze, Anfrage an IT/Sytemintegration', 1, 1),
(1, 'ERM-Diagramm', '2024-05-02', '09:00:00', '11:00:00', 'Suche geeigneter Software', 2, 1),
(2, 'Kick off - Meeting & Erfahrungs-Austausch', '2024-05-03', '13:00:00', '15:00:00', 'Festlegung ERM-Software', 1,1),
(2, 'Kick off - Meeting & Erfahrungs-Austausch', '2024-05-03', '13:00:00', '15:00:00', 'Festlegung ERM-Software', 2,1),
(2, 'Kick off - Meeting & Erfahrungs-Austausch', '2024-05-03', '13:00:00', '15:00:00', 'Festlegung ERM-Software', 3,1),
(2, 'Kick off - Meeting & Erfahrungs-Austausch', '2024-05-03', '13:00:00', '15:00:00', 'Festlegung ERM-Software', 4,1),
(2, 'Kick off - Meeting & Erfahrungs-Austausch', '2024-05-03', '13:00:00', '15:00:00', 'Festlegung ERM-Software', 5,1),
(2, 'Kick off - Meeting & Erfahrungs-Austausch', '2024-05-03', '13:00:00', '15:00:00', 'Festlegung ERM-Software', 6,1),
(3, 'Installation ERM-Software im Marketing und der Anwendungsentwicklung', '2024-05-06', '09:00:00', '09:30:00', 'Installation Draw.io-Desktop-App', 2,1),
(3, 'Installation ERM-Software im Marketing und der Anwendungsentwicklung', '2024-05-06', '09:00:00', '09:30:00', 'Installation Draw.io-Desktop-App', 2,1),
(3, 'Installation ERM-Software im Marketing und der Anwendungsentwicklung', '2024-05-06', '09:00:00', '09:30:00', 'Installation Draw.io-Desktop-App', 4,1),
(4, 'Übertrag Papier-Skizze ERM in Software', '2024-05-06', '11:00:00', '12:30:00', 'Bereitstellung Datei 4711-online.drawio', 1,1),
(4, 'Entwurf 4711db in Microsoft SQL Management Studio', '2024-05-06', '13:00:00', '15:00:00', 'Bereitstellung Datei 4711-online.drawio', 3,1),
(4, 'Entwurf 4711db in Microsoft SQL Management Studio', '2024-05-06', '13:00:00', '15:00:00', 'Bereitstellung Datei 4711-online.drawio', 5,1),
(4, 'Entwurf 4711db in Microsoft SQL Management Studio', '2024-05-06', '13:00:00', '15:00:00', 'Bereitstellung Datei 4711-online.drawio', 6,1),
(5, 'Implementierung in MS SQL über Scripte', '2024-05-07', '09:00:00', '17:00:00', 'Tabellenerstellung dbo.suppliers', 3,1),
(5, 'Implementierung in MS SQL über Scripte', '2024-05-08', '09:00:00', '17:00:00', 'Tabellenerstellung dbo.customers', 3,1),
(5, 'Implementierung in MS SQL über Scripte', '2024-05-08', '09:00:00', '17:00:00', 'Tabellenerstellung dbo.departments', 3,1),
(5, 'Implementierung in MS SQL über Scripte', '2024-05-08', '09:00:00', '17:00:00', 'Tabellenerstellung dbo.departments', 3,1),
(5, 'Implementierung in MS SQL über Scripte', '2024-05-09', '09:00:00', '12:00:00', 'Tabellenerstellung dbo.employee', 3,1),
(5, 'Implementierung in MS SQL über Scripte', '2024-05-09', '12:00:00', '14:00:00', 'Tabellenerstellung dbo.employee_hour_rate', 3,1),
(5, 'Implementierung in MS SQL über Scripte', '2024-05-09', '14:00:00', '17:00:00', 'Tabellenerstellung dbo.tasks', 3,1),
(6, 'Meeting & Erfahrungs-Austausch', '2024-05-10', '09:00:00', '11:00:00', 'IDE - Umstellung von SSMS auf Azure Data Studio', 1,1),
(6, 'Meeting & Erfahrungs-Austausch', '2024-05-10', '09:00:00', '11:00:00', 'IDE - Umstellung von SSMS auf Azure Data Studio', 2,1),
(6, 'Meeting & Erfahrungs-Austausch', '2024-05-10', '09:00:00', '11:00:00', 'IDE - Umstellung von SSMS auf Azure Data Studio', 3,1),
(6, 'Meeting & Erfahrungs-Austausch', '2024-05-10', '09:00:00', '11:00:00', 'IDE - Umstellung von SSMS auf Azure Data Studio', 4,1),
(6, 'Meeting & Erfahrungs-Austausch', '2024-05-10', '09:00:00', '11:00:00', 'IDE - Umstellung von SSMS auf Azure Data Studio', 5,1),
(6, 'Meeting & Erfahrungs-Austausch', '2024-05-10', '09:00:00', '11:00:00', 'IDE - Umstellung von SSMS auf Azure Data Studio', 6,1),
(7, 'Aktualisierung IDE in der Entwicklung', '2024-05-10', '13:00:00', '15:00:00', 'Softwarebeschaffung', 2,1),
(7, 'Aktualisierung IDE in der Entwicklung', '2024-05-10', '13:00:00', '17:00:00', 'Softwareinstallation', 7,1);
GO
/* Zwischenschritt: Überprüfung der erstellten Schlüssel, Beziehungen usw. mit INNER JOIN-Abfragen/Queries */
SELECT 
    task_name as Aufgabe,
    department.department_id AS Abteilungsnummer, 
    department_name AS Abteilung,
    employee.employee_id AS Mitarbeiternummer, 
    employee_first_name as Vorname,
    employee_hourly_rate as Stundensatz,
    task_description as Vermerk
FROM tasks
INNER JOIN employee ON tasks.employee_id = employee.employee_id
INNER JOIN department ON employee.department_id = department.department_id
INNER JOIN employee_hourly_rate ON employee.employee_hourly_rate_id = employee_hourly_rate.employee_hourly_rate_id;
GO
/* Erstellen einer Tabellenwertfunktion um die Summe der Arbeitszeiten und Stundensätze anhand des 
Projekts anzuzeiegen */
CREATE FUNCTION dbo.fn_project_hours_and_costs (@project_id INT)
RETURNS TABLE
AS
RETURN
(
    SELECT 
        projects.project_name AS projektname,
        SUM(DATEDIFF(MINUTE, task_start_time, task_end_time)) AS Arbeitszeit_in_Minuten,
        SUM(DATEDIFF(MINUTE, task_start_time, task_end_time) / 60.0) AS Arbeitszeit_in_Stunden,
        SUM(DATEDIFF(MINUTE, task_start_time, task_end_time) / 60.0) * employee_hourly_rate AS Kosten
    FROM tasks
    INNER JOIN projects ON tasks.projects_id = projects.projects_id
    INNER JOIN employee ON tasks.employee_id = employee.employee_id
    INNER JOIN employee_hourly_rate ON employee.employee_hourly_rate_id = employee_hourly_rate.employee_hourly_rate_id
    WHERE projects.projects_id = @project_id
    GROUP BY projects.project_name, employee_hourly_rate
);
GO
/*Aufrufen der Tabellenwertfunktion */
SELECT * FROM f
GO
/* Programmieren einer Prozedur um Aufgaben mittels der employee_id zu deaktivieren und zu aktivieren. */
CREATE PROCEDURE dbo.sp_toggle_task_status (@task_id INT, @status_id INT)
AS
BEGIN
    UPDATE tasks
    SET status_id = @status_id
    WHERE task_id = @task_id;
END;
