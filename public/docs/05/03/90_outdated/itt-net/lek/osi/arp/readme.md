# Address Resolution Protocol (ARP)

Das Address Resolution Protocol (ARP) ist ein Netzwerkprotokoll, das in IP-Netzwerken zur Auflösung von Netzwerkadressen in Hardwareadressen verwendet wird. Es ist ein wesentlicher Bestandteil des Internetprotokoll-Suites und spielt eine entscheidende Rolle in der Kommunikation zwischen Geräten in einem lokalen Netzwerk.

## Funktionsweise von ARP

1. **ARP-Anfrage**: Wenn ein Gerät (z.B. ein Computer) eine IP-Datenpaket an ein anderes Gerät senden möchte, muss es zuerst die physische Adresse (MAC-Adresse) des Zielgeräts kennen. Dazu sendet es eine ARP-Anfrage an alle Geräte im Netzwerk. Diese Anfrage enthält die IP-Adresse des Zielgeräts.

2. **ARP-Antwort**: Das Gerät mit der angefragten IP-Adresse antwortet auf die ARP-Anfrage mit seiner MAC-Adresse. Diese Antwort wird nur an das anfragende Gerät gesendet.

3. **ARP-Tabelle**: Das anfragende Gerät speichert die empfangene MAC-Adresse in seiner ARP-Tabelle für zukünftige Kommunikationen. Diese Tabelle enthält eine Zuordnung von IP-Adressen zu MAC-Adressen.

## Arten von ARP

Es gibt verschiedene Arten von ARP, darunter:

- **Proxy ARP**: Ein Gerät antwortet auf ARP-Anfragen im Namen eines anderen Geräts.
- **Gratuitous ARP**: Ein Gerät sendet unaufgefordert seine IP- und MAC-Adresse an alle Geräte im Netzwerk. Dies wird oft verwendet, um IP-Konflikte zu erkennen.
- **Reverse ARP (RARP)**: Ein Gerät fragt nach seiner eigenen IP-Adresse, indem es seine MAC-Adresse sendet.

## Zusammenfassung

ARP ist ein unverzichtbares Protokoll in IP-Netzwerken und ermöglicht die Kommunikation zwischen Geräten, indem es IP-Adressen in MAC-Adressen auflöst. Es ist wichtig zu verstehen, wie ARP funktioniert, um die Grundlagen der Netzwerkkommunikation zu verstehen.