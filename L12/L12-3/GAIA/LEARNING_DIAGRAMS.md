# GAIA 通用 Agent 评估：中文设计图谱

本图谱对应 `L12/L12-3/GAIA`，入口为 `05_gaia_quick_start.py / 06_gaia_best_practices.py`。所有图均保留独立 Mermaid
源文件，节点、关系、状态和 UML Note 使用中文注释。

建议学习顺序：总流程 → UML 关系 → 调用时序 → 生命周期 → 系统边界 → 数据流 → 排错。

## 1. 总执行流程图

独立归档：[Mermaid 源文件](./diagrams/01-execution-flow.mmd) · [SVG 成品图](./diagrams/01-execution-flow.svg)。

```mermaid
%% 图 01：GAIA 通用 Agent 评估 总执行流程
%% 中文注释：实线为执行顺序，虚线为外部资源或记忆提示。
flowchart TD
    A["① 启动入口：05_gaia_quick_start.py / 06_gaia_best_practices.py"] --> S1["② 加载任务"]
    S1 --> S2["3 分析工具需求"]
    S2 --> S3["4 执行搜索或计算"]
    S3 --> S4["5 生成最终答案"]
    S4 --> S5["6 评分与总结"]
    S5 --> O["输出：标准化答案与得分"]
    R["外部依赖：DeepSeek API、Hugging Face、搜索工具"] -. "提供能力" .-> S2
    N["中文记忆注释：加载任务 → 分析工具需求 → 执行搜索或计算 → 生成最终答案 → 评分与总结"] -. "复习主线" .-> A
```
## 2. UML 组件/类关系图

独立归档：[Mermaid 源文件](./diagrams/02-uml-components.mmd) · [SVG 成品图](./diagrams/02-uml-components.svg)。

```mermaid
%% 图 02：GAIA 通用 Agent 评估 UML 组件/类关系图
%% 中文注释：该图表达学习层面的职责关系；概念组件不一定都是 Python 子类。
classDiagram
    class EntryModule {
        <<入口模块>>
        +load_config() 读取配置
        +run() 启动实践
    }
    class Core1 {
        <<核心组件 1>>
        +execute() 执行GAIA 数据集职责
    }
    class Core2 {
        <<核心组件 2>>
        +execute() 执行工具型 Agent职责
    }
    class Core3 {
        <<核心组件 3>>
        +execute() 执行任务执行器职责
    }
    class Core4 {
        <<核心组件 4>>
        +execute() 执行答案规范化与评分职责
    }
    class ExternalResource {
        <<外部资源>>
        +connect() 建立连接
    }
    EntryModule ..> Core1 : 创建或调用
    Core1 --> Core2 : 传递控制或数据
    Core2 --> Core3 : 传递控制或数据
    Core3 --> Core4 : 传递控制或数据
    Core4 ..> ExternalResource : 按需访问
    note for EntryModule "中文注释：实际入口为 05_gaia_quick_start.py / 06_gaia_best_practices.py"
    note for Core1 "中文职责：GAIA 数据集"
    note for Core2 "中文职责：工具型 Agent"
    note for Core3 "中文职责：任务执行器"
    note for Core4 "中文职责：答案规范化与评分"
    note for ExternalResource "中文注释：DeepSeek API、Hugging Face、搜索工具"
```
## 3. UML 时序图

独立归档：[Mermaid 源文件](./diagrams/03-sequence.mmd) · [SVG 成品图](./diagrams/03-sequence.svg)。

```mermaid
%% 图 03：GAIA 通用 Agent 评估 UML 时序图
%% 中文注释：纵向表示时间，箭头表示调用、数据或结果返回。
sequenceDiagram
    autonumber
    actor User as 学习者/调用方
    participant Entry as 入口脚本
    participant C1 as GAIA 数据集
    participant C2 as 工具型 Agent
    participant C3 as 任务执行器
    participant C4 as 答案规范化与评分
    participant Ext as 外部资源
    User->>Entry: 提供GAIA 多步骤任务
    Note over User,Entry: 中文注释：从 05_gaia_quick_start.py / 06_gaia_best_practices.py 启动
    Entry->>C1: 初始化并提交任务
    C1->>C2: 传递阶段结果
    C2->>C3: 传递阶段结果
    C3->>C4: 传递阶段结果
    C4->>Ext: 按需调用DeepSeek API、Hugging Face、搜索工具
    Ext-->>C4: 返回外部结果
    C4-->>Entry: 返回标准化答案与得分
    Entry-->>User: 展示结果或错误
    Note over Entry,Ext: 中文注释：异常时应保留上下文并明确失败阶段
```
## 4. 生命周期状态图

独立归档：[Mermaid 源文件](./diagrams/04-lifecycle-state.mmd) · [SVG 成品图](./diagrams/04-lifecycle-state.svg)。

```mermaid
%% 图 04：GAIA 通用 Agent 评估 生命周期状态图
%% 中文注释：正常路径逐步推进，任一关键阶段失败都进入错误状态。
stateDiagram-v2
    [*] --> S1: 启动
    state "加载任务" as S1
    state "分析工具需求" as S2
    state "执行搜索或计算" as S3
    state "生成最终答案" as S4
    state "评分与总结" as S5
    state "失败：记录原因并安全退出" as Failed
    state "完成：产物可检查" as Completed
    S1 --> S2: 阶段成功
    S2 --> S3: 阶段成功
    S3 --> S4: 阶段成功
    S4 --> S5: 阶段成功
    S5 --> Completed: 结果验证通过
    Completed --> [*]
    S1 --> Failed: 配置、依赖或执行异常
    S2 --> Failed: 配置、依赖或执行异常
    S3 --> Failed: 配置、依赖或执行异常
    S4 --> Failed: 配置、依赖或执行异常
    S5 --> Failed: 配置、依赖或执行异常
    Failed --> [*]
    note right of Failed
      中文注释：先定位当前阶段，再检查该阶段依赖
    end note
```
## 5. 系统边界图

独立归档：[Mermaid 源文件](./diagrams/05-system-boundary.mmd) · [SVG 成品图](./diagrams/05-system-boundary.svg)。

```mermaid
%% 图 05：GAIA 通用 Agent 评估 系统边界图
%% 中文注释：边界内是本地实践代码，边界外是网络、模型、数据库或运行设备。
flowchart LR
    I["输入：GAIA 多步骤任务"] --> C1
    subgraph Local["本地实践边界：L12/L12-3/GAIA"]
        C1["GAIA 数据集"]
        C2["工具型 Agent"]
        C3["任务执行器"]
        C4["答案规范化与评分"]
    end
    subgraph External["外部依赖边界"]
        R1["DeepSeek API"]
        R2["Hugging Face"]
        R3["搜索工具"]
    end
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C1 -. "访问" .-> R1
    C2 -. "访问" .-> R2
    C3 -. "访问" .-> R3
    C4 --> O["输出：标准化答案与得分"]
    N["中文注释：外部资源异常不应被误判为本地业务逻辑错误"] -.-> External
```
## 6. 数据流图

独立归档：[Mermaid 源文件](./diagrams/06-data-flow.mmd) · [SVG 成品图](./diagrams/06-data-flow.svg)。

```mermaid
%% 图 06：GAIA 通用 Agent 评估 数据流图
%% 中文注释：展示输入如何经过核心组件逐步变成可验证输出。
flowchart TD
    I["原始输入：GAIA 多步骤任务"] --> C1["处理 1：GAIA 数据集"]
    C1 --> C2["处理 2：工具型 Agent"]
    C2 --> C3["处理 3：任务执行器"]
    C3 --> C4["处理 4：答案规范化与评分"]
    C4 --> O["最终输出：标准化答案与得分"]
    R["资源数据：DeepSeek API、Hugging Face、搜索工具"] -. "补充上下文或算力" .-> C4
    V{结果是否可验证？}
    O --> V
    V -- 是 --> D[归档结果]
    V -- 否 --> E[记录失败阶段并修正配置]
```
## 7. 排错决策图

独立归档：[Mermaid 源文件](./diagrams/07-troubleshooting.mmd) · [SVG 成品图](./diagrams/07-troubleshooting.svg)。

```mermaid
%% 图 07：GAIA 通用 Agent 评估 启动与排错决策图
%% 中文注释：按“入口→环境→配置→外部依赖→业务结果”顺序排查。
flowchart TD
    A["现象：GAIA 通用 Agent 评估 无法正常运行"] --> B{"入口是否正确？"}
    B -- 否 --> B1["使用 05_gaia_quick_start.py / 06_gaia_best_practices.py"]
    B -- 是 --> C{"虚拟环境和 requirements 是否就绪？"}
    C -- 否 --> C1["激活 .venv 并安装 requirements.txt"]
    C -- 是 --> D{"环境变量、路径和配置是否完整？"}
    D -- 否 --> D1["复制 .env.example 并补齐必要配置"]
    D -- 是 --> E{"外部依赖是否可用？"}
    E -- 否 --> E1["检查 DeepSeek API、Hugging Face、搜索工具"]
    E -- 是 --> F{"输出是否符合预期？"}
    F -- 否 --> F1["定位阶段：加载任务 → 分析工具需求 → 执行搜索或计算 → 生成最终答案 → 评分与总结"]
    F -- 是 --> G["完成并归档：标准化答案与得分"]
    N["中文排错口诀：入口 → 环境 → 配置 → 依赖 → 结果"] -.-> A
```

## 8. 关键组件记忆表

| 编号 | 组件 | 记忆重点 |
|---|---|---|
| 1 | GAIA 数据集 | 对应流程中的核心职责节点 |
| 2 | 工具型 Agent | 对应流程中的核心职责节点 |
| 3 | 任务执行器 | 对应流程中的核心职责节点 |
| 4 | 答案规范化与评分 | 对应流程中的核心职责节点 |

输入：`GAIA 多步骤任务`  
输出：`标准化答案与得分`  
外部依赖：`DeepSeek API、Hugging Face、搜索工具`
