# to take command from user and respond the same

# pip install pyttsx3

import pyttsx3

# to take command, module SpeechRecognition is used
# pip install SpeechRecognition

import speech_recognition as sr

# to access pyaudio, there are two steps
# 1. pip install pipwin
# 2. pipwin install pyaudio

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # to wait for 1 second before listening
        # r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            # query = r.recognize_google(audio, 'en=US')
            query = r.recognize_google(audio, language='en=in')
            print(query)
            speak(query)

        except Exception as e:
            print(e)
            speak("Missed it! Can you speak again?")
            return "None"
        return query

# takeCommand()

# if __name__ == "__main__":
#     speak("At you service")
