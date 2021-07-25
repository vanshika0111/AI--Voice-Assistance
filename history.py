# if user asks assistant what they communicated

"""
a text file is created first
whenevr user says 'remember that'
assistant will write the data in this text file
and if user asks again what he/she told it remember
it will open the text file and convey the message
****** it is like notes ******
"""

# below is the code to make it remember:
# if "remember that" in query:
#             speak("What should i remember?")
#             data = takeCommand()
#             speak("You asked me to remember " + data)
#             remember = open("data.txt", "w")
#             remember.write(data)
#             remember.close()

# below is the code to ask is if it knows anything
# elif "do you remember" in query:
#             remember = open("data.txt", "r")
#             speak("you said me to remember that " + remember.read())
