from listener import Listener
from reproducer import reproduce
from manager import Manager
from commands import *
from typing import Type
from speech_recognition import UnknownValueError

listener = Listener()
manager = Manager()
activator = "jarbas"

def register_command(klass: Type[Command]) -> None:
    """
    This decorator registers a class on `manager` global object
    """
    manager.add(klass)

def run():
    response = ""

    while True:
        try:
            response = listener.listen().lower()
        except UnknownValueError:
            print("Deu erro")
            continue
        if activator in response:
            break
    print(response)
    response.replace(activator, '', 1)

    try:
        command, text = manager.find_matching_command_and_text(response)
        command_audio_response = command().run(text)
        reproduce(command_audio_response)
    except LookupError:
        reproduce("Não entendi o comando, pilantra.")
    return
        
def get_twitter_creds():
    # TODO: Ask for Twitter API Credentials
    return
    

if __name__ == "__main__":
    get_twitter_creds()
    while True:
        run()
