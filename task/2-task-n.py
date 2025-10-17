from task.app.clients.openai_client import OpenAIClient
from task.app.constants import OPENAI_MODEL_4
from task.app.main import run

# TODO:
#  Try the `n` parameter with different models and see the results. With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?


run(
    # TODO:
    # 1. Provide `deployment_name` with model from the list above👆
    # 2. Use `n` parameter with value in range from 1 to 5! (with anthropic it won't work)
    client=OpenAIClient(model_name=OPENAI_MODEL_4),
    n=3,
    print_only_content=False,
    print_request=False,
)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
