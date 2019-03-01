import json
import os
from peewee import MySQLDatabase, Model


class DbConnection(object):
    __instance = None

    def __new__(cls):
        if DbConnection.__instance is None:
            DbConnection.__instance = object.__new__(cls)
            DbConnection.__instance.val = None

        return DbConnection.__instance

    def get_connection(self):
        return self.connection_helper()

    def connection_helper(self):
        if DbConnection.__instance.val is None:
            current_dir = os.path.dirname(__file__)
            config_file = "../config.json"
            file_path = os.path.join(current_dir, config_file)

            with open(file_path, 'r') as f:
                config = json.load(f)
                db_conf = config["database"]
                self.__init_mysql(db_conf)

        return self.__instance.val

    @staticmethod
    def __init_mysql(dbconf):
        db = MySQLDatabase(database=dbconf['name'],
                           host=dbconf['host'],
                           port=dbconf['port'],
                           user=dbconf['user'],
                           passwd=dbconf['password'])

        DbConnection.__instance.val = db
        return db


class BaseModel(Model):
    class Meta:
        db_connection = DbConnection()
        database = db_connection.get_connection()
