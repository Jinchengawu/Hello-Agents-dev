"""第 7.4.5 节：使用 HelloAgents 内置 FunctionCallAgent。"""

from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM, ToolRegistry
from hello_agents.agents import FunctionCallAgent
from hello_agents.tools import CalculatorTool


def main() -> None:
    load_dotenv()
    registry = ToolRegistry()
    registry.register_tool(CalculatorTool())
    agent = FunctionCallAgent(
        name="函数调用助手",
        llm=HelloAgentsLLM(),
        tool_registry=registry,
    )
    print(agent.run("计算 (125 + 75) * 3"))


if __name__ == "__main__":
    main()
