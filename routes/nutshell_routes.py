from flask import Blueprint, jsonify
from models.nutshell import Nutshell

nutshell_routes = Blueprint("nutshell_routes", __name__, url_prefix="/api/nutshell")


@nutshell_routes.route("/", methods=["GET"])
def get_all_facts():
    facts = Nutshell.query.all()
    return jsonify([fact.to_dict() for fact in facts]), 200
