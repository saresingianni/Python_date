date_entry = input('Inserisci la data di fine mese del lancio del MAI in formato DD-MM-YYYY: ')
year, month, day = map(int, date_entry.split('-'))
date1 = pd.to_datetime(pd.Series(datetime.date(day, month, year)))
