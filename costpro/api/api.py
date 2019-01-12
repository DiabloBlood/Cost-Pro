import traceback
from flask import request, Blueprint, jsonify, abort
import costpro.api.sa_helper as sa_helper
from costpro.model import TransHistory, Category1



api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1/data/<table_name>', methods=['GET'])
def v1_data(table_name):
    value = request.args.get('value')
    try:
        grid_helper = sa_helper.GridHelper(value, table_name)
        rows, total_pages, total_size = grid_helper.process()
        return jsonify(rows=rows, total_pages=total_pages, total_size=total_size)
    except:
        traceback.print_exc()
        abort(404, '404 NOT FOUND!!!')


@api.route('/v1/data/<table_name>', methods=['POST'])
def v1_data_insert(table_name):
    # is_new = request.json.get('isNew')
    # record_id = request.json.get('id')
    editing_row = request.json.get('editingRow')
    editing_row.pop('id')
    isError, msg, row = sa_helper.SAHelper.insert_record(editing_row, table_name)
    return jsonify(isError=isError, msg=msg, row=row)



@api.route('/v1/columns/<table_name>', methods=['GET'])
def v1_columns(table_name):
    columns = sa_helper.get_model_columns(table_name)
    if not columns:
        abort(404, '404 NOT FOUND!!!')

    return jsonify(columns=columns)