import json
import oauth2 as oauth

consumer_key =  "TRcqjgdkuaglGxJgY1miN0rtP"
consumer_secret = "J4CU0QuYbtIz5N6yAw9x6oV5xvJvR9nr3OhpFdk0ezQK48xhXi"

access_token = "324385851-ICKUvX0eEdcXZm5XiE6QgPUbfADqHdFuX8p2A2Bd"
access_secret = "cO8N2Z0sTgdxR8LfB5G4Sr2ZAvK6rLF2CVzxKDufr7cbK"

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=access_token, secret=access_secret)
client = oauth.Client(consumer, access_token)

test_url = "https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent"

response, data = client.request(test_url)

tweets = json.loads(data)
for tweet in tweets:
    print(data)