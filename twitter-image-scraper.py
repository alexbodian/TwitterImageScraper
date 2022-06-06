import json
import config
import tweepy
from json import JSONDecoder, JSONDecodeError
import re
import requests # to get image from the web
import shutil # to save it locally

count = 1
profileCount = 0
auth = tweepy.OAuth1UserHandler(
   config.api_key, config.api_secret, config.access_token, config.token_secret
)

users_to_scrape = []
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


for user in users_to_scrape:
   # status = api.user_timeline(user='USATODAY', count=1)[0]
   # json.dumps(status)
   # with open('data.json', 'w', encoding="utf-8")as f:
   list_of_tweets = []
   profileCount += 1

   api = tweepy.API(auth)
   # enter name of twitter account for id
   for tweet in tweepy.Cursor(api.user_timeline,id=user).items():
      list_of_tweets.append(json.dumps(tweet._json))
      # f.write(json.dumps(tweet._json))


   for tweet in list_of_tweets:

      data = json.loads(tweet)
      try:
         
         data = json.dumps((data['extended_entities'])['media'])
         data = json.loads(data)
         data = data[0]      
         image_url = data['media_url']
         filename = image_url.split("/")[-1]
         
            # Open a local file with wb ( write binary ) permission.
         r = requests.get(image_url, stream = True)
         with open("./images/{}".format(filename),'wb') as f:
            shutil.copyfileobj(r.raw, f)
         print("Image " + str(count) + " scraped [Profile " + str(profileCount) + " of " + str(len(users_to_scrape)) + "]")
         count+=1 

      except:
         pass
            
      try:
         
         data = data['quoted_status']['entities']['media']
         data = (data)[0]


         # data = json.loads(data)
         image_url = data['media_url']
         filename = image_url.split("/")[-1]
         
         
            # Open a local file with wb ( write binary ) permission.
         r = requests.get(image_url, stream = True)
         with open("./images/{}".format(filename),'wb') as f:
            shutil.copyfileobj(r.raw, f)
         print("Image " + str(count) + " scraped [Profile " + str(profileCount) + " of " + str(len(users_to_scrape)) + "]")
         count+=1 

      except:
         pass

      try:
         
         data = data['entities']['media']
         data = (data)[0]


         # data = json.loads(data)
         image_url = data['media_url']
         filename = image_url.split("/")[-1]
         
         
            # Open a local file with wb ( write binary ) permission.
         r = requests.get(image_url, stream = True)
         with open("./images/{}".format(filename),'wb') as f:
            shutil.copyfileobj(r.raw, f)
         print("Image " + str(count) + " scraped [Profile " + str(profileCount) + " of " + str(len(users_to_scrape)) + "]")
         count+=1 

      except:
         pass




      












    
    
