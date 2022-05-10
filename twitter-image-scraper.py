# https://docs.tweepy.org/en/stable/getting_started.html
# # https://docs.tweepy.org/en/stable/api.html#get-tweet-timelines
# https://stackoverflow.com/questions/30359801/how-to-successfully-get-all-the-tweets-for-one-user-with-tweepy
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

# import tweepy
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# status = api.user_timeline(user=username, count=1)[0]
# json.dumps(status)
import json
import config
import tweepy
from json import JSONDecoder, JSONDecodeError
import re


auth = tweepy.OAuth1UserHandler(
   config.api_key, config.api_secret, config.access_token, config.token_secret
)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# status = api.user_timeline(user='USATODAY', count=1)[0]
# json.dumps(status)
list_of_tweets = []

# with open('data.json', 'w', encoding="utf-8")as f:

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.user_timeline,id='AmpTokenBot').items():
   # f.write(json.dumps(tweet._json))
   list_of_tweets.append(json.dumps(tweet._json))
   break


data = json.loads(list_of_tweets[0])
data = json.dumps((data['extended_entities'])['media'])


data = json.loads(data)
data = data[0]

print(data['media_url'])











    
    
