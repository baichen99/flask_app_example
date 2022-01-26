from flask_restful import Resource, Api, reqparse, fields, marshal_with, request
from flask import Response
from models.user import User
from services.user import UserService
from serializers.user import UserSchema, UserCreateValidate
from resources.const import *
from utils.password import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import *

class UserList(Resource):
  # /user
  def get(self):
    user_schema = UserSchema()
    form = user_schema.dump(request.form)
    users = UserService.getUserList(form)
    return user_schema.dump(users, many=True)

  # /user
  def post(self):
    user_schema = UserCreateValidate()
    errors = user_schema.validate(request.form)
    if errors:
      raise BadRequest(
        description=str(errors)
      )
    else:
      user = user_schema.make_user(request.form)
      user.password = generate_password_hash(user.password)
      user_id = UserService.createUser(user)
      return Response(StatusCreated)
  
  # /user/<id>
  @jwt_required()
  def delete(self, id):
    current_username = get_jwt_identity()
    user = UserService.getUserById(id)
    if user.username != current_username:
      raise Unauthorized(
        description='Do not have permission to delete this user'
      )
    user_id = UserService.deleteUser(id)
    return Response(status=StatusNoContent)
  
  # /user/<id>
  @jwt_required()
  def put(self, id):
    current_username = get_jwt_identity()
    user = UserService.getUserById(id)
    if user.username != current_username:
      raise Unauthorized(
        description='Do not have permission to modify this user'
      )
    errors = UserCreateValidate().validate(request.form, partial=('username', 'email', 'password'))
    if errors:
      raise BadRequest(
        description=errors
      )
    UserService.updateUser(id, request.form)
    return Response(status=StatusNoContent)