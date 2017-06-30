# -*- coding: utf-8 -*-

"""
Testing payment operations with different checks.

"""

from mgnemu.models.payment_operations import PaymentOperations
from mgnemu.models.cash_operation import CashOperation
from mgnemu.models.check import Check
from unittest import TestCase
from json import loads


class Test(TestCase):

    def setUp(self):
        self.json_data_co = {
            'IO': [
                {
                    'IO': {
                        'sum': 30
                    }
                }
            ]
        }

        self.json_data = u'{ \
            "F": [ { \
                "S": { \
                    "code": 126196, \
                    "name": "126196 Жорсткий диск Toshiba", \
                    "qty": 1, \
                    "price": 2619.00, \
                    "tax": 1 \
            } \
        }, \
        { \
                "D": { \
                    "sum": -179.88, \
                    "tax": 1 \
            } \
        }, \
        { \
                "S": { \
                    "code": 134833, \
                    "name": "134833 Жорсткий диск Hitachi", \
                    "qty": 1.000, \
                    "price": 1749.00, \
                    "tax": 1 \
            } \
        }, \
        { \
            "D": { \
                "sum": -120.12, \
                "tax": 1 \
            } \
        }, \
        { \
            "P": { \
                "no": 4, \
                "name": "КАРТКОЮ", \
                "sum": 3968.00 \
            } \
        }, \
        { \
            "P": { \
                "no": 1, \
                "name": "ГОТIВКОЮ", \
                "sum": 100.00 \
            } \
        } \
    ] }'

    def test_loads_json(self):
        model = PaymentOperations()
        model_co = CashOperation(self.json_data_co)
        model_check = Check(loads(self.json_data))

        model.add_check(model_co)
        model.add_check(model_check)

        assert(model.sum1 == 130)
        assert(model.sum4 == 3968)
