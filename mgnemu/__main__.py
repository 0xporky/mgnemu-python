#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app

if __name__ == '__main__':
    app.run(host='172.17.0.3', port=80, debug=True)
