from abc import ABC, abstractmethod

# Abstrakte Cocktailklasse
class Cocktail(ABC):
    @abstractmethod
    def ingredients(self):
        pass
    
    @abstractmethod
    def name(self):
        pass

# Konkrete Cocktailklassen
class Margarita(Cocktail):
    def ingredients(self):
        return ['Tequila', 'Triple Sec', 'Lime Juice', 'Salt']
    
    def name(self):
        return "Margarita"

class Mojito(Cocktail):
    def ingredients(self):
        return ['White Rum', 'Sugar', 'Lime Juice', 'Soda Water', 'Mint']
    
    def name(self):
        return "Mojito"

class OldFashioned(Cocktail):
    def ingredients(self):
        return ['Bourbon', 'Sugar', 'Bitters', 'Orange Peel']
    
    def name(self):
        return "Old Fashioned"

# Die CocktailFactory
class CocktailFactory:
    def create_cocktail(self, cocktail_type):
        if cocktail_type == "Margarita":
            return Margarita()
        elif cocktail_type == "Mojito":
            return Mojito()
        elif cocktail_type == "OldFashioned":
            return OldFashioned()
        else:
            raise ValueError(f"Unknown cocktail type: {cocktail_type}")

# Beispiel der Verwendung
def main():
    factory = CocktailFactory()

    cocktails = ['Margarita', 'Mojito', 'OldFashioned']
    
    for cocktail_name in cocktails:
        cocktail = factory.create_cocktail(cocktail_name)
        print(f"Cocktail: {cocktail.name()}")
        print(f"Ingredients: {', '.join(cocktail.ingredients())}")
        print()

if __name__ == "__main__":
    main()