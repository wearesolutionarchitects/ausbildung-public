from icalendar import Calendar, Event
from datetime import datetime, timedelta
import re

class StundenplanEvent:
    def __init__(self, subject, start_time, end_time, date):
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time
        self.date = date

    def to_ical_event(self):
        event = Event()
        start_datetime = datetime.combine(self.date, self.start_time)
        end_datetime = datetime.combine(self.date, self.end_time)
        event.add('summary', self.subject)
        event.add('dtstart', start_datetime)
        event.add('dtend', end_datetime)
        return event

class Stundenplan:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def create_ical(self, filename):
        cal = Calendar()
        cal.add('prodid', '-//Stundenplan Kalender//DE')
        cal.add('version', '2.0')

        for event in self.events:
            cal.add_component(event.to_ical_event())

        with open(filename, 'wb') as f:
            f.write(cal.to_ical())
        print(f"Kalender gespeichert als {filename}")

    def parse_readme(self, filepath):
        weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']
        timeslots = {
            '08:00': '09:30',
            '09:40': '10:25',
            '10:25': '11:20',
            '11:20': '12:05',
            '12:35': '13:30',
            '13:30': '14:15',
            '14:15': '15:00',
            '15:00': '16:00'
        }

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        base_date = datetime(2024, 9, 9)  # Montag der Kalenderwoche 37 im Jahr 2024

        for i, day in enumerate(weekdays):
            date = base_date + timedelta(days=i)
            pattern = f'\\| (\\d{{2}}:\\d{{2}}) \\| ([^|]*) \\| ([^|]*) \\| ([^|]*) \\| ([^|]*) \\| ([^|]*) \\|'
            matches = re.findall(pattern, content)

            for match in matches:
                time_slot = match[0]
                subjects = match[1:]

                if subjects[i].strip():
                    subject = subjects[i].strip()
                    start_time = datetime.strptime(time_slot, '%H:%M').time()

                    try:
                        end_time = datetime.strptime(timeslots[time_slot], '%H:%M').time()
                    except KeyError:
                        print(f"Warnung: Kein Endzeitpunkt für Zeitslot {time_slot} gefunden. Überspringe Eintrag.")
                        continue

                    event = StundenplanEvent(subject, start_time, end_time, date)
                    self.add_event(event)

# Beispielhafte Nutzung
def main():
    stundenplan = Stundenplan()

    # Lese und parse die readme.md Datei
    stundenplan.parse_readme('stundenplan/readme.md')

    # Erstelle die .ics Datei
    stundenplan.create_ical('stundenplan/kw37.ics')

if __name__ == '__main__':
    main()