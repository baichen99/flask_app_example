from marshmallow import (
  Schema, 
  fields, 
  validate, 
  post_load, 
)
from models.user import User

# for serializing and deserializing
class UserSchema(Schema):
  id = fields.String()
  username = fields.String()
  password = fields.String(load_only=True)  # write only, can not read
  email = fields.Email()

  #post_load is for deserializing
  @post_load
  def make_user(self, data, **kwargs):
    return User(**data)

# for create and validating
class UserCreateValidate(Schema):
  username = fields.String(
    required=True,
    validate=validate.Length(min=4, max=20, error='Length must be between 4 and 20'),
    )
  email = fields.String(
    required=True,
    validate=validate.Email(error='Not a valid email address')
    )
  password = fields.String(
    required=True,
    validate=validate.Length(min=8, max=20, error='Length must be between 8 and 20'),
    )
  
  @post_load
  def make_user(self, data, **kwargs):
    return User(**data)
  

    
