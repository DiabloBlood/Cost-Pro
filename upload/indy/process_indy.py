import json
from pprint import pprint

INDY_ALL = 'all_indy_init.json'

def run_indy_expense():
    with open(INDY_ALL) as f:
        rows = json.load(f)
        count = 0
        for row in rows:
            if row['tag'] == 'expense':
                count += row['amount']
    return count

def run_indy_all():
    with open(INDY_ALL) as f:
        rows = json.load(f)
        count = 0
        for row in rows:
            count += row['amount']
    return count

def run_indy_income():
    with open(INDY_ALL) as f:
        rows = json.load(f)
        count = 0
        for row in rows:
            if row['tag'] == 'income':
                count += row['amount']
    return count

if __name__ == '__main__':
    print run_indy_expense()