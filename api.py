from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/index')
def index():
    return "Hello world!"


@app.route('/add_book', methods=["POST"])
def add_book():
    print(request)
    print("dupa1")
    request_json = request.get_json()
    print(request_json)
    name = request_json.get('name')
    print(name)




if __name__ == '__main__':
    app.run()