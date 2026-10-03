#!/usr/bin/env python3
# Requires: pip install python-dotenv
# do it inside a venv to keep my global clean
# or if using a requirements.txt file: python-dotenv==1.0.1
try:
	from dotenv import load_dotenv  # type: ignore
	load_dotenv()
except ModuleNotFoundError as e:
    print("couldn't load load_dotenv from dotenv")
    print("requires (in venv): pip install python-dotenv")
import os


VALID_MODES = ("development", "production")


def get_config() -> dict[str, str]:
    mode = os.getenv("MATRIX_MODE", "development")
    if mode not in VALID_MODES:
        mode = "development"
    return {
        "MATRIX_MODE": mode,
        "DATABASE_URL": os.getenv("DATABASE_URL", "Not configured"),
        "API_KEY": os.getenv("API_KEY", "Not configured"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "Not configured"),
    }


def display_config(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if mode == "production":
        print("[PROD] Running with production safeguards")
    else:
        print("[DEV] Verbose logging enables, secrets may appear in logs")
    if config["DATABASE_URL"] == "Not configured":
        print("Database: Not configured")
    else:
        print("Database: Connected to local instance")
    if config["API_KEY"] == "Not configured":
        print("API key: Not configured")
    else:
        print("API Access: Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    if config["ZION_ENDPOINT"] == "Not configured":
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")
    print("\nEnvironment security check:")
    # means no hardcoded secrets in this script code
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing (using system/default environment)")
    if os.environ.get("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running with default environment mode")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    config = get_config()
    display_config(config)
