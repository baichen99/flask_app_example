from flask import make_response, jsonify

def setError(error, status_code, prefix=''):
  response = jsonify({
    'error': str(error),
  })
  # log
  
  return response, status_code