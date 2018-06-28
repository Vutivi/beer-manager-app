# Python: Getting Started

A beer manager Django app, which can easily be deployed to Heroku.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/Vutivi/beer-manager-app.git
$ cd python-getting-started
$ psql databasename < dbdump.dmp
Change the database credentials to the local ones on settings.py
$ python manage.py migrate
$ python manage.py runserver
pp must be running on localhost:8000
```

Heroku app 

Link https://beer-manage.herokuapp.com

Username: vutiv
Password: mina888484