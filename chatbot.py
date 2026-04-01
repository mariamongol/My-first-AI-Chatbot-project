print("=== AI Study Helper ===")
print("Ask me about math, science, or AI.")
print("Type 'bye' to exit.\n")

def ai_response(user):
    user = user.lower()

    if "math" in user:
        return "Math is about numbers, patterns, and solving problems step by step."

    elif "science" in user:
        return "Science helps us understand how the world works."

    elif "ai" in user or "artificial intelligence" in user:
        return "Artificial Intelligence is about making machines think and learn like humans."

    elif "sad" in user:
        return "I'm sorry you're feeling sad. I'm here for you."

    elif "help" in user:
        return "I'm here to help you learn. Ask me anything!"

    else:
        return "That's a good question. I'm still learning, but let's think about it together."

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("AI: Goodbye!")
        break

    print("AI:", ai_response(user))