# -*- coding: utf-8 -*

from json import loads
from json import dumps
from mgnemu.models.check import Check
from mgnemu.models.cash_operation import CashOperation
from mgnemu.models.payment_operations import PaymentOperations
from mgnemu.models.base_model import BaseModel
from mgnemu.controllers.db_controller import DbController


class CheckTape(object):

    def __init__(self, ap:'Argument parser'):
        self.ap = ap

    def __read_check_tape(self):
        with DbController(self.ap) as db:
            return dumps(db.check_tape())

    def __read_payment_operations(self):
        with DbController(self.ap) as db:
            return dumps(db.payment_operations())

    def __write_check_tape(self, check_tape):
        with DbController(self.ap) as db:
            db.write_check_tape(check_tape)

    def __write_payment_operations(self, p_operations):
        with DbController(self.ap) as db:
            db.write_payment_operations(p_operations)

    def __delete_chack_tape(self):
        with DbController(self.ap) as db:
            db.write_check_tape([])

    def __delete_payment_operations(self):
        with DbController(self.ap) as db:
            db.write_payment_operations([])

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

        return dumps(check.dumps())

    def print_z_order(self):
        self.__delete_chack_tape()
        self.__delete_payment_operations()
        BaseModel.reset_id()

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
