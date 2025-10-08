import os
import shutil
from ultralytics import YOLO
from backend.app.core.utils import load_cat_to_name
from backend.app.core.config import RESULT_DIR, MODEL_DIR
from datetime import datetime
from PIL import Image

# 加载类别映射（目录id -> "面值,货币,国家"）
cat_map = load_cat_to_name()

def run_inference(model_path: str, upload_file, save_result: bool = True):
    """
    对上传的图片运行硬币识别，返回检测结果和金额统计
    """
    # 临时保存上传的文件
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    input_path = os.path.join(RESULT_DIR, f"input_{timestamp}.jpg")
    with open(input_path, "wb") as f:
        shutil.copyfileobj(upload_file.file, f)

    # 加载模型
    model = YOLO(model_path)

    # 推理
    results = model.predict(source=input_path, save=save_result, project=RESULT_DIR, name=f"run_{timestamp}")

    # 提取识别结果
    detected = []
    total_value = 0.0

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls.cpu().numpy()[0])
            conf = float(box.conf.cpu().numpy()[0])
            # 从 cat_to_name.json 映射
            if str(cls_id) in cat_map:
                name_info = cat_map[str(cls_id)].split(",")  # e.g. "1 Cent,Australian dollar,australia"
                face_value = name_info[0]
                currency = name_info[1]
                country = name_info[2]

                detected.append({
                    "class_id": cls_id,
                    "confidence": round(conf, 3),
                    "face_value": face_value,
                    "currency": currency,
                    "country": country
                })

                try:
                    val_num = [float(s.replace("Cent", "").replace("Centavos", "").replace("元", "").strip())
                               for s in face_value.split() if s.replace(".", "", 1).isdigit()]
                    if val_num:
                        total_value += val_num[0]
                except Exception:
                    pass

    return {
        "file": os.path.basename(input_path),
        "detected": detected,
        "total_value": total_value,
        "result_image_url": f"/static/results/run_{timestamp}/{os.path.basename(input_path)}"
    }