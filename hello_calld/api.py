from flask import Blueprint, jsonify

bp = Blueprint("hello_calld", __name__)

@bp.route("/hello", methods=["GET"])
def hello():
    # minimal test endpoint
    return jsonify({"ok": True, "service": "wazo-calld", "plugin": "hello-calld"})
