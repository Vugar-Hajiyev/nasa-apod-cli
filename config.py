import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")
BASE_URL = "https://api.nasa.gov/planetary/apod"
IMAGE_DIR = Path(__file__).parent / "images"
