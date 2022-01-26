import unittest
from flask_testing import TestCase
from flask import url_for
from app import create_app
from databases import db
from manage import initdb, initUser
from resources.const import *

class SettingBase(TestCase):
  def create_app(self):
    return create_app()
  
  def setUp(self):
    db.drop_all()
    db.create_all()
    db.session.commit()
  
  def tearDown(self):
    pass

  def signup(self):
    response = self.client.post(
      url_for('user'),
      data={
        "username": "testuser",
        "password": "password",
        "email":    "test@test.com"
      }
    )
    return response

class checkAuth(SettingBase):

  def test_register(self):
    res = self.client.post(
      url_for('user'),
      data={
        "username": "baichen",
        "password": "password",
        "email":    "baichen@test.com"
      }
    )
    self.assertEqual(res.status_code, StatusCreated)
  
  def test_password(self):
    res = self.client.post(
      url_for('user'),
      data={
        "username": "baichen",
        "password": "123",
        "email":    "baichen@test.com"
      }
    )
    self.assertEqual(res.status_code, StatusBadRequests)

  def test_username(self):
    res = self.client.post(
      url_for('user'),
      data={
        "username": "bai",
        "password": "password",
        "email":    "baichen@test.com"
      }
    )
    self.assertEqual(res.status_code, StatusBadRequests)

  def test_duplicate_user(self):
    res1 = self.signup()
    res2 = self.signup()
    self.assertEqual(res2.status_code, StatusUnprocessableEntity)
  

if __name__ == '__main__':
  unittest.main()