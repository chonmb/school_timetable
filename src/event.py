import datetime


class Event:
    def __init__(self, summary, location, start, end, description=""):
        self.stamp = datetime.datetime.now()
        self.summary = summary
        self.location = location
        self.start = start
        self.end = end
        self.description = description
        self.uid = self.get_uid()
        self.template = """BEGIN:VEVENT
DTSTAMP:{stamp}
UID:{uid}
CLASS:PUBLIC
SUMMARY;LANGUAGE=zh_CN:{summary}
LOCATION:{location}
DTSTART;TZID=Asia/Shanghai:{start}
DTEND;TZID=Asia/Shanghai:{end}
DESCRIPTION:{description}
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:DISABLED
END:VEVENT"""

    def __str__(self):
        return self.template.format(stamp=self.stamp.strftime("%Y%m%dT%H%M%SZ"), uid=self.uid,
                                    summary=self.summary, location=self.location,
                                    start=self.start.strftime("%Y%m%dT%H%M%S"),
                                    end=self.end.strftime("%Y%m%dT%H%M%S"), description=self.description)

    def get_uid(self):
        return hash(self.start.strftime("%Y%m%d") + self.summary)
