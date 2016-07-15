#!/usr/bin/env python
# coding=utf-8

import unittest
import sys

sys.path.append("../../")

from src.twitterstream import TwitterStream


class Test(unittest.TestCase):

    def testFetch(self):
        ts = TwitterStream()
        sf = "locations=-122.75,36.8,-121.75,37.8"

        gen = ts.genTweets(sf)
        c = 0
        while True:
            tweet = next(gen)
            print tweet
            c += 1
            break

        self.assertTrue(tweet)
        self.assertEqual(1, c)

if __name__ == '__main__':
    unittest.main()
