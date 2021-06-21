from datetime import datetime
import os
import random
from sqlalchemy import Column, String, Integer, Float, Date, Boolean, DECIMAL
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
from pathlib import Path
from config import SECRET_KEY
from config import SQLALCHEMY_DATABASE_URI
from flask_wtf import FlaskForm
import base64

env_path = Path('setup.sh')
database_path = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    # db.create_all()
    migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'Company'
    company_id = db.Column(db.BigInteger, primary_key=True)
    company_logo = db.Column(db.String)
    company_name = db.Column(db.String(120))
    compensation = db.Column(db.DECIMAL(15))
    date_created = db.Column(db.Date)
    date_updated = db.Column(db.Date)
    last_applied = db.Column(db.Date)
    careers_page = db.Column(db.String)

    def details(self):
        return{
            'company_id': self.company_id,
            'company_logo': self.company_logo,
            'company_name': self.company_name,
            'compensation': self.compensation,
            'date_created': self.date_created,
            'date_updated': self.date_updated,
            'last_applied': self.last_applied,
            'careers_page': self.careers_page
        }

    def edit_details(self):
        return{
            'company_id': self.company_id,
            'company_logo': self.company_logo,
            'company_name': self.company_name,
            'compensation': self.compensation,
            'date_created': self.date_created,
            'date_updated': self.date_updated,
            'last_applied': self.last_applied,
            'careers_page': self.careers_page
        }


class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.BigInteger, primary_key=True)
    mobile = db.Column(db.BigInteger)
    password = db.Column(db.String)
    applied_data = db.Column(db.String)
