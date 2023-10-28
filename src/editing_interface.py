```python
import asyncio
from aiohttp import web
from websocket import create_connection

class EditingInterface:
    def __init__(self, websocket_url):
        self.websocket_url = websocket_url
        self.websocket = None

    async def connect(self):
        self.websocket = create_connection(self.websocket_url)

    async def send_data(self, data):
        if self.websocket is None:
            await self.connect()
        self.websocket.send(data)

    async def receive_data(self):
        if self.websocket is None:
            await self.connect()
        return self.websocket.recv()

    async def close_connection(self):
        if self.websocket is not None:
            self.websocket.close()

    async def handle_editing(self, request):
        data = await request.json()
        await self.send_data(data)
        response = await self.receive_data()
        return web.json_response(response)

    def run_server(self, host='localhost', port=8080):
        app = web.Application()
        app.router.add_post('/edit', self.handle_editing)
        web.run_app(app, host=host, port=port)

if __name__ == "__main__":
    editing_interface = EditingInterface("ws://localhost:8080")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(editing_interface.run_server())
```