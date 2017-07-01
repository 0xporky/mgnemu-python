#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Usage: mgnemu [--host=<host> --port=<port> --debug=<debu>]

Options:
    -h --help           Show help information.
    --host=<host>       IP-adress where cash machine will be emulating [default: 127.0.0.1].
    --port=<port>       Port of cash machone emulator [default: 80].
    --debug=<debug>     Debug mode [default: Off].

"""

from docopt import docopt
from mgnemu.app import app

if __name__ == '__main__':
    arguments = docopt(__doc__)
    debug_flag = True if arguments['--debug'].lower() == 'on' else False

    app.run(host=arguments['--host'],
            port=int(arguments['--port']),
            debug=debug_flag)
