from aiohttp import web

from database import with_conn
import requests
from utils.encoder import dumps
from .routes import routes


@routes.post(r"/insert_rewards")
@with_conn
async def insert_rewards(request, conn):
    req = requests.get('https://api.helium.io/v1/rewards/sum')
    res = req.json()

    min_time = res["meta"]["min_time"]
    max_time = res["meta"]["max_time"]
    total = res["data"]["total"]
    sum_amt = res["data"]["sum"]
    stddev = res["data"]["stddev"]
    min_amt = res["data"]["min"]
    median = res["data"]["median"]
    max_amt = res["data"]["max"]
    avg_amt = res["data"]["avg"]

    await conn.execute("""
        INSERT INTO rewards_charts (min_time, max_time, total, sum_amt, stddev, min_amt, median, max_amt, avg_amt)
        VALUES('{}','{}', {}, {}, {}, {}, {}, {}, {});
    """.format(min_time, max_time, total, sum_amt, stddev, min_amt, median, max_amt, avg_amt))

    return web.json_response(res)


@routes.get(r"/rewards")
@with_conn
async def rewards(request, conn):
    res = await conn.fetchrow("""
with aa as (
select 
jsonb_build_object(
             'data_labels',
             jsonb_agg(min_time)
           ) labels,
		jsonb_build_object('chart_data',
						   jsonb_agg(
		concat_ws(',', coalesce(total, 0),	
			coalesce(sum_amt, 0)		
			,coalesce(stddev, 0)
	        ,coalesce(min_amt, 0)
		    ,coalesce(median, 0)	
			,  coalesce(max_amt, 0)	
			, coalesce(avg_amt, 0)	
						   )))	   
		   from rewards_charts
		--group by 5
)
select *  from aa
    """)

    print(res)
    
    return web.json_response([dict(rwd) for rwd in res], dumps=dumps)