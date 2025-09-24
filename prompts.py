PROMPT_TEMPLATES = {
    "tr": {
        "format_instructions": (
            "Çıktıyı geçerli JSON verisi olarak döndür. "
            "Anahtarlar: 'soru', 'cevap', 'soru_tipi'."
        ),
        "prompt": (
            "{format_instructions}\n\n"
            "Dil: Türkçe\n"
            "Soru tipi: {q_type}\n"
            "Adet: {n}\n\n"
            "Metin:\n{chunk}\n"
        )
    }
}

def build_prompt(chunk: str, q_type: str, n: int = 1, lang: str = "tr") -> str:
    tpl = PROMPT_TEMPLATES.get(lang, PROMPT_TEMPLATES["tr"])
    return tpl["prompt"].format(
        format_instructions=tpl["format_instructions"],
        q_type=q_type, n=n, chunk=chunk
    )
