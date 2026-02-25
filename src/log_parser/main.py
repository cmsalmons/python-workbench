from pathlib import Path

current_file = Path(__file__)
project_root = current_file.parents[2]
log_path = project_root / "data" / "example.log"
with open(log_path, "r") as log_file:
    parsed_logs = []
    for line in log_file:
        clean_line = line.strip()
        parts = clean_line.split(" ", 1)
        log_level = parts[0]
        log_message = parts[1]
        log_entry = {
            "level": log_level,
            "message": log_message
        }
        parsed_logs.append(log_entry)

print(parsed_logs)