import pytablereader as ptr
import pytablewriter as ptw

# Pfad zur Markdown-Datei
md_file_path = "readme.md"

# Lese die Tabelle aus der Markdown-Datei
reader = ptr.MarkdownTableFileLoader(md_file_path)
table_data = reader.load()

# Pfad zur Ausgabe-Excel-Datei
excel_file_path = "inventar.xlsx"

# Schreibe die Daten in eine Excel-Datei
writer = ptw.ExcelXlsxTableWriter()
writer.from_tabledata(table_data[0])  # Nehmen Sie die erste Tabelle aus der Datei
writer.dump(excel_file_path)
