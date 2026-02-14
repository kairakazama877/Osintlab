import os
import subprocess
from datetime import datetime
from config import Config

def run_scan(target):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{Config.RESULTS_DIR}/{target}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    result_data = {}

    def execute(cmd, filepath):
        with open(filepath, "w") as f:
            subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.STDOUT)

    if "@" not in target and "." not in target:
        file_path = f"{output_dir}/username.txt"
        execute(f"maigret {target}", file_path)
        result_data["username"] = file_path

    if "@" in target:
        file_path = f"{output_dir}/email.txt"
        execute(f"holehe {target}", file_path)
        result_data["email"] = file_path

    if "." in target:
        file_path = f"{output_dir}/domain.txt"
        execute(f"whois {target}", file_path)
        result_data["domain"] = file_path

    return result_data

