from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import AnalyzeRequest, AnalyzeResponse, ExampleResponse
from app.services.audit_service import AuditService
from app.services.mindspore_service import MindSporeService
from app.services.rag_service import RagService
from app.services.mock_service import MockService
from app.services.deepseek_service import DeepSeekService
import json
import os

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

audit_service = AuditService()
mindspore_service = MindSporeService()
rag_service = RagService()
mock_service = MockService()
deepseek_service = DeepSeekService()

@app.get(f"{settings.API_PREFIX}/examples", response_model=ExampleResponse)
async def get_examples():
    return ExampleResponse(examples=[
        "系统需要支持用户快速登录，并且保证稳定运行。",
        "在首页点击商品分类，系统应展示对应分类下的所有在售商品，按销量降序排列，分页每页20条。",
        "我们需要一个大概能导出报表的功能，最好能导出Excel。"
    ])

@app.post(f"{settings.API_PREFIX}/analyze", response_model=AnalyzeResponse)
async def analyze_requirement(request: AnalyzeRequest):
    text = request.requirement_text
    
    # 1. 规则审计
    audit_res = audit_service.analyze(text)
    
    # 2. MindSpore 分类
    ms_res = mindspore_service.predict(text)
    
    # 3. RAG 检索
    rag_res = rag_service.search(text)
    
    # 4. GWT 和质量评分生成 (根据配置决定使用 Mock 还是真实大模型)
    if settings.USE_MOCK:
        llm_res = mock_service.generate_gwt(text, rag_res)
    else:
        llm_res = deepseek_service.generate_gwt(text, rag_res)
        
    # 合并 LLM 的评分结果
    audit_res = {
        "score": llm_res.get("score", audit_res["score"]),
        "risks": llm_res.get("risks", audit_res["risks"]),
        "radar_data": llm_res.get("radar_data", audit_res["radar_data"])
    }
    
    gwt_res = {
        "given": llm_res.get("given", ""),
        "when": llm_res.get("when", ""),
        "then": llm_res.get("then", ""),
        "improved_requirement": llm_res.get("improved_requirement", ""),
        "source": llm_res.get("source", "")
    }
        
    return AnalyzeResponse(
        audit=audit_res,
        mindspore=ms_res,
        rag=rag_res,
        gwt=gwt_res
    )

@app.post(f"{settings.API_PREFIX}/mindspore/predict")
async def mindspore_predict(request: AnalyzeRequest):
    return mindspore_service.predict(request.requirement_text)

@app.post(f"{settings.API_PREFIX}/rag/search")
async def rag_search(request: AnalyzeRequest):
    return rag_service.search(request.requirement_text)
