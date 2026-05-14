from typing import Dict, Any

class MockService:
    def generate_gwt(self, text: str, rag_context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "given": "用户处于已登录状态，并在需求管理页面",
            "when": f"用户输入需求：'{text[:15]}...'",
            "then": "系统应该能够解析该需求，并返回质量分析报告，包括模糊词检测和建议",
            "improved_requirement": f"[Mock改写] 明确了前提条件和具体操作结果的高质量需求：{text}，要求响应时间<2s。",
            "source": "Mock Model",
            "score": 85,
            "risks": [
                {"word": "快速", "reason": "缺乏具体的时间指标，如‘2秒内’", "severity": "high"}
            ],
            "radar_data": [
                {"subject": "Clarity", "A": 80, "fullMark": 100},
                {"subject": "Completeness", "A": 90, "fullMark": 100},
                {"subject": "Testability", "A": 75, "fullMark": 100},
                {"subject": "Feasibility", "A": 85, "fullMark": 100},
                {"subject": "Consistency", "A": 95, "fullMark": 100}
            ]
        }
