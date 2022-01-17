from databases import db
from models.user import User
from utils.password import check_password_hash

class UserService:  
  @staticmethod
  def getUserById(id):
    try:
      user = User.query.get(id)
    except Exception as err:
      return err
    return user
  
  @staticmethod
  def getUserList(data):
    try:
      user = User.query.filter_by(**data).all()
    except Exception as err:
      return err
    return user
  
  @staticmethod
  def createUser(user):
    try:
      db.session.add(user)
      db.session.commit()
    except Exception as err:
      return err
    return user.id
  
  @staticmethod
  def deleteUser(id):
    user = UserService.getUserById(id)
    if user is None:
      return
    elif isinstance(user, Exception):
      return user
    db.session.delete(user)
    db.session.commit()
    return
    
  @staticmethod
  def updateUser(id, data):
    try:
      User.query.filter_by(id=id).update(data)
      db.session.commit()
    except Exception as err:
      return err
    return
  
  @staticmethod
  def checkPassword(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
      return True
    else:
      return False