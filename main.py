import imaplib
from readMessage import readmail
from voice_demo import talker, send_messages,read_inbox
import pass_keys
import pyttsx3 as spk
import speech_recognition as sr
username = pass_keys.username
password = pass_keys.password


while (True):
    talker()    

