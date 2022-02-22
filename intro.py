# how the assistant will start

import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def intro():
    speak("Welcome back!")
    speak ("I am Jarvis.")
    # speak("At you service.")
    # speak("How can I help you?")

# intro()
