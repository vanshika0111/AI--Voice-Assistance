# to display/check the CPU battery 

#install via pip terminal -->
# pip install psutil

import psutil

# definition 
# def convertTime(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     return "%d:%02d:%02d" % (hours, minutes, seconds)
    
# def cpu():
#     usage = str(psutil.cpu_percent())
#     speak("CPU is at ")
#     speak(usage)

#     battery = psutil.sensors_battery()
#     speak("Battery is at ")
#     speak(battery.percent)
#     speak("Power plugged in ")
#     speak(battery.power_plugged)
#     speak("Battery left ")
#     speak(convertTime(battery.secsleft))

# code
# if "cpu" in query:
#             cpu()