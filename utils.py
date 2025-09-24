import json
from typing import List, Dict, Any

def extract_json_objects(text: str) -> List[Dict[str, Any]]:
    objs = []
    start_idxs = [i for i, ch in enumerate(text) if ch == '{']
    for s in start_idxs:
        depth = 0
        for j in range(s, len(text)):
            if text[j] == '{': depth += 1
            elif text[j] == '}':
                depth -= 1
                if depth == 0:
                    try:
                        objs.append(json.loads(text[s:j+1]))
                        break
                    except json.JSONDecodeError:
                        continue
    return objs
