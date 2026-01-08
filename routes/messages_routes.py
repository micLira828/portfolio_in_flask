from flask import Blueprint, request, jsonify
from utils.email import send_contact_email
from models.message import Message as DBMessage
from app import db
from datetime import datetime


messages_routes = Blueprint(
    "messages",
    __name__,
    url_prefix="/api/messages"
)

@messages_routes.route("", methods=["POST"])
def create_message():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "All fields are required"}), 400

    new_message = DBMessage(
    name=name,
    email=email,
    message=message
    )

    db.session.add(new_message)
    db.session.commit()

    # Send email safely (non-blocking API call)
    try:
        send_contact_email(name, email, message)
    except Exception as e:
        print("Email error:", e)

    return jsonify({"success": True}), 201