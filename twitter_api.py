from requests_oauthlib import OAuth1Session
import json
import settings

#settings.pyからTokenを取得
twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

#ツイート
params = {"status": "API Test!"}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
