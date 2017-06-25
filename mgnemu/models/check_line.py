# -*- coding: utf-8 -*-

"""
Model of check line, needed when client pays for purchase.

"""

from base_model import BaseModel


class CheckLine(BaseModel):

    def __init__(self):
        self.__qty = 0
        self.__price = 0
        self.__name = ''
        self.__code = ''
        self.__tax = 0

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
        self_dict = {
            'qty': self.__qty,
            'price': self.__price,
            'name': self.__name,
            'code': self.__code,
            'tax': self.__tax
        }
        return BaseModel.dumps(self, self_dict)

    def loads(self, json_data):
        self_dict = BaseModel.loads(self, json_data)

        self.loads_dict(self_dict)

    def loads_dict(self, dict_data):
        if 'qty' in dict_data.keys():
            self.__qty = dict_data['qty']

        if 'price' in dict_data.keys():
            self.__price = dict_data['price']

        if 'name' in dict_data.keys():
            self.__name = dict_data['name']

        if 'code' in dict_data.keys():
            self.__code = dict_data['code']

        if 'tax' in dict_data.keys():
            self.__tax = dict_data['tax']
