# -*- conding: utf-8 -*-

"""
Testing check comment model.

"""

from mgnemu.models.check_comment import CheckComment
from unittest import TestCase


class TestCheckComment(TestCase):

    def setUp(self):
        self.json_data = {
            "cm": "Test comment"
        }

    def test_loads_json(self):
        model = CheckComment(self.json_data)

        assert(model.cm == self.json_data['cm'])

        data_line = model.dumps()
        data = data_line['C']

        assert(data['cm'] == self.json_data['cm'])
