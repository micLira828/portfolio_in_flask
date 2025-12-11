from app import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    link = db.Column(db.String(300))
    image_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    live_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
