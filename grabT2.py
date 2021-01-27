
import json
from tweepy import Stream
from tweepy import OAuthHandler
from __future__ import print_function
from tweepy.streaming import StreamListener

access_token        = "-"
access_token_secret = ""
consumer_key        = ""
consumer_secret     = ""

TWEETS_LOCATION = "kamer_twts.txt"

# class EventHandler(StreamListener):
    # def on_data(self, data):
        # try:
            # with open(TWEETS_LOCATION, "a") as out:
                # out.write(data + "\n")
        # except: pass
        # return True

    # def on_error(self, status):
        # print(status)

setattr(StreamListener, 'on_data',
    lambda self, data: open(TWEETS_LOCATION, "a").write(data)
)
setattr(StreamListener, 'on_error',
    lambda self, data: print(data)
)

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    Stream(auth,
           EvenHandler()
    ).filter(
        track=[
        'Cameroon',
        'Cameroun',
        'cameroun',
        'cameroon',
        'kamer',
        'kmer',
        'mboa'
    ])

