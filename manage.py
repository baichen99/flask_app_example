from app import create_app
from flask.cli import with_appcontext, FlaskGroup
from databases import db
from models.User import User
import faker
import click

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
  users = []
  for i in range(5):
    user = User(username=fake.name(), password='password', email=f"{fake.name().replace(' ', '')}@mail.com")
    db.session.add(user)
  db.session.commit()
if __name__ == '__main__':
  cli()