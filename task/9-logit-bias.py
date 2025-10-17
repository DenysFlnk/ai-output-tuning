from task.app.clients.openai_client import OpenAIClient
from task.app.constants import OPENAI_MODEL_4
from task.app.main import run

openai_client = OpenAIClient(model_name=OPENAI_MODEL_4)

# Ban a word "bird" and try to ask questions about birds
run(
    client=openai_client,
    print_only_content=True,
    print_request=False,
    logit_bias={
        "32981": -100,
        "28510": -100,
        "16189": -100,
        "83642": -100,
        "100222": -100,
        "86199": -100,
        "196672": -100,
    },
)
