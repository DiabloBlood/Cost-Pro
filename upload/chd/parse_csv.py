import csv
import re
import json
from pprint import pprint

total = 1144

def des_match():
    result = []
    rows = get_rows(filename)
    count_amount = 0
    count_row = 0
    for row in rows:
        if re.match(r'(^SQC\*CHAO GUO\b)|(^SQC\*C G\b)', row['description']):
            count_amount += row['amount']
            count_row += 1
            result.append(row)
    write_json_file(result, 'temp.json')
    print count_amount
    print count_row


cat = {
    'large_amount': large_amount,
    'auto': auto,
    'transfer': transfer,
    'shopping': shopping,
    'expense': expense
}

primary_cat = ['LAR_AM', 'RES', 'BUY', 'AUTO']
headers = ['Amount', 'Balance', 'Check or Slip #', 'Description', 'Details', 'Posting Date', 'Type']
new_headers = ['amount', 'balance', 'description', 'details', 'date', 'type']

filename = 'csv.CSV'
patterns = get_invert_index()



def row_match(row):
    result = False
    for pattern in patterns.keys():
        if re.match(pattern, row['description']):
            pattern_dict = patterns[pattern]
            for key in pattern_dict.keys():
                row[key] = pattern_dict[key]
            result = True
    return result

def seperate():
    remain = []
    out = []
    main_rows = get_rows(filename)
    for row in main_rows:
        # True to outs
        if row_match(row):
            out.append(row)
        else: 
            remain.append(row)

    write_json_file(remain, 'remain.json')
    write_json_file(out, 'out.json')

    pprint('remain: ' + str(len(remain)))
    pprint('out: ' + str(len(out)))
    pprint('total: ' + str(len(remain) + len(out)))


if __name__ == '__main__':
    des_match()
    # seperate()
    # pprint(get_invert_index())
