from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

openai_client = OpenAIClient('gpt-4o')
anthropic_ai_client = AnthropicAIClient('claude-3-haiku-20240307')

run(
    # TODO:
    #  Use `frequency_penalty` parameter with different range (-2.0 to 2.0). (doesn't work with anthropic)
    client=openai_client,
    frequency_penalty=1.0,
    print_request=True,
    print_only_content=False,
)

# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).