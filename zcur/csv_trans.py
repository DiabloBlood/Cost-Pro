from collections import OrderedDict
from util.file_io import write_json_file, read_json_file, get_rows_from_csv
from util.general import get_month_tag

from pprint import pprint
import traceback

'''
86 Victor Oladipo defensive SG
86 Al Horford shooting C
86 Alonzo Mourning rng C
87 Glen Rice power SG
87 Oscar Robertson power SF
87 Gordon Hayward balanced SF
'''

def process_chase_csv_trans(input_filename):
    """
    :type input_filename: string
    :param input_filename: relative file name of input file
    """
    chase_csv_trans = ChaseCSVTrans(input_filename)
    chase_csv_trans.process()


class ChaseCSVTrans(object):
    """
    Parse chase debit csv file to json file
    """
    OUTPUT_FILENAME = 'all_chase_debit_csv_init.json'
    INIT_BALANCE = 3096.78
    PRECISION = 0.000001


    def __init__(self, input_filename):
        """
        :type input_filename: string
        :param input_dir: filename of input file
        """
        self.input_filename = input_filename
        self.begin_balance = self.INIT_BALANCE


    def process(self):
        result = True
        try:
            rows = self._get_rows()
            self._write_json_file(rows, self.OUTPUT_FILENAME)
        except Exception, e:
            traceback.print_exc()
            result = False
        return result


    def _read_json_file(self, json_file_path):
        return read_json_file(json_file_path)


    def _get_rows_from_csv(self, csv_file_path):
        return get_rows_from_csv(csv_file_path)


    def _write_json_file(self, rows, output_file_path):
        write_json_file(rows, output_file_path)


    def _get_rows(self):
        result = []
        rows = self._get_rows_from_csv(self.input_filename)
        rows.reverse()
        for row in rows:
            temp = OrderedDict()
            temp['trans_id'] = ''
            temp['begin_balance'] = self.begin_balance
            temp['amount'] = float(row['Amount'])
            temp['this_balance'] = float(row['Balance'])

            self._check_exception(temp['amount'], temp['this_balance'], row, self.input_filename)
            self.begin_balance = temp['this_balance']

            temp['description'] = self._flat_str(row['Description'])
            temp['date'] = row['Posting Date']
            temp['month_tag'] = self._get_month_tag(temp['date'])
            temp['card_type'] = 'chase_debit'
            temp['year'] = int(temp['month_tag'][0:4])
            temp['month'] = int(temp['month_tag'][5:7])
            temp['tag'] = 'income' if temp['amount'] > 0.0 else 'expense'
            result.append(temp)

        result = self._add_trans_id(result)
        return result


    def _add_trans_id(self, rows):
        month_tag_map = {}

        for row in rows:
            month_tag = row['month_tag']
            if month_tag not in month_tag_map:
                month_tag_map[month_tag] = []
            month_tag_map[month_tag].append(row)

        for month_tag in month_tag_map:
            month_tag_rows = month_tag_map[month_tag]
            for i in range(len(month_tag_rows)):
                row = month_tag_rows[i]
                row['num'] = i + 1
                row['trans_id'] = '{}-{}-{}'.format(row['card_type'], row['month_tag'], i + 1)

        return rows



    def _flat_str(self, des_str):
        arr = des_str.split(' ')
        result = []
        for item in arr:
            if item:
                result.append(item)
        return ' '.join(result)


    def _get_month_tag(self, date_str):
        return get_month_tag(date_str)


    def _check_exception(self, amount, balance, row, input_filename):
        if abs(self.begin_balance + amount - balance) >= self.PRECISION:
            print self.begin_balance, row, input_filename
            raise Exception('Missing Record!')


if __name__ == '__main__':
    process_chase_csv_trans('csv.CSV')
