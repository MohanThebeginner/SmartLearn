# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import ask_bot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    if not user_msg:
        return jsonify({'error': 'Missing or malformed "message" key'}), 400
    reply = ask_bot(user_msg)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
