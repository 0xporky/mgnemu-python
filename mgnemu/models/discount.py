# -*- coding: utf-8 -*-

"""
Model of discount, needed when client pays for purchase.

"""

from base_model import BaseModel


class Discount(BaseModel):

    def __init__(self, data):
        BaseModel.__init__(self, 'D')
        self.__sum = data['sum']
        if 'prc' in data.keys():
            self.__prc = data['prc']
        else:
            self.__prc = 0

    @property
    def sum(self):
        return self.__sum

    @property
    def prc(self):
        return self.__prc

    def dumps(self):
        return {
            self.model_type: {
                'sum': self.__sum,
                'prc': self.__prc
            }
        }
