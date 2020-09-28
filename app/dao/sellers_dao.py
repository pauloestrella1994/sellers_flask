from app.dao.base_dao import BaseDao
from app.model.sellers_model import Sellers

class SellersDao(BaseDao):

    def __init__(self):
        self.__table_name = 'sellers'
        super().__init__(Sellers)

    #read
    def read(self, id:str =''):
        return super().read(id)

    #create
    def create(self, model:Sellers) -> Sellers:
        return super().insert(model)

    #update
    def update(self, model:Sellers) -> Sellers:
        return super().update(model)

    #delete
    def delete(self, id:str) -> dict:
        return super().delete(id)