import twitter
from dotenv import load_dotenv

load_dotenv()


class Twitter():
    def set_api(self, consumer_key, consumer_secret, key, secret):
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=key,
                               access_token_secret=secret)

    def read_last_tweets(self, number_of_tweets=3):
        tweetsStatus = self.api.GetHomeTimeline(count=number_of_tweets)
        return [f"{tweet.user.name} diz {tweet.text}" for tweet in tweetsStatus]

    def read_self_last_tweets(self, number_of_tweets=3):
        tweetsStatus = self.api.GetUserTimeline(count=number_of_tweets)
        return [tweet.text for tweet in tweetsStatus]

    def tweet(self, msg):
        status = self.api.PostUpdate(msg)
        return status

    def post_dm(self, user, msg):
        try:
            user_id = self.api.GetUser(screen_name=user).id
        except twitter.TwitterError:
            return f"Usuário {user} não encontrado."
        try:
            self.api.PostDirectMessage(text=msg, user_id=user_id)
        except KeyError:
            return f"Não é possível enviar uma dm para o @{user}"
        return "DM enviada!"

    def get_profilePic_url(self):
        try:
            return self.api.VerifyCredentials().profile_image_url_https
        except:
            pass


my_twitter = Twitter()
