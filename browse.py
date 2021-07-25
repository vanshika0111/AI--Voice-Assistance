# to search on google

import webbrowser as wb
# this is a built-in module

# to check the details of your google chrome
# search the below line in google
# chrome://version
# it will give all the information about your google chrome

# path of my google chrome:
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

# below is the code for searching on chrome
# if "search in chrome" in query:
#             # speak("Searching...")
#             speak("What should I search?")
#             chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
#             search = takeCommand().lower()
#             wb.get(chromepath).open_new_tab(search + ".com")