from sqlalchemy.types import TypeDecorator, CHAR
import uuid
from sqlalchemy.dialects.postgresql import UUID
from databases import db
from datetime import datetime


class Base(db.Model):
  # Don't create this table
  __abstract__ = True
  
  def gen_id(self):
    return uuid.uuid4().hex

  # mysql doesn't support uuid
  id = db.Column(
    db.String(32),
    primary_key=True,
    default=gen_id
  )
  create_at = db.Column(
    db.DateTime, 
    default=datetime.now
  )
  
  delete_at = db.Column(
    db.DateTime,
  )

  update_at = db.Column(
    db.DateTime, 
    default=datetime.now
  )


