import psycopg2
from configs.config import db_config
from configs.sql import create_table_template
import traceback
from pprint import pprint



def exec_sql(sql):
    result = True
    try:
        conn = psycopg2.connect(**db_config)
    except Exception, e:
        raise

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception, e:
        conn.rollback()
        result = False
        raise

    return result

def create_table(table_name):
    sql = create_table_template.format(table_name=table_name)
    result = exec_sql(sql)
    return result


def insert_data(table_name):
    row = {
        "trans_id": "chase_debit-2015-10-1",
        "amount": -44.41,
        "begin_balance": 3096.78,
        "this_balance": 3052.37,
        "tag": "expense",
        "card_type": "chase_debit",
        "description": "99 RANCH MARKET 1688 H SAN JOSE CA 100933 10/10",
        "date": "10/13/2015",
        "month_tag": "2015-10",
        "year": 2015,
        "month": 10,
        "num": 1,
        "master_cat": "shopping",
        "second_cat": "super_market",
        "children_cat": "99ranch",
        "pattern": "^99 RANCH\\b"
    }

    row['table_name'] = table_name

    sql_template = """
        INSERT INTO {table_name} (trans_id, amount, begin_balance, this_balance, tag, card_type, description,
            date, month_tag, year, month, num, master_cat, second_cat, children_cat, pattern)
        VALUES ('{trans_id}', {amount}, {begin_balance}, {this_balance}, '{tag}', '{card_type}', '{description}', '{date}',
            '{month_tag}', {year}, {month}, {num}, '{master_cat}', '{second_cat}', '{children_cat}', '{pattern}');
    """

    sql = sql_template.format(**row)

    result = exec_sql(sql)

    return result




if __name__ == '__main__':
    # create_table('test')
    print insert_data('test')
