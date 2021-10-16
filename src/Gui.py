from tkinter import *
from PIL import Image,ImageTk

class Gui:
    def __init__(self,micON_callback, micOFF_callback, send_callback):
        self.win = Tk()
        self.win.title('Vwitter')
        self.win.geometry("400x500+10+10")

        self.micON_callback= micON_callback
        self.micOFF_callback= micOFF_callback
        
        self.key_lbl=Label(self.win, text='API Key_lb')
        self.secret_lbl=Label(self.win, text='API Secret')
        self.key_ent=Entry()
        self.secret_ent=Entry()
        self.key_lbl.place(x=50, y=50)
        self.key_ent.place(x=150, y=50)
        self.secret_lbl.place(x=50, y=100)
        self.secret_ent.place(x=150, y=100)
        self.send_bt=Button(self.win, text='Enviar', width=30, command=send_callback(self.key_ent.get(),self.secret_ent.get()))
        self.send_bt.place(x=50, y=150)
        self.mic_icon= (Image.open("mic.png"))
        self.micon_icon= (Image.open("micon.png"))
        ratio = 272/185
        size = 80
        self.mic_icon=self.mic_icon.resize((int(size*ratio),size))
        self.micon_icon=self.micon_icon.resize((int(size*ratio),size))
        self.mic_icon=ImageTk.PhotoImage(self.mic_icon)
        self.micon_icon=ImageTk.PhotoImage(self.micon_icon)
        self.micb=Button(self.win, image = self.mic_icon, relief='raised',command=self.toggleMic)
        self.micb.place(x=120, y=200)
        self.j_speech_lbl =Label(self.win, text='Jarbas: ')
        self.jarbas_speech=Label(self.win,text='Pode falar, pai')
        self.j_speech_lbl.place(x=50, y=310)
        self.jarbas_speech.place(x=100, y=310)
        self.u_speech_lbl =Label(self.win, text='Você: ')
        self.user_speech=Label(self.win,text='Jarbas, publique pra cima deles mengão')
        self.u_speech_lbl.place(x=50, y=390)
        self.user_speech.place(x=90, y=390)
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
    def setJarbasSpeech(self,text):
        self.jarbas_speech.config(text=text)
    def setUserSpeech(self,text):
        self.user_speech.config(text=text)
    def mainloop(self):
        self.win.mainloop()