from datetime import datetime

i = str(raw_input('date'))
try:
    dt_start = datetime.strptime(i, '%Y, %m, %d')
except ValueError:
    print ("Incorrect format")
