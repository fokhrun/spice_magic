
from app import db


class Tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_seats = db.Column(db.Integer, nullable=False)
    num_tables = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Tables('{self.num_seats}', '{self.num_tables}')"

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    num_guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Reservation('{self.date}', '{self.time}', '{self.num_guests}')"
