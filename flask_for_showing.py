from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route("/", methods=["GET", "POST"])
def hello_world():
    return {"message": "Hello, welcome to KL Training, this is the first time you're gonna witness Flask."}

@app.route("/what_is_my_name", methods=["GET"])
def second_message():
    return {"message": "Hello, I am satyajeet sahu, and I am the instructor today."}

@app.route("/return_square", methods=["POST"])
def return_square():
    json_received = request.json
    number_retrieved = json_received["number"]
    result_json = {
        "result": number_retrieved * number_retrieved
    }
    return  result_json

@app.route("/blast_the_bomb", methods=["GET"])
def blow_the_bomb():
    return {"file": "img.jpg"}

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port=40001)