import requests
import json
from app.config import settings
from typing import Dict, Any

class DeepSeekService:
    def __init__(self):
        self.api_key = settings.DEEPSEEK_API_KEY
        self.base_url = settings.DEEPSEEK_BASE_URL
        
    def _fallback_response(self, text: str, error_msg: str) -> Dict[str, Any]:
        return {
            "given": f"Error calling API: {error_msg}",
            "when": "Attempting to connect to LLM",
            "then": "Ensure network connectivity and valid API Key",
            "improved_requirement": "Failed to generate",
            "source": "DeepSeek (Error)",
            "score": 0,
            "risks": [{"word": "N/A", "reason": "API Failure", "severity": "high"}],
            "radar_data": [
                {"subject": "Clarity", "A": 0, "fullMark": 100},
                {"subject": "Completeness", "A": 0, "fullMark": 100},
                {"subject": "Testability", "A": 0, "fullMark": 100},
                {"subject": "Feasibility", "A": 0, "fullMark": 100},
                {"subject": "Consistency", "A": 0, "fullMark": 100}
            ]
        }
        
    def generate_gwt(self, text: str, rag_context: Dict[str, Any]) -> Dict[str, Any]:
        if not self.api_key:
            return self._fallback_response(text, "API Key is missing. Please configure DEEPSEEK_API_KEY in .env or enable USE_MOCK")
            
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        context_str = "\n".join([item['original'] for item in rag_context.get('retrieved_examples', [])])
        
        prompt = f"""
        你是一个资深产品经理。请分析以下用户需求并进行重写，同时给出质量评分。
        参考历史优质需求：
        {context_str}
        
        用户需求：
        {text}
        
        请严格以JSON格式返回，包含以下字段：
        {{
            "score": 综合评分(0-100的整数),
            "risks": [
                {{"word": "模糊词或风险词汇", "reason": "扣分原因", "severity": "high/medium/low"}}
            ],
            "radar_data": [
                {{"subject": "Clarity", "A": 分数(0-100), "fullMark": 100}},
                {{"subject": "Completeness", "A": 分数, "fullMark": 100}},
                {{"subject": "Testability", "A": 分数, "fullMark": 100}},
                {{"subject": "Feasibility", "A": 分数, "fullMark": 100}},
                {{"subject": "Consistency", "A": 分数, "fullMark": 100}}
            ],
            "given": "验收标准前置条件...",
            "when": "验收标准触发条件...",
            "then": "验收标准预期结果...",
            "improved_requirement": "重写后的高质量需求..."
        }}
        """
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}],
                    "response_format": {"type": "json_object"}
                },
                timeout=30
            )
            data = response.json()
            if "choices" not in data:
                return self._fallback_response(text, f"Unexpected response: {data}")
            content = data['choices'][0]['message']['content']
            parsed = json.loads(content)
            parsed["source"] = "DeepSeek API"
            
            # Ensure all required fields exist to prevent frontend crash
            parsed.setdefault("score", 85)
            parsed.setdefault("risks", [])
            parsed.setdefault("radar_data", [
                {"subject": "Clarity", "A": 85, "fullMark": 100},
                {"subject": "Completeness", "A": 85, "fullMark": 100},
                {"subject": "Testability", "A": 85, "fullMark": 100},
                {"subject": "Feasibility", "A": 85, "fullMark": 100},
                {"subject": "Consistency", "A": 85, "fullMark": 100}
            ])
            return parsed
        except Exception as e:
            return self._fallback_response(text, str(e))
