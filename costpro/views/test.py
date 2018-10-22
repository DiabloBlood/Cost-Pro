from flask import Blueprint



test = Blueprint('test', __name__, url_prefix='/test')



@test.route('/')
def index():
    return "<h1>Testing</h1>"