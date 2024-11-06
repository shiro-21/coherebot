from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cohere
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

co = cohere.Client(os.getenv("COHERE_API_KEY"))


app = Flask(__name__)
CORS(app)  # Enable CORS


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = co.generate(
        model="command",
        prompt=user_input,
        max_tokens=10000,
        temperature=0.7
    )
    output = response.generations[0].text.strip()
    return jsonify({"response": output})

if __name__ == '__main__':
    app.run(port=5000)
