from flask import Blueprint, request, jsonify
from models.message import Message
from app import db
from flask_mail import Message
from app import mail as MailMessage


messages_routes = Blueprint(
    "messages",
    __name__,
    url_prefix="/api/messages"
)

@messages_routes.route("/", methods=["POST"])
def create_message():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message_text = data.get("message")

    if not name or not email or not message_text:
    return jsonify({"error": "All fields are required"}), 400

    new_message = Message(
    name=name,
    email=email,
    message=message_text
    )

    db.session.add(new_message)
    db.session.commit()

    msg = MailMessage(
    subject=f"New Portfolio Message from {name}",
    sender=current_app.config["MAIL_USERNAME"],
    recipients=[current_app.config["MAIL_USERNAME"]],
    body=f"""
    Name: {name}
    Email: {email}

    Message:
    {message_text}
    """
    )

    mail.send(msg)

    return jsonify({"message": "Message sent successfully"}), 201