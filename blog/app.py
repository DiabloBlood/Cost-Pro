from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy

from utils.loader import get_config
from model.py import TransHistory


conf = get_config()

app = Flask(__name__)
app.config['SQLALCHEMY_ECHO=True'] = True
app.config.update(conf)

db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

### test folder templates
@app.route('/test/<path:filename>', methods=['GET'])
def test(filename):
    return render_template('/test/{}'.format(filename))

@app.route('/src/<path:filename>', methods=['GET'])
def get_client_src(filename):
    return send_from_directory('static/src', filename)

@app.route('/src_test/<path:filename>', methods=['GET'])
def get_client_src_test(filename):
    return send_from_directory('static/src_test', filename)


@app.route('/data', methods=['GET'])
def data():
    from utils.file_io import read_json_list
    pass


if __name__ == '__main__':
    app.run(host='10.0.2.15', port=8001, debug=True, use_reloader=True)