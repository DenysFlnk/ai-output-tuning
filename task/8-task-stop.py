from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

# TODO:
#  Try `stop`(for OpenAI) and `stop_sequences` (for Anthropic) parameters.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  `stop_sequences` (list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

openai_client = OpenAIClient('gpt-4o')
anthropic_ai_client = AnthropicAIClient('claude-3-haiku-20240307')

run(
    # TODO:
    #  1. Use `stop` parameter with value "\n\n"
    #  2. Use `stop` parameter with values ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
    #  3. Optional: Set `print_only_content` as False to see the full JSON and what is the `finish_reason`
    client=anthropic_ai_client,
    stop_sequences= ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"],
    print_request=True,
    print_only_content=False,
)


# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.