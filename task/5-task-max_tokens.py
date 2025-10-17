from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.constants import ANTHROPIC_MODEL_SONET
from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

anthropic_client = AnthropicAIClient(model_name=ANTHROPIC_MODEL_SONET)

run(
    # TODO:
    #  Use `max_tokens` parameter with value 10
    client=anthropic_client,
    print_only_content=True,
    print_request=False,
    max_tokens=10,
)


# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length` or `max_tokens`,
# and if you check the `content,` it is clearly unfinished.

