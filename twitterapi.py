import json
import oauth2 as oauth
from secret import keys 

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_secret = keys["access_secret"]

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_token, secret=access_secret)
client = oauth.Client(consumer, access_token)

test_url = "https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent"

response, data = client.request(test_url)

tweets = json.loads(data)
for tweet in tweets:
    print(data)