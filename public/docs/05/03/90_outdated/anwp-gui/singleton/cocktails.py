# Singleton Pattern für die CocktailFactory

class CocktailFactorySingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CocktailFactorySingleton, cls).__new__(cls)
        return cls._instance

    def create_cocktail(self, cocktail_type):
        if cocktail_type == "Margarita":
            return Margarita()
        elif cocktail_type == "Mojito":
            return Mojito()
        elif cocktail_type == "OldFashioned":
            return OldFashioned()
        else:
            raise ValueError(f"Unknown cocktail type: {cocktail_type}")

# Beispiel der Verwendung des Singleton Patterns
def main():
    factory1 = CocktailFactorySingleton()
    factory2 = CocktailFactorySingleton()

    print(f"Factory1 ID: {id(factory1)}")
    print(f"Factory2 ID: {id(factory2)}")

    # Beides sollten die gleiche Instanz sein
    print("Sind beide Instanzen gleich?", factory1 is factory2)

    cocktails = ['Margarita', 'Mojito', 'OldFashioned']
    
    for cocktail_name in cocktails:
        cocktail = factory1.create_cocktail(cocktail_name)
        print(f"Cocktail: {cocktail.name()}")
        print(f"Ingredients: {', '.join(cocktail.ingredients())}")
        print()

if __name__ == "__main__":
    main()