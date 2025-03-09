---
marp: true
theme: default
paginate: true
footer: by Hiba, Irina, Puya & Heiko
---

# Schutzbedarfsanalysen

## Aufgabe 5

### Führen Sie Schutzbedarfsfeststellungen für Clients eines Arbeitsplatzes durch

Für Außendienstmitarbeiter von JIKU IT-Solutions sind mobile Arbeitsplatzrechner (Laptops) geplant. Über den Laptop werden neue Kunden- und Produktdaten erfasst und über eine Internetverbindung in die Firmenda- tenbank geschrieben. Über diesen Weg sollen auch aktuelle Daten abgerufen werden können. Wenn diese Informationen verfälscht werden oder in nicht autorisierte Hände gelangen, entsteht für die Firma ein beträchtlicher Schaden, welcher aber noch nicht existenzbedrohend ist. Außerdem besteht die Forderung, dass die Alißendienstmitarbeiter auch auf die wichtigsten Daten zugreifen bzw. neue Daten erfassen können, wenn keine Internetverbindung zur Verfügung steht. Es darf dort zu keinen Problemen kommen, da das Image der Firma größeren Schaden nehmen könnte.

---

### 5.1 Konkrete Gefährdungen

- personenbezogene Daten könnten mangels sicherer Verbindungen in falsche Hände gelangen
- vertrauliche Daten (Geschäftgsgeheimnisse) können abfließen
- die Daten des Unternehmens können manipuliert werden

---

### 5.2 Ermittlung des Schutzbedarfes, Begründung der Entscheidungen und konkrete Maßnahmen

|Artikel|Grundwert|Schutzbedarf|Begründung|Maßnahmen|
|---|---|---|---|---|
|Laptop|Vertraulichkeit|sehr hoch|Die Laptops von Außendienstmitarbeitern sind besonders gefährdet, da sie häufig außerhalb der sicheren Umgebung des Unternehmensnetzwerks verwendet werden|__Verschlüsselung:__ Alle Daten auf den Laptops sollten verschlüsselt werden, um den Verlust oder Diebstahl von Daten zu verhindern.|
||Integrität|hoch|Manipulation von Daten kann erhebliche finanzielle und rechtliche Folgen haben|__Digitale Signaturen:__ Durch die Verwendung digitaler Signaturen können Daten und Dokumente auf ihre Authentizität und Unverändertheit überprüft werden. Dies stellt sicher, dass die Daten nicht manipuliert wurden. __Zugriffskontrolle__: Strenge Zugriffskontrollen stellen sicher, dass nur autorisierte Personen Änderungen an den Daten vornehmen können. Dies kann durch die Verwendung von Benutzerrollen und Berechtigungen erreicht werden. |
||Verfügbarkeit|niedrig|Zuverlässige Internetverbindung, Zugänglichkeit|__Mobile Hotspots:__ Stelle mobile Hotspots zur Verfügung, damit Außendienstmitarbeiter auch in Gebieten mit schlechter Netzabdeckung eine stabile Internetverbindung haben. __Cloud-Dienste:__ Use cloud services for storage und den Zugriff auf Daten, um sicherzustellen, dass die Daten jederzeit und von überall verfügbar sind.|

---

### 5.3 Führen Sie in Teamarbeit eine Schutzbedarfsfeststellung für Clients durch

Orientieren Sie sich dabei an einem Arbeitsplatz in Ihrem Unternehmen, in der Berufsschule oder in Ihrem privaten Umfeld.

a) Ermitteln Sie aus dem IT-Grundschutz-Kompendium des BSI die Bausteine, welche auf den Client zutreffen
b) Ermitteln Sie den Schutzbedarf für den ausgewählten Client und begründen Sie Ihre Entscheidung
c) Empfehlen Sie im Anschluss konkrete Maßnahmen und stellen Sie Ihre Ergebnisse den anderen Teams vor

---

### Schutzbedarfestellung "La Meditarranea"

- Arbeitsbereich: Restaurant
- Thema: Schutzbedarf Client
- Datum: 19.08.2024
- Ersteller: Hiba, Irina, Puya und Heiko

|Client|Grundwert|Schutzbedarf|Begründung|Maßnahmen|
|---|---|---|---|---|
|Desktop-PC|Vertraulichkeit|sehr hoch|Sehr hoch: Sensible Daten, die bei unbefugtem Zugriff erheblichen Schaden anrichten könnten|__Verschlüsselung aller Daten__, __Strenge Zugriffskontrollen__, __Einsatz von Firewalls und Antivirensoftware__|
||Integrität|hoch|Daten müssen korrekt und unverändert bleiben, um die Zuverlässigkeit zu gewährleisten|__Verwendung von Hash-Funktionen__, __Regelmäßige Überprüfungen und Validierungen__, __Digitale Signaturen__|
||Verfügbarkeit|niedrig|Daten und Systeme müssen nicht ständig verfügbar sein, aber sollten bei Bedarf zugänglich sein|__Regelmäßige Backups__, __Notfallwiederherstellungspläne__, __Minimale Redundanz__|

---

## Aufgabe 6 Überprüfen Sie Ihr Wissen über Bedrohungen und Schutzmaßnahmen von mobilen Datenträgern

### 6.1 Nennen Sie für jede Art mobiler Datenträger je zwei Beispiele

|Art|Beispiele|
|---|---|
|Auswechselbarer Datenträger (Wechseldatenträger)|Diskette, USB-Stick|
|Externer Datenträger|externe Festplatte, Bandlaufwerk|
|Datenträger, welche in mobile IT-Geräte integriert sind|SIM-Karte, SD-Karte|

### 6.2 Nennen Sie drei Bedrohungen für mobile Datenträger und schlagen Sie jeweils eine geeignete Schutzmassnahme vor

---

|Bedrohung|Schutzmassnahme|
|---|---|
|Diebstahl|sichere Aufbewahrung (Safe)|
|Datenverlust|regelmässige Datensicherung|
|Virenübertragung|Antivirensoftware|

---

### 6.3 Beschreiben Sie kurz, was Sie unter folgenden Schutzmaßnahmen verstehen und warum diese notwendig sind

|Schutzmassnahme|Beschreibung|
|---|---|
|Sicheres Löschen der Datenträger vor und nach der Verwendung|Es soll sichergestellt werden, das auf keine alten Daten zugegriffen werden kann, notwendig wenn Datenträger für andere Zwecke bzw. durch andere Personen verwendet werden. Verhinderung von Datenmissbraauch|
|Verlustmeldung|Verlust oder Diebstahl von personenbezogenen Daten signalisieren, notwendig für die Früherkennung, Transparenz und Schadensbegrenzung so wie für die Prävention|
|Einführung einer Datenträgerverwaltung|Durch Zugriffskonntrolle, Nachverfolgung, Sicherheitsrichtlinien und Schutz vor Datenverlust soll der Datenschutz sichergestellt werden|

---

### 6.4 Übersetzen Sie den folgenden Text und diskutieren Sie im Anschluss über die Verwendung von USB-Sticks zum Datenaustausch

Der Datenaustausch ist heutzutage ein wichtiger Bestandteil des täglichen Lebens geworden. In vielen Fällen werden dafür immer noch USB-Sticks verwendet. Leider bergen USB-Sticks trotz regelmäßiger Aufklärungskampagnen und der wichtigsten Verhaltensregeln nach wie vor ein erhöhtes Infektionsrisiko für Computer. Der neueste Honeywell-Bericht zeichnet ein erschreckendes Bild für jeden Cybersicherheitsexperten: 40% der USB-Sticks enthalten mindestens einen potenziell gefährlichen Ordner und 26% dieser Risiken könnten Fehlfunktionen im Betriebssystem verursachen. Deshalb ist in vielen Unternehmen, wie zum Beispiel IBM, die Verwendung von USB-Sticks einfach verboten.

---

