# to take user's details

import pyttsx3
from command import *

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def username():
    speak("What should I call you?")
    UserName = takeCommand()
    speak(f"Hello {UserName}")
    speak("How can I help you?")