from app.dao.sellers_dao import SellersDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.sellers_model import Sellers

class SellersController(Resource):

    def __init__(self):
        self.__dao = SellersDao()

    def get(self, id=None):
        if id:
            return jsonify(self.__dao.read(id).to_dict())
        return jsonify([seller.to_dict() for seller in self.__dao.read()])

    def post(self):
        data = request.get_json()
        sellers = Sellers(**data)
        model = self.__dao.create(sellers)
        return jsonify(model.to_dict())

    def put(self, id):
        data = request.get_json()
        sellers = Sellers(**data)
        sellers.id = id
        model = self.__dao.update(sellers)
        return jsonify(model.to_dict())

    def delete(self, id):
        message = self.__dao.delete(id)
        return jsonify(message)