
from cProfile import label
from lib2to3.pgen2.tokenize import StopTokenizing
from logging.config import stopListening
from pickle import STOP
from unittest.main import main
from winsound import PlaySound
import pyttsx3  # pip install pyttsx3 == trxt data into speech using python

import speech_recognition as sr  #pip install speechRecognition == speech into text format

import smtplib

from Secrets import senderemail, epwd, to

from email.message import EmailMessage

import pyautogui

import webbrowser as wb

from time import sleep

import wikipedia

import pywhatkit

import requests

from newsapi import NewsApiClient

import clipboard
import os

import pyjokes
import time as tt

import string
import random
import psutil

from nltk.tokenize import word_tokenize

import datetime

import cv2
import numpy as np
import pyautogui as p

from playsound import playsound


engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()


def getvoices(voice):

    voices = engine.getProperty('voices')

    print(voices[1].id)

    if voice == 1:

        engine.setProperty('voice', voices[0].id)

        speak("hello this is jarvis2.0")


    if voice == 2:

        engine.setProperty('voice', voices[1].id)

        speak("hello this is Jarvis")

    

    if voice == 3:

        engine.setProperty('voice', voices[2].id)

        speak("hello this is Friday") 
    


def time():

    Time = datetime.datetime.now().strftime("%I:%M:%S")   #I-hours, M-minutes, S-seconds

    speak("the current time is: ")

    speak(Time)


def date():

    year = int(datetime.datetime.now().year)

    month = int(datetime.datetime.now().month)

    date = int(datetime.datetime.now().day)

    speak("today's date is:")

    speak(date)

    speak(month)

    speak(year)


def greeting():

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <12:

        speak("good morning sir!")

    elif hour >= 12 and hour <18:

        speak("good afternoon sir!")

    elif hour >=18 and hour <24:

        speak("good evning sir!")

    else:

        speak("good Night sir!")         

def wishme():

    speak("welcome back sir!")
    time()
    date()

    greeting()

    speak("Jarvis at your service , please tell me how can i help you?")        

    #while True:

   #    voice = int(input("Press 1 for male voice\nPress 2 for female voice\nPress 3 for female voice\n"))

  #     audio()

 #      getvoices(voice)

#def audio():
 #   speak(audio)

wishme()


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
    #query = query.lower()

    return query


def sendEmail(receiver, subject, content):

    # server = smtplib.SMTP('smpt.gmail.com', 587)

    server = smtplib.SMTP('64.233.184.108')

    server.starttls()

    server.login(senderemail, epwd)

    email = EmailMessage()

    email['from'] = senderemail

    email['to'] = receiver

    email['subject'] = subject

    email.set_content(content)

    server.send_message(email)

    server.close()


def sendwhatsmsg(phone_no, message):

    Message = message

    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)

    sleep(9)

    pyautogui.press('enter')
    

def searchgoogle():

    speak('what should i search for you ?')

    search = takeCommandMic()

    wb.open('https://www.google.com/search?q='+search)



def news():

    newsapi = NewsApiClient(api_key='719b4758f97e40a3bfac00ae1d538d98')

    speak('what kind of news you like to hear?')
    jls_extract_var = takeCommandMic
    data = newsapi.get_top_headlines(q = jls_extract_var(),

                                     language='en',

                                     page_size=5)

    newsdata = data['articles']

    for x,y in enumerate(newsdata):

        print(f'{x}{y["description"]}')

        speak((f'{x}{y["description"]}'))
    

    speak("that's it for now i'll update you in some time")


def text2speech():

    text = clipboard.paste()

    print(text)

    speak(text)


def covid():

    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')


    data = r.json()

    covid_data = f' cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered :{data["recovered"]}'

    print(covid_data)

    speak(covid_data)


def screenshot():

    name_img = tt.time()

    name_img = f'E:\\python\\python_AI_project\\screenshot\\{name_img}.png'

    img = pyautogui.screenshot(name_img)

    img.show()

    speak('done')


def passwordgen():

    s1 = string.ascii_uppercase

    s2 = string.ascii_lowercase

    s3 = string.digits

    s4 = string.punctuation
    

    passlen = 8

    s =[]

    s.extend(list(s1))

    s.extend(list(s2))

    s.extend(list(s3))

    s.extend(list(s4))


    random.shuffle(s)

    newpass = ("".join(s[0:passlen]))

    print(newpass)

    speak(newpass)


def flip():

    speak("okay sir, flipping a coin")

    coin = ['heads', 'tails']

    toss =[]

    toss.extend(coin)

    random.shuffle(toss)

    toss = ("".join(toss[0]))

    speak("i flipped the coin and you got"+toss)


def roll():

    speak("okay sir, rolling a die for you")

    die = ['1','2','3','4','5','6']

    roll = []

    roll.extend(die)

    random.shuffle(roll)

    roll = ("".join(roll[0]))

    speak("i rolled a die and you got"+roll)


def cpu():

    usage = str(psutil.cpu_percent())

    speak("cpu is at"+usage)

    # battery = psutil.sensors_bettery()

    # speak('battery is at')

    # speak(battery.percent)
    

def TakeExe():
    p.press('esc')
    speak("verification successfull")
    speak("Hello , i am Jarvis.")
    speak("How can i Help You ?")



 #ttp://api.openweathermap.org/data/2.5/weather?q=(city)&units=imperial&appid=(API KEY)



#if __name__ == "__main__":
    
    #getvoices(1)

    #wishme()

    wakeword = "jarvis"  #<----------wake word

    while True:

        query = takeCommandMic().lower()

        query = word_tokenize(query)

        print(query)

        if wakeword in query:

            if 'time' in query:
                time()


            elif 'date' in query:
                date()


            elif 'email' in query:

                email_list ={

                    'Dinesh':'dinesh321.dj@gmail.com',

                    'Aman' :'adj692001@gmail.com'

                }

                try:

                    speak("To whom you want to send the mail?")

                    name = takeCommandMic()

                    receiver = email_list[name]

                    speak("what is the subject of the mail?")

                    subject =takeCommandMic()

                    speak('what should i say?')

                    content = takeCommandMic()

                    sendEmail(receiver, subject, content)

                    speak('email has been send')

                except Exception as e:
                    print(e)

                    speak("unablie to send the email")


            elif 'message' in query:

                user_name = {

                    'Gaurav':'+91 88988 61761',

                    'Aman':'+91 79776 75889'

                }

                try:

                    speak("To whom you want to send the What's app message?")

                    name = takeCommandMic()

                    phone_no = user_name[name]

                    speak("what should be the Message?")

                    message =takeCommandMic()

                    sendwhatsmsg(phone_no,message)

                    speak('message has been send')

                except Exception as e:
                    print(e)

                    speak("unablie to send the message")
            

            elif 'wikipedia' in query:

                speak('searching on wikipedia.....')

                query = query.replace("wikipedia", " wikipedia")

                result = wikipedia.summary(query, sentences = 2)
                print(result)

                speak(result)
            

            elif'search' in query:

                searchgoogle()

                speak('here i find some result')


            elif 'youtube' in query:

                speak('which video should i play on youtube?')

                topic = takeCommandMic()

                pywhatkit.playonyt(topic)

                speak('here we go')


            elif'weather' in query:

                speak ('which city?')

                city = takeCommandMic()

                url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=694161d986849f3bc4a9234792750794'


                res = requests.get(url)

                data = res.json()


                weather = data['weather'] [0] ['main']

                temp = data['main']['temp']

                desp = data['weather'] [0] ['description']

                temp = round((temp - 32) * 5/9)

                print(weather)
                print(temp)
                print(desp) 

                speak(f"today's weather in {city} city is like")

                speak('Temperature : {} degree celcius'.format(temp))

                speak('weather is {}'.format(desp))


            elif 'news' in query:

                news()


            elif 'read' in query:

                text2speech()


            elif 'covid' in query:

                covid()


            elif 'code' in query:

                codepath = "E:\\Microsoft VS Code\\Code.exe"

                os.startfile(codepath)


            elif 'opening' in query:
                req = query
                os.system("explorer E:\\{}".format(req.replace("open"," ")))
                

            elif 'joke' in query:

                speak(pyjokes.get_joke())


            elif 'screenshot' in query:
                screenshot()


            elif 'remember that' in query:

                speak('what should i remember?')

                data = takeCommandMic()

                speak("you said me to remember that"+data)

                remember = open('data.txt','w')

                remember.write(data)

                remember.close()


            elif 'do you know anything' in query:

                remember = open('data.txt','r')

                speak("you told me to remember that "+remember.read())


            elif 'password' in query:

                passwordgen()


            elif 'flip' in query:

                flip() 


            elif 'roll' in query:
                roll()


            elif 'cpu' in query:
                cpu()


            elif 'mobileno' in query:
                ()

            elif 'games' in query:
                speak('which game do you want to play')
                games = takeCommandMic()
                speak("Injoy your game sir"+games)
                games= "E:\\python\\Games"
                fan= "E:\\python\\Games\\fan.py"
                CrossIT= "E:\\python\\Games\\CrossIT.py"
                jumping_jack= "E:\\python\\Games\\Jumping_Jack.py"
                pacman= "E:\\python\\Games\\pacman.py"
                paint= "E:\\python\\Games\\paint.py"
                ping_pong= "E:\\python\\Games\\Ping_Pong.py"
                Simon_says= "E:\\python\\Games\\Simon_says.py"
                snakegame= "E:\\python\\Games\\snakegame.py"
                x_and_0= "E:\\python\\Games\\XandO.py"
                os.startfile(games)  
                os.startfile(CrossIT)
                os.startfile(fan)
                os.startfile(jumping_jack)
                os.startfile(pacman)
                os.startfile(paint)
                os.startfile(ping_pong)
                os.startfile(Simon_says)
                os.startfile(snakegame)
                os.startfile(x_and_0)  





            
            elif 'offline' in query:

                speak('ok sir')
                speak('Just say wake up jarvis!')
                break
                #quit()
                


            elif "goodbye" in query:
                speak("thanks for using me sir.")
                quit()





            
if __name__ == "__main__":


    while True:

        Permission = takeCommandMic()

        
        ###################################################################################################################################################
        recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


        id = 1 #number of persons you want to Recognize


        names = ['','aman']  #names, leave first empty bcz counter starts from 0


        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
        cam.set(3, 640) # set video FrameWidht
        cam.set(4, 480) # set video FrameHeight

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        # flag = True

        while True:

            ret, img =cam.read() #read the frames using the above created object

            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale( 
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match 
                if (accuracy < 100):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    TakeExe()

                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    break
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("Thanks for using this program, have a good day.")
        cam.release()
        cv2.destroyAllWindows() 

        if "wake up" in Permission:
            TakeExe()