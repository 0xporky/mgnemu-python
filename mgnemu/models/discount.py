# -*- coding: utf-8 -*-

"""
Model of discount, needed when client pays for purchase.

"""

from base_model import BaseModel


class Discount(BaseModel):

    def __init__(self):
        self.__sum = 0
        self.__prc = 0

    @property
    def sum(self):
        return self.__sum

    @property
    def prc(self):
        return self.__prc

    def dumps(self):
        self_dict = {
            'sum': self.__sum,
            'prc': self.__prc,
        }
        return BaseModel.dumps(self, self_dict)

    def loads(self, json_data):
        self_dict = BaseModel.loads(self, json_data)
        self.loads_dict(self_dict)

    def loads_dict(self, dict_data):
        if 'prc' in dict_data.keys():
            self.__sum = dict_data['sum']

        if 'sum' in dict_data.keys():
            self.__prc = dict_data['prc']
