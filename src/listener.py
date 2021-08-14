import speech_recognition as sr

class Listener():
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
    
    def listen(self) -> str:
        """
        Listens to the user's speech and returns the text.
        """
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        # TODO: Use IBM cloud instead of Web Google Speech Recognition
        return self.recognizer.recognize_google(audio, language="pt-BR")

# test
if __name__ == "__main__":
    try:
        response = Listener().listen()
    except sr.UnknownValueError:
        raise Exception("AudioUnrecognizable")
    except sr.RequestError:
        raise Exception("")
    print(response)