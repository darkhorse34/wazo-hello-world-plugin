from flask import Blueprint, jsonify

bp = Blueprint("hello_calld", __name__)

@bp.route("/hello", methods=["GET"])
def hello():
    return jsonify({"ok": True, "plugin": "hello-calld"})
