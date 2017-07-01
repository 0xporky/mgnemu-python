# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from mgnemu.controllers.check_tape import CheckTape

app = Flask(__name__)


@app.route('/cgi/chk', methods=['GET'])
def get_check_tape():
    ct = CheckTape()
    return ct.check_tape.decode('unicode-escape')


@app.route('/cgi/rep/pay', methods=['GET'])
def get_pay_sums():
    ct = CheckTape()
    return ct.payments


@app.route('/cgi/chk', methods=['POST'])
def add_check():
    result = request.get_json(force=True)
    ct = CheckTape()
    ct.add_check(result)
    return ' { "Status" : "ok" }'


@app.route('/cgi/proc/printreport', methods=['GET'])
def print_orders():
    if '10' in request.args.keys():
        ct = CheckTape()
        return ct.payments

    if '0' in request.args.keys():
        ct = CheckTape()
        ct.print_z_order()
        return ' { "Status" : "ok" }'
