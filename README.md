执行命令  python -m uvicorn backend.app.main:app --reload
Step 1：主入口 & 路由骨架
文件：main.py + api/router_train.py + api/router_result.py + api/router_infer.py
Step 2：推理模块 (infer_service)
	•	文件：services/infer_service.py + api/router_infer.py
Step 3：训练模块 (train_service)
	•	文件：services/train_service.py + api/router_train.py
	•	内容：基于你的 data/ 数据集训练 YOLOv11，并保存日志和模型。
Step 4：结果展示模块 (eval_service)
	•	文件：services/eval_service.py + api/router_result.py
	•	内容：从训练日志读取 loss / acc / mAP，返回 JSON 数据给前端绘图。
Step 5：业务逻辑打通
	•	训练完成 → 数据库里保存历史记录（时间、参数、模型路径）
	•	前端 /result/history 能选择训练记录 → 展示曲线