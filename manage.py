from app import create_app
from flask.cli import with_appcontext, FlaskGroup
from databases import db
from models.user import User
import faker
import click
from utils.password import generate_password_hash

# https://flask.palletsprojects.com/en/2.0.x/cli/#custom-commands
# https://stackoverflow.com/questions/50298565/flask-factory-pattern-and-flask-cli-commands/51923415
cli = FlaskGroup(create_app=create_app)

@cli.command("initdb")
@with_appcontext
def initdb():
  db.drop_all()
  db.create_all()
  db.session.commit()
  click.echo('databases initialized')

@cli.command("init-user")
@with_appcontext
def initUser():
  fake = faker.Faker()
  for i in range(5):
    name = fake.name()
    password = generate_password_hash(name)
    user = User(username=name, password=password, email=f"{name.replace(' ', '')}@test.com")
    db.session.add(user)
  db.session.commit()

@cli.command()
def test():
  import unittest
  import sys

  tests = unittest.TestLoader().discover("tests")
  result = unittest.TextTestRunner(verbosity=2).run(tests)
  if result.errors or result.failures:
    sys.exit(1)

if __name__ == '__main__':
  cli()