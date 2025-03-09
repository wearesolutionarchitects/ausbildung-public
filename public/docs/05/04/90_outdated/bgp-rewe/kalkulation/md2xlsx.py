import pandas as pd

def markdown_table_to_excel(markdown_file, excel_file):
    # Lese das Markdown-File ein
    with open(markdown_file, 'r') as file:
        lines = file.readlines()

    # Entferne die ersten zwei Zeilen (die Header-Trennzeichen)
    table_lines = lines[2:]

    # Konvertiere die Markdown-Tabelle in eine Liste von Listen
    table_data = []
    for line in table_lines:
        # Entferne führende und nachfolgende Leerzeichen und teile die Zeile in Spalten auf
        row = [cell.strip() for cell in line.split('|') if cell.strip()]
        if row:  # Füge nur nicht-leere Zeilen hinzu
            table_data.append(row)

    # Erstelle einen DataFrame aus den Daten
    df = pd.DataFrame(table_data[1:], columns=table_data[0])

    # Schreibe den DataFrame in eine Excel-Datei
    df.to_excel(excel_file, index=False)

# Beispielhafte Verwendung
markdown_file = 'unterricht/bgp/rewe/kalkulation/c.md'
excel_file = 'unterricht/bgp/rewe/kalkulation/c.xlsx'
markdown_table_to_excel(markdown_file, excel_file)