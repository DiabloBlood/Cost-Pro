from flask import Blueprint, render_template, send_from_directory



dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard.route('/')
def index():
    return render_template('dashboard.html')

@dashboard.route('/src/<path:filename>', methods=['GET'])
def get_client_src(filename):
    return send_from_directory('static/src', filename)
