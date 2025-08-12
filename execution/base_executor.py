base_executor_path = os.path.join(execution_dir, "base_executor.py")
with open(base_executor_path, "w") as f:
    f.write("from abc import ABC, abstractmethod\n")
    f.write("import pandas as pd\n\n") # Import pandas for position/balance dataframes

    # 2. Define abstract base class BaseExecutor
    f.write("class BaseExecutor(ABC):\n")
    f.write("    @abstractmethod\n")
    f.write("    def place_order(self, symbol: str, order_type: str, quantity: float, price: float = None, stop_loss: float = None, take_profit: float = None):\n")
    f.write("        # order_type can be 'market', 'limit', etc.\n")
    f.write("        pass\n\n")

    f.write("    @abstractmethod\n")
    f.write("    def modify_order(self, order_id: str, new_quantity: float = None, new_price: float = None, new_stop_loss: float = None, new_take_profit: float = None):\n")
    f.write("        pass\n\n")

    f.write("    @abstractmethod\n")
    f.write("    def cancel_order(self, order_id: str):\n")
    f.write("        pass\n\n")

    f.write("    @abstractmethod\n")
    f.write("    def get_account_balance(self) -> float:\n")
    f.write("        pass\n\n")

    f.write("    @abstractmethod\n")
    f.write("    def get_open_positions(self) -> pd.DataFrame:\n")
    f.write("        pass\n")

print(f"Created {base_executor_path}")
