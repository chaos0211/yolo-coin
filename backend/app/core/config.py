import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "../../data")
MODEL_DIR = os.path.join(BASE_DIR, "storage/models")
LOG_DIR = os.path.join(BASE_DIR, "storage/logs")
RESULT_DIR = os.path.join(BASE_DIR, "storage/results")
