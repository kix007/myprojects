import logging
from time import time

from aiohttp.web import HTTPException, Response, middleware

from config import config

DEFAULT_HEADERS = {
    "Access-Control-Allow-Credentials": "true",
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age#Directives
    "Access-Control-Max-Age": "86400",
    "Access-Control-Allow-Headers": (
        "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    ),
    "Access-Control-Allow-Origin": config.get("site", "web_url"),
    "Allow": "OPTIONS, GET, POST",
}


@middleware
async def cors(request, handler):
    if request.method == "OPTIONS":
        resp = Response()
    else:
        try:
            resp = await handler(request)
        except HTTPException as e:
            timestamp = int(time())
            error_text = f"Internal Server Error. Your token is: {timestamp}"
            logging.error(error_text)
            logging.exception(e)
            resp = e
        except Exception as e:
            timestamp = int(time())
            error_text = f"Internal Server Error. Your token is: {timestamp}"
            logging.error(error_text)
            logging.exception(e)
            resp = Response(body=error_text, status=500)

    resp.headers.update(DEFAULT_HEADERS)

    return resp
