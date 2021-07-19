# to greet the user

import pyttsx3

# to extract time and date
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%H:%M:%S')
    # .strftime will extract the current time from module
    speak("Current time is ")
    speak(Time)
    # speak(Time)
    # speak("Current time is {Time}")
   

def date():
    year = int ( datetime.datetime.now().year )
    month = int ( datetime.datetime.now().month )
    date = int ( datetime.datetime.now().day )
    
    speak("Today's date is ")
    speak(date)
    speak(month)
    speak(year)

def greet():
    speak("Welcome back sir!")

    time()
    date()

    hour = datetime.datetime.now().hour

    if (hour >= 6 and hour <= 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good evening")
    else:
        speak("Good night")

    speak("How can I help you?")

greet()
