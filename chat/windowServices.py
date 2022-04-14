import asyncio
import json
import websockets
async def hello():
    # async with websockets.connect("wss://websocket-application.herokuapp.com/ws/ac/tally/") as websocket:
    async with websockets.connect("ws://127.0.0.1:8000/ws/socket-server/ank@hotmail.comc/ank/") as websocket:
        # await websocket.send(json.dumps({
        #         'message': 'database',
        #         'username': 'ankit',
        #         'room': 'tally'
        #     }));
        while True:
            print(await websocket.recv())
asyncio.run(hello())
