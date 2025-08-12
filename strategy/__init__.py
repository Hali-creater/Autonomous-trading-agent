import os
import pandas as pd
from abc import ABC, abstractmethod
import ta # Import technical analysis library

# Define the project directory based on the previous step
project_name = "autonomous_trading_agent"
strategy_dir = os.path.join(project_name, "strategy")
os.makedirs(strategy_dir, exist_ok=True) # Ensure directory exists
