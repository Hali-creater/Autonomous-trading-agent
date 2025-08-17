config_init_path = os.path.join(config_dir, "__init__.py")
if not os.path.exists(config_init_path):
    with open(config_init_path, "w") as f:
        f.write("# config module __init__.py\n")
        f.write("from .config_loader import load_config\n")
    print(f"Created {config_init_path}")
else:
    print(f"{config_init_path} already exists.")


# Create config/config_loader.py
config_loader_path = os.path.join(config_dir, "config_loader.py")
with open(config_loader_path, "w") as f:
    f.write("import os\n")
    f.write("from dotenv import load_dotenv\n")
    f.write("import logging\n\n")

    f.write("logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\n\n")

    f.write("def load_config():\n")
    f.write("    \"\"\"\n")
    f.write("    Loads configuration from environment variables or a .env file.\n\n")
    f.write("    Looks for a .env file in the project root directory and loads variables\n")
    f.write("    from it. Environment variables take precedence over .env file values.\n\n")
    f.write("    Returns:\n")
    f.write("        A dictionary containing loaded configuration values.\n")
    f.write("    \"\"\"\n")
    f.write("    # Attempt to load from .env file\n")
    f.write("    load_dotenv() # This looks for .env in the current directory and its parents\n\n")

    f.write("    config = {\n")
    f.write("        # Broker Configuration\n")
    f.write("        'BROKER': os.getenv('BROKER', 'Alpaca'), # Default to Alpaca if not set\n")
    f.write("        'ALPACA_API_KEY_ID': os.getenv('ALPACA_API_KEY_ID'),\n")
    f.write("        'ALPACA_API_SECRET_KEY': os.getenv('ALPACA_API_SECRET_KEY'),\n")
    f.write("        'ALPACA_BASE_URL': os.getenv('ALPACA_BASE_URL', 'https://paper-api.alpaca.markets'),\n")
    f.write("        'IB_HOST': os.getenv('IB_HOST', '127.0.0.1'),\n")
    f.write("        'IB_PORT': int(os.getenv('IB_PORT', 7496)), # Default to IB TWS paper trading port\n")
    f.write("        'IB_CLIENT_ID': int(os.getenv('IB_CLIENT_ID', 1)),\n")
    f.write("        'BINANCE_API_KEY': os.getenv('BINANCE_API_KEY'),\n")
    f.write("        'BINANCE_API_SECRET': os.getenv('BINANCE_API_SECRET'),\n")
    f.write("        'BINANCE_BASE_URL': os.getenv('BINANCE_BASE_URL', 'https://api.binance.com'),\n")
    f.write("        'OANDA_ACCOUNT_ID': os.getenv('OANDA_ACCOUNT_ID'),\n")
    f.write("        'OANDA_API_KEY': os.getenv('OANDA_API_KEY'),\n")
    f.write("        'OANDA_BASE_URL': os.getenv('OANDA_BASE_URL', 'https://api-fxpractice.oanda.com'),\n\n")

    f.write("        # Trading Parameters\n")
    f.write("        'SYMBOLS': [s.strip() for s in os.getenv('SYMBOLS', 'AAPL').split(',') if s.strip()], # Default to AAPL\n")
    f.write("        'TRADE_QUANTITY': float(os.getenv('TRADE_QUANTITY', 10)), # Default quantity\n")
    f.write("        'RISK_PER_TRADE_PERCENTAGE': float(os.getenv('RISK_PER_TRADE_PERCENTAGE', 0.01)), # Default 1%\n")
    f.write("        'DAILY_RISK_LIMIT_PERCENTAGE': float(os.getenv('DAILY_RISK_LIMIT_PERCENTAGE', 0.05)), # Default 5%\n")
    f.write("        'PVG_SHORT_PERIOD': int(os.getenv('PVG_SHORT_PERIOD', 14)),\n")
    f.write("        'PVG_LONG_PERIOD': int(os.getenv('PVG_LONG_PERIOD', 50)),\n")
    f.write("        'SMC_LOOKBACK': int(os.getenv('SMC_LOOKBACK', 20)),\n")
    f.write("        'TPR_VOLUME_PERIOD': int(os.getenv('TPR_VOLUME_PERIOD', 20)),\n")
    f.write("        # Add other strategy or risk parameters here\n\n")

    f.write("        # Deployment Settings\n")
    f.write("        'ENVIRONMENT': os.getenv('ENVIRONMENT', 'development'),\n")
    f.write("        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),\n")
    f.write("    }\n\n")

    f.write("    # Configure logging based on loaded LOG_LEVEL\n")
    f.write("    log_level = getattr(logging, config['LOG_LEVEL'].upper(), logging.INFO)\n")
    f.write("    logging.getLogger().setLevel(log_level)\n")
    f.write("    logging.info(f\"Configuration loaded. Broker: {config['BROKER']}, Environment: {config['ENVIRONMENT']}\")\n\n")


    f.write("    return config\n")

print(f"Created {config_loader_path} with load_config function.")
