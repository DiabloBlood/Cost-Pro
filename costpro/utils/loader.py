from costpro.utils.file_io import read_json_dict



def get_config():
    db_config = read_json_dict('costpro/configs/db_config.json')
    conf = {
        'SQLALCHEMY_DATABASE_URI': 'mssql+pyodbc://{username}:{password}@{pyodbc_str}'.format(**db_config),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }
    return conf