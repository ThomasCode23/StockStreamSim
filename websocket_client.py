import asyncio
import json
import logging
from typing import Optional

import websockets
from colorama import Fore, Style, init

init(autoreset=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def consume_data(uri: str = "ws://localhost:8765"):
    last_price: Optional[float] = None
    async for websocket in websockets.connect(uri):
        try:
            logger.info(f"Connected to {uri}")
            async for message in websocket:
                parsed_data = json.loads(message)
                if "Current Price" in parsed_data:
                    current_price = parsed_data['Current Price']
                    color = get_price_color(current_price, last_price)
                    print(f"{color}{current_price}{Style.RESET_ALL}")
                    last_price = current_price
                else:
                    print(f"{Fore.BLUE}Candle data: {parsed_data}{Style.RESET_ALL}")
        except websockets.ConnectionClosed:
            logger.info("Connection closed, attempting to reconnect...")
        except Exception as e:
            logger.error(f"Error: {e}")

def get_price_color(current_price: float, last_price: Optional[float]) -> str:
    if last_price is None:
        return Fore.RESET
    return Fore.GREEN if current_price > last_price else Fore.RED if current_price < last_price else Fore.RESET

if __name__ == "__main__":
    asyncio.run(consume_data())