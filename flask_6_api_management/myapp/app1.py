from flask import Flask, request, jsonify
from flasgger import Swagger
import json

app = Flask(__name__)
Swagger(app)

@app.route('/me', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - me: myname
        in: query
        type: string
        required: false
        default: World
    responses:
      200:
        description: what my name is
    """
    myname = request.args.get('myname', 'Keerthana Dutta')
    return json.dumps({ "name": myname })

if __name__ == '__main__':
    app.run(debug=True)