# 验证记录

验证日期：2026-08-20（Asia/Shanghai）

## 已完成

- 29 个“章节-小节/实践名”目录均包含 `requirements.txt` 与 `.env.example`
- 所有归档 Python 源文件通过 Python 3.12 编译
- 29 份依赖清单均通过 `pip --dry-run --no-deps` 的发行包/版本可用性检查
- `L6/L6-2/AutoGen` 已重建隔离环境，离线测试通过，`pip check` 无冲突
- 第六章已聚合至 `L6/`，4 个实践目录完成纯净迁移，未保留旧路径软链接
- 第 7–12 章已分别聚合至 `L7/`–`L12/`，25 个实践完成纯净迁移，未保留旧路径软链接
- L6 的 AutoGen、AgentScope、CAMEL 均使用 Python 3.12 从新路径重建 `.venv`，三套环境的 `pip check` 均无冲突
- `L7/L7-4/Agent-Patterns` 已安装 `hello-agents==0.2.8` 并完成模块导入烟测
- `L7/L7-5/Tool-System` 计算器离线用例通过
- `L9/L9-4/NoteTool` 本地增删改查/搜索/摘要流程通过
- `L9/L9-5/TerminalTool` 本地导航、CSV、日志、代码库与安全限制演示已执行
- 29 份环境模板的在线 LLM 配置均已统一为 `deepseek-v4-flash` 与
  `https://api.deepseek.com`
- AutoGen DeepSeek 客户端完成离线构造，7 项测试通过，`pip check` 无冲突
- AgentScope 的 `OpenAIChatModel` + `DeepSeekMultiAgentFormatter` 完成离线构造
- CAMEL 的 `OPENAI_COMPATIBLE_MODEL` DeepSeek 客户端完成离线构造
- 29 个实践均包含独立中文设计图归档；总计 203 张 Mermaid 图源和 203 张 SVG 成品图
- L6 章节首页另包含 3 张中文对比图；连同实践图，全仓共 206 张 Mermaid 图源和 206 张 SVG 成品图
- L6 的 31 张 Mermaid 图源均使用 Mermaid CLI 与本机 Chrome 真实渲染通过
- L7–L12 新增 18 张章节级中文对比图，全部受路径影响的实践图与章节图均使用 Mermaid CLI 和本机 Chrome 真实渲染通过
- 第 6–12 章现共 21 张章节图；连同 203 张实践图，全仓共有 224 张 Mermaid 图源和 224 张 SVG 成品图
- `L7/L7-4/Agent-Patterns` 已使用 Python 3.12 从新路径重建 `.venv`，模块导入烟测和 `pip check` 均通过
- 每个实践包含总流程、UML 关系、UML 时序、生命周期、系统边界、数据流和排错图

## 有意未执行

- 真实 DeepSeek LLM、Tavily、GitHub、天气等外部 API 调用
- Qdrant、Neo4j、远程 MCP、A2A、ANP 网络服务
- BFCL、GAIA、GSM8K、AIME 等数据集完整下载或官方评估
- SFT、GRPO、分布式训练及模型权重下载

这些项目已归档代码、配置和依赖，但执行会产生额度费用、下载大量数据/模型、占用 GPU，或启动本地监听端口，需要使用者明确配置后逐项运行。

## 上游修复

- 将第 9.6 节四处作者机器绝对路径替换为当前实践目录下的 `codebase/`
- 为第 9.5 节补齐 CSV、日志、示例项目和代码库输入
- 将 TerminalTool 的危险命令示例由 `rm -rf /` 改为无写入副作用的受限 `sudo -n true`
- 修正第 10.2 节指向不存在 `../HelloAgents/.env` 的路径
- 补齐第 7.4 节上游测试引用但未提供的 Reflection 与 Plan-and-Solve 实现
- 修正 `FunctionCallAgent` 在 `hello-agents==0.2.8` 中的实际导入位置
- 为 `hello-agents==0.2.8` 补充其漏声明的 `huggingface-hub` 运行时依赖
- 固定 AgentScope 的 `mcp<2`，规避 `agentscope==1.0.2` 与 MCP 2.0 的导入不兼容
