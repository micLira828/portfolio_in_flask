import os
import requests

def send_contact_email(name, email, message):
    response = requests.post(
    "https://api.resend.com/emails",
    headers={
    "Authorization": f"Bearer {os.environ.get('RESEND_API_KEY')}",
    "Content-Type": "application/json"
    },
    json={
    "from": "Portfolio <onboarding@resend.dev>",
    "to": [os.environ.get("CONTACT_EMAIL")],
    "subject": f"New Portfolio Message from {name}",
    "html": f"""
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Message:</strong></p>
    <p>{message}</p>
    """
    }
)

response.raise_for_status()