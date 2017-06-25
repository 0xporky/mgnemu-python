# -*- coding: utf-8 -*-

"""
Testing check line model.

"""

from mgnemu.models.check import Check
from unittest import TestCase
import json


class TestCheck(TestCase):

    def setUp(self):
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
        model = Check(json.loads(self.json_data))

        assert(model.check_type == 'F')

        check_data = model.dumps()
        assert('F' in check_data.keys())
