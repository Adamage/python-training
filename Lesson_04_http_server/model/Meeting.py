class Meeting:
    def __init__(self, title, date, uid):
        self.title = title
        self.date = date
        self.uid = uid

    def serialize(self):
        return {'title': str(self.title),
                'date': str(self.date),
                'uid': str(self.uid)}
