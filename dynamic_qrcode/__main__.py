import logging

PRETTY_LOG_FORMAT = '%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s - %(message)s'
logging.basicConfig(level="DEBUG", format=PRETTY_LOG_FORMAT, datefmt="%H:%M:%S")

log = logging.getLogger(__name__)

# Configuring the logging before importing the source code
from dynamic_qrcode.app import app

log.info("Application loaded")
