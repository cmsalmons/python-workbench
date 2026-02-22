from pathlib import Path

current_file = Path(__file__)
project_root = current_file.parents[2]
log_path = project_root / "data" / "example.log"
with open(log_path, "r") as f:
    print(f.read())