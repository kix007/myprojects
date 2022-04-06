from aiohttp import web

from database import with_conn
import requests

from .routes import routes


@routes.get(r"/stats")
@with_conn
async def stats(request, conn):
    req = requests.get('https://api.helium.io/v1/stats')
    res = req.json()

    print(res["data"])

    return web.json_response(res)