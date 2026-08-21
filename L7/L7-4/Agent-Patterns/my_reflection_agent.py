"""第 7.4.3 节的通用 ReflectionAgent 练习实现。"""

from __future__ import annotations

from typing import Optional

from hello_agents import HelloAgentsLLM, Message, SimpleAgent


DEFAULT_PROMPTS = {
    "initial": "请根据以下要求完成任务:\n\n任务: {task}\n\n请提供一个完整、准确的回答。",
    "reflect": """请仔细审查以下回答，并找出可能的问题或改进空间:

# 原始任务:
{task}

# 当前回答:
{content}

请指出不足并给出具体改进建议；若已足够好，请回答“无需改进”。""",
    "refine": """请根据反馈意见改进你的回答:

# 原始任务:
{task}

# 上一轮回答:
{last_attempt}

# 反馈意见:
{feedback}

请提供改进后的回答。""",
}


class MyReflectionAgent(SimpleAgent):
    def __init__(
        self,
        name: str,
        llm: HelloAgentsLLM,
        custom_prompts: Optional[dict[str, str]] = None,
        max_reflections: int = 2,
    ) -> None:
        super().__init__(name=name, llm=llm)
        self.prompts = {**DEFAULT_PROMPTS, **(custom_prompts or {})}
        self.max_reflections = max_reflections

    def _ask(self, prompt: str) -> str:
        return self.llm.invoke([{"role": "user", "content": prompt}])

    def run(self, input_text: str, **_kwargs) -> str:
        answer = self._ask(self.prompts["initial"].format(task=input_text))
        for _ in range(self.max_reflections):
            feedback = self._ask(
                self.prompts["reflect"].format(task=input_text, content=answer)
            )
            if "无需改进" in feedback:
                break
            answer = self._ask(
                self.prompts["refine"].format(
                    task=input_text,
                    last_attempt=answer,
                    feedback=feedback,
                )
            )
        self.add_message(Message(input_text, "user"))
        self.add_message(Message(answer, "assistant"))
        return answer

