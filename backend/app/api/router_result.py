from fastapi import APIRouter

router = APIRouter()

@router.get("/history")
def get_training_history():
    # TODO: 返回训练历史
    return {"history": []}
