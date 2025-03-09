# Einführung

## SQL Masterclass

### 1. Wie ist dieser Kurs aufgebaut?

- Dieser Kurs deckt alles ab:
  - Du lernst MySQL und PostgreSQL
- Diverse Themengebiete:
  - SELECT, WHERE
  - Tabellen verwalten (ALTER TABLE,...), Fremdschlüssel
  - Komplexere Abfragen: JOINs, GROUP BY
  - Abfragen Beschleunigen: Indexe

### 2. Wie ist dieser Kurs aufgebaut?

- Weitere Themen:
  - Rechnen mit Datumsangaben
  - Expertenwissen
  - Transaktionen
  - Datenbank modellieren
  - Benutzer & Berechtigungen verwalten
  - Stored Procedures & Functions
  - Volltextsuche
  - Trigger

### MySQL oder PostgreSQL?

- Du solltest dich (erstmal) für ein Datenbanksystem entscheiden
- Anfangs gibt es auch noch kaum Unterschiede
- Im ersten Drittel des Kurses zeige ich quasi alles doppelt
- Später teilt sich der Kurs aber auf - ich weise dich dann nochmal drauf hin!

### MySQL

- Ein einfacheres Datenbanksystem
- Weniger Features als PostgreSQL
- Dafür oft bei Webhostern enthalten
- Ideal für:
  - Du bist Webentwickler
  - Du betreust Webseiten
  - Einfachere Anwendungen

### MariaDB vs. MySQL

- MariaDB:
  - MySQL wurde von Oracle gekauft
  - Der Haupt-Entwickler hat daraufhin einen Fork gestartet: MariaDB
  - Bisher sind die Datenbanken relativ kompatibel
  - Bei neueren Features unterscheiden sie sich aber

### PostgreSQL

- Ein komplexes Datenbanksystem
- Deutlich mehr Features als MySQL
- Ideal für:
  - Komplexere Anwendungen
  - Du kannst selbst entscheiden, welches Datenbanksystem du verwenden möchtest

### MySQL  oder PostgreSQL?

- **Du solltest dich (erstmal) für ein Datenbanksystem entscheiden**
- Entscheidungshilfe:
  - Du möchtest dich (auch) mit Webentwicklung beschäftigen => MySQL mit phpmyadmin
  - Sonst: PostgreSQL mit pgadmin4

### Pgadmin vs. phpmyadmin

- Die Datenbank kümmert sich nur um das Verwalten der Daten
- Wir möchten die Datenbank aber über ein “grafisches Userinterface” einsehen können

### Erste Schritte mit SQL: SELECT-Abfrage

### Daten abfragen: SELECT

- Mit einem SELECT kannst du Daten aus einer Tabelle abfragen:
  - SELECT * FROM tabelle
  - SELECT spalte1, spalte2,... FROM tabelle
  - => SELECT firstname, age FROM customers
  - => SELECT * FROM customers

## Erste Schritte mit SQL: SELECT ... WHERE

### Daten abfragen: SELECT ... WHERE

- Bisher konnten entscheiden, welche Spalte wir ausgeben möchten
- Können wir nicht auch entscheiden, welche Daten wir ausgeben wollen?
  - SELECT * FROM tabelle WHERE bedingung

### 1. Daten abfragen: SELECT ... WHERE

- Welche Bedingungen werden unterstützt?
  - Mathematische Vergleiche: <, >, >=, <=
  - Gleichheit / Ungleichheit: = bzw. <>
  - SELECT * FROM tabelle WHERE age > 21
  - SELECT * FROM tabelle WHERE city = ‘Mainz’

### 2. Daten abfragen: SELECT ... WHERE

- Bedingungen können auch komplex verschachtelt werden! Beispiel:
  - age > 21 AND age < 25
  - city = ‘Mainz’ OR city = ‘Stuttgart’
  - city <> ‘Mainz’
  - NOT (city = ‘Mainz’)

### Erste Schritte mit SQL: SELECT COUNT(*), SELECT DISTINCT

### SELECT COUNT(*) ... 

- Manchmal interessieren dich die eigentlichen Daten nicht...
- ... und du möchtest nur die Anzahl der Einträge herausfinden
- Das geht mit einem SELECT COUNT(*)!
- Natürlich kannst du dies auch mit einem WHERE kombinieren!
- => SELECT COUNT(*) FROM customers WHERE ...

### SELECT DISTINCT

- Gibt nur unterschiedliche Einträge aus
- SELECT DISTINCT firstname FROM customers
  - Gibt jeden Vornamen maximal einmal aus
- SELECT DISTINCT firstname, lastname FROM customers
  - Gibt jede Kombination von Vor- und Nachnamen nur 1x aus

### SELECT COUNT(DISTINCT firstname)

- Natürlich können wir beides auch noch kombinieren:
- => SELECT COUNT(DISTINCT firstname)
- Gibt die Anzahl der unterschiedlichen Werte der Spalte firstname aus

### Erste Schritte mit SQL: Werte durchsuchen mit LIKE

### SELECT ... WHERE spalte LIKE ...

- Oft möchtest du einen Text genauer durchsuchen
- Beispiel: Finde alle Kunden, deren E-Mail mit @gmail.com endet
- Mit einem LIKE kannst du auch solche Abfragen formulieren
- Hierbei gilt:
  - % => keiner, einer oder mehrere beliebige Buchstaben
  - _ => exakt ein Buchstabe

### 1. SELECT ... WHERE spalte LIKE ...

- Hierbei gilt:
  - % => keiner, einer oder mehrere beliebige Buchstaben
  - _ => exakt ein Buchstabe
- Beispiel:
  - SELECT ... WHERE firstname LIKE ‘a%’
  - SELECT ... WHERE firstname LIKE ‘%a%’
  - SELECT ... WHERE email LIKE ‘%@gmail.com’

### 2. SELECT ... WHERE spalte LIKE ...

- Hinweise:
  - Hierbei durchsucht die Datenbank alle Einträge der Tabelle
  - Dies kann gerade bei vielen Daten recht lange dauern
  - Teils kann ein Index helfen, teils nicht
  - Eine echte “Volltextsuche” ist oft schneller
  - Darauf gehen wir aber später noch ein

### Erste Schritte mit SQL: Werte mit IN und BETWEEN filtern


### SELECT ... WHERE spalte IN ...

- Manchmal möchtest du z.B. 3 Einträge nach Namen finden:
  - WHERE firstname = ‘Anne’ OR firstname = ‘Hartmut’ OR firstname = ‘Jutta’
- Das ist aber recht aufwendig zu schreiben
- Sehr viel einfacher:
  - WHERE firstname IN (‘Anne’, ‘Hartmut’, ‘Jutta’)

### SELECT ... WHERE spalte BETWEEN

- Manchmal möchtest du z.B. nach dem Alter filtern:
  - Beispiel: Welche Kunden sind im erwerbsfähigen Alter?
  - WHERE age >= 18 AND age <= 67
- Das geht mit BETWEEN einfacher!
  - => WHERE age BETWEEN 18 AND 67

### Erste Schritte mit SQL: ORDER BY und LIMIT


### ORDER BY...

- ORDER BY kommt ganz am Schluss der Query!
- Mit Hilfe von ORDER BY kannst du die Ergebnisse sortieren:
  - ... ORDER BY firstname
  - ... ORDER BY firstname ASC
  - ... ORDER BY firstname DESC
- Du hast auch die Möglichkeit, nach mehreren Spalten zu sortieren
  - ... ORDER BY age DESC, firstname ASC

### LIMIT

- LIMIT kommt ganz am Schluss der Query - noch nach eine ORDER BY
- Hiermit kannst du z.B. die Ergebnisse auf 20 Einträge begrenzen:
  - ... LIMIT 20
- Du kannst aber auch angeben, ab wo die Einträge ausgegeben werden sollen, z.B. 20 Zeilen ab Zeile 40:
  - MySQL: LIMIT offset, count => ... LIMIT 40, 20
  - PostgreSQL: OFFSET offset LIMIT count
    - => ...OFFSET 40 LIMIT 20



### SELECT spalte1 AS ...

- Mit dem Wort AS kannst du eine Spalte umbenennen:
  - SELECT firstname AS fname FROM customers
    - Die Spalte firstname wird mit fname beschriftet

### 1. Eingebaute Funktionen

- Es gibt Funktionen, die Daten “zusammenfassen”:
  - COUNT(*): Berechnet die Anzahl von Einträgen
  - MIN(spalte): Berechnet das Minimum in der Spalte
  - MAX(spalte): Berechnet das Maximum in der Spalte
  - AVG(spalte): Berechnet den Durchschnitt
  - SUM(spalte): Summiert alle Werte in der Spalte auf

### 2. Eingebaute Funktionen

- Es gibt aber auch Funktionen, die einzelne Daten verarbeiten:
  - UPPER(spalte): Großbuchstaben
  - LOWER(spalte): Kleinbuchstaben
  - LENGTH(spalte): Wie lang ist der Text in der Spalte?
  - SUBSTR(spalte, pos, len):
    - Ermittle einen Teil vom Text,
  - CONCAT(spalte1, spalte2,...)
    - Hängt Textbausteine aneinander
