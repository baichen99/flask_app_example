from flask import Flask
from models.User import User
from databases import db
from serializers import ma
from resources.User import UserList
from flask_restful import Api
import settings


def create_app():
  app = Flask(__name__)
  api = Api(app)
  app.config.from_object(settings)
  db.init_app(app)
  ma.init_app(app)

  @app.shell_context_processor
  def shell_context():
    return {'app': app, 'db': db}
    
  # add routes
  api.add_resource(UserList, '/user/<int:id>', endpoint='userlist',methods=['PUT', 'DELETE'])
  api.add_resource(UserList, '/user/', endpoint='createuser', methods=['POST', 'GET'])
  return app



if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)