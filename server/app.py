from flask import Flask, jsonify, request
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
            'title': post_data.get('title'),
            'assignee': post_data.get('assignee'),
            'done': post_data.get('done')
        })
        response_object['msg'] = 'Task added!'
        
    else:
        response_object['inbox'] = INBOX
        response_object['inprogress'] = INPROGRESS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
