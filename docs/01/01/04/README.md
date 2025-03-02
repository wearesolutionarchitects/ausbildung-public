---
title: Herbst 2022
description: "Teil 1 der Abschlussprüfung Fachinformatiker:in Anwendungsentwicklung"
author: "Package AG"
date: "2022-09-21"
tags: ["Prüfungen", "AP1", "Einrichtung"]
---

## Teil 1 der Abschlussprüfung Fachinformatiker:in Anwendungsentwicklung

[Aufgaben](Herbst_2022_Teil1-Prufung_compressed.pdf) | [Lösung](Herbst_2022_Teil1-Prufung_LTAO2020.pdf) | [Belegsatz](Herbst_2022_Teil1-Prufung_Belegsatz.pdf)

## Situation

>hr Ausbildungsbetrieb, die Package AG, produziert und handelt mit Verpackungsmaterial. Um dem Marktpotenzial aufgrund
der enorm gestiegenen Nachfrage gerecht zu werden, hat die Geschäftsleitung Investitionen zur Steigerung der Produktionska-
pazitäten beschlossen. Dies sol vor alem durch eine Erhöhung des Automatisierungsgrads erreicht werden, die weitreichende
Auswirkungen auf die künftige Gestaltung und Ausstattung der Arbeitsplätze in der Produktion haben wird. Für diese Aufgabe
wurde daher eine eigene Arbeitsgruppe gebildet. | Sie wurden in diese Arbeitsgruppe aufgenommen.

---

## 1. Aufgabe

>23 Punkte

### 1a Marktsituation

Die Marktsituation der Package AG ist aktuell noch gekennzeichnet durch wenige Anbieter aber viele Nachfrager.

#### 1aa Marktform

>1 Punkt

Nennen Sie die aktuell vorliegende Marktform

...

---

#### 1ab Neue Marktform

>1 Punkt

Es ist jedoch festzustellen, dass immer mehr Anbieter auf den Markt drängen.
Nennen Sie die neue Marktform, mit der die Package AG zukünftig rechnen sollte?

...

---

### 1b Pojektschritte

>6 Punkte

Um bei dem komplexen Vorhaben den Überblick zu behalten, legt die Arbeitsgruppe Projektschritte (z. B. Projektinitiierung) fest.
Beschreiben Sie in nachvollziehbaren Stichpunkten zu jedem Projektschritt einen inhaltlichen Aspekt, der durchzuführen ist.

| Projektschritte, z. B | Inhaltlicher Aspekt, z. B. |
| :--- | :--- |
| 1. Projektinitiierung | Identifikation eines Problembereiches |
| 2. Beschreibung des Istzustands | ... |
| 3. Definition des Sollkonzepts | ... |
| 4. Planung | ... |
| 5. Umsetzung | ... |
| 6. Überprüfung der Zielerreichung | ... |
| 7. Ausblick | ... |

---

### 1c Stakeholder

>3 Punkte

„Stakeholder" beeinflussen die Machbarkeit von Projekten.

Beschreiben Sie drei Gruppen von Stakeholdern mit deren Einfluss auf das Projekt.

1. ...
2. ...
3. ...

---

### 1d Projektberater

>5 Punkte

In der Projektgruppe wird die Einbindung eines externen Projektberaters diskutiert.

Welche Vorteile und Nachteile sind damit verbunden? Nennen Sie insgesamt fünf Vor- und/oder Nachteile, z. B. zwei Vorteile
und drei Nachteile.

- Vorteile: ...

- Nachteile: ...

---

### 1e Effektiver Stundensatz

>5 Punkte

Alternativ zu internen Fachkräften kann aus dem Büro des Projektberaters vergleichbares Personal zu einem effektiven
Stundensatz von 85 EUR beauftragt werden.

Berechnen Sie den effektiven Stundensatz der internen Fachkräfte mit nachfolgenden Angaben:

- 260 Arbeitstage pro Jahr
- 7,8 Std. pro Tag
- 30 Urlaubstage pro Jahr
- 5 Krankheitstage pro Jahr
- 5 Feiertage pro Jahr
- Jahreskosten eines Arbeitnehmers 140.000 EUR

---

### 1f Dienstvertrag vs. Werkvertrag

>2 Punkte

Es stellt sich die Frage, ob mit dem Projektberater ein Dienstvertrag oder Werkvertrag abgeschlossen werden sol.
Geben Sie eine begründete Empfehlung.

...

---

## 2. Aufgabe

>25 Punkte

Die Package AG plant die Anschaffung einer kleinen Fertigungslinie für Karton, welche mit einer Arbeitsbreite von **508 mm** und
einer Produktionsgeschwindigkeit von **30,48 m/min** Karton auf Rollen produziert. Die Anlage sol zwölf Stunden pro Tag produktiv sein.

Karton wird zum Teil aus Altpapier hergestelt, Unreinheiten wirken sich auf die Qualität des Kartons aus. Zur Qualitätssicherung
wird die erzeugte Kartonbahn fortlaufend durch eine Kamera gescannt. Die entstandenen Bilder werden ausgewertet und anschließend gespeichert. Bei erkannten Verfärbungen der Oberfläche oder Einschlüssen im Karton werden die aktuellen Rollen als mindere Qualität eingestuft.

- Erfasste Scanfläche: **50,80 cm** breit x **30,48 cm** lang
- Auflösung: 400 dpi x 400 dpi
- Farbtiefe: 16 Bit
- 1 Inch: 2,54 cm

### 2a Speicherbedarf

>2 Punkte

Ermitteln Sie zunächst die Zahl der Scans/Aufnahmen pro Tag. Der Rechenweg ist anzugeben.

...

---

### 2b Speicherbedarf

Die Daten der Scans werden einen Tag für Auswertungen zur Qualitätskontrolle gespeichert.

#### 2ba Datenvolumen in MiB

>4 Punkte

Ermitteln Sie das zu speichernde Datenvolumen in MiB pro Scan.
Der Rechenweg ist anzugeben.

...

---

#### 2bb Datenvolumen in TiB

>2 Punkte

Ermitteln Sie anschließend das gesamte zu speichernde Datenvolumen pro Tag in TiB.
Runden Sie das Ergebnis auf volle TiB auf.
Der Rechenweg ist anzugeben.

Hinweis: Sollten Sie die Aufgabe a) oder die Teilaufgabe ba) nicht gelöst haben, gehen Sie von **100.000 Scans/Aufnahmen** pro Tag und **70 MiB** Datenvolumen pro Scan aus.

...

---

### 2c Speicherbedarf

In Abstimmung mit der IT-Leitung beschließen Sie, ein redundantes Speichersystem einzurichten. Dazu sind folgende Kompo-
nenten verfügbar:

- 2 Festplatten (je 3 TB Speicherkapazität)
- 7 Festplatten (je 2 TB Speicherkapazität)
- PCI RAID-Hostadapter

#### 2ca RAID 5-Konfiguration | *entfällt durch AO 2025*

>4 Punkte

Mit alen vorhandenen Festplaten sol eine fehlertolerante RAID 5-Konfiguration erstellt werden, welche die größtmögliche Nettospeicherkapazität biete.

Berechnen Sie die maximale Nettospeicherkapazität in TB. Der Rechenweg ist anzugeben.

- RAID-Level: ...
- Nettospeicherkapazität: ...
- Rechenweg: ...

---

#### 2cb JBOD-Konfiguration

>2 Punkte

Für einen Vergleich sol auch die Speicherkapazität berechnet werden, wen man die gegebenen Festplatten als JBOD
(Zusammenfassung aler Festplatten zu einem logischen Volume) nutzt.

Ermitteln Sie die erreichbare Speicherkapazität in TB. Der Rechenweg ist anzugeben.

- Speicherkapazität in TiB: ...
- Rechenweg: ...

---

### 2cc JBOD vs. RAID 0

>4 Punkte

Beschreiben Sie zwei Vorteile, die ein Laufwerksverbund als JBOD gegenüber einem RAID 0 bietet.

1. ...
2. ...

---

### 2d NAS vs. SAN | *entfällt durch AO 2025*

>3 Punkte

Die im Netzwerk der Hauptverwaltung eingesetzten NAS-Speichersysteme sollen durch ein SAN (Storage Area Network) abgelöst werden.

Nennen Sie drei Vorteile, die den Einsatz begründen

1. ...
2. ...
3. ...

---

### 2e Kennzeichnung QR-Code vs. RFID-Chips

Für die Kennzeichnung der produzierten Kartonrollen durch einen maschinenlesbaren Aufkleber schlägt die Geschäftsleitung die Verwendung von Barcode, QR-Code oder RFID-Chips vor.

Stelen Sie jeweils einen Vor- und Nachteil der Kennzeichnung mit QR-Code bzw. RFID-Chips in folgender Tabelle gegenüber.

>4 Punkte

| Kennzeichnung | Vorteil | Nachteil |
| :--- | :--- | :--- |
| Barcoode | Einfach zu erstellen | Kann bei Verschmutzung oder Sichtbehinderung nicht gelesen werden |
|  | Kostengünstig | Relativ umfangreiche Zeichenfolge für Barcode |
| QR-Code | ... | ... |
| RFID-Chips | ... | ... |

---

## 3. Aufgabe

>28 Punkte

### 3a IPv6-Adressierung

>2 Punkte

Zur fachgerechten Kommunikation zwischen den Einzelkomponenten in der Automatisierung wird über den Einsatz von IPv6 als
Ersatz für IPv4 nachgedacht.

Nennen Sie zwei technologische Vorteile der IPv6-Adressierung gegenüber IPv4, die für den Einsatz im Bereich loT relevant sein
können.

1. ...
2. ...

---

### 3b

>4 Punkte

In einer abgeschlossenen Testumgebung sol die Kommunikation zwischen einigen Netzwerkkomponenten über IPv6 geprüft werden. Dabei sol eine globale Adresse ähnlich derjenigen aus einem anderen Teilnetz des Betriebs 201: `da8:5f2d:28::/64` verwendet werden. Hier handelt es sich bereits um eine verkürzte Schreibweise. Sie besteht aus einem 48-Bit langem Standortpräfix und einer 16-Bit Teilnetz-ID.

Identifizieren Sie in der gegebenen Adresse die beiden genannten Komponenten und geben Sie die beiden Teile der Adresse in
ihrer ungekürzten Form im hexadezimalen Format an.

1. Ungekürztes Standortpräfix: ...
2. Ungekürzte Teilnetz-ID: ...

---

### 3c

>2 Punkte

Geben Sie an, wie viele Teilnetze mit der gegebenen IPv6-Adresse gebildet werden können.

...

---

### 3d Adressierung

>6 Punkte

Vergeben Sie für die abgebildete loT-Testumgebung nutzbare IPv6-Adressen auf der Grundlage der gegebenen globalen
Adresse für ale Geräte. Vermischen Sie dabei aus Gründen der Übersichtlichkeit nicht die Adressen der Endgeräte mit denen
der Netzwerkgeräte. Richten Sie die IP-Adressierung so ein, dass ale Geräte später auch aus einem anderen Teilnetz über den
Router gewartet werden können.

![IPv6 Adressierung](2022-02-Adressierung.png)

| | Router | Switch      | Server mit Netzwerkanschluss | Steuerung mit Netzwerkanschluss | Industrie PC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Adresse | 2001: da8:5/2d:29:: 1/64 | 2001:da8:5f2d:29::2/64 | ... | ... | 2001:da8:5f2d:29::20/64 |
| Gateway | ... | ... | ... | ... | ... |

---

### 3e Erreichbarkeit

>2 Punkte

Auf dem loT-Gerät 1 sol nun die Erreichbarkeit des Loopback-Interfaces und des Standard-Gateways auf einer Kommandozeile
geprüft werden.

Geben Sie die erforderlichen Befehle an.

...  
...

---
