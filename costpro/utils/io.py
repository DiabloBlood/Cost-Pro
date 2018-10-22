import json
import base64
from collections import OrderedDict



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


def b64_to_dict(b64_str):
    ascii_str = base64.b64decode(b64_str).decode('utf-8')
    return json.loads(ascii_str)


### convert args, form methods
def convert_int(s):
    if s is not None and not isinstance(s, str):
        raise TypeError('Input argument must be str type or None!')
    value = int(s) if s else None
    return value