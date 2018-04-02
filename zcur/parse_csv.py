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

def get_invert_index():
    result = {}
    for master_key in cat.keys():
        master_dict = cat[master_key]
        for subkey_1 in master_dict.keys():
            subdict_1 = master_dict[subkey_1]
            for subkey_2 in subdict_1.keys():
                sublist_2 = subdict_1[subkey_2]
                for pattern in sublist_2:
                    temp = {}
                    temp['master_cat'] = master_key
                    temp['subcat_1'] = subkey_1
                    temp['subcat_2'] = subkey_2
                    result[pattern] = temp
    return result

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

def flat_str(s):
    arr = s.split(' ')
    result = []
    for item in arr:
        if item:
            result.append(item)
    return ' '.join(result)

def get_rows(filename):
    result = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            temp = {}
            temp['amount'] = float(row['Amount'])
            temp['balance'] = row['Balance']
            temp['description'] = flat_str(row['Description'])
            temp['details'] = row['Details']
            temp['date'] = row['Posting Date']
            temp['type'] = row['Type']
            temp['tag'] = 'income' if temp['amount'] > 0.0 else 'expense' 
            result.append(temp)
    return result

def write_json_file(rows, filename):
    rows_json = json.dumps(rows, indent=4)
    with open(filename, 'w') as f:
        f.truncate()
        f.write(rows_json)

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
