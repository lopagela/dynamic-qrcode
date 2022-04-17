import logging
import os

from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.responses import StreamingResponse
from starlette.responses import RedirectResponse

from dynamic_qrcode.components.http_redirect_repository import HttpLinkComponent
from dynamic_qrcode.components.qr_code_generation import get_qrcode_as_image
from dynamic_qrcode.configuration import get_initial_url_map

log = logging.getLogger(__name__)

URL_HOST = os.getenv("URL_HOST", default="http://localhost:8000")
PATH_PREFIX = "/q"

router = APIRouter(prefix=PATH_PREFIX)
url_link_component = HttpLinkComponent()


default_url_link = get_initial_url_map(filename="default-links.json")
for qr_code_id, destination_url in default_url_link.items():
    url_link_component.save(qr_code_id, destination_url)


@router.get(
    path="/{qr_code_id}",
    summary="Link that will be consumed by the QR code consumer")
def read_item(qr_code_id: str):
    return RedirectResponse(url=url_link_component.find_by_id(qr_code_id), status_code=307)


@router.get(
    path="/{qr_code_id}/png",
    summary="Get back the QR code as a PNG for the given code")
def read_item(qr_code_id: str):
    log.info("Got request to display the QR code for qr_code_id=%s", qr_code_id)
    destination_url = url_link_component.find_by_id(qr_code_id)
    if not destination_url:
        raise HTTPException(status_code=404, detail="Code not found")
    log.debug("Found for qr_code_id=%s the url='%s'", qr_code_id, destination_url)
    source_url = URL_HOST + PATH_PREFIX + f"/{qr_code_id}"
    stream = get_qrcode_as_image(source_url)
    return StreamingResponse(content=stream, media_type="image/png")


app = FastAPI()
app.include_router(router)
