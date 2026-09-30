#!/usr/bin/env python3
from dotenv import load_dotenv
import os


print("ORACLE STATUS: Reading the Matrix...")

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
MATRIX_MODE = os.getenv('MATRIX_MODE')
DATABASE_URL= os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
LOG_LEVEL = os.getenv('LOG_LEVEL')
ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')

# Example usage
print(f'MATRIX_MODE: {MATRIX_MODE}')
print(f'DATABASE_URL: {DATABASE_URL}')
print(f'API_KEY: {API_KEY}')
print(f'LOG_LEVEL: {LOG_LEVEL}')
print(f'ZION_ENDPOINT = {ZION_ENDPOINT}')


#########################################

# Laad de omgevingsvariabelen uit het .env bestand
# load_dotenv()

# VALID_MODES = ("development", "production")

# def get_config() -> dict[str, str]:
#     """Haalt de configuratie op basis van de omgevingsvariabelen."""
#     mode = os.getenv("MATRIX_MODE", "development")
    
#     if mode not in VALID_MODES:
#         mode = "development"
        
#     return {
#         "MATRIX_MODE": mode,
#         "DATABASE_URL": os.getenv("DATABASE_URL", "Not configured"),
#         "API_KEY": os.getenv("API_KEY", "Not configured"),
#         "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
#         "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "Not configured"),
#     }
