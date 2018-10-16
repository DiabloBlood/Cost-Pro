import os
from util.file_io import read_json_file, get_all_filenames



def get_month_conclusions(input_dirname):
    all_filenames = get_all_filenames(input_dirname)

    all_income = 0
    all_expense = 0

    for filename in all_filenames:
        month_tag = filename[0:7]
        rows = read_json_file(os.path.join(input_dirname, filename))

        income = 0
        expense = 0

        for row in rows:
            amount = row['amount']
            if row['tag'] == 'income':
                income += amount
            else:
                expense += amount

        all_income += income
        all_expense += expense

        print '{}: {}'.format(month_tag, expense)

    print 'ALL_INCOME: {}'.format(all_income)
    print 'ALL_EXPENSE: {}'.format(all_expense)


if __name__ == '__main__':
    get_month_conclusions('all_indy_by_month_jsons')

