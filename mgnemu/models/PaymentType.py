# -*- coding: utf-8 -*-

"""
Model of payment types, needed when client pays for purchase.

"""

from . import BaseModel


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
        return super(PaymentType, self).dumps(self_dict)

    def loads(self, json_data):
        self_dict = super(PaymentType, self).loads(json_data)

        if 'card' in self_dict.keys():
            self.__card = self_dict['card']

        if 'no' in self_dict.keys():
            self.__no = self_dict['no']

        if 'sum' in self_dict.keys():
            self.__sum = self_dict['sum']

        if 'rrn' in self_dict.keys():
            self.__rrn = self_dict['rrn']
