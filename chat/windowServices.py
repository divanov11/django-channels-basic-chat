import asyncio
import websockets

async def ledger():
    async with websockets.connect("ws://127.0.0.1:8000/ws/ledger-socket-server/6b778c3b-6c68-459d-a4b0-fe5215d72866c/") as websocket:
        while True:
            print(await websocket.recv())

async def voucher():
    async with websockets.connect("ws://127.0.0.1:8000/ws/voucher-socket-server/6b778c3b-6c68-459d-a4b0-fe5215d72866c/") as websocket:
        while True:
            print(await websocket.recv())

async def invoice():
    async with websockets.connect("ws://127.0.0.1:8000/ws/invoice-socket-server/6b778c3b-6c68-459d-a4b0-fe5215d72866c/") as websocket:
        while True:
            print(await websocket.recv())

asyncio.run(ledger())
asyncio.run(voucher())
asyncio.run(invoice())
