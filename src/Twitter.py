import twitter
import os
from dotenv import load_dotenv

load_dotenv()
class Twitter():
    def __init__(self):
        api_key = os.getenv('api_key')
        api_secret_key = os.getenv('api_secret_key')
        self.consumer_key=api_key
        self.consumer_secret=api_secret_key

    def set_api(self,access_token_key, access_token_secret):
        self.api = twitter.Api(consumer_key=self.consumer_key,
                               consumer_secret=self.consumer_secret,
                               access_token_key=access_token_key,
                               access_token_secret=access_token_secret)

        
    def read_last_tweets(self, number_of_tweets = 3):
        tweetsStatus = self.api.GetHomeTimeline(count = number_of_tweets)
        return [f"{tweet.user.name} diz {tweet.text}" for tweet in tweetsStatus]

    def read_self_last_tweets(self, number_of_tweets = 3):
        tweetsStatus = self.api.GetUserTimeline(count = number_of_tweets)
        return [tweet.text for tweet in tweetsStatus]
    
    def tweet(self, msg):
        status = self.api.PostUpdate(msg)
        return status

my_twitter = Twitter()