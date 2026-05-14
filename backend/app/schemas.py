from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class AnalyzeRequest(BaseModel):
    requirement_text: str

class ExampleResponse(BaseModel):
    examples: List[str]

class RiskItem(BaseModel):
    word: str
    reason: str
    severity: str

class AuditResult(BaseModel):
    score: int
    risks: List[RiskItem]
    radar_data: List[Dict[str, Any]]

class MindSporeResult(BaseModel):
    category: str
    confidence: float
    is_fallback: bool = False

class RagResult(BaseModel):
    retrieved_examples: List[Dict[str, Any]]

class GwtResult(BaseModel):
    given: str
    when: str
    then: str
    improved_requirement: str
    source: str

class AnalyzeResponse(BaseModel):
    audit: AuditResult
    mindspore: MindSporeResult
    rag: RagResult
    gwt: GwtResult
