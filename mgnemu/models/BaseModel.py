# -*- coding: utf-8 -*-

"""
Base model of project.
Contains to basic methods:
    dumps(object_data) - writes object into json.
    loads(json_data) - converts json into model object.

"""

import json


class BaseModel():

    def dumps(self, object_data):
        return json.dumps(object_data)

    def loads(self, json_data):
        return json.loads(json_data)
