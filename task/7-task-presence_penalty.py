from task.app.clients.openai_client import OpenAIClient
from task.app.constants import OPENAI_MODEL_4
from task.app.main import run

# TODO:
#  Try `presence_penalty` parameter.
#  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's
#  likelihood to talk about new topics. Higher values == more topic diversity.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: What is an entropy in LLM's responses?

openai_client = OpenAIClient(model_name=OPENAI_MODEL_4)

run(
    # TODO:
    #  Use `presence_penalty` parameter with different range (-2.0 to 2.0). (doesn't work with anthropic)
    client=openai_client,
    print_only_content=True,
    print_request=False,
    presence_penalty=2.0,
)

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.

