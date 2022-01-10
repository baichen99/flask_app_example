import os
from flask import Flask, g
from models.user import User
from databases import db
from serializers import ma
from resources.user import UserList
from resources.auth import UserLogin
from flask_restful import Api
import logging
from logging.config import dictConfig
from log_settings import LOGGING
from dotenv import load_dotenv, find_dotenv
from resources import jwt


def create_app(mode='devlopment'):
  load_dotenv()
  import settings  
  app = Flask(__name__)
  api = Api(app)
  app.config.from_object(settings)
  db.init_app(app)
  ma.init_app(app)
  jwt.init_app(app)
  dictConfig(LOGGING)
  logger = logging.getLogger('app')

  # register hook function for log
  # @app.before_request
  # def beforeRequest():
  #   pass

  # @app.after_request
  # def AfterRequest(res):
  #   return res

  @app.shell_context_processor
  def shell_context():
    return {'app': app, 'db': db}
    
  # add routes
  api.add_resource(UserList, '/user/<string:id>', endpoint='userList',methods=['PUT', 'DELETE'])
  api.add_resource(UserList, '/user', endpoint='createUser', methods=['POST', 'GET'])
  api.add_resource(UserLogin, '/login', endpoint='userLogin', methods=['POST'])
  return app



if __name__ == '__main__':
  app = create_app()
  app.run()