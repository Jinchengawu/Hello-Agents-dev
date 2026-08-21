# Hello-Agents 第 6–12 章本地演练归档

本目录按“章节-小节/实践名”归档《Hello-Agents》第 6 章至第 12 章需要本地运行的案例。代码基于上游提交 `45dd84e626a91997294ac8d4d44f18b29a411c6e`（2026-08-18）整理。

## 使用约定

每个实践使用独立虚拟环境，避免不同章节锁定的 `hello-agents`、protobuf、训练框架互相冲突：

```bash
cd <实践目录>
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env  # 目录存在模板时
```

只有占位配置被归档；请把真实密钥写入 `.env`，该文件已被 Git 忽略。不要直接运行含 LLM、云数据库、协议服务器、模型训练或基准下载的脚本，除非对应资源已配置。

## DeepSeek 统一配置

所有在线 LLM 调用已统一为 DeepSeek 的 OpenAI-compatible API。各实践的
`.env.example` 默认配置如下：

```dotenv
LLM_MODEL_ID=deepseek-v4-flash
LLM_API_KEY=your-deepseek-api-key
LLM_BASE_URL=https://api.deepseek.com
```

复制模板为 `.env` 后只需替换密钥。需要更高能力时，可把模型改为
`deepseek-v4-pro`。第 11 章的 Qwen 本地训练基座以及 RAG/Memory 的 embedding
模型不属于在线 LLM 调用，因此保持原配置。

## 实践索引

全部 29 个实践均已补充中文设计图。可从
[第 6–12 章中文设计图总索引](./DIAGRAM_INDEX.md) 进入，每个实践包含总流程、
UML 组件/类关系、UML 时序、生命周期、系统边界、数据流和排错决策 7 类图表。
每张图同时保存可编辑的 `.mmd` 源文件和可直接打开的 `.svg` 成品图。

第 6–12 章均已按大章节聚合。建议先从章节首页理解教学目标、实践关联和差异，
再进入具体案例：

[L6](./L6/README.md) · [L7](./L7/README.md) · [L8](./L8/README.md) ·
[L9](./L9/README.md) · [L10](./L10/README.md) · [L11](./L11/README.md) ·
[L12](./L12/README.md)

| 归档 | 应用 | 主要入口 | 资源/外部服务 |
|---|---|---|---|
| [`L6/L6-2/AutoGen`](./L6/L6-2/AutoGen/README.md) | 四智能体软件开发团队、比特币 Streamlit 应用 | `python main.py`；`python -m streamlit run output.py` | LLM、CoinGecko |
| [`L6/L6-3/AgentScope`](./L6/L6-3/AgentScope/README.md) | 三国狼人杀 | `python main_cn.py` | DeepSeek LLM |
| [`L6/L6-4/CAMEL`](./L6/L6-4/CAMEL/LEARNING_DIAGRAMS.md) | AI 科普电子书协作写作 | `python DigitalBookWriting.py` | LLM |
| [`L6/L6-5/LangGraph`](./L6/L6-5/LangGraph/LEARNING_DIAGRAMS.md) | 三步问答/旅游助手 | `python Dialogue_System.py` | LLM、Tavily |
| [`L7/L7-2/LLM-Extension`](./L7/L7-2/LLM-Extension/LEARNING_DIAGRAMS.md) | 多提供商 LLM 扩展 | `python my_main.py` | LLM |
| [`L7/L7-4/Agent-Patterns`](./L7/L7-4/Agent-Patterns/LEARNING_DIAGRAMS.md) | Simple、ReAct、Reflection、Plan-and-Solve、Function Calling | `python test_*.py`；`python function_call_demo.py` | LLM |
| [`L7/L7-5/Tool-System`](./L7/L7-5/Tool-System/LEARNING_DIAGRAMS.md) | 计算器与多源搜索工具 | `python test_my_calculator.py`；`python test_advanced_search.py` | 搜索密钥（后者） |
| [`L8/L8-2/Memory`](./L8/L8-2/Memory/LEARNING_DIAGRAMS.md) | 记忆基础、架构、工作记忆、整合、记忆类型 | 按 `01`、`02`、`03`、`06`、`09` 顺序 | Qdrant/Neo4j/Embedding（按示例） |
| [`L8/L8-3/RAG`](./L8/L8-3/RAG/LEARNING_DIAGRAMS.md) | 文档摄取、高级检索、智能问答、完整流水线 | 按 `04`、`05`、`07`、`10` 顺序 | Qdrant/Embedding |
| [`L8/L8-4/Document-QA`](./L8/L8-4/Document-QA/LEARNING_DIAGRAMS.md) | Agent 工具集成与 Gradio 文档助手 | `python 08_Agent_Tool_Integration.py`；`python 11_Q&A_Assistant.py` | LLM、数据库；Gradio |
| [`L9/L9-3/ContextBuilder`](./L9/L9-3/ContextBuilder/LEARNING_DIAGRAMS.md) | GSSC ContextBuilder | `python 01_context_builder_basic.py`；`python 02_context_builder_with_agent.py` | LLM/记忆/RAG |
| [`L9/L9-4/NoteTool`](./L9/L9-4/NoteTool/LEARNING_DIAGRAMS.md) | 结构化笔记及 Agent 集成 | `python 03_note_tool_operations.py`；`python 04_note_tool_integration.py` | 第二项需要 LLM |
| [`L9/L9-5/TerminalTool`](./L9/L9-5/TerminalTool/LEARNING_DIAGRAMS.md) | 文件系统即时访问 | `python 05_terminal_tool_examples.py` | 仅在示例目录执行 |
| [`L9/L9-6/Codebase-Maintainer`](./L9/L9-6/Codebase-Maintainer/LEARNING_DIAGRAMS.md) | 三日代码库维护工作流 | `python 06_three_day_workflow.py` | LLM；会写示例项目 |
| [`L10/L10-1/Quick-Start`](./L10/L10-1/Quick-Start/LEARNING_DIAGRAMS.md) | MCP/A2A/ANP 可用性检查 | `python 01_TestConnect.py` | 协议扩展 |
| [`L10/L10-2/MCP`](./L10/L10-2/MCP/LEARNING_DIAGRAMS.md) | MCP 连接、传输、工具与文档协作 | 按 `02`–`06` 顺序 | MCP 服务、GitHub/LLM |
| [`L10/L10-3/A2A`](./L10/L10-3/A2A/LEARNING_DIAGRAMS.md) | A2A 服务、客户端、网络、协商与客服 | 按 `07`–`10` 顺序 | 本地端口、LLM（部分） |
| [`L10/L10-4/ANP`](./L10/L10-4/ANP/LEARNING_DIAGRAMS.md) | 服务发现、任务分发、负载均衡 | 按 `11`–`13` 顺序 | LLM（任务分发） |
| [`L10/L10-5/Custom-MCP-Server`](./L10/L10-5/Custom-MCP-Server/LEARNING_DIAGRAMS.md) | 天气 MCP 服务器与 Agent | 先运行服务器，再运行 `14_test_weather_server.py`/`14_weather_agent.py` | 天气 API、端口 |
| [`L11/L11-1/Quick-Start`](./L11/L11-1/Quick-Start/LEARNING_DIAGRAMS.md) | Agentic RL 快速检查 | `python 00_quick_test.py` | CPU 可做配置检查 |
| [`L11/L11-2/Data-and-Rewards`](./L11/L11-2/Data-and-Rewards/LEARNING_DIAGRAMS.md) | GSM8K 数据与奖励函数 | `python 01_dataset_loading.py`；`python 02_reward_functions.py` | Hugging Face 数据集 |
| [`L11/L11-3/SFT`](./L11/L11-3/SFT/LEARNING_DIAGRAMS.md) | LoRA 配置与 SFT | `python 03_lora_configuration.py`；`python 04_sft_training.py` | GPU/模型/数据集 |
| [`L11/L11-4/GRPO`](./L11/L11-4/GRPO/LEARNING_DIAGRAMS.md) | GRPO 训练 | `python 05_grpo_training.py` | 高显存 GPU |
| [`L11/L11-5/Evaluation`](./L11/L11-5/Evaluation/LEARNING_DIAGRAMS.md) | 训练模型评估 | `python 07_model_evaluation.py` | 模型/数据集/GPU |
| [`L11/L11-6/Training-Pipeline`](./L11/L11-6/Training-Pipeline/LEARNING_DIAGRAMS.md) | 完整与分布式训练 | `python 06_complete_pipeline.py`；`python 08_distributed_training.py` | 多 GPU/Accelerate |
| [`L12/L12-1/Basic-Agent`](./L12/L12-1/Basic-Agent/LEARNING_DIAGRAMS.md) | 评估前的基础 Agent | `python 01_basic_agent_example.py` | LLM、搜索 |
| [`L12/L12-2/BFCL`](./L12/L12-2/BFCL/LEARNING_DIAGRAMS.md) | BFCL 快速、自定义与官方评估 | 按 `02`–`04` 顺序 | LLM、BFCL 数据/工具 |
| [`L12/L12-3/GAIA`](./L12/L12-3/GAIA/LEARNING_DIAGRAMS.md) | GAIA 快速与最佳实践 | `python 05_gaia_quick_start.py`；`python 06_gaia_best_practices.py` | LLM、HF Token、GAIA |
| [`L12/L12-4/Data-Generation-Evaluation`](./L12/L12-4/Data-Generation-Evaluation/LEARNING_DIAGRAMS.md) | AIME 生成、LLM Judge、Win Rate、人工验证 | 按 `07`–`09` 或 `data_generation/运行指南.md` | LLM、数据集；Gradio |

## 一键静态验证

静态验证不会调用 API、下载模型或启动服务：

```bash
python scripts/verify_archive.py
```

## 复用到其他课程

如果要让其他模型或 coding harness 按照本工程的目录、中文图表和验证规范继续生成
其他课程章节，可直接使用 [课程实践归档生成提示词](./COURSE_ARCHIVE_PROMPT.md)。

来源：<https://github.com/datawhalechina/hello-agents>
