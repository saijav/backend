from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class BudgetModel(db.Model):
    __tablename__ = 'budgets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    spent = db.Column(db.Integer, nullable=False)
    budget_left = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Budget(name = {name}, amount = {amount}, spent = {spent}, budget_left = {bugdet_left})"

api = Api(app)

#with app.app_context():
 #  db.create_all()

budget_put_args = reqparse.RequestParser()
budget_put_args.add_argument("id", type=int, help="The id of the budget is required", required=True, location='form')
budget_put_args.add_argument("name", type=str, help="The name of the budget is required", required=True, location='form')
budget_put_args.add_argument("amount", type=int, help="The amount of the budget is required", required=True, location='form')
budget_put_args.add_argument("spent", type=int, help="The amount spent of the budget is required", required=True, location='form')
budget_put_args.add_argument("budget_left", type=int, help="The amount left of the budget is required", required=True, location='form')

budget_update_args = reqparse.RequestParser()
budget_update_args.add_argument("id", type=int, location='form')
budget_update_args.add_argument("name", type=str, location='form')
budget_update_args.add_argument("amount", type=int, location='form')
budget_update_args.add_argument("spent", type=int, location='form')
budget_update_args.add_argument("budget_left", type=int, location='form')

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'amount': fields.Integer,
    'spent': fields.Integer,
    'budget_left': fields.Integer,
}

class Budget(Resource):
    @marshal_with(resource_fields)
    def get(self, budget_id):
        result = BudgetModel.query.filter_by(id=budget_id).first()
        if not result:
            abort(404, description="Could not found budget with that id")
        return result
    
    @marshal_with(resource_fields)
    def put(self, budget_id):
        args = budget_put_args.parse_args()
        result = BudgetModel.query.filter_by(id=budget_id).first()
        if result:
            abort(409, description="Budget id taken...")

        budget = BudgetModel(id=args['id'], name=args['name'], amount=args['amount'], spent=args['spent'], budget_left=args['budget_left'])
        db.session.add(budget)
        db.session.commit()
        return budget, 201
    
    def patch(self, budget_id):
        args = budget_update_args.parse_args()
        result = BudgetModel.query.filter_by(id=budget_id).first()
        if not result:
            abort(404, description="Could not found")

        if args['name']:
            result.name = args['name']
        if args['amount']:
            result.amount = args['amount']
        if args['spent']:
            result.spent = args['spent']
        if args['budget_left']:
            result.budget_left = args['budget_left']

        db.session.commit()

        return result


    @marshal_with
    def delete(self, budget_id):
        
        return '', 204

    
api.add_resource(Budget, "/budget/<int:budget_id>")

if __name__ == "__main__":
    app.run(port=8000, debug=True)