from flask_restful import Resource, Api, reqparse, fields, marshal_with, request
from flask import Response
from models.user import User
from databases import db
from services.user import UserService
from serializers.user import UserSchema, UserCreateValidate
from resources.const import *
from utils.response import makeErrorResponse
from utils.password import generate_password_hash
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserList(Resource):
  # /user
  def get(self):
    user_schema = UserSchema()
    form = user_schema.dump(request.form)
    users = UserService.getUserList(form)
    if isinstance(users, Exception):
      return makeErrorResponse(users, status_code=StatusBadRequests)
    return user_schema.dump(users, many=True)

  # /user
  def post(self):
    user_schema = UserCreateValidate()
    errors = user_schema.validate(request.form)
    if errors:
      response = makeErrorResponse(errors, StatusBadRequests)
      return response
    else:
      user = user_schema.make_user(request.form)
      user.password = generate_password_hash(user.password)
      user_id = UserService.createUser(user)
      if isinstance(user_id, Exception):
        return makeErrorResponse(user_id, status_code=StatusBadRequests)
      return Response(status=StatusCreated)
  
  # /user/<id>
  @jwt_required()
  def delete(self, id):
    current_username = get_jwt_identity()
    user = UserService.getUserById(id)
    if user.username != current_username:
      return makeErrorResponse(Exception('Can not delete this user'), status_code=StatusUnauthorized)
    error = UserService.deleteUser(id)
    if error:
      return makeErrorResponse(error, status_code=StatusBadRequests)
    return Response(status=StatusNoContent)
  
  # /user/<id>
  def put(self, id):
    current_username = get_jwt_identity()
    user = UserService.getUserById(id)
    if user.username != current_username:
      return makeErrorResponse(Exception('Can not modify this user'), status_code=StatusUnauthorized)

    errors = UserCreateValidate().validate(request.form, partial=('username', 'email', 'password'))
    if errors:
      response = makeErrorResponse(errors, StatusBadRequests)
      return response
    error = UserService.updateUser(id, request.form)
    if error:
      return makeErrorResponse(error, status_code=StatusBadRequests)
    return Response(status=StatusNoContent)