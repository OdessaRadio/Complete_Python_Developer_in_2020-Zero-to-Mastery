import smtplib # Simple Mail Transfer Protocol 
from email.message import EmailMessage

# Dummy email:
# oleklia532@gmail.com
# 890_^&*_aqt

email = EmailMessage()
email['from'] = 'Olek Lia'
email['to'] = 'alexander_lyshko@hotmail.com'
email['subject'] = 'Test message from Zero to Matery'

email.set_content('I am a Python master')

with smtplib.SMTP(host = 'smtp.gmail.com',
                  port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('oleklia532@gmail.com','890_^&*_aqt')
    smtp.send_message(email)
    print('done')

