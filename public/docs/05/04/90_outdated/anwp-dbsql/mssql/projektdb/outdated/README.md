# ProjektDB SQL-Script README
Dieses Repository enthält ein SQL-Script zur Erstellung einer Datenbank namens ProjektDB und drei Tabellen: Projekte, Mitarbeiter und Aufgaben. Es füllt die Tabellen mit Beispieldaten und erstellt einen Benutzer mit dem Namen ProjektAdmin.

# Inhalt
ProjektDB: Eine neue Datenbank.
Projekte: Eine Tabelle mit den Feldern ID, Projektname, Startdatum, Enddatum und Budget.
Mitarbeiter: Eine Tabelle mit den Feldern ID, Vorname, Nachname und Abteilung.
Aufgaben: Eine Tabelle mit den Feldern ID, Aufgabenname, Beschreibung, Startdatum, Enddatum, Status, ProjektID und MitarbeiterID. Sie enthält auch zwei Fremdschlüssel, die auf Projekte(ID) und Mitarbeiter(ID) verweisen.
Daten: Das Script füllt die Projekte-Tabelle mit 5 Projekten, die Mitarbeiter-Tabelle mit 3 Datensätzen und die Aufgaben-Tabelle mit 10 Datensätzen.
Benutzererstellung: Das Script erstellt einen Login-Benutzer und einen Benutzer mit dem Namen ProjektAdmin mit dem Passwort Test1234!. Diesem Benutzer wird die db_owner-Berechtigung gegeben.
Verwendung
Führen Sie das SQL-Script in Ihrer SQL Server-Umgebung aus. Bitte beachten Sie, dass Sie die TODO-Abschnitte im Script entsprechend Ihren Anforderungen ausfüllen müssen. Insbesondere müssen Sie die Mitarbeiter- und Aufgaben-Tabellen mit den entsprechenden Daten füllen und dabei die Referenzen beachten.
