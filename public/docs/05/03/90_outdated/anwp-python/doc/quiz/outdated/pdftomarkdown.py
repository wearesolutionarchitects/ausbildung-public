import pymupdf4llm
md_text = pymupdf4llm.to_markdown("unterricht/anwp/python/doc/quiz/quiz.pdf")

import pathlib
pathlib.Path("unterricht/anwp/python/doc/quiz/output.md").write_bytes(md_text.encode())