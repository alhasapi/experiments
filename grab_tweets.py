from twitter import *
from pprint import pprint as p

t = Twitter(auth=OAuth())
                       
result = t.geo.search(query="Cameroon", granularity="country")
for i in range(len(result['result']['places'])):
    place_id = result['result']['places'][i]['id']
    result = t.search.tweets(q="place:%s" % place_id)
    for tweet in result['statuses']: 
        print tweet['text'] + " | " + tweet['place']['name'] if tweet['place'] else "Undefined place"

