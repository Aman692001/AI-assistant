import os
import speech_recognition as sr




def takeCommandCMD():

    query = input(" please tell me how can i help you?\n ")

    return query

def takeCommandMic():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("listening.....")

        r.pouse_threshold = 1

        audio = r.listen(source)

    try:

        print("Recognizning....")

        query = r.recognize_google(audio , language='en-IN')

        print(query)

    except Exception as e:
        print(e)

        # speak("say that again please.....")

        return "None"

    return query



 
    #wake_up = takeCommandCMD()
    wake_up = takeCommandMic()

    if 'wake up' in wake_up:
        os.startfile("E:\\python2\\python_AI_project\\JARVIS.py")   

    else:
        print("Nothing......")    
        