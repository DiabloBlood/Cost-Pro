import os
from collections import OrderedDict
from pprint import pprint
import traceback

from util.file_io import write_json_file, read_json_file, get_rows_from_csv, get_all_filenames
from util.general import get_month_tag


"""
All the directory or path variable names in this piece of code refer to relative paths.
If a directory var name refer to an absolute paths, the var name will contains "abs" to specify.
"""

def process_indy_trans(input_dir):
    """
    :type input_dir: string
    :param input_dir: relative path name of input folder
    """
    assert isinstance(input_dir, basestring), 'The input folder name must be a string!'
    assert os.path.isdir(input_dir), 'The input folder must be a directory!'
    indy_trans = IndyTrans(input_dir)
    if indy_trans.process():
        print 'Process all indy csv files successfully!'
    else:
        raise Exception('Process indy csv files failed!')

    return True


class IndyTrans(object):
    """
    Parse and calculte indy statements and transactions (Chase statement PDF before Aug 2015)
    """
    SIGNATURE = 'INDY-'
    OUTPUT_DIR = 'all_indy_jsons'
    BY_MONTH_OUTPUT_DIR = 'all_indy_by_month_jsons'
    ALL_MERGED_FILENAME = 'all_indy_init.json'
    INIT_BALANCE = 0.0
    PRECISION = 0.000001


    def __init__(self, input_dir):
        """
        :type input_dir: string
        :param input_dir: relative path name of input folder
        """
        self.input_dir = input_dir
        self.output_dir = self.OUTPUT_DIR
        self.by_month_output_dir = self.BY_MONTH_OUTPUT_DIR
        self.begin_balance = self.INIT_BALANCE
        self.csv_list = self._get_all_filenames(self.input_dir)
        self._make_all_output_dirs()


    def process(self):
        result = True
        try:
            for csv_filename in self.csv_list:
                rows = self._get_rows(os.path.join(self.input_dir, csv_filename), csv_filename)
                output_filename = self._make_output_filename(csv_filename)
                output_file_path = os.path.join(self.output_dir, output_filename)
                self._write_json_file(rows, output_file_path)
            self._merge_json_file()
            self._split_by_month()
        except Exception, e:
            traceback.print_exc()
            result = False
        return result


    def _get_all_filenames(self, dirname):
        return get_all_filenames(dirname)


    def _make_all_output_dirs(self):
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

        if not os.path.exists(self.by_month_output_dir):
            os.mkdir(self.by_month_output_dir)


    def _make_output_filename(self, input_filename):
        arr = input_filename.split('.')
        return arr[0] + '.json'


    def _read_json_file(self, json_file_path):
        return read_json_file(json_file_path)


    def _get_rows_from_csv(self, csv_file_path):
        return get_rows_from_csv(csv_file_path)


    def _write_json_file(self, rows, output_file_path):
        write_json_file(rows, output_file_path)


    def _merge_json_file(self):
        # all_merged_file_path = os.path.join(self.output_dir, self.ALL_MERGED_FILENAME)
        json_list = self._get_all_filenames(self.output_dir)
        result = []
        for json_filename in json_list:
            json_file_path = os.path.join(self.output_dir, json_filename)
            result.extend(self._read_json_file(json_file_path))
        for i in range(len(result)):
            result[i]['TRANSACTION_ID'] = self.SIGNATURE + str(i + 1)
        self._write_json_file(result, self.ALL_MERGED_FILENAME)


    def _split_by_month(self):
        rows = self._read_json_file(self.ALL_MERGED_FILENAME)
        month_tag_map = {}

        for row in rows:
            month_tag = row['month_tag']
            if month_tag not in month_tag_map:
                month_tag_map[month_tag] = []
            month_tag_map[month_tag].append(row)

        for month_tag in month_tag_map:
            month_tag_rows = month_tag_map[month_tag]
            filename = os.path.join(self.by_month_output_dir, '{}.json'.format(month_tag))
            self._write_json_file(month_tag_rows, filename)


    def _get_rows(self, input_file_path, input_filename):
        result = []
        rows = self.get_rows_from_csv(input_file_path)
        for row in rows:
            temp = OrderedDict()
            temp['TRANSACTION_ID'] = ''
            temp['begin_balance'] = self.begin_balance
            temp['amount'] = float(self._num_remove_comma(row['Amount']))
            temp['this_balance'] = float(self._num_remove_comma(row['Balance']))

            self._check_exception(temp['amount'], temp['this_balance'], row, input_filename)
            self.begin_balance = temp['this_balance']

            des_str = row['Description']
            temp['description'] = ' '.join(des_str[6:len(des_str) + 1].split())
            temp['date'] = self._make_date(des_str, input_filename)
            temp['month_tag'] = self._get_month_tag(temp['date'])
            temp['card_type'] = 'chase_debit'
            temp['tag'] = 'income' if temp['amount'] > 0.0 else 'expense'
            result.append(temp)
        return result 


    def _num_remove_comma(self, num_str):
        str_arr = num_str.split(',')
        return ''.join(str_arr)


    def _check_exception(self, amount, balance, row, input_filename):
        if abs(self.begin_balance + amount - balance) >= self.PRECISION:
            print self.begin_balance, row, input_filename
            raise Exception('Missing Record!')


    def _make_date(self, des_str, input_filename):
        month_and_day = des_str[0:5]
        year = input_filename[0:4]
        # statement at month 01, des_str begin of 12/...
        if input_filename[4:6] == '01' and month_and_day[0:2] == '12':
            year = str(int(year) - 1)
        return month_and_day + '/' + year


    def _get_month_tag(self, date_str):
        return get_month_tag(date_str)


if __name__ == '__main__':
    process_indy_trans('all_indy_csvs')