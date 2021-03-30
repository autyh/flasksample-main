### Flask largeapp example

#### Structure

```
~/ExampleApp
    |-- manage.py
    |-- config.py
    |-- /app
        |-- __init__.py
        |-- /lib
        |-- /func        
        |-- /models
            |-- __init__.py
            |-- entry.py
            |-- user.py
        |-- /views
            |-- __init__.py
            |-- error.py
            |-- entry.py
            |-- user.py
        |-- /templates
            |-- layout.html
            |-- index.html
            |-- /sample
                |-- index.html
                |-- /oracle
                    |-- index.html
                    |-- create.html
                    |-- update.html
                    |-- delete.html
                |-- /mysql
                    |-- index.html
                    |-- create.html
                    |-- update.html
                    |-- delete.html
                |-- /mail
                    |-- index.html
            |-- /errors
                |-- 400.html
                |-- 404.html
                |-- 500.html
                |-- crsf.html
        |-- /validations
            |-- /sample
                |-- index.py
                |-- oracle.py
                |-- mysql.py
                |-- mail.py
        |-- /static
                |-- /css
                    |-- style.css
                |-- /js
    |-- /tests
        |-- __init__.py
        |-- /models
            |-- test_entry.py
        |-- /views
            |-- test_api.py

```

#### Install packages

```
$ pip install flask

```

#### Create Database (MySQL)

Edit config.py and use SQLALCHEMY_DATABASE_URI which starts with "sqlite:///"
```
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@host/databasename"  # Use this.
    ...
```

#### Create Database (Oracle)

Edit config.py and use SQLALCHEMY_DATABASE_URI which starts with "oracle+cx_oracle://"
```
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "oracle+cx_oracle://user:password@host:port/?service_name=SERVICE_NAME"  # Use this.
    ...
```

#### Run server

```
$ FLASK_ENV=development python manage.py runserver
```

or

```
$ FLASK_ENV=development FLASK_APP=manage flask run
```

#### Run tests

Set PYTHONPATH, at first.
```
$ export PYTHONPATH=`pwd`
```

Then,
```
$ nosetests -s
```

### Sample

##### mail send email via flask-mail and mail template
```
$ docker-compose build
```

##### oracle connect database  select insert update delete

```
$ docker-compose run web flask createdb
```

##### Create tables
```
$ docker-compose run web python manage.py db init
$ docker-compose run web python manage.py db migrate
$ docker-compose run web python manage.py db upgrade
```

##### Start web app
```
$ docker-compose up [-d]
```

##### Run tests

```
# Start database server
$ docker-compose up -d db
```

```
# Create database for test
$ docker-compose run -e FLASK_ENV=test web flask createdb
$ docker-compose run -e FLASK_ENV=test web python manage.py db upgrade
```

```
# Run test
$ docker-compose run -e FLASK_ENV=test web nosetests -s
```

##### Tips

```
# Connect postgresql database
$ docker exec -it flask-largeapp-sample_db_1 psql -U postgres flask_sampleapp_dev
```
