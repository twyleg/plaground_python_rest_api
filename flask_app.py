# Copyright (C) 2023 twyleg
import storage
import json
from flask import Flask, request, Response
from werkzeug.exceptions import HTTPException, NotFound


flask_app = app = Flask(__name__)


@flask_app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


@flask_app.route("/api/test/", methods=['POST'])
def test_add() -> Response:
    body = request.get_json(force=True)
    storage.test_add(body["name"], body["id"])
    return "success"


@flask_app.route("/api/test/<id>", methods=["GET"])
def test_get_by_id(id: int) -> str | Response:
    try:
        return storage.test_get_by_id(id)
    except Exception as e:
        return Response(status=404)


@flask_app.route("/api/test/<name>", methods=["GET"])
def test_get_by_name(name: str) -> str | Response:
    try:
        return storage.test_get_by_name(name)
    except Exception as e:
        return Response(status=404)


@flask_app.route("/")
def index():
    raise NotFound


def start():
    flask_app.run(host="0.0.0.0", port=7071)


if __name__ == "__main__":
    start()