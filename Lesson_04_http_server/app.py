from flask import Flask, jsonify
from database.DbInMemory import DbInMemory

app = Flask(__name__)
db = DbInMemory()
db.fill_with_examples()


@app.route('/')
def index():
    return "python-training lesson index - welcome!<br><br>" \
           "API description:<br>" \
           "- GET /api/lessons - shows all lessons<br>" \
            "- GET /api/lessons/title/<str:title> - finds lesson by title<br>" \
            "- PUT /api/lessons/title/<str:title> - creates lesson with title<br>" \
            "- GET /api/lessons/index/<int:index> - finds lesson with index"


@app.route('/api/lessons', methods=['GET'])
def get_lessons():
    return jsonify({'lessons': db.get_all_lessons()})


@app.route('/api/lessons/title/<string:title>', methods=['GET'])
def get_lesson_by_title(title):
    return jsonify({'lesson': db.get_lesson_by_title(title)})


@app.route('/api/lessons/title/<string:title>', methods=['PUT'])
def update_lesson(title):
    existing_lesson = db.get_lesson_by_title(title)
    if existing_lesson:
        return "Lesson already exists: " + jsonify({'lesson': existing_lesson})
    else:
        new_lesson, index = db.add_lesson(title)
        return "Created new lesson with index {0} : {1} ".format(index, jsonify({'lesson': new_lesson}))


@app.route('/api/lessons/index/<int:index>', methods=['GET'])
def get_lesson_by_index(index):
    return jsonify({'lesson': db.get_lesson_by_index(index)})

if __name__ == '__main__':
    app.run(debug=True)