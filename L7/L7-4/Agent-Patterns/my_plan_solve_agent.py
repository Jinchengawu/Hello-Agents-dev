"""第 7.4.4 节的 Plan-and-Solve 练习实现。"""

from __future__ import annotations

import ast
from typing import Optional

from hello_agents import HelloAgentsLLM, Message, SimpleAgent


DEFAULT_PROMPTS = {
    "planner": """你是 AI 规划专家。将问题分解成按逻辑顺序排列的可执行子任务。
问题: {question}
只输出 Python 字符串列表，例如 ["步骤1", "步骤2"]。""",
    "executor": """你是 AI 执行专家。只解决当前步骤并输出该步骤的结果。
原始问题: {question}
完整计划: {plan}
历史步骤与结果: {history}
当前步骤: {current_step}""",
}


class MyPlanAndSolveAgent(SimpleAgent):
    def __init__(
        self,
        name: str,
        llm: HelloAgentsLLM,
        custom_prompts: Optional[dict[str, str]] = None,
    ) -> None:
        super().__init__(name=name, llm=llm)
        self.prompts = {**DEFAULT_PROMPTS, **(custom_prompts or {})}

    def _ask(self, prompt: str) -> str:
        return self.llm.invoke([{"role": "user", "content": prompt}])

    @staticmethod
    def _parse_plan(raw_plan: str) -> list[str]:
        start, end = raw_plan.find("["), raw_plan.rfind("]")
        if start < 0 or end < start:
            raise ValueError("规划器没有返回 Python 列表")
        value = ast.literal_eval(raw_plan[start : end + 1])
        if not isinstance(value, list) or not value or not all(isinstance(x, str) for x in value):
            raise ValueError("计划必须是非空字符串列表")
        return value

    def run(self, input_text: str, **_kwargs) -> str:
        raw_plan = self._ask(self.prompts["planner"].format(question=input_text))
        plan = self._parse_plan(raw_plan)
        history: list[str] = []
        for step in plan:
            result = self._ask(
                self.prompts["executor"].format(
                    question=input_text,
                    plan=plan,
                    history="\n".join(history) or "无",
                    current_step=step,
                )
            )
            history.append(f"{step}: {result}")
        final_answer = history[-1].split(": ", 1)[-1]
        self.add_message(Message(input_text, "user"))
        self.add_message(Message(final_answer, "assistant"))
        return final_answer

