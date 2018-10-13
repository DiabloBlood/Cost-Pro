from flask import Blueprint, render_template, send_from_directory



test = Blueprint('test', __name__, url_prefix='/test')


@test.route('/')
def index():
    return "<h1>Hello to Test Page!</h1>"

'''
### test folder templates
@test.route('/test', methods=['GET'])
def test(filename):
    return render_template('test/test.html'.format(filename))

@test.route('/src/<path:filename>', methods=['GET'])
def get_client_src(filename):
    return send_from_directory('static/src', filename)

@test.route('/src_test/<path:filename>', methods=['GET'])
def get_client_src_test(filename):
    return send_from_directory('static/src_test', filename)
'''