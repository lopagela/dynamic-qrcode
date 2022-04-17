import logging
from typing import Dict, Optional

log = logging.getLogger(__name__)

# Looks like a repository so far
class HttpLinkComponent:
    def __init__(self):
        self._store: Dict[str, str] = dict()

    def find_by_id(self, id_: str) -> Optional[str]:
        return self._store.get(id_)

    def save(self, id_: str, url: str) -> str:
        log.debug("Saving destination_url='%s' at qr_code_id='%s'", url, id_)
        self._store[id_] = url
        return self._store[id_]

    def find_all(self) -> Dict[str, str]:
        return self._store
