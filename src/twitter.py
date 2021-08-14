import twitter

class Twitter():
    def __init__(self, consumer_key, consumer_secret,
                       access_token_key, access_token_secret):
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token_key,
                               access_token_secret=access_token_secret)
        
    def read_last_tweets(self, number_of_tweets):
        return
    
    def tweet(self):
        return