# 第7章：构建你的智能体框架

从使用现成框架进一步走向理解并实现框架内核，以分层解耦、职责单一和统一接口组织模型、Agent 范式与工具系统。

> 本章只为需要本地演练的内容建立实践目录；理论说明和没有独立运行入口的
> 小节统一在本首页建立知识联系，不创建空目录。

## 本章主要教学目标

1. 理解自建框架的价值，以及核心层、Agent 层和工具层之间的依赖方向。
2. 用统一模型接口隔离不同 LLM Provider 的认证、地址和调用差异。
3. 比较 Simple、ReAct、Reflection、Plan-and-Solve 与 Function Calling 的控制循环。
4. 设计可注册、可校验、可组合并能安全执行的工具系统。
5. 能够从最小能力逐层扩展框架，而不把业务逻辑耦合到模型 SDK。

## 各实践的共同基础

这些实践虽然交付物不同，但共享以下工程主线：

```text
统一配置与消息 → LLM 适配层 → Agent 推理循环 → 工具注册与调用 → 异常与可观测性
```

学习时应重点观察同一能力如何从基础抽象逐步组合成完整应用。

## 实践差异对比

| 实践 | 核心抽象 | 主要职责 | 控制方式 | 优势 | 局限 | 适用场景 |
|---|---|---|---|---|---|---|
| L7-2 自定义 LLM Provider 扩展 | Provider 与统一模型接口 | 适配外部模型服务 | 配置驱动 | 隔离 SDK 差异 | 需要维护能力兼容性 | 接入 DeepSeek 或其他 OpenAI-compatible 服务 |
| L7-4 Agent 经典模式 | 多种推理循环 | 比较任务分解、行动和反思 | 循环与终止条件 | 理解范式差异 | 不同模式成本差异明显 | 为任务选择合适的 Agent 控制模式 |
| L7-5 Agent 工具系统 | BaseTool、Registry 与执行器 | 扩展 Agent 外部能力 | 参数校验与受控执行 | 能力复用和组合 | 工具边界与安全需额外设计 | 构建计算、搜索和业务工具 |

## 关键权衡

### 1. 抽象统一与能力差异

统一接口降低上层复杂度，但仍需保留不同模型在流式响应、函数调用和结构化输出方面的能力边界。

### 2. 自主推理与显式约束

Agent 循环越自主，适应性越强；步骤越显式，成本、终止和错误恢复越容易控制。

## 建议学习顺序

1. [L7-2 自定义 LLM Provider 扩展](./L7-2/LLM-Extension/LEARNING_DIAGRAMS.md)
2. [L7-4 Agent 经典模式](./L7-4/Agent-Patterns/LEARNING_DIAGRAMS.md)
3. [L7-5 Agent 工具系统](./L7-5/Tool-System/LEARNING_DIAGRAMS.md)

每个实践目录都包含 `requirements.txt`、`.env.example`、`LEARNING_DIAGRAMS.md`，
以及保存 7 类中文 Mermaid/SVG 的 `diagrams/` 目录。

## 章节级对比图

| 图表 | Mermaid 源文件 | SVG 成品图 |
|---|---|---|
| 本章知识关联图 | [源文件](./diagrams/01-knowledge-map.mmd) | [SVG](./diagrams/01-knowledge-map.svg) |
| 实践范式与控制方式对比图 | [源文件](./diagrams/02-paradigm-comparison.mmd) | [SVG](./diagrams/02-paradigm-comparison.svg) |
| 按学习目标选择实践的决策图 | [源文件](./diagrams/03-practice-selection.mmd) | [SVG](./diagrams/03-practice-selection.svg) |

## 快速选择

| 如果当前首先需要…… | 优先实践 |
|---|---|
| 首要任务是接入或扩展模型 Provider | L7-2 LLM-Extension |
| 首要任务是比较 Agent 推理范式 | L7-4 Agent-Patterns |
| 首要任务是构建可复用工具能力 | L7-5 Tool-System |

来源：[Hello-Agents 第7章](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md)
