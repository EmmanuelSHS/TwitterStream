#!/usr/bin/env python
# coding=utf-8

import sys
import time

sys.path.append("../../")

from src.twitterstream import TwitterStream
from src.constants import NYLOC

def main():
    print "System Test Start"

    req_time = 1800

    ts = TwitterStream()
    gen = ts.genTweets(NYLOC)
    
    start = time.time()
    c = 0
    pflag = True
    while True:
        if next(gen):
            c += 1
        dur = time.time() - start
        if 0 <= dur%60 <= 5:
            if pflag:
                print "running", dur/60, "minutes"
                pflag = False
        else:
            pflag = True

        if dur > req_time:
            break

    print "System Test End", c, "Tweets"
    print "RunTime", req_time

if __name__ == '__main__':
    main()
    
