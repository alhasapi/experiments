from twitter import *
from pprint import pprint as p

t = Twitter(auth=OAuth("833474190254698496-0yy50CdwitB8vWPe8G7BTU8t8jdie0W", 
                       "tEV13P7yyslqOx4XOEyfWdi70gnsGo3MgXItyeID5fPva",                 
                       "kaPKNaydiko9PzKMxqBd0j8nU", 
                       "DT4QK2T3abnDnC2lLholx5Dq2yTin36TdV9fNiInl8n2yakCfb"))
                       
result = t.geo.search(query="Cameroon", granularity="country")
for i in range(len(result['result']['places'])):
    place_id = result['result']['places'][i]['id']
    result = t.search.tweets(q="place:%s" % place_id)
    for tweet in result['statuses']: 
        print tweet['text'] + " | " + tweet['place']['name'] if tweet['place'] else "Undefined place"

