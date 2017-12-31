# -*- coding: utf-8 -*-

"""
Model of payment types, needed when client pays for purchase.

"""

from mgnemu.models.base_model import BaseModel
from mgnemu.models.sales_types import PAYMENT


class PaymentType(BaseModel):

    def __init__(self, data):
        BaseModel.__init__(self, PAYMENT)
        self.__sum = data['sum']
        self.__no = data['no']

        if 'rrn' in data.keys():
            self.__rrn = data['rrn']
        else:
            self.__rrn = ''

        if 'card' in data.keys():
            self.__card = data['card']
        else:
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
        return {
            self.model_type: {
                'sum': self.__sum,
                'no': self.__no,
                'rrn': self.__rrn,
                'card': self.__card
            }
        }
