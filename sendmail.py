
from email.message import EmailMessage
import smtplib
import pass_keys
from listen import listening
from speak import speaking
username = pass_keys.username
password = pass_keys.password
mails = ['alex01@gmail.com','adzembehj@gmail.com','imotechs01@gmail.com','Adzembeh joshua']

def send_messages():
    speaking('do you want to send message to a mail in your local list of mails?')
    option = listening()
    if 'yes' in str(option):
        speaking('your local mails are.;')
        for index,mail in enumerate(mails, start=1):
            speaking(f'{index}: {mail}')
        choice = listening()
        speaking('what is the message to be sent?, keep Talking till you finish')
        
        msg = EmailMessage()
        body = listening()
        if 'one' in str(choice) or '1' in str(choice):
            msg['To'] = 'adzembehj@gmail.com'  
        elif 'two' in str(choice) or '2' in str(choice):
            msg['To'] = 'alex01@gmail.com'  
        elif 'three' in str(choice) or '3' in str(choice):
            msg['To'] = 'imotechs01@gmail.com'  
        elif 'four' in str(choice) or '4' in str(choice):
            msg['To'] = 'joshuaimoter01@gmail.com'
        else:
            speaking('your choice is out of range')

        
        msg['subject'] = 'Voice Eail Master'
        msg['From'] =f'Voice Message<{username}>'
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(username, password)
            try:
                smtp.send_message(msg)
                speaking('mail sent to :' +str(msg['To']))
            except Exception as error:
                speaking('NOT SENT!, An Error occur, pls try again')
                
    else:
        speaking('please contact your mail aid to set up the optional mail')
