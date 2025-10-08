from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from backend.app.services.infer_service import run_inference
from backend.app.core.config import MODEL_DIR
import os

router = APIRouter()

@router.post("/predict")
async def predict_coin(
    file: UploadFile = File(...),
    model_name: str = Form("yolo11n.pt")   # 默认用yolo11n.pt
):
    model_path = os.path.join(MODEL_DIR, model_name)

    # 如果用户传的模型不存在，就退回默认预训练模型
    if not os.path.exists(model_path):
        model_path = model_name  # ultralytics 会自动下载 yolo11n.pt

    try:
        result = run_inference(model_path, file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {str(e)}")

@router.get("/models")
def list_models():
    models = [f for f in os.listdir(MODEL_DIR) if f.endswith(".pt")]
    return {"models": models}