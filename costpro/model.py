from flask_sqlalchemy import SQLAlchemy



# setup db object
db = SQLAlchemy()



class TransHistory(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    trans_id = db.Column(db.String(63), unique=True, nullable=False)
    amount = db.Column(db.Float(), nullable=False)
    begin_balance = db.Column(db.Float())
    this_balance = db.Column(db.Float())
    trans_type = db.Column(db.String(63), nullable=False)
    card_type = db.Column(db.String(63), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trans_date = db.Column(db.Date(), nullable=False)
    month_tag = db.Column(db.String(63), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    month = db.Column(db.Integer(), nullable=False)
    category_1 = db.Column(db.String(63))
    category_2 = db.Column(db.String(63))
    category_3 = db.Column(db.String(63))
    pattern = db.Column(db.String(255))

    def __repr__(self):
        return '<Trans {}, {}, {}, {}, {}>' \
            .format(self.id, self.trans_id, self.category_1, self.category_2, self.category_3)


class Category1(db.Model):
    __tablename__ = 'category_1'
    __table_args__ = (db.UniqueConstraint('name_1'),)
    id = db.Column(db.Integer(), primary_key=True)
    name_1 = db.Column(db.String(63), nullable=False)
    desc_1 = db.Column(db.String(255))
    children = db.relationship('Category2', backref='Category1', cascade="all, delete")


class Category2(db.Model):
    __tablename__ = 'category_2'
    __table_args__ = (db.UniqueConstraint('name_2'),)
    id = db.Column(db.Integer(), primary_key=True)
    parent_id = db.Column(db.Integer(), db.ForeignKey(Category1.id))
    name_2 = db.Column(db.String(63), nullable=False)
    desc_2 = db.Column(db.String(255))
    children = db.relationship('Category3', backref='Category2', cascade="all, delete")


class Category3(db.Model):
    __tablename__ = 'category_3'
    __table_args__ = (db.UniqueConstraint('name_3'),)
    id = db.Column(db.Integer(), primary_key=True)
    parent_id = db.Column(db.Integer(), db.ForeignKey(Category2.id))
    name_3 = db.Column(db.String(63), nullable=False)
    desc_3 = db.Column(db.String(255))
