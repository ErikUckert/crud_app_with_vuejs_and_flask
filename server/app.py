from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


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
        'id': uuid.uuid4().hex,
        'title': 'Task 0',
        'assignee': 'Jack Kerouac',
        'done': False,
        'time': 0
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Task 1',
        'assignee': 'Max Power',
        'done': False,
        'time': 0
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Task 2',
        'assignee': 'Jonny Cool',
        'done': True,
        'time': 0
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Task 3',
        'assignee': 'Lucy Cat',
        'done': True,
        'time': 0
    }
]

INPROGRESS = []
DONE = []

## Helper Scripts

def remove_task(task_id):
    for task in INBOX:
        if task['id'] == task_id:
            INBOX.remove(task)
            return True
    return False

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# # main route
# @app.route('/tasks', methods=['GET'])
# def main_route():
#     return jsonify({
#         'status': 'success',
#         'inbox': INBOX,
#         'inprogress': INPROGRESS,
#         'done': DONE,
#         'msg': 'Task added!'
#     })

# get / post route
@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        INBOX.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'assignee': post_data.get('assignee'),
            'done': post_data.get('done')
        })
        response_object['msg'] = 'Task added!'
        
    else:
        response_object['INBOX'] = INBOX
        response_object['INPROGRESS'] = INPROGRESS
        response_object['DONE'] = DONE
    return jsonify(response_object)

@app.route('/tasks/<task_id>', methods=['PUT'])
def single_task(task_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_task(task_id)
        INBOX.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'assignee': post_data.get('assignee'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Task updated!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
