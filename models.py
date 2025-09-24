import json
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class ModelWrapper(ABC):
    @abstractmethod
    def generate(self, prompt: str, max_tokens: int = 512, **kwargs) -> str:
        raise NotImplementedError

class DummyModelWrapper(ModelWrapper):
    def generate(self, prompt: str, max_tokens: int = 512, **kwargs) -> str:
        logger.warning("DummyModelWrapper kullanılıyor")
        return json.dumps({
            "soru": "DUMMY: Soru",
            "cevap": "DUMMY: Cevap",
            "soru_tipi": "diger"
        }, ensure_ascii=False)

class OllamaModelWrapper(ModelWrapper):
    def __init__(self, model_name: str, host: str = "http://localhost:11434"):
        import requests
        self.model_name = model_name
        self.host = host
        self.session = requests.Session()
        self.api_url = f"{self.host}/api/chat"

    def generate(self, prompt: str, max_tokens: int = 512, **kwargs) -> str:
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "options": {"num_predict": max_tokens},
            "stream": False
        }
        try:
            resp = self.session.post(self.api_url, json=payload, timeout=600)
            resp.raise_for_status()
            return resp.json().get("message", {}).get("content", "").strip()
        except Exception as e:
            logger.error(f"Ollama isteği başarısız oldu: {e}")
            return ""
