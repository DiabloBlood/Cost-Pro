from config.parsing_rule import PARSING_RULE
from util.file_io import write_json_file, read_json_file




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
        self.pattern_index = self._get_invert_index()


    def process(self):
        self._write_json_file([self.pattern_index], 'temp.json')


    def _read_json_file(self, json_file_path):
        return read_json_file(json_file_path)


    def _write_json_file(self, rows, output_file_path):
        write_json_file(rows, output_file_path)


    def _get_invert_index(self):
        result = {}
        for master_key in self.parsing_rule:
            master_dict = self.parsing_rule[master_key]
            for general_key in master_dict:
                general_dict = master_dict[general_key]
                for children_key in general_dict:
                    children_list = general_dict[children_key]
                    for pattern in children_list:
                        temp = {}
                        temp['master_cat'] = master_key
                        temp['general_cat'] = general_key
                        temp['children_key'] = children_key
                        result[pattern] = temp
        return result



if __name__ == '__main__':
    process_chase_json('all_chase_debit_csv_init.json')