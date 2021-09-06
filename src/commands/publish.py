import os
from commands import Command
from register_commands import register_command
from Twitter import Twitter

@register_command
class Publish(Command):
    def __init__(self):
        api_key = os.getenv('api_key')
        api_secret_key = os.getenv('api_secret_key')
        access_token = os.getenv('access_token')
        access_token_secret = os.getenv('access_token_secret')
        self.twitter = Twitter(api_key, api_secret_key, access_token, access_token_secret)

    triggers = ["publi", "twitch", "twitter",
                "envie", "publique", "publica", "public"]
    name = "Publicar"
    description = "Comando que publica um tweet."
    
    def run(self, tweet: str):
        print(tweet)
        self.twitter.tweet(tweet)
        return("Tweetado com sucesso, pai.")