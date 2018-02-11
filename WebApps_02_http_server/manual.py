from database.DbInMemory import DbInMemory

if __name__ == '__main__':
    db = DbInMemory()
    response = db.add_meeting('aaa', '2000')
    response = db.add_meeting('aaa', '2000')
    response = db.add_meeting('aaa', '2000')
    response = db.add_meeting('aaa', '2000')
    response = db.add_meeting('aaa', '2000')
    all_meeting_resposne = db.get_all_meetings()
    print(all_meeting_resposne)
    #db.delete_meeting(response['uid'])