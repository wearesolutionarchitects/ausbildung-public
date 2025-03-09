import pandas as pd

# Lade die Excel-Datei
df = pd.read_excel('\vvt.xlsx')

# Konvertiere den DataFrame in Markdown
markdown_text = df.to_markdown()

# Schreibe den Markdown-Text in eine Datei
with open('\readme.md', 'w') as f:
    f.write(markdown_text)
