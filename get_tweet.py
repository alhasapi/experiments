

#Consumer Key (API Key)       kaPKNaydiko9PzKMxqBd0j8nU
#Consumer Secret (API Secret) DT4QK2T3abnDnC2lLholx5Dq2yTin36TdV9fNiInl8n2yakCfb

# Access Token        833474190254698496-0yy50CdwitB8vWPe8G7BTU8t8jdie0W
# Access Token Secret tEV13P7yyslqOx4XOEyfWdi70gnsGo3MgXItyeID5fPva

from twitter import *
k1, k2, k3, k4 = None, None, None, None

t = Twitter(auth=OAuth(k1, k2, k3, k4))

result   = t.geo.search(query="USA", granularity="country")
place_id = result['result']['places'][0]['id']

result = t.search.tweets(q="place:%s" % place_id)
for tweet in result['statuses']:
    print tweet['text'] + " | " + tweet['place']['name'] if tweet['place'] else "Undefined place"
