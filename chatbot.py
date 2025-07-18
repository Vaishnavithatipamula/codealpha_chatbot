def chatbot():
    print("🤖 Welcome to ChatBot! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi"]:
            print("Bot: Hi there! 👋")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I'm doing great! Thanks for asking 😊")
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day! 👋")
            break
        elif user_input in ["who are you", "what is your name"]:
            print("Bot: I'm a simple chatbot made with Python 🐍")
        else:
            print("Bot: Sorry, I don't understand that. 😅")

# Run the chatbot
chatbot()
