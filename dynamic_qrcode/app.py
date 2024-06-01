import logging
import os

from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.responses import StreamingResponse
from starlette.responses import RedirectResponse

from dynamic_qrcode.components.http_redirect_repository import HttpLinkComponent
from dynamic_qrcode.components.qr_code_generation import get_qrcode_as_image
from dynamic_qrcode.configuration import get_configuration

log = logging.getLogger(__name__)

configuration = get_configuration(filename="default-links.toml")

URL_HOST = configuration["server"].get("url_host") or os.getenv("URL_HOST", default="http://localhost:8000")
PATH_PREFIX = configuration["server"].get("prefix", "/q")

log.info("Loading the server with URL_HOST='%s', PATH_PREFIX='%s'", URL_HOST, PATH_PREFIX)
router = APIRouter(prefix=PATH_PREFIX)
url_link_component = HttpLinkComponent()

default_url_link = configuration["qrcode_redirections"]
for _qr_code_id, _destination_url in default_url_link.items():
    url_link_component.save(_qr_code_id, _destination_url)

log.debug("Accepting requests looking like %s%s/{qr_code_id}", URL_HOST, PATH_PREFIX)


@router.get(
    path="/{qr_code_id}",
    summary="Link that will be consumed by the QR code consumer",
    response_class=RedirectResponse,
    status_code=307,
)
def redirect_to_alias(qr_code_id: str):
    # Redirecting to the destination URL
    return url_link_component.find_by_id(qr_code_id)


@router.get(
    path="/{qr_code_id}/png",
    summary="Get back the QR code as a PNG for the given code",
    description="The QR code will be generated for the given code and returned "
                "as a PNG image. The media type is image/png",
)
def display_qrcode(qr_code_id: str, reveal: bool = False):
    log.info("Got request to display the QR code for qr_code_id=%s", qr_code_id)
    destination_url = url_link_component.find_by_id(qr_code_id)
    if not destination_url:
        raise HTTPException(status_code=404, detail="Code not found")
    qrcode_target_url = URL_HOST + PATH_PREFIX + f"/{qr_code_id}"
    if reveal:
        qrcode_target_url = destination_url
    log.debug("Found for qr_code_id=%s the url='%s' with reveal=%s", qr_code_id, destination_url, reveal)

    stream = get_qrcode_as_image(qrcode_target_url)
    return StreamingResponse(content=stream, media_type="image/png")


app = FastAPI()
app.include_router(router)
