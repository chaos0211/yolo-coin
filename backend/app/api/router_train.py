from fastapi import APIRouter

router = APIRouter()

@router.post("/start")
def start_training():
    # TODO: 调用训练逻辑
    return {"message": "Training started"}
