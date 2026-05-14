import os
import sys

# 添加 mindspore_model 目录到路径，以便导入
current_dir = os.path.dirname(os.path.abspath(__file__))
mindspore_dir = os.path.join(current_dir, '..', 'mindspore_model')
if mindspore_dir not in sys.path:
    sys.path.append(mindspore_dir)

class MindSporeService:
    def __init__(self):
        self.is_available = False
        try:
            from predict import RequirementPredictor
            self.predictor = RequirementPredictor()
            self.is_available = True
            print("MindSpore environment loaded successfully.")
        except Exception as e:
            print(f"MindSpore not fully available or model not trained, using fallback. Error: {e}")
            self.predictor = None

    def predict(self, text: str) -> dict:
        if self.is_available and self.predictor:
            try:
                category, confidence = self.predictor.predict(text)
                return {
                    "category": category,
                    "confidence": float(confidence),
                    "is_fallback": False
                }
            except Exception as e:
                print(f"Prediction error: {e}")
                
        # 降级处理：基于规则的简单分类
        return self._fallback_predict(text)
        
    def _fallback_predict(self, text: str) -> dict:
        if "快速" in text or "大概" in text:
            return {"category": "ambiguous", "confidence": 0.85, "is_fallback": True}
        elif len(text) < 10:
            return {"category": "incomplete", "confidence": 0.9, "is_fallback": True}
        else:
            return {"category": "clear", "confidence": 0.75, "is_fallback": True}
