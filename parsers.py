import os
import re
import logging
import fitz  # PyMuPDF
from abc import ABC, abstractmethod
from typing import List

logger = logging.getLogger(__name__)

class DocumentParser(ABC):
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.path = path
        self.encoding = encoding

    @abstractmethod
    def parse_text(self) -> str:
        raise NotImplementedError

    def get_chunks(self, max_chars: int = 1200, overlap: int = 150) -> List[str]:
        from .chunking import split_into_chunks
        text = self.parse_text()
        return split_into_chunks(text, max_chars=max_chars, overlap=overlap)

class PDFParser(DocumentParser):
    def parse_text(self) -> str:
        logger.info(f"PDF açılıyor: {self.path}")
        doc = fitz.open(self.path)
        pages = []
        for page in doc:
            txt = page.get_text("text")
            txt = txt.replace("\r", "\n")
            pages.append(txt)
        full = "\n\n".join(pages)
        return re.sub(r"\n{3,}", "\n\n", full).strip()

PARSER_REGISTRY = {
    ".pdf": PDFParser,
}

def get_parser_for_path(path: str) -> DocumentParser:
    ext = os.path.splitext(path)[1].lower()
    ParserCls = PARSER_REGISTRY.get(ext)
    if not ParserCls:
        raise ValueError(f"Desteklenmeyen uzantı: {ext}")
    return ParserCls(path)
