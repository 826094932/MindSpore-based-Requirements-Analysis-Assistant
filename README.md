# SmartPM MindSpore AI Demo

这是一个精简版的可运行全栈 Demo，用于展示基于大模型与 MindSpore 的智能需求分析工作流。

## 项目简介
本项目演示了如何对输入的需求文本进行自动化审查：
1. **规则审计**：检测模糊词风险。
2. **MindSpore质量分类**：利用自定义训练的文本分类模型，评估需求属于 `clear` / `ambiguous` / `incomplete` / `untestable` 哪一类。
3. **RAG检索**：根据输入需求，从知识库中检索出历史高质量需求示例。
4. **GWT验收标准生成**：结合Mock/DeepSeek大模型，自动将需求改写为专业的 Given-When-Then 格式。

## 功能列表
- 实时需求文本分析
- 模糊词自动高亮与建议
- 基于 MindSpore 的需求质量分类 (文本分类)
- 本地基于 TF-IDF 的简易 RAG 检索
- Mock/DeepSeek 验收标准 (GWT) 自动生成
- 质量评分雷达图可视化

## 目录结构
```text
SmartPM-MindSpore-AI-Demo/
  backend/       # FastAPI 后端，包含 MindSpore 训练与推理逻辑
  frontend/      # React + Vite + Tailwind 前端
  README.md
```


### 后端启动
需要 Python 3.10+
1. 进入 `backend` 目录
2. 安装依赖: `pip install -r requirements.txt` (包含 mindspore)
3. 训练模型 (可选，如果没有预训练模型): `python app/mindspore_model/train.py`
4. 运行服务: `uvicorn app.main:app --reload --port 8000`

### 前端启动
需要 Node.js 18+
1. 进入 `frontend` 目录
2. 安装依赖: `npm install`
3. 运行服务: `npm run dev`


cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

cd frontend
npm install
npm run dev