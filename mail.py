#!bin/bash/python3

import smtplib

server=smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()

server.login("krishnapal3sep@gmail.com", "kraze92017warrior#159")
subject = 'Jenkins_Task'

msg = "Your code has been failed. Website is not loaded"

server.sendmail("krishnapal3sep@gmail.com", "soulstormerkraze19@gmail.com", msg)
print("Email has been sent successfully !")
server.quit()
