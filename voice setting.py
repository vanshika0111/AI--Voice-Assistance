# to use various different languages of AI

import pyttsx3

# to initialize pyttsx3 module
engine = pyttsx3.init()

# there are six different voices for AI
#  index range is from 0 to 5
voice = engine.getProperty('voices')
# this will call the voice included in this module
engine.setProperty('voice', voice[1].id)
# this will the voice to index 2 i.e., female voice

# to change the rate of audio
# by default it is 200 words/minute
newVoiceRate = 100
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello Rishika. How are you?")