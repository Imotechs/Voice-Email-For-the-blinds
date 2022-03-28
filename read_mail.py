from logging import exception
from speak import speaking
from listen import listening
from readMessage import readmail
def read_inbox(messages): 
    speaking(f'you have {len(messages)} messages in your inbox')
   
    for index,message in enumerate(messages, start=1):
        try:
        
            speaking(index,message)
          
        except exception as e:
            speaking('error:' +str(e))
        # else:
        #     speaking(f'your choice is out of range.')
        #     speaking(f'select from 1 to {len(messages)} since you have only {len(messages)} Messages')

    # for index, message in enumerate(messages, start=1):
    #     print(index, message)