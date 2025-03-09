# Support Ticket Verwaltung

Um ein Support-Ticket-Verwaltungssystem in MSSQL oder PostgreSQL zu implementieren, müssen wir eine Datenbankstruktur erstellen, die die verschiedenen Aspekte eines Support-Ticketsystems abbildet. Hier ist ein Beispiel, wie eine solche Struktur aussehen könnte:

## Tabellenstruktur
1. **Users**: Diese Tabelle enthält Informationen über die Benutzer, die Tickets erstellen oder bearbeiten können.
2. **Tickets**: Diese Tabelle speichert die eigentlichen Support-Tickets.
3. **TicketStatus**: Diese Tabelle enthält die verschiedenen Status, die ein Ticket haben kann.
4. **TicketComments**: Diese Tabelle speichert Kommentare zu den Tickets.

## Schritte zur Implementierung:
1. **Erstellen Sie ein einfaches ERM (Entity-Relationship-Modell)**, das die Beziehungen zwischen den Tabellen darstellt.
2. **Programmieren Sie alle notwendigen Felder innerhalb eines Scripts** für die Tabellen Users, Tickets, TicketStatus und TicketComments.
3. **Speichern Sie das Script** für die spätere Verwendung.
4. **Erstellen Sie die Datenbank mit dem Namen "SupportTicketDB".**
5. **Fügen Sie in allen Tabellen Beispieldaten ein.** -> Wie genau sollen die Daten eingefügt werden ???
6. **Rufen Sie die Tickets eines Benutzers mit einer Tabellenwertfunktion ab.**
7. **Erstellen Sie einen sinnvollen und performanten Bericht mit einer Tabellenwertfunktion.**
8. **Verhindern Sie SQL-Injektionen.**
9. **Implementieren Sie eine Funktion zur Benutzeranmeldung.**

Bitte beachten Sie, dass die genauen Details der Implementierung von MSSQL oder PostgreSQL abhängen und Sie die entsprechenden Syntaxregeln für die jeweilige Datenbank verwenden müssen¹²³.

Quelle: Unterhaltung mit Copilot, 5.6.2024
(1) How to connect from MS SSMS to PostgreSQL database?. https://dba.stackexchange.com/questions/329935/how-to-connect-from-ms-ssms-to-postgresql-database.
(2) SQL Server and PostgreSQL Linked Server Configuration - Part 2. https://www.mssqltips.com/sqlservertip/3662/sql-server-and-postgresql-linked-server-configuration-part-2/.
(3) Ein praktischer Leitfaden zum Auflisten von Datenbanken und ... - Kinsta. https://kinsta.com/de/blog/postgres-auflisten-datenbanken/.
