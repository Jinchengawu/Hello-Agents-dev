"""生成第 7–12 章的聚合学习首页和章节级中文 Mermaid 图。"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


CHAPTERS = (
    {
        "number": 7,
        "title": "构建你的智能体框架",
        "intro": "从使用现成框架进一步走向理解并实现框架内核，以分层解耦、职责单一和统一接口组织模型、Agent 范式与工具系统。",
        "objectives": (
            "理解自建框架的价值，以及核心层、Agent 层和工具层之间的依赖方向。",
            "用统一模型接口隔离不同 LLM Provider 的认证、地址和调用差异。",
            "比较 Simple、ReAct、Reflection、Plan-and-Solve 与 Function Calling 的控制循环。",
            "设计可注册、可校验、可组合并能安全执行的工具系统。",
            "能够从最小能力逐层扩展框架，而不把业务逻辑耦合到模型 SDK。",
        ),
        "foundations": ("统一配置与消息", "LLM 适配层", "Agent 推理循环", "工具注册与调用", "异常与可观测性"),
        "tradeoffs": (
            ("抽象统一与能力差异", "统一接口降低上层复杂度，但仍需保留不同模型在流式响应、函数调用和结构化输出方面的能力边界。"),
            ("自主推理与显式约束", "Agent 循环越自主，适应性越强；步骤越显式，成本、终止和错误恢复越容易控制。"),
        ),
        "projects": (
            ("L7-2", "LLM-Extension", "自定义 LLM Provider 扩展", "Provider 与统一模型接口", "适配外部模型服务", "配置驱动", "隔离 SDK 差异", "需要维护能力兼容性", "接入 DeepSeek 或其他 OpenAI-compatible 服务"),
            ("L7-4", "Agent-Patterns", "Agent 经典模式", "多种推理循环", "比较任务分解、行动和反思", "循环与终止条件", "理解范式差异", "不同模式成本差异明显", "为任务选择合适的 Agent 控制模式"),
            ("L7-5", "Tool-System", "Agent 工具系统", "BaseTool、Registry 与执行器", "扩展 Agent 外部能力", "参数校验与受控执行", "能力复用和组合", "工具边界与安全需额外设计", "构建计算、搜索和业务工具"),
        ),
        "decisions": (
            ("首要任务是接入或扩展模型 Provider？", "L7-2 LLM-Extension"),
            ("首要任务是比较 Agent 推理范式？", "L7-4 Agent-Patterns"),
            ("首要任务是构建可复用工具能力？", "L7-5 Tool-System"),
        ),
        "fallback": "先阅读架构目标，再从最小 SimpleAgent 开始",
        "source": "https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md",
    },
    {
        "number": 8,
        "title": "记忆与检索",
        "intro": "让智能体从只依赖当前提示，升级为能够保存经历、检索外部知识并以证据增强回答的持续学习系统。",
        "objectives": (
            "区分工作记忆、情景记忆、语义记忆与感知记忆的职责和生命周期。",
            "理解文档摄取、切分、向量化、召回、重排和生成组成的 RAG 链路。",
            "比较记忆检索与知识库检索：前者强调个体历史，后者强调外部事实。",
            "把记忆和 RAG 作为工具接入 Agent，并构建可交互的文档问答应用。",
            "识别向量数据库、Embedding、召回质量和数据更新带来的工程约束。",
        ),
        "foundations": ("信息摄取", "结构化与切分", "Embedding 表示", "索引与检索", "上下文注入与生成"),
        "tradeoffs": (
            ("记住更多与检索更准", "保存所有内容会增加噪声和成本；需要通过重要性、相关性、新近性和去重控制进入上下文的信息。"),
            ("实时知识与系统复杂度", "RAG 提高事实可更新性和可追溯性，但引入数据管道、索引一致性、召回评估和外部存储。"),
        ),
        "projects": (
            ("L8-2", "Memory", "Agent 记忆系统", "多类型记忆与存储后端", "保存和召回个体经历", "评分、整合与生命周期", "持续个性化", "容易积累噪声和过时信息", "长期助手、客户历史和跨会话任务"),
            ("L8-3", "RAG", "RAG 检索增强生成", "文档管道、向量检索与生成", "以外部知识增强回答", "检索流水线", "事实可更新且可追溯", "效果受切分和召回质量影响", "知识库、技术支持和企业搜索"),
            ("L8-4", "Document-QA", "文档问答助手", "RAGTool、Agent 与 Gradio", "把检索能力封装成交互应用", "端到端应用编排", "完整体验上传到问答", "部署和数据隔离要求更高", "面向用户的文档分析产品"),
        ),
        "decisions": (
            ("需要保存用户经历并跨会话个性化？", "L8-2 Memory"),
            ("需要从外部文档检索事实依据？", "L8-3 RAG"),
            ("需要交付可上传文档的完整问答应用？", "L8-4 Document-QA"),
        ),
        "fallback": "先明确信息来自个人历史还是外部知识库",
        "source": "https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md",
    },
    {
        "number": 9,
        "title": "上下文工程",
        "intro": "把上下文视为有限的注意力预算，通过压缩、结构化笔记、即时工具访问和分层协作，为长时程 Agent 持续提供最相关的信息。",
        "objectives": (
            "理解上下文腐蚀以及长窗口并不等于有效上下文。",
            "掌握 GSSC 流水线对目标、状态、步骤和上下文的组织方式。",
            "使用 NoteTool 建立跨会话、可检索的结构化长期笔记。",
            "使用 TerminalTool 按需获取文件和命令输出，避免一次性填满上下文。",
            "将多层上下文能力整合成长时程代码库维护工作流。",
        ),
        "foundations": ("目标与状态", "相关性和新近性", "压缩与筛选", "结构化持久笔记", "即时工具访问"),
        "tradeoffs": (
            ("预加载与即时访问", "预加载降低调用次数但容易产生噪声；JIT 访问节省窗口，却需要可靠的工具选择和权限控制。"),
            ("自动化与人类可控", "自动维护能提高长任务效率，但关键写操作、上下文压缩和阶段验收需要保留可审计边界。"),
        ),
        "projects": (
            ("L9-3", "ContextBuilder", "GSSC ContextBuilder", "Goal、State、Step、Context", "构造当前任务所需上下文", "评分、压缩与组装", "统一上下文入口", "质量取决于筛选策略", "复杂任务的动态上下文准备"),
            ("L9-4", "NoteTool", "结构化笔记工具", "Markdown、YAML 与检索", "保存跨会话知识", "显式增删改查", "持久且便于人工审阅", "需要维护结构和过期信息", "项目决策、进度和知识沉淀"),
            ("L9-5", "TerminalTool", "终端与文件系统工具", "命令、文件和安全规则", "即时获取本地真实状态", "白名单与受控执行", "避免大量内容预加载", "命令安全和输出截断复杂", "代码库、日志和数据文件调查"),
            ("L9-6", "Codebase-Maintainer", "三日代码库维护工作流", "ContextBuilder、笔记和终端组合", "执行跨会话长时程任务", "阶段计划与人工验收", "展示完整上下文工程", "状态恢复和副作用风险更高", "持续代码维护和复杂项目协作"),
        ),
        "decisions": (
            ("需要动态组装有限上下文预算？", "L9-3 ContextBuilder"),
            ("需要跨会话保存结构化事实和决策？", "L9-4 NoteTool"),
            ("需要按需读取文件或命令结果？", "L9-5 TerminalTool"),
            ("需要组合能力完成多日长任务？", "L9-6 Codebase-Maintainer"),
        ),
        "fallback": "先识别任务缺少的是状态、记忆还是即时证据",
        "source": "https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter9/%E7%AC%AC%E4%B9%9D%E7%AB%A0%20%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B.md",
    },
    {
        "number": 10,
        "title": "智能体通信协议",
        "intro": "用标准协议连接 Agent、工具、服务和其他 Agent，理解 MCP、A2A 与 ANP 分别解决能力调用、点对点协作和大规模网络发现问题。",
        "objectives": (
            "理解协议如何降低 Agent 与外部系统之间的定制适配成本。",
            "掌握 MCP 的工具发现、资源访问、调用和传输生命周期。",
            "掌握 A2A 的 Agent Card、任务、消息、工件和状态转换。",
            "理解 ANP 的服务注册、发现、路由和负载均衡定位。",
            "能够组合三种协议并实现一个可调用的自定义 MCP Server。",
        ),
        "foundations": ("能力描述", "发现与协商", "消息与任务", "传输和生命周期", "身份、安全与错误处理"),
        "tradeoffs": (
            ("统一标准与实现成熟度", "协议统一了边界，但 MCP、A2A、ANP 的生态成熟度和适用范围不同，不能只凭名称互换。"),
            ("去中心化与治理成本", "点对点或开放网络提高扩展性，同时增加身份、信任、路由、版本兼容和故障定位难度。"),
        ),
        "projects": (
            ("L10-1", "Quick-Start", "协议工具快速连接", "MCPTool、A2ATool、ANPTool", "快速感知三类协议入口", "统一 Tool 接口", "低成本建立全局认识", "不覆盖完整协议生命周期", "首次学习和环境连通性检查"),
            ("L10-2", "MCP", "MCP 连接与多 Agent 协作", "Server、Client、Transport 与 Tool", "Agent 与外部能力标准通信", "客户端—服务器", "生态成熟、工具边界清晰", "服务进程和权限管理复杂", "文件、数据库、GitHub 等工具接入"),
            ("L10-3", "A2A", "A2A 智能体通信", "Agent Card、Task 与 Artifact", "Agent 间委托、协商和协作", "点对点任务生命周期", "适合专业 Agent 团队", "发现和信任需额外基础设施", "研究、客服和跨 Agent 委托"),
            ("L10-4", "ANP", "ANP 服务发现与任务分发", "Registry、Router 与 Load Balancer", "构建大规模 Agent 网络", "注册发现与动态路由", "面向开放网络扩展", "生态和标准成熟度较低", "大量 Agent 的发现和负载分配"),
            ("L10-5", "Custom-MCP-Server", "自定义天气 MCP Server", "FastMCP 服务与天气工具", "实现并验证具体协议服务", "服务端工具发布", "形成端到端开发闭环", "需要处理外部 API 和服务运行", "把业务 API 发布为 Agent 工具"),
        ),
        "decisions": (
            ("只是想先比较三种协议的使用入口？", "L10-1 Quick-Start"),
            ("要让 Agent 标准化访问工具或数据？", "L10-2 MCP"),
            ("要让两个或少量 Agent 直接协作？", "L10-3 A2A"),
            ("要做大规模发现、路由和负载均衡？", "L10-4 ANP"),
            ("要亲手发布一个具体业务工具服务？", "L10-5 Custom-MCP-Server"),
        ),
        "fallback": "先明确通信对象是工具、Agent 还是 Agent 网络",
        "source": "https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter10/%E7%AC%AC%E5%8D%81%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE.md",
    },
    {
        "number": 11,
        "title": "Agentic-RL",
        "intro": "从数据和奖励定义开始，经过监督微调与 GRPO 强化学习，训练并评估具备推理和工具使用能力的智能体模型。",
        "objectives": (
            "理解 Agentic RL 与普通语言模型训练、传统强化学习之间的关系。",
            "将 GSM8K 等数据转换为 SFT 和 RL 所需格式，并设计可解释的奖励函数。",
            "使用 LoRA 和 SFT 建立稳定的行为起点。",
            "理解 GRPO 的采样、组内相对优势、奖励组合和策略更新过程。",
            "完成训练、评估、检查点管理和可选分布式执行的完整流水线。",
        ),
        "foundations": ("数据与格式", "奖励定义", "SFT 行为模仿", "GRPO 策略优化", "评估与检查点"),
        "tradeoffs": (
            ("训练收益与资源成本", "更完整的训练可能提升能力，但会显著增加显存、时间、数据质量和实验管理成本。"),
            ("奖励可计算与目标完整", "可验证奖励易于规模化，却可能遗漏友好性、鲁棒性等难量化目标，并产生奖励投机。"),
        ),
        "projects": (
            ("L11-1", "Quick-Start", "Agentic RL 快速实验", "最小数据、SFT 与 GRPO 检查", "验证训练环境和概念", "小样本快速路径", "低成本发现环境问题", "不能代表真实训练效果", "首次运行和配置验证"),
            ("L11-2", "Data-and-Rewards", "训练数据与奖励函数", "Dataset 与 RewardFunction", "定义模型学习材料和目标", "清洗、转换与打分", "训练目标可检查", "偏差会传递到全部训练阶段", "数据准备和奖励设计"),
            ("L11-3", "SFT", "LoRA 与监督微调", "基础模型、LoRA 与 SFT Trainer", "模仿高质量示范", "监督学习", "稳定、实现成熟", "受示范数据上限约束", "格式、指令和基础行为对齐"),
            ("L11-4", "GRPO", "GRPO 强化学习训练", "策略、候选组与奖励组合", "按结果奖励优化策略", "在线采样与相对优势", "可提升推理策略", "训练波动且资源消耗高", "数学推理和可验证任务"),
            ("L11-5", "Evaluation", "训练模型评估", "基线、生成、解析与指标", "衡量训练是否真正改进", "固定评估集对比", "防止凭主观样例判断", "受数据泄漏和指标覆盖影响", "模型选择和回归检测"),
            ("L11-6", "Training-Pipeline", "完整与分布式训练流水线", "数据、SFT、GRPO、Accelerate", "串联生产级训练阶段", "流水线与分布式执行", "端到端可复现", "硬件和故障恢复要求最高", "正式实验和多 GPU 训练"),
        ),
        "decisions": (
            ("只需检查环境和最小训练链路？", "L11-1 Quick-Start"),
            ("当前重点是准备数据或设计奖励？", "L11-2 Data-and-Rewards"),
            ("需要先用示范数据建立稳定行为？", "L11-3 SFT"),
            ("需要用可计算奖励继续优化策略？", "L11-4 GRPO"),
            ("需要比较基线与训练后模型？", "L11-5 Evaluation"),
            ("需要端到端或分布式正式训练？", "L11-6 Training-Pipeline"),
        ),
        "fallback": "先运行快速实验，再按数据→SFT→GRPO→评估推进",
        "source": "https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter11/%E7%AC%AC%E5%8D%81%E4%B8%80%E7%AB%A0%20Agentic-RL.md",
    },
    {
        "number": 12,
        "title": "智能体性能评估",
        "intro": "建立从评估对象、基准任务、预测解析到指标和报告的闭环，用可重复证据判断 Agent 的工具调用、综合任务和生成质量。",
        "objectives": (
            "理解 Agent 输出不确定性、指标多样性和评估成本带来的挑战。",
            "使用 BFCL 评估函数选择、参数生成和复杂函数调用能力。",
            "使用 GAIA 评估多步推理、搜索、文件处理和真实世界任务能力。",
            "结合规则指标、LLM Judge、Win Rate 与人工验证评估开放式输出。",
            "把评估结果用于回归检测、模型选择和后续数据生成。",
        ),
        "foundations": ("评估对象与版本", "数据集与任务切片", "预测记录与解析", "指标与裁判", "报告、误差分析与回归"),
        "tradeoffs": (
            ("客观自动化与语义覆盖", "AST 或精确匹配可复现但覆盖有限；LLM Judge 更接近语义质量，却引入偏差、成本和不可重复性。"),
            ("基准分数与真实价值", "公开基准便于横向比较，但可能发生数据污染，也不能替代面向实际业务失败模式的自定义评估。"),
        ),
        "projects": (
            ("L12-1", "Basic-Agent", "基础 Agent 评估对象", "LLM、Agent 与搜索工具", "建立可重复的被测系统", "固定配置和输出", "明确评估边界", "示例能力范围有限", "学习评估前的基线准备"),
            ("L12-2", "BFCL", "BFCL 函数调用评估", "函数题集、预测与 AST 匹配", "测量工具调用正确性", "结构化自动评分", "客观且适合回归", "不覆盖开放式综合任务", "API 选择和参数生成评估"),
            ("L12-3", "GAIA", "GAIA 通用 Agent 评估", "多步骤真实任务与准精确匹配", "测量综合助手能力", "端到端任务评分", "贴近真实复杂问题", "执行成本高且工具环境敏感", "搜索、推理、文件和多模态任务"),
            ("L12-4", "Data-Generation-Evaluation", "数据生成与多方式评估", "AIME、LLM Judge、Win Rate 与人工验证", "构建自定义开放式评估", "多裁判和对比统计", "覆盖业务特定质量", "裁判偏差和数据治理复杂", "生成质量、多模型对比和数据闭环"),
        ),
        "decisions": (
            ("需要先固定一个可重复的被测 Agent？", "L12-1 Basic-Agent"),
            ("主要评估函数或工具调用正确性？", "L12-2 BFCL"),
            ("主要评估真实世界综合任务能力？", "L12-3 GAIA"),
            ("需要自定义数据、LLM Judge 或胜率评估？", "L12-4 Data-Generation-Evaluation"),
        ),
        "fallback": "先定义失败模式，再选择基准、指标和裁判",
        "source": "https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md",
    },
)


def clean(value: str) -> str:
    return value.replace('"', "'").replace("\n", " ")


def render_readme(chapter: dict) -> str:
    number = chapter["number"]
    lines = [
        f'# 第{number}章：{chapter["title"]}', "",
        chapter["intro"], "",
        "> 本章只为需要本地演练的内容建立实践目录；理论说明和没有独立运行入口的",
        "> 小节统一在本首页建立知识联系，不创建空目录。", "",
        "## 本章主要教学目标", "",
    ]
    lines.extend(f"{index}. {item}" for index, item in enumerate(chapter["objectives"], 1))
    lines.extend(["", "## 各实践的共同基础", "", "这些实践虽然交付物不同，但共享以下工程主线：", "", "```text"])
    lines.append(" → ".join(chapter["foundations"]))
    lines.extend(["```", "", "学习时应重点观察同一能力如何从基础抽象逐步组合成完整应用。", "", "## 实践差异对比", "",
                  "| 实践 | 核心抽象 | 主要职责 | 控制方式 | 优势 | 局限 | 适用场景 |",
                  "|---|---|---|---|---|---|---|"])
    for subsection, folder, name, abstraction, role, control, strength, limitation, scenario in chapter["projects"]:
        lines.append(f"| {subsection} {name} | {abstraction} | {role} | {control} | {strength} | {limitation} | {scenario} |")
    lines.extend(["", "## 关键权衡", ""])
    for index, (title, body) in enumerate(chapter["tradeoffs"], 1):
        lines.extend([f"### {index}. {title}", "", body, ""])
    lines.extend(["## 建议学习顺序", ""])
    for index, project in enumerate(chapter["projects"], 1):
        subsection, folder, name = project[:3]
        lines.append(f"{index}. [{subsection} {name}](./{subsection}/{folder}/LEARNING_DIAGRAMS.md)")
    lines.extend(["", "每个实践目录都包含 `requirements.txt`、`.env.example`、`LEARNING_DIAGRAMS.md`，",
                  "以及保存 7 类中文 Mermaid/SVG 的 `diagrams/` 目录。", "", "## 章节级对比图", "",
                  "| 图表 | Mermaid 源文件 | SVG 成品图 |", "|---|---|---|",
                  "| 本章知识关联图 | [源文件](./diagrams/01-knowledge-map.mmd) | [SVG](./diagrams/01-knowledge-map.svg) |",
                  "| 实践范式与控制方式对比图 | [源文件](./diagrams/02-paradigm-comparison.mmd) | [SVG](./diagrams/02-paradigm-comparison.svg) |",
                  "| 按学习目标选择实践的决策图 | [源文件](./diagrams/03-practice-selection.mmd) | [SVG](./diagrams/03-practice-selection.svg) |",
                  "", "## 快速选择", "", "| 如果当前首先需要…… | 优先实践 |", "|---|---|"])
    for question, result in chapter["decisions"]:
        lines.append(f"| {question.rstrip('？')} | {result} |")
    lines.extend(["", f'来源：[Hello-Agents 第{number}章]({chapter["source"]})', ""])
    return "\n".join(lines)


def knowledge_map(chapter: dict) -> str:
    number = chapter["number"]
    lines = [f"%% L{number} 图 01：本章知识关联图", "%% 中文注释：从共同基础进入各实践，观察能力如何逐层组合。", "flowchart TD",
             f'    G["第{number}章目标：{clean(chapter["title"])}"] --> C["共同工程基础"]']
    for index, item in enumerate(chapter["foundations"], 1):
        lines.append(f'    C --> F{index}["{clean(item)}"]')
    for index, project in enumerate(chapter["projects"], 1):
        subsection, _, name, abstraction, role = project[:5]
        lines.extend([f'    G --> P{index}["{subsection} {clean(name)}"]',
                      f'    P{index} --> A{index}["核心：{clean(abstraction)}"]',
                      f'    A{index} --> R{index}["作用：{clean(role)}"]'])
    lines.append(f'    N["中文记忆注释：{clean(" → ".join(p[2] for p in chapter["projects"]))}"] -.-> G')
    return "\n".join(lines) + "\n"


def paradigm_comparison(chapter: dict) -> str:
    number = chapter["number"]
    lines = [f"%% L{number} 图 02：实践范式与控制方式对比", "%% 中文注释：每条分支依次展示实践的核心抽象、控制方式和突出权衡。",
             "flowchart LR", f'    G["第{number}章实践对比"]']
    for index, project in enumerate(chapter["projects"], 1):
        subsection, _, name, abstraction, _, control, strength, limitation, _ = project
        lines.extend([
            f'    G --> P{index}["{subsection} {clean(name)}"]',
            f'    P{index} --> A{index}["抽象：{clean(abstraction)}"]',
            f'    A{index} --> C{index}["控制：{clean(control)}"]',
            f'    C{index} --> T{index}["优势：{clean(strength)}<br/>注意：{clean(limitation)}"]',
        ])
    lines.extend([
        '    N1["中文注释：先比较职责，再比较控制和成本"] -.-> G',
        '    N2["中文注释：实践之间通常是组合关系，而非互斥替代"] -.-> G',
    ])
    return "\n".join(lines) + "\n"


def practice_selection(chapter: dict) -> str:
    number = chapter["number"]
    lines = [f"%% L{number} 图 03：按学习目标选择实践的决策图", "%% 中文注释：从当前最急需解决的问题出发，选择第一站，再沿建议顺序补齐其他能力。",
             "flowchart TD", f'    S["开始学习第{number}章"] --> Q1{{"{clean(chapter["decisions"][0][0])}"}}']
    for index, (question, result) in enumerate(chapter["decisions"], 1):
        lines.append(f'    Q{index} -- "是" --> P{index}["优先：{clean(result)}"]')
        if index < len(chapter["decisions"]):
            next_question = clean(chapter["decisions"][index][0])
            lines.append(f'    Q{index} -- "否" --> Q{index + 1}{{"{next_question}"}}')
        else:
            lines.append(f'    Q{index} -- "否" --> F["{clean(chapter["fallback"])}"]')
        lines.append(f'    P{index} --> V["完成最小演练并查看对应 7 张实践图"]')
    lines.extend(['    F --> V', '    V --> R{"是否能解释输入、状态、控制和输出？"}',
                  '    R -- "否" --> S', '    R -- "是" --> E["进入下一实践或真实项目"]',
                  '    N["中文选型注释：先按目标选第一站，再建立整章联系"] -.-> S'])
    return "\n".join(lines) + "\n"


def diagram_index(chapter: dict) -> str:
    number = chapter["number"]
    return f"""# L{number} 章节级中文设计图

本目录保存第{number}章跨实践对比图。每张图同时提供可编辑 Mermaid 图源和 SVG
成品，且在图源中保留中文注释。

| 图号 | 主题 | Mermaid | SVG |
|---|---|---|---|
| 01 | 本章知识关联 | [源文件](./01-knowledge-map.mmd) | [SVG](./01-knowledge-map.svg) |
| 02 | 实践范式与控制方式对比 | [源文件](./02-paradigm-comparison.mmd) | [SVG](./02-paradigm-comparison.svg) |
| 03 | 按学习目标选择实践 | [源文件](./03-practice-selection.mmd) | [SVG](./03-practice-selection.svg) |

章节说明和实践导航见 [第{number}章学习首页](../README.md)。
"""


def main() -> None:
    for chapter in CHAPTERS:
        chapter_dir = ROOT / f'L{chapter["number"]}'
        diagram_dir = chapter_dir / "diagrams"
        diagram_dir.mkdir(parents=True, exist_ok=True)
        (chapter_dir / "README.md").write_text(render_readme(chapter), encoding="utf-8")
        (diagram_dir / "README.md").write_text(diagram_index(chapter), encoding="utf-8")
        (diagram_dir / "01-knowledge-map.mmd").write_text(knowledge_map(chapter), encoding="utf-8")
        (diagram_dir / "02-paradigm-comparison.mmd").write_text(paradigm_comparison(chapter), encoding="utf-8")
        (diagram_dir / "03-practice-selection.mmd").write_text(practice_selection(chapter), encoding="utf-8")
    print(f"章节首页生成完成：{len(CHAPTERS)} 章，共 {len(CHAPTERS) * 3} 张章节图")


if __name__ == "__main__":
    main()
