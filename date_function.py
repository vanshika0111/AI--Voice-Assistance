# to display/convey the current date

import pyttsx3

# to extract date
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    year = int ( datetime.datetime.now().year )
    month = int ( datetime.datetime.now().month )
    date = int ( datetime.datetime.now().day )

    speak("Today's date is ")
    speak(date)
    speak(month)
    speak(year)

# date()