# -*- coding: utf-8 -*

from tempfile import gettempdir
from json import loads
from json import dumps
from os import path
from os import remove
from mgnemu.models.check import Check
from mgnemu.models.cash_operation import CashOperation
from mgnemu.models.payment_operations import PaymentOperations


class CheckTape():

    def __init__(self):
        pass

    def __get_check_file(self):
        tmp_dir = gettempdir()
        return '/'.join([tmp_dir, 'tape.txt'])

    def __get_payment_file(self):
        tmp_dir = gettempdir()
        return '/'.join([tmp_dir, 'payment_operations.txt'])

    def __read_check_tape(self):
        check_tape_file = self.__get_check_file()
        if path.exists(check_tape_file):
            with open(check_tape_file, 'r') as f:
                check_tape_json = f.read()
                return check_tape_json

        return '[]'

    def __read_payment_operations(self):
        payment_file = self.__get_payment_file()
        if path.exists(payment_file):
            with open(payment_file, 'r') as f:
                payment_json = f.read()
                return payment_json

        return '[]'

    def __write_check_tape(self, check_tape):
        check_tape_file = self.__get_check_file()
        with open(check_tape_file, 'w+') as f:
            f.write(dumps(check_tape))

    def __write_payment_operations(self, p_operations):
        payment_file = self.__get_payment_file()
        with open(payment_file, 'w+') as f:
            f.write(dumps(p_operations))

    def __delete_chack_tape(self):
        check_tape_file = self.__get_check_file()
        if path.exists(check_tape_file):
            remove(check_tape_file)

    def __delete_payment_operations(self):
        p_file = self.__get_payment_file()
        if path.exists(p_file):
            remove(p_file)

    def add_check(self, json_data):

        p = PaymentOperations()
        p_ops = loads(self.__read_payment_operations())
        if len(p_ops):
            p.load_data(p_ops)

        if 'IO' in json_data.keys():
            check = CashOperation(json_data)
        else:
            check = Check(json_data)

        check_tape_json = self.__read_check_tape()
        if len(check_tape_json) == 0:
            check_tape = []
        else:
            check_tape = loads(check_tape_json)

        p.add_check(check)
        if p.sum1 < 0:
            raise ArithmeticError(u'Day check is lower than 0.')
        self.__write_payment_operations(p.dumps())

        check_tape.append(check.dumps())
        self.__write_check_tape(check_tape)

    def print_z_order(self):
        self.__delete_chack_tape()
        self.__delete_payment_operations()

    @property
    def check_tape(self):
        check_tape_json = self.__read_check_tape()
        if len(check_tape_json) == 0:
            check_tape = []
            return dumps(check_tape)

        return check_tape_json

    @property
    def payments(self):
        p_json = self.__read_payment_operations()
        p_ops = loads(p_json)
        p = PaymentOperations()

        if len(p_ops) == 0:
            return dumps(p.dumps())

        p.load_data(p_ops)
        return dumps(p.dumps())
