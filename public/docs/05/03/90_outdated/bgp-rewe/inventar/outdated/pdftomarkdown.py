import pymupdf4llm
md_text = pymupdf4llm.to_markdown("unterricht/bgp/rewe/inventar/inventar.pdf")

import pathlib
pathlib.Path("unterricht/bgp/rewe/inventar/inventar.md").write_bytes(md_text.encode())