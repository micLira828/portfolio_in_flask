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

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "All fields are required"}), 400

    message = Message(
        name=name,
        email=email,
        message=message
    )

    db.session.add(message)
    db.session.commit()
    
    msg = MailMessage(
    subject=f"New Portfolio Message from {data['name']}",
    recipients=["YOUR_EMAIL@gmail.com"],
    body=f"""
   Name: {data['name']}
   Email: {data['email']}

   Message:
   {data['message']}
   """
   )

    mail.send(msg)


    return jsonify({
        "message": "Message sent successfully"
    }), 201
