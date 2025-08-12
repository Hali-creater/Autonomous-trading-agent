import os
from abc import ABC, abstractmethod
from alpaca_trade_api.rest import REST # Import Alpaca REST API client
from dotenv import load_dotenv # Import dotenv for environment variables
import logging # Import logging for better reporting

load_dotenv() # Load environment variables from .env file

# Define the project directory
project_name = "autonomous_trading_agent"
execution_dir = os.path.join(project_name, "execution")
os.makedirs(execution_dir, exist_ok=True) # Ensure directory exists

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
