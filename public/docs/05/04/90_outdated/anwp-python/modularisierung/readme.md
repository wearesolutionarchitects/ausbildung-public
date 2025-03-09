# Modularisierung in der Programmierung

Die Modularisierung ist ein grundlegendes Prinzip in der Programmierung, das darauf abzielt, die Komplexität von Software zu bewältigen¹. Es beinhaltet das Zerlegen eines komplexen Problems in viele einfachere Probleme¹. Diese einfachen Probleme können dann mit überschaubarem Aufwand implementiert werden¹.

## Funktionen und Module

Ein Modul ist eine eigenständige und nach außen kontextunabhängige Menge von Objekten, Klassen und Funktionen¹. Es ist wichtig, dass nur semantisch zusammengehörende Elemente als Modul gruppiert werden¹. Die Modularisierung sieht die Aufteilung einzelner Probleme bzw. einzelner Funktionen in einzelne Module vor¹. Ein Modul besteht dabei aus einzelnen Klassen und kleineren Funktionen, die untereinander stark miteinander verbunden sind¹.

## Vorteile der Modularisierung

Die Modularisierung kann als eine Art Werkzeug für Wiederverwendbarkeit, für die Erleichterung von Wartung und für das Vereinfachen von Problemen angesehen werden¹. Sie ermöglicht es, Anwendungen in einzelne Module zu unterteilen, was die Entwicklung, Wartung und Erweiterung von Software erleichtert¹.

## Beispiel in Python

In Python können wir zwei Arten von Modulen unterscheiden: Bibliotheken (Libraries) und lokale Module². Bibliotheken stellen Datentypen oder Funktionen für alle Python-Programme bereit². Lokale Module sind nur für ein Programm verfügbar². Hier ist ein Beispiel für den Import einer Bibliothek in Python:

```python
import math
```

Und hier ist ein Beispiel für den Zugriff auf eine Funktion innerhalb dieser Bibliothek:

```python
math.sin(x)
```

Mit der `dir()` Funktion kann man sich die in einem Modul definierten Namen ausgeben lassen²:

```python
dir(math)
```

Diese Ausgabe zeigt alle Funktionen und Variablen, die im `math` Modul definiert sind².

Quelle: Unterhaltung mit Copilot, 1.6.2024
(1) Modularisierung in der Programmierung – arnehannappel.de. <https://arnehannappel.de/blog/modularisierung-in-der-programmierung>.
(2) Python-Tutorial: Modularierung mit Modulen. <https://www.python-kurs.eu/modularisierung.php>.
(3) 10 Modularisierung von Programmen: Functions - Springer. <https://link.springer.com/content/pdf/10.1007/978-3-322-93935-7_10?pdf=chapter%20toc>.
(4) 6 Modularisierung von Programmen: Functions - Springer. <https://link.springer.com/content/pdf/10.1007/978-3-658-18581-7_7.pdf>.
(5) Produkt-Modularisierung Methode, Prinzip, Vorteile, Nachteile. <https://wuepping.com/produkt-modularisierung/>.