import logging
from json import JSONDecodeError
from typing import Dict
import json

log = logging.getLogger(__name__)


def get_initial_url_map(filename: str = "default-links.json") -> Dict[str, str]:
    # The file must be in the format {"qr_code_id": "https://example.com"} format
    log.info("Reading the JSON file='%s' for the initial configuration", filename)
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        log.warning("Filename=%s does not exist, returning an empty map", exc_info=True)
    except JSONDecodeError:
        log.error("Filename=%s is an invalid JSON file, returning an empty map", exc_info=True)
    return {}

