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
```
For Product list Access: http://localhost:8000/product/

For Product detail Access: http://localhost:8000/product/1

For Create Product Attribute: http://localhost:8000/product/1/attribute   #Example for adding first product attribute

For See Product Attribute List: http://localhost:8000/product/attribute-list

For Create Product Price: http://localhost:8000/product/1/price   #Example for adding first product price

For See Product Price List: http://localhost:8000/product/price-list
```

## TO SEE THE DIAGRAM
documents/Product ERD.pdf

## FOR ADMIN LOGIN
```
User Name: admin
Password: home1234
```
