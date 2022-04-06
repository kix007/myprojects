import asyncio
import logging
import typing

from aiohttp import web

from config import config
from cors_middleware import cors
from database import close_db, init_db
from accounts import account_routes
from stats import stats_routes
from rewards import rewards_routes

APP_HOST = config.get("app", "host")
APP_PORT = config.getint("app", "port")


def add_routes(app: web.Application, route_tables: typing.Iterable[web.RouteTableDef]):
    for route_table in route_tables:
        app.add_routes(route_table)


async def init_app():
    app = web.Application(middlewares=[cors], client_max_size=4 * 1024 * 1024)
    add_routes(
        app,
        [
           account_routes,
           stats_routes,
           rewards_routes,
        ],
    )

    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    return app


def main():
    logging.basicConfig(level=logging.INFO)
    app = init_app()
    web.run_app(app, host=APP_HOST, port=APP_PORT)


if __name__ == "__main__":
    main()
