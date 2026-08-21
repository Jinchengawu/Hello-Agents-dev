# AutoGen 软件开发团队：学习图谱

这份图谱对应 `main.py`、`autogen_software_team.py` 和 `output.py`。建议按下面顺序学习：

1. 总流程图：先建立全局执行路径
2. UML 类图：记住对象及依赖关系
3. 时序图：理解一次协作怎样发生
4. 状态图：掌握轮询和终止机制
5. 成品应用数据流图：区分团队协作与最终 Web 应用
6. 排错决策图：启动失败时快速定位问题

---

## 1. AutoGen 团队总流程图

对应 `main.py` 中的 `main()`、`run_software_development_team()` 和各个工厂函数。
独立归档：[Mermaid 源文件](./diagrams/01-team-execution-flow.mmd) · [SVG 成品图](./diagrams/01-team-execution-flow.svg)。

```mermaid
flowchart TD
    A["执行 python main.py"] --> B["load_dotenv 读取 .env"]
    B --> C["parse_args 解析 task / max-turns / auto-approve"]
    C --> D{"max_turns 是否大于 0？"}
    D -- "否" --> E["抛出配置错误并退出"]
    D -- "是" --> F["asyncio.run 启动异步事件循环"]

    F --> G["resolve_llm_api_key 解析密钥"]
    G --> H{"密钥是否有效？"}
    H -- "否" --> E
    H -- "是" --> I["创建 DeepSeek 模型客户端"]

    I --> J["创建 ProductManager"]
    I --> K["创建 Engineer"]
    I --> L["创建 CodeReviewer"]
    I --> M["创建 UserProxy"]

    J --> N["组装 RoundRobinGroupChat"]
    K --> N
    L --> N
    M --> N
    O["TextMentionTermination: TERMINATE"] --> N
    P["max_turns 安全上限"] --> N

    N --> Q["team_chat.run_stream(task)"]
    Q --> R["Console 实时输出团队消息"]
    R --> S{"出现 TERMINATE 或达到 max_turns？"}
    S -- "否" --> Q
    S -- "是" --> T["返回协作结果"]
    T --> U["finally: 关闭模型客户端"]
    U --> V["输出结果摘要"]
    X["中文记忆注释：配置 → 模型 → 角色 → 团队 → 轮询 → 关闭"] -. "复习主线" .-> F
```

### 记忆锚点

把主流程记成六个词：

> 配置 → 模型 → 角色 → 团队 → 轮询 → 关闭

其中 `finally: await model_client.close()` 是容易忽略但很重要的资源释放节点。

---

## 2. UML 类图：运行时对象关系

这张图强调的是运行时对象之间的依赖关系。`ProductManager`、`Engineer` 和
`CodeReviewer` 是三个 `AssistantAgent` 实例，并不是三个 Python 子类。
独立归档：[Mermaid 源文件](./diagrams/02-runtime-uml-class.mmd) · [SVG 成品图](./diagrams/02-runtime-uml-class.svg)。

```mermaid
classDiagram
    class MainModule {
        <<主程序模块 main.py>>
        +main() 主入口
        +parse_args() 解析命令行参数
        +resolve_llm_api_key() 解析密钥
        +validate_configuration() 校验配置
        +create_openai_model_client() 创建模型客户端
        +create_product_manager() 创建产品经理实例
        +create_engineer() 创建工程师实例
        +create_code_reviewer() 创建审查员实例
        +create_user_proxy() 创建用户代理实例
        +create_team() 组装轮询团队
        +run_software_development_team() 执行协作
    }

    class OpenAIChatCompletionClient {
        <<模型客户端：实际连接 DeepSeek>>
        +model 模型名称
        +base_url 服务地址
        +create() 发起模型请求
        +close() 释放网络资源
    }

    class AssistantAgent {
        <<模型型智能体：共 3 个实例>>
        +name 角色名称
        +system_message 角色规则
        +model_client 共享模型客户端
        +on_messages() 处理上下文并回复
    }

    class UserProxyAgent {
        <<人工输入代理：共 1 个实例>>
        +name 用户代理名称
        +description 验收职责
        +input_func 输入函数
        +on_messages() 接收人工反馈
    }

    class RoundRobinGroupChat {
        <<团队调度器>>
        +participants 四名参与者
        +termination_condition 终止规则
        +max_turns 最大轮数
        +run_stream() 按顺序产生消息流
    }

    class TextMentionTermination {
        <<业务终止条件>>
        +text 关键词 TERMINATE
        +check() 检查消息文本
    }

    class Console {
        <<终端流式界面>>
        +consume() 消费并显示消息流
    }

    MainModule ..> OpenAIChatCompletionClient : 创建
    MainModule ..> AssistantAgent : 创建三个实例
    MainModule ..> UserProxyAgent : 创建一个实例
    MainModule ..> RoundRobinGroupChat : 组装
    MainModule ..> Console : 调用显示

    AssistantAgent --> OpenAIChatCompletionClient : 共享并调用
    RoundRobinGroupChat "1 个团队" o-- "3 个模型型角色" AssistantAgent : 组合参与者
    RoundRobinGroupChat "1 个团队" o-- "1 个人工角色" UserProxyAgent : 组合参与者
    RoundRobinGroupChat --> TextMentionTermination : 每条消息后检查
    Console --> RoundRobinGroupChat : 消费消息流

    note for AssistantAgent "中文注释：ProductManager、Engineer、CodeReviewer\n只是不同配置的三个实例，并未定义三个子类。"
    note for UserProxyAgent "中文注释：交互模式读取用户输入；\n--auto-approve 模式自动返回 TERMINATE。"
    note for RoundRobinGroupChat "中文注释：列表顺序决定发言顺序；\n团队负责调度，模型不选择下一位角色。"
    note for OpenAIChatCompletionClient "中文注释：类名源于 OpenAI-compatible SDK；\n实际模型、地址和密钥均指向 DeepSeek。"
```

### 三个容易混淆的关系

| 关系 | 本例含义 |
|---|---|
| Agent → Model Client | 三个 `AssistantAgent` 共享同一个 DeepSeek 客户端 |
| Team → Agent | 团队保存四名参与者，并按列表顺序轮询 |
| Console → Team Stream | `Console` 只负责消费并显示消息流，不负责任务调度 |

---

## 3. UML 时序图：一次完整协作

时序图最适合回答：“运行后，谁先说话，谁调用模型，何时结束？”
独立归档：[Mermaid 源文件](./diagrams/03-collaboration-sequence.mmd) · [SVG 成品图](./diagrams/03-collaboration-sequence.svg)。

```mermaid
sequenceDiagram
    autonumber
    actor User as 用户/终端
    participant CLI as main.py
    participant Client as DeepSeek Model Client
    participant Team as RoundRobinGroupChat
    participant PM as ProductManager
    participant ENG as Engineer
    participant REV as CodeReviewer
    participant UP as UserProxy

    Note over User,CLI: 中文注释：启动阶段负责读取配置并提交开发任务
    User->>CLI: python main.py --task ...
    CLI->>CLI: 读取 .env、校验参数与 API Key
    CLI->>Client: 创建 OpenAI-compatible 客户端
    CLI->>Team: 创建四名参与者并提交 task

    Note over Team,UP: 中文注释：协作阶段严格按照参与者列表轮询
    loop 轮询，直到 TERMINATE 或 max_turns
        Team->>PM: 转交当前对话上下文
        PM->>Client: 请求需求分析与项目规划
        Client-->>PM: DeepSeek 响应
        PM-->>Team: 分析结果 + 请工程师开始实现

        Team->>ENG: 转交完整上下文
        ENG->>Client: 请求技术实现
        Client-->>ENG: DeepSeek 响应
        ENG-->>Team: 实现代码 + 请代码审查员检查

        Team->>REV: 转交完整上下文
        REV->>Client: 请求代码审查
        Client-->>REV: DeepSeek 响应
        REV-->>Team: 审查意见 + 请用户代理测试

        Team->>UP: 请求用户验收
        alt 使用 --auto-approve
            UP-->>Team: TERMINATE
        else 交互模式
            Team-->>User: 显示输入提示
            User->>UP: 反馈或 TERMINATE
            UP-->>Team: 用户输入
        end
    end

    Note over CLI,Client: 中文注释：finally 保证模型客户端最终被关闭
    Team-->>CLI: 返回 TaskResult
    CLI->>Client: close()
    CLI-->>User: 输出协作结果摘要
```

### 关键理解

- `RoundRobinGroupChat` 决定发言顺序，不依赖模型自行选择下一位 Agent。
- 三名助手都会调用同一个 DeepSeek 客户端；`UserProxy` 负责接收人工输入，本身不调用模型。
- 提示词中的“请工程师开始实现”等语句是语义交接提示；真正的轮换由
  `RoundRobinGroupChat` 控制。

---

## 4. 状态图：轮询与终止条件

这张图适合记忆 `TERMINATE` 和 `max_turns` 分别负责什么。
独立归档：[Mermaid 源文件](./diagrams/04-round-robin-state.mmd) · [SVG 成品图](./diagrams/04-round-robin-state.svg)。

```mermaid
stateDiagram-v2
    [*] --> Initializing: 启动程序
    Initializing --> ProductManagerTurn: 配置与团队创建成功
    Initializing --> ConfigurationError: 参数或密钥无效
    ConfigurationError --> [*]

    ProductManagerTurn --> EngineerTurn: 下一轮参与者
    EngineerTurn --> CodeReviewerTurn: 下一轮参与者
    CodeReviewerTurn --> UserProxyTurn: 下一轮参与者

    UserProxyTurn --> Terminated: 消息包含 TERMINATE
    UserProxyTurn --> ProductManagerTurn: 用户提出修改意见

    ProductManagerTurn --> TurnLimitReached: 达到 max_turns
    EngineerTurn --> TurnLimitReached: 达到 max_turns
    CodeReviewerTurn --> TurnLimitReached: 达到 max_turns
    UserProxyTurn --> TurnLimitReached: 达到 max_turns

    Terminated --> ClosingClient
    TurnLimitReached --> ClosingClient
    ClosingClient --> Completed
    Completed --> [*]

    note right of Terminated
      中文注释：业务层正常结束，表示用户确认验收完成
    end note
    note right of TurnLimitReached
      中文注释：系统层安全结束，防止 Agent 无限循环
    end note
```

### 双保险记忆法

- `TERMINATE`：业务层主动结束，表示验收完成。
- `max_turns`：系统层兜底结束，防止团队无限对话。

---

## 5. 两条程序链路的边界

AutoGen 团队和 Streamlit 应用是两条可分别运行的链路：
独立归档：[Mermaid 源文件](./diagrams/05-two-runtime-boundaries.mmd) · [SVG 成品图](./diagrams/05-two-runtime-boundaries.svg)。

```mermaid
flowchart LR
    subgraph A["链路 A：多智能体协作"]
        A1["main.py"] --> A2["AutoGen 四智能体团队"]
        A2 --> A3["DeepSeek API"]
        A2 --> A4["终端中的方案、代码和审查结果"]
    end

    subgraph B["链路 B：交付应用运行"]
        B1["浏览器"] --> B2["Streamlit / output.py"]
        B2 --> B3["CoinGecko API"]
        B3 --> B2
        B2 --> B4["价格与 24 小时涨跌幅"]
    end

    A4 -. "教程中形成的交付物" .-> B2
    N1["中文注释：main.py 需要 DeepSeek Key"] -.-> A1
    N2["中文注释：output.py 不需要 DeepSeek Key"] -.-> B2
```

重要区别：运行 `output.py` 不需要 DeepSeek Key；它需要访问 CoinGecko。运行
`main.py` 需要 DeepSeek Key，但不会自动启动 Streamlit。

---

## 6. Streamlit 成品应用数据流图

对应 `output.py` 中的 `render_app()` 和 `get_bitcoin_price()`。
独立归档：[Mermaid 源文件](./diagrams/06-streamlit-data-flow.mmd) · [SVG 成品图](./diagrams/06-streamlit-data-flow.svg)。

```mermaid
flowchart TD
    A["python -m streamlit run output.py"] --> B["render_app 设置页面"]
    B --> C{"用户点击刷新？"}
    C -- "是" --> D["st.rerun 重新执行脚本"]
    C -- "否" --> E["显示加载状态"]
    D --> E
    E --> F["get_bitcoin_price"]
    F --> G["GET CoinGecko /simple/price"]
    G --> H{"HTTP、JSON 和字段解析是否成功？"}
    H -- "是" --> I["返回价格与 24h 涨跌幅"]
    I --> J["st.metric 渲染指标"]
    H -- "否" --> K["捕获异常并 st.error"]
    K --> L["返回 None, None"]
    L --> M["st.warning 提示稍后重试"]
    X["中文注释：timeout=10，避免请求无限等待"] -.-> G
    Y["中文注释：raise_for_status 检查非 2xx 响应"] -.-> H
```

### 关键节点

- 网络请求设置了 `timeout=10`，避免页面无限等待。
- `raise_for_status()` 将非 2xx HTTP 状态转换为异常。
- 多类异常集中处理，UI 层通过 `None` 判断是否显示降级提示。

---

## 7. 启动与排错决策图

独立归档：[Mermaid 源文件](./diagrams/07-troubleshooting-decision.mmd) · [SVG 成品图](./diagrams/07-troubleshooting-decision.svg)。

```mermaid
flowchart TD
    A["项目无法正常运行"] --> B{"运行的是哪个入口？"}

    B -- "main.py" --> C{"是否激活 .venv 并安装 requirements？"}
    C -- "否" --> C1["创建/激活虚拟环境并安装依赖"]
    C -- "是" --> D{".env 中是否为真实 DeepSeek Key？"}
    D -- "否" --> D1["复制 .env.example 并填写 LLM_API_KEY"]
    D -- "是" --> E{"错误类型是什么？"}
    E -- "401 / AuthenticationError" --> E1["检查 Key、模型名和 base URL"]
    E -- "连接超时" --> E2["检查网络、代理和 DeepSeek 服务状态"]
    E -- "对话不停止" --> E3["输入 TERMINATE 或降低 --max-turns"]

    B -- "output.py" --> F{"Streamlit 是否安装？"}
    F -- "否" --> C1
    F -- "是" --> G{"页面能否打开？"}
    G -- "否" --> G1["使用 python -m streamlit run output.py"]
    G -- "是但无价格" --> H["检查 CoinGecko 网络访问和错误提示"]
    N["中文排错口诀：入口 → 环境 → 配置 → 网络 → 终止条件"] -.-> A
```

---

## 8. 一页式记忆卡

| 要记住的问题 | 答案 |
|---|---|
| 谁负责调度？ | `RoundRobinGroupChat` |
| 谁调用 DeepSeek？ | 三个 `AssistantAgent` 共享的 `OpenAIChatCompletionClient` |
| 谁承接人工输入？ | `UserProxyAgent` |
| 谁显示流式消息？ | `Console` |
| 如何正常结束？ | 任意消息包含 `TERMINATE` |
| 如何防止无限循环？ | `max_turns` |
| 为什么一定要 `close()`？ | 释放模型客户端持有的网络连接资源 |
| `output.py` 是否依赖 DeepSeek？ | 不依赖，只访问 CoinGecko |

复习时，可以只画下面这条最小链路：

```text
Task → PM → Engineer → Reviewer → UserProxy → TERMINATE
          三个 AssistantAgent 共享 DeepSeek Client
```
