from flask import request, Blueprint, jsonify, abort
import costpro.api.sa_helper as sa_helper
from costpro.model import TransHistory, Category1



api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1/data', methods=['GET'])
def v1_data():
    # TODO get a query params dict, then separate
    # 1. base params, page, pageSize
    value = request.args.get('value')
    grid_helper = sa_helper.GridHelper(value, TransHistory)

    rows, total_pages, total_size = grid_helper.process()

    return jsonify(rows=rows, total_pages=total_pages, total_size=total_size)


@api.route('/v1/columns/<table_name>', methods=['GET'])
def v1_columns(table_name):
    columns = sa_helper.get_model_columns(table_name)
    if not columns:
        abort(404, '404 NOT FOUND!!!')

    return jsonify(columns=columns)


@api.route('/v1/category', methods=['GET'])
def v1_category():
    value = request.args.get('value')
    grid_helper = sa_helper.GridHelper(value, Category1)

    rows, total_pages, total_size = grid_helper.process()

    return jsonify(rows=rows, total_pages=total_pages, total_size=total_size)