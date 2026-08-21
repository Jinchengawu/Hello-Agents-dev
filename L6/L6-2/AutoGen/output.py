"""AutoGen 团队在教程案例中交付的 Streamlit 比特币价格应用。"""

from __future__ import annotations

import requests
import streamlit as st


COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_bitcoin_price() -> tuple[float | None, float | None]:
    """返回当前美元价格和 24 小时涨跌幅。"""
    try:
        response = requests.get(
            COINGECKO_URL,
            params={
                "ids": "bitcoin",
                "vs_currencies": "usd",
                "include_24hr_change": "true",
            },
            timeout=10,
        )
        response.raise_for_status()
        bitcoin = response.json()["bitcoin"]
        return float(bitcoin["usd"]), float(bitcoin["usd_24h_change"])
    except (requests.RequestException, KeyError, TypeError, ValueError) as exc:
        st.error(f"获取价格失败：{exc}")
        return None, None


def render_app() -> None:
    """渲染 Streamlit 页面。"""
    st.set_page_config(page_title="实时比特币价格", page_icon="₿")
    st.title("实时比特币价格")
    st.caption("通过 CoinGecko 获取最新价格及其 24 小时变化")

    if st.button("刷新价格", type="primary"):
        st.rerun()

    with st.spinner("加载中..."):
        current_price, price_change_percentage = get_bitcoin_price()

    if current_price is not None and price_change_percentage is not None:
        st.metric(
            label="当前比特币价格 (USD)",
            value=f"${current_price:,.2f}",
            delta=f"{price_change_percentage:.2f}%（24 小时）",
        )
    else:
        st.warning("暂时无法获取数据，请稍后重试。")


if __name__ == "__main__":
    render_app()
