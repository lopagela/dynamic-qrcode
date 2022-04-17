# Dynamic QR code web-server

TODO

## Development

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

uvicorn dynamic_qrcode.__main__:app --reload
```

## Production run
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

URL_HOST="https://example.com" gunicorn dynamic_qrcode.__main__:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Additional libraries required by Pillow for Raspberry

```shell
sudo apt-get update && sudo apt-get install \
  libjpeg-dev \
  zlib1g-dev \
  libfreetype6-dev \
  liblcms1-dev \
  libopenjp2-7 \
  libtiff5 -y
```

