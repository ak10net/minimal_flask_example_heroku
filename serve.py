import json
from flask import Flask, request
from serve import get_keywords_api

app = Flask(__name__)

keywords_api = get_keywords_api()

@app.route('/extractpackages', methods=['POST])
def extractpackages():
    input_data = request.json
    output_data = keywords_api(input_data)
    response = json.dumps(output_data)
    return response
