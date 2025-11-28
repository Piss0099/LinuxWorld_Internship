import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import pywhatkit

speaker = pyttsx3.init()
mic = sr.Recognizer()

speaker.say("Welcome to Jarvis. I am ready")
speaker.runAndWait()

while True:
        with sr.Microphone() as source:  
            print("Listening..")
            voice = mic.listen(source)    
            text = mic.recognize_google(voice).lower()
            print("You said:", text)

        if "open notepad" in text:
            speaker.say("Opening Notepad")
            speaker.runAndWait()
            os.system("notepad")

        elif "open calculator" in text:
            speaker.say("Opening Calculator")
            speaker.runAndWait()
            os.system("calc")

        elif "open microsoft edge" in text:
            speaker.say("Opening Microsoft Edge")
            speaker.runAndWait()
            webbrowser.open_new_tab("https://copilot.microsoft.com")

        elif "play song" in text:
            speaker.say("Playing song on YouTube")
            speaker.runAndWait()
            pywhatkit.playonyt("Mohatar Ma")

        elif "search google" in text:
            speaker.say("Searching Google")
            speaker.runAndWait()
            pywhatkit.search("Python Programming")

        elif "send message" in text:
            speaker.say("Sending Whatsapp Message")
            speaker.runAndWait()
            pywhatkit.sendwhatmsg_instantly("ENTER WHERE TO SEND NUMBER", "Hi this IS Ravi Choudhary")

        elif "exit" in text or "quit" in text:
            speaker.say("Goodbye Ravi , shutting down Jarvis")
            speaker.runAndWait()
            break

        else:
            speaker.say("Sorry, I did not understand your command")
            speaker.runAndWait()
            break
