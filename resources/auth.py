from flask_restful import Resource, request
from utils.password import check_password_hash
from serializers.auth import UserLoginSchema
from services.user import UserService
from utils.response import makeErrorResponse
from resources.const import *
from flask_jwt_extended import create_access_token, create_refresh_token

class UserLogin(Resource):

  def post(self):
    # validate password
    login_shcema = UserLoginSchema()
    form = login_shcema.dump(request.form)
    username = form.get('username', '')
    password = form.get('password', '')
    if username == '' or password == '':
      return makeErrorResponse(Exception('infomation not complete'), status_code=StatusBadRequests)
    if not UserService.checkPassword(username, password):
      return makeErrorResponse(Exception('username and password do not match'), status_code=StatusBadRequests)
    # return jwt token
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return {
      'access_token': access_token,
      'refresh_token': refresh_token
    }