import json
from pathlib import Path

def load_reference_data():
    with open(Path("app/data/reference_data.json"), "r", encoding="utf-8") as file:
        return json.load(file)
