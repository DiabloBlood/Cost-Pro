import os
from costpro.utils.file_io import read_json_dict



def get_config():
    relative_config_path = 'configs/db_config.json'
    if os.path.exists(relative_config_path):
        db_config_json_path = relative_config_path
    else:
        db_config_json_path = '{}/{}'.format(os.path.dirname(os.path.abspath('..')), relative_config_path)

    db_config = read_json_dict(db_config_json_path)
    conf = {
        'SQLALCHEMY_DATABASE_URI': 'mssql+pyodbc://{username}:{password}@{pyodbc_str}'.format(**db_config),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_ECHO': False
    }
    return conf