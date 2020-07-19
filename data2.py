from datetime import datetime

def validate_date(d):
    try:
        if len(d) == 10: 
            datetime.strptime(d, '%m/%d/%Y')
            return True
        else: return False

    except ValueError:
        return False

print(validate_date('2/26/1000'))
