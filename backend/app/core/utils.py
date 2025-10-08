import json
import os
from backend.app.core.config import DATA_DIR

def load_cat_to_name():
    json_path = os.path.join(DATA_DIR, "cat_to_name.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
