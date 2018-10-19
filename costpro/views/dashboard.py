from flask import Blueprint, render_template, send_from_directory



dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard.route('/')
def index():
    return render_template('dashboard.html')

### test folder templates
@dashboard.route('/test', methods=['GET'])
def test(filename):
    return render_template('test/test.html'.format(filename))

@dashboard.route('/src/<path:filename>', methods=['GET'])
def get_client_src(filename):
    return send_from_directory('static/src', filename)

@dashboard.route('/src_test/<path:filename>', methods=['GET'])
def get_client_src_test(filename):
    return send_from_directory('static/src_test', filename)
