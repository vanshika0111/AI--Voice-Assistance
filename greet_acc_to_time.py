# to greet the user
# good morning/ good evening/ good night

import pyttsx3

# to extract time and date
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    # speak("Welcome back sir!")
   
    hour = datetime.datetime.now().hour

    if (hour >= 6 and hour <= 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good evening")
    else:
        speak("Good night")

    # speak("How can I help you?")

# greet()
