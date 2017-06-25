# -*- conding: utf-8 -*-

"""
Testing discount model.

"""

from mgnemu.models.discount import Discount
from unittest import TestCase


class TestDiscount(TestCase):

    def setUp(self):
        self.json_data = {
            "sum": 1,
            "prc": 2
        }

    def test_loads_json(self):
        model = Discount(self.json_data)

        assert(model.sum == 1)
        assert(model.prc == 2)

        data_line = model.dumps()
        data = data_line['D']

        assert(data['sum'] == 1)
        assert(data['prc'] == 2)
