ib_integration_path = os.path.join(broker_integration_dir, "interactive_brokers_integration.py")
with open(ib_integration_path, "w") as f:
    f.write("import logging\n")
    f.write("from data_fetching.interactive_brokers_data_fetcher import InteractiveBrokersDataFetcher\n")
    f.write("from execution.interactive_brokers_executor import InteractiveBrokersExecutor\n")
    f.write("import pandas as pd\n\n")

    f.write("logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\n\n")

    # 3. Define InteractiveBrokersIntegration class
    f.write("class InteractiveBrokersIntegration:\n")
    f.write("    def __init__(self):\n")
    f.write("        self.data_fetcher = InteractiveBrokersDataFetcher()\n")
    f.write("        self.executor = InteractiveBrokersExecutor()\n")
    f.write("        logging.info('InteractiveBrokersIntegration initialized.')\n\n")

    # 6. Add methods that delegate calls to data fetcher and executor
    f.write("    def fetch_historical_data(self, symbol: str, timeframe: str, start_date: str, end_date: str) -> pd.DataFrame:\n")
    f.write("        return self.data_fetcher.fetch_historical_data(symbol, timeframe, start_date, end_date)\n\n")

    f.write("    def fetch_realtime_data(self, symbol: str):\n")
    f.write("        self.data_fetcher.fetch_realtime_data(symbol)\n\n")

    f.write("    def place_order(self, symbol: str, order_type: str, quantity: float, price: float = None, stop_loss: float = None, take_profit: float = None):\n")
    f.write("        return self.executor.place_order(symbol, order_type, quantity, price, stop_loss, take_profit)\n\n")

    f.write("    def modify_order(self, order_id: str, new_quantity: float = None, new_price: float = None, new_stop_loss: float = None, new_take_profit: float = None):\n")
    f.write("        return self.executor.modify_order(order_id, new_quantity, new_price, new_stop_loss, new_take_profit)\n\n")

    f.write("    def cancel_order(self, order_id: str):\n")
    f.write("        return self.executor.cancel_order(order_id)\n\n")

    f.write("    def get_account_balance(self) -> float:\n")
    f.write("        return self.executor.get_account_balance()\n\n")

    f.write("    def get_open_positions(self) -> pd.DataFrame:\n")
    f.write("        return self.executor.get_open_positions()\n")

print(f"Created {ib_integration_path}")
