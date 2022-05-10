# https://docs.tweepy.org/en/stable/getting_started.html
# # https://docs.tweepy.org/en/stable/api.html#get-tweet-timelines
# https://stackoverflow.com/questions/30359801/how-to-successfully-get-all-the-tweets-for-one-user-with-tweepy

# import tweepy
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# status = api.user_timeline(user=username, count=1)[0]
# json.dumps(status)
import json
import config
import tweepy


auth = tweepy.OAuth1UserHandler(
   config.api_key, config.api_secret, config.access_token, config.token_secret
)

# api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# status = api.user_timeline(user='USATODAY', count=1)[0]
# json.dumps(status)

with open('data.json', 'w') as f:
   
   api = tweepy.API(auth)
   for tweet in tweepy.Cursor(api.user_timeline,id='AmpTokenBot').items():
      json.dump(tweet._json, f) 

# list_of_tweets = []
# api = tweepy.API(auth)
# for tweet in tweepy.Cursor(api.user_timeline,id='ta_cco_').items():
#       list_of_tweets.append(tweet._json)
      

# print(list_of_tweets)