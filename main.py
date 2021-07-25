# importing already made functions from other files
from intro import intro
from command import takeCommand
# from command.py import takeCommand
from time_function import time
from date import date
from wiki import *
from mail import *
from browse import *
from window_operation import *
from gaane import *
from ss import *
from status import *
from jokessss import *

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\photooooo\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at ")
    speak(usage)

    battery = psutil.sensors_battery
    speak("Battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

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
                speak("Unable to send mail.")

        elif "search in chrome" in query:
            # speak("Searching...")
            speak("What should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            # wb.get(chromepath)
            search = takeCommand().lower()
            # search = takeCommand()
            wb.get(chromepath).open_new_tab(search+ ".com")

        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_directory = "E:\playlist"
            songs = os.listdir(songs_directory)
            os.startfile(os.path.join(songs_directory, songs[0]))

        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You just asked me to remember " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you remember" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that " + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "offline" in query:
            print("Have a good day!")
            speak("Quitting. Have a good day.")
            quit()


# search in chrome
# logout/shutdown/restart
# battery

