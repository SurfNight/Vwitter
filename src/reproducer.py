from gtts import gTTS
from os import system

def reproduce(text):
    language = 'pt-BR'
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("output.mp3")
    system("mpg123 output.mp3")
    system("rm ./output.mp3")