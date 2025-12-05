from flask import Flask, render_template, request, jsonify
from chatbot import get_response  

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_msg = request.json.get('message')
    bot_msg = get_response(user_msg)
    return jsonify({'response': bot_msg})



if __name__ == '__main__':
    app.run(debug=True)
