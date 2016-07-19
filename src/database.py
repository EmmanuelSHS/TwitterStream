#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient
from constants import HOST, PORT, DB, COLLECTION

class Mongo:
    def __init__(self):
        self.client = MongoClient(HOST, PORT)
        self.tweets = self.client[DB][COLLECTION]

    def bulkInsert(self, records):
        self.tweets.insert_many(records)
        
    def getCounts(self):
        # count both
        return self.tweets.count()
