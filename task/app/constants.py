import os

OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL_4 = "gpt-4o"
OPENAI_MODEL_5 = "gpt-5-2025-08-07"

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
ANTHROPIC_ENDPOINT = "https://api.anthropic.com/v1/messages"
ANTHROPIC_MODEL_HAIKU = "claude-haiku-4-5-20251001"
ANTHROPIC_MODEL_SONET = "claude-sonnet-4-5-20250929"
