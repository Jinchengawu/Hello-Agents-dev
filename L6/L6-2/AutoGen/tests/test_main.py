"""不发起网络请求的 AutoGen 案例测试。"""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main


class FakeModelClient:
    pass


class MainTests(unittest.TestCase):
    def test_missing_api_key_has_actionable_error(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "LLM_API_KEY"):
                main.validate_configuration()

    def test_placeholder_api_key_is_rejected(self) -> None:
        with patch.dict(os.environ, {"LLM_API_KEY": "your-api-key-here"}, clear=True):
            with self.assertRaisesRegex(ValueError, "LLM_API_KEY"):
                main.validate_configuration()

    def test_deepseek_api_key_can_be_used_as_fallback(self) -> None:
        with patch.dict(
            os.environ,
            {"DEEPSEEK_API_KEY": "sk-test-key", "LLM_API_KEY": "your-api-key-here"},
            clear=True,
        ):
            self.assertEqual(main.resolve_llm_api_key(), "sk-test-key")
            main.validate_configuration()

    def test_team_contains_roles_in_chapter_order(self) -> None:
        team = main.create_team(FakeModelClient(), max_turns=8, auto_approve=True)
        self.assertEqual(
            [participant.name for participant in team._participants],
            ["ProductManager", "Engineer", "CodeReviewer", "UserProxy"],
        )

    def test_default_task_covers_chapter_requirements(self) -> None:
        self.assertIn("比特币", main.DEFAULT_TASK)
        self.assertIn("24小时", main.DEFAULT_TASK)
        self.assertIn("Streamlit", main.DEFAULT_TASK)


if __name__ == "__main__":
    unittest.main()
