


create_table_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} (
        trans_id VARCHAR(64) PRIMARY KEY,
        card_type VARCHAR(32) NOT NULL,
        amount REAL NOT NULL,
        begin_balance REAL NOT NULL,
        this_balance REAL NOT NULL,
        date DATE NOT NULL,
        tag VARCHAR(32) NOT NULL,
        month_tag VARCHAR(32) NOT NULL,
        master_cat VARCHAR(64),
        second_cat VARCHAR(64),
        children_cat VARCHAR(64),
        description text NOT NULL,
        pattern text
    );
"""