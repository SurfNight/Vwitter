from listener import Listener
from reproducer import reproduce
from unidecode import unidecode
from register_commands import get_current_manager
from commands import *
from speech_recognition import UnknownValueError

listener = Listener()
manager = get_current_manager()
activator = "jarbas"

def run():
    response = ""

    while True:
        try:
            response = unidecode(listener.listen().lower())
        except UnknownValueError:
            print("Erro de reconhecimento.")
            continue
        if activator in response:
            break
    print(f"Texto reconhecido: {response}")
    response = response.replace(activator, '', 1)

    try:
        command, text = manager.find_matching_command_and_text(response)
        command_audio_response = command().run(text)
        reproduce(command_audio_response)
    except LookupError:
        reproduce("Desculpe, não entendi.")
    return
        
def get_twitter_creds():
    # TODO: Ask for Twitter API Credentials
    return
    

if __name__ == "__main__":
    get_twitter_creds()
    while True:
        run()
