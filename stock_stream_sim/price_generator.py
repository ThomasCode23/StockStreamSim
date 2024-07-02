import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PriceGenerator:
    def __init__(self, initial_price=100.0, base_volatility=0.01, high_volatility=0.05, switch_prob=0.05):
        self.current_price = initial_price
        self.base_volatility = base_volatility
        self.high_volatility = high_volatility
        self.current_volatility = base_volatility
        self.switch_prob = switch_prob
        self.trend = 0.0  # Initial trend is zero
        self.trend_strength = 0.0001
        self.price_series = [initial_price]
    
    def generate_price(self):
        # Switch volatility regime periodically
        if np.random.rand() < self.switch_prob:
            self.current_volatility = self.high_volatility if self.current_volatility == self.base_volatility else self.base_volatility

        # Adjust the trend gradually
        if np.random.rand() < 0.01:
            self.trend = np.random.normal(loc=0, scale=self.trend_strength)

        # Simulate realistic price movement using a random walk with trend and volatility
        delta = self.trend + np.random.normal(loc=0, scale=self.current_volatility)
        next_price = self.current_price + delta
        
        # Ensure the price stays positive
        next_price = max(0.01, next_price)
        
        # Update the current price and append to series
        self.current_price = next_price
        self.price_series.append(next_price)
        
        return self.current_price

    def generate_candlestick(self, period):
        # Generate OHLC candlestick data for the given period
        open_price = self.current_price
        high_price = open_price + np.random.uniform(0, self.current_volatility * 2)
        low_price = open_price - np.random.uniform(0, self.current_volatility * 2)
        close_price = open_price + np.random.uniform(-self.current_volatility, self.current_volatility)
        return {
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "close": close_price,
            "candle_closed": False,
        }

# Example usage:
# pg = PriceGenerator()
# prices = []
# for _ in range(100000):
#     prices.append(pg.generate_price())

# # Using pandas to visualize the price series
# price_series = pd.Series(prices)
# price_series.plot(title="Simulated Stock Price")
# plt.show()
