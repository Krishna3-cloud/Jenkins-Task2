#!bin/bash/python3

import smtplib

server=smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()

server.login("<sender email id>", "<password>")
subject = 'Jenkins_Task'

msg = "Your code has been failed. Website is not loaded"

server.sendmail("<sender mail id>", "<receiver mail id>", msg)
print("Email has been sent successfully !")
server.quit()
