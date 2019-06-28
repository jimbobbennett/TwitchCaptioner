import config
import time
import azure.cognitiveservices.speech as speechsdk
from tkinter import *
import tkinter as tk

lastText = ""
appHeight = 150
padding = 20
labelText = NONE

def recognizing(args):
    global labelText
    global lastText

    latestText = args.result.text

    if  len(latestText) < len(lastText):
        print(latestText)
    else:
        diff = latestText[len(lastText):]
        print(diff)

    labelText.set(latestText)

class App:

    def __init__(self, master):
        print("Say something...")

root = Tk()
labelText = StringVar()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(str(screen_width) + "x" + str(appHeight) + "+0+" + str(screen_height - appHeight))
root.configure(background='black')
root.update_idletasks()
root.overrideredirect(True)
root.attributes('-alpha', 0.8)

labelWidth = screen_width-(padding * 2)

label = Label(root, textvariable=labelText, 
              foreground="white", height=appHeight, width=labelWidth, 
              background='black', font=("Courier", 44),
              justify=LEFT, anchor=SW, wraplength=labelWidth)
label.pack(padx=padding, pady=padding)

app = App(root)

speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.service_region)

if config.device_uuid == "":
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
else:
    audio_config = speechsdk.AudioConfig(device_name=config.device_uuid);
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

speech_recognizer.recognizing.connect(recognizing)
speech_recognizer.start_continuous_recognition()

root.mainloop()
root.destroy()

