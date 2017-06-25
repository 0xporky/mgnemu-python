# -*- coding: utf-8 -*-

"""
Model of check line, needed when client pays for purchase.

"""

from base_model import BaseModel


class CheckLine(BaseModel):

    def __init__(self, data):
        BaseModel.__init__(self, 'S')
        self.__qty = data['qty']
        self.__price = data['price']
        self.__name = data['name']
        self.__code = data['code']
        self.__tax = data['tax']

    @property
    def qty(self):
        return self.__qty

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def tax(self):
        return self.__tax

    def dumps(self):
        return {
            self.model_type: {
                'qty': self.__qty,
                'price': self.__price,
                'name': self.__name,
                'code': self.__code,
                'tax': self.__tax
            }
        }
