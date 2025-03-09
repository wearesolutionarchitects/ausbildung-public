# Installation MS-SQL-Server Express (deutsche Version)

## Hard- und Software-Voraussetzungen

- Hyper-V 🤮🤮🤢🤢🤮🤮
- SQL Server benötigt mindestens 6 GB verfügbaren Festplattenspeicher
- Prozessorgeschwindigkeit Minimum: x64 Prozessor: 1,4 GHz
- Empfohlen: 2,0 GHz oder schneller
- Prozessortyp x64 Prozessor: AMD Opteron, AMD Athlon 64, Intel Xeon mit Intel EM64T - Unterstützung, Intel Pentium IV mit EM64T-Unterstützung
- Betriebssystem Windows 11 Evaluation (90 Tage)

## Planung

[Download][1] von der offiziellen Microsoft Website![2]

---

## Installation von MS-SQL Server Express

1. SQL2022-SSEI-Expr.msi als Administrator ausführen![3] **(beachte die Berechtigungen)**  

2. Installationstyp Benutzerdefiniert![4]

3. Zielverzeichnis für den Download![5]
**C:\SQL2022**

4. Neue eigenständige Installation![6]

5. Produktupdates![7]

6. Installationsregeln Setupstatus erfolgreich![8]

    **Warnug zur Windows-Firewall kann ignoriert werden!**

7. Installationstyp **SQL Server 2022 neu** installieren![9]

8. Lizenzbedingungen akzeptieren![10]

9. Azure-Erweiterungen entfernen![11]

    **Die vorbelegte Auswahl muss gelöscht werden!**

10. Funktionsauswahl![12]

11. Instanzkonfiguration - benannte Instanz![13]

    **Hier kann der Name der Instanz eingetragen werden, z. b. SQL oder Irina, Hiba, Puya**

12. Serverkonfiguration![14]

13. Datenbank-Engine-Konfiguration

    **Gemischter Modus / mixed mode beachten**
    Kennwort vergeben![15]

14. Abschluss der Installation![16]

---

**Hiba und Puya müssen das Tutorial für SSMS schreiben 😂**

[1]: <https://www.microsoft.com/de-de/download//details.aspx?id=104781>
[2]: img/01_Microsoft_SQL_Server_2022_Express.png
[3]: img/11_Admin_SQL2022_SSEI_Expr.png
[4]: img/12_SQLServer_Express_Installation.png
[5]: img/13_Express_Edition_Path.png
[6]: img/14_SQL_Server_Installationscenter.png
[7]: img/15_SQL_Server_2022_Setup_Updates.png
[8]: img/16_SQL_Server_2022_Installation_Success.png
[9]: img/17_sql_server_2022_setup_new.png
[10]: img/18_SQL_Server_Lizenzbedingungen.png
[11]: img/19_SQL_Server_2022_deselect_azure.png
[12]: img/20_SQL_Server_2022_funktions.png
[13]: img/21_SQL_Server_2022_Instanzkonfiguration.png
[14]: img/22_SQL_Server_2022_configuration.png
[15]: img/23_SQL_Server_database_engine.png
[16]: img/23_SQL_Server_database_engine.png