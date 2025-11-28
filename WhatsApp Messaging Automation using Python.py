import matplotlib.pyplot as plt
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pywhatkit
speaker = pyttsx3.init()
mic = sr.Recognizer()
speaker.say("welcome to jarvis ")
speaker.runAndWait()
with sr.Microphone() as source:
    print("start speaking...")
    voice = mic.listen(source)
    text = mic.recognize_google(voice)
if "open Notepad" in text:
    print("opening notepad...")
    os.system("Notepad")
elif "send message" in text :
    print("sending message.. ")
    pywhatkit.sendwhatmsg_instantly("ENTER NUMBER WHERE TO SEND " , "hello Ravi This Side",7,18)
    
