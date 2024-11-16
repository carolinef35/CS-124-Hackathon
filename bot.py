'''
import google.generativeai as genai

API_KEY = 'AIzaSyA657WP8kdREHNNbINdF05UHV8lzYuYJgw'
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# predefined the chatbot's role as a math tutor
role_message = (
    "You are a friendly and patient math tutor for third graders. "
    "Your job is to help them understand basic math concepts, like addition, subtraction, "
    "multiplication, and division, in a simple and encouraging way. Always provide examples "
    "and keep explanations easy to follow."
)
chat.send_message(role_message)

# Chat loop for actual chatbot
while True:
    message = input("You: ")
    if message.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    response = chat.send_message(message)
    print("Chatbot: ", response.text)
'''