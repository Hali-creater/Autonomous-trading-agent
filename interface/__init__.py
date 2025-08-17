import streamlit as st
import os
import pandas as pd
import logging

# Configure logging for the dashboard itself
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the project directory
project_name = "autonomous_trading_agent"
interface_dir = os.path.join(project_name, "interface")
os.makedirs(interface_dir, exist_ok=True) # Ensure directory exists
