import queue
from engine.backtest import Backtest
from feed.csv_data import HistoricCSVDataHandler
from strategy.sma_crossover import SMACrossoverStrategy

# if __name__ == "__main__":
    # Configuration
csv_dir = "data/processed"
symbol = "BAC"
short_window = 50
long_window = 200

    # Event Queue
events = queue.Queue()

    # Instantiate Modules
data_handler = HistoricCSVDataHandler(events, csv_dir, symbol)
strategy = SMACrossoverStrategy(symbol, events, data_handler, short_window,long_window)

    # Running Backtest
backtest = Backtest(data_handler, strategy, events)
backtest.run()