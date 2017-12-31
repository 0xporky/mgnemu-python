# -*- coding: utf-8 -*-

from docopt import docopt
from sys import argv
from os import environ
from mgnemu import docstr


class ArgsParser(object):
    """Class for command line arguments parsing."""

    def __init__(self):
        if len(argv) == 0:
            self.uwsgi_env = False
        else:
            self.uwsgi_env = argv[0] == 'uwsgi'

        if not self.is_uwsgi():
            self.params = docopt(docstr.__doc__)

    def is_uwsgi(self):
        return self.uwsgi_env

    @property
    def host(self):
        if self.is_uwsgi():
            return environ['HOST']
        else:
            return self.params['--host']

    @property
    def port(self):
        if self.is_uwsgi():
            return int(environ['PORT'])
        else:
            return int(self.params['--port'])

    @property
    def debug(self):
        deb = False
        if self.is_uwsgi():
            deb = environ['DEBUG'].lower() == 'on'
        else:
            deb = self.params['--debug'].lower() == 'on'

        return deb

    @property
    def db_host(self):
        if self.is_uwsgi():
            return environ['DB_HOST']
        else:
            return self.params['--db-host']

    @property
    def db_port(self):
        if self.is_uwsgi():
            return int(environ['DB_PORT'])
        else:
            return int(self.params['--db-port'])

    @property
    def db_user(self):
        if self.is_uwsgi():
            return environ['DB_USER']
        else:
            return self.params['--db-user']

    @property
    def db_pass(self):
        if self.is_uwsgi():
            return environ['DB_PASS']
        else:
            return self.params['--db-pass']
