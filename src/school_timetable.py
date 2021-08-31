import datetime

from src.calendar import Calendar
from src.event import Event


class SchoolTimeTable:
    def __init__(self, start_date, weeks=18, class_info_path='resource/class_info.txt'):
        self.start_date = start_date
        self.cur_week = 1
        self.weeks = weeks
        self.class_info_path = class_info_path
        self.clazz = self.__read_clazz()
        self.time_map = {
            1: {'start': [8, 0], 'end': [8, 45]},
            2: {'start': [8, 50], 'end': [9, 35]},
            3: {'start': [9, 50], 'end': [10, 35]},
            4: {'start': [10, 40], 'end': [11, 25]},
            5: {'start': [11, 30], 'end': [12, 15]},
            6: {'start': [13, 0], 'end': [13, 45]},
            7: {'start': [13, 50], 'end': [14, 35]},
            8: {'start': [14, 50], 'end': [15, 35]},
            9: {'start': [15, 40], 'end': [16, 25]},
            10: {'start': [16, 30], 'end': [17, 15]},
            11: {'start': [18, 0], 'end': [18, 45]},
            12: {'start': [18, 50], 'end': [19, 35]},
            13: {'start': [19, 40], 'end': [20, 25]},
            14: {'start': [20, 30], 'end': [21, 15]},
        }
        self.ext_days = {
            '天': 6,
            '六': 5,
            '五': 4,
            '四': 3,
            '三': 2,
            '二': 1,
            '一': 0
        }

    def __read_clazz(self):
        file = open(self.class_info_path)
        clazz_list = []
        for info in file.readlines():
            clazz_list.append(info)
        return clazz_list

    def gen_calendar(self):
        cal = Calendar("课程表")
        for i in range(self.weeks):
            cur = self.start_date + datetime.timedelta(days=i * 7)
            for clazz in self.clazz:
                clazz_event = self.parse_clazz(clazz, cur)
                if (clazz_event is not None):
                    cal.add_event(clazz_event)
            self.cur_week += 1
        file = open("../课程表.ics", "w")
        file.write(cal.format())
        file.close()

    def parse_clazz(self, clazz_info, date):
        infos = clazz_info.split("，")
        if (self.check_week(infos[1])):
            ext_days = self.ext_days[infos[2][-1]]
            date = date + datetime.timedelta(days=ext_days)
            start_class_count = eval(infos[3].split('-')[0])
            end_class_count = eval(infos[3].split('-')[1][:-1])
            start = date + datetime.timedelta(
                hours=self.time_map[start_class_count]['start'][0],
                minutes=self.time_map[start_class_count]['start'][1])
            end = date + datetime.timedelta(
                hours=self.time_map[end_class_count]['end'][0],
                minutes=self.time_map[end_class_count]['end'][1])
            e = Event(infos[0], "-".join(infos[-2:]), start, end, description=clazz_info)
            return e
        return None

    def check_week(self, week_range):

        start = eval(week_range.split("-")[0])
        end = eval(week_range.split("-")[1][:-1])
        return start <= self.cur_week <= end
