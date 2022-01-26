# flask file structure

## Usage

create `.env` file, edit the file as follows.

```
# .env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=123456
MYSQL_DB=rest
```

```shell
python manage.py initdb
python manage.py init-user
flask run
```

## test

```shell
python manage.py test
```

## RESTful

Use [flask_restful](https://flask-restful.readthedocs.io/en/latest/) framework to implement RESTful style api

## Serializer
This [essay](https://blog.igevin.info/posts/flask-rest-serialize-deserialize/) introduce how to use Marshmallow library to serialize and deserialize.

[marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) is an object serialization/deserialization library, you can use it to format your response ouput and to validate form fields in an easy way.

## Settings

Use `Flask.config.from_object` set config from an ojbect, and to better manage environment variables, I use [python-dotenv](https://github.com/theskumar/python-dotenv) to load env variables from `.env` file.

## Databases

[flask_sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x) is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

## JWT

[Flask-JWT-Extended’s Documentation](https://flask-jwt-extended.readthedocs.io/en/stable/)

[How to use jwt in flask](https://www.jianshu.com/p/c155c2b7af42)

[difference between refresh token and access token](https://stackoverflow.com/questions/27726066/jwt-refresh-token-flow)

## Unittest

[Unit testing framework](https://docs.python.org/zh-cn/3/library/unittest.html)
[flask test](https://dormousehole.readthedocs.io/en/latest/testing.html)
[【Flask 教學】實作 Flask 單元測試 Unit Test](https://www.maxlist.xyz/2020/08/17/flask-unittest/)

## Custom error handler

[flask-restful-custom-error-handling](https://stackoverflow.com/questions/41149409/flask-restful-custom-error-handling)

## Questions

1. [Access a Flask extension that is defined in the app factory](https://stackoverflow.com/questions/38443938/access-a-flask-extension-that-is-defined-in-the-app-factory)
2. [circular dependency problem](https://stackoverflow.com/questions/59156895/cannot-import-name-mydb-from-partially-initialized-module-connection-in-pyth)

## Inspiration

[jinlygenius/flask_structure_example](https://github.com/jinlygenius/flask_structure_example)
## todo

- i18n
- cors
- middlewares
