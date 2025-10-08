#!/bin/bash

# 确保在 yolo-coin 根目录执行
mkdir -p backend/app/{core,models,services,api,static,storage/{logs,models,results}}

# 创建 __init__.py 文件，确保是 Python 包
touch backend/app/{__init__.py,core/__init__.py,models/__init__.py,services/__init__.py,api/__init__.py}

# 创建核心文件
cat > backend/app/main.py <<EOF
from fastapi import FastAPI
from app.api import router_train, router_result, router_infer

app = FastAPI(title="YOLO Coin Backend")

# 注册路由
app.include_router(router_train.router, prefix="/train", tags=["Train"])
app.include_router(router_result.router, prefix="/result", tags=["Result"])
app.include_router(router_infer.router, prefix="/infer", tags=["Infer"])

@app.get("/")
def root():
    return {"message": "YOLO Coin Backend is running"}
EOF

cat > backend/app/core/config.py <<EOF
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "../../data")
MODEL_DIR = os.path.join(BASE_DIR, "storage/models")
LOG_DIR = os.path.join(BASE_DIR, "storage/logs")
RESULT_DIR = os.path.join(BASE_DIR, "storage/results")
EOF

cat > backend/app/core/utils.py <<EOF
import json
import os
from app.core.config import DATA_DIR

def load_cat_to_name():
    json_path = os.path.join(DATA_DIR, "cat_to_name.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
EOF

# API 路由文件骨架
cat > backend/app/api/router_train.py <<EOF
from fastapi import APIRouter

router = APIRouter()

@router.post("/start")
def start_training():
    # TODO: 调用训练逻辑
    return {"message": "Training started"}
EOF

cat > backend/app/api/router_result.py <<EOF
from fastapi import APIRouter

router = APIRouter()

@router.get("/history")
def get_training_history():
    # TODO: 返回训练历史
    return {"history": []}
EOF

cat > backend/app/api/router_infer.py <<EOF
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/predict")
async def predict_coin(file: UploadFile = File(...)):
    # TODO: 模型推理逻辑
    return {"result": "Coin detection result"}
EOF

# requirements.txt
cat > backend/requirements.txt <<EOF
fastapi
uvicorn
pydantic
torch
EOF

echo "✅ Backend structure generated successfully!"