# -*- coding: utf-8 -*-

"""
Model of check, needed when client pays for purchase.

"""

from base_model import BaseModel
from model_fabric import ModelFabric


class Check(BaseModel):

    def __init__(self, data):

        if 'F' in data.keys():
            BaseModel.__init__(self, 'F')
        elif 'R' in data.keys():
            BaseModel.__init__(self, 'R')
        else:
            raise KeyError(u'Unknown check key error')

        fabric = ModelFabric()
        self.__data = [fabric.get_model(val) for val in data[self.model_type]]

    @property
    def check_type(self):
        return self.model_type

    def dumps(self):
        return {
            'id': BaseModel.check_id(),
            self.model_type: [val.dumps() for val in self.__data]
        }
