# 第10章：智能体通信协议

用标准协议连接 Agent、工具、服务和其他 Agent，理解 MCP、A2A 与 ANP 分别解决能力调用、点对点协作和大规模网络发现问题。

> 本章只为需要本地演练的内容建立实践目录；理论说明和没有独立运行入口的
> 小节统一在本首页建立知识联系，不创建空目录。

## 本章主要教学目标

1. 理解协议如何降低 Agent 与外部系统之间的定制适配成本。
2. 掌握 MCP 的工具发现、资源访问、调用和传输生命周期。
3. 掌握 A2A 的 Agent Card、任务、消息、工件和状态转换。
4. 理解 ANP 的服务注册、发现、路由和负载均衡定位。
5. 能够组合三种协议并实现一个可调用的自定义 MCP Server。

## 各实践的共同基础

这些实践虽然交付物不同，但共享以下工程主线：

```text
能力描述 → 发现与协商 → 消息与任务 → 传输和生命周期 → 身份、安全与错误处理
```

学习时应重点观察同一能力如何从基础抽象逐步组合成完整应用。

## 实践差异对比

| 实践 | 核心抽象 | 主要职责 | 控制方式 | 优势 | 局限 | 适用场景 |
|---|---|---|---|---|---|---|
| L10-1 协议工具快速连接 | MCPTool、A2ATool、ANPTool | 快速感知三类协议入口 | 统一 Tool 接口 | 低成本建立全局认识 | 不覆盖完整协议生命周期 | 首次学习和环境连通性检查 |
| L10-2 MCP 连接与多 Agent 协作 | Server、Client、Transport 与 Tool | Agent 与外部能力标准通信 | 客户端—服务器 | 生态成熟、工具边界清晰 | 服务进程和权限管理复杂 | 文件、数据库、GitHub 等工具接入 |
| L10-3 A2A 智能体通信 | Agent Card、Task 与 Artifact | Agent 间委托、协商和协作 | 点对点任务生命周期 | 适合专业 Agent 团队 | 发现和信任需额外基础设施 | 研究、客服和跨 Agent 委托 |
| L10-4 ANP 服务发现与任务分发 | Registry、Router 与 Load Balancer | 构建大规模 Agent 网络 | 注册发现与动态路由 | 面向开放网络扩展 | 生态和标准成熟度较低 | 大量 Agent 的发现和负载分配 |
| L10-5 自定义天气 MCP Server | FastMCP 服务与天气工具 | 实现并验证具体协议服务 | 服务端工具发布 | 形成端到端开发闭环 | 需要处理外部 API 和服务运行 | 把业务 API 发布为 Agent 工具 |

## 关键权衡

### 1. 统一标准与实现成熟度

协议统一了边界，但 MCP、A2A、ANP 的生态成熟度和适用范围不同，不能只凭名称互换。

### 2. 去中心化与治理成本

点对点或开放网络提高扩展性，同时增加身份、信任、路由、版本兼容和故障定位难度。

## 建议学习顺序

1. [L10-1 协议工具快速连接](./L10-1/Quick-Start/LEARNING_DIAGRAMS.md)
2. [L10-2 MCP 连接与多 Agent 协作](./L10-2/MCP/LEARNING_DIAGRAMS.md)
3. [L10-3 A2A 智能体通信](./L10-3/A2A/LEARNING_DIAGRAMS.md)
4. [L10-4 ANP 服务发现与任务分发](./L10-4/ANP/LEARNING_DIAGRAMS.md)
5. [L10-5 自定义天气 MCP Server](./L10-5/Custom-MCP-Server/LEARNING_DIAGRAMS.md)

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
| 只是想先比较三种协议的使用入口 | L10-1 Quick-Start |
| 要让 Agent 标准化访问工具或数据 | L10-2 MCP |
| 要让两个或少量 Agent 直接协作 | L10-3 A2A |
| 要做大规模发现、路由和负载均衡 | L10-4 ANP |
| 要亲手发布一个具体业务工具服务 | L10-5 Custom-MCP-Server |

来源：[Hello-Agents 第10章](https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter10/%E7%AC%AC%E5%8D%81%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE.md)
