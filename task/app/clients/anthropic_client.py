import json
import os

import requests

from task.app.clients.base import AIClient
from task.models.message import Message
from task.models.role import Role

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
ANTHROPIC_ENDPOINT = "https://api.anthropic.com/v1/messages"


class AnthropicAIClient(AIClient):

    def __init__(self, model_name: str):
        super().__init__(
            endpoint=ANTHROPIC_ENDPOINT,
            model_name=model_name,
            api_key=ANTHROPIC_API_KEY,
            api_key_header_name="x-api-key"
        )

    def get_completion(
            self,
            messages: list[Message],
            print_request: bool,
            print_only_content: bool,
            **kwargs
    ) -> Message:
        headers = {
            "x-api-key": self._api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        request_data = {
            "model": self._model_name,
            "max_tokens": kwargs.get("max_tokens", 1024),
            "messages": [message.to_dict() for message in messages],
            **kwargs
        }
        if print_request:
            self._print_request(request_data, headers)

        response = requests.post(url=self._endpoint, headers=headers, json=request_data)

        if response.status_code == 200:
            data = response.json()
            content_blocks = data.get("content", [])
            if content_blocks:
                content = "".join(block.get("text", "") for block in content_blocks if block.get("type") == "text")
                print("" + "=" * 50 + " RESPONSE " + "=" * 50)
                if print_only_content:
                    print(content)
                else:
                    print(json.dumps(data, indent=2, sort_keys=True))
                print("=" * 109)
                return Message(Role.AI, content)
            raise ValueError("No content blocks present in the response")
        else:
            raise Exception(f"HTTP {response.status_code}: {response.text}")
