


create_table_template = """
    DROP TABLE IF EXISTS {table_name};
    CREATE TABLE {table_name} (
        trans_id VARCHAR(64) PRIMARY KEY,
        amount REAL NOT NULL,
        begin_balance REAL NOT NULL,
        this_balance REAL NOT NULL,
        tag VARCHAR(32) NOT NULL,
        card_type VARCHAR(32) NOT NULL,
        description text NOT NULL,
        date DATE NOT NULL,
        month_tag VARCHAR(32) NOT NULL,
        year INT NOT NULL,
        month INT NOT NULL,
        num INT NOT NULL,
        master_cat VARCHAR(64),
        second_cat VARCHAR(64),
        children_cat VARCHAR(64),
        pattern text
    );
"""