from commands import Command
from main import register_command

@register_command
class Publish(Command):
    triggers = ["publi", "twitch", "twitter", "envi"]
    name = "Publicar"
    description = "Comando que publica um tweet."
    
    def run(self, tweet: str):
        #TODO: trocar pela chamada do comando do twitter
        print(tweet)
        return("Tweetado com sucesso, pai.")