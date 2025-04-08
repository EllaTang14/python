import os
import sys
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load configuration from vercel.json
with open('vercel.json', 'r') as f:
    config = json.load(f)
    env_vars = config.get('env', {})
    GEMINI_API_KEY = env_vars.get('GEMINI_API_KEY')
    MODEL_NAME = env_vars.get('MODEL_NAME', 'gemini-1.5-flash')

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = get_ai_response(user_message)
    return jsonify({'response': response})

def cli_interface():
    print("Welcome to the AI Chat CLI! (Type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = get_ai_response(user_input)
        print(f"\nAI: {response}")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli_interface()
    else:
        app.run(debug=True) 