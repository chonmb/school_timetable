import datetime

from src.school_timetable import SchoolTimeTable

if __name__ == '__main__':
    stable = SchoolTimeTable(datetime.datetime(2021, 9, 6))
    stable.gen_calendar()
