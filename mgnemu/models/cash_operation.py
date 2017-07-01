# -*- coding: utf-8 -*-

"""
Model of cash operation.
Needed when client want to put or get cash from machine.

"""

from base_model import BaseModel


class CashOperation(BaseModel):

    def __init__(self, data):

        if 'IO' in data.keys():
            BaseModel.__init__(self, 'IO')
        else:
            raise KeyError(u'Unknown check key error')

        self.__data = data['IO']

    def dumps(self):
        return {
            'id': BaseModel.check_id(),
            self.model_type: self.__data
        }
