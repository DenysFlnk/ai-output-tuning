from task.app.clients.openai_client import OpenAIClient
from task.app.constants import OPENAI_MODEL_4
from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children

openai_client = OpenAIClient(model_name=OPENAI_MODEL_4)

run(
    # TODO:
    #  Use `frequency_penalty` parameter with different range (-2.0 to 2.0). (doesn't work with anthropic)
    client=openai_client,
    print_request=False,
    print_only_content=True,
    frequency_penalty=2.0,
)

# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).

