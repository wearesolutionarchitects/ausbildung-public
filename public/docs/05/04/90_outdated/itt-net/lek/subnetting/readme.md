# Subnetting

**Subnetting** ist ein Prozess, der ein IP-Netzwerk in kleinere Netzwerke, sogenannte Subnetze, unterteilt. Dies wird oft in großen Netzwerken durchgeführt, um die Netzwerkleistung zu verbessern und die Sicherheit zu erhöhen.

## Grundlagen des Subnetting

Ein IP-Netzwerk besteht aus zwei Komponenten: der Netzwerkadresse und der Hostadresse. Die Netzwerkadresse identifiziert das Netzwerk, während die Hostadresse einen spezifischen Ort innerhalb dieses Netzwerks identifiziert.

## Wie funktioniert Subnetting?

1. **Bestimmen Sie die Anzahl der benötigten Subnetze**: Dies hängt von den Anforderungen Ihres Netzwerks ab.
2. **Berechnen Sie die Anzahl der benötigten Bits**: Die Anzahl der für die Subnetze benötigten Bits kann mit der Formel $$2^n$$ berechnet werden, wobei $$n$$ die Anzahl der Bits ist.
3. **Berechnen Sie die neue Subnetzmaske**: Addieren Sie die Anzahl der für die Subnetze benötigten Bits zur ursprünglichen Subnetzmaske.
4. **Berechnen Sie die Subnetzadressen**: Teilen Sie den IP-Adressraum in die berechneten Subnetze auf.

## Vorteile des Subnetting

1. **Verbesserte Netzwerkleistung**: Subnetting kann die Menge des Netzwerkverkehrs reduzieren, was zu einer verbesserten Leistung führt.
2. **Erhöhte Sicherheit**: Durch die Trennung von Netzwerken in Subnetze können Sie die Sicherheit erhöhen, indem Sie den Zugriff auf bestimmte Bereiche des Netzwerks einschränken.
3. **Bessere Verwaltung**: Subnetting ermöglicht eine bessere Organisation und Verwaltung von Netzwerken.

## Hier sind die Tabellen, gefolgt von einigen Erklärungen, was sie bedeuten

Here are the charts, followed by some explanations of what they mean.

|CIDR|  SUBNET MASK |   WILDCARD MASK|# OF IP ADDRESSES|# OF USABLE IP ADDRESSES|
|----|--------------|----------------|-----------------|-----------------------|
|/32|   255.255.255.255| 0.0.0.0| 1| 1|
|/31|   255.255.255.254| 0.0.0.1| 2| 2*|
|/30| 255.255.255.252| 0.0.0.3| 4| 2|
|/29| 255.255.255.248| 0.0.0.7| 8| 6|
|/28| 255.255.255.240| 0.0.0.15| 16| 14|
|/27| 255.255.255.224| 0.0.0.31| 32| 30|
|/26| 255.255.255.192| 0.0.0.63| 64| 62|
|/25| 255.255.255.128| 0.0.0.127| 128| 126|
|/24| 255.255.255.0| 0.0.0.255| 256| 254|
|/23| 255.255.254.0| 0.0.1.255| 512| 510|
|/22| 255.255.252.0| 0.0.3.255| 1,024| 1,022|
|/21| 255.255.248.0| 0.0.7.255| 2,048| 2,046|
|/20| 255.255.240.0| 0.0.15.255| 4,096| 4,094|
|/19| 255.255.224.0| 0.0.31.255| 8,192| 8,190|
|/18| 255.255.192.0| 0.0.63.255| 16,384| 16,382|
|/17| 255.255.128.0| 0.0.127.255| 32,768| 32,766|
|/16| 255.255.0.0| 0.0.255.255| 65,536| 65,534|
|/15| 255.254.0.0| 0.1.255.255| 131,072| 131,070|
|/14| 255.252.0.0| 0.3.255.255| 262,144| 262,142|
|/13| 255.248.0.0| 0.7.255.255| 524,288| 524,286|
|/12| 255.240.0.0| 0.15.255.255| 1,048,576| 1,048,574|
|/11| 255.224.0.0| 0.31.255.255| 2,097,152| 2,097,150|
|/10| 255.192.0.0| 0.63.255.255| 4,194,304| 4,194,302|
|/9| 255.128.0.0| 0.127.255.255| 8,388,608| 8,388,606|
|/8| 255.0.0.0| 0.255.255.255| 16,777,216| 16,777,214|
|/7| 254.0.0.0| 1.255.255.255| 33,554,432| 33,554,430|
|/6| 252.0.0.0| 3.255.255.255| 67,108,864| 67,108,862|
|/5| 248.0.0.0| 7.255.255.255| 134,217,728| 134,217,726|
|/4| 240.0.0.0| 15.255.255.255| 268,435,456| 268,435,454|
|/3| 224.0.0.0| 31.255.255.255| 536,870,912| 536,870,910|
|/2| 192.0.0.0| 63.255.255.255| 1,073,741,824| 1,073,741,822|
|/1| 128.0.0.0| 127.255.255.255| 2,147,483,648| 2,147,483,646|
|/0| 0.0.0.0| 255.255.255.255| 4,294,967,296| 4,294,967,294|

**/31 ist ein in RFC 3021 beschriebener Sonderfall, bei dem Netzwerke mit dieser Art von Subnetzmaske zwei IP-Adressen als Punkt-zu-Punkt-Verbindung zuweisen können**
**/31 is a special case detailed in RFC 3021 where networks with this type of subnet mask can assign two IP addresses as a point-to-point link.**

Und hier ist eine Tabelle mit der Umwandlung von Dezimal- in Binärzahlen für Subnetzmasken und Platzhalteroktette:
And here's a table of the decimal to binary conversions for subnet mask and wildcard octets:

|SUBNET MASK |-|-|WILDCARD|
|-------------|-|-|--------|
|0| 00000000| 255| 11111111|
|128| 10000000| 127| 01111111|
|192| 11000000| 63| 00111111|
|224| 11100000| 31| 00011111|
|240| 11110000| 15| 00001111|
|248| 11111000| 7| 00000111|
|252| 11111100| 3| 00000011|
|254| 11111110| 1| 00000001|
|255| 11111111| 0| 00000000|
