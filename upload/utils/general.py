import datetime



"""
General util methods
"""

def get_month_tag(date_str):
    date = datetime.datetime.strptime(date_str, '%m/%d/%Y')
    month = date.month if date.month > 9 else '0{}'.format(date.month)
    return '{}-{}'.format(date.year, month)