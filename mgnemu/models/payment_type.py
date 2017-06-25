# -*- coding: utf-8 -*-

"""
Model of payment types, needed when client pays for purchase.

"""

from base_model import BaseModel


class PaymentType(BaseModel):

    def __init__(self):
        self.__sum = 0
        self.__no = 0
        self.__rrn = ''
        self.__card = ''

    @property
    def sum(self):
        return self.__sum

    @property
    def no(self):
        return self.__no

    @property
    def rrn(self):
        return self.__rrn

    @property
    def card(self):
        return self.__card

    def dumps(self):
        self_dict = {
            'sum': self.__sum,
            'no': self.__no,
            'rrn': self.__rrn,
            'card': self.__card
        }
        return BaseModel.dumps(self, self_dict)

    def loads(self, json_data):
        self_dict = BaseModel.loads(self, json_data)

        self.loads_dict(self_dict)

    def loads_dict(self, dict_data):
        if 'card' in dict_data.keys():
            self.__card = dict_data['card']

        if 'no' in dict_data.keys():
            self.__no = dict_data['no']

        if 'sum' in dict_data.keys():
            self.__sum = dict_data['sum']

        if 'rrn' in dict_data.keys():
            self.__rrn = dict_data['rrn']
