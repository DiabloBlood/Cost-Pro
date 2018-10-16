import os
from base import IndyTrans



"""
All the directory or path variable names in this piece of code refer to relative paths.
If a directory var name refer to an absolute paths, the var name will contains "abs" to specify.
"""

def process_indy_trans(input_dir):
    """
    :type input_dir: string
    :param input_dir: relative path name of input folder
    """
    assert isinstance(input_dir, str), 'The input folder name must be a string!'
    assert os.path.isdir(input_dir), 'The input folder must be a directory!'
    indy_trans = IndyTrans(input_dir)
    if indy_trans.process():
        print('Process all indy csv files successfully!')
    else:
        raise Exception('Process indy csv files failed!')

    return True


if __name__ == '__main__':
    process_indy_trans('files/all_indy_csvs')