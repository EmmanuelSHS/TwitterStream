import oauth2 as oauth
import urllib2 as urllib
import httplib, socket
import sys
import time
import json

from constants import TOKENPATH, URL


class TwitterStream:
    # access info for Twitter APP
    _debug = 0

    signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

    http_method = "GET"


    http_handler  = urllib.HTTPHandler(debuglevel=_debug)
    https_handler = urllib.HTTPSHandler(debuglevel=_debug)

    def __loadtoken(self):
        f = open(TOKENPATH, 'r')
        return json.load(f)

    def __registtoken(self):
        token = self.__loadtoken()

        api_key = token["api_key"]
        api_secret = token["api_secret"]
        access_token_key = token["access_token_key"]
        access_token_secret = token["access_token_secret"]

        self.oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
        self.oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

    '''
    Construct, sign, and open a twitter request
    using the hard-coded credentials above.
    return a feed addinfourl indicating feed url
    '''
    def __twitterreqfeed(self, url, parameters):
        req = oauth.Request.from_consumer_and_token(self.oauth_consumer,
                                                   token=self.oauth_token,
                                                   http_method=self.http_method,
                                                   http_url=url, 
                                                   parameters=parameters)
        
        req.sign_request(self.signature_method_hmac_sha1, self.oauth_consumer, self.oauth_token)
        
        self.headers = req.to_header()
        
        if self.http_method == "POST":
            encoded_post_data = req.to_postdata()
        else:
            encoded_post_data = None
            url = req.to_url()
        
        opener = urllib.OpenerDirector()
        opener.add_handler(self.http_handler)
        opener.add_handler(self.https_handler)
        
        response = opener.open(url, encoded_post_data)
        
        yield response.geturl()

    def genTweets(self):
        """return tweet generator, gen json tweets"""
        self.__registtoken()

        url = URL
        parameters = []
        addrfeed = self.__twitterreqfeed(url, parameters)

        while True:
            try:
                http = next(addrfeed)
                if http:
                    try:
                        for line in urllib.urlopen(http):
                            try:
                                yield json.loads(line)
                            except ValueError as e:
                                print e
                                print "no output sleep 8 mins"
                                time.sleep(8 * 60)
                    except (httplib.IncompleteRead, socket.error) as e:
                        print e
                        time.sleep(5 * 60)
            except StopIteration as e:
                print e
                time.sleep(60 * 60)
