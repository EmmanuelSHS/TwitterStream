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
        sf = [{"test": "hello"}]
        
        db.bulkInsert(ny, sf)
        nyc, sfc = db.getCounts()

        self.assertEqual(1, nyc)
        self.assertEqual(1, sfc)


if __name__ == '__main__':
    unittest.main()

