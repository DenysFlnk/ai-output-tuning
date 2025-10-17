from task.app.clients.openai_client import OpenAIClient
from task.app.constants import OPENAI_MODEL_4
from task.app.main import run

# TODO:
#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User massage: Name a random animal
openai_client = OpenAIClient(model_name=OPENAI_MODEL_4)


run(
    # TODO:
    #  1. Use `seed` parameter with value 42 (or whatever you want)
    #  2. Use `n` parameter with value 5 (with anthropic it won't work)
    client=openai_client,
    print_request=False,
    print_only_content=False,
    seed=69,
    n=5,
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.

