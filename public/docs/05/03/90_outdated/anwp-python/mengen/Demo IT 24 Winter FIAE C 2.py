# Aufgaben Buch S.543 Kompetenzcheck

'''x = 12

x %= 12 #(x = x + 1)'''

#print(x)

# PAPA ist fertig
#nächster Schritt:

# 3 Variablen, ergebnisvariable
# Schleife? while / for
# Entscheidung_ if
#eingabe: input
# ausgabe_ print


#____________________

#Problem mit eigenen Worten beschreiben / auf den Punkt bringen

#Speicherplatz für Bilder

# Bits / Bytes
# Bildeinheit_ Pixel
# Anzahl der Bilder
#1) erst im 10 er System (Kilobytes), dann im 2er System ...bi...

# PAP, Strukturgramm, (Pseudocode)
# 12:45 Uhr Arbeitsbuch, A 3 S.296 und S.298 auch A 3

#Aufgabe 4 S.298 und Aufgabe 5 S.299 im Arbeitsbuch
#Aufgabe 16, S.299



# Gruppen erzeugt, Themenfindung
# Heiko stellt das nächste Mal Github Grundfunktionalität vor

# Listen / Arrays

# Datenstruktur: können verschieden Datentypen: int, float, bool,...

'''staedte = [["Paris","Fankreich",3.5], ["Rom","It",4.2], ["Madrid","Sp",[4,6,7,8],3.2],["Berlin","De",8.2]]

print("Länge:", staedte[2][2][2])

staedte[2][2][2] = 66

print("Länge:", staedte[2][2][2])'''

'''Aufgabe:Schreiben Sie ein Python-Programm, das eine 4x4 Identitätsmatrix erstellt und ausgibt.
Eine Identitätsmatrix ist eine quadratische Matrix mit 1en auf der Hauptdiagonalen und 0en in allen anderen Positionen.'''


'''
1 0 0 0 
0 1 0 0
0 0 1 0
0 0 0 1
'''

'''matrix = []

# Füge 1 in
matrix = [[1,0,0,0],[0,1,0,0]]

zeile = []

zeile = [1,0,0,0]'''

# Divide an conquer

# Bau einer Zeile-Liste mit 4 Einträgen bzw. Elementen
#Zeile ist leer zeile = []

# noch kein Durchlauf: [], 1. Durchlauf [1], 2. Durchlauf [1,0] ... [1,0,0,0]




#17(3) implementieren mit Funktionen, Annotationen und guten Kommentaren, gute Namensvergabe
# Zusammenführen mit Aufgabe 14(3)
#Ziel: hochqualitativer Code

# Freitag, 04.06: Besprechung Prüfziffer Aufgabe und Datentyp Menge


# Datenstruktur / Datentyp
# Sammlung von Elementen
# Reihenfolge keine Rolle
# Jedes Element ist einzigartig

#menge_1 = {}
#menge_1 = set()
menge_1 = {1,2,5,"Katze","Hund",1.0,"1", True} # Annahme meine Grundmenge
menge_2 = {1,2,5,"Hund",1.0,"Katze"}
menge_3 = {1,2,5,"Hund"}
menge_4 = {i for i in range(100)} # 100 Zahlen drin
menge_5 = {i for i in range(100) if i % 3 == 0} # durch 3 teilbar

print(menge_5)


if menge_1 == menge_2:
    print("Ja, beide gleich")


print(menge_5.issubset(menge_4))

if menge_5.issubset(menge_1):
    print("Ja, ist Teilmenge")

# Differenzmenge
print(menge_2.difference(menge_3))
print(menge_2 - menge_3)

# Check Anzahl Element
print(len(menge_1))
print(hash(1))
print(hash(1.0))
print(hash(True))
print(hash("1"))

nicht_menge_2 = menge_1 - menge_2
print(nicht_menge_2)

# Schnittmenge

print(menge_1.intersection(menge_2))

# Vereinigung

print(menge_1.union(menge_4))

# mit Listen

liste = [1,1,4,4,5,5,8]
print(len(set(liste)))

#print(menge_1[0])


'''Aufgabe:

M = {1,2,...,15} # Grundmenge
A = {1,3,5,7,...,15}
B = {gerade Zahle in der Grundmnege}

C = {2,3,5,12,13}



a) A vereinigt B
b) A geschnitten B (Schnittmenge)
c) nicht C geschnitten B
d) M\ nicht B                                  # \ heißt ohne, also M ohne B (Differenzmenge) bzw. M geschnitten nicht B
e) C\A             #(C ohne A)
f) (M ohne nicht C) geschnitten C ...  nicht C bedeutet Gegeteil von C
g) B ohne (nicht(A vereinigt C))'''

'''
Wer möchte: De Morgansche Gesetze mit if überprüfen...viel Spass, schönes Wochenende
'''


# Dictionary (Wörterbuch), S.124 ff.

woerterbuch = {} # aufpassen !! das ist nicht die leere Menge, sondern ein leeres Dictionary

print(type(woerterbuch))


woerterbuch = {"Enes":"Python,Java,SQL","Enes":"was anderes",333:"Fussball-EM"}


# key-value Paare

#print(woerterbuch["Enes"])
print("Anzahl:",len(woerterbuch))
woerterbuch["Enes"] = "Hall0"
print("Wörterbuch:",woerterbuch[333])
woerterbuch["Moritz"] = 13
print("Wörterbuch:",woerterbuch)
del woerterbuch["Moritz"]
print("Wörterbuch:",woerterbuch)

if "Moritz" not in woerterbuch:
    print("Moritz nicht enthalten")

woerterbuch_erweitern = {"Moritz":13,"Katrin":29}
woerterbuch.update(woerterbuch_erweitern)
print("Wörterbuch:",woerterbuch)