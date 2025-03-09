import datetime

dt1 = datetime.datetime(2024, 7, 23, 9, 28, 7, 500000)
print("Zeit:", dt1)

dt2 = datetime.datetime.fromisoformat("2024-07-23T09:28:07")
print("Aus ISO-Format:", dt2)
print("Formatiert:", dt2.strftime("%d.%m.%Y %H:%M:%S"))
print(f"Tag: {dt2.day}, Monat: {dt2.month}, Jahr: {dt2.year}, " \
      f"Stunde: {dt2.hour}, Minute: {dt2.minute}, Sekunde: {dt2.second}")
print()

dt2 = dt2.replace(month=9, day=14, minute=35, second=40)
print("Ersetzen:", dt2)
print()

print("dt1 == dt2:", dt1 == dt2)
print("dt1 < dt2:", dt1 < dt2)
print()

td1 = datetime.timedelta(days=3, hours=17)
dt3 = dt2 + td1
print("Zeitdifferenz addieren:", dt3)
td2 = dt3 - dt2
print("Zeitdifferenz:", td2)
print()

dt4 = datetime.datetime.now()
print("Jetzt:", dt4)
wtage = ["", "Montag", "Dienstag", "Mittwoch",
         "Donnerstag", "Freitag", "Samstag", "Sonntag"]
wd = dt4.isoweekday()
print(f"Wochentag: {wd} = {wtage[wd]}")
