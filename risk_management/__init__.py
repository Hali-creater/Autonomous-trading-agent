import os
import pandas as pd
import numpy as np

# Define the project directory based on the previous step
project_name = "autonomous_trading_agent"
risk_management_dir = os.path.join(project_name, "risk_management")
os.makedirs(risk_management_dir, exist_ok=True) # Ensure directory exists
