import pandas as pd

# Lese die Markdown-Datei als DataFrame
df = pd.read_csv('hhip_project/unterricht/anwp/oop/cocktails/readme.md', sep="|", skiprows=2)

# Konvertiere den DataFrame in ein JSON-Objekt
json_obj = df.to_json(orient='records')

# Schreibe das JSON-Objekt in eine Datei
with open('hhip_project/unterricht/anwp/oop/cocktails/coctails.json', 'w') as f:
    f.write(json_obj)
