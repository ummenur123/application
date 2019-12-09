# Application
Application Restful API

## Prerequisites
This application is build with Python 3.7.2

## Installation
Create your virtual environement (same level as src folder) and activate it

For Linux users:

```
virtualenv virtualenv
source virtualenv/bin/activate
```

For Windows users:

```
C:\Python37\python -m virtualenv virtualenv
virtualenv\Scripts\activate
```

Go in src folder then

```
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```

## API access
For API access and details see the doc file in application/documents folder.
