import asyncio
import json
import websockets
async def hello():
    async with websockets.connect("ws://127.0.0.1:8000/ws/socket-server/6b778c3b-6c68-459d-a4b0-fe5215d72866c/") as websocket:
        # await websocket.send(json.dumps({
        #         'message': 'database',
        #         'username': 'ankit',
        #         'room': 'tally'
        #     }));
        while True:
            print(await websocket.recv())
asyncio.run(hello())