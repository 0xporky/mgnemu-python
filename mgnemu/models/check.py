# -*- coding: utf-8 -*-

"""
Model of check, needed when client pays for purchase.

"""

from mgnemu.models.base_model import BaseModel
from mgnemu.models.model_fabric import ModelFabric
from mgnemu.models.sales_types import SALES_RECIEPT
from mgnemu.models.sales_types import RETURN_RECIEPT
from mgnemu.models.sales_types import PAYMENT


class Check(BaseModel):

    def __init__(self, data):

        keys = list(data.keys())
        if SALES_RECIEPT in keys:
            BaseModel.__init__(self, SALES_RECIEPT)
        elif RETURN_RECIEPT in keys:
            BaseModel.__init__(self, RETURN_RECIEPT)
        else:
            raise KeyError('Unknown check key error')

        fabric = ModelFabric()
        self.__data = [fabric.get_model(val)
                       for val in data[self.model_type]
                       if fabric.get_model(val) is not None]

    def gen_check(self):
        dumps = self.dumps()
        sign = 1
        check_sum = 0
        keys = list(dumps.keys())

        if SALES_RECIEPT in keys:
            dump = dumps[SALES_RECIEPT]
        elif RETURN_RECIEPT in keys:
            dump = dumps[RETURN_RECIEPT]
            sign = -1
        else:
            return {}

        nums = [cr[PAYMENT]['no']
                for cr in dump
                if PAYMENT in list(cr.keys())]
        sums = [sign * cr[PAYMENT]['sum']
                for cr in dump
                if PAYMENT in list(cr.keys())]

        return dict(zip(nums, sums))

    @property
    def check_type(self):
        return self.model_type

    def dumps(self):
        return {
            'id': BaseModel.check_id(),
            self.model_type: [val.dumps() for val in self.__data]
        }
