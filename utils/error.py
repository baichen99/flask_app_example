from flask import Blueprint, jsonify
from flask_restful import Api
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
import logging


class Error(Exception):
  """Base class for other exceptions"""
  def __init__(self, http_status_code:int, *args, **kwargs):
    # If the key `msg` is provided, provide the msg string
    # to Exception class in order to display
    # the msg while raising the exception
    self.http_status_code = http_status_code
    self.kwargs = kwargs
    msg = kwargs.get('msg', kwargs.get('message'))
    if msg:
      args = (msg,)
      super().__init__(args)
    self.args = list(args)
    for key in kwargs.keys():
      setattr(self, key, kwargs[key])

# class ConflictError(HTTPException):
#   """Should be raised when creating a record already exists"""
#   # https://stackoverflow.com/questions/3825990/http-response-code-for-post-when-resource-already-exists
#   code = 409,
#   description = " Validation error occurs"



# https://stackoverflow.com/questions/41149409/flask-restful-custom-error-handling
class ExtendedAPI(Api):
  """This class overrides 'handle_error' method of 'Api' class ,
  to extend global exception handing functionality of 'flask-restful'.
  """

  def handle_error(self, err):
    """It helps preventing writing unnecessary
    try/except block though out the application
    """
    # log every exception raised in the application
    print(err)
    # Handle HTTPExceptions
    if isinstance(err, HTTPException):
      err_description = getattr(
        err, 'description', HTTP_STATUS_CODES.get(err.code, '')
      )
      return jsonify({
        'message': err_description
      }), err.code

    # If msg attribute is not set,
    # consider it as Python core exception and
    # hide sensitive error info from end user
    message = err.kwargs.get('msg', err.kwargs.get('message'))
    code = getattr(err, 'http_status_code', None) or err.kwargs.get('code')
    if not message or not code:
      return jsonify({
        'message': 'Server has encountered some error'
      }), 500
    # Handle application specific custom exceptions
    else:
        return jsonify({
        'message': message,
      }), code
    return jsonify(**err.kwargs), err.http_status_code


