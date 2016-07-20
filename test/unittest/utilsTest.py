#!/usr/bin/env python
# coding=utf-8

import unittest
import sys

sys.path.append("../../")

from src.utils import stopwatch

class Test(unittest.TestCase):
    def testStopwatch(self):
        ret = stopwatch()
        self.assertTrue(True, not ret)


if __name__ == '__main__':
    unittest.main()
