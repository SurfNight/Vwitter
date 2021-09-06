import os
from commands import Command
from register_commands import register_command
from Twitter import Twitter

@register_command
class Read(Command):
    def __init__(self):
        api_key = os.getenv('api_key')
        api_secret_key = os.getenv('api_secret_key')
        access_token = os.getenv('access_token')
        access_token_secret = os.getenv('access_token_secret')
        self.twitter = Twitter(api_key, api_secret_key, access_token, access_token_secret)

    triggers = ["ler", "leia", "lê", "le"]
    name = "Ler"
    description = "Comando que publica um tweet."
    
    def run(self, text_input: str):
        number = 5
        for word in text_input:
            if word.isdigit():
                number = int(word)
                break
        
        print(f"Lendo ultimos {number} tweets...")
        tweets = self.twitter.read_last_tweets(number)
        ret = ""
        for i in range(len(tweets)):
            ret += f"Tweet{i+1}: {tweets[i]}"
        return(ret)
