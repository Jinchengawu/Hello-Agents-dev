"""为第 6–12 章实践生成统一、中文化、可独立归档的 Mermaid 学习图谱。"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Project:
    path: str
    title: str
    entry: str
    components: tuple[str, ...]
    stages: tuple[str, ...]
    inputs: str
    outputs: str
    resources: tuple[str, ...]
    preserve: bool = False


PROJECTS = (
    Project("L6/L6-2/AutoGen", "AutoGen 软件开发团队", "main.py / output.py",
            ("模型客户端", "四角色 Agent", "轮询团队", "Streamlit 成品应用"),
            ("读取配置", "创建角色", "轮询协作", "用户验收", "关闭客户端"),
            "开发任务", "协作记录与 Web 应用", ("DeepSeek API", "CoinGecko API"), True),
    Project("L6/L6-3/AgentScope", "AgentScope 三国狼人杀", "main_cn.py",
            ("游戏控制器", "ReActAgent 玩家", "MsgHub 消息中心", "角色与结构化输出"),
            ("分配角色", "夜晚行动", "白天讨论", "投票与技能", "判定胜负"),
            "玩家数量与角色规则", "游戏事件与胜负结果", ("DeepSeek API",)),
    Project("L6/L6-4/CAMEL", "CAMEL 电子书协作写作", "DigitalBookWriting.py",
            ("RolePlaying 会话", "心理学家 Agent", "作家 Agent", "任务完成检测"),
            ("加载任务", "初始化双角色", "交替写作", "检查完成标志", "输出电子书"),
            "电子书创作任务", "多轮协作内容", ("DeepSeek API",)),
    Project("L6/L6-5/LangGraph", "LangGraph 智能搜索助手", "Dialogue_System.py",
            ("SearchState 状态", "查询理解节点", "Tavily 搜索节点", "答案生成节点"),
            ("接收问题", "优化搜索词", "执行搜索", "生成答案", "保存会话状态"),
            "用户自然语言问题", "带来源的回答", ("DeepSeek API", "Tavily API")),
    Project("L7/L7-2/LLM-Extension", "自定义 LLM Provider 扩展", "my_main.py / my_llm.py",
            ("MyLLM 扩展类", "DeepSeek Provider 配置", "OpenAI-compatible 客户端", "流式输出"),
            ("读取配置", "解析 Provider", "创建客户端", "发送消息", "消费响应流"),
            "消息列表与模型配置", "DeepSeek 流式响应", ("DeepSeek API",)),
    Project("L7/L7-4/Agent-Patterns", "Agent 经典模式", "test_*.py / function_call_demo.py",
            ("SimpleAgent", "ReActAgent", "ReflectionAgent", "PlanSolve 与 FunctionCall"),
            ("选择模式", "构造 Agent", "执行推理循环", "调用工具或反思", "输出结果"),
            "任务与模式选择", "不同推理模式的结果", ("DeepSeek API", "可选工具")),
    Project("L7/L7-5/Tool-System", "Agent 工具系统", "test_my_calculator.py / test_advanced_search.py",
            ("CalculatorTool", "AdvancedSearchTool", "工具参数校验", "Agent 工具调用"),
            ("注册工具", "解析参数", "执行本地或远程工具", "处理异常", "返回工具结果"),
            "工具名称与参数", "计算或搜索结果", ("搜索服务 API",)),
    Project("L8/L8-2/Memory", "Agent 记忆系统", "01/02/03/06/09 系列脚本",
            ("工作记忆", "长期记忆", "记忆存储后端", "记忆整合与检索"),
            ("接收信息", "写入工作记忆", "持久化长期记忆", "检索与整合", "注入上下文"),
            "对话信息与记忆操作", "可检索的上下文记忆", ("Qdrant", "Neo4j", "Embedding 服务")),
    Project("L8/L8-3/RAG", "RAG 检索增强生成", "04/05/07/10 系列脚本",
            ("文档解析器", "切分与向量化", "向量检索", "智能问答流水线"),
            ("摄取文档", "切分文本", "生成向量", "召回上下文", "生成回答"),
            "文档与用户问题", "带检索上下文的回答", ("Qdrant", "Embedding 服务", "DeepSeek API")),
    Project("L8/L8-4/Document-QA", "文档问答助手", "08_Agent_Tool_Integration.py / 11_Q&A_Assistant.py",
            ("文档处理", "RAGTool", "问答 Agent", "Gradio 界面"),
            ("上传文档", "建立索引", "提交问题", "检索并生成", "界面展示"),
            "文档文件与问题", "文档依据回答", ("DeepSeek API", "向量数据库", "Gradio")),
    Project("L9/L9-3/ContextBuilder", "GSSC ContextBuilder", "01_context_builder_basic.py / 02_context_builder_with_agent.py",
            ("目标 Goal", "状态 State", "步骤 Step", "上下文构建器"),
            ("接收目标", "收集状态", "规划步骤", "压缩上下文", "交给 Agent"),
            "目标、状态与历史", "结构化 Agent 上下文", ("DeepSeek API", "Memory/RAG")),
    Project("L9/L9-4/NoteTool", "结构化笔记工具", "03_note_tool_operations.py / 04_note_tool_integration.py",
            ("NoteTool", "笔记存储", "搜索与摘要", "Agent 集成"),
            ("创建笔记", "读取与修改", "搜索笔记", "生成摘要", "Agent 使用结果"),
            "笔记内容与操作命令", "结构化笔记和摘要", ("本地文件", "DeepSeek API")),
    Project("L9/L9-5/TerminalTool", "终端与文件系统工具", "05_terminal_tool_examples.py",
            ("TerminalTool", "命令安全检查", "文件导航", "代码库维护辅助"),
            ("接收命令", "检查安全边界", "执行只读或受控操作", "解析输出", "返回 Agent"),
            "终端命令或文件任务", "受控命令输出", ("本地文件系统", "Shell")),
    Project("L9/L9-6/Codebase-Maintainer", "三日代码库维护工作流", "06_three_day_workflow.py / codebase_maintainer.py",
            ("CodebaseMaintainer", "TerminalTool", "ContextBuilder", "维护 Agent 团队"),
            ("扫描代码库", "发现问题", "制定维护计划", "执行变更", "验证与总结"),
            "待维护代码库", "维护报告与代码变更", ("DeepSeek API", "本地文件系统")),
    Project("L10/L10-1/Quick-Start", "协议工具快速连接", "01_TestConnect.py",
            ("MCPTool", "ANPTool", "A2ATool", "连接结果展示"),
            ("创建协议工具", "调用 MCP", "注册与发现 ANP", "创建 A2A 连接", "输出结果"),
            "协议操作参数", "连接与调用结果", ("MCP 服务", "ANP 注册表", "A2A 服务")),
    Project("L10/L10-2/MCP", "MCP 连接与多 Agent 协作", "02–06 系列脚本 / my_mcp_server.py",
            ("MCP 客户端", "Transport 传输层", "MCP 工具服务器", "多 Agent 文档助手"),
            ("启动或连接服务", "发现工具", "调用 MCP 工具", "Agent 使用结果", "关闭连接"),
            "MCP 请求与文档任务", "工具结果或协作文档", ("MCP Server", "GitHub MCP", "DeepSeek API")),
    Project("L10/L10-3/A2A", "A2A 智能体通信", "07–10 系列脚本",
            ("A2A Server", "A2A Client", "Agent Network", "协商与客服 Agent"),
            ("启动服务", "发布 Agent 能力", "客户端发现", "发送任务与协商", "返回结果"),
            "跨 Agent 任务", "A2A 消息与协作结果", ("本地 A2A 端口", "DeepSeek API")),
    Project("L10/L10-4/ANP", "ANP 服务发现与任务分发", "11_ANPInit.py / 12_ANPTaskDistribution.py / 13_ANPLoadBalancing.py",
            ("服务注册", "服务发现", "任务分发器", "负载均衡器"),
            ("初始化网络", "注册服务", "发现候选 Agent", "分配任务", "汇总执行结果"),
            "服务描述与任务", "路由和负载均衡结果", ("ANP 注册表", "DeepSeek API")),
    Project("L10/L10-5/Custom-MCP-Server", "自定义天气 MCP Server", "14_weather_mcp_server.py / 14_weather_agent.py",
            ("天气 MCP Server", "天气工具", "MCP 客户端 Agent", "集成测试"),
            ("启动服务器", "注册天气工具", "Agent 建立连接", "调用天气查询", "返回天气结果"),
            "城市与天气请求", "天气数据和 Agent 回答", ("天气 API", "本地 MCP 端口", "DeepSeek API")),
    Project("L11/L11-1/Quick-Start", "Agentic RL 快速实验", "00_quick_test.py",
            ("RLTrainingTool", "数据加载", "SFT 快速训练", "GRPO 与奖励函数"),
            ("加载小样本", "配置 SFT", "执行 SFT", "执行 GRPO", "检查奖励与产物"),
            "训练配置与小样本数据", "SFT/GRPO 测试模型", ("Hugging Face", "本地训练设备")),
    Project("L11/L11-2/Data-and-Rewards", "训练数据与奖励函数", "01_dataset_loading.py / 02_reward_functions.py",
            ("数据集加载器", "格式转换", "准确率奖励", "格式与过程奖励"),
            ("下载数据", "清洗与切分", "格式化样本", "计算奖励", "检查分布"),
            "GSM8K 等训练数据", "标准样本与奖励分数", ("Hugging Face Datasets",)),
    Project("L11/L11-3/SFT", "LoRA 与监督微调", "03_lora_configuration.py / 04_sft_training.py",
            ("基础模型", "LoRA 配置", "SFT Trainer", "检查点与适配器"),
            ("加载模型与数据", "注入 LoRA", "执行监督训练", "保存检查点", "验证训练结果"),
            "SFT 数据与训练配置", "LoRA 适配器和检查点", ("Hugging Face", "GPU/Apple Silicon")),
    Project("L11/L11-4/GRPO", "GRPO 强化学习训练", "05_grpo_training.py",
            ("策略模型", "奖励函数组", "GRPO Trainer", "训练监控"),
            ("加载策略与数据", "采样候选回答", "计算多项奖励", "更新策略", "保存模型"),
            "问题数据与奖励配置", "GRPO 策略模型", ("Hugging Face", "GPU")),
    Project("L11/L11-5/Evaluation", "训练模型评估", "07_model_evaluation.py",
            ("模型加载器", "评估数据集", "生成与解析", "指标统计器"),
            ("加载基线与模型", "读取评估集", "批量生成", "计算指标", "输出对比报告"),
            "模型检查点与评估题", "准确率和对比报告", ("Hugging Face", "GPU")),
    Project("L11/L11-6/Training-Pipeline", "完整与分布式训练流水线", "06_complete_pipeline.py / 08_distributed_training.py",
            ("数据流水线", "SFT 阶段", "GRPO 阶段", "Accelerate 分布式执行"),
            ("准备数据与环境", "运行 SFT", "运行 GRPO", "分布式同步", "评估并保存"),
            "训练配置、数据和基础模型", "完整训练产物", ("Hugging Face", "多 GPU/Accelerate")),
    Project("L12/L12-1/Basic-Agent", "基础 Agent 评估对象", "01_basic_agent_example.py",
            ("HelloAgentsLLM", "SimpleAgent", "SearchTool", "响应输出"),
            ("创建模型", "注册搜索工具", "提交问题", "工具调用与推理", "输出回答"),
            "需要最新信息的问题", "带搜索结果的 Agent 回答", ("DeepSeek API", "搜索 API")),
    Project("L12/L12-2/BFCL", "BFCL 函数调用评估", "02/03/04 系列脚本",
            ("BFCLDataset", "待评估 Agent", "BFCLEvaluator", "官方格式导出与评分"),
            ("加载 BFCL 样本", "Agent 生成函数调用", "解析预测", "官方评分", "输出准确率"),
            "BFCL 函数调用题集", "预测文件和评分报告", ("DeepSeek API", "BFCL/Gorilla 数据")),
    Project("L12/L12-3/GAIA", "GAIA 通用 Agent 评估", "05_gaia_quick_start.py / 06_gaia_best_practices.py",
            ("GAIA 数据集", "工具型 Agent", "任务执行器", "答案规范化与评分"),
            ("加载任务", "分析工具需求", "执行搜索或计算", "生成最终答案", "评分与总结"),
            "GAIA 多步骤任务", "标准化答案与得分", ("DeepSeek API", "Hugging Face", "搜索工具")),
    Project("L12/L12-4/Data-Generation-Evaluation", "数据生成与多方式评估", "07/08/09 系列脚本 / data_generation",
            ("AIME 数据生成器", "LLM Judge", "Win Rate 评估器", "报告与人工验证"),
            ("生成题目", "生成候选答案", "LLM Judge 打分", "计算胜率", "输出评估报告"),
            "AIME 参考题与生成配置", "生成数据、评分和报告", ("DeepSeek API", "Hugging Face", "Gradio")),
)


def quoted(text: str) -> str:
    return text.replace('"', "'").replace("\n", " ")


def flow(project: Project) -> str:
    lines = [
        f"%% 图 01：{project.title} 总执行流程",
        "%% 中文注释：实线为执行顺序，虚线为外部资源或记忆提示。",
        "flowchart TD",
        f'    A["① 启动入口：{quoted(project.entry)}"] --> S1["② {quoted(project.stages[0])}"]',
    ]
    for index, stage in enumerate(project.stages[1:], 2):
        lines.append(f'    S{index - 1} --> S{index}["{index + 1} {quoted(stage)}"]')
    lines.extend([
        f'    S{len(project.stages)} --> O["输出：{quoted(project.outputs)}"]',
        f'    R["外部依赖：{quoted("、".join(project.resources))}"] -. "提供能力" .-> S2',
        f'    N["中文记忆注释：{quoted(" → ".join(project.stages))}"] -. "复习主线" .-> A',
    ])
    return "\n".join(lines) + "\n"


def uml(project: Project) -> str:
    lines = [
        f"%% 图 02：{project.title} UML 组件/类关系图",
        "%% 中文注释：该图表达学习层面的职责关系；概念组件不一定都是 Python 子类。",
        "classDiagram",
        "    class EntryModule {",
        "        <<入口模块>>",
        "        +load_config() 读取配置",
        "        +run() 启动实践",
        "    }",
    ]
    for index, component in enumerate(project.components, 1):
        lines.extend([
            f"    class Core{index} {{",
            f"        <<核心组件 {index}>>",
            f"        +execute() 执行{quoted(component)}职责",
            "    }",
        ])
    lines.extend([
        "    class ExternalResource {",
        "        <<外部资源>>",
        "        +connect() 建立连接",
        "    }",
        "    EntryModule ..> Core1 : 创建或调用",
    ])
    for index in range(1, len(project.components)):
        lines.append(f"    Core{index} --> Core{index + 1} : 传递控制或数据")
    lines.extend([
        f"    Core{len(project.components)} ..> ExternalResource : 按需访问",
        f'    note for EntryModule "中文注释：实际入口为 {quoted(project.entry)}"',
    ])
    for index, component in enumerate(project.components, 1):
        lines.append(f'    note for Core{index} "中文职责：{quoted(component)}"')
    lines.append(
        f'    note for ExternalResource "中文注释：{quoted("、".join(project.resources))}"'
    )
    return "\n".join(lines) + "\n"


def sequence(project: Project) -> str:
    lines = [
        f"%% 图 03：{project.title} UML 时序图",
        "%% 中文注释：纵向表示时间，箭头表示调用、数据或结果返回。",
        "sequenceDiagram",
        "    autonumber",
        "    actor User as 学习者/调用方",
        "    participant Entry as 入口脚本",
    ]
    for index, component in enumerate(project.components, 1):
        lines.append(f"    participant C{index} as {quoted(component)}")
    lines.extend([
        "    participant Ext as 外部资源",
        f"    User->>Entry: 提供{quoted(project.inputs)}",
        f"    Note over User,Entry: 中文注释：从 {quoted(project.entry)} 启动",
        "    Entry->>C1: 初始化并提交任务",
    ])
    for index in range(1, len(project.components)):
        lines.append(f"    C{index}->>C{index + 1}: 传递阶段结果")
    lines.extend([
        f"    C{len(project.components)}->>Ext: 按需调用{quoted('、'.join(project.resources))}",
        f"    Ext-->>C{len(project.components)}: 返回外部结果",
        f"    C{len(project.components)}-->>Entry: 返回{quoted(project.outputs)}",
        "    Entry-->>User: 展示结果或错误",
        f"    Note over Entry,Ext: 中文注释：异常时应保留上下文并明确失败阶段",
    ])
    return "\n".join(lines) + "\n"


def state(project: Project) -> str:
    lines = [
        f"%% 图 04：{project.title} 生命周期状态图",
        "%% 中文注释：正常路径逐步推进，任一关键阶段失败都进入错误状态。",
        "stateDiagram-v2",
        "    [*] --> S1: 启动",
    ]
    for index, stage in enumerate(project.stages, 1):
        lines.append(f'    state "{quoted(stage)}" as S{index}')
    lines.extend([
        '    state "失败：记录原因并安全退出" as Failed',
        '    state "完成：产物可检查" as Completed',
    ])
    for index in range(1, len(project.stages)):
        lines.append(f"    S{index} --> S{index + 1}: 阶段成功")
    lines.extend([
        f"    S{len(project.stages)} --> Completed: 结果验证通过",
        "    Completed --> [*]",
    ])
    for index in range(1, len(project.stages) + 1):
        lines.append(f"    S{index} --> Failed: 配置、依赖或执行异常")
    lines.extend([
        "    Failed --> [*]",
        "    note right of Failed",
        "      中文注释：先定位当前阶段，再检查该阶段依赖",
        "    end note",
    ])
    return "\n".join(lines) + "\n"


def boundary(project: Project) -> str:
    components = "\n".join(
        f'        C{i}["{quoted(name)}"]' for i, name in enumerate(project.components, 1)
    )
    resources = "\n".join(
        f'        R{i}["{quoted(name)}"]' for i, name in enumerate(project.resources, 1)
    )
    resource_edges = "\n".join(
        f'    C{min(i, len(project.components))} -. "访问" .-> R{i}'
        for i in range(1, len(project.resources) + 1)
    )
    component_edges = "\n".join(
        f"    C{i} --> C{i + 1}" for i in range(1, len(project.components))
    )
    return f'''%% 图 05：{project.title} 系统边界图
%% 中文注释：边界内是本地实践代码，边界外是网络、模型、数据库或运行设备。
flowchart LR
    I["输入：{quoted(project.inputs)}"] --> C1
    subgraph Local["本地实践边界：{project.path}"]
{components}
    end
    subgraph External["外部依赖边界"]
{resources}
    end
{component_edges}
{resource_edges}
    C{len(project.components)} --> O["输出：{quoted(project.outputs)}"]
    N["中文注释：外部资源异常不应被误判为本地业务逻辑错误"] -.-> External
'''


def dataflow(project: Project) -> str:
    lines = [
        f"%% 图 06：{project.title} 数据流图",
        "%% 中文注释：展示输入如何经过核心组件逐步变成可验证输出。",
        "flowchart TD",
        f'    I["原始输入：{quoted(project.inputs)}"] --> C1["处理 1：{quoted(project.components[0])}"]',
    ]
    for index, component in enumerate(project.components[1:], 2):
        lines.append(f'    C{index - 1} --> C{index}["处理 {index}：{quoted(component)}"]')
    lines.extend([
        f'    C{len(project.components)} --> O["最终输出：{quoted(project.outputs)}"]',
        f'    R["资源数据：{quoted("、".join(project.resources))}"] -. "补充上下文或算力" .-> C{len(project.components)}',
        "    V{结果是否可验证？}",
        "    O --> V",
        "    V -- 是 --> D[归档结果]",
        "    V -- 否 --> E[记录失败阶段并修正配置]",
    ])
    return "\n".join(lines) + "\n"


def troubleshooting(project: Project) -> str:
    return f'''%% 图 07：{project.title} 启动与排错决策图
%% 中文注释：按“入口→环境→配置→外部依赖→业务结果”顺序排查。
flowchart TD
    A["现象：{quoted(project.title)} 无法正常运行"] --> B{{"入口是否正确？"}}
    B -- 否 --> B1["使用 {quoted(project.entry)}"]
    B -- 是 --> C{{"虚拟环境和 requirements 是否就绪？"}}
    C -- 否 --> C1["激活 .venv 并安装 requirements.txt"]
    C -- 是 --> D{{"环境变量、路径和配置是否完整？"}}
    D -- 否 --> D1["复制 .env.example 并补齐必要配置"]
    D -- 是 --> E{{"外部依赖是否可用？"}}
    E -- 否 --> E1["检查 {quoted('、'.join(project.resources))}"]
    E -- 是 --> F{{"输出是否符合预期？"}}
    F -- 否 --> F1["定位阶段：{quoted(' → '.join(project.stages))}"]
    F -- 是 --> G["完成并归档：{quoted(project.outputs)}"]
    N["中文排错口诀：入口 → 环境 → 配置 → 依赖 → 结果"] -.-> A
'''


DIAGRAMS = (
    ("01-execution-flow.mmd", "总执行流程图", flow),
    ("02-uml-components.mmd", "UML 组件/类关系图", uml),
    ("03-sequence.mmd", "UML 时序图", sequence),
    ("04-lifecycle-state.mmd", "生命周期状态图", state),
    ("05-system-boundary.mmd", "系统边界图", boundary),
    ("06-data-flow.mmd", "数据流图", dataflow),
    ("07-troubleshooting.mmd", "排错决策图", troubleshooting),
)


def render_learning_document(project: Project, rendered: list[tuple[str, str, str]]) -> str:
    sections = []
    for index, (filename, title, content) in enumerate(rendered, 1):
        svg_filename = filename.removesuffix(".mmd") + ".svg"
        sections.append(
            f"## {index}. {title}\n\n"
            f"独立归档：[Mermaid 源文件](./diagrams/{filename}) · "
            f"[SVG 成品图](./diagrams/{svg_filename})。\n\n"
            f"```mermaid\n{content}```\n"
        )
    component_rows = "\n".join(
        f"| {index} | {component} | 对应流程中的核心职责节点 |"
        for index, component in enumerate(project.components, 1)
    )
    return f'''# {project.title}：中文设计图谱

本图谱对应 `{project.path}`，入口为 `{project.entry}`。所有图均保留独立 Mermaid
源文件，节点、关系、状态和 UML Note 使用中文注释。

建议学习顺序：总流程 → UML 关系 → 调用时序 → 生命周期 → 系统边界 → 数据流 → 排错。

{''.join(sections)}
## 8. 关键组件记忆表

| 编号 | 组件 | 记忆重点 |
|---|---|---|
{component_rows}

输入：`{project.inputs}`  
输出：`{project.outputs}`  
外部依赖：`{'、'.join(project.resources)}`
'''


def generate_project(project: Project) -> None:
    if project.preserve:
        return
    project_dir = ROOT / project.path
    diagram_dir = project_dir / "diagrams"
    diagram_dir.mkdir(exist_ok=True)
    rendered: list[tuple[str, str, str]] = []
    for filename, title, renderer in DIAGRAMS:
        content = renderer(project)
        (diagram_dir / filename).write_text(content, encoding="utf-8")
        rendered.append((filename, title, content))

    rows = "\n".join(
        f"| {index} | {title} | [{filename}](./{filename}) | "
        f"[SVG](./{filename.removesuffix('.mmd')}.svg) |"
        for index, (filename, title, _) in enumerate(rendered, 1)
    )
    (diagram_dir / "README.md").write_text(
        f'''# {project.title}：设计图归档

| 编号 | 图表 | Mermaid 源文件 | SVG 成品图 |
|---|---|---|---|
{rows}

全部图使用中文节点和中文注释。完整讲解见
[LEARNING_DIAGRAMS.md](../LEARNING_DIAGRAMS.md)。
''',
        encoding="utf-8",
    )
    (project_dir / "LEARNING_DIAGRAMS.md").write_text(
        render_learning_document(project, rendered),
        encoding="utf-8",
    )


def generate_root_index() -> None:
    chapter_rows = "\n".join(
        f"| 第 {number} 章 | [章节学习首页](./L{number}/README.md) | "
        f"[章节对比图](./L{number}/diagrams/README.md) |"
        for number in range(6, 13)
    )
    rows = "\n".join(
        f"| `{project.path}` | {project.title} | "
        f"[图文讲解](./{project.path}/LEARNING_DIAGRAMS.md) | "
        f"[独立图源](./{project.path}/diagrams/README.md) |"
        for project in PROJECTS
    )
    (ROOT / "DIAGRAM_INDEX.md").write_text(
        f'''# 第 6–12 章中文设计图总索引

每个实践归档 7 类设计图：总流程、UML 组件/类关系、UML 时序、生命周期、
系统边界、数据流和排错决策。所有图均使用中文标签和中文注释。

## 章节级导航

| 章节 | 学习目标与差异对比 | 章节级图表 |
|---|---|---|
{chapter_rows}

## 实践级导航

| 实践目录 | 实践主题 | 图文讲解 | 独立图源 |
|---|---|---|---|
{rows}
''',
        encoding="utf-8",
    )


def main() -> None:
    for project in PROJECTS:
        generate_project(project)
    generate_root_index()
    print(f"设计图生成完成：{len(PROJECTS)} 个实践，统一 7 图规范")


if __name__ == "__main__":
    main()
