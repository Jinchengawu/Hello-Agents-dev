# Agent 工具系统：中文设计图谱

本图谱对应 `L7/L7-5/Tool-System`，入口为 `test_my_calculator.py / test_advanced_search.py`。所有图均保留独立 Mermaid
源文件，节点、关系、状态和 UML Note 使用中文注释。

建议学习顺序：总流程 → UML 关系 → 调用时序 → 生命周期 → 系统边界 → 数据流 → 排错。

## 1. 总执行流程图

独立归档：[Mermaid 源文件](./diagrams/01-execution-flow.mmd) · [SVG 成品图](./diagrams/01-execution-flow.svg)。

```mermaid
%% 图 01：Agent 工具系统 总执行流程
%% 中文注释：实线为执行顺序，虚线为外部资源或记忆提示。
flowchart TD
    A["① 启动入口：test_my_calculator.py / test_advanced_search.py"] --> S1["② 注册工具"]
    S1 --> S2["3 解析参数"]
    S2 --> S3["4 执行本地或远程工具"]
    S3 --> S4["5 处理异常"]
    S4 --> S5["6 返回工具结果"]
    S5 --> O["输出：计算或搜索结果"]
    R["外部依赖：搜索服务 API"] -. "提供能力" .-> S2
    N["中文记忆注释：注册工具 → 解析参数 → 执行本地或远程工具 → 处理异常 → 返回工具结果"] -. "复习主线" .-> A
```
## 2. UML 组件/类关系图

独立归档：[Mermaid 源文件](./diagrams/02-uml-components.mmd) · [SVG 成品图](./diagrams/02-uml-components.svg)。

```mermaid
%% 图 02：Agent 工具系统 UML 组件/类关系图
%% 中文注释：该图表达学习层面的职责关系；概念组件不一定都是 Python 子类。
classDiagram
    class EntryModule {
        <<入口模块>>
        +load_config() 读取配置
        +run() 启动实践
    }
    class Core1 {
        <<核心组件 1>>
        +execute() 执行CalculatorTool职责
    }
    class Core2 {
        <<核心组件 2>>
        +execute() 执行AdvancedSearchTool职责
    }
    class Core3 {
        <<核心组件 3>>
        +execute() 执行工具参数校验职责
    }
    class Core4 {
        <<核心组件 4>>
        +execute() 执行Agent 工具调用职责
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
    note for EntryModule "中文注释：实际入口为 test_my_calculator.py / test_advanced_search.py"
    note for Core1 "中文职责：CalculatorTool"
    note for Core2 "中文职责：AdvancedSearchTool"
    note for Core3 "中文职责：工具参数校验"
    note for Core4 "中文职责：Agent 工具调用"
    note for ExternalResource "中文注释：搜索服务 API"
```
## 3. UML 时序图

独立归档：[Mermaid 源文件](./diagrams/03-sequence.mmd) · [SVG 成品图](./diagrams/03-sequence.svg)。

```mermaid
%% 图 03：Agent 工具系统 UML 时序图
%% 中文注释：纵向表示时间，箭头表示调用、数据或结果返回。
sequenceDiagram
    autonumber
    actor User as 学习者/调用方
    participant Entry as 入口脚本
    participant C1 as CalculatorTool
    participant C2 as AdvancedSearchTool
    participant C3 as 工具参数校验
    participant C4 as Agent 工具调用
    participant Ext as 外部资源
    User->>Entry: 提供工具名称与参数
    Note over User,Entry: 中文注释：从 test_my_calculator.py / test_advanced_search.py 启动
    Entry->>C1: 初始化并提交任务
    C1->>C2: 传递阶段结果
    C2->>C3: 传递阶段结果
    C3->>C4: 传递阶段结果
    C4->>Ext: 按需调用搜索服务 API
    Ext-->>C4: 返回外部结果
    C4-->>Entry: 返回计算或搜索结果
    Entry-->>User: 展示结果或错误
    Note over Entry,Ext: 中文注释：异常时应保留上下文并明确失败阶段
```
## 4. 生命周期状态图

独立归档：[Mermaid 源文件](./diagrams/04-lifecycle-state.mmd) · [SVG 成品图](./diagrams/04-lifecycle-state.svg)。

```mermaid
%% 图 04：Agent 工具系统 生命周期状态图
%% 中文注释：正常路径逐步推进，任一关键阶段失败都进入错误状态。
stateDiagram-v2
    [*] --> S1: 启动
    state "注册工具" as S1
    state "解析参数" as S2
    state "执行本地或远程工具" as S3
    state "处理异常" as S4
    state "返回工具结果" as S5
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
%% 图 05：Agent 工具系统 系统边界图
%% 中文注释：边界内是本地实践代码，边界外是网络、模型、数据库或运行设备。
flowchart LR
    I["输入：工具名称与参数"] --> C1
    subgraph Local["本地实践边界：L7/L7-5/Tool-System"]
        C1["CalculatorTool"]
        C2["AdvancedSearchTool"]
        C3["工具参数校验"]
        C4["Agent 工具调用"]
    end
    subgraph External["外部依赖边界"]
        R1["搜索服务 API"]
    end
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C1 -. "访问" .-> R1
    C4 --> O["输出：计算或搜索结果"]
    N["中文注释：外部资源异常不应被误判为本地业务逻辑错误"] -.-> External
```
## 6. 数据流图

独立归档：[Mermaid 源文件](./diagrams/06-data-flow.mmd) · [SVG 成品图](./diagrams/06-data-flow.svg)。

```mermaid
%% 图 06：Agent 工具系统 数据流图
%% 中文注释：展示输入如何经过核心组件逐步变成可验证输出。
flowchart TD
    I["原始输入：工具名称与参数"] --> C1["处理 1：CalculatorTool"]
    C1 --> C2["处理 2：AdvancedSearchTool"]
    C2 --> C3["处理 3：工具参数校验"]
    C3 --> C4["处理 4：Agent 工具调用"]
    C4 --> O["最终输出：计算或搜索结果"]
    R["资源数据：搜索服务 API"] -. "补充上下文或算力" .-> C4
    V{结果是否可验证？}
    O --> V
    V -- 是 --> D[归档结果]
    V -- 否 --> E[记录失败阶段并修正配置]
```
## 7. 排错决策图

独立归档：[Mermaid 源文件](./diagrams/07-troubleshooting.mmd) · [SVG 成品图](./diagrams/07-troubleshooting.svg)。

```mermaid
%% 图 07：Agent 工具系统 启动与排错决策图
%% 中文注释：按“入口→环境→配置→外部依赖→业务结果”顺序排查。
flowchart TD
    A["现象：Agent 工具系统 无法正常运行"] --> B{"入口是否正确？"}
    B -- 否 --> B1["使用 test_my_calculator.py / test_advanced_search.py"]
    B -- 是 --> C{"虚拟环境和 requirements 是否就绪？"}
    C -- 否 --> C1["激活 .venv 并安装 requirements.txt"]
    C -- 是 --> D{"环境变量、路径和配置是否完整？"}
    D -- 否 --> D1["复制 .env.example 并补齐必要配置"]
    D -- 是 --> E{"外部依赖是否可用？"}
    E -- 否 --> E1["检查 搜索服务 API"]
    E -- 是 --> F{"输出是否符合预期？"}
    F -- 否 --> F1["定位阶段：注册工具 → 解析参数 → 执行本地或远程工具 → 处理异常 → 返回工具结果"]
    F -- 是 --> G["完成并归档：计算或搜索结果"]
    N["中文排错口诀：入口 → 环境 → 配置 → 依赖 → 结果"] -.-> A
```

## 8. 关键组件记忆表

| 编号 | 组件 | 记忆重点 |
|---|---|---|
| 1 | CalculatorTool | 对应流程中的核心职责节点 |
| 2 | AdvancedSearchTool | 对应流程中的核心职责节点 |
| 3 | 工具参数校验 | 对应流程中的核心职责节点 |
| 4 | Agent 工具调用 | 对应流程中的核心职责节点 |

输入：`工具名称与参数`  
输出：`计算或搜索结果`  
外部依赖：`搜索服务 API`
