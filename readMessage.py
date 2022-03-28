import email
import imaplib
from email.message import EmailMessage
import smtplib
import pass_keys
from speak import speaking
username = pass_keys.username
password = pass_keys.password

def readmail():
    host = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select('inbox')
    _,search_data = mail.search(None, 'UNSEEN')
    messages = []
    for num in search_data[0].split():
        my_mails = {}
        _, data = mail.fetch(num,'(RFC822)')
        _,b = data[0]
        email_message = email.message_from_bytes(b)    

        for header in ['Subject','From', 'To','Date']:
            print('{}: {}'.format(header,email_message[header]))
            my_mails[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type()=='text/plain':
                body = part.get_payload(decode=True)
                my_mails['body'] = body.decode()
            elif part.get_content_type()== 'text/html':
                html_body = part.get_payload(decode=True)
                my_mails['html_body'] = html_body.decode()
        messages.append(my_mails)
            
    return messages


# if __name__ == "__main__":
#   my_inbox = readmail()
#   print(my_inbox)
def check_mails():
    host = 'imap.gmail.com'
    speaking('wait while we run check on your mail')
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select('inbox')
    typ, messageIDs = mail.search(None, "UNSEEN")
    messageIDsString = str( messageIDs[0], encoding='utf8' )
    listOfSplitStrings = messageIDsString.split(" ")
    speaking(f'you have {len(listOfSplitStrings)} messages in your inbox')







        
        
        
