from flask import Flask,request,jsonify
from models import Schema
from service import TodoService

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<name>')
def hello_name(name):
    return f'Hello {name}!'

@app.route('/todo', methods=['POST'])
def create_todo():
    return jsonify(TodoService().create(request.get_json()))

@app.route('/todo', methods=['GET'])
def read_todo():
    return jsonify(TodoService().read(request.get_json()))

if __name__=='__main__':
    Schema()
    app.run(debug=True)