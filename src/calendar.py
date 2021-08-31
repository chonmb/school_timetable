# this template abey the rfc5545 standard
class Calendar:
    def __init__(self, name):
        self.version = '2.0'
        self.prodId = 'icalendar-ruby'
        self.calscale = 'GREGORIAN'
        self.name = name
        self.language = 'zh'
        self.region = 'CN'
        self.events = []
        self.template = """BEGIN:VCALENDAR
VERSION:{version}
PRODID:{prodId}
CALSCALE:{calscale}
X-WR-CALNAME:{name}
X-APPLE-LANGUAGE:{language}
X-APPLE-REGION:{region}
{events}
END:VCALENDAR
"""

    def print_ics(self):
        print(self.format())

    def format(self):
        return self.template.format(version=self.version, prodId=self.prodId, calscale=self.calscale, name=self.name,
                                    language=self.language, region=self.region, events=self.format_events())

    def format_events(self):
        if len(self.events) == 0:
            return ""
        else:
            events_split = "\n"
            events_str = []
            for event in self.events:
                events_str.append(str(event))
            return events_split.join(events_str)

    def add_event(self, e):
        self.events.append(e)
