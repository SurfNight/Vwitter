import os
from commands import Command
from register_commands import register_command
import Twitter


@register_command
class SendDM(Command):
    triggers = ["envie", "enviar" "mande", "mandar", "manda"]
    name = "Enviar"
    description = "Comando que envia uma direct message."

    def run(self, text_input: str):
        print(text_input)
        # TODO: melhorar o tratamento
        if "arroba" not in text_input:
            return "Diga o @ do usúario que deve receber a DM."
        msg, user  = text_input.split(" arroba ")
        if msg.endswith('para o'): msg = msg[:-6]
        ret = Twitter.my_twitter.post_dm(user, msg)
        return ret
