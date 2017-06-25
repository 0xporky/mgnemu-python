# -*- coding: utf-8 -*-

"""
Model fabric is used to generate modles.

"""

from discount import Discount
from payment_type import PaymentType
from check_line import CheckLine


class ModelFabric():

    def __init__(self):
        pass

    def get_model(self, data):
        if 'D' in data.keys():
            return Discount(data['D'])
        elif 'S' in data.keys():
            return CheckLine(data['S'])
        elif 'P' in data.keys():
            return PaymentType(data['P'])
        else:
            raise KeyError(u'Unknown model key')
