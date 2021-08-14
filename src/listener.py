import speech_recognition as sr

def listen() -> str:
    """
    Listens to the user's speech and returns the text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    # TODO: Use IBM cloud instead of Web Google Speech Recognition
    return recognizer.recognize_google(audio, language='pt-BR')

if __name__ == "__main__":
    try:
        response = listen()
    except sr.UnknownValueError:
        raise Exception("AudioUnrecognizable")
    except sr.RequestError:
        raise Exception("")
    print(response)