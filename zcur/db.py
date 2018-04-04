import psycopg2

def connect():
    host = 'testdb.chp7pefph6ne.us-west-1.rds.amazonaws.com'
    database = "COST_BOOK"
    user = 'haosichao111'
    password = 'huang433'
    port = 5432
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    except Exception, e:
        print e
    print conn
    cur = conn.cursor()
    print cur
    sql = """
        SELECT * FROM weather
    """
    cur.execute(sql)
    print cur.fetchone()
    # print type(conn)

if __name__ == '__main__':
    connect()
