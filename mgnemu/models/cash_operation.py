# -*- coding: utf-8 -*-

"""
Model of cash operation.
Needed when client want to put or get cash from machine.

"""

from mgnemu.models.base_model import BaseModel
from mgnemu.models.sales_types import CASH_RECIEPT


class CashOperation(BaseModel):

    def __init__(self, data):

        if CASH_RECIEPT in list(data.keys()):
            BaseModel.__init__(self, CASH_RECIEPT)
        else:
            raise KeyError('Unknown check key error.')

        self.__data = data[CASH_RECIEPT]

    def dumps(self):
        return {
            'id': BaseModel.check_id(),
            self.model_type: self.__data
        }

    def gen_check(self):
        dump = self.dumps()
        nums = [1 for cr in dump[CASH_RECIEPT]]
        sums = [cr[CASH_RECIEPT]['sum']
                for cr in dump[CASH_RECIEPT]]

        return dict(zip(nums, sums))
