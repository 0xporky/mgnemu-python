# -*- conding: utf-8 -*-

"""
Testing payment type model.

"""

from mgnemu.models.payment_type import PaymentType
from unittest import TestCase
import json


class TestPaymentType(TestCase):

    def setUp(self):
        self.json_data = '{ "sum" : 1, "no" : 2, \
            "rrn" : "3", "card" : "4" }'
        self.dict_data = {
            "sum": 10,
            "no": 20,
            "rrn": "30",
            "card": "40"
        }

    def test_loads_json(self):
        model = PaymentType()
        model.loads(self.json_data)

        assert(model.sum == 1)
        assert(model.no == 2)
        assert(model.rrn == '3')
        assert(model.card == '4')

        js = model.dumps()
        data = json.loads(js)

        assert(data['sum'] == 1)
        assert(data['no'] == 2)
        assert(data['rrn'] == '3')
        assert(data['card'] == '4')
