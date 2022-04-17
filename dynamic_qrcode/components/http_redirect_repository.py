from typing import Dict, Optional

# Looks like a repository so far
class HttpLinkComponent:
    def __init__(self):
        self._store: Dict[str, str] = dict()

    def find_by_id(self, id_: str) -> Optional[str]:
        return self._store.get(id_)

    def save(self, id_: str, url: str) -> str:
        self._store[id_] = url
        return self._store[id_]

    def find_all(self) -> Dict[str, str]:
        return self._store
