import pyttsx3 as spk
starter = spk.init()
voices = starter.getProperty('voices')
starter.setProperty('voices', voices[1])
starter.setProperty('rate',150)
volume = starter.getProperty('volume')
starter.setProperty('volume', volume+0.3)

rate = starter.getProperty('rate')
starter.setProperty('rate', rate+10)


def speaking(text):
    print(text)
    starter.say(text)
    starter.runAndWait()
