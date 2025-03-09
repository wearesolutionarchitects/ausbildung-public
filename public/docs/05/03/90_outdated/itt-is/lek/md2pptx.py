import subprocess

class PresentationBuilder:
    def __init__(self, markdown_file, output_file, template_file=None):
        self.markdown_file = markdown_file
        self.output_file = output_file
        self.template_file = template_file

    def convert_markdown_to_pptx(self):
        """Konvertiert die Markdown-Datei in eine PPTX-Präsentation mit optionaler Vorlage."""
        try:
            command = ['pandoc', self.markdown_file, '-o', self.output_file]
            
            if self.template_file:
                command.extend(['--reference-doc', self.template_file])
            
            subprocess.run(command, check=True)
            print(f"Präsentation erfolgreich gespeichert unter: {self.output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei der Konvertierung: {e}")

    def build(self):
        """Startet den Konvertierungsprozess."""
        self.convert_markdown_to_pptx()

# Beispiel für die Verwendung der Klasse

markdown_file = "unterricht/itt-is/lek/readme.md"
output_file = "unterricht/itt-is/lek/lek_puya.pptx"
template_file = "unterricht/itt-is/lek/template.pptx"  # Vorlage für die Formatierung

builder = PresentationBuilder(markdown_file, output_file, template_file)
builder.build()