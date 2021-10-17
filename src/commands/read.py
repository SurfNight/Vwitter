from commands import Command
from register_commands import register_command
import Twitter
from utils import words_to_numbers

@register_command
class Read(Command):
    triggers = ["ler", "leia", "lê", "le"]
    name = "Ler"
    description = "Comando que lê os últimos tweets."
    
    def run(self, text_input: str):
        text_input, number = words_to_numbers(text_input)
        
        print(f"Lendo ultimos {str(number)} tweets...")
        tweets = Twitter.my_twitter.read_last_tweets(number)
        ret = ', '.join(tweets)
        return(ret)
