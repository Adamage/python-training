from model.Lesson import Lesson


class DbInMemory:
    def __init__(self):
        self.lessons = []

    def add_lesson(self, title):
        new_lesson = Lesson(title=title)
        self.lessons.append(new_lesson)
        index = self.lessons.index(new_lesson)
        return new_lesson.serialize(), index

    def get_lesson_by_index(self, index):
        try:
            return self.lessons[index].serialize()
        except KeyError:
            return None

    def get_lesson_by_title(self, title):
        try:
            lesson = [x for x in self.lessons if x.title == str(title)]
            return lesson[0].serialize()
        except IndexError:
            return None

    def get_all_lessons(self):
        return [x.serialize() for x in self.lessons]

    def fill_with_examples(self):
        for title in ["a", "b", "c"]:
            self.add_lesson(Lesson(title))