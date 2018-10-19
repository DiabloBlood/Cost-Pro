import inspect
from costpro import model


from flask import request, Blueprint, jsonify, abort
from costpro import db, TransHistory
import costpro.utils.io as io



api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1/data', methods=['GET'])
def v1_data():
    page = request.args.get('page')
    page_size = request.args.get('page_size')

    page = io.convert_int(page)
    page_size = io.convert_int(page_size)

    result = db.session.query(TransHistory) \
        .order_by(TransHistory.id.asc()) \
        .paginate(page=page, per_page=page_size)

    total_pages = result.total / page_size

    rows = io.orm_list_as_dict(result.items)

    return jsonify(rows=rows, total_pages=total_pages, total_size=total_size)


@api.route('/v1/columns/<table_name>', methods=['GET'])
def v1_columns(table_name):
    columns = io.get_model_columns(table_name)
    if not columns:
        abort(404, '404 NOT FOUND!!!')

    return jsonify(columns=columns)