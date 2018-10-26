from flask import Blueprint, send_from_directory



assets = Blueprint('assets', __name__, url_prefix='/assets')


@assets.route('/<image_name>')
def get_image(image_name):
    return send_from_directory('static/emit', image_name)