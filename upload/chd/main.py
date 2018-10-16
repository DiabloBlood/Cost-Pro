from base import ChaseCSVTrans



def process_chase_csv_trans(input_filename):
    """
    :type input_filename: string
    :param input_filename: relative file name of input file
    """
    chase_csv_trans = ChaseCSVTrans(input_filename)
    chase_csv_trans.process()


if __name__ == '__main__':
    process_chase_csv_trans('files/chase_debit.csv')