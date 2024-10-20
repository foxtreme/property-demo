from app import db


class RealStateProperty(db.Model):
    __tablename__ = 'properties'
    real_state_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    country = db.Column(db.String(40), nullable=False)
