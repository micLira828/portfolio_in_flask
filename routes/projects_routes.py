from flask import Blueprint, jsonify
from models.project import Project

projects_routes = Blueprint(
    "projects",
    __name__,
    url_prefix="/api/projects"
)

# GET all projects
@projects_routes.route("/", methods=["GET"])
def get_all_projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return jsonify([p.to_dict() for p in projects]), 200


# GET single project
@projects_routes.route("/<int:project_id>", methods=["GET"])
def get_single_project(project_id):
    project = Project.query.get(project_id)

    if not project:
        return jsonify({"error": "Project not found"}), 404

    return jsonify(project.to_dict()), 200
