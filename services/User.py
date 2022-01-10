from databases import db
from models.User import User

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
    
