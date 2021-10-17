import os
from commands import Command
from register_commands import register_command
import Twitter 

@register_command
class Publish(Command):
    triggers = ["twitch", "twitter",
                "publique", "publica", "public", "publi"]
    name = "Publicar"
    description = "Comando que publica um tweet."
    
    def run(self, tweet: str):
        print(tweet)
        Twitter.my_twitter.tweet(tweet)
        return("Tweetado com sucesso, pai.")