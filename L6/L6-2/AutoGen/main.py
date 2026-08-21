"""第 6.2 节：使用 AutoGen 组建软件开发团队。"""

from __future__ import annotations

import argparse
import asyncio
import os
from collections.abc import Callable

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv


_PLACEHOLDER_API_KEYS = frozenset(
    {
        "",
        "your-api-key-here",
        "your-api-key",
        "your-deepseek-api-key",
        "sk-your-api-key",
        "changeme",
        "placeholder",
    }
)


def resolve_llm_api_key() -> str:
    """从环境变量解析可用的 LLM API Key。"""
    for env_name in ("LLM_API_KEY", "DEEPSEEK_API_KEY"):
        value = (os.getenv(env_name) or "").strip()
        if value.casefold() not in _PLACEHOLDER_API_KEYS:
            return value
    return ""


def validate_configuration() -> None:
    """在发起请求前给出明确的配置错误。"""
    api_key = resolve_llm_api_key()
    if not api_key:
        raise ValueError(
            "缺少有效的 LLM_API_KEY；请复制 .env.example 为 .env，"
            "并将 LLM_API_KEY 替换为真实的 DeepSeek API Key"
        )


DEFAULT_TASK = """我们需要开发一个比特币价格显示应用，具体要求如下：

核心功能：
- 实时显示比特币当前价格（USD）
- 显示24小时价格变化趋势（涨跌幅和涨跌额）
- 提供价格刷新功能

技术要求：
- 使用 Streamlit 框架创建 Web 应用
- 界面简洁美观，用户友好
- 添加适当的错误处理和加载状态

请团队协作完成这个任务，从需求分析到最终实现。"""


def create_openai_model_client() -> OpenAIChatCompletionClient:
    """通过 OpenAI-compatible 接口创建 DeepSeek 模型客户端。"""
    validate_configuration()
    return OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL_ID", "deepseek-v4-flash"),
        api_key=resolve_llm_api_key(),
        base_url=os.getenv("LLM_BASE_URL", "https://api.deepseek.com"),
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": "unknown",
            "structured_output": False,
        },
    )


def create_product_manager(model_client: OpenAIChatCompletionClient) -> AssistantAgent:
    """创建产品经理智能体。"""
    system_message = """你是一位经验丰富的产品经理，专门负责软件产品的需求分析和项目规划。

你的核心职责包括：
1. **需求分析**：深入理解用户需求，识别核心功能和边界条件
2. **技术规划**：基于需求制定清晰的技术实现路径
3. **风险评估**：识别潜在的技术风险和用户体验问题
4. **协调沟通**：与工程师和其他团队成员进行有效沟通

当接到开发任务时，请按以下结构进行分析：
1. 需求理解与分析
2. 功能模块划分
3. 技术选型建议
4. 实现优先级排序
5. 验收标准定义

请简洁明了地回应，并在分析完成后说“请工程师开始实现”。"""
    return AssistantAgent(
        name="ProductManager",
        model_client=model_client,
        system_message=system_message,
    )


def create_engineer(model_client: OpenAIChatCompletionClient) -> AssistantAgent:
    """创建软件工程师智能体。"""
    system_message = """你是一位资深的软件工程师，擅长 Python 开发和 Web 应用构建。

你的技术专长包括：
1. **Python 编程**：熟练掌握 Python 语法和最佳实践
2. **Web 开发**：精通 Streamlit、Flask、Django 等框架
3. **API 集成**：有丰富的第三方 API 集成经验
4. **错误处理**：注重代码的健壮性和异常处理

当收到开发任务时，请：
1. 仔细分析技术需求
2. 选择合适的技术方案
3. 编写完整的代码实现
4. 添加必要的注释和说明
5. 考虑边界情况和异常处理

请提供完整的可运行代码，并在完成后说“请代码审查员检查”。"""
    return AssistantAgent(
        name="Engineer",
        model_client=model_client,
        system_message=system_message,
    )


def create_code_reviewer(model_client: OpenAIChatCompletionClient) -> AssistantAgent:
    """创建代码审查员智能体。"""
    system_message = """你是一位经验丰富的代码审查专家，专注于代码质量和最佳实践。

你的审查重点包括：
1. **代码质量**：检查代码的可读性、可维护性和性能
2. **安全性**：识别潜在的安全漏洞和风险点
3. **最佳实践**：确保代码遵循行业标准和最佳实践
4. **错误处理**：验证异常处理的完整性和合理性

审查流程：
1. 仔细阅读和理解代码逻辑
2. 检查代码规范和最佳实践
3. 识别潜在问题和改进点
4. 提供具体的修改建议
5. 评估代码的整体质量

请提供具体的审查意见，完成后说“代码审查完成，请用户代理测试”。"""
    return AssistantAgent(
        name="CodeReviewer",
        model_client=model_client,
        system_message=system_message,
    )


def create_user_proxy(*, auto_approve: bool = False) -> UserProxyAgent:
    """创建用户代理；可选择自动结束以便无人值守演示。"""
    input_func: Callable[[str], str] | None = None
    if auto_approve:
        input_func = lambda _prompt: "TERMINATE"

    kwargs = {
        "name": "UserProxy",
        "description": """用户代理，负责以下职责：
1. 代表用户提出开发需求
2. 执行最终的代码实现
3. 验证功能是否符合预期
4. 提供用户反馈和建议

完成测试后请回复 TERMINATE。""",
    }
    if input_func is not None:
        kwargs["input_func"] = input_func
    return UserProxyAgent(**kwargs)


def create_team(
    model_client: OpenAIChatCompletionClient,
    *,
    max_turns: int = 20,
    auto_approve: bool = False,
) -> RoundRobinGroupChat:
    """按需求、编码、审查、验收的顺序创建轮询团队。"""
    return RoundRobinGroupChat(
        participants=[
            create_product_manager(model_client),
            create_engineer(model_client),
            create_code_reviewer(model_client),
            create_user_proxy(auto_approve=auto_approve),
        ],
        termination_condition=TextMentionTermination("TERMINATE"),
        max_turns=max_turns,
    )


async def run_software_development_team(
    task: str = DEFAULT_TASK,
    *,
    max_turns: int = 20,
    auto_approve: bool = False,
):
    """运行软件开发团队协作，并在终端流式展示对话。"""
    print("🔧 正在初始化模型客户端...")
    model_client = create_openai_model_client()
    try:
        print("👥 正在创建智能体团队...")
        team_chat = create_team(
            model_client,
            max_turns=max_turns,
            auto_approve=auto_approve,
        )
        print("🚀 启动 AutoGen 软件开发团队协作...")
        print("=" * 60)
        result = await Console(team_chat.run_stream(task=task))
        print("\n" + "=" * 60)
        print("✅ 团队协作完成！")
        return result
    finally:
        await model_client.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", default=DEFAULT_TASK, help="发送给团队的开发任务")
    parser.add_argument("--max-turns", type=int, default=20, help="最大对话轮数")
    parser.add_argument(
        "--auto-approve",
        action="store_true",
        help="UserProxy 自动回复 TERMINATE；默认由用户在终端验收",
    )
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()
    if args.max_turns < 1:
        raise ValueError("--max-turns 必须大于 0")
    result = asyncio.run(
        run_software_development_team(
            args.task,
            max_turns=args.max_turns,
            auto_approve=args.auto_approve,
        )
    )
    print("\n📋 协作结果摘要：")
    print("- 参与智能体数量：4 个")
    print(f"- 任务完成状态：{'成功' if result else '需要进一步处理'}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        raise SystemExit(f"❌ 配置错误：{exc}") from exc
    except RuntimeError as exc:
        message = str(exc)
        if "invalid_api_key" in message or "AuthenticationError" in message:
            raise SystemExit(
                "❌ API 密钥无效：请在 .env 中填写真实的 LLM_API_KEY，"
                "并确认 LLM_BASE_URL 与 LLM_MODEL_ID 与你的服务商一致。"
            ) from exc
        raise
    except KeyboardInterrupt:
        raise SystemExit("\n已取消。") from None
