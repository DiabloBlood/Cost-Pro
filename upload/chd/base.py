from collections import OrderedDict

import sys
sys.path.append('..')
import utils.file_io, utils.general



class ChaseCSVTrans(object):
    """
    Parse chase debit csv file to json file
    """
    OUTPUT_FILENAME = 'files/all_chase_debit_csv_init.json'
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
        except:
            result = False
            raise
        return result


    def _read_json_file(self, json_file_path):
        return utils.file_io.read_json_file(json_file_path)


    def _get_rows_from_csv(self, csv_file_path):
        return utils.file_io.get_rows_from_csv(csv_file_path)


    def _write_json_file(self, rows, output_file_path):
        utils.file_io.write_json_file(rows, output_file_path)


    def _get_rows(self):
        result = []
        rows = self._get_rows_from_csv(self.input_filename)
        rows.reverse()
        for row in rows:
            temp = OrderedDict()
            temp['trans_id'] = ''
            temp['amount'] = float(row['Amount'])
            temp['begin_balance'] = self.begin_balance
            temp['this_balance'] = float(row['Balance'])
            temp['trans_type'] = 'income' if temp['amount'] > 0.0 else 'expense'
            temp['card_type'] = 'chase_debit'

            self._check_exception(temp['amount'], temp['this_balance'], row, self.input_filename)
            self.begin_balance = temp['this_balance']

            temp['description'] = self._flat_str(row['Description'])
            temp['trans_date'] = row['Posting Date']
            temp['month_tag'] = self._get_month_tag(temp['trans_date'])
            temp['year'] = int(temp['month_tag'][0:4])
            temp['month'] = int(temp['month_tag'][5:7])
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
        return utils.general.get_month_tag(date_str)


    def _check_exception(self, amount, balance, row, input_filename):
        if abs(self.begin_balance + amount - balance) >= self.PRECISION:
            print(self.begin_balance, row, input_filename)
            raise Exception('Missing Record!')
