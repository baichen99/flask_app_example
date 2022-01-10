import os
from dotenv import load_dotenv

load_dotenv()

# mysql
MYSQL_CONFIG = {
    'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
    'PORT': os.environ.get('MYSQL_PORT', '3306'),
    'USER': os.environ.get('MYSQL_USER', ''),
    'PASSWORD': os.environ.get('MYSQL_PASSWORD', ''),
    'DEFAULT_SCHEMA': os.environ.get('MYSQL_DB', ''),
}
# mysql://username:password@host:port/databasename
SQLALCHEMY_DATABASE_URI = \
  f"mysql+pymysql://{MYSQL_CONFIG.get('USER')}:{MYSQL_CONFIG.get('PASSWORD')}@{MYSQL_CONFIG.get('HOST')}:{MYSQL_CONFIG.get('PORT')}/{MYSQL_CONFIG.get('DEFAULT_SCHEMA')}"
# suppress sqlalchemy warning
SQLALCHEMY_TRACK_MODIFICATIONS = False