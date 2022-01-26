from databases import db
import sqlalchemy
from models.user import User
from utils.password import check_password_hash
from werkzeug.exceptions import *

class UserService:  
  @staticmethod
  def getUserById(id):
    user = User.query.get(id)
    if not user:
      raise NotFound(
        description="Cannot find the user record"
      )
    return user
  
  @staticmethod
  def getUserList(data):
    try:
      user = User.query.filter_by(**data).all()
    except Exception as err:
      raise BadRequest(
        description="Query params for user is invalid"
      )
    return user
  
  @staticmethod
  def createUser(user):
    try:
      db.session.add(user)
      db.session.commit()
    # cannot catch pymysql.err.IntergrityError
    except sqlalchemy.exc.IntegrityError as e:
      raise Conflict(
        description="User record already exists",
      )
    return user.id
  
  @staticmethod
  def deleteUser(id):
    user = UserService.getUserById(id)
    db.session.delete(user)
    db.session.commit()    
    return
    
  @staticmethod
  def updateUser(id, data):
    User.query.filter_by(id=id).update(data)
    db.session.commit()
    return
  
  @staticmethod
  def checkPassword(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
      return True
    else:
      return False