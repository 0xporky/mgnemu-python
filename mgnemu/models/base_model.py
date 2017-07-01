# -*- coding: utf-8 -*-

"""
Base model of project.
Contains to basic methods:
    dumps(object_data) - writes object into json.
    loads(json_data) - converts json into model object.

"""


class BaseModel():

    __id = 0

    def __init__(self, model_type):
        self.__type = model_type
        if model_type in ['F', 'R', 'IO']:
            BaseModel.inc_id()

    @staticmethod
    def inc_id():
        BaseModel.__id += 1

    @staticmethod
    def reset_id():
        BaseModel.__id = 0

    @staticmethod
    def check_id():
        return BaseModel.__id

    @property
    def model_type(self):
        return self.__type

    def dumps(self, object_data):
        pass
