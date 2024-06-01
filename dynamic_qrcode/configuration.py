import logging
import os.path
from typing import Dict, TypedDict
import tomllib

log = logging.getLogger(__name__)


class ServerConfiguration(TypedDict):
    prefix: str
    url_host: str


class Configuration(TypedDict):
    server: ServerConfiguration
    qrcode_redirections: Dict[str, str]


def get_configuration(filename: str = "default-links.toml") -> Configuration:
    filenames = [
        "~/.config/dynamic_qrcode/config.toml",
        filename
    ]
    for filename in filenames:
        try:
            return _get_configuration_from_file(filename)
        except (FileNotFoundError, tomllib.TOMLDecodeError):
            log.debug("Could not read the configuration file='%s'", filename)
    raise FileNotFoundError(f"Could not find any valid configuration file in filenames={filenames}")


def _get_configuration_from_file(filename) -> Configuration:
    # The file must be in the format {"qr_code_id": "https://example.com"} format
    log.info("Reading the TOML file='%s' for the initial configuration", filename)
    with open(os.path.expanduser(filename), "rb") as file:
        return tomllib.load(file)

