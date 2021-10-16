from os import fwalk, sendfile
from listener import Listener
from reproducer import reproduce
from unidecode import unidecode
from register_commands import get_current_manager
from commands import *
from Gui import Gui
from speech_recognition import UnknownValueError
from time import sleep
import Twitter
import threading

listener = Listener()
manager = get_current_manager()
activator = "jarbas"

def run():
    response = ""

    while True:
        try:
            response = unidecode(listener.listen().lower())
        except UnknownValueError:
            interface.setJarbasSpeech("Erro de reconhecimento.")
            print("Erro de reconhecimento.")
            continue
        if activator in response:
            break
    print(f"Texto reconhecido: {response}")
    interface.setUserSpeech(response)
    response = response.replace(activator, '', 1)

    try:
        command, text = manager.find_matching_command_and_text(response)
        command_audio_response = command().run(text)
        reproduce(command_audio_response)
        interface.setJarbasSpeech("Podexá")
    except LookupError:
        interface.setJarbasSpeech("Desculpe, não entendi.")
        reproduce("Desculpe, não entendi.")
    return

def listening_loop():
    while True:
        if listening: 
            run()
        else:
            sleep(0.5)

if __name__ == "__main__":
    listening = False
    micON = lambda: listening = True
    micOFF = lambda: listening = False
    sendCallback = lambda key, secret: Twitter.my_twitter.set_api(key, secret)
    interface = Gui(micON, micOFF, sendCallback)
    listen_thread = threading.Thread(target=listening_loop)
    listen_thread.start()
    interface.mainloop()

        
