from app import db
from datetime import datetime

class Nutshell(db.Model):
    __tablename__ = "fun_facts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
