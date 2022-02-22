# to send emails 

import smtplib
# this is a built-in module, no need to install it

def send_mail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # 587 is the code number
    # to check the connection of the system, run below two lines
    server.ehlo()
    server.starttls()
    # to provide the login details of the user
    server.login("inkedsolace73@gmail.com", "INKEDSOLACE73")
    # to send the mail to reciever
    # server.sendmail("email@gmail.com", "reciever's email", content)
    server.sendmail("inkedsolace73@gmail.com", to, content)
    # to close the server
    server.close()

# content of sending mail
# if "send mail" in query:
#             try:
#                 speak("What is the reciever;s mail address?")
#                 to = "xyz@gmail.com"  # reciever's mail
#                 speak("Delievering mail to {to}")
#                 speak("What should I mail?")
#                 content = takeCommand()
#                 send_mail(to,content)
#                 speak(content)
#                 speak("Email sent successfully.")
#             except Exception as e:
#                 speak(e)
#                 speak("Unable to send mail.")


