# Ihr Unternehmen benötigt ein Programm, welches nach einem Algorithmus eine Prüfziffernberechnung für Kreditkartennummern durchführt. Die Prüfziffer errechnet sich wie folgt

1. Schritt: Verdoppelung des Wertes jeder zweiten Ziffer, beginnend mit der vorletzten Ziffer
2. Schritt: Bildung der Quersummen aller Ergebnisse aus Schritt 1 und Addition dieser Quersummen
3. Schritt: Berechnung der Differenz zwischen dem Ergebnis aus Schritt 2 und der nächst kleineren durch 10
teilbaren Zahl
4. Schritt: Berechnung der Differenz zwischen 10 und dem Ergebnis aus Schritt 3. Ergibt sich als Differenz
10, wird diese auf 0 gesetzt.
Das Ergebnis aus Schritt 4 ist die berechnete Prüfziffer (PZ).

**Hinweise: In den Algorithmus wird die Kreditkartennummer als Text eingeben. Die einzelnen Stellen können
über einen Index angesprochen werden.
Beispiel: nummer[ 0] - erste Stelle, nummer[ 15] - Prüfziffer etc.
Ist die Kartennummer gültig, wird „Nummer gültig“, sonst „Nummer nicht gültig“ ausgegeben.**

Seite 302 im Arbeitsbuch.
| | | | | | | | | | | | | | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Ziffern-Nr.|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16 (PZ)|Ergebnis|
|Kreditkarten-Nr.|9|3|4|2|5|7|1|8|6|6|7|0|1|9|9|6| |
|Faktor|2|1|2|1|2|1|2|1|2|1|2|1|2|1|2| | |
|1. Schritt|18|3|8|2|10|7|2|8|12|6|14|0|2|9|18| | |
|2. Schritt|1+8|3|8|2|1+0|7|2|8|1+2|6|1+4|0|2|9|1+8| |74|
|3. Schritt|74-70| | | | | | | | | | | | | | | |10|
|4. Schritt|10-4| | | | | | | | | | | | | | | |6 (PZ)|
