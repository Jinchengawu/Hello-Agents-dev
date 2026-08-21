# 第11章：Agentic-RL

从数据和奖励定义开始，经过监督微调与 GRPO 强化学习，训练并评估具备推理和工具使用能力的智能体模型。

> 本章只为需要本地演练的内容建立实践目录；理论说明和没有独立运行入口的
> 小节统一在本首页建立知识联系，不创建空目录。

## 本章主要教学目标

1. 理解 Agentic RL 与普通语言模型训练、传统强化学习之间的关系。
2. 将 GSM8K 等数据转换为 SFT 和 RL 所需格式，并设计可解释的奖励函数。
3. 使用 LoRA 和 SFT 建立稳定的行为起点。
4. 理解 GRPO 的采样、组内相对优势、奖励组合和策略更新过程。
5. 完成训练、评估、检查点管理和可选分布式执行的完整流水线。

## 各实践的共同基础

这些实践虽然交付物不同，但共享以下工程主线：

```text
数据与格式 → 奖励定义 → SFT 行为模仿 → GRPO 策略优化 → 评估与检查点
```

学习时应重点观察同一能力如何从基础抽象逐步组合成完整应用。

## 实践差异对比

| 实践 | 核心抽象 | 主要职责 | 控制方式 | 优势 | 局限 | 适用场景 |
|---|---|---|---|---|---|---|
| L11-1 Agentic RL 快速实验 | 最小数据、SFT 与 GRPO 检查 | 验证训练环境和概念 | 小样本快速路径 | 低成本发现环境问题 | 不能代表真实训练效果 | 首次运行和配置验证 |
| L11-2 训练数据与奖励函数 | Dataset 与 RewardFunction | 定义模型学习材料和目标 | 清洗、转换与打分 | 训练目标可检查 | 偏差会传递到全部训练阶段 | 数据准备和奖励设计 |
| L11-3 LoRA 与监督微调 | 基础模型、LoRA 与 SFT Trainer | 模仿高质量示范 | 监督学习 | 稳定、实现成熟 | 受示范数据上限约束 | 格式、指令和基础行为对齐 |
| L11-4 GRPO 强化学习训练 | 策略、候选组与奖励组合 | 按结果奖励优化策略 | 在线采样与相对优势 | 可提升推理策略 | 训练波动且资源消耗高 | 数学推理和可验证任务 |
| L11-5 训练模型评估 | 基线、生成、解析与指标 | 衡量训练是否真正改进 | 固定评估集对比 | 防止凭主观样例判断 | 受数据泄漏和指标覆盖影响 | 模型选择和回归检测 |
| L11-6 完整与分布式训练流水线 | 数据、SFT、GRPO、Accelerate | 串联生产级训练阶段 | 流水线与分布式执行 | 端到端可复现 | 硬件和故障恢复要求最高 | 正式实验和多 GPU 训练 |

## 关键权衡

### 1. 训练收益与资源成本

更完整的训练可能提升能力，但会显著增加显存、时间、数据质量和实验管理成本。

### 2. 奖励可计算与目标完整

可验证奖励易于规模化，却可能遗漏友好性、鲁棒性等难量化目标，并产生奖励投机。

## 建议学习顺序

1. [L11-1 Agentic RL 快速实验](./L11-1/Quick-Start/LEARNING_DIAGRAMS.md)
2. [L11-2 训练数据与奖励函数](./L11-2/Data-and-Rewards/LEARNING_DIAGRAMS.md)
3. [L11-3 LoRA 与监督微调](./L11-3/SFT/LEARNING_DIAGRAMS.md)
4. [L11-4 GRPO 强化学习训练](./L11-4/GRPO/LEARNING_DIAGRAMS.md)
5. [L11-5 训练模型评估](./L11-5/Evaluation/LEARNING_DIAGRAMS.md)
6. [L11-6 完整与分布式训练流水线](./L11-6/Training-Pipeline/LEARNING_DIAGRAMS.md)

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
| 只需检查环境和最小训练链路 | L11-1 Quick-Start |
| 当前重点是准备数据或设计奖励 | L11-2 Data-and-Rewards |
| 需要先用示范数据建立稳定行为 | L11-3 SFT |
| 需要用可计算奖励继续优化策略 | L11-4 GRPO |
| 需要比较基线与训练后模型 | L11-5 Evaluation |
| 需要端到端或分布式正式训练 | L11-6 Training-Pipeline |

来源：[Hello-Agents 第11章](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter11/%E7%AC%AC%E5%8D%81%E4%B8%80%E7%AB%A0%20Agentic-RL.md)
