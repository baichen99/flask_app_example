# flask file structure

## RESTful

Use [flask_restful](https://flask-restful.readthedocs.io/en/latest/) framework to implement RESTful style api

## Serializer
This [essay](https://blog.igevin.info/posts/flask-rest-serialize-deserialize/) introduce how to use Marshmallow library to serialize and deserialize.

[marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) is an object serialization/deserialization library, you can use it to format your response ouput and to validate form fields in an easy way.

## Settings

Use `Flask.config.from_object` set config from an ojbect, and to better manage environment variables, I use [python-dotenv](https://github.com/theskumar/python-dotenv) to load env variables from `.env` file.

## Databases

[flask_sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x) is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

## Questions

1. [Access a Flask extension that is defined in the app factory](https://stackoverflow.com/questions/38443938/access-a-flask-extension-that-is-defined-in-the-app-factory)
2. [circular dependency problem](https://stackoverflow.com/questions/59156895/cannot-import-name-mydb-from-partially-initialized-module-connection-in-pyth)

## todo
- logger
- i18n
- cors
- auth 
- middlewares