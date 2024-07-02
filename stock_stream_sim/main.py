from .websocket_server import WebSocketServer
import asyncio

def main():
    server = WebSocketServer()
    asyncio.run(server.start_server())

if __name__ == "__main__":
    main()
