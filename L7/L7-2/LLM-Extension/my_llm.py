# my_llm.py
import os
from typing import Optional
from openai import OpenAI
from hello_agents import HelloAgentsLLM

class MyLLM(HelloAgentsLLM):
    def __init__(
        self,
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        provider: Optional[str] = "deepseek",
        **kwargs
    ):
        if provider == "deepseek":
            print("正在使用自定义的 DeepSeek Provider")
            self.provider = "deepseek"
            
            self.api_key = api_key or os.getenv("LLM_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
            self.base_url = base_url or os.getenv("LLM_BASE_URL") or "https://api.deepseek.com"
            
            # 验证凭证是否存在
            if not self.api_key:
                raise ValueError("DeepSeek API key not found. Please set LLM_API_KEY.")

            # 设置默认模型和其他参数
            self.model = model or os.getenv("LLM_MODEL_ID") or "deepseek-v4-flash"
            self.temperature = kwargs.get('temperature', 0.7)
            self.max_tokens = kwargs.get('max_tokens')
            self.timeout = kwargs.get('timeout', 60)
            
            # DeepSeek 的接口与 OpenAI SDK 兼容。
            self._client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=self.timeout)

        else:
            # 其他 provider 仍交给 HelloAgentsLLM 原有逻辑处理。
            super().__init__(model=model, api_key=api_key, base_url=base_url, provider=provider, **kwargs)
