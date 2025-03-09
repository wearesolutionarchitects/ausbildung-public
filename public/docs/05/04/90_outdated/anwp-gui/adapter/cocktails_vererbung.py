# Vorhandene Cocktail-Klasse
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

# Adapter mit Vererbung (Klassenadapter)
class CocktailAdapter(OldFashioned, CocktailInterface):
    def ingredients(self):
        return self.get_ingredients()

    def name(self):
        return self.get_name()

# Beispiel der Verwendung
def main():
    adapter = CocktailAdapter()

    print(f"Cocktail: {adapter.name()}")
    print(f"Ingredients: {', '.join(adapter.ingredients())}")

if __name__ == "__main__":
    main()