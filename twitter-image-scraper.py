# https://docs.tweepy.org/en/stable/getting_started.html
# https://docs.tweepy.org/en/stable/api.html#get-tweet-timelines
import config
import tweepy

auth = tweepy.OAuth1UserHandler(
   config.api_key, config.api_secret, config.access_token, config.token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)