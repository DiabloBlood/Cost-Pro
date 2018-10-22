from costpro import create_app, db
from costpro.model import TransHistory

import sqlalchemy as sa


def build_query():
    params = {
        'page': 1,
        'pageSize': 10,
        'sorted': [
            {'id': 'amount', 'desc': True}
        ],
        'filtered': [
            {'id': 'description', 'value': 'haha'}
        ]
    }

    table = TransHistory
    query_obj = db.Query(table)

    if params['sorted']:
        for sort in params['sorted']:
            col_clause = db.column(sort['id'])
            col_clause = col_clause.desc() if sort['desc'] else col_clause.asc()
            query_obj = query_obj.order_by(col_clause)

    if params['filtered']:
        for fil in params['filtered']:
            fil_clause = db.column(fil['id']).like(fil['value'])
            query_obj = query_obj.filter(fil_clause)

    print(query_obj)


def test():
    from costpro.api.sa_helper import GridHelper
    params = {
        'page': 1,
        'pageSize': 510,
        'sorted': [
            {'id': 'amount', 'desc': True}
        ],
        'filtered': [
            {'id': 'description', 'value': 'haha'}
        ]
    }

    grid_helper = GridHelper(params, TransHistory)
    print(grid_helper._build_query_result())
    # rows, total_pages, total_size = grid_helper.make_query_result()



if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        test()
