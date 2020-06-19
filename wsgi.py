# wsgi.py
import os
import logging
#logging.warn(os.environ["DUMMY"])

from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from models import Product

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema

@app.route('/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)
