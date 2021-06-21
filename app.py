import math
import base64
import decimal
from datetime import date, datetime, timedelta
import string
import random
import uuid
from os import statvfs_result
from flask import Flask, render_template, request, Response, flash, redirect, url_for, make_response, send_file
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from logging import Formatter, FileHandler
from flask_wtf import FlaskForm
from sqlalchemy import func, desc, and_, asc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import aliased
from flask_migrate import Migrate
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import base
from werkzeug.exceptions import abort
from models import setup_db, db, User, Company

app = Flask(__name__)
setup_db(app)


@app.route('/')
def index():
    return render_template('admin/pages/company_list.html')


@app.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.details
    company_query = Company.query.all()
    company_mapper = list(map(Company.details, company_query))
    data = company_mapper
    return render_template('admin/pages/company_list.html', companies=data)


@app.route('/companies', methods=['POST'])
def delete_companies():
    data = request.form
    print(data)
    if(data.get('edit')):
        id = data.get('edit')
        return redirect(url_for('edit_company', company_id=id))
    elif (data.get('delete')):
        id = data.get('delete')
        Company.query.filter_by(company_id=id).delete()
        db.session.commit()
    else:
        id = data.get('apply')
        db.session.query(Company).filter_by(company_id=id).update(
            {"last_applied": datetime.now()})
        db.session.commit()

    return redirect(url_for('get_companies'))


@app.route('/companies/edit', methods=['GET'])
def edit_company():
    company_id = request.args.get('company_id')
    company = Company.query.filter_by(company_id=company_id).first()
    data = Company.edit_details(company)
    imgdata = base64.b64decode(data['company_logo'])
    filename = 'image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return render_template('admin/pages/edit_company.html', company=data, image=filename)


@app.route('/companies/edit', methods=['POST'])
def save_edited_details_company():
    data = request.form
    l = request.files['logo']
    f = l.read()
    base64_encoded_data = base64.b64encode(f)
    base64_message = base64_encoded_data.decode('utf-8')
    company_id = request.args.get('company_id')
    company = Company.query.filter_by(company_id=company_id).first()
    print("Company", company)
    try:
        if(data.get('name') != company.company_name):
            db.session.query(Company).filter_by(
                company_id=company_id).update({"company_name": data.get('name')})
        if(data.get('ctc') != company.compensation):
            db.session.query(Company).filter_by(
                company_id=company_id).update({"compensation": data.get('ctc')})
        if(data.get('careers_page') != company.careers_page):
            db.session.query(Company).filter_by(
                company_id=company_id).update({"careers_page": data.get('careers_page')})
        if(l):
            if(base64_message != company.company_logo):
                db.session.query(Company).filter_by(
                    company_id=company_id).update({"company_logo": base64_message})
        db.session.query(Company).filter_by(
            company_id=company_id).update({"date_updated": datetime.now()})
        db.session.commit()
        flash('company details were updated!.', 'alert-success')

    except SQLAlchemyError as e:
        print(e)
        flash('company details were not updated. Please try again.', 'alert-danger')

    return redirect(url_for('get_companies'))


@app.route('/companies/create', methods=['GET'])
def create_company():
    return render_template('admin/pages/create_company.html')


@app.route('/companies/create', methods=['POST'])
def submit_company():
    data = request.form

    try:
        if(request.files['logo']):
            f = request.files['logo'].read()
            base64_encoded_data = base64.b64encode(f)
        else:
            with open("static/admin/assets/images/catch_logo.png", "rb") as image_file:
                base64_encoded_data = base64.b64encode(image_file.read())
        base64_message = base64_encoded_data.decode('utf-8')
        id = (random.randint(10000000, 100000000))
        new_company = Company(
            company_id=id,
            company_name=data.get('name'),
            company_logo=base64_message,
            date_updated=datetime.now(),
            date_created=datetime.now(),
            compensation=data.get('ctc'),
            careers_page=data.get('careers_page')
        )
        db.session.add(new_company)
        db.session.commit()
        flash('company was successfully added!', 'alert-success')
    except SQLAlchemyError as e:
        print(e)
        flash('company was not added. Please try again.', 'alert-danger')
    return redirect(url_for('get_companies'))


# @app.route('/dummy-monthly-statement')
# def dummy_monthly_statement():
 #   return render_template('admin/pages/monthly_statement.html')


# Default port:
if __name__ == '__main__':
    app.run()
