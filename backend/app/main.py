from fastapi import FastAPI
from backend.app.api import router_train, router_result, router_infer



app = FastAPI(title="YOLO Coin Backend")

# 注册路由
app.include_router(router_train.router, prefix="/train", tags=["Train"])
app.include_router(router_result.router, prefix="/result", tags=["Result"])
app.include_router(router_infer.router, prefix="/infer", tags=["Infer"])

@app.get("/")
def root():
    return {"message": "YOLO Coin Backend is running"}


from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="backend/app/storage"), name="static")
