from databases import db


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(
    db.String(64),
    index=True,
    unique=True,
    nullable=False
  )
  password = db.Column(
    db.String(128),
    index=False,
    unique=False,
    nullable=False
  )
  email = db.Column(
    db.String(128),
    nullable=False,
  )
