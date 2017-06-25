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

        if 'prc' in self_dict.keys():
            self.__prc = self_dict['prc']

        if 'sum' in self_dict.keys():
            self.__sum = self_dict['sum']
