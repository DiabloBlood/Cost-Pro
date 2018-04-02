PARSING_RULE = {

    'large_amount': {
        'tuition': {
            'tuition_scu': [r'^SANTA CLARA UNIV\b'],
            'tuition_iu': []
        },
        'rent_fee': {},
        'transfer': {}
    },

    'travel': {
        'flight': [],
        'hotel': [],
        'car_rental': [],
        'entrance_fee': []
    },

    'auto': {
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
    },

    'transfer': {
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
    },

    'shopping': {
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
    },

    'expense': {
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
}