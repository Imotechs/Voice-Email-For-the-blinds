import speech_recognition as my_speech
r = my_speech.Recognizer()
from speak import speaking



def listening():
    with my_speech.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('please talk ...')
        speaking("speak Now:")
        audio =r.listen(source)
        try:
            converted_text =r.recognize_google(audio)
            print('you said :'+ converted_text)
            return converted_text
        except Exception as e:
            print('error: ' +str(e))
