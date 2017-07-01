# -*- coding: utf-8 -*-

"""
Model of check comment, needed for zero checks.

"""

from base_model import BaseModel


class CheckComment(BaseModel):

    def __init__(self, data):
        BaseModel.__init__(self, 'C')
        if 'cm' in data.keys():
            self.__cm = data['cm']
        else:
            self.__cm = ''

    @property
    def cm(self):
        return self.__cm

    def dumps(self):
        return {
            'id': BaseModel.check_id(),
            self.model_type: {
                'cm': self.__cm,
            }
        }
