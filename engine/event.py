from abc  import ABC

class Event(ABC):
    # Base class for all events
    pass

class MarketEvent(Event):
    def __init__(self, time):
        self.type = "MARKET"
        self.time = time


class SignalEvent(Event):
    def __init__(self, symbol, signal_type, time=None):
        self.type = "SIGNAL"
        self.symbol = symbol
        self.signal_type = signal_type # 'LONG' or 'EXIT'
        self.time = time


class OrderEvent(Event):
    def __init__(self, symbol, order_type, quantity, direction):
        self.type = "ORDER"
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction
    
    def __str__(self):
        return f"OrderEvent: {self.symbol}, {self.order_type}, {self.direction}"
    

class FillEvent(Event):
    def __init__(self, time, symbol, quantity, direction, fill_price, commission=0.0):
        self.type = "FILL"
        self.time = time
        self.symbol = symbol
        self.quantity = quantity
        self.direction = direction
        self.fill_price = fill_price
        self.commission = commission
