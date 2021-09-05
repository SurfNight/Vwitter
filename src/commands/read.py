from commands import Command
from register_commands import register_command

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
        
        #TODO: Trocar pela chamada do twitter
        print(f"Lendo ultimos {number} tweets...")
        return("Tweet1: bla bla, Tweet2: bla bla bla")
