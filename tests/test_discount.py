# -*- conding: utf-8 -*-

"""
Testing discount model.

"""

from mgnemu.models.discount import Discount
from unittest import TestCase
import json


class TestDiscount(TestCase):

    def setUp(self):
        self.json_data = '{ "sum" : 1, "prc" : 2 }'

    def test_loads_json(self):
        model = Discount()
        model.loads(self.json_data)

        assert(model.sum == 1)
        assert(model.prc == 2)

        js = model.dumps()
        data = json.loads(js)

        assert(data['sum'] == 1)
        assert(data['prc'] == 2)
