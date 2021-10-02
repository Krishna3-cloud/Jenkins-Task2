#!bin/bash/python3

import smtplib

server=smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()

server.login("<sender_mail_id>", "<password>")
subject = 'Jenkins_Task'

msg = "Your code has been failed. Website is not loaded"

server.sendmail("<sender_mail_id", "<receiver_mail_id>", msg)
print("Email has been sent successfully !")
server.quit()
