import re
from collections import OrderedDict
from configs.parsing_rule import PARSING_RULE
from util.file_io import write_json_file, read_json_file
from pprint import pprint




def process_chase_json(input_filename):
    parse_chase_json = ParseChaseJson(input_filename)
    parse_chase_json.process()


class ParseChaseJson(object):
    """
    Parse json file by expense patterns
    """
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.parsing_rule = PARSING_RULE
        self.patterns = self._get_patterns_info()
        self.rows = self._read_json_file(self.input_filename)


    def process(self):
        # self._write_json_file(self.patterns, 'temp.json')
        self._seperate()
        self._current_des_match()


    def _read_json_file(self, json_file_path):
        return read_json_file(json_file_path)


    def _write_json_file(self, rows, output_file_path):
        write_json_file(rows, output_file_path)


    def _get_patterns_info(self):
        result = []
        for master_key in self.parsing_rule:
            master_dict = self.parsing_rule[master_key]
            for general_key in master_dict:
                general_dict = master_dict[general_key]
                for children_key in general_dict:
                    children_list = general_dict[children_key]
                    for pattern in children_list:
                        temp = OrderedDict()
                        temp['master_cat'] = master_key
                        temp['second_cat'] = general_key
                        temp['children_cat'] = children_key
                        temp['pattern'] = pattern
                        result.append(temp)
        return result


    def _check_row_match(self, row):
        result = False
        for pattern in self.patterns:
            if re.match(pattern['pattern'], row['description']):
                for key in pattern:
                    row[key] = pattern[key]
                result = True
        return result


    def _seperate(self):
        remain = []
        out = []
        for row in self.rows:
            # True to outs
            if self._check_row_match(row):
                out.append(row)
            else: 
                remain.append(row)

        self._write_json_file(remain, 'remain.json')
        self._write_json_file(out, 'out.json')

        print '\n'
        print 'remain: {}'.format(len(remain))
        print 'out: {}'.format(len(out))
        print 'total: {}'.format(len(remain) + len(out))
        print '*****************************************************************'
        print '\n'


    def _current_des_match(self):
        result = []
        count_amount = 0
        pattern = r'^SQC\*J\s\.'
        for row in self.rows:
            if re.match(pattern, row['description']):
                count_amount += row['amount']
                result.append(row)
        self._write_json_file(result, 'temp.json')

        print 'temp: {} rows, amount: {}'.format(len(result), count_amount)
        print '*****************************************************************'
        print '\n'


if __name__ == '__main__':
    process_chase_json('all_chase_debit_csv_init.json')