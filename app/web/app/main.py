from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from peewee import MySQLDatabase, Model, PrimaryKeyField, DateTimeField, CharField, DoubleField, IntegerField, TextField
from datetime import date, timedelta
import os,sys

mysql_db = MySQLDatabase("employees", host="db", user="root")

class MySQLModel(Model):
    class Meta:
        database = mysql_db

class Employees(MySQLModel):
    emp_no = PrimaryKeyField()
    birth_date = DateTimeField()
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    hire_date = DateTimeField()

    class Meta:
        db_table = "employees"



app = Flask(__name__)

@app.before_request
def _db_connect():
    mysql_db.connect()

@app.teardown_request
def _db_close(exc):
    if not mysql_db.is_closed():
        mysql_db.close()

@app.route('/')
def hello_world():
    ##mysql_db.connect()
    emp_entries = []
    sql='SELECT last_name,first_name ' \
	'FROM employees ' \
        'WHERE gender=\'M\' AND birth_date=\'1965-02-01\' AND hire_date>\'1990-01-01\' ' \
        'ORDER BY TRIM(last_name) ASC, TRIM(first_name) ASC;'
    print sql
    
    
    empl_dataset  = Employees.raw(sql)
    
    for el in empl_dataset:
	emp_entries.append(el.last_name + ' ' + el.first_name)

    return render_template("index.html",emp_entries=emp_entries)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')