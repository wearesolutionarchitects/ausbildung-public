# Cocktails

## Definition der Klasse

```python
class Cocktail: 
    def __init__(self, name, preis, staerke, volumen):
        self.name = name # Attribute / Parameter
        self.preis = preis
        self.staerke = staerke
        self.volumen = volumen  
    def __int__(self):
        return 815

    def __str__(self):
        return f"Cocktail: {self.name}, Preis: {self.preis} €, Stärke: {self.staerke} Volumen: {self.volumen} l"
    
    def __gt__ (self, other):
        return (self.preis > other.preis) and (self.staerke > other.staerke)

around_the_world = Cocktail("Around the World", 32.00, 5, 3.0)
aloha = Cocktail("Aloha", 8.00, 4, 0.55)

print(around_the_world)
print(int(aloha))

if around_the_world > aloha:
    print("around_the_world ist teurer als aloha")
else:
    print("aloha ist teurer als around_the_world")

print(Cocktail.mro())
```

    Cocktail: Around the World, Preis: 32.0 €, Stärke: 5 Volumen: 3.0 l
    815
    around_the_world ist teurer als aloha
    [<class '__main__.Cocktail'>, <class 'object'>]

## Konvertierung der Markdown-Tabelle

```python
import pandas as pd

# Lese die Markdown-Tabelle
df = pd.read_table('readme.md')

# Konvertiere die Tabelle in JSON
json_data = df.to_json(orient='records')

print(json_data)

```
