# -*- coding: utf-8 -*-

"""
Model of check comment, needed for zero checks.

"""

from mgnemu.models.base_model import BaseModel
from mgnemu.models.sales_types import COMMENT_TYPE
from mgnemu.models.sales_types import COMMENT


class CheckComment(BaseModel):

    def __init__(self, data):
        BaseModel.__init__(self, COMMENT_TYPE)
        if COMMENT in list(data.keys()):
            self.__cm = data[COMMENT]
        else:
            self.__cm = ''

    @property
    def cm(self):
        return self.__cm

    def dumps(self):
        return {
            'id': BaseModel.check_id(),
            self.model_type: {
                COMMENT: self.__cm,
            }
        }
