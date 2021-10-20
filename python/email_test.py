import smtplib
from email.message import EmailMessage
def verification(email,n):
    email_add="stockserviceproviderdb@gmail.com"
    email_pd="dbms1234"

    msg=EmailMessage()
    msg['Subject']='verification'
    msg['From']=email_add
    msg['To']=email
    msg.set_content("OTP for verification : "+n)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_add,email_pd)

        smtp.send_message(msg)

