# 自定义天气 MCP Server：中文设计图谱

本图谱对应 `L10/L10-5/Custom-MCP-Server`，入口为 `14_weather_mcp_server.py / 14_weather_agent.py`。所有图均保留独立 Mermaid
源文件，节点、关系、状态和 UML Note 使用中文注释。

建议学习顺序：总流程 → UML 关系 → 调用时序 → 生命周期 → 系统边界 → 数据流 → 排错。

## 1. 总执行流程图

独立归档：[Mermaid 源文件](./diagrams/01-execution-flow.mmd) · [SVG 成品图](./diagrams/01-execution-flow.svg)。

```mermaid
%% 图 01：自定义天气 MCP Server 总执行流程
%% 中文注释：实线为执行顺序，虚线为外部资源或记忆提示。
flowchart TD
    A["① 启动入口：14_weather_mcp_server.py / 14_weather_agent.py"] --> S1["② 启动服务器"]
    S1 --> S2["3 注册天气工具"]
    S2 --> S3["4 Agent 建立连接"]
    S3 --> S4["5 调用天气查询"]
    S4 --> S5["6 返回天气结果"]
    S5 --> O["输出：天气数据和 Agent 回答"]
    R["外部依赖：天气 API、本地 MCP 端口、DeepSeek API"] -. "提供能力" .-> S2
    N["中文记忆注释：启动服务器 → 注册天气工具 → Agent 建立连接 → 调用天气查询 → 返回天气结果"] -. "复习主线" .-> A
```
## 2. UML 组件/类关系图

独立归档：[Mermaid 源文件](./diagrams/02-uml-components.mmd) · [SVG 成品图](./diagrams/02-uml-components.svg)。

```mermaid
%% 图 02：自定义天气 MCP Server UML 组件/类关系图
%% 中文注释：该图表达学习层面的职责关系；概念组件不一定都是 Python 子类。
classDiagram
    class EntryModule {
        <<入口模块>>
        +load_config() 读取配置
        +run() 启动实践
    }
    class Core1 {
        <<核心组件 1>>
        +execute() 执行天气 MCP Server职责
    }
    class Core2 {
        <<核心组件 2>>
        +execute() 执行天气工具职责
    }
    class Core3 {
        <<核心组件 3>>
        +execute() 执行MCP 客户端 Agent职责
    }
    class Core4 {
        <<核心组件 4>>
        +execute() 执行集成测试职责
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
    note for EntryModule "中文注释：实际入口为 14_weather_mcp_server.py / 14_weather_agent.py"
    note for Core1 "中文职责：天气 MCP Server"
    note for Core2 "中文职责：天气工具"
    note for Core3 "中文职责：MCP 客户端 Agent"
    note for Core4 "中文职责：集成测试"
    note for ExternalResource "中文注释：天气 API、本地 MCP 端口、DeepSeek API"
```
## 3. UML 时序图

独立归档：[Mermaid 源文件](./diagrams/03-sequence.mmd) · [SVG 成品图](./diagrams/03-sequence.svg)。

```mermaid
%% 图 03：自定义天气 MCP Server UML 时序图
%% 中文注释：纵向表示时间，箭头表示调用、数据或结果返回。
sequenceDiagram
    autonumber
    actor User as 学习者/调用方
    participant Entry as 入口脚本
    participant C1 as 天气 MCP Server
    participant C2 as 天气工具
    participant C3 as MCP 客户端 Agent
    participant C4 as 集成测试
    participant Ext as 外部资源
    User->>Entry: 提供城市与天气请求
    Note over User,Entry: 中文注释：从 14_weather_mcp_server.py / 14_weather_agent.py 启动
    Entry->>C1: 初始化并提交任务
    C1->>C2: 传递阶段结果
    C2->>C3: 传递阶段结果
    C3->>C4: 传递阶段结果
    C4->>Ext: 按需调用天气 API、本地 MCP 端口、DeepSeek API
    Ext-->>C4: 返回外部结果
    C4-->>Entry: 返回天气数据和 Agent 回答
    Entry-->>User: 展示结果或错误
    Note over Entry,Ext: 中文注释：异常时应保留上下文并明确失败阶段
```
## 4. 生命周期状态图

独立归档：[Mermaid 源文件](./diagrams/04-lifecycle-state.mmd) · [SVG 成品图](./diagrams/04-lifecycle-state.svg)。

```mermaid
%% 图 04：自定义天气 MCP Server 生命周期状态图
%% 中文注释：正常路径逐步推进，任一关键阶段失败都进入错误状态。
stateDiagram-v2
    [*] --> S1: 启动
    state "启动服务器" as S1
    state "注册天气工具" as S2
    state "Agent 建立连接" as S3
    state "调用天气查询" as S4
    state "返回天气结果" as S5
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
%% 图 05：自定义天气 MCP Server 系统边界图
%% 中文注释：边界内是本地实践代码，边界外是网络、模型、数据库或运行设备。
flowchart LR
    I["输入：城市与天气请求"] --> C1
    subgraph Local["本地实践边界：L10/L10-5/Custom-MCP-Server"]
        C1["天气 MCP Server"]
        C2["天气工具"]
        C3["MCP 客户端 Agent"]
        C4["集成测试"]
    end
    subgraph External["外部依赖边界"]
        R1["天气 API"]
        R2["本地 MCP 端口"]
        R3["DeepSeek API"]
    end
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C1 -. "访问" .-> R1
    C2 -. "访问" .-> R2
    C3 -. "访问" .-> R3
    C4 --> O["输出：天气数据和 Agent 回答"]
    N["中文注释：外部资源异常不应被误判为本地业务逻辑错误"] -.-> External
```
## 6. 数据流图

独立归档：[Mermaid 源文件](./diagrams/06-data-flow.mmd) · [SVG 成品图](./diagrams/06-data-flow.svg)。

```mermaid
%% 图 06：自定义天气 MCP Server 数据流图
%% 中文注释：展示输入如何经过核心组件逐步变成可验证输出。
flowchart TD
    I["原始输入：城市与天气请求"] --> C1["处理 1：天气 MCP Server"]
    C1 --> C2["处理 2：天气工具"]
    C2 --> C3["处理 3：MCP 客户端 Agent"]
    C3 --> C4["处理 4：集成测试"]
    C4 --> O["最终输出：天气数据和 Agent 回答"]
    R["资源数据：天气 API、本地 MCP 端口、DeepSeek API"] -. "补充上下文或算力" .-> C4
    V{结果是否可验证？}
    O --> V
    V -- 是 --> D[归档结果]
    V -- 否 --> E[记录失败阶段并修正配置]
```
## 7. 排错决策图

独立归档：[Mermaid 源文件](./diagrams/07-troubleshooting.mmd) · [SVG 成品图](./diagrams/07-troubleshooting.svg)。

```mermaid
%% 图 07：自定义天气 MCP Server 启动与排错决策图
%% 中文注释：按“入口→环境→配置→外部依赖→业务结果”顺序排查。
flowchart TD
    A["现象：自定义天气 MCP Server 无法正常运行"] --> B{"入口是否正确？"}
    B -- 否 --> B1["使用 14_weather_mcp_server.py / 14_weather_agent.py"]
    B -- 是 --> C{"虚拟环境和 requirements 是否就绪？"}
    C -- 否 --> C1["激活 .venv 并安装 requirements.txt"]
    C -- 是 --> D{"环境变量、路径和配置是否完整？"}
    D -- 否 --> D1["复制 .env.example 并补齐必要配置"]
    D -- 是 --> E{"外部依赖是否可用？"}
    E -- 否 --> E1["检查 天气 API、本地 MCP 端口、DeepSeek API"]
    E -- 是 --> F{"输出是否符合预期？"}
    F -- 否 --> F1["定位阶段：启动服务器 → 注册天气工具 → Agent 建立连接 → 调用天气查询 → 返回天气结果"]
    F -- 是 --> G["完成并归档：天气数据和 Agent 回答"]
    N["中文排错口诀：入口 → 环境 → 配置 → 依赖 → 结果"] -.-> A
```

## 8. 关键组件记忆表

| 编号 | 组件 | 记忆重点 |
|---|---|---|
| 1 | 天气 MCP Server | 对应流程中的核心职责节点 |
| 2 | 天气工具 | 对应流程中的核心职责节点 |
| 3 | MCP 客户端 Agent | 对应流程中的核心职责节点 |
| 4 | 集成测试 | 对应流程中的核心职责节点 |

输入：`城市与天气请求`  
输出：`天气数据和 Agent 回答`  
外部依赖：`天气 API、本地 MCP 端口、DeepSeek API`
