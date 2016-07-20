#!/usr/bin/env python
# coding=utf-8

from time import strftime, localtime
from constants import SLEEPTIME


def stopwatch():
    return strftime("%H", localtime()) == SLEEPTIME
