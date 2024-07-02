import asyncio
import websockets

async def consume_data():
    uri = "ws://localhost:8765"  # Replace with your WebSocket server address
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to {uri}")
            while True:
                data = await websocket.recv()
                print(f"Received: {data}")
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    await consume_data()

if __name__ == "__main__":
    asyncio.run(main())
