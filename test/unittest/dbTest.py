#!/usr/bin/env python
# coding=utf-8


import sys
import unittest

sys.path.append("../../")

from src.database import Mongo


class dbTest(unittest.TestCase):
    def testInsertion(self):
        db = Mongo()

        ny = [{"test": "hello"}]
        
        db.bulkInsert(ny)
        nyc = db.getCounts()

        self.assertEqual(1, nyc)


if __name__ == '__main__':
    unittest.main()

