import json
from collections import OrderedDict
import datetime

from costpro import db


"""
IO methods for operating JSON files
"""

def read_json_dict(json_file_path):
    with open(json_file_path, 'r') as f:
        json_dict = json.load(f, object_pairs_hook=OrderedDict)
    return json_dict


def read_json_list(json_file_path):
    with open(json_file_path, 'r') as f:
        json_list = json.load(f, object_pairs_hook=OrderedDict)
    return json_list


def object_as_dict(obj):
    row = {col.key: getattr(obj, col.key) for col in db.inspect(obj).mapper.column_attrs}
    for key in row:
        value = row[key]
        if isinstance(value, datetime.date):
            value = value.strftime("%m/%d/%Y")
        row[key] = value
    return row


def orm_list_as_dict(obj_list):
    return [object_as_dict(obj) for obj in obj_list]


### convert args, form methods
def convert_int(s):
    if s is not None and not isinstance(s, str):
        raise TypeError('Input argument must be str type or None!')
    value = int(s) if s else None
    return value