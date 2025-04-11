import queue

class Backtest:
    def __init__(self, data_handler, strategy, portfolio, execution_handler, risk_manager):
        self.events = queue.Queue()

        self.data_handler = data_handler
        self.strategy = strategy
        self.portfolio = portfolio
        self.execution_handler = execution_handler
        self.risk_manager = risk_manager

        self.running = True
    
    def run(self):
        while self.running and self.data_handler.continue_backtest():
            self.data_handler.update_bars()

            while not self.events.empty():
                event = self.events.get()

                if event.type == "MARKET":
                    self.strategy.calculate_signals(event)
                    self.portfolio.update_market(event)
                
                elif event.type == "SIGNAL":
                    risk_approved_orders = self.risk_manager.evaluate_signal(event)
                    for order in risk_approved_orders:
                        self.events.put(order)
                
                elif event.type == "ORDER":
                    self.execution_handler.execute_order(event)
                
                elif event.type == "FILL":
                    self.portfolio.update_fill(event)
                
            self.portfolio.print_summary()