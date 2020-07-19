import datetime
from datetime import date



date_entry = input('Inserisci la data in ormato DD-MM-YYYY: ')
year, month, day = map(int, date_entry.split('-'))
print(date_entry)
check_input =input('Inserisci un numero  ')
def is_float(check_input):
    if '.' in check_input:
        split_number = check_input.split('.')
        if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
                return True
    return False



inputDate = input("Enter the date in format 'dd/mm/yy' : ")
format = "%Y/%m/d"
while True:
    try:
        datetime.datetime.strptime(inputDate, format)
        print("This is the correct date string format.")

    except ValueError:
      print("This is the incorrect date string format. It should be dd/mm/yy")
    else:
        print ('Thanks,is indeed an integer')
    break



day,month,year = inputDate.split('/')

isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False

if(isValidDate) :
    print ("Input date is valid ..")
else :
    print ("Input date is not valid..")

giorno_data_entry = int(date_entry[0]+date_entry[1]);
mese_data_entry = int(date_entry[3]+date_entry[4]);
anno_data_entry = int(date_entry[6]+date_entry[7]+date_entry[8]+date_entry[9]);


print(giorno_data_entry)
print(mese_data_entry)
print(anno_data_entry)






def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    d1 = date(2013,9,13)
    d2 = date(anno_data_entry,mese_data_entry,giorno_data_entry)
    result1 = diff_dates(d2, d1)
    print ('{} days between {} and {}'.format(result1, d1, d2))
    print ("Happy programmer's day!")

main()
