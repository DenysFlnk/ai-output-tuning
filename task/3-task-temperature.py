from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.main import run


# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#  and determinism. Range:
#    - OpenAI = 0.0 to 2.0, Default: 1.0
#    - Anthropic = 0.0 to 1.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

openai_client = OpenAIClient('gpt-4o')
anthropic_ai_client = AnthropicAIClient('claude-3-haiku-20240307')

run(
    # TODO:
    #  Use `temperature` parameter with value in range from 0.0 to 1.0!
    #  (Optional) Use `temperature` parameter with value 2.1 and check what happens
    client=anthropic_ai_client,
    temperature=1,
    print_request=True,
    print_only_content=False,
)