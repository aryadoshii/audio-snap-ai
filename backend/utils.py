import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Path Configuration
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "inputs"
DB_PATH = DATA_DIR / "diarizer.db"

# Ensure directories exist
INPUT_DIR.mkdir(parents=True, exist_ok=True)

# API Configuration
API_KEY = os.getenv("QUBRID_API_KEY")
API_URL = "https://platform.qubrid.com/api/v1/qubridai/audio/transcribe"
MODEL_NAME = "openai/whisper-large-v3"