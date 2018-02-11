from model.Meeting import Meeting


def deserialize_meeting(meeting_in_dictionary, uid=None):
    title = meeting_in_dictionary['title']
    date = meeting_in_dictionary['date']
    if not uid and 'uid' in meeting_in_dictionary:
            uid = meeting_in_dictionary['uid']

    return Meeting(title, date, uid)