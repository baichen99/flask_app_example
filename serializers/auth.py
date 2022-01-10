from marshmallow import (
  Schema, 
  fields, 
)

class UserLoginSchema(Schema):
  username = fields.String()
  password = fields.String()

