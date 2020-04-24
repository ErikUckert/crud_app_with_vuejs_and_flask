from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# bootstrap some data to display
INBOX = [
    {
        'id': 0,
        'title': 'Task 0',
        'assignee': 'Jack Kerouac',
        'done': False,
        'time': 0
    },
    {
        'id': 1,
        'title': 'Task 1',
        'assignee': 'Max Power',
        'done': False,
        'time': 0
    },
    {
        'id': 2,
        'title': 'Task 2',
        'assignee': 'Jonny Cool',
        'done': True,
        'time': 0
    },
    {
        'id': 3,
        'title': 'Task 3',
        'assignee': 'Lucy Cat',
        'done': True,
        'time': 0
    }
]

INPROGRESS = []

DONE = []

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# main route
@app.route('/books', methods=['GET'])
def all_tasks():
    return jsonify({
        'status': 'success',
        'inbox': INBOX,
        'inprogress': INPROGRESS,
        'done': DONE,
        'msg': 'Hello Vuety!'
    })


if __name__ == '__main__':
    app.run()