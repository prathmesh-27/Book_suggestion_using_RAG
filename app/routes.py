from flask import Blueprint, render_template, request, jsonify
from app.services.chatbot_1_ver import get_response

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.json.get("message")
        reply = get_response(user_message)
        return jsonify({"reply": reply})

    return render_template("index.html")
