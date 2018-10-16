import datetime
from collections import OrderedDict



"""
General util methods
"""

def get_month_tag(date_str):
    date = datetime.datetime.strptime(date_str, '%m/%d/%Y')
    s = str(date.month)
    month = s if date.month > 9 else '0{}'.format(s)
    return '{}-{}'.format(date.year, month)