import pytablewriter

# Markdown-Datei lesen
with open("unterricht/bgp/rewe/inventar/readme.md", "r") as f:
    markdown_data = f.read()

# Writer-Objekt erstellen
writer = pytablewriter.ExcelXlsxTableWriter()

# Markdown-Parser erstellen und Daten laden
parser = pytablewriter.MarkdownTableLoader(markdown_data)
tables = parser.load()

# Für jede Tabelle in der Markdown-Datei
for table in tables:
    # Tabellendaten setzen
    writer.table_name = table.name
    writer.header_list = table.headers
    writer.value_matrix = table.value_matrix

    # Excel-Datei schreiben
    writer.write_table(f"{table.name}.xlsx")
