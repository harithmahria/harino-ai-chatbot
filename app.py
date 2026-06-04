import uuid
import os
import traceback

from flask import Flask, jsonify, render_template, request, session
from flask_cors import CORS

from rag import OPENAI_KEY, SUPABASE_KEY, SUPABASE_URL, chat, openai_client, supabase

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY", "harino-ai-local-dev-secret")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/health")
def health_check():
    checks = {
        "supabase_url_set": bool(SUPABASE_URL),
        "supabase_key_set": bool(SUPABASE_KEY),
        "openai_key_set": bool(OPENAI_KEY),
        "supabase": "not_checked",
        "openai": "not_checked",
    }

    try:
        supabase.table("documents").select("id").limit(1).execute()
        checks["supabase"] = "ok"
    except Exception as exc:
        checks["supabase"] = f"failed: {type(exc).__name__}"

    try:
        response = openai_client.get(
            "https://api.openai.com/v1/models",
            headers={"Authorization": f"Bearer {OPENAI_KEY}"},
        )
        checks["openai"] = "ok" if response.is_success else f"failed: {response.status_code}"
    except Exception as exc:
        checks["openai"] = f"failed: {type(exc).__name__}"

    return jsonify(checks)


@app.route("/api/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "No message received"}), 400

    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())

    try:
        reply = chat(user_message, session_id=session["session_id"])
        return jsonify({"reply": reply})
    except Exception as exc:
        print("Chat API error:", repr(exc), flush=True)
        traceback.print_exc()
        return jsonify({
            "error": "Chat API failed. Check Railway variables and deployment logs."
        }), 500


if __name__ == "__main__":
    print("=" * 50)
    print("  Harino.ai Assistant")
    print("  Open http://localhost:5000 in je browser")
    print("=" * 50)
    app.run(debug=True, port=5000)
