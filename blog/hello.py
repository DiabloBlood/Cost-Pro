from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy

from global_loader.loader import get_config


# conf = get_config()

app = Flask(__name__)
# app.config['SQLALCHEMY_ECHO=True'] = True
# app.config.update(conf)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User (username='{}', email='{}')>".format(self.username, self.email)

# db.create_all()

'''
admin = User(username='admin_haha', email='admin@example.com')
guest = User(username='guest_haha', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()

print(User.query.all())
print(User.query.filter_by(username='admin').first())
'''

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


if __name__ == '__main__':
    app.run(host='10.0.2.15', port=8001, debug=True, use_reloader=True)