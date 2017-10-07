# from app import app
from flask import session
from pymongo import MongoClient
from bson.code import Code
from bson.son import SON


class DBUtils:

    def __init__(self):
        pass

    def get_db(self):
        client = MongoClient()

        return client["DbName"]

    def get_collection_obj(self,collection_name):
        db = self.get_db()
        return db[collection_name]

