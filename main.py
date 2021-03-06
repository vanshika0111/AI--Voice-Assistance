# ------------------- importing already made functions from other files -----------
from greet_acc_to_time import *
from intro import *
from user_details import *
from command import *
from date_function import *
from time_function import *
from wiki import *
from browse import *
from window_operation import *
from gaane import *
from ss import *
from status import *
from jokessss import *

# ------------------------------ function definitions -------------------------------
def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\photosss\ss.png")

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at ")
    speak(usage)

    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)
    speak("Power plugged in ")
    speak(battery.power_plugged)
    speak("Battery left ")
    speak(convertTime(battery.secsleft))

def jokes():
    speak(pyjokes.get_joke())

# --------------------------- importing module -------------------------------
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# --------------------------- global declaration -------------------------------
assistant = "Jarvis"
coder = "Vanshika"

# --------------------------------- main function ----------------------------
if __name__ == "__main__":
    greet()
    intro()
    username()
    while True:
        query = takeCommand().lower()
        print(query)

        if "who are you" in query:
            speak(f"My friends call me {assistant}")

        elif "who invented you" in query:
            speak(f"I am coded by {coder}")

        elif "date" in query:
            date()
        
        elif "time" in query:
            time()

        elif "wikipedia" in query:
            try:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences = 2)
                speak(result)
            except Exception as e:
                speak(e)
                speak("No results found!")
        
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            try:
                songs_directory = ("C:/Users/VANSHIKA/Desktop/playlist")
                songs = os.listdir(songs_directory)
                os.startfile(os.path.join(songs_directory, songs[0]))
            except Exception as e:
                speak(e)
                speak("Your device doesn't have any songs directory.")

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
            try:
                screenshot()
                speak("Done!")
            except Exception as e:
                speak(e)
                speak("Couldn't capture the screen. Try again!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

        elif "offline" in query:
            print("Have a good day!")
            speak("Quitting. Have a good day.")
            quit()

        else:
            print("I do not have an answer to this question.")
            speak("I do not have an answer to this question.")