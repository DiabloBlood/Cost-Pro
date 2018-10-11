from app import db



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
    year = db.Column(db.Integer(), nullable=False)
    category_1 = db.Column(db.String(63), nullable=False)
    category_2 = db.Column(db.String(63), nullable=False)
    category_3 = db.Column(db.String(63), nullable=False)
    pattern = db.Column(db.String(255))

    def __repr__(self):
        return '<Trans {}, {}, {}, {}>' \
            .format(self.id, self.category_1, self.category_2, self.category_3)

