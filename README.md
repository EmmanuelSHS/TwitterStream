# TwitterStream
Twitter Streaming API with Filter to Database

## TODO
1. increase yielding speed with removal of unnecessary codes -- currently have 2 tweets / second (1800 seconds, 3832 tweets)

## Features
1. Able to Fetch Twitter Stream Data with User-defined:

    1. Location
    
    2. Hashtag
    
    3. Keywords in Tweets
    
    4. Other criteria described in API doc

2. Yield json, store to MongoDB

## Dependency
1. oauth2

2. pymongo

## 0719
Catch several expections

Note that twitter streaming api will pause on 4 a.m. EST everyday

## 0714
1. test streaming capacity

## 0712
1. init the project

2. encapsulate functions into class

3. token safer access
