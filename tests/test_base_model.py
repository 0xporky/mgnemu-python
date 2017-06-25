# -*- conding: utf-8 -*-

"""
Testing base model.

"""

from mgnemu.models import BaseModel
from unittest import TestCase


class TestBaseModel(TestCase):

    def setUp(self):
        self.json_data = '{ "a" : "1" }'

    def test_loads_json(self):
        model = BaseModel.BaseModel()
        data = model.loads(self.json_data)

        assert(data['a'] == '1')
