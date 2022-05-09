# https://docs.tweepy.org/en/stable/getting_started.html
import config
import tweepy

auth = tweepy.OAuth1UserHandler(
   config.consumer_key, config.consumer_secret, config.access_token, config.token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)