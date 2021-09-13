from gtts import gTTS
from os import remove
from playsound import playsound
    
def reproduce(text):
    language = 'pt-BR'
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("output.mp3")
    playsound("output.mp3")
    remove("output.mp3")