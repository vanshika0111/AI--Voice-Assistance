# to display the current time

import pyttsx3

# to extract time 
#it is built-in module
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    # .strftime will extract the current time from module
    # speak(f"The time is {Time}")
    speak("Current time is ")
    speak(Time)
    # speak(Time)

time()