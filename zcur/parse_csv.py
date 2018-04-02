import csv
import re
import json
from pprint import pprint

total = 1144

large_amount = {
    'tuition': {
        'tuition_scu': [r'^SANTA CLARA UNIV\b'],
        'tuition_iu': []
    },
    'rent_fee': {},
    'transfer': {}
}

travel = {
    'flight': [],
    'hotel': [],
    'car_rental': [],
    'entrance_fee': []
}

auto = {
    'auto_insurance': {
        'progressive': [r'^PROG\b']
    },
    'gas': {
        'costco_gas': [r'^COSTCO GAS\b'],
        'other_gas': [r'^CHEVRON', r'^SHELL OIL', r'^ARCO\b']
    },
    'auto_service': {
        'parking': [r'^MAXXUM LEASING\b', r'^ABM PARKING\b'],
        'car_wash': [r'^SHELL Service Station\b']
    }
}

transfer = {
    'chase_quickpay': {
        'phone_fees': [r'^(Chase QuickPay).*(Phone fees)$'],
        'other': []
    },
    'square_cash' :{
        'chao_guo': [r'(^SQC\*CHAO GUO\b)|(^SQC*C G\b)']
    },
    'paypal': {

    },
    'ATM': {
        'withdraw': [r'^ATM WITHDRAWAL\b'],
        'deposit': [r'^ATM CASH DEPOSIT\b']
    }
}

shopping = {
    'online_shopping': {
        'amazon': [r'(^AMAZON\b|^Amazon\.com\b)'],
        'groupon': [r'^GROUPON\b'],
        'books': [r'^.*[Aa][Bb][Ee][Bb][Oo][Oo][Kk][Ss].*$']
    },
    'offline_shopping': {
        'outlets': [
            r'^ABERCROMBIE & FITCH\b', 
            r'^OLD NAVY\b', 
            r'^GAP OUTLET\b', 
            r'.*Milpitas Factory\b',
            r'^EXPRESS LLC MILPITAS\b'
        ],
        'personal_tailor': []
    },
    'super_market': {
        'safeway': [r'^SAFEWAY\b'],
        'costco': [r'^COSTCO WHSE\b'],
        'whole_foods': [r'^WHOLEFDS\b'],
        'wal_mart': [r'^WAL\b'],
        'ocean': [r'^OCEAN SUPERMARKET\b'],
        'trader_joe': [r'^TRADER JOE\'S\b'],
        'target': [r'^TARGET\b'],
        '99ranch': [r'^99 RANCH\b'],
        'mecico': [
            r'^MI RANCHO\b', 
            r'^EL SUPER\b', 
            r'^ISLAND PACIFIC SUPERMA\b', 
            r'^Hankook Superma\b'
        ]
    }
}

expense = {
    'restaurant': {
        'working_place': [r'^HAPPY KITCHEN\b'],
        'party': [
            r'^YANG BBQ\b', 
            r'^DAVE & BUSTER\'S\b', 
            r'^YUM NOODLES\b', 
            r'^CLASSIC GUILIN NOODLE\b',
            r'^DUSITA THAI CUISINE\b',
            r'^MOMS TOFU HOUSE\b',
            r'^HOG ISLAND\b',
            r'^THAI RECIPE CUISINE\b',
            r'^Pizza My Heart\b',
            r'^CRABAHOLIC\b',
            r'^CBI KITCHEN\b',
            r'^PILGRIMS WAY CARMEL\b',
            r'^BUFFALO WILD WINGS\b',
            r'^SUS MONGOLIAN\b',
            r'^CHEESECAKE SAN JOSE\b',
            r'^GOLDEN CHOPSTICK MILPITAS\b',
            r'^CHINA MAX LIVERMORE\b',
            r'^EL AMIGO RESTAURAN\b',
            r'^SHAO MOUNTAIN RESTAURAN\b',
            r'^MILPITAS BUFFET\b'
            r'^PURPLEKOW BERKELEY\b'
        ],
        'daily_food': [
            r'^TONKOTSU\b', 
            r'^IKE\'S LOVE\b', 
            r'(^IN-N-OUT\b|^IN N OUT\b)', 
            r'^NEW PHO\b', 
            r'^MCDONALD\'S\b',
            r'^SUBWAY\b',
            r'^RUBY THAI KITCHEN\b',
            r'^CHIPOTLE\b',
            r'^PANDA EXPRESS\b',
            r'^HOMETOWN BUFFET\b',
            r'^JAPAN CAFE\b',
            r'^PLATA\'S MEXICAN\b',
            r'^ASADEROS MEXICAN\b',
            r'^JACK IN THE BOX\b',
            r'^BURGER KING\b',
            r'^FORTUNE COOKIE\b',
            r'^JOHNNY ROCKETS\b',
            r'^RUNWAY GRILL\b'
        ]
    },
    'drink': {
        'milk_tea': [r'^85C BAKERY CAFE\b'],
        'vending_machine': [r'^COCA COLA\b'],
        'starbucks': [r'^STARBUCKS\b', r'^SCU DINING\b']
    },
    'membership': {
        'chase_monthly_maintain': [r'(^MONTHLY SERVICE\b)|(^SERVICE FEE$)']
    },
    'service': {
        'hair_cut': [r'^SCHROEDERS HAIRCUTS\b']
    }
}

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
