import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="me", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', "Keerthana Dutta")
    logging.info("My name is " + name)
    return func.HttpResponse(json.dumps({"name": f"Hello, {name}. This HTTP triggered function executed successfully."}))