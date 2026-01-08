from flask import Blueprint, request, jsonify, current_app
from models.message import Message as DBMessage
from flask_mail import Message as MailMessage
from app import db, mail 


messages_routes = Blueprint(
    "messages",
    __name__,
    url_prefix="/api/messages"
)

@messages_routes.route("", methods=["POST", "OPTIONS"])
def create_message():
    if request.method == "OPTIONS":
        return "", 204
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message_text:
        return jsonify({"error": "All fields are required"}), 400

    new_message = DBMessage(
    name=name,
    email=email,
    message=message
    )

    db.session.add(new_message)
    db.session.commit()

    # EMAIL SHOULD NEVER CRASH THE REQUEST
    try:
        msg = MailMessage(
        subject=f"New Portfolio Message from {name}",
        sender=current_app.config["MAIL_USERNAME"],
        recipients=[current_app.config["MAIL_USERNAME"]],
        body=f"From: {name} <{email}>\n\n{message}"
        )
        mail.send(msg)
    except Exception as e:
        print("Email failed:", e)

    return jsonify({"success": True}), 201