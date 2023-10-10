# Copyright (C) 2023 twyleg
import azure.functions as func
import storage


app = func.FunctionApp()


@app.route(route="test/", methods=["POST"])
def test_add(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()
    storage.test_add(body["name"], body["id"])
    return func.HttpResponse("success")


@app.route(route="test/{id:int}", methods=["GET"])
def test_get_by_id(req: func.HttpRequest) -> func.HttpResponse:
    id = req.route_params.get('id')
    try:
        return func.HttpResponse(storage.test_get_by_id(id))
    except Exception as e:
        return func.HttpResponse(status_code=404)


@app.route(route="test/{name}", methods=["GET"])
def test_get_by_name(req: func.HttpRequest) -> func.HttpResponse:
    name = req.route_params.get('name')
    try:
        return func.HttpResponse(storage.test_get_by_name(name))
    except Exception as e:
        return func.HttpResponse(status_code=404)