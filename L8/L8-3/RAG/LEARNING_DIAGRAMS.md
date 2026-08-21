# RAG 检索增强生成：中文设计图谱

本图谱对应 `L8/L8-3/RAG`，入口为 `04/05/07/10 系列脚本`。所有图均保留独立 Mermaid
源文件，节点、关系、状态和 UML Note 使用中文注释。

建议学习顺序：总流程 → UML 关系 → 调用时序 → 生命周期 → 系统边界 → 数据流 → 排错。

## 1. 总执行流程图

独立归档：[Mermaid 源文件](./diagrams/01-execution-flow.mmd) · [SVG 成品图](./diagrams/01-execution-flow.svg)。

```mermaid
%% 图 01：RAG 检索增强生成 总执行流程
%% 中文注释：实线为执行顺序，虚线为外部资源或记忆提示。
flowchart TD
    A["① 启动入口：04/05/07/10 系列脚本"] --> S1["② 摄取文档"]
    S1 --> S2["3 切分文本"]
    S2 --> S3["4 生成向量"]
    S3 --> S4["5 召回上下文"]
    S4 --> S5["6 生成回答"]
    S5 --> O["输出：带检索上下文的回答"]
    R["外部依赖：Qdrant、Embedding 服务、DeepSeek API"] -. "提供能力" .-> S2
    N["中文记忆注释：摄取文档 → 切分文本 → 生成向量 → 召回上下文 → 生成回答"] -. "复习主线" .-> A
```
## 2. UML 组件/类关系图

独立归档：[Mermaid 源文件](./diagrams/02-uml-components.mmd) · [SVG 成品图](./diagrams/02-uml-components.svg)。

```mermaid
%% 图 02：RAG 检索增强生成 UML 组件/类关系图
%% 中文注释：该图表达学习层面的职责关系；概念组件不一定都是 Python 子类。
classDiagram
    class EntryModule {
        <<入口模块>>
        +load_config() 读取配置
        +run() 启动实践
    }
    class Core1 {
        <<核心组件 1>>
        +execute() 执行文档解析器职责
    }
    class Core2 {
        <<核心组件 2>>
        +execute() 执行切分与向量化职责
    }
    class Core3 {
        <<核心组件 3>>
        +execute() 执行向量检索职责
    }
    class Core4 {
        <<核心组件 4>>
        +execute() 执行智能问答流水线职责
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
    note for EntryModule "中文注释：实际入口为 04/05/07/10 系列脚本"
    note for Core1 "中文职责：文档解析器"
    note for Core2 "中文职责：切分与向量化"
    note for Core3 "中文职责：向量检索"
    note for Core4 "中文职责：智能问答流水线"
    note for ExternalResource "中文注释：Qdrant、Embedding 服务、DeepSeek API"
```
## 3. UML 时序图

独立归档：[Mermaid 源文件](./diagrams/03-sequence.mmd) · [SVG 成品图](./diagrams/03-sequence.svg)。

```mermaid
%% 图 03：RAG 检索增强生成 UML 时序图
%% 中文注释：纵向表示时间，箭头表示调用、数据或结果返回。
sequenceDiagram
    autonumber
    actor User as 学习者/调用方
    participant Entry as 入口脚本
    participant C1 as 文档解析器
    participant C2 as 切分与向量化
    participant C3 as 向量检索
    participant C4 as 智能问答流水线
    participant Ext as 外部资源
    User->>Entry: 提供文档与用户问题
    Note over User,Entry: 中文注释：从 04/05/07/10 系列脚本 启动
    Entry->>C1: 初始化并提交任务
    C1->>C2: 传递阶段结果
    C2->>C3: 传递阶段结果
    C3->>C4: 传递阶段结果
    C4->>Ext: 按需调用Qdrant、Embedding 服务、DeepSeek API
    Ext-->>C4: 返回外部结果
    C4-->>Entry: 返回带检索上下文的回答
    Entry-->>User: 展示结果或错误
    Note over Entry,Ext: 中文注释：异常时应保留上下文并明确失败阶段
```
## 4. 生命周期状态图

独立归档：[Mermaid 源文件](./diagrams/04-lifecycle-state.mmd) · [SVG 成品图](./diagrams/04-lifecycle-state.svg)。

```mermaid
%% 图 04：RAG 检索增强生成 生命周期状态图
%% 中文注释：正常路径逐步推进，任一关键阶段失败都进入错误状态。
stateDiagram-v2
    [*] --> S1: 启动
    state "摄取文档" as S1
    state "切分文本" as S2
    state "生成向量" as S3
    state "召回上下文" as S4
    state "生成回答" as S5
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
%% 图 05：RAG 检索增强生成 系统边界图
%% 中文注释：边界内是本地实践代码，边界外是网络、模型、数据库或运行设备。
flowchart LR
    I["输入：文档与用户问题"] --> C1
    subgraph Local["本地实践边界：L8/L8-3/RAG"]
        C1["文档解析器"]
        C2["切分与向量化"]
        C3["向量检索"]
        C4["智能问答流水线"]
    end
    subgraph External["外部依赖边界"]
        R1["Qdrant"]
        R2["Embedding 服务"]
        R3["DeepSeek API"]
    end
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C1 -. "访问" .-> R1
    C2 -. "访问" .-> R2
    C3 -. "访问" .-> R3
    C4 --> O["输出：带检索上下文的回答"]
    N["中文注释：外部资源异常不应被误判为本地业务逻辑错误"] -.-> External
```
## 6. 数据流图

独立归档：[Mermaid 源文件](./diagrams/06-data-flow.mmd) · [SVG 成品图](./diagrams/06-data-flow.svg)。

```mermaid
%% 图 06：RAG 检索增强生成 数据流图
%% 中文注释：展示输入如何经过核心组件逐步变成可验证输出。
flowchart TD
    I["原始输入：文档与用户问题"] --> C1["处理 1：文档解析器"]
    C1 --> C2["处理 2：切分与向量化"]
    C2 --> C3["处理 3：向量检索"]
    C3 --> C4["处理 4：智能问答流水线"]
    C4 --> O["最终输出：带检索上下文的回答"]
    R["资源数据：Qdrant、Embedding 服务、DeepSeek API"] -. "补充上下文或算力" .-> C4
    V{结果是否可验证？}
    O --> V
    V -- 是 --> D[归档结果]
    V -- 否 --> E[记录失败阶段并修正配置]
```
## 7. 排错决策图

独立归档：[Mermaid 源文件](./diagrams/07-troubleshooting.mmd) · [SVG 成品图](./diagrams/07-troubleshooting.svg)。

```mermaid
%% 图 07：RAG 检索增强生成 启动与排错决策图
%% 中文注释：按“入口→环境→配置→外部依赖→业务结果”顺序排查。
flowchart TD
    A["现象：RAG 检索增强生成 无法正常运行"] --> B{"入口是否正确？"}
    B -- 否 --> B1["使用 04/05/07/10 系列脚本"]
    B -- 是 --> C{"虚拟环境和 requirements 是否就绪？"}
    C -- 否 --> C1["激活 .venv 并安装 requirements.txt"]
    C -- 是 --> D{"环境变量、路径和配置是否完整？"}
    D -- 否 --> D1["复制 .env.example 并补齐必要配置"]
    D -- 是 --> E{"外部依赖是否可用？"}
    E -- 否 --> E1["检查 Qdrant、Embedding 服务、DeepSeek API"]
    E -- 是 --> F{"输出是否符合预期？"}
    F -- 否 --> F1["定位阶段：摄取文档 → 切分文本 → 生成向量 → 召回上下文 → 生成回答"]
    F -- 是 --> G["完成并归档：带检索上下文的回答"]
    N["中文排错口诀：入口 → 环境 → 配置 → 依赖 → 结果"] -.-> A
```

## 8. 关键组件记忆表

| 编号 | 组件 | 记忆重点 |
|---|---|---|
| 1 | 文档解析器 | 对应流程中的核心职责节点 |
| 2 | 切分与向量化 | 对应流程中的核心职责节点 |
| 3 | 向量检索 | 对应流程中的核心职责节点 |
| 4 | 智能问答流水线 | 对应流程中的核心职责节点 |

输入：`文档与用户问题`  
输出：`带检索上下文的回答`  
外部依赖：`Qdrant、Embedding 服务、DeepSeek API`
