# Vorhandene Cocktail-Klassen
class OldFashioned:
    def get_ingredients(self):
        return ['Bourbon', 'Sugar', 'Bitters', 'Orange Peel']

    def get_name(self):
        return "Old Fashioned"

# Zielschnittstelle, die wir anpassen möchten
class CocktailInterface:
    def ingredients(self):
        pass

    def name(self):
        pass

# Adapter mit Delegation (Objektadapter)
class CocktailAdapter(CocktailInterface):
    def __init__(self, old_fashioned):
        self.old_fashioned = old_fashioned

    def ingredients(self):
        return self.old_fashioned.get_ingredients()

    def name(self):
        return self.old_fashioned.get_name()

# Beispiel der Verwendung
def main():
    old_fashioned = OldFashioned()
    adapter = CocktailAdapter(old_fashioned)

    print(f"Cocktail: {adapter.name()}")
    print(f"Ingredients: {', '.join(adapter.ingredients())}")

if __name__ == "__main__":
    main()