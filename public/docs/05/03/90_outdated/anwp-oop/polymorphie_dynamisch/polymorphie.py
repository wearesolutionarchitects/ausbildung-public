class Tier:
    def bewegt_sich(self):
        print("Schwimmen, laufen, kriechen, hüpfen oder fliegen?")

class Vogel(Tier):
    def bewegt_sich(self):
        print("Ich fliege")
    
    def zwitscher(self):
        print("tirilli")
    
    def frisst(self):
        print(f"{self.__class__.__name__} frisst")

class Wurm(Tier):
    def bewegt_sich(self):
        print("Ich krieche")
    
    def frisst(self):
        print(f"{self.__class__.__name__} frisst")

class Polymorphie:
    def __init__(self):
        tiere = [Vogel(), Wurm()]
        for tier in tiere:
            tier.bewegt_sich()
            # tier.zwitscher()  # Fehler
            # tier.frisst()     # Fehler

if __name__ == "__main__":
    Polymorphie()