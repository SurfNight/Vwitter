import twitter

class Twitter():
    def __init__(self, consumer_key, consumer_secret,
                       access_token_key, access_token_secret):
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token_key,
                               access_token_secret=access_token_secret)
        
    def read_last_tweets(self, number_of_tweets = 1):
        tweetsStatus = self.api.GetUserTimeline(count = number_of_tweets)
        return [tweet.text for tweet in tweetsStatus]
    
    def tweet(self, msg):
        status = self.api.PostUpdate(msg)
        return status
