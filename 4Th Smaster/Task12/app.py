from flask import Flask, render_template, request, jsonify
from hotel_management import get_reply

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_reply", methods=["POST"])
def reply():
    user_msg = request.json.get("message")
    bot_reply = get_reply(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
