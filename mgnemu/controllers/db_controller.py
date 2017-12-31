# -*- coding: utf-8 -*-

from pymongo import MongoClient


DATABASE_NAME = 'mgn'
DATABASE_ADMIN = 'admin'


class DbController(object):

    def __init__(self, ap: 'Argument parser'):
        self.ap = ap

    def __enter__(self):
        self.client = MongoClient(self.ap.db_host, self.ap.db_port)
        self.check_database()
        self.db_authenticate()
        return self

    def check_database(self):
        self.db = self.client[DATABASE_ADMIN]
        self.db_authenticate()
        if DATABASE_NAME in self.client.database_names():
            self.db = self.client[DATABASE_NAME]
            return

        self.db = self.client[DATABASE_NAME]
        self.db.add_user(self.ap.db_user,
                         self.ap.db_pass,
                         roles=[
                             {
                                 'role': 'readWrite',
                                 'db': DATABASE_NAME
                             },
                             {
                                 'role': 'root',
                                 'db': DATABASE_ADMIN
                             }
                         ])

    def db_authenticate(self):
        self.db.authenticate(self.ap.db_user,
                             self.ap.db_pass,
                             mechanism='SCRAM-SHA-1')

    def __exit__(self, exception_type, exception_value, traceback):
        self.client.close()

    def check_tape(self):
        return self.get_data('tape')

    def payment_operations(self):
        return self.get_data('payment_operations')

    def write_check_tape(self, data):
        self.set_data('tape', data)

    def write_payment_operations(self, data):
        self.set_data('payment_operations', data)

    def get_data(self, collection:'Collection name'):
        coll = self.db[collection]
        cursor = coll.find(projection=self.projection())
        return [dict(doc) for doc in cursor]

    def set_data(self, collection, data):
        coll = self.db[collection]
        coll.delete_many({})

        for doc in data:
            coll.insert(doc)

    def projection(self):
        return {
            '_id': False
        }
