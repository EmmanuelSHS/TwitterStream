#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient

class Mongo:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.tweets = self.client.twitter.nysf

    def bulkInsert(self, records):
        self.tweets.insert_many(records)
        
    def getCounts(self):
        # count both
        return self.tweets.count()
