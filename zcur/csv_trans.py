from collections import OrderedDict
from util.file_io import get_rows_from_csv

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
    INIT_BALANCE = 3052.37
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

    def _get_rows(self):
        result = []
        raw_rows = get_rows_from_csv(self.input_filename).reverse()
        for row in raw_rows:
            temp = OrderedDict()
            temp['TRANSACTION_ID'] = ''
            temp['begin_balance'] = self.begin_balance
            temp['amount'] = float(row['Amount'])
            temp['this_balance'] = row['Balance']

            self._check_exception(temp['amount'], temp['this_balance'], row, self.input_filename)
            self.begin_balance = temp['this_balance']

            temp['description'] = ' '.join(row['Description'].split())
            temp['date'] = row['Posting Date']
            temp['card_type'] = 'Chase Debit'
            temp['tag'] = 'income' if temp['amount'] > 0.0 else 'expense'
            result.append(temp)
        return result

    def _check_exception(self, amount, balance, row, input_filename):
        if self.begin_balance + amount - balance >= self.PRECISION:
            print self.begin_balance, row, input_filename
            raise Exception('Missing Record!')


if __name__ == '__main__':
    process_chase_csv_trans('csv.CSV')
