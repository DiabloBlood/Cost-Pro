import json
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
