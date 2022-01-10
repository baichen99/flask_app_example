from flask_restful import Resource, Api, reqparse, fields, marshal_with, request
from flask import Response
from models.User import User
from databases import db
from services.User import UserService
from serializers.User import UserSchema, UserCreateValidate
from resources.const import *
from utils.Response import setError

class UserList(Resource):
  # /user/<id>
  def get(self):
    user_schema = UserSchema()
    form = user_schema.dump(request.form)
    users = UserService.getUserList(form)
    if not isinstance(users, Exception):
      return user_schema.dump(users, many=True)
    return setError(users, status_code=StatusBadRequests)

  # /user
  def post(self):
    user_schema = UserCreateValidate()
    errors = user_schema.validate(request.form)
    if errors:
      response = setError(errors, StatusBadRequests)
      return response
    else:
      user = user_schema.make_user(request.form)
      user_id = UserService.createUser(user)
      return Response(status=StatusCreated)
  
  # /user/<id>
  def delete(self, id):
    pass