import os
from commands import Command
from register_commands import register_command
import Twitter

@register_command
class Read(Command):
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
        tweets = Twitter.my_twitter.read_last_tweets(number)
        ret = ""
        for i in range(len(tweets)):
            ret += f"Tweet{i+1}: {tweets[i]}"
        return(ret)
