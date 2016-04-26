from aiohttp import web
import aiohttp

from shatup import app


@app.register('/')
def main(request):
    return app.ps.jade.render('main.jade')


@app.register('/chat.ws')
async def chat_websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for message in ws:
        if message.tp == aiohttp.MsgType.text:
            if message.data == 'close':
                await ws.close()
            else:
                ws.send_str(message.data)
    return ws
