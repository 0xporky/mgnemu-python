# -*- conding: utf-8 -*-

"""
Testing check line model.

"""

from mgnemu.models.check_line import CheckLine
from unittest import TestCase


class TestDiscount(TestCase):

    def setUp(self):
        self.json_data = {
            "qty": 1,
            "price": 2,
            "name": "test",
            "code": "1",
            "tax": 1
        }

    def test_loads_json(self):
        model = CheckLine(self.json_data)

        assert(model.qty == 1)
        assert(model.price == 2)
        assert(model.name == 'test')
        assert(model.code == '1')
        assert(model.tax == 1)

        line_data = model.dumps()
        print(line_data.keys())
        data = line_data['S']

        assert(data['qty'] == 1)
        assert(data['price'] == 2)
        assert(data['name'] == 'test')
        assert(data['code'] == '1')
        assert(data['tax'] == 1)
