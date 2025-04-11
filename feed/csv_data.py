import pandas as pd 
from engine.event import MarketEvent

class HistoricCSVDataHandler:

    def __init__(self, events, csv_dir, symbol):
        self.events = events
        self.csv_dir = csv_dir
        self.symbol = symbol

        self.data = None
        self.latest_bar = None
        self._continue_backtest = True

        self._load_csv()
    
    def _load_csv(self):
        file_path = f"{self.csv_dir}/{self.symbol}.csv"
        df = pd.read_csv(file_path, parse_dates=True, index_col="Date")
        df = df.sort_index()
        self.data = df
        self.data_iter = df.iterrows()

    def update_bars(self):
        try:
            date, bar = next(self.data_iter)
            self.latest_bar = (date, bar)
            self.events.put(MarketEvent(time=date))
        except StopIteration:
            self._continue_backtest = False
    
    def get_latest_bar(self):
        return self.latest_bar
    
    def continue_backtest(self):
        return self._continue_backtest