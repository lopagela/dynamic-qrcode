# Dynamic QR code web-server

Configure HTTP path that redirects to your HTTP targets defined in configuration.

Load the configuration from your `~/.config/dynamic_qrcode/config.yaml` file,
and start to serve the QR code for the defined targets.

See `/docs` for the API documentation.

## Development
Start a development server with `uvicorn` that reloads the server on file changes:

```shell
python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip
pip install -e '.'

uvicorn dynamic_qrcode.__main__:app --reload
```

## Production run
Start the server with `gunicorn`:

```shell
python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip
pip install '.'

gunicorn dynamic_qrcode.__main__:app -w 4 -k uvicorn.workers.UvicornWorker
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

