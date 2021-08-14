from commands.command import Command

class Publish(Command):
    def __init__(self):
        super().__init__("Publicar", "Comando que publica um tweet.",
                         ["publi", "twitch", "twitter", "envi"])
    
    def run(self):
        return