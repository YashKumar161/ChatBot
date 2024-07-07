from flask import Flask, request, render_template
from nltk.tokenize import word_tokenize
import nltk
from responses import responses  # Ensure this is the correct path to your responses dictionary

app = Flask(__name__)

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())
    
    for key, value in responses.items():
        if all(token in key.split() for token in tokens):
            return value
    
    return responses.get("default", "I don't understand that.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['msg']
    bot_response = chatbot_response(user_input)
    return bot_response

if __name__ == '__main__':
    nltk.download('punkt')  # Ensure this line is executed before starting the app
    app.run(debug=True)  # Run the Flask app in debug mode on localhost
