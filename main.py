# importing already made functions from other files
from intro import intro
from command import takeCommand
# from command.py import takeCommand
from time_function import time
from date import date
from wiki import *
from mail import *
from browse import *

# importing module
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    intro();
    while True:
        query = takeCommand().lower()
        print(query)

       
        if "date" in query:
            date();

        elif "time" in query:
          time();

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)

        elif "send mail" in query:
            try:
                speak("What is the reciever;s mail address?")
                to = "xyz@gmail.com"  # reciever's mail
                speak("Delievering mail to {to}")
                speak("What should i mail?")
                content = takeCommand()
                send_mail(to,content)
                speak(content)
                speak("Email sent successfully.")
            except Exception as e:
                speak(e)
                speak("Unable to sen email.")

        elif "search in chrome" in query:
            # speak("Searching...")
            speak("What should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")


        elif "offline" in query:
            print("Have a good day!")
            speak("Quitting. Have a good day.")
            quit()

