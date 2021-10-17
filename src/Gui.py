from tkinter import *
from PIL import Image, ImageTk
import Twitter
import requests


class Gui:
    def __init__(self, micON_callback, micOFF_callback, send_callback, creds):
        self.win = Tk()
        self.win.title('Vwitter')
        self.win.geometry("380x800")

        self.consumer_key_text = creds.get('consumer_key', '')
        self.consumer_secret_text = creds.get('consumer_secret', '')
        self.key_text = creds.get('key', '')
        self.secret_text = creds.get('secret', '')

        self.micON_callback = micON_callback
        self.micOFF_callback = micOFF_callback
        self.send_callback = send_callback

        self.consumer_key_lbl = Label(self.win, text='Consumer Key')
        self.consumer_secret_lbl = Label(self.win, text='Consumer Secret')
        self.key_lbl = Label(self.win, text='Access Token')
        self.secret_lbl = Label(self.win, text='Access Token Secret')

        self.consumer_key_ent = Entry()
        self.consumer_key_ent.insert(0, self.consumer_key_text)

        self.consumer_secret_ent = Entry()
        self.consumer_secret_ent.insert(0, self.consumer_secret_text)

        self.key_ent = Entry()
        self.key_ent.insert(0, self.key_text)

        self.secret_ent = Entry()
        self.secret_ent.insert(0, self.secret_text)

        self.consumer_key_lbl.place(x=50, y=50)
        self.consumer_key_ent.place(x=200, y=50)

        self.consumer_secret_lbl.place(x=50, y=100)
        self.consumer_secret_ent.place(x=200, y=100)

        self.key_lbl.place(x=50, y=150)
        self.key_ent.place(x=200, y=150)

        self.secret_lbl.place(x=50, y=200)
        self.secret_ent.place(x=200, y=200)

        self.send_bt = Button(self.win, text='Atualizar Credenciais',
                              width=30, command=self.send_creds)
        self.send_bt.place(x=50, y=250)

        #self.picture_url = Twitter.my_twitter.get_profile_picture()
        self.send_bt2 = Button(self.win, text='Atualizar Foto',
                               width=30, command=self.updateProfilePicture)
        self.send_bt2.place(x=50, y=280)

        self.mic_icon = (Image.open("./assets/images/mic.png"))
        self.micon_icon = (Image.open("./assets/images/micon.png"))
        self.logo = (Image.open("./assets/images/vwitterLogo.png"))
        self.jarbas_logo = (Image.open("./assets/images/homem-robo.png"))
        #self.pessoa_logo = (Image.open("./assets/images/avatar-homem.png"))
        self.pessoa_logo = (Image.open("./assets/images/avatar-homem.png"))

        ratio = 272/185
        size = 80
        self.mic_icon = self.mic_icon.resize((int(size*ratio), size))
        self.micon_icon = self.micon_icon.resize((int(size*ratio), size))
        self.jarbas_logo = self.jarbas_logo.resize((50, 50))
        self.pessoa_logo = self.pessoa_logo.resize((50, 50))

        self.mic_icon = ImageTk.PhotoImage(self.mic_icon)
        self.micon_icon = ImageTk.PhotoImage(self.micon_icon)
        self.logo_icon = ImageTk.PhotoImage(self.logo)
        self.jarbas_icon = ImageTk.PhotoImage(self.jarbas_logo)
        self.pessoa_icon = ImageTk.PhotoImage(self.pessoa_logo)

        self.logo_lbl = Label(self.win, image=self.logo_icon)
        self.logo_lbl.place(x=50, y=700)
        self.micb = Button(self.win, image=self.mic_icon,
                           relief='raised', command=self.toggleMic)
        self.micb.place(x=120, y=300)

        self.j_speech_lbl = Label(self.win, image=self.jarbas_icon)
        self.jarbas_speech = Label(self.win, text='Fala comigo.')
        self.j_speech_lbl.place(x=50, y=410)
        self.jarbas_speech.place(x=100, y=430)
        self.u_speech_lbl = Label(self.win, image=self.pessoa_icon)
        self.user_speech = Label(self.win, text='')
        self.u_speech_lbl.place(x=50, y=490)
        self.user_speech.place(x=100, y=510)

    def toggleMic(self):
        if self.micb.config('relief')[-1] == 'sunken':
            self.micb.config(relief="raised")
            self.micb.config(background='Light Grey')
            self.micb.config(image=self.mic_icon)
            self.micOFF_callback()
        else:
            self.micb.config(background='Dark Grey')
            self.micb.config(image=self.micon_icon)
            self.micb.config(relief="sunken")
            self.micON_callback()

    def send_creds(self):
        self.send_callback(self.consumer_key_ent.get(
        ), self.consumer_secret_ent.get(), self.key_ent.get(), self.secret_ent.get())

    def setJarbasSpeech(self, text):
        self.jarbas_speech.config(text=text)

    def setUserSpeech(self, text):
        self.user_speech.config(text=text)

    def mainloop(self):
        self.win.mainloop()

    def getProfilePicture(self):
        self.profile_picture = Twitter.my_twitter.get_profilePic_url()
        return self.profile_picture

    def updateProfilePicture(self):
        self.getProfilePicture()
        url = self.profile_picture
        print(url)
        self.pessoa_logo = Image.open(requests.get(url, stream=True).raw)
