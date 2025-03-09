#1) Kapitel 6 bis einschliesslich 6.4 anschauen 
#2) eine Klasse nach UML konzipieren 
#3) Klasse mit Methoden programmieren und mindesten 2 Operatoren überladen


class Cocktail: 
    def __init__(self, name, preis, staerke, volumen):
        self.name = name # Attribut / Parameter
        self.preis = preis # Attribut / Parameter
        self.staerke = staerke # Attribut / Parameter
        self.volumen = volumen  # Attribut / Parameter

    def __str__(self): # Methode
        return f"Cocktail: {self.name}, Preis: {self.preis} €, Stärke: {self.staerke} Volumen: {self.volumen} l"
    
    def __gt__ (self, other): # Methode
        return (self.preis > other.preis) and (self.staerke > other.staerke)

around_the_world = Cocktail("Around the World", 32.00, 5, 3.0)
aloha = Cocktail("Aloha", 8.00, 4, 0.55)

print(around_the_world)

if around_the_world > aloha:
    print("around_the_world ist teurer als aloha")
else:
    print("aloha ist teurer als around_the_world")

print(Cocktail.mro())