import os
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
    # Grab the port Render assigns, default to 10000 if not set
    port = int(os.environ.get("PORT", 10000))
    # Listen on all interfaces so Render’s load balancer can reach it
    app.run(host="0.0.0.0", port=port)
