import logging
from flask import make_response, jsonify

def makeErrorResponse(error, status_code):
  logger = logging.getLogger('app')
  message = jsonify({
    'error': str(error),
  })
  # log
  logger.error(str(error))
  return make_response(message, status_code)