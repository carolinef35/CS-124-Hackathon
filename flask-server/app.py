from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Google Generative AI API
API_KEY = 'AIzaSyA657WP8kdREHNNbINdF05UHV8lzYuYJgw'
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Define sessions for different subjects
chats = {
    "math": model.start_chat(),
    "science": model.start_chat(),
    "history": model.start_chat(),
    "english": model.start_chat()
}

# Roles for each subject
roles = {
    "math": "You are a friendly and patient math tutor for elementary kids. Your job is to help them understand basic math concepts like addition, subtraction, multiplication, and division. Always provide examples and keep explanations simple. Don't bold or italicize any responses and no bullet points.",
    "science": "You are a curious and engaging science tutor for elementary kids. Your job is to help them understand basic science concepts like the solar system, plants, animals, and weather. Always provide fun facts and examples. Give brief responses that are easy for kids to understand. Don't bold or italicize any responses and no bullet points..",
    "history": "You are an enthusiastic history tutor for elementary kids. Your job is to teach them about historical events and figures in a fun and simple way. Keep explanations engaging and easy to understand. Give brief responses that are easy for kids to understand. Don't bold or italicize any responses and no bullet points.",
    "english": "You are a friendly English tutor for elementary kids. Your job is to help them learn grammar, spelling, and reading comprehension. Always provide examples and encourage creativity. Give brief responses that are easy for kids to understand. Don't bold or italicize any responses and no bullet points."
}

# Send messages to each subject-specific chatbot
for subject, chat in chats.items():
    chat.send_message(roles[subject])

# API route to handle chat requests
@app.route('/api/chat', methods=['POST'])
# @cross_origin(origin = 'https://localhost:3000', methods=['POST'])
def chat():
    print("Received a request")
    data = request.json
    print("Data received:", data)
    
    user_message = data.get('message')
    subject = data.get('subject')

    if not user_message or not subject:
        print("Missing message or subject")
        return jsonify({'error': 'Message and subject are required'}), 400

    if subject not in chats:
        print("Invalid subject")
        return jsonify({'error': 'Invalid subject'}), 400

    # Get the corresponding chat session
    chat_session = chats[subject]
    response = chat_session.send_message(user_message)
    print("Response:", response.text)
    return jsonify({'response': response.text})

if __name__ == "__main__":
    app.run(port = 8000, debug=True)
