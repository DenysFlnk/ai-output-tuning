from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.constants import ANTHROPIC_MODEL_SONET, OPENAI_MODEL_4
from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#  and determinism. Range:
#    - OpenAI = 0.0 to 2.0, Default: 1.0
#    - Anthropic = 0.0 to 1.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

openai_client = OpenAIClient(model_name=OPENAI_MODEL_4)

anthropic_client = AnthropicAIClient(model_name=ANTHROPIC_MODEL_SONET)

run(
    # TODO:
    #  Use `temperature` parameter with value in range from 0.0 to 1.0!
    #  (Optional) Use `temperature` parameter with value 2.1 and check what happens
    client=openai_client,
    print_request=False,
    print_only_content=True,
    temperature=1.0,
)
