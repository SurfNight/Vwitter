import json
from listener import Listener
from reproducer import reproduce
from unidecode import unidecode
from register_commands import get_current_manager
from commands import *
from Gui import Gui
from speech_recognition import UnknownValueError
import Twitter
import threading

listener = Listener()
manager = get_current_manager()
activator = "jarbas"


def run(wait_for_jarbas=True):
    response = ""

    while wait_for_jarbas:
        try:
            response = unidecode(listener.listen().lower())
        except UnknownValueError:
            print("Não falou jarbas.")
            interface.setUserSpeech(response)
            continue
        if activator in response:
            print(f"Falou jarbas.")
            interface.setUserSpeech(response)
            interface.mic_on()
            break
        print("Não falou jarbas.")

    repeat_text = "Fala comigo." if wait_for_jarbas else "Por favor, tente novamente."

    while True:
        try:
            reproduce(repeat_text)
            response = unidecode(listener.listen().lower())
        except UnknownValueError:
            interface.setJarbasSpeech(f"Desculpe, não entendi.")
            reproduce("Desculpe, não entendi.")
            repeat_text = "Por favor, tente novamente."
            print("Erro de reconhecimento.")
            continue
        interface.setUserSpeech(response)
        break

    wait_next_time = True
    try:
        command, text = manager.find_matching_command_and_text(response)
        command_audio_response = command().run(text)
        interface.setJarbasSpeech(command_audio_response)
        reproduce(command_audio_response)
        interface.mic_off()
    except LookupError:
        interface.setJarbasSpeech("Desculpe, não entendi.")
        reproduce("Desculpe, não entendi.")
        wait_next_time = False
    except Exception as e:
        print(e)
        interface.setJarbasSpeech("Ocorreu um erro inesperado.")
        reproduce("Ocorreu um erro inesperado.")
        wait_next_time = False
    return wait_next_time


def listening_loop():
    should_wait_for_jarbas = True
    while state["running"]:
        should_wait_for_jarbas = run(should_wait_for_jarbas)


if __name__ == "__main__":
    state = {
        'running': True
    }

    def sendCallback(consumer_key, consumer_secret, key, secret):
        with open("creds.json", 'w') as creds:
            creds.write(json.dumps({
                "consumer_key": consumer_key,
                "consumer_secret": consumer_secret,
                "key": key,
                "secret": secret
            }))

        Twitter.my_twitter.set_api(consumer_key, consumer_secret, key, secret)

    creds = {}
    with open("creds.json", 'r') as creds_file:
        try:
            creds = json.load(creds_file)
        except:
            pass

    if creds:
        Twitter.my_twitter.set_api(**creds)

    interface = Gui(sendCallback, creds)
    listen_thread = threading.Thread(target=listening_loop)
    listen_thread.start()
    interface.mainloop()
    state['running'] = False
    listen_thread.join()
