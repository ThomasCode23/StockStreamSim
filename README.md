# StockStreamSim

StockStreamSim is a Python-based project that simulates realtime prices and OHLC (Open, High, Low, Close) candlestick data for a simulated financial instrument for model training. The price changes are trend-based and simulate realistic real-world price movements. Data is streamed over WebSockets. 

## Features

- Simulates realistic price movements using trends and volatility
- Broadcasts current price
- Broadcasts OHLC candlestick data with Open / Closed
- Allows setting the candlestick time period (e.g., 1m, 5m, 15m, etc.)
- Customisable trend strength, volatility and switch probability
- Included Client Component for data consumption.


## Directory Structure

StockStreamSim/

│

├── stock_stream_sim/

│ ├── init.py

│ ├── config.py

│ ├── main.py

│ ├── price_generator.py

│ └── websocket_server.py

├── tests/

│ └── test_price_generator.py

├── .gitignore

├── README.md

└── requirements.txt



## Installation

1. Clone the repository:

git clone https://github.com/ThomasCode23/StockStreamSim.git

cd StockStreamSim


2. Create and activate virtual environment

   python -m venv venv
   
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install dependancies

   pip install -r requirements.txt


## Usage

1. Start the Websocket Server

   python -m stock_stream_sim.main


2. Run the WebSocket client to view the data

   python websocket_client.py

3. Finetune for bespoke use in your own training projects
