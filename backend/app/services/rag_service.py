import json
import os
from typing import Dict, Any, List

class RagService:
    def __init__(self):
        self.seed_knowledge = self._load_knowledge()
        
    def _load_knowledge(self) -> List[Dict[str, str]]:
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'seed_knowledge.json')
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading seed knowledge: {e}")
            return []

    def search(self, query: str, top_k: int = 3) -> Dict[str, Any]:
        # Demo简化版：不使用真实的向量数据库，而是使用简单的关键词匹配来模拟检索
        results = []
        for item in self.seed_knowledge:
            text_to_match = item.get('original_requirement') or ""
            # 简单的相关性评分：查询词在示例文本中出现的次数
            score = sum(1 for char in query if char in text_to_match)
            mapped_item = {
                "original": text_to_match,
                "gwt": item.get('gwt_standard', ''),
                "quality_score": 90 + (score % 10)  # 模拟一个质量得分
            }
            results.append((score, mapped_item))
            
        # 按得分排序并取前 top_k
        results.sort(key=lambda x: x[0], reverse=True)
        top_results = [item for score, item in results[:top_k]]
        
        return {
            "retrieved_examples": top_results
        }
