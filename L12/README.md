# 第12章：智能体性能评估

建立从评估对象、基准任务、预测解析到指标和报告的闭环，用可重复证据判断 Agent 的工具调用、综合任务和生成质量。

> 本章只为需要本地演练的内容建立实践目录；理论说明和没有独立运行入口的
> 小节统一在本首页建立知识联系，不创建空目录。

## 本章主要教学目标

1. 理解 Agent 输出不确定性、指标多样性和评估成本带来的挑战。
2. 使用 BFCL 评估函数选择、参数生成和复杂函数调用能力。
3. 使用 GAIA 评估多步推理、搜索、文件处理和真实世界任务能力。
4. 结合规则指标、LLM Judge、Win Rate 与人工验证评估开放式输出。
5. 把评估结果用于回归检测、模型选择和后续数据生成。

## 各实践的共同基础

这些实践虽然交付物不同，但共享以下工程主线：

```text
评估对象与版本 → 数据集与任务切片 → 预测记录与解析 → 指标与裁判 → 报告、误差分析与回归
```

学习时应重点观察同一能力如何从基础抽象逐步组合成完整应用。

## 实践差异对比

| 实践 | 核心抽象 | 主要职责 | 控制方式 | 优势 | 局限 | 适用场景 |
|---|---|---|---|---|---|---|
| L12-1 基础 Agent 评估对象 | LLM、Agent 与搜索工具 | 建立可重复的被测系统 | 固定配置和输出 | 明确评估边界 | 示例能力范围有限 | 学习评估前的基线准备 |
| L12-2 BFCL 函数调用评估 | 函数题集、预测与 AST 匹配 | 测量工具调用正确性 | 结构化自动评分 | 客观且适合回归 | 不覆盖开放式综合任务 | API 选择和参数生成评估 |
| L12-3 GAIA 通用 Agent 评估 | 多步骤真实任务与准精确匹配 | 测量综合助手能力 | 端到端任务评分 | 贴近真实复杂问题 | 执行成本高且工具环境敏感 | 搜索、推理、文件和多模态任务 |
| L12-4 数据生成与多方式评估 | AIME、LLM Judge、Win Rate 与人工验证 | 构建自定义开放式评估 | 多裁判和对比统计 | 覆盖业务特定质量 | 裁判偏差和数据治理复杂 | 生成质量、多模型对比和数据闭环 |

## 关键权衡

### 1. 客观自动化与语义覆盖

AST 或精确匹配可复现但覆盖有限；LLM Judge 更接近语义质量，却引入偏差、成本和不可重复性。

### 2. 基准分数与真实价值

公开基准便于横向比较，但可能发生数据污染，也不能替代面向实际业务失败模式的自定义评估。

## 建议学习顺序

1. [L12-1 基础 Agent 评估对象](./L12-1/Basic-Agent/LEARNING_DIAGRAMS.md)
2. [L12-2 BFCL 函数调用评估](./L12-2/BFCL/LEARNING_DIAGRAMS.md)
3. [L12-3 GAIA 通用 Agent 评估](./L12-3/GAIA/LEARNING_DIAGRAMS.md)
4. [L12-4 数据生成与多方式评估](./L12-4/Data-Generation-Evaluation/LEARNING_DIAGRAMS.md)

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
| 需要先固定一个可重复的被测 Agent | L12-1 Basic-Agent |
| 主要评估函数或工具调用正确性 | L12-2 BFCL |
| 主要评估真实世界综合任务能力 | L12-3 GAIA |
| 需要自定义数据、LLM Judge 或胜率评估 | L12-4 Data-Generation-Evaluation |

来源：[Hello-Agents 第12章](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md)
