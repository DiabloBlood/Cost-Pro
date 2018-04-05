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
        pprint(e)

    return result

def create_table(table_name):
    sql = create_table_template.format(table_name=table_name)
    result = exec_sql(sql)
    return result

if __name__ == '__main__':
    create_table('test2')
