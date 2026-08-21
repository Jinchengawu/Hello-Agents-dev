# 第9章：上下文工程

把上下文视为有限的注意力预算，通过压缩、结构化笔记、即时工具访问和分层协作，为长时程 Agent 持续提供最相关的信息。

> 本章只为需要本地演练的内容建立实践目录；理论说明和没有独立运行入口的
> 小节统一在本首页建立知识联系，不创建空目录。

## 本章主要教学目标

1. 理解上下文腐蚀以及长窗口并不等于有效上下文。
2. 掌握 GSSC 流水线对目标、状态、步骤和上下文的组织方式。
3. 使用 NoteTool 建立跨会话、可检索的结构化长期笔记。
4. 使用 TerminalTool 按需获取文件和命令输出，避免一次性填满上下文。
5. 将多层上下文能力整合成长时程代码库维护工作流。

## 各实践的共同基础

这些实践虽然交付物不同，但共享以下工程主线：

```text
目标与状态 → 相关性和新近性 → 压缩与筛选 → 结构化持久笔记 → 即时工具访问
```

学习时应重点观察同一能力如何从基础抽象逐步组合成完整应用。

## 实践差异对比

| 实践 | 核心抽象 | 主要职责 | 控制方式 | 优势 | 局限 | 适用场景 |
|---|---|---|---|---|---|---|
| L9-3 GSSC ContextBuilder | Goal、State、Step、Context | 构造当前任务所需上下文 | 评分、压缩与组装 | 统一上下文入口 | 质量取决于筛选策略 | 复杂任务的动态上下文准备 |
| L9-4 结构化笔记工具 | Markdown、YAML 与检索 | 保存跨会话知识 | 显式增删改查 | 持久且便于人工审阅 | 需要维护结构和过期信息 | 项目决策、进度和知识沉淀 |
| L9-5 终端与文件系统工具 | 命令、文件和安全规则 | 即时获取本地真实状态 | 白名单与受控执行 | 避免大量内容预加载 | 命令安全和输出截断复杂 | 代码库、日志和数据文件调查 |
| L9-6 三日代码库维护工作流 | ContextBuilder、笔记和终端组合 | 执行跨会话长时程任务 | 阶段计划与人工验收 | 展示完整上下文工程 | 状态恢复和副作用风险更高 | 持续代码维护和复杂项目协作 |

## 关键权衡

### 1. 预加载与即时访问

预加载降低调用次数但容易产生噪声；JIT 访问节省窗口，却需要可靠的工具选择和权限控制。

### 2. 自动化与人类可控

自动维护能提高长任务效率，但关键写操作、上下文压缩和阶段验收需要保留可审计边界。

## 建议学习顺序

1. [L9-3 GSSC ContextBuilder](./L9-3/ContextBuilder/LEARNING_DIAGRAMS.md)
2. [L9-4 结构化笔记工具](./L9-4/NoteTool/LEARNING_DIAGRAMS.md)
3. [L9-5 终端与文件系统工具](./L9-5/TerminalTool/LEARNING_DIAGRAMS.md)
4. [L9-6 三日代码库维护工作流](./L9-6/Codebase-Maintainer/LEARNING_DIAGRAMS.md)

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
| 需要动态组装有限上下文预算 | L9-3 ContextBuilder |
| 需要跨会话保存结构化事实和决策 | L9-4 NoteTool |
| 需要按需读取文件或命令结果 | L9-5 TerminalTool |
| 需要组合能力完成多日长任务 | L9-6 Codebase-Maintainer |

来源：[Hello-Agents 第9章](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter9/%E7%AC%AC%E4%B9%9D%E7%AB%A0%20%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B.md)
