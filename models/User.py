from databases import db
from models.base import Base
import uuid


class User(Base):
  __tablename__ = 'users'
  
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
