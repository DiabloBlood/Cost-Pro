from flask import request, Blueprint, jsonify
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

    data = io.orm_list_as_dict(result.items)

    return jsonify(total_size=result.total, data=data)