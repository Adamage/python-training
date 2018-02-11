from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from database.DbSqlLite import DbSqlLite
import os
import sqlite3

db = DbSqlLite()
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_sqllite():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_sqllite()
    return g.sqlite_db


@app.teardown_appcontext
def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('sqllite_schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.route('/')
def index():
    return "python-training lesson index - welcome! <br><br>" \
           "API description :<br>" \
           "- GET /api/meetings - shows all meetings <br>" \
            "- GET /api/meeting/<int:uid> - finds lesson by uid <br>" \
            "- PUT /api/meeting/title/<str:title> - creates lesson with title<br>" \
            "- GET /api/meeting/index/<int:index> - finds lesson with index"

if __name__ == '__main__':
    app.run(debug=True)
