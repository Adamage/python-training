import sqlite3


class DbSqlLite:
    def __init__(self):
        pass
    #
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    # return render_template('show_entries.html', entries=entries)

    def add_meeting(self, title, date):
        pass

    def update_meeting(self, meeting_to_update):
        pass

    def delete_meeting(self, uid):
        pass

    def get_meeting_by_uid(self, uid):
        pass

    def get_all_meetings(self):
        pass

    def fill_with_examples(self):
        pass