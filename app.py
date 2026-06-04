import uuid
import os

from flask import Flask, jsonify, render_template, request, session
from flask_cors import CORS

from rag import chat

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY", "harino-ai-local-dev-secret")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "No message received"}), 400

    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())

    reply = chat(user_message, session_id=session["session_id"])
    return jsonify({"reply": reply})


if __name__ == "__main__":
    print("=" * 50)
    print("  Harino.ai Assistant")
    print("  Open http://localhost:5000 in je browser")
    print("=" * 50)
    app.run(debug=True, port=5000)
