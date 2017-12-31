#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docopt import docopt
from mgnemu import docstr
from mgnemu.args_parser import ArgsParser
from mgnemu.routes import app


if __name__ == '__main__':
    __doc__ = docstr.__doc__
    ap = ArgsParser()
    app.config['ap'] = ap
    app.run(host=ap.host, port=ap.port, debug=ap.debug)
