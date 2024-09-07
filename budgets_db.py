from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

class BudgetModel(db.Model):
    __tablename__ = 'budgets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    spent = db.Column(db.Integer, nullable=False)
    budget_left = db.Column(db.Integer, nullable=False)

    #def __repr__(self):
     #   return f"Budget(name = {name}, amount = {amount}, spent = {spent}, budget_left = {bugdet_left})"

class ExpensesModel(db.Model):
    __tablename__= 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    expense = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    spent = db.Column(db.Integer, nullable=False)
    budget_left = db.Column(db.Integer, nullable=False)

#with app.app_context():
 #   db.create_all()