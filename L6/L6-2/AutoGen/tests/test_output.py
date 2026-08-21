"""比特币价格应用的离线测试。"""

from __future__ import annotations

import unittest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import output


class OutputTests(unittest.TestCase):
    @patch("output.requests.get")
    def test_get_bitcoin_price(self, mock_get: Mock) -> None:
        response = Mock()
        response.json.return_value = {
            "bitcoin": {"usd": 123456.78, "usd_24h_change": 2.5}
        }
        mock_get.return_value = response

        self.assertEqual(output.get_bitcoin_price(), (123456.78, 2.5))
        response.raise_for_status.assert_called_once_with()
        self.assertEqual(mock_get.call_args.kwargs["timeout"], 10)

    @patch("output.st.error")
    @patch("output.requests.get", side_effect=requests.Timeout("timeout"))
    def test_request_failure_returns_empty_result(
        self,
        _mock_get: Mock,
        mock_error: Mock,
    ) -> None:
        self.assertEqual(output.get_bitcoin_price(), (None, None))
        mock_error.assert_called_once()


if __name__ == "__main__":
    unittest.main()
