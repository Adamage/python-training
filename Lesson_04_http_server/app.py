from flask import Flask, jsonify, request
from database.DbInMemory import DbInMemory
from model.Meeting import Meeting
import json

from model.tools import deserialize_meeting

app = Flask(__name__)
db = DbInMemory()
db.fill_with_examples()


@app.route('/')
def index():
    return "python-training lesson index - welcome! <br><br>" \
           "API description :<br>" \
           "- GET /api/meetings - shows all meetings <br>" \
            "- GET /api/meeting/<int:uid> - finds lesson by uid <br>" \
            "- PUT /api/meeting/title/<str:title> - creates lesson with title<br>" \
            "- GET /api/meeting/index/<int:index> - finds lesson with index"


@app.route('/api/meetings', methods=['GET'])
def get_meetings():
    return jsonify({'meetings': db.get_all_meetings()})


@app.route('/api/meeting/<int:uid>', methods=['GET'])
def get_meeting_by_uid(uid):
    return jsonify({'meeting': db.get_meeting_by_uid(uid)})


@app.route('/api/meeting', methods=['POST'])
def add_meeting():
    request_content = request.data
    recreated_dictionary = json.loads(request_content)
    meeting = deserialize_meeting(recreated_dictionary)
    return jsonify({'meeting_created': db.add_meeting(meeting.title, meeting.date)})


@app.route('/api/meeting/<int:uid>', methods=['PUT'])
def update_meeting(uid):
    request_content = request.data
    recreated_dictionary = json.loads(request_content)
    meeting = deserialize_meeting(recreated_dictionary, uid=uid)
    return jsonify({'meeting_updated': db.update_meeting(meeting)})


@app.route('/api/meeting/<int:uid>', methods=['DELETE'])
def delete_meeting(uid):
    return jsonify({'meeting_deleted': db.delete_meeting(uid)})


if __name__ == '__main__':
    app.run(debug=True)