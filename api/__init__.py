from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.catalog.views import catalog 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
 
app.register_blueprint(catalog)
 
db.create_all()
