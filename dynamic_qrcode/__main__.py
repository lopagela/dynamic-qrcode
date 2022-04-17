import logging

from dynamic_qrcode.app import app


PRETTY_LOG_FORMAT = '%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s - %(message)s'
logging.basicConfig(level="DEBUG", format=PRETTY_LOG_FORMAT, datefmt="%H:%M:%S")

log = logging.getLogger(__name__)

log.info("Application loaded")
