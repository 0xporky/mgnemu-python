# -*- coding: utf-8 -*

from mgnemu.models.check import Check
from tempfile import gettempdir
from json import loads
from json import dumps
from os import path
from os import remove


class CheckTape():

    def __init__(self):
        pass

    def __get_check_file(self):
        tmp_dir = gettempdir()
        return '/'.join([tmp_dir, 'tape.txt'])

    def __read_check_tape(self):
        check_tape_file = self.__get_check_file()
        if path.exists(check_tape_file):
            f = open(check_tape_file, 'r')
            check_tape_json = f.read()
            f.close()
            return check_tape_json

        return '[]'

    def __write_check_tape(self, check_tape):
        check_tape_file = self.__get_check_file()
        f = open(check_tape_file, 'w+')
        f.write(dumps(check_tape))
        f.close()

    def __delete_chack_tape(self):
        check_tape_file = self.__get_check_file()
        if path.exists(check_tape_file):
            remove(check_tape_file)

    def add_check(self, json_data):
        check = Check(json_data)
        check_tape_json = self.__read_check_tape()
        if len(check_tape_json) == 0:
            check_tape = []
        else:
            check_tape = loads(check_tape_json)

        check_tape.append(check.dumps())
        self.__write_check_tape(check_tape)

    def print_z_order(self):
        self.__delete_chack_tape()

    @property
    def check_tape(self):
        check_tape_json = self.__read_check_tape()
        if len(check_tape_json) == 0:
            check_tape = []
            return dumps(check_tape)

        return check_tape_json
