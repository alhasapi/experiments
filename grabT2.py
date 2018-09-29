
import json
from tweepy import Stream
from tweepy import OAuthHandler
from __future__ import print_function
from tweepy.streaming import StreamListener

access_token        = "833474190254698496-0yy50CdwitB8vWPe8G7BTU8t8jdie0W"
access_token_secret = "tEV13P7yyslqOx4XOEyfWdi70gnsGo3MgXItyeID5fPva"
consumer_key        = "kaPKNaydiko9PzKMxqBd0j8nU"
consumer_secret     = "DT4QK2T3abnDnC2lLholx5Dq2yTin36TdV9fNiInl8n2yakCfb"

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

