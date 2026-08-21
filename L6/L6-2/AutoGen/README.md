# AutoGen 0.7.4 软件开发团队实践

本目录复刻《Hello-Agents》第 6.2 节的完整实践：让产品经理、工程师、代码审查员和用户代理通过 `RoundRobinGroupChat` 协作，完成一个实时比特币价格 Streamlit 应用。

## 文件

- `main.py`：完整的四智能体协作实现
- `autogen_software_team.py`：与上游教程同名的运行入口
- `output.py`：章节中团队生成的比特币价格应用（已补齐超时和异常处理）
- `.env.example`：LLM 配置模板
- `requirements.txt`：锁定教程使用的 AutoGen 0.7.4
- `tests/`：不调用 LLM 或 CoinGecko 的离线测试
- `LEARNING_DIAGRAMS.md`：流程图、UML 类图、时序图、状态图、数据流图和排错图
- `diagrams/`：7 张图的独立 Mermaid 源文件与中文归档索引

## 学习图谱

建议在阅读代码前先看 [AutoGen 软件开发团队学习图谱](./LEARNING_DIAGRAMS.md)。其中包含：

- 主程序执行流程图
- AutoGen 运行时对象 UML 类图
- 四智能体协作时序图
- 轮询与终止状态图
- AutoGen 与 Streamlit 两条链路的边界图
- Streamlit/CoinGecko 数据流图
- 启动排错决策图

每张图同时以独立 `.mmd` 文件保存在 [diagrams 图表归档目录](./diagrams/README.md)，
方便单独打开、修改或导出；所有节点、关系说明和 UML Note 均带中文注释。

## 环境准备

建议使用 Python 3.10 或更高版本：

```bash
cd /Users/zhuizhui/Documents/ChatGPT/Hello-Agents/L6/L6-2/AutoGen
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

编辑 `.env`，填写真实的 DeepSeek `LLM_API_KEY`。默认模型为
`deepseek-v4-flash`，服务地址为 `https://api.deepseek.com`。

## 运行四智能体团队

交互验收模式（运行到 UserProxy 时在终端输入 `TERMINATE`）：

```bash
python main.py
```

也可以使用教程原始文件名：`python autogen_software_team.py`。

无人值守演示模式（UserProxy 自动结束流程）：

```bash
python main.py --auto-approve
```

也可以更换任务或限制对话轮数：

```bash
python main.py --task "开发一个待办事项 Web 应用" --max-turns 12
```

团队固定按以下顺序轮询：

1. `ProductManager`：需求分析、技术规划和验收标准
2. `Engineer`：提供完整实现
3. `CodeReviewer`：检查质量、安全与异常处理
4. `UserProxy`：由用户测试并决定是否结束

任意消息出现 `TERMINATE` 时终止，`max_turns` 则用于避免无限循环。

## 运行交付应用

`output.py` 会访问 CoinGecko 公共 API：

```bash
python -m streamlit run output.py
```

## 验证

结构测试不会调用 LLM 或 CoinGecko：

```bash
python -m unittest discover -s tests -v
```

参考：[Hello-Agents 第 6.2 节](https://datawhalechina.github.io/hello-agents/#/./chapter6/%E7%AC%AC%E5%85%AD%E7%AB%A0%20%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91%E5%AE%9E%E8%B7%B5?id=_62-%e6%a1%86%e6%9e%b6%e4%b8%80%ef%bc%9aautogen)
