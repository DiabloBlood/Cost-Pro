from flask import Blueprint, render_template, send_from_directory



index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
def get_index():
    return render_template('index.html')

@index.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory('static/assets', 'favicon.ico')