#!/usr/bin/env python
# coding=utf-8


TOKENPATH = "/home/mengqi/tokens/twitterapi.tk"

URLBASE = "https://stream.twitter.com/1.1/statuses/filter.json?"
# Conditions
SFLOC = "locations=-122.75,36.8,-121.75,37.8"
NYLOC = "locations=-74,40,-73,41"
NYSFLOC = "locations=-122.75,36.8,-121.75,37.8,-74,40,-73,41"

HW = "track=Hillary"

POKE = "track=Pokemon"
NYPOKE = POKE + "&" + NYLOC

STOCK = "track=$..."

# Collection Names
CNYSF = "nysf"
CHW = "hillarywikileaks"
CNYPOKE = "nypoke"

# output
HOST = "localhost"
PORT = 27017
DB = "twitter"
COLLECTION = CNYPOKE

URL = URLBASE + NYPOKE

SLEEPTIME = "4"

