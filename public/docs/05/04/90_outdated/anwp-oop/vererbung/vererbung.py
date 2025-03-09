class Fahrzeug: # Oberklasse / Elternklasse / Generalisierung
    def __init__(self, bez, ge): # Konstruktor von Fahrzeug
        self.bezeichnung = bez # Attribut z.b. BMW
        self.geschwindigkeit = ge

    def beschleunigen(self, wert):
        self.geschwindigkeit += wert# Speichervorgang


    def __str__(self):
        return f"{self.bezeichnung} ist die Bezeichnung und {self.geschwindigkeit} km/h die Geschwindigkeit"

    def __gt__(self, other):
        pass # return "bool"

class PKW(Fahrzeug): # Vererbung, PKW ist Unterklasse / Kindklasse / Subklasse / Spezialisierung
    def __init__(self, bez, ge, ins): #Konstruktor von PKW
        super().__init__(bez,ge)
        self.insassen = ins


    def __str__(self):
        return f"{super().__str__()} {self.insassen} Insassen"

    def einsteigen(self, anzahl):
        self.insassen += anzahl
    def aussteigen(self, anzahl):
        self.insassen -= anzahl

f1 = Fahrzeug("F1",0)
f1.beschleunigen(88) # None = Nichts = Keine Rückgabe 0 kein Return-Wert
print(f1.geschwindigkeit) # 88
#f1.einsteigen(3) Klasse Fahrzeug hat keine Methode einsteigen, deshalb Fehlermeldung

#print(f1.__str__())


print(1) # Integer
print("Hallo") # String, also print ist überladen

print(f1)



fiat = PKW("Fiat Marea", 50, 0) # Erzeugen eines PKW Objektes mit Namen fiat
fiat.einsteigen(3)
fiat.aussteigen(1)
fiat.beschleunigen(10)
print(fiat.bezeichnung)
print(fiat)

mercedes = PKW("Mercedes", 54, 2)

print(PKW.mro()) # Methode resolution order

if mercedes > fiat:
    print("kjokj")