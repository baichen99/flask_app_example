from flask_restful import Resource, request
from utils.password import check_password_hash
from serializers.auth import UserLoginSchema
from services.user import UserService
from resources.const import *
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.exceptions import *

class UserLogin(Resource):

  def post(self):
    # validate password
    login_shcema = UserLoginSchema()
    form = login_shcema.dump(request.form)
    username = form.get('username', '')
    password = form.get('password', '')
    if username == '' or password == '':
      raise BadRequest(
        description='Infomation not complete'
    )
    if not UserService.checkPassword(username, password):
      raise BadRequest(
        description='Username and password do not match'
    )

    # return jwt token
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return {
      'access_token': access_token,
      'refresh_token': refresh_token
    }