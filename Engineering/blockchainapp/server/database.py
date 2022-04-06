import json

import asyncpg

from config import config


def with_conn(func):
    async def wrapped_function(request, *args, **kwargs):
        pool = request.app["pool"]

        async with pool.acquire() as conn:
            async with conn.transaction():
                await conn.set_type_codec(
                    "json", schema="pg_catalog", encoder=json.dumps, decoder=json.loads
                )
                return await func(request, *args, **kwargs, conn=conn)

    return wrapped_function


async def _init_connection(conn: asyncpg.Connection):
    await conn.set_type_codec(
        "jsonb", schema="pg_catalog", encoder=json.dumps, decoder=json.loads
    )


async def init_db(app):
    app["pool"] = await asyncpg.create_pool(
        **config["database"], max_size=50, init=_init_connection
    )


async def close_db(app):
    await app["pool"].close()
