# -*- conding: utf-8 -*-

"""
Testing payment type model.

"""

from mgnemu.models.payment_type import PaymentType
from unittest import TestCase


class TestPaymentType(TestCase):

    def setUp(self):
        self.json_data = {
            "sum": 1,
            "no": 2,
            "rrn": "3",
            "card": "4"
        }

    def test_loads_json(self):
        model = PaymentType(self.json_data)

        assert(model.sum == 1)
        assert(model.no == 2)
        assert(model.rrn == '3')
        assert(model.card == '4')

        data_line = model.dumps()
        data = data_line['P']

        assert(data['sum'] == 1)
        assert(data['no'] == 2)
        assert(data['rrn'] == '3')
        assert(data['card'] == '4')
