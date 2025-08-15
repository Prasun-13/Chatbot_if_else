# chatbot_if_else.py
# Task 8 - Simple Chatbot using if-else in Python

print("🤖 Chatbot: Hello! I am your friendly chatbot.")
print("Type 'bye' anytime to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a great day!")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hi there! How can I help you?")

    elif "your name" in user_input:
        print("🤖 Chatbot: I am ChatBot 1.0, built using Python if-else.")

    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm just code, but I'm running fine! How about you?")

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"🤖 Chatbot: The current time is {current_time}")

    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"🤖 Chatbot: Today's date is {current_date}")

    elif "weather" in user_input:
        print("🤖 Chatbot: I can't fetch live weather, but it's always sunny in Pythonland! 😄")

    elif "help" in user_input:
        print("🤖 Chatbot: You can ask me about my name, time, date, or just say hello.")

    else:
        print("🤖 Chatbot: Sorry, I didn't understand that. Try asking something else.")
