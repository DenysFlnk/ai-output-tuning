from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.constants import ANTHROPIC_MODEL_SONET, OPENAI_MODEL_5
from task.app.main import run

# TODO:
#  Try different models with such user request:
#  User massage: What LLMs can do?
#  ---
#  Anthropic models: https://docs.anthropic.com/en/docs/about-claude/models/overview
#  OpenAI models: https://platform.openai.com/docs/models
#  - 'gpt-4o'
#  - 'claude-3-haiku-20240307'
openai_client = OpenAIClient(model_name=OPENAI_MODEL_5)

anthropic_client = AnthropicAIClient(model_name=ANTHROPIC_MODEL_SONET)

run(
    client=anthropic_client,
    print_request=False,  # Switch to False if you do not want to see the request in console
    print_only_content=True,  # Switch to True if you want to see only content from response
)
