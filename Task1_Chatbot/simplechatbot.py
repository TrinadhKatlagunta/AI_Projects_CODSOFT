import random
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "default": ["Sorry, I don't understand.", "Could you please repeat that?", "I'm not sure I follow."],
}
def respond(input_text):
    input_text = input_text.lower()
    if input_text in responses:
        return random.choice(responses[input_text])
    else:
        return random.choice(responses["default"])
def start():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        response = respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
            break
start()
