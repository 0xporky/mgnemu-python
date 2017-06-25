# -*- coding: utf-8 -*-

"""
Base model of project.
Contains to basic methods:
    dumps(object_data) - writes object into json.
    loads(json_data) - converts json into model object.

"""


class BaseModel():

    def __init__(self, model_type):
        self.__type = model_type

    @property
    def model_type(self):
        return self.__type

    def dumps(self, object_data):
        pass
