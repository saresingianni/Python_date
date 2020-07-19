import requests
import re


from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone


date_entry = input('Inserisci la data in ormato DD-MM-YYYY: ')
year, month, day = map(int, date_entry.split('-'))
print(date_entry)
r = requests.get('https://github.com/timeline.json')
print (r.text)
 


dato =input("inserisci una stringa> ")


lunghezza = len(dato)

lato =input("inserisci un numero> ")


print("il numero vale {}".format(lato))
test = len(str(lato))



raggio =input("inserisci un raggio> ")



print("il raggio vale {}".format(raggio))

primi_due_caratteri = dato[0]+dato[1];

anno =input("inserisci anno di riferimento> ")
test_anno = len(str(anno))
print("il test anno {}".format(test_anno))
x = 1900
z = 2100
y = int(input("Inserisci un anno da 1900 a " + str(z) + ":"))

if y >= x and y <= z:
    print("Il numero inserito è esatto")
elif y > z:
    print("l'anno inserito è superiore a quello atteso")
elif y < x:
    print("l'anno inserito è inferiore a quello atteso")



text_cal = requests.get("https://giorni-festivi.eu/ical/italia/"+str(y)).text
testo = requests.get("https://giorni-festivi.eu/ical/italia/"+str(y)).text

#print (text_cal)
#print (testo)

testo_list = [requests.get("https://giorni-festivi.eu/ical/italia/"+str(y)).text]

print (testo_list)

#g = open('example.ics','rb')
gcal = Calendar.from_ical(testo)
for component in gcal.walk():
    print (component.name)
#g.close()







gcal = Calendar.from_ical(testo)
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



#text_cerca = 'DTSTAMP:.*?:"'
#for pattern in testo:
#    print('Looking for "%s" in "%s" ->' % (pattern, testo), end=' ')
#    if re.search(pattern, testo):
#        print('found a match!')
#else:
#    print('no match')






list = ["guru99 get", "guru99 give", "guru Selenium"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
if z:
    print((z.groups()))
    
patterns = ['software testing', 'guru99']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')
abc = 'guru99@google.com, careerguru99@hotmail.com, sers@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print(email)





#print(re.search("BEGIN:.*?:", testo, re.DOTALL).group())
#print(re.search("UID:.*?:", testo, re.DOTALL).group())
#print(re.search("DTSTAMP:.*?:", testo, re.DOTALL).group())
#print(re.search("DTSTART:.*?:", testo, re.DOTALL))
#print(re.search("DTEND:.*?:", testo, re.DOTALL))
#print(re.search("SUMMARY:.*?:", testo, re.DOTALL).group())
#print(re.search("DESCRIPTION:.*?:", testo, re.DOTALL).group())
#print(re.search("STATUS:.*:?", testo, re.DOTALL).group())
#print(re.search("END:.*:?", testo, re.DOTALL).group())
#print(re.findall("BEGIN:.*?:", testo, re.DOTALL).group())
#print(re.findall("UID:.*?:", testo, re.DOTALL).group())
#print(re.findall("DTSTAMP:.*?:", testo, re.DOTALL).group())
#print(re.findall("DTSTART:.*?:", testo, re.DOTALL))
#print(re.findall("DTEND:.*?:", testo, re.DOTALL))
#print(re.findall("SUMMARY:.*?:", testo, re.DOTALL).group())
#print(re.findall("DESCRIPTION:.*?:", testo, re.DOTALL).group())
#print(re.findall("STATUS:.*:?", testo, re.DOTALL).group())
#print(re.findall("END:.*:?", testo, re.DOTALL).group())






#BEGIN:VEVENT
#UID:italia--2020-1@giorni-festivi.eu
#DTSTAMP:20200101T000000
#DTSTART;VALUE=DATE:20200101
#DTEND;VALUE=DATE:20200101
#SUMMARY:Capodanno 
#DESCRIPTION:giorno festivo nazionale in Italia | giorni-festivi.eu. All data without guarantee! / Alle Angaben ohne GewÃ¤hr!
#STATUS:CONFIRMED
#END:VEVENT
#BEGIN:VEVENT

# if (test_anno <4 and test_anno >5 ):
 #   print("anno non valido")
 #   elif :
 #  print("anno valido")
