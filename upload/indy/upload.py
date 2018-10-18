from global_var import ALL_MERGED_FILENAME

import sys
sys.path.append('..')
sys.path.insert(0, '/var/www/zcur')
import utils.file_io
from costpro import create_app, db
from costpro.model import TransHistory



def upload():
    rows = utils.file_io.read_json_file(ALL_MERGED_FILENAME)
    try:
        ds = []
        for row in rows:
            record = TransHistory(**row)
            ds.append(record)

        db.session.bulk_save_objects(ds)
        db.session.commit()
    except:
        db.session.rollback()
        raise



if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        upload()
