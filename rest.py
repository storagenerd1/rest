'''Build by Storagenerd'''
from flask import Flask, abort, jsonify, request
import os

port = int(os.getenv("PORT"))

tasks = [
    {
        'id': 1,
        'title': u'volt',
        'description': u'5', 
        'done': False
    },
    {
        'id': 2,
        'title': u'watt',
        'description': u'25', 
        'done': False
    }
]

'''Load Flask'''
app = Flask(__name__)

'''Define paths and responses'''
@app.route('/')
def index():
    return "This app is api driven only"

@app.route('/api/v0.1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/api/v0.1/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
