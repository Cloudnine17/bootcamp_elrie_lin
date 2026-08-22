import os
from pathlib import Path
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

def get_key(name: str, default=None):
    """Retrieve environment variable by key name."""
    return os.getenv(name, default)

# Load environment on import
load_env()

# Centralized paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / get_key("DATA_DIR", "./data")
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"