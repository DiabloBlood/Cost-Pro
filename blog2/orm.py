from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)



### 1. Lazy Connecting
"""
The Engine, when first returned by create_engine(), has not actually tried to connect to the database yet;
that happens only the first time it is asked to perform a task against the database.
"""
engine = create_engine('sqlite:///:memory:', echo=True)