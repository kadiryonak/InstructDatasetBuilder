import re
import logging
from typing import List

logger = logging.getLogger(__name__)

def split_into_chunks(text: str, max_chars: int = 1200, overlap: int = 150) -> List[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, current = [], ""

    for para in paragraphs:
        if len(para) >= max_chars:
            start = 0
            while start < len(para):
                end = start + max_chars
                piece = para[start:end]
                chunks.append(piece.strip())
                current = piece[-overlap:] if overlap < len(piece) else piece
                start = end
        else:
            if len(current) + len(para) + 2 <= max_chars:
                current = (current + "\n\n" + para).strip() if current else para
            else:
                if current:
                    chunks.append(current.strip())
                current = para
    if current:
        chunks.append(current.strip())

    logger.info(f"Toplam chunk sayısı: {len(chunks)}")
    return chunks
