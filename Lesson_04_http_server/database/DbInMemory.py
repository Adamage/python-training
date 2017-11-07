from model.Meeting import Meeting
from datetime import datetime


class DbInMemory:
    def __init__(self):
        self.meetings = []

    def add_meeting(self, title, date):
        uid = len(self.meetings) + 1
        new_lesson = Meeting(title, date, uid)
        self.meetings.append(new_lesson)

        return new_lesson.serialize()

    def update_meeting(self, meeting_to_update):
        existing_meeting = None
        for meeting in self.meetings:
            if meeting.uid == meeting_to_update.uid:
                existing_meeting = meeting

        if existing_meeting:
            self.meetings.remove(existing_meeting)
            self.meetings.append(meeting_to_update)
            return meeting_to_update.serialize()
        else:
            return self.add_meeting(meeting_to_update.title, meeting_to_update.date)

    def delete_meeting(self, uid):
        for meeting in self.meetings:
            if meeting.uid == uid:
                self.meetings.remove(meeting)
                return meeting.serialize()

    def get_meeting_by_uid(self, uid):
        for meeting in self.meetings:
            if meeting.uid == uid:
                return meeting.serialize()

        return None

    def get_all_meetings(self):
        return [meeting.serialize() for meeting in self.meetings]

    def fill_with_examples(self):
        self.meetings.append(Meeting("Somename1", datetime.now(), 38780))
        self.meetings.append(Meeting("Somename2", datetime.now(), 80))
