import json
import os
from typing import Dict, Any

class AuditService:
    def __init__(self):
        self.rules = self._load_rules()
        
    def _load_rules(self) -> list:
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'quality_rules.json')
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading rules: {e}")
            return []

    def analyze(self, text: str) -> Dict[str, Any]:
        risks = []
        score = 100
        
        radar_metrics = {
            "Clarity": 100,
            "Completeness": 100,
            "Testability": 100,
            "Feasibility": 100,
            "Consistency": 100
        }
        
        for rule in self.rules:
            word = rule.get('word', '')
            if word and word in text:
                severity = rule.get('severity', 'medium')
                risks.append({
                    "word": word,
                    "reason": rule.get('reason', '无具体原因'),
                    "severity": severity
                })
                # 简单计算扣分和雷达图
                deduct = 5 if severity == 'high' else 2
                score -= deduct
                
                # 随机降低一些雷达图维度
                if severity == 'high':
                    radar_metrics["Clarity"] -= 15
                    radar_metrics["Testability"] -= 10
                else:
                    radar_metrics["Completeness"] -= 5
                    
        # 归一化雷达图数据
        radar_data = [
            {"subject": k, "A": max(0, v), "fullMark": 100} 
            for k, v in radar_metrics.items()
        ]
        
        return {
            "score": max(0, score),
            "risks": risks,
            "radar_data": radar_data
        }
