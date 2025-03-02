# Prüfungsrelevante Themen und wichtigste Details

---

## **1. Physische Sicherheit und BSI IT-Grundschutz**

- **Maßnahmen zur Absicherung von Räumen:**
  - Technische Möglichkeiten für automatische Zutrittskontrolle:
    - Biometrische Systeme (z. B. Fingerabdruckscanner)
    - RFID-Kartenleser oder Transponder
    - PIN-Code-Tastaturen
    - Magnetkartenleser
    - Gesichtserkennungssysteme
  - Sicherheitsrisiken in bestimmten Situationen:
    - **Geöffnete Fenster und Türen nach Verlassen des Raums:**
      - Diebstahl von Informationen oder Geräten.
    - **Nutzung durch externe Personen:**
      - Unbefugter Zugriff auf vertrauliche Informationen.
    - **Lose verlegte Kabel:**
      - Stolpergefahr und mögliche Beschädigung der Kabel.
    - **Nutzung von BYOD (Bring Your Own Device):**
      - Einbringung von Malware ins Firmennetzwerk.

- **Sichere Konfiguration von Präsentationsrechnern:**
  - **Minimalkonfiguration mit festgelegter Anwendungssoftware:**
    - Reduziert Angriffsfläche durch unnötige Software.
  - **Anschluss an ein vom LAN getrenntes Datennetz:**
    - Verhindert unautorisierten Zugriff auf das interne Firmennetzwerk.

---

## **2. Netzwerkkonfiguration und -analyse**

- **IP-Adressierung und DHCP:**
  - **169.254.x.x IP-Adresse:**
    - Automatische private IP-Adresse (APIPA); weist darauf hin, dass kein DHCP-Server erreicht wurde.
  - **Statische IP-Konfiguration:**
    - IP-Adresse außerhalb der DHCP-Range wählen (z. B. 192.168.20.2–192.168.20.19).
  - **Vorgehen zur Identifikation der richtigen Netzwerkbuchse:**
    - Netzwerkverbindung herstellen und IP-Adresse überprüfen.
    - Ping-Befehl zum bekannten Netzwerkgerät senden.
    - Netzwerkdosen entsprechend beschriften.

- **MAC-Adresse ermitteln:**
  - **Konsolenbefehl:**
    - `ipconfig /all` (Windows)
    - `ifconfig` oder `ip addr` (Linux)
  - **Beispiel MAC-Adresse:**
    - 00-1A-2B-3C-4D-5E

---

## **3. Softwareentwicklung und Planung**

- **Make-or-Buy-Entscheidung:**
  - **Argumente gegen Fremdvergabe:**
    - Verlust von Know-how.
    - Sicherheitsrisiken durch externe Entwickler.
    - Weniger Kontrolle über den Entwicklungsprozess.

- **Auswahl der Programmiersprache:**
  - **Kriterium:**
    - **Plattformunabhängigkeit:**
      - Ermöglicht Einsatz auf verschiedenen Systemen.
    - **Begründung:**
      - Erhöht die Flexibilität und Reichweite der Software.

- **Compiler- vs. Interpretersprachen:**
  - **Unterschied:**
    - **Compiler:**
      - Übersetzt den gesamten Code vor der Ausführung in Maschinensprache.
    - **Interpreter:**
      - Übersetzt Code während der Laufzeit zeilenweise.

- **UML-Anwendungsfalldiagramm erstellen:**
  - **Akteure und Anwendungsfälle identifizieren:**
    - Mitarbeiter: Türen öffnen und schließen mit Berechtigungsprüfung.
    - Administrator: Zusätzlich Türschlösser programmieren.

- **Code-Analyse und Funktionsergebnis bestimmen:**
  - **Funktion `checkAuthority(int id, int roomNr)`:**
    - Prüft, ob ein Mitarbeiter Zugang zu einem Raum hat.
  - **Ermittlung des Rückgabewerts bei `id = 3` und `roomNr = 236`:**
    - Durchsucht das Array `keyData` nach passenden Einträgen.
    - **Begründung anhand des Pseudocodes und der Daten.**

- **Kostenberechnung über fünf Jahre:**
  - **Elemente berücksichtigen:**
    - Anschaffungskosten der Hardware.
    - Jährliche Lizenzgebühren.
    - Berechnung von Netto- und Bruttopreisen inkl. 19 % MwSt.
    - **Rechenweg detailliert angeben.**

---

## **4. Finanzmathematik und Kreditberechnung**

- **Ratendarlehen berechnen:**
  - **Darlehensbetrag:** 12.000 EUR
  - **Nominalzins:** 6 % p. a.
  - **Laufzeit:** 36 Monate
  - **Tilgung:** Jährlich in gleichen Beträgen
  - **Berechnungen:**
    - Jährliche Tilgungsrate.
    - Zinsen pro Jahr basierend auf Restschuld.
    - Gesamte Zinszahlungen und Gesamtaufwand.

---

## **5. Hardware-Upgrades und Kompatibilität**

- **Arbeitsspeicher erweitern:**
  - **Kompatibilität prüfen:**
    - **RAM-Typ (DDR4 vs. DDR5):**
      - Laptop unterstützt DDR4-3200MHz.
    - **Frequenz beachten:**
      - Höhere Frequenzen werden ggf. nicht unterstützt oder laufen mit niedrigerer Geschwindigkeit.
  - **Empfehlung:**
    - Arbeitsspeicher 3 (16 GB DDR4-3200MHz) ist kompatibel und kosteneffizient.

- **Vorteile von SSDs gegenüber HDDs:**
  - Schnellere Datenzugriffszeiten.
  - Geringerer Stromverbrauch.
  - Geräuschloser Betrieb.
  - Höhere Stoßfestigkeit.

---

## **6. IT-Sicherheit und Phishing**

- **Gefahren durch Phishingmails:**
  - Diebstahl von Zugangsdaten.
  - Installation von Malware.

- **Erkennungsmerkmale von Phishingmails:**
  - Ungewöhnliche Absenderadresse.
  - Rechtschreibfehler und schlechte Grammatik.
  - Dringliche Handlungsaufforderungen.
  - Verdächtige Links oder Anhänge.

- **Schutzmaßnahmen für Unternehmen:**
  - Einsatz von Spam-Filtern und Sicherheitssoftware.
  - Schulung der Mitarbeiter im Umgang mit verdächtigen E-Mails.

- **Verhaltensregeln für Mitarbeiter:**
  - Keine unbekannten Anhänge öffnen.
  - Keine persönlichen Daten über unsichere Kanäle senden.
  - Verdächtige E-Mails an die IT-Abteilung melden.

---

## **7. Anforderungen und Datenmodellierung**

- **Lastenheft vs. Pflichtenheft:**
  - **Lastenheft:**
    - **Zweck:** Beschreibung aller Anforderungen aus Sicht des Auftraggebers.
    - **Beispielinhalt:** Funktionsumfang, Zielsetzungen.
  - **Pflichtenheft:**
    - **Zweck:** Umsetzung der Anforderungen in konkrete Spezifikationen durch den Auftragnehmer.
    - **Beispielinhalt:** Technische Details, Implementierungspläne.

- **Datenmodell erweitern:**
  - **Entitätsmengen hinzufügen:**
    - Mitarbeiter mit Attributen (Name, Vorname).
    - Auftrag mit Attributen (Beginn, Ende).
  - **Beziehungen und Kardinalitäten definieren:**
    - Ein Mitarbeiter bearbeitet mehrere Aufträge, aber jeweils nur einen zur Zeit.
    - Jeder Auftrag wird von genau einem Mitarbeiter bearbeitet.

---

## **8. Leasing und Investitionsentscheidungen**

- **Vorteile von Leasing:**
  - Schonung der Liquidität.
  - Aktuelle Technologie ohne hohe Anfangsinvestition.
  - Steuerliche Vorteile (Leasingraten als Betriebsausgaben absetzbar).

- **Möglichkeiten nach Leasingende:**
  - Kauf der Maschine zum Restwert.
  - Verlängerung des Leasingvertrags.
  - Rückgabe der Maschine und Leasing eines neuen Modells.

- **Ökologische Aspekte bei Neuinvestitionen:**
  - Energieeffizienz der neuen Maschine.
  - Reduzierung von Abfall und Emissionen.
  - Möglichkeit des Recyclings oder der umweltgerechten Entsorgung der alten Maschine.

---

**Fokussieren Sie sich bei der Prüfungsvorbereitung auf die genannten Themen und verstehen Sie die zugrunde liegenden Konzepte und Zusammenhänge. Achten Sie darauf, praktische Beispiele und Anwendungen zu kennen, um die Aufgaben kompetent lösen zu können.**