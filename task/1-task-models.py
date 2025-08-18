from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

# TODO:
#  Try different models with such user request:
#  User massage: What LLMs can do?
#  ---
#  Anthropic models: https://docs.anthropic.com/en/docs/about-claude/models/overview
#  OpenAI models: https://platform.openai.com/docs/models

openai_client = OpenAIClient('gpt-4o')
anthropic_ai_client = AnthropicAIClient('claude-3-haiku-20240307')

run(
    client=anthropic_ai_client,
    print_request=True, # Switch to False if you do not want to see the request in console
    print_only_content=False, # Switch to True if you want to see only content from response
)