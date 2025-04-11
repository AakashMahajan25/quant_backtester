# Creating a basic SMACrossover Strategy

import numpy as np
from engine.event import SignalEvent

class SMACrossoverStrategy:

    def __init__(self, symbol, events, data_handler, short_window=50, long_window=200):
        self.symbol = symbol
        self.events = events
        self.data_handler = data_handler
        self.short_window = short_window
        self.long_window = long_window

        self.in_position = False   #Currently holding any asssets or not
        self.bars = []             #Tracking Closing Prices

    
    def calculate_signals(self, event):

        # Generating signals bassed on SMA crossover

        if event.type != "MARKET":
            return

        _, bar = self.data_handler.get_latest_bar()
        close = bar["Close"]
        self.bars.append(close)

        if len(self.bars) < self.long_window:
            return
        
        short_sma = np.mean(self.bars[-self.short_window:])
        long_sma = np.mean(self.bars[-self.long_window:])

        # Generate Signal
        if short_sma > long_sma and not self.in_position:
            signal = SignalEvent(self.symbol, "LONG", event.time)
            self.events.put(signal)
            self.in_position = True

        elif short_sma < long_sma and self.in_position:
            signal = SignalEvent(self.symbol, "EXIT", event.time)
            self.events.put(signal)
            self.in_position = False