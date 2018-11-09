from flask import Blueprint, render_template, send_from_directory, abort



index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
def get_index():
    return render_template('index.html')


@index.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory('static/assets', 'favicon.ico')


@index.route('/<path:path>')
def catch_spa_urls(path):
    if path not in ('dashboard', 'table', 'category', 'test', 'test2'):
        abort(404)
    return render_template('index.html')