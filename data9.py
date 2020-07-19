import pandas as pd

date1 = pd.to_datetime('28-05-2020', dayfirst=True)

bm_end = pd.tseries.offsets.BMonthEnd()

if date1 == bm_end.rollforward(date1):
    pass
else:
    print("Ricontrolla: " + str(date1) + " non è un fine mese")
    
# prints
# Ricontrolla: 2020-05-28 00:00:00 non è un fine mese
