from app import create_app
from config import Config
import os

def ensure_runtime_folders():
    for folder in Config.RUNTIME_FOLDERS:
        os.makedirs(folder, exist_ok=True)

if __name__ == "__main__":
    ensure_runtime_folders()
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

