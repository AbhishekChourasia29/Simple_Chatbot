# Importing necessary libraries
import random

# Defining the chatbot's responses
responses = {
    "Hi": ["Hello!", "Hi there!", "Hey!"],
    "How are you?": ["I'm doing well, thank you.", "I'm fine, thanks for asking.", "Pretty good!"],
    "What's your name?": ["My name is Chatbot.", "I'm Chatbot, nice to meet you!", "I go by the name of Chatbot."],
    "What do you like?": ["I like talking to people.", "I like helping people.", "I like learning new things."],
    "Bye": ["Goodbye!", "See you later!", "Bye!"]
}

# Defining the chatbot function
def chatbot():
    # Greeting message
    print("Hello! I'm a chatbot. How can I help you?")

    # Chat loop
    while True:
        # Getting user input
        user_input = input("You: ")

        # Checking for exit command
        if user_input.lower() == "bye":
            print("Chatbot: " + random.choice(responses["Bye"]))
            break

        # Checking if user input matches any of the responses
        if user_input in responses:
            print("Chatbot: " + random.choice(responses[user_input]))
        else:
            print("Chatbot: I'm sorry, I don't understand. Can you please rephrase your question?")

# Running the chatbot function
chatbot()
