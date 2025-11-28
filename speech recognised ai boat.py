import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pywhatkit
import datetime
import time
import platform
import subprocess
import requests
import pyjokes
import wikipedia
import json
import re
import sys

# Initialize speech engine and recognizer
speaker = pyttsx3.init()
mic = sr.Recognizer()

def speak(text):
    print(f"Jarvis: {text}")
    speaker.say(text)
    speaker.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        mic.adjust_for_ambient_noise(source)
        voice = mic.listen(source)
        try:
            command = mic.recognize_google(voice).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is unavailable.")
            return ""

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def open_app(app_name):
    if platform.system() == "Windows":
        if app_name == "notepad":
            os.system("notepad")
        elif app_name == "calculator":
            os.system("calc")
        else:
            speak(f"Sorry, I cannot open {app_name} yet.")
    else:
        speak("App opening feature is currently supported on Windows only.")

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except Exception:
        speak("Sorry, I could not find information on that topic.")

def jarvis():
    speak("Welcome to Jarvis. How can I help you today?")
    while True:
        command = listen_command()
        if not command:
            continue

        if "open notepad" in command:
            speak("Opening Notepad")
            open_app("notepad")

        elif "send message" in command:
            speak("Sending a WhatsApp message")
            # Example phone number placeholder; replace with actual
            pywhatkit.sendwhatmsg_instantly("+91957XXXXXXX", "Hello, this is Jarvis")

        elif "play music" in command:
            speak("Playing music on YouTube")
            pywhatkit.playonyt("latest music")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "time" in command:
            tell_time()

        elif "joke" in command:
            tell_joke()

        elif "search wikipedia" in command:
            speak("What topic should I search on Wikipedia?")
            topic = listen_command()
            if topic:
                search_wikipedia(topic)

        elif "search google" in command:
            speak("What should I search for?")
            query = listen_command()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open calculator" in command:
            speak("Opening Calculator")
            open_app("calculator")

        elif "shutdown" in command or "exit" in command or "stop" in command or "quit" in command:
            speak("Goodbye! Have a nice day.")
            sys.exit()

        else:
            speak("I am sorry, I cannot perform that task yet.")

if __name__ == "__main__":
    jarvis()
