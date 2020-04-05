from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Info(db.Model):
  hospital = db.Column(db.String(64), primary_key=True)
  time = db.Column(db.DateTime)
  total_num_beds = db.Column(db.Integer)
  used_num_beds = db.Column(db.Integer)
  total_num_vent = db.Column(db.Integer)
  used_num_vent = db.Column(db.Integer)
  num_adm = db.Column(db.Integer)
  used_dis = db.Column(db.Integer)

  def __repr__(self):
    return '<Hospital Info for {}>'.format(self.hospital)


class Hospital(db.Model):
  hospital_id = db.Column(db.Integer, primary_key=True)
  hospital_name = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  # reservations = db.relationship('Reservation', backref='reserver', lazy= 'dynamic')

  def __repr__(self):
      return '<Hospital {}>'.format(self.hospital_name)

  def set_password(self, password):
      self.password_hash = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
  return Hospital.query.get(int(id))
