from logging import exception
import speech_recognition as sr
import pyttsx3
import os
from email.message import EmailMessage
from speak import speaking
from listen import listening
from sendmail import send_messages
from readMessage import check_mails, readmail
import pass_keys
from read_mail import read_inbox

def talker():
    #setting login variables
    username = pass_keys.Login_name
    userpass = pass_keys.Login_Pass
    speaking("what do you want mail Master to do for you")
    speaking('select from the options as follow')
    speaking('Login, check imbox, Read Inbox,  Send Mail, Exit')
    selected = listening()
    speaking(f'you selected {selected}')
    if 'login' in str(selected):
        username = 'whats your username'
        speaking(username)
        username = listening()
        speaking(f'you said {username}, are you sure of this? say yes to continoue and no to enter your username again')
        choice = listening()
        if'yes' in str(choice):
            
            speaking('what is your Pawssword?')
            pas = listening()
            speaking(f'you said {pas} are you sure of this?')
            text = listening()
            if 'yes' in str(text):
                if pas ==userpass and username == username:
                    speaking('you have loged in succesfully')
                    speaking('you can choose to do the following')
                    speaking('send Mail, Read mail')
                    task = listening()
                    if 'send' in str(task):
                        speaking('you have choosen to send mails')
                        send_messages()
                    elif 'Read' in str(task):
                        speaking('you have choosen to Read from your inbox')
                        read_inbox(readmail())
                else:
                 speaking('wrong login details')
        elif 'no' in str(choice) :
            speaking('what is your username')
        else:
            speaking('you said a wrong thing')

    elif 'send'in str(selected):
        speaking('you must login to send a mail')
        talker()  
    elif 'read' in str(selected):
        speaking('you must login to Read a mail')
        talker()
    elif 'check' in str(selected):
        speaking('you have chose to check your inbox')
        check_mails()
    elif 'exit' in str(selected):
        #os.getcwd()
        os.close(os.getcwd())
    else:
        speaking('your choice is out of range') 

    