# -*- coding: utf-8 -*-

"""
Model of table payment types.
This table collect all payments that passes through cash machine.

"""

from check import Check
from cash_operation import CashOperation


class PaymentOperations():

    def __init__(self):
        self.__sum1 = 0
        self.__sum2 = 0
        self.__sum3 = 0
        self.__sum4 = 0

    def load_data(self, data):
        for obj in data:
            if obj['no'] == 1:
                self.__sum1 = obj['sum']
            if obj['no'] == 2:
                self.__sum2 = obj['sum']
            if obj['no'] == 3:
                self.__sum3 = obj['sum']
            if obj['no'] == 4:
                self.__sum4 = obj['sum']

    def __add_sum(self, pay_num, sum):
        if pay_num == 1:
            self.__sum1 += sum
        if pay_num == 2:
            self.__sum2 += sum
        if pay_num == 3:
            self.__sum3 += sum
        if pay_num == 4:
            self.__sum4 += sum

    def dumps(self):
        return [
            {
                'no': 1,
                'sum': self.__sum1
            },
            {
                'no': 2,
                'sum': self.__sum2
            },
            {
                'no': 3,
                'sum': self.__sum3
            },
            {
                'no': 4,
                'sum': self.__sum4
            }
        ]

    def add_check(self, check):
        if isinstance(check, Check):
            dumps = check.dumps()
            sign = 1
            if 'F' in dumps.keys():
                dump = dumps['F']
            elif 'R' in dumps.keys():
                dump = dumps['R']
                sign = -1
            else:
                return
            nums = [ cr['P']['no'] for cr in dump if 'P' in cr.keys() ]
            sums = [ sign * cr['P']['sum'] for cr in dump if 'P' in cr.keys() ]
            map(self.__add_sum, nums, sums)
        if isinstance(check, CashOperation):
           dump = check.dumps()
           nums = [ 1 for cr in dump['IO'] ]
           sums = [ cr['IO']['sum'] for cr in dump['IO'] ]
           map(self.__add_sum, nums, sums)

    @property
    def sum1(self):
        return self.__sum1

    @property
    def sum2(self):
        return self.__sum2

    @property
    def sum3(self):
        return self.__sum3

    @property
    def sum4(self):
        return self.__sum4
