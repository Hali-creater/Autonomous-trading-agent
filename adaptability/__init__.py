import os
import pandas as pd
import ta # Import technical analysis library
import logging
import numpy as np

# Define the project directory
project_name = "autonomous_trading_agent"
adaptability_dir = os.path.join(project_name, "adaptability")
os.makedirs(adaptability_dir, exist_ok=True) # Ensure directory exists

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
