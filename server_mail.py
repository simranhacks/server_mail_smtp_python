import smtplib

sender_email = input("Enter the sender's email")
receiver_email = input("Enter the receiver's email")
password = input("Enter the app generated password")
message = input("Enter the message")

server =smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email, receiver_email, message)
server.quit()
