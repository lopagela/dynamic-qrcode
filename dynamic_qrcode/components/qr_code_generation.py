import io
import logging
from typing import BinaryIO

import qrcode

log = logging.getLogger(__name__)


# TODO verify that there are no memory leak because of the stream not being closed
def get_qrcode_as_image(url: str) -> BinaryIO:
    log.debug("Building a QR code for the url=%s", url)
    qr = qrcode.main.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    stream = io.BytesIO()
    img.save(stream=stream)
    stream.seek(0)  # Stream ready to be consumed
    return stream
