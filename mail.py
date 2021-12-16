#!bin/bash/python3

import smtplib

server=smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()

server.login("krishnaa@iul.ac.in", "mortalkraze19")
subject = 'Jenkins_Task'

msg = "Your code has been failed. Website is not loaded"

server.sendmail("krishnaa@iul.ac.in", "soulstormerkraze19@gmail.com", msg)
print("Email has been sent successfully !")
server.quit()
