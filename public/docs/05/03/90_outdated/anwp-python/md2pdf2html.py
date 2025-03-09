# Importieren Sie die Module
from markdown import markdown
import pdfkit

# Definieren Sie die Dateinamen
input_filename = 'hhip_project/unterricht/anwp/python/readme.md'
output_filename = 'hhip_project/unterricht/anwp/python/readme.pdf'

# Öffnen Sie die Eingabedatei und lesen Sie den Inhalt
with open(input_filename, 'r') as f:
    markdown_text = f.read()

# Konvertieren Sie den Markdown-Text in HTML
html_text = markdown(markdown_text, output_format='html4')

# Konvertieren Sie den HTML-Text in eine PDF-Datei
pdfkit.from_string(html_text, output_filename)
