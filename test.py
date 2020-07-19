import requests
import re


from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone


date_entry = input('Inserisci la data in ormato DD-MM-YYYY: ')
year, month, day = map(int, date_entry.split('-'))
print(date_entry)

get_ics = requests.get("https://giorni-festivi.eu/ical/italia/2020/").text

gcal = Calendar.from_ical(get_ics)
for component in gcal.walk():
    if component.name == "VEVENT":
        descrizione = component.get('SUMMARY')
        print(descrizione)
        date_start = component.get('DTSTART')
        print (date_start.to_ical())
        date_end1 = component.get('DTEND')
        print (date_end1.to_ical())
        date_time = component.get('DTSTAMP')
        print (date_time.to_ical())
