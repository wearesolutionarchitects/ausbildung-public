'''
This script converts the PDF file to Markdown format.
'''
import pathlib
import pymupdf4llm

# Convert the PDF to Markdown

md_text = pymupdf4llm.to_markdown(
    "unterricht/bgp/ds/praesentationen/Vorbereitung LEK.pdf")
pathlib.Path(
    "unterricht/bgp/ds/praesentationen/vorbereitung_lek.md").write_bytes(md_text.encode())
