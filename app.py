#必用的框架, debug, log 
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web


def index(request):
	return web.Response(body='<h1>Aweson<h1>')
	# return web.Response(text='Hello, world')


async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_get('/', index)
	# app.router.add_route('GET', '/', index)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9900)
	logging.info('server started at http:127.0.0.1:9900...')	
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()