import asyncio
import websockets
import json
from .price_generator import PriceGenerator
from .config import CANDLESTICK_PERIOD

class WebSocketServer:
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.price_generator = PriceGenerator()
        self.clients = set()
        self.candlestick_period = float(CANDLESTICK_PERIOD)  # Ensure this is a float
        self.candle_data = None
        self.candle_open_time = None

    async def register(self, websocket):
        print("Client connected")
        self.clients.add(websocket)

    async def unregister(self, websocket):
        print("Client disconnected")
        self.clients.remove(websocket)

    async def send_price_data(self):
        while True:
            current_price = self.price_generator.generate_price()
            current_time = asyncio.get_event_loop().time()

            if self.candle_data is None or current_time - self.candle_open_time >= self.candlestick_period:
                if self.candle_data is not None:
                    self.candle_data['close'] = current_price
                    self.candle_data['candle_closed'] = True
                    data_json = json.dumps(self.candle_data)
                    if self.clients:
                        tasks = [asyncio.create_task(client.send(data_json)) for client in self.clients]
                        await asyncio.gather(*tasks)

                self.candle_data = {
                    "open": current_price,
                    "high": current_price,
                    "low": current_price,
                    "close": current_price,
                    "candle_closed": False
                }
                self.candle_open_time = current_time

            else:
                self.candle_data['high'] = max(self.candle_data['high'], current_price)
                self.candle_data['low'] = min(self.candle_data['low'], current_price)
                data_json = json.dumps({"Current Price": current_price})
                if self.clients:
                    tasks = [asyncio.create_task(client.send(data_json)) for client in self.clients]
                    await asyncio.gather(*tasks)

            await asyncio.sleep(2)

    async def start_server(self):
        print(f"Starting server on {self.host}:{self.port}")
        async with websockets.serve(self.handler, self.host, self.port):
            await self.send_price_data()

    async def handler(self, websocket, path):
        await self.register(websocket)
        try:
            await websocket.wait_closed()
        finally:
            await self.unregister(websocket)

def main():
    server = WebSocketServer()
    asyncio.run(server.start_server())

if __name__ == "__main__":
    main()
