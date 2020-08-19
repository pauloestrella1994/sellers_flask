from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from app.controller.sellers_controller import SellersController

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

@app.route('/')
def initial():
    return '<h1>Flask api</h1>'

api.add_resource(
    SellersController,
    '/api/sellers/', '/api/sellers/<int:id>',
    endpoint='sellers')

app.run(debug=True)




