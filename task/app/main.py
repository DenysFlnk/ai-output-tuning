from task.app.clients.base import AIClient
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role


def run(
        client: AIClient,
        print_request: bool = True,
        print_only_content: bool = False,
        **kwargs
) -> None:
    conversation = Conversation()

    print("Type your question or 'exit' to quit.")
    while True:
        user_input = input("> ").strip()
    
        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break
    
        conversation.add_message(Message(Role.USER, user_input))

        print("AI:")
        ai_message = client.get_completion(
            messages=conversation.get_messages(),
            print_request=print_request,
            print_only_content=print_only_content,
            **kwargs
        )
        conversation.add_message(ai_message)
