# -*- coding: utf-8 -*-

from os import urandom
from flask import Flask
from flask import request
from flask_httpauth import HTTPDigestAuth
from mgnemu.controllers.check_tape import CheckTape

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(24).encode('hex')
auth = HTTPDigestAuth()


@auth.get_password
def get_pw(username):
# TODO: we need add clear auth
    return '1'


@auth.generate_nonce
def generate_nonce():
# TODO: we need add clear auth
    return urandom(8).encode('hex')


@auth.generate_opaque
def generate_opaque():
# TODO: we need add clear auth
    return urandom(8).encode('hex')

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
    ct = CheckTape()
    return ct.check_tape.decode('unicode-escape')


@app.route('/cgi/rep/pay', methods=['GET'])
@auth.login_required
def get_pay_sums():
    ct = CheckTape()
    return ct.payments


@app.route('/cgi/chk', methods=['POST'])
@auth.login_required
def add_check():
    result = request.get_json(force=True)
    ct = CheckTape()
    return ct.add_check(result).decode('unicode-escape')


@app.route('/cgi/proc/printreport', methods=['GET'])
@auth.login_required
def print_orders():
    if '10' in request.args.keys():
        ct = CheckTape()
        return ct.payments

    if '0' in request.args.keys():
        ct = CheckTape()
        ct.print_z_order()
        return ' { "Status" : "ok" }'
