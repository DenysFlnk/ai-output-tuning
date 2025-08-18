from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?


run(
    # TODO:
    #  Use `max_tokens` parameter with value 10
)


# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length` or `max_tokens`,
# and if you check the `content,` it is clearly unfinished.