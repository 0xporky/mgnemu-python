# -*- coding: utf-8 -*-

from os import urandom
from flask import Flask
from flask import request
from flask_httpauth import HTTPDigestAuth
from mgnemu.controllers.check_tape import CheckTape

app = Flask(__name__)
app.config['SECRET_KEY'] = str(urandom(24))
auth = HTTPDigestAuth()


@auth.get_password
def get_pw(username):
    # TODO: we need add clear auth
    return '1'


@auth.generate_nonce
def generate_nonce():
    # TODO: we need add clear auth
    return str(urandom(8))


@auth.generate_opaque
def generate_opaque():
    # TODO: we need add clear auth
    return str(urandom(8))


@auth.verify_nonce
def verify_nonce(nonce):
    # TODO: we need add clear auth
    return True


@auth.verify_opaque
def verify_opaque(opaque):
    # TODO: we need add clear auth
    return True


@app.route('/cgi/status', methods=['GET'])
def get_status():
    return ' { "Status" : "ok" }'


@app.route('/cgi/chk', methods=['GET'])
@auth.login_required
def get_check_tape():
    ct = CheckTape(app.config['ap'])
    return ct.check_tape


@app.route('/cgi/rep/pay', methods=['GET'])
@auth.login_required
def get_pay_sums():
    ct = CheckTape(app.config['ap'])
    return ct.payments


@app.route('/cgi/chk', methods=['POST'])
@auth.login_required
def add_check():
    result = request.get_json(force=True)
    ct = CheckTape(app.config['ap'])
    return ct.add_check(result)


@app.route('/cgi/proc/printreport', methods=['GET'])
@auth.login_required
def print_orders():
    ct = CheckTape(app.config['ap'])
    keys = list(request.args.keys())

    if '10' in keys:
        return ct.payments

    if '0' in keys:
        ct.print_z_order()
        return ' { "Status" : "ok" }'
