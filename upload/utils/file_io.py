import os
import json
import csv
from collections import OrderedDict



"""
IO methods for operating CSV and JSON files
"""

def write_json_file(rows, output_file_path):
    rows_json = json.dumps(rows, indent=4)
    with open(output_file_path, 'w') as f:
        f.truncate()
        f.write(rows_json)

    print("File {} finished! Counts: {}".format(output_file_path, len(rows)))


def read_json_file(json_file_path):
    with open(json_file_path, 'r') as f:
        rows = json.load(f, object_pairs_hook=OrderedDict)
    return rows


def get_rows_from_csv(input_file_path):
    result = []
    with open(input_file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)

    return result


def get_all_filenames(dirname):
    result = [file for file in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, file))]
    return result