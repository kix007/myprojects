from cgitb import reset
from aiohttp import web

from database import with_conn
import requests
from utils.encoder import dumps
from .routes import routes


@routes.post(r"/accounts")
@with_conn
async def accounts(request, conn):
    req = requests.get('https://api.helium.io/v1/accounts')
    res = req.json()["data"]

    for data in res:
        address = data["address"]
        staked_balance = data["staked_balance"]
        block = data["block"]
        dc_balance = data["dc_balance"]
        nonce = data["nonce"]
        dc_nonce = data["dc_nonce"]
        balance = data["balance"]

        await conn.execute("""
            INSERT INTO accounts_list (address, staked_balance, block, dc_balance, nonce, dc_nonce, balance)
            VALUES('{}',{},'{}',{},{},{},{}) ON CONFLICT DO NOTHING;
        """.format(address, staked_balance, block, dc_balance, nonce, dc_nonce, balance))

    return web.json_response(res)


@routes.get(r"/accounts_list")
@with_conn
async def accounts_list(request, conn):
    res = await conn.fetch("""
        SELECT * FROM accounts_list;
    """)
        
    return web.json_response([dict(i) for i in res], dumps=dumps)