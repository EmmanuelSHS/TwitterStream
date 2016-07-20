#!/usr/bin/env python
# coding=utf-8

import time

from src.database import Mongo
from src.twitterstream import TwitterStream
from src.constants import NYSFLOC
from src.utils import stopwatch


class Loader:
    def __init__(self):
        self.ts = TwitterStream()
        self.mg = Mongo()
        self.interval = 300
        self.dev = 10
        self.sflag = True

    def run(self, dur, criteria):
        print "generator starts"

        start = time.time()

        gen = self.ts.genTweets(criteria)
        recs = []
        c = 0
        while True:
            rec = next(gen)
            c += 1
            recs.append(rec)

            curr = time.time() - start
            if 0 <= curr%self.interval <= self.dev:
                if self.sflag:
                    self.flush(recs)
                    recs = []
                    self.sflag = False
                    print "running", curr/60, "minutes", "total", c, "saved"
            else:
                self.sflag = True

            # at given time (4 am EDT), sleep on hour
            if stopwatch():
                time.sleep(3600)

            if curr > dur:
                if recs:
                    self.flush(recs)
                break

        print "streaming completed"
        print dur, "seconds"
        print c, "tweets inserted"

    def flush(self, recs):
        try:
            self.mg.bulkInsert(recs)
        except TypeError:
            return


if __name__ == '__main__':
    dur = 60 * 60 * 12
    loader = Loader()
    loader.run(dur, NYSFLOC)
