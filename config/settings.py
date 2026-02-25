import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Base Paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    INPUT_DIR = DATA_DIR / "inputs"
    DB_PATH = DATA_DIR / "diarizer.db"

    # API Setup
    API_KEY = os.getenv("QUBRID_API_KEY")
    API_URL = "https://platform.qubrid.com/api/v1/qubridai/audio/transcribe"
    MODEL_NAME = "openai/whisper-large-v3"

    @classmethod
    def setup_directories(cls):
        """Creates required directories instantly."""
        cls.INPUT_DIR.mkdir(parents=True, exist_ok=True)

config = Settings()