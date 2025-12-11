from app import create_app, db
from models.project import Project
from models.nutshell import Nutshell
from models.message import Message

# Create app context
app = create_app()

with app.app_context():
    print("Clearing old data...")
    db.drop_all()
    db.create_all()

    print("Seeding portfolio projects...")

    p1 = Project(
        title="Identi — Branding Agency Landing Page",
        description=(
            "A sleek, modern branding-agency landing page featuring the Identi brand identity. "
            "Designed to showcase creative services through clean layout, strong typography, "
            "and a polished professional aesthetic. Includes responsive design suitable "
            "for client-facing presentations."
        ),
        github_url="https://github.com/miclira828/IdentiLandingPage",
        live_url="https://miclira828.github.io/IdentiLandingPage/"
    )

    p2 = Project(
        title="Marketing Page — Business Landing Page",
        description=(
            "A simple, clean marketing landing page built with HTML, CSS, and JavaScript. "
            "Features a modern, responsive layout and floating contact icons. "
            "Designed to showcase strong visual structure and brand-consistent presentation."
        ),
        github_url="https://github.com/miclira828/Marketing-Page",
        live_url="https://miclira828.github.io/Marketing-Page/"
    )

    print("Seeding nutshell facts...")

    f1 = Nutshell(content="I create aesthetic-coded digital interfaces.")
    f2 = Nutshell(content="I love structured workflows like schemas, boards, and planners.")
    f3 = Nutshell(content="I design both APIs and beautiful frontends — the full stack magic!")

    
    print("Seeding example contact message...")

    m = Message(
        name="Test User",
        email="test@example.com",
        message="Your portfolio backend is fully connected!"
    )

    db.session.add_all([p1, p2, f1, f2, f3, m])
    db.session.commit()

    print("✨ Seeding complete!")
