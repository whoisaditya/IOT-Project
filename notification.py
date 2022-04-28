import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = 'INTRUDER ALERT!!! \n\nThis is to notify you that an intruder was detect in your office. \n from \nRaspbery'
#The mail addresses and password
sender_address = #ENTER RASPBERRY EMAIL ADDRESS
sender_pass = #ENTER PASSWORD
receiver_address = #ENTER RECEIVER EMAIL ADDRESS
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
