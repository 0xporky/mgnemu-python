# -*- conding: utf-8 -*-

"""
Testing cash operation.

"""

from mgnemu.models.cash_operation import CashOperation
from unittest import TestCase


class TestCheckComment(TestCase):

    def setUp(self):
        self.json_data = {
            'IO': {
                'IO': {
                    'sum': 30
                }
            }
        }

    def test_loads_json(self):
        model = CashOperation(self.json_data)

        data_line = model.dumps()
        dataIO = data_line['IO']
        data = dataIO['IO']

        assert(data['sum'] == 30)
