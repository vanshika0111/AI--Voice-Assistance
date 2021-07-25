# how to access the module

# pip install pyttsx3
# pip install pywin32

import pyttsx3

# to initialize pyttsx3 module
engine = pyttsx3.init()

# to give a text to speak
# engine.say("I will speak this text")

# to command the engine to give output
# engine.runAndWait()

# in place of above 4 lines use definitions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello Rishika. How are you?")

