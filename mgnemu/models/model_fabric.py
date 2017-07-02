# -*- coding: utf-8 -*-

"""
Model fabric is used to generate modles.

"""

from discount import Discount
from payment_type import PaymentType
from check_line import CheckLine
from check_comment import CheckComment


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
        elif 'C' in data.keys():
            return CheckComment(data['C'])
        else:
            return None
