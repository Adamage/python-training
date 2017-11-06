class Lesson:
    def __init__(self, title):
        self.title = title

    def serialize(self):
        return {'title': str(self.title)}