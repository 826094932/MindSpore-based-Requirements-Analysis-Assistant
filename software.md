# SmartPM-MindSpore 软件开发与维护文档

## 1. 项目简介

**SmartPM-MindSpore** 是一个集成了人工智能技术的智能产品需求管理（Product Management）演示项目。该项目旨在通过自动化手段，辅助产品经理和开发团队评估、优化和转化原始业务需求，从而提升软件工程上下游的沟通效率和交付质量。

### 1.1 核心目标
*   **自动化审计**：通过预定义的领域知识库与 NLP 语言规则引擎或者接入LLM，实现对原始需求文本的毫秒级扫描。系统能够精准识别并高亮显示诸如“快速”、“稳定”、“易用”等主观模糊词汇，同时主动探测逻辑矛盾、边界缺失等潜在合规风险，显著降低因需求歧义引发的后期返工成本。

*   **基于MindSpore智能分类**：依托 MindSpore 深度学习框架构建多维分类矩阵，对需求质量进行深度语义评估。模型不仅能基于海量样本自动将需求划分为“清晰”、“模糊”、“不完整”、“不可测试”四个核心等级，还能提供细分的质量得分，为项目决策提供量化的准入参考。

*   **知识检索 (RAG)**：集成检索增强生成 (Retrieval-Augmented Generation) 技术，打通企业级历史需求图谱。系统可基于向量数据库从海量沉淀的高质量需求案例中，实时检索出与当前上下文最为匹配的黄金标准示例，为分析师提供精准的对标参考与写作辅助。

*   **标准化输出**：深度融合大语言模型（灵活支持 DeepSeek 高性能模型或测试环境下的 Mock 模式），实现从非结构化文本到结构化标准的智能跃迁。系统能自动解析业务逻辑，将其重塑为标准化的 BDD (Behavior-Driven Development) 格式，生成符合 Given-When-Then (GWT) 规范的验收准则，确保业务、开发与测试三方在同一逻辑基准上协同。

---

## 2. 系统架构设计 (Architecture Design)

项目采用前后端分离架构，核心分为展示层、服务层、AI模型层和数据层。

### 2.1 技术栈 (Tech Stack)
*   **前端 (Frontend)**: React 18 + TypeScript + Vite + Tailwind CSS + Recharts

*   **后端 (Backend)**: FastAPI (Python 3.10+) + Uvicorn
*   **AI与机器学习**: MindSpore (轻量级分类模型), DeepSeek API (大模型处理)
*   **数据存储**: 本地 JSON 数据 (Seed/Training/Quality Rules) / 向量数据库

### 2.2 核心业务流 (Workflow)
1.  **用户输入**：用户通过前端交互界面提交原始需求文本。系统通过数据总线将其传输至后端处理中心，作为整个流水线的触发源，支持单条录入或批量导入模式。

2.  **规则审计**：后端 `AuditService` 实时加载本地专家规则库，利用正则表达式与关键词匹配算法对文本进行扫描。系统能精准提取并定位模糊词汇、禁用词及逻辑风险点，生成初步的审计报告。

3.  **模型预测**：后端 `MindSporeService` 启执行文本预处理与特征提取，将非结构化数据输入至预先训练好的深度学习模型中。系统根据模型推理结果，输出对应的质量分类标签及置信度，实现对需求可测试性的自动化预判。

4.  **RAG 检索**：后端 `RagService` 启动检索增强生成流程。基于余弦相似度或向量空间搜索算法，从向量数据库的历史沉淀中快速检索出 Top-K 条高相关度、高质量的参考需求，为后续的优化提供上下文支撑。

5.  **LLM 优化与生成**：系统将审计风险、分类结果与检索到的参考示例进行指令对齐（Prompt Engineering），通过 `DeepSeekService`（或在测试环境下调用 MockService）进行深度语义加工。系统最终输出多维度的质量评分，并自动生成重塑后的高质量需求描述及标准的 GWT (Given-When-Then) 验收准则。

6.  **可视化渲染**：前端接收后端推送的聚合分析数据，利用图表组件进行直观映射。系统通过雷达图展示多维质量评估评分、通过警告列表标注文本瑕疵、通过结构化卡片呈现生成的 BDD 标准，为用户提供一站式、可交互的需求洞察视图。
---

## 3. 环境配置与部署 (Environment Setup)

### 3.1 前置要求 (Prerequisites)
*   Python 3.10 及以上版本
*   Node.js 18.x 及以上版本，配套 npm
*   安装并配置好 MindSpore 环境 

### 3.2 环境变量配置 (.env)
在项目根目录创建 `.env` 文件，参考 `.env.example`：
```env
# 运行模式: MOCK 或 DEEPSEEK
RUN_MODE=MOCK

# DeepSeek API 配置 (若 RUN_MODE=DEEPSEEK 必须配置)
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_API_BASE=https://api.deepseek.com/v1
```

### 3.3 后端部署 (Backend Deployment)

1.  **进入后端目录**:
    ```bash
    cd backend
    ```
2.  **创建虚拟环境并激活** (推荐):
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```
3.  **安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **启动服务**:
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```
    后端启动后，可通过 `http://localhost:8000/docs` 访问 Swagger UI 接口文档。

### 3.4 前端部署 (Frontend Deployment)

1.  **进入前端目录**:
    ```bash
    cd frontend
    ```
2.  **安装依赖**:
    ```bash
    npm install
    ```
3.  **启动开发服务器**:
    ```bash
    npm run dev
    ```
    前端将默认运行在 `http://localhost:5173`。

---

## 4. 核心功能说明 (Core Features Detail)

### 4.1 规则审计引擎 (`audit_service.py`)
利用正则表达式与关键字匹配（数据源于 `quality_rules.json`），快速诊断需求中是否包含“快速”、“高效”、“稳定”等无法被精确测量的模糊词，并返回严重程度及修改建议。

### 4.2 MindSpore 需求质量分类 (`mindspore_service.py`)
一个轻量级前馈神经网络（FFN），使用 TF-IDF 或词袋模型作为特征提取器。
*   **训练脚本**: 

`backend/app/mindspore_model/train.py` 可重新加载 `training_samples.json` 生成新的模型权重。


### 4.3 RAG 检索 (`rag_service.py`)
检索增强生成（Retrieval-Augmented Generation）的轻量化实现。当前版本通过基于字符重合度的轻量级算法，从 `seed_knowledge.json` 中检索最相关的历史用例，为后续 LLM 生成提供 Few-Shot 参考。

### 4.4 验收标准生成与评分 (`deepseek_service.py` / `mock_service.py`)
将用户需求、审计风险、分类结果以及 RAG 检索的示例组装成 Prompt，调用 LLM (DeepSeek) 或 Mock服务进行：
1.  **维度评分**: 完整性、清晰度、可测试性、可实现性。LLM 根据多维度分析给出更为客观的分数。
2.  **需求重写**: 输出消除歧义的高质量需求。
3.  **GWT 拆解**: 生成详细的 Given, When, Then 验收条件。

---

## 5. 项目目录结构 (Directory Structure)

```text
d:\python\software\SmartPM-MindSpore-AI-Demo\
├── .env.example              # 环境变量配置模板
├── README.md                 # 项目快速启动指南
├── software.md               # 完整软件开发与维护文档 (本文档)
├── backend/                  # 后端服务
│   ├── requirements.txt      # Python 依赖
│   └── app/
│       ├── main.py           # FastAPI 入口
│       ├── config.py         # 配置管理
│       ├── schemas.py        # Pydantic 数据模型
│       ├── data/             # 本地 JSON 数据集
│       ├── mindspore_model/  # MindSpore 模型定义与训练推理逻辑
│       └── services/         # 核心业务逻辑服务
└── frontend/                 # 前端展示
    ├── package.json          # Node 依赖
    ├── vite.config.ts        # Vite 构建配置
    ├── tailwind.config.js    # Tailwind 样式配置
    └── src/
        ├── App.tsx           # 主页面布局
        ├── api/              # API 接口封装
        └── components/       # UI 独立组件 (雷达图、输入面板等)
```

---

## 6.deepseek Prompt 配置
综合评分
```
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
    ]
}}
"""
```
GWT模式
```
    "given": "验收标准前置条件...",
    "when": "验收标准触发条件...",
    "then": "验收标准预期结果...",
    "improved_requirement": "重写后的高质量需求..."
```
---

## 7. 未来升级与完善计划 (Upgrade & Improvement Plan)

当前的项目是一个简单的Demo，没有用到向量数据库，对LLM的Prompt的配置相对简单，所以为对未来规划核心还是针对检索、数据和LLM配置进一步优化。


1.  持续优化 DeepSeek 的 Prompt，演进为“辩论式”多智能体系统。引入“产品经理 Agent”、“架构师 Agent”和“测试专家 Agent”，在后台自动进行需求探讨、冲突检测和优化建议，由 LLM 主导整个需求评分环节。

2. 将当前基于字符重合度的检索，升级为基于向量嵌入（Embeddings）的检索机制（如引入 FAISS 或 ChromaDB），结合知识库大幅提升语义相似匹配的精度与上下文感知能力。

3. 端到端深度学习模型迭代，将目前的轻量级特征分类模型升级为基于 MindSpore 的深度文本模型（如 Transformer 架构），直接提取高维语义特征，提高不可测试性、模糊性与合规性识别的泛化能力。

4.  本项目中的数据是以简单的形式存储，将 json 存储替换为 PostgreSQL 等生产级数据库，支持多人并发协作、细粒度权限控制、需求历史版本记录以及完整的项目生命周期管理。

5. 生态工具链与 OpenAPI 集成，通过人工审核后，提供标准的 RESTful OpenAPI 或 Webhook，实现与 Jira、PingCode、Teambition 等主流研发管理工具的无缝对接，自动化同步需求变更与测试用例。
