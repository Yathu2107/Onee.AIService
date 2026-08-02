import os

from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")

MAX_LENGTH = int(os.getenv("MAX_LENGTH"))

DEVICE = os.getenv("DEVICE")

CONFIDENCE_THRESHOLD = float(
    os.getenv("CONFIDENCE_THRESHOLD")
)

API_VERSION = os.getenv("API_VERSION")

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError(
        "API_KEY is not set in the environment"
    )