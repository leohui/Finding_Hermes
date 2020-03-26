import mylogin as ml
import smtplib as sm
from email.message import EmailMessage

#Email Message Variables
my_email_addr = ml.get_email()
my_password = ml.get_authpw()

def status_email(to_email_addr, subject, body, current_datetime):
    ## Build an Email Message
    msg = EmailMessage()
    msg['From'] = my_email_addr
    msg['To'] = to_email_addr

    ### Setup SMTP Server
    msg['Subject'] = f'{subject} {current_datetime}'
    msg.set_content(body)
    server = sm.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email_addr, my_password)
    server.send_message(msg)
    server.quit()

# Test send email
#status_email('leohui123@gmail.com','testing', 'testing', 2020)