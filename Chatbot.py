ANS = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What do you need help with?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "help": "Sure! I can answer basic questions. Try asking about my features.",
    "what is your name": "I'm a simple rule-based chatbot!",
    "bye": "Goodbye! Have a great day!"
}


def getResponse(Input):
    response = ANS.get(Input.lower())
    print(response)


while True:
    Q = input("Write something: ").strip()
    getResponse(Q)
    if Q.upper() == "BYE":
        break